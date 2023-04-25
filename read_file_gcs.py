from google.cloud import storage

def read_file_from_gcs(bucket_name, blob_name):
    # Create a client
    storage_client = storage.Client()

    # Access the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Access the blob
    blob = bucket.blob(blob_name)

    # Read the content of the file
    content = blob.download_as_text()

    return content

if __name__ == "__main__":
    # Replace these with your bucket and blob name
    my_bucket_name = "bucket"
    my_blob_name = "path/to/file.txt"

    file_content = read_file_from_gcs(my_bucket_name, my_blob_name)
    print(file_content)
