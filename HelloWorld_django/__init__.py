# import pymysql
#
# pymysql.install_as_MySQLdb()

import psycopg2

conn = psycopg2.connect(database='postgres',user='postgres',password='123456',host='localhost',port='5432')
print ("connect successfully")