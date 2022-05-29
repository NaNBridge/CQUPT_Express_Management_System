import pymysql
#打开数据库连接

conn=pymysql.connect(host="localhost",user="root",password="200149",database="cquptems_db",port=3306,charset="utf8")
#测试连接
if conn:
    print("连接成功")
#获取游标
cur = conn.cursor()
#利用游标来执行mysql语句
"""向Packages表中插入数据"""

#创建station表
#cur.execute("")
message=conn.close()
