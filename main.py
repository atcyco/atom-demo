import json
import uuid
from google.cloud import storage

def simulate_new_mortgage_application(request):
    # Generate some sample data for a mortgage application
    name = "John Doe"
    age = 35
    annual_income = 80000
    requested_loan_amount = 300000
    credit_score = 700
    employment_status = "employed"
    property_address = "123 Main St, Anytown USA"
    application_type = "mortgage"
    application_id = str(uuid.uuid4())

    # Create a dictionary to store the data
    mortgage_application_data = json.dumps({
        "name": name,
        "age": age,
        "annual_income": annual_income,
        "requested_loan_amount": requested_loan_amount,
        "credit_score": credit_score,
        "employment_status": employment_status,
        "property_address": property_address,
        "application_type": application_type,
        "application_id": application_id
    })

    # create a Cloud Storage client
    client = storage.Client()

    # get the Cloud Storage bucket
    bucket = client.get_bucket('atom-demo-mortgage-applications')

    # create a new Cloud Storage blob (file)
    filename = "mortgage_application_" + application_id + ".json"
    blob = bucket.blob(filename)

    # upload the JSON data to the Cloud Storage blob
    blob.upload_from_string(mortgage_application_data)
