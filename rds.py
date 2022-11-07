import pymysql
import os
# Database_endpoint = os.environ['ENDPOINT']
# Username = os.environ['USER']
# Password = os.environ['PASS']
Database_endpoint = 'database-1.cluster-cigdubc02cgf.ap-northeast-1.rds.amazonaws.com'
Username = 'admin'
Password = 'koke1505'
try:
    print("Connecting to "+Database_endpoint)
    db = pymysql.connect(Database_endpoint,Username,Password)
    print ("Connection successful to "+Database_endpoint)
except Exception as e:
    print ("Connection unsuccessful due to "+str(e))