import os
#import gcp_auth
from google.cloud import scheduler_v1

client = scheduler_v1.CloudSchedulerClient()

project_id = 'atom-demo-378221'
location = 'us-central1'

parent = client.common_location_path(project_id, location)

#parent = client.location_path('atom-demo-378221', 'us-central1')

# Build the job specification
job = {
    'name': client.job_path('atom-demo-378221', 'us-central1', 'simulate-new-mortgage-application-job'),
    'schedule': '*/30 * * * *', # Run every 30 minutes
    'time_zone': 'America/Los_Angeles',
    'http_target': {
        'uri': 'https://us-central1-atom-demo-378221.cloudfunctions.net/simulate_new_mortgage_application',
        'http_method': 'POST',
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': b'' # No body required
    }
}

response = client.create_job(parent='projects/atom-demo-378221/locations/us-central1', job=job)

print("Created job: {}".format(response.name))
