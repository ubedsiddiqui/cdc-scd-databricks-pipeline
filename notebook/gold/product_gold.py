import dlt 
from pyspark.sql.functions import *

dlt.create_streaming_table(
    name = 'product_stream'
)

dlt.create_auto_cdc_flow(name='product_scd',
                         source='product_view',
                         target= 'product_stream',
                         keys= ['product_id'],
                         sequence_by= col('last_updated')
                         )