import json
import uuid
import os
from faker import Faker
from datetime import datetime

# Generate some sample data for a mortgage application
loan_ltvs = [60, 70, 80, 90, 100]
loan_terms = [20, 25, 30, 35, 40]
mortgage_brokers = [
    "Mortgages4U",
    "Buy Your Dream",
    "Shearer, Lee & Venison Mortgage Brokers"
]

fake = Faker("en_GB")

name = fake.name()
email = fake.email()
telephone = fake.phone_number()
address_house_number = str(fake.random_int(min=1, max=66))
address_postcode = fake.postcode()
age = fake.random_int(min=18, max=85)
annual_income = fake.random_int(min=15000, max=250000)
requested_loan_amount = fake.random_int(min=80000, max=1000000)
requested_loan_ltv = loan_ltvs[fake.random_int(min=0, max=4)]
requested_loan_with_fee = fake.random_int(min=0, max=1)
requested_loan_term = loan_terms[fake.random_int(min=0, max=4)]
requested_loan_fixed_period = fake.random_int(min=2, max=5)
credit_score = fake.random_int(min=500, max=1500)
employment_status = "employed"
property_address_house_number = str(fake.random_int(min=1, max=66))
property_address_postcode = fake.postcode()
mortgage_broker = mortgage_brokers[fake.random_int(min=0, max=2)]
application_type = "mortgage"
application_date = str(datetime.today())
application_id = str(uuid.uuid4())


# Create a dictionary to store the data
mortgage_application_data = json.dumps({
    "name": name,
    "email": email,
    "telephone": telephone,
    "address_house_number": address_house_number,
    "address_postcode": address_postcode,
    "age": age,
    "annual_income": annual_income,
    "requested_loan_amount": requested_loan_amount,
    "requested_loan_ltv": requested_loan_ltv,
    "requested_loan_with_fee": requested_loan_with_fee,
    "requested_loan_term": requested_loan_term,
    "requested_loan_fixed_period": requested_loan_fixed_period,
    "credit_score": credit_score,
    "employment_status": employment_status,
    "property_address_house_number": property_address_house_number,
    "property_address_postcode": property_address_postcode,
    "mortgage_broker": mortgage_broker,
    "application_type": application_type,
    "application_date": application_date,
    "application_id": application_id
})

# Create a filename using the application_id and folder name
filename = "mortgage_application_" + application_id + ".json"
folder = "mortgage_applications"
file_path = os.path.join(folder, filename)

# Save the data as a JSON file with the unique filename and in the folder
with open(file_path, "w") as outfile:
    json.dump(mortgage_application_data, outfile)