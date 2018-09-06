from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession, HiveContext

SparkContext.setSystemProperty("hive.metastore.uris", "thrift://hadoop-m:9083")
spark = (
    SparkSession.builder.appName('example-pyspark-read-and-write-from-hive')
    .enableHiveSupport().getOrCreate())
spark.sql('SET hive.exec.dynamic.partition=true')
spark.sql('SET hive.exec.dynamic.partition.mode=nonstrict')
spark.sql('SET hive.exec.max.dynamic.partitions.pernode=1000')
spark.sql('SET hive.enforce.bucketing=true')

spark.sql(
    'LOAD DATA LOCAL INPATH \'/home/kolisachint/IMDB/movie_ratings.csv\' OVERWRITE INTO TABLE IMDBPreStg.MovieData'
)

spark.sql('''
INSERT OVERWRITE TABLE IMDBStg.MovieData PARTITION(Yr)
SELECT  
MovieNm,IMDBScr,METAScr,Votes,
to_date(current_timestamp()),
to_date(current_timestamp()),
current_timestamp(),
current_timestamp(),
Yr  
FROM IMDBPreStg.MovieData
''')

spark.sql('''
INSERT OVERWRITE TABLE IMDB.MovieData PARTITION(Yr)
SELECT MovieNm,IMDBScr,METAScr,Votes,Eff_STRT_DTE,Eff_END_DTE,CREATE_TMSTMP,UPD_TMSTMP,YR
FROM IMDBStg.MovieData
''')

df_load = spark.sql('select * from IMDB.MovieData')

df_load.show()
