from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from generate_data.config.ConfigStore import *
from generate_data.udfs.UDFs import *
from prophecy.utils import *
from generate_data.graph import *

def pipeline(spark: SparkSession) -> None:
    df_SQLStatement_0 = SQLStatement_0(spark)
    df_Reformat_1 = Reformat_1(spark, df_SQLStatement_0)
    generated_data(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/generate_data")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/generate_data", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/generate_data")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
