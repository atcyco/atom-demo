# atom-demo

Demo of a possible ETL and Data Warhouse design for Atom bank.  Initially focussing on the mortgage products.

Should include:

* automated process for simulating now mortgage applications and storing them as JSON
* Data model design including customers, applications, products and brokers
* loading of new applications in BigQuery
* automated process for simulating repayments, including late and nonepayment
* updating of slowly changing dimensions like interest rates
