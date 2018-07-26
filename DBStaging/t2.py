
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext,SparkSession, HiveContext
from pyspark.sql.types import *


SparkContext.setSystemProperty("hive.metastore.uris", "thrift://hadoop-m:9083")
sparkSession = (SparkSession
                .builder
                .appName('example-pyspark-read-and-write-from-hive')
                                .config("hive.metastore.uris", "thrift://hadoop-m:9083")
                                .enableHiveSupport()
                .getOrCreate())

sparkSession.sql('select * from IMDBPreStg.MovieData')
