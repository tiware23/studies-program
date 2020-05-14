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
#  "appId": "4631b7ff-bd2a-4269-80b6-218fc694c0a7",
#  "password": "5c242d31-3617-4198-b663-f40f4f4a1f05"
#}
# Create ACR
az acr create \
--resource-group $RG \
--name akstiware \
--sku Basic \
--admin-enabled true

#Add permission for our SP to read ACR images
az role assigment create --assignee "<appid_sp>" --role acrpull --scope <id acr>

# Create a Dockerfile:
echo "FROM hello-world" > Dockerfile

# Use ACR tasks to build the image to new ACR
az acr build --image=/path/image:v1 --registry akstiware --file Dockerfile .
az acr build --registry aksdeepdive --image node:v1 .

# Run the image
az acr run --registry akstiware --cmd '$Registry/path/image:v1' /dev/null

# Delete resource group and everything in it:
az group delete --name myaks-rg