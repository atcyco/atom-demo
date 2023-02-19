import os

# Set the path to your key file
key_path = "gcp_key/atom-demo-378221-0b3966105752.json"

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Get the value of the GOOGLE_APPLICATION_CREDENTIALS environment variable
key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Print the value of the environment variable
print("Key file path:", key_path)