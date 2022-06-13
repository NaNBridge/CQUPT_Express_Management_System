import pymysql
import csv


# 打开数据库连接
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="liang1925tt",
                       database="cquptems_db",
                       port=3306,
                       charset="utf8")
# 测试连接
if conn:
    print("连接成功")
# 获取游标
cur = conn.cursor()

"""打开csv文件"""
filename = "F:\\study\\DBwork\\CQUPT_Express_Management_System\\CQUPTEMS_QT\\TKINTER\\data_set\\user_information.csv"
filename_2 = "F:\\study\\DBwork\\CQUPT_Express_Management_System\\MySQL_query\\user_password.csv"
f = open(filename_2, "r", encoding="utf-8")

# 设置csv文件读取器
csv_reader = csv.reader(f)
# 读取首行
header_row = next(csv_reader)
print(header_row)
# 读取csv文件中的信息,并将这些信息插入到users表中
for row in csv_reader:
    nama, student_id, phone_number, pickup_code,password = str(
        row[0]), str(row[1]), str(row[2]), str(row[3]),str(row[4])
    # 打印相关信息
    # print(row)
    # 定义SQL语句
    mysql_sentence = f"""
    insert
    into users(user_name, user_student_ID, user_phone_number, unique_pickup_code,user_password)
    values ('{nama}','{student_id}','{phone_number}','{pickup_code}','{password}');
    """
    # string=f"""{type(nama)},{student_id},{phone_number},{pickup_code}"""
    # print(string)
    # 执行SQL语句
    cur.execute(mysql_sentence)
    # 提交执行结果
    conn.commit()
    pass

message = conn.close()
