from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from generate_data.config.ConfigStore import *
from generate_data.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(explode(sequence(lit(0), lit(100))).alias("row_id"), lit("abc").alias("field_a"))
