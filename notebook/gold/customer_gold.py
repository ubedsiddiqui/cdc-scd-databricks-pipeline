import dlt 
from pyspark.sql.functions import *

dlt.create_streaming_table(
    name = 'customer_stream'
)

dlt.create_auto_cdc_flow(name='customer_scd',
                         source='customer_view',
                         target= 'customer_stream',
                         keys= ['customer_id'],
                         sequence_by= 'last_updated'
                         )