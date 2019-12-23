# pip install google-cloud-storage
from google.cloud import storage


def upload_to_bucket(blob_name, path_to_file, bucket_name):
    """ Upload data to a bucket"""

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'uwcc-admin.json')

    #print(buckets = list(storage_client.list_buckets())

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)

    #returns a public url
    return blob.public_url

public_url = upload_to_bucket(blob_name='wrf/4.0/d0/18/2019-12-18/output/mwrf/T5/test_bucket_upload.nc',
                              path_to_file='test_bucket_upload.nc',
                              bucket_name='wrf_nfs')

print(public_url)
