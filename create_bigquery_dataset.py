import gcp_auth
from google.cloud import bigquery

client = bigquery.Client()

# Create the dataset for the mortgage data
dataset_id = 'atom_demo_mortgage_data_test'
dataset = bigquery.Dataset(client.dataset(dataset_id))
dataset.location = 'US'
client.create_dataset(dataset)

# Define the tables for the mortgage data
tables = [
    {
        'name': 'MortgageFact',
        'schema': [
            bigquery.SchemaField('ApplicationID', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('MortgageID', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('CustomerID', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('ProductID', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('ApplicationDate', 'DATE', mode='REQUIRED'),
            bigquery.SchemaField('ApprovalDate', 'DATE'),
            bigquery.SchemaField('MaturityDate', 'DATE', mode='REQUIRED'),
            bigquery.SchemaField('LoanAmount', 'FLOAT', mode='REQUIRED'),
            bigquery.SchemaField('InterestRate', 'FLOAT', mode='REQUIRED'),
            bigquery.SchemaField('PaymentAmount', 'FLOAT', mode='REQUIRED'),
            bigquery.SchemaField('PaymentDate', 'DATE', mode='REQUIRED')
        ],
        'partitioning': bigquery.TimePartitioning(
            type_=bigquery.TimePartitioningType.DAY,
            field='ApplicationDate'
        )
    },
    {
        'name': 'CustomerDim',
        'schema': [
            bigquery.SchemaField('CustomerID', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('Name', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('Address', 'STRING'),
            bigquery.SchemaField('City', 'STRING'),
            bigquery.SchemaField('State', 'STRING'),
            bigquery.SchemaField('ZipCode', 'STRING')
        ]
    },
    {
        'name': 'ProductDim',
        'schema': [
            bigquery.SchemaField('ProductID', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('ProductName', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('ProductType', 'STRING'),
            bigquery.SchemaField('LTV', 'FLOAT', mode='REQUIRED'),
            bigquery.SchemaField('ProductFee', 'FLOAT', mode='REQUIRED'),
            bigquery.SchemaField('FixedRateDuration', 'INTEGER', mode='REQUIRED')
        ]
    },
    {
        'name': 'TimeDim',
        'schema': [
            bigquery.SchemaField('Date', 'DATE', mode='REQUIRED'),
            bigquery.SchemaField('Day', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('Month', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('Year', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('DayOfWeek', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('Quarter', 'INTEGER', mode='REQUIRED'),
            bigquery.SchemaField('IsWeekend', 'BOOLEAN', mode='REQUIRED')
        ]
    }
]

# Create the tables in the mortgage data dataset
for table in tables:
    table_ref = dataset.table(table['name'])
    bigquery_table = bigquery.Table(table_ref, schema=table['schema'])
    if 'partitioning' in table:
        bigquery_table.time_partitioning = table['partitioning']
    client.create_table(bigquery_table)
