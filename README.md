# atom-demo

Demo of a possible ETL and Data Warhouse design for Atom bank.  Initially focussing on the mortgage products.

Should include:

* automated process for simulating now mortgage applications and storing them as JSON
* Data model design including customers, applications, products and brokers
* loading of new applications in BigQuery
* automated process for simulating repayments, including late and nonepayment
* updating of slowly changing dimensions like interest rates

Does now have a Cloud Function called simulate_new_mortgage_application that will use the Faker library to simulate new mortgage applications and save them in Cloud Storage as JSON files.  Currently have a Cloud Scheduler job that runs every 30 minutes to generate a new JSON file.

Cloud Storage Bucket, Cloud Function and Cloud Scheduler job created using API.

Have an initial / placeholder schema design in BigQuery that is also created using the API but I will be looking to improve the data model once I get Dataflow working.

Need to do some refactoring work to extract stuff like project name into variables as well as figuring out how to call deploy code from a file.