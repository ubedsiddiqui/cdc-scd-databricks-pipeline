import dlt 
from pyspark.sql.functions import * 

@dlt.view(
    name= 'product_view',
    comment='transformed product_data'
)

def product_view():
    df = spark.readStream.table('jumia_cat.jumia_pipline.product')
    return df
   


dlt.create_streaming_table(name='product_tranform',
                           comment= 'slowely changing dimension part 2'

                               )


dlt.apply_changes(
    source='product_view',
    target='product_tranform',
    keys=['product_id'],
    sequence_by= col('last_updated'),
    except_column_list=[],
    stored_as_scd_type=2
)