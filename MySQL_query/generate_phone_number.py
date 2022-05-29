'''
中国电信号段：133，153， 180，181，189，173， 177，149
中国联通号段：130，131，132，155，156，185，186，145，176，185
中国移动号段：134，135，136，137，138，139，150，151，152，158，159，182，183，184，147，178
11位
第一位 ：1
第二位：3，4，5，7，8
第三位：根据第二位来确定
    3 + 【0-9】
    4 + 【5，7，9】
    5 + 【0-9】 ！4
    7 + 【0-9】！ 4and9
    8 + 【0-9】
后8位： 随机生成8个数字
'''
import random
# creat_phone()
# 生成电话号
def creat_phone():
    # 第二位
    second = [3,4,5,7,8][random.randint(0,4)]
    
    # 第三位的值根据第二位来确定
    third = {
        3:random.randint(0,9),
        4:[5,7,9][random.randint(0,2)],
        5:[i for i in range(10) if i!=4][random.randint(0,8)], 
        7:[i for i in range(10) if i not in [4,9]][random.randint(0,7)],
        8:random.randint(0,9)
    }[second]
    # 后8位随机抽取
    suffix = ''
    for x in range(8):
        suffix = suffix + str(random.randint(0,9))
    # 拼接
    return "1{}{}{}".format(second,third,suffix)
# 调用
# print(creat_phone())
#num = input('请输入生成的数量')
num=int(10)
for index in range(0,int(num)):
    print(creat_phone())
