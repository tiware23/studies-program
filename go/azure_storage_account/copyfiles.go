package main

import (
	"context"
	"fmt"
	"log"
	"net/url"
	"os"
	"path"

	"github.com/Azure/azure-storage-blob-go/azblob"
)

const containerName = "static"

func setAccountVars() (accountName string, accountKey string) {
	accountName, accountKey = os.Getenv("AZURE_STORAGE_ACCOUNT"), os.Getenv("AZURE_STORAGE_ACCESS_KEY")

	if len(accountName) == 0 || len(accountKey) == 0 {
		log.Fatal("Either the AZURE_STORAGE_ACCOUNT or AZURE_STORAGE_ACCESS_KEY environment variable is not set")
	}
	return accountName, accountKey
}

func getCrendials(blobStorage, accountKey string) *azblob.SharedKeyCredential {
	credential, err := azblob.NewSharedKeyCredential(blobStorage, accountKey)
	if err != nil {
		log.Fatal("Invalid credentials with error: " + err.Error())
	}

	return credential
}

func parseContainerURL(credential *azblob.SharedKeyCredential, blobStorage string, containerName string) azblob.ContainerURL {
	p := azblob.NewPipeline(credential, azblob.PipelineOptions{})

	URL, _ := url.Parse(
		fmt.Sprintf("https://%s.blob.core.windows.net/%s", blobStorage, containerName))

	containerURL := azblob.NewContainerURL(*URL, p)
	return containerURL
}

func uploadToBlob(f string, contentType string, blobURL azblob.BlockBlobURL) {
	file, err := os.Open(f)

	ctx := context.Background()

	if err != nil {
		log.Fatal(err)
	}

	urlProperties := azblob.BlobHTTPHeaders{ContentType: contentType}

	fmt.Println("Uploading the file", f)
	_, err = azblob.UploadFileToBlockBlob(ctx, file, blobURL, azblob.UploadToBlockBlobOptions{
		BlockSize:       4 * 1024 * 1024,
		BlobHTTPHeaders: urlProperties,
		Parallelism:     16})

	if err != nil {
		log.Fatal(err)
	}

	file.Close()
}

func main() {
	fileName := os.Args[1:]
	blobStorage, accountKey := setAccountVars()
	credential := getCrendials(blobStorage, accountKey)
	containerURL := parseContainerURL(credential, blobStorage, containerName)

	for _, f := range fileName {
		blobURL := containerURL.NewBlockBlobURL(f)
		fileExtension := path.Ext(f)

		if fileExtension == ".json" {
			uploadToBlob(f, "application/json", blobURL)
		} else {
			uploadToBlob(f, "text/plain", blobURL)
		}
	}
}
