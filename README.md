
# IMDBDataProcessing
IMDB Data processing using Bigdata technologies. Placeholder to explore and learn new technologies

#Commands
	  
	gcloud dataproc jobs submit hive --cluster=hadoop --file=TblMovieDDL.hive
	gcloud dataproc jobs submit hive --cluster=hadoop --file=TblMovieLoad.hive
	gcloud dataproc jobs submit pyspark TblMovieLoad.py --cluster=hadoop
