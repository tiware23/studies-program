#!/bin/bash
RG=akstiware
LOCATION=eastus

# Resource Group
az group create \
--name $RG \
--location $LOCATION

# Service Principal
az ad sp create-for-rbac --skip-assignment
# Copy the app ID and password from the output:
# {
#   "appId": "5e26bb2c-ba35-45c6-9259-409c0b31937e",
#   
#   
#   "password": "",
#   
# }
# Create ACR
az acr create \
--resource-group $RG \
--name akstiware \
--sku Basic \
--admin-enabled true

#Add permission for our SP to read ACR images
az role assigment create --assignee "<appid_sp" --role acrpull --scope <id acr

# Create a Dockerfile:
echo "FROM hello-world"  Dockerfile

# Use ACR tasks to build the image to new ACR
az acr build --image=/path/image:v1 --registry akstiware --file Dockerfile .
az acr build --registry aksdeepdive --image node:v1 .

# Run the image
az acr run --registry akstiware --cmd '$Registry/path/image:v1' /dev/null

# Delete resource group and everything in it:
az group delete --name myaks-rg

#########################################

# Create AKS cluster:
az aks create \
 --resource-group akstiware \
 --name myAKStiware \
 --node-count 1 \
 --enable-addons monitoring \
 --generate-ssh-keys \
 --enable-rbac \
 --service-principal "5e26bb2c-ba35-45c6-9259-409c0b31937e" \
 --client-secret ""

 # Get Credentials
 az aks get-credentials --resource-group <name> --name <aks-name>

# Create a deployment
kubectl run nodeapp --image=akstiwarecr.azurecr.io/node:v1 --replicas=1 --port=8080

# Expose deployment
kubectl expose deploy nodeapp --port=80 --target-port=8080 --dry-run -o yaml > svc.yaml
