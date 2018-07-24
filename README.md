
# IMDBDataProcessing
IMDB Data processing using Bigdata technologies. Placeholder to explore and learn new technologies

#Commands
	  gcloud dataproc jobs submit pyspark IMDB2018FetchData.py --cluster=hadoop
	  gcloud dataproc jobs submit hive --cluster=hadoop --file=TblMovieLoad.hive 
