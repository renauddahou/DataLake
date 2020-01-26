from pyspark.sql import *
import pyspark
from pyspark.context import SparkContext
import boto3
spark = SparkSession.builder.appName("Word Count").getOrCreate()
object = boto3.client('s3')
s3 = boto3.resource('s3')
file = 0
for i in object.list_objects(Bucket='structproject')['Contents']:
    file+=1
    print(i['Key'])
print(file)
hostname='rds-inc.cdlqydqaoedi.us-east-1.rds.amazonaws.com'
jdbcPort=3306
dbname='task'
username='root'
password='password'
jdbc_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}".format(hostname,jdbcPort, dbname,username,password)
if file==1:
    query = 'select * from groupmem'
    df1 = spark.read.format('jdbc').options(driver = 'com.mysql.jdbc.Driver',url=jdbc_url, query=query).load()
    df1.coalesce(1).write.mode("append").option("header","true").format("csv").save("s3a://structproject/")
else:
    query = 'select * from groupmem where substr(log_date,1,10) = date(curdate()-1)'
    df1 = spark.read.format('jdbc').options(driver = 'com.mysql.jdbc.Driver',url=jdbc_url, query=query).load()
    df1.coalesce(1).write.mode("append").option("header","true").format("csv").save("s3a://structproject/")
df1.show()
