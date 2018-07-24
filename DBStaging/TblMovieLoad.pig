CREATE TABLE IMDBMovieData (
SerNo string,
MovieNm string,
Yr string,
IMDBScr string,
METAScr string,
Votes string
) ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS TEXTFILE
LOCATION '../Resources/Output/movie_ratings.json;
