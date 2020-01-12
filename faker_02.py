"""模拟多个用户的用户名，工作，地址，文本
"""
from faker import Faker


for x in range(5):
    fa = Faker("zh_CN")
    print('name:', fa.name())
    print('job:', fa.job())
    print('address:', fa.address())
    # print('text:', fa.text())

