We will be using a preview command to create an autoscaling capable cluster, so we first need to add the preview commands to our az CLI:

az extension add --name aks-preview

Until the preview commands become standard, if you need a stable cluster, do not enable the preview parameter (or the vmss and autoscaler parameters below).

Finally we can create an AKS cluster (you will need your <appId> and <password> from the previous section):

cat ../sp.txt

Get versions
az aks get-versions -l brazilsouth --output table

az aks create \
    --resource-group az-sandbox \
    --name AksArch \
    --node-count 1 \
    --max-pods 30 \
    --kubernetes-version 1.15.7 \
    --generate-ssh-keys \
    --enable-cluster-autoscaler \
    --min-count 1 \
    --max-count 3 \
    --service-principal 6003dca4-eeee-4120-bc0d-18a08973b465 --client-secret 14adffda-0537-4471-871c-c36b8e0429d1

This will create a cluster (which may take 5-10 minutes). Once done, we can connect to the kubernetes environment via the Kubernetes CLI. If you are using the Azure Cloud Shell, the kubernetes client (kubectl) is already installed. You can also install locally if you haven't previously installed a version of kubectl:
az aks install-cli

az aks get-credentials --resource-group az-sandbox --name AksArch --admin

The resource-group and name were set during the creation process, and you should use those if different from what we're using here.

Check your connection and that the kubernetes cli is working with:
kubectl get nodes

If you have issues with connecting, one thing you can check is the version of your kubernetes client:
kubectl version

This will tell you both the local client, and the configured kubernetes service version, make sure the client is at least the same if not newer than the server.
