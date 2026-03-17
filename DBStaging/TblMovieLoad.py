from pyspark.sql import SparkSession

SparkSession._jvm.System.setProperty("hive.metastore.uris", "thrift://hadoop-m:9083")
spark = (
    SparkSession.builder
    .appName('imdb-data-load')
    .enableHiveSupport()
    .getOrCreate()
)

spark.sql('SET hive.exec.dynamic.partition=true')
spark.sql('SET hive.exec.dynamic.partition.mode=nonstrict')
spark.sql('SET hive.exec.max.dynamic.partitions.pernode=1000')
spark.sql('SET hive.enforce.bucketing=true')

spark.sql(
    "LOAD DATA LOCAL INPATH '/home/kolisachint/IMDB/movie_ratings.csv' "
    "OVERWRITE INTO TABLE IMDBPreStg.MovieData"
)

spark.sql("""
INSERT OVERWRITE TABLE IMDBStg.MovieData PARTITION(Yr)
SELECT
    MovieNm,
    IMDBScr,
    METAScr,
    Votes,
    to_date(current_timestamp())    AS Eff_STRT_DTE,
    CAST('9999-12-31' AS date)      AS Eff_END_DTE,
    current_timestamp()             AS CREATE_TMSTMP,
    current_timestamp()             AS UPD_TMSTMP,
    Yr
FROM IMDBPreStg.MovieData
""")

spark.sql("""
INSERT OVERWRITE TABLE IMDB.MovieData PARTITION(Yr)
SELECT
    MovieNm, IMDBScr, METAScr, Votes,
    Eff_STRT_DTE, Eff_END_DTE,
    CREATE_TMSTMP, UPD_TMSTMP,
    Yr
FROM IMDBStg.MovieData
""")

df_load = spark.sql('SELECT * FROM IMDB.MovieData')
df_load.show()
