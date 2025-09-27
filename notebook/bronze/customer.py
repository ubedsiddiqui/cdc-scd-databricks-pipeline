import dlt 

# ingestion customer data
rules = {"rules": "customer_id IS NOT NULL"}

@dlt.table(
    name = 'jumia_pipline.customer',
    comment='customer data ingest',
)
@dlt.expect_all_or_drop(rules)

def customer():
    return spark.readStream.table('jumia_cat.jumia_schema.customers')


