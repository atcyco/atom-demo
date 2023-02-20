import gcp_auth
from google.cloud import storage

# Create a client object
client = storage.Client()

# Create a new bucket with a unique name
bucket_name = 'atom-demo-mortgage-applications'
bucket = client.create_bucket(bucket_name)
