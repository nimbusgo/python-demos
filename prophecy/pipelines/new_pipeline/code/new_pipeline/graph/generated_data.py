from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from new_pipeline.config.ConfigStore import *
from new_pipeline.udfs.UDFs import *

def generated_data(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("/tmp/nimbus/generated_data")
