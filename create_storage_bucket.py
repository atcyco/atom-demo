import gcp_auth
from google.cloud import storage

# Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable
# to the path of your service account key file
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_key/atom-demo-378221-0b3966105752.json'

# Create a client object
client = storage.Client()

# Create a new bucket with a unique name
bucket_name = 'my-test-bucket-with-python'
bucket = client.create_bucket(bucket_name)
