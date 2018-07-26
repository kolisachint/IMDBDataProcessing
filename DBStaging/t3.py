from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, HiveContext

SparkContext.setSystemProperty("hive.metastore.uris", "thrift://hadoop-m:9083")
sparkSession = (SparkSession
                .builder
                .appName('example-pyspark-read-and-write-from-hive')
                .enableHiveSupport()
                .getOrCreate())
df_load = sparkSession.sql('select * from IMDBPreStg.MovieData')
df_load.show()
