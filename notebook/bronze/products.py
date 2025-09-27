import dlt
# lets ingest product data
rules = {"rule1": "product_id IS NOT NULL"}

@dlt.table(
    name = 'product' 
)
@dlt.expect_all_or_drop(rules)

def product():
    return spark.readStream.table('jumia_cat.jumia_schema.products')


