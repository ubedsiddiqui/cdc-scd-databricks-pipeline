import dlt
from pyspark.sql.functions import *

@dlt.view(name='sales_view')

def sales_view():
    df = spark.readStream.table("jumia_cat.jumia_pipline.sales")
    df = df.withColumn("total", col("amount") * col("quantity"))
    return df

dlt.create_streaming_table(name = 'sales_transformed',comment='sales data transformation')

dlt.create_auto_cdc_flow(
    source='sales_view',
    target='sales_transformed',
    keys=['sales_id'],
    sequence_by='sale_timestamp',
    ignore_null_updates=False,
    name = 'sales_transformed_cdc_flow',
    except_column_list=[],
    stored_as_scd_type= 2,


)
