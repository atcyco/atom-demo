import json
import uuid
import os

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
mortgage_application_data = {
    "name": name,
    "age": age,
    "annual_income": annual_income,
    "requested_loan_amount": requested_loan_amount,
    "credit_score": credit_score,
    "employment_status": employment_status,
    "property_address": property_address,
    "application_type": application_type,
    "application_id": application_id
}

# Create a filename using the application_id and folder name
filename = "mortgage_application_" + application_id + ".json"
folder = "mortgage_applications"
file_path = os.path.join(folder, filename)

# Save the data as a JSON file with the unique filename and in the folder
with open(file_path, "w") as outfile:
    json.dump(mortgage_application_data, outfile)