"""模拟多个用户的用户名，工作，地址，文本

"""
from faker import Faker

for x in range(1,5):
    fa = Faker(locale="zh_CN")
    # print('name:', fa.name())
    # print('job:', fa.job())
    # print('身份证号:', fa.ssn())
    # print('address:', fa.address())
    # print('text:', fa.text())
    print('随机生成档案信息:', fa.profile())

