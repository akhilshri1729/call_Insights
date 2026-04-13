from azure.storage.blob import BlobServiceClient
from config import AZURE_BLOB_CONNECTION_STRING, CONTAINER_NAME

blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

def upload_file(file_path):
    blob_name = file_path.split("/")[-1]

    with open(file_path, "rb") as data:
        container_client.upload_blob(name=blob_name, data=data, overwrite=True)

    print(f"✅ Uploaded: {blob_name}")


def upload_text(text, path):
    container_client.upload_blob(name=path, data=text, overwrite=True)
    print(f"✅ Stored: {path}")
