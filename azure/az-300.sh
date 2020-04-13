#!/bin/bash
RG=$1
AZ=$(which az)
PUBIP_ID=$(az network public-ip list -g $RG --query "[0].id" |sed 's/\"//g')
VNET="vnet-lab"
LOCATION="eastus"


echo "Creating VNET: $VNET..."
$AZ network vnet create \
--resource-group ${RG} \
--name $VNET \
--address-prefixes 10.0.0.0/16 \
-l $LOCATION

sleep 1

echo "Creating SUBNET..."
$AZ network vnet subnet create -g $RG \
--vnet-name $VNET \
-n subnet1 \
--address-prefix 10.0.1.0/24

sleep 1

$AZ network nic create -g $RG \
--vnet-name $VNET \
--subnet subnet1 \
-n mynic1 \
-l $LOCATION

sleep 1

$AZ network public-ip create \
--name pub1 \
-g $RG \
-l eastus \
--sku basic \
-l $LOCATION

sleep 1

$AZ network nic ip-config create \
-g $RG \
--nic-name mynic1 \
--public-ip-address $PUBIP_ID \
--name ipconfig3 \

sleep 1 

$AZ network public-ip update \
-g ${RG} \
-n pub1 \
--allocation-method Static

echo "Creating SA Blob storage"
$AZ storage account create \
-n blobtiware \
-g ${RG} \
-l eastus \
--sku Standard_LRS \
--kind BlobStorage \
--access-tier Hot
