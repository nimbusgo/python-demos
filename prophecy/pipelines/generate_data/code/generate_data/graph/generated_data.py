from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from generate_data.config.ConfigStore import *
from generate_data.udfs.UDFs import *

def generated_data(spark: SparkSession, in0: DataFrame):
    in0.write.format("parquet").mode("overwrite").save("/tmp/nimbus/generated_data")
