import dlt 

# create a empty table

# ingest data sales

rules = {"rule1": "sales_id IS NOT NULL"}

dlt.create_streaming_table(
    name = 'sales',
    comment = 'sales data ghana and nigeria',
    expect_all_or_drop= (rules)
)

# create a append flow all data from both region

@dlt.append_flow(target = 'sales')
def source1():
    return spark.readStream.table('jumia_cat.jumia_schema.ghana_sales')



@dlt.append_flow(target = 'sales')
def source2():
    return spark.readStream.table('jumia_cat.jumia_schema.nigeria_sales')


