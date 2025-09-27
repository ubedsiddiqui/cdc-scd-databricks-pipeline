import dlt 
from pyspark.sql.functions import *

dlt.create_streaming_table(
    name = 'sales_stream'
)

dlt.create_auto_cdc_flow(name='sales_cdc',
                         source='sales_view',
                         target= 'sales_stream',
                         keys= ['sales_id'],
                         sequence_by= col('sale_timestamp')
                         )