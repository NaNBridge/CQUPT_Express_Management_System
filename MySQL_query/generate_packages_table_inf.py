import pymysql
import csv
import random
import string
"""利用Faker库生成虚假数据"""
from faker import Faker
#创建对象，默认生成的数据为为英文，使用zh_CN指定为中文
fake = Faker('zh_CN')

#快递公司列表,方便之后生成数据 
express_companies_list=['顺丰','中通','圆通','润通','百世','极兔快递','京东','申通','韵达','中国邮政']

#打开存储电话号码的文件
filename="D:/Project/CQUPT_Express_Management_System/MySQL_query/user_phone_number.csv"
f=open(filename, "r")

#定义一个csv读取器,读取电话号码
csv_reader=csv.reader(f)
#读取首行
header_row=next(csv_reader)
#定义一个列表来存储从csv文件中读取的电话号码
phone_numbers_list=list()
for row in csv_reader:
    row=str(row[0])
    phone_numbers_list.append(row)
    #print(row)
    pass
print(phone_numbers_list)
#定义一个随机生成快递ID的函数,快递ID长度为50
def generate_random_str(randomlength=50):    
    '''    
    string.digits = 0123456789    
    string.ascii_letters = 26个小写,26个大写    
    '''    
    str_list = random.sample(string.digits + string.ascii_letters,randomlength)    				
    random_str = ''.join(str_list)    
    return random_str
# print(generate_random_str())

# 打开数据库连接
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="200149",
                       database="cquptems_db",
                       port=3306,
                       charset="utf8")
# 测试连接
if conn:
    print("连接成功")
# 获取游标
cur = conn.cursor()


#print(fake_address_info,type(fake_address_info))#随机生成地址
"""生成1000个快递信息,并将其插入packages表中"""
for i in range(1000):
    #生成快递ID
    package_id=generate_random_str()
    #生成随机地址
    fake_address_info=(fake.address()).split(' ')[0]
    #随机在电话号码列表中挑选一个电话号码
    phone_number=random.choice(phone_numbers_list)
    #随机在快递公司列表中选择一个快递公司
    express_company=random.choice(express_companies_list)
    """开始插入数据"""
    #定义SQL语句
    sql_sentence=f"""
    insert
    into packages(package_ID, package_owner_phone_number, shipping_address, express_company)
    values ('{package_id}',
    '{phone_number}',
    '{fake_address_info}',
    '{express_company}');
    """
    #执行SQL语句
    cur.execute(sql_sentence)
    #提交执行结果
    conn.commit()
    
    
    pass



f.close()
message = conn.close()