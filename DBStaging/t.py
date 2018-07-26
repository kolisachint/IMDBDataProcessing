import org.apache.spark.sql.SparkSession
from pyspark.sql import SQLContext, HiveContext
from pyspark import SparkContext
from pyspark.sql.types import *



val spark = SparkSession
          .builder()
          .appName("interfacing spark sql to hive metastore without configuration file")
          .config("hive.metastore.uris", "thrift://hadoop-m:9083") 
          .enableHiveSupport() 
          .getOrCreate()

sc = SparkContext.getOrCreate()
hivContext = HiveContext(sc)
hivContext.setConf("hive.metastore.uris", "thrift://hadoop-m:9083");

print sc
hivContext.sql("select * from IMDBPreStg.MovieData").show
