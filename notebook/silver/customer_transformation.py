import dlt
from pyspark.sql.functions import *


@dlt.view(name="customer_view")
def customer_trans():
    df = spark.readStream.table('jumia_cat.jumia_pipline.customer')
    return df

    

dlt.create_streaming_table(name = 'customer_transformed',
                           comment='customer data transformation')
                        

dlt.create_auto_cdc_flow(
    source='customer_view',
    target='customer_transformed',
    keys=['customer_id'],
    sequence_by='last_updated',
    ignore_null_updates=False,
    name = 'customer_transformed_cdc_flow',
    except_column_list=[],
    stored_as_scd_type= 2,
    

)


