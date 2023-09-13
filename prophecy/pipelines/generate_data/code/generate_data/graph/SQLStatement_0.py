from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from generate_data.config.ConfigStore import *
from generate_data.udfs.UDFs import *

def SQLStatement_0(spark: SparkSession, ) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    df1 = spark.sql("select 1")

    return df1
