cd /home/hadoop/


mkdir images
hdfs dfs -get s3://scrapsh/code_scrap.py
hdfs dfs -get s3://scrapsh/image_scrap.py
hdfs dfs -get s3://scrapsh/rds_incremental.py

wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.45.tar.gz
tar -xvzf mysql-connector-java-5.1.45.tar.gz

sudo cp mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar /usr/lib/spark/jars/

python code_scrap.py
spark-submit rds_incremental.py
spark-submit image_scrap.py
