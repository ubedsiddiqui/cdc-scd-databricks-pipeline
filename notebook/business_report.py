import dlt
from pyspark.sql.functions import *

@dlt.table(name = 'business_insig')

def report():
    sale = spark.readStream.table('sales_stream').alias('s')
    customer = spark.readStream.table('customer_stream').alias('c')
    product = spark.readStream.table('product_stream').alias('p')

    join =(
        sale
           .join(customer, col('s.customer_id') == col('c.customer_id'),'inner')
           .join(product,col('s.product_id') == col('p.product_id'),'inner').select(
              col('s.sales_id'),
              col('s.customer_id'),
              col('s.product_id'),
              col('s.total'),
              col('s.sale_timestamp'),
              col('c.customer_name'),
              col('c.region'),
              col('p.product_name'),
              col('p.category'),
              col('p.price'),


               
           )
    )
    return join       




@dlt.table(name='sales_by_reg')
def sales_by_region():
    data = spark.readStream.table('business_insig')

    agg = (data
           .groupBy('region','category').agg(sum('total').alias('total_sal_region')))
    return agg