"""模拟单个用户的用户名，工作，地址，文本
"""
from faker import Faker

fa = Faker("zh_CN")
print('name:', fa.name())
print('job:', fa.job())
print('address:', fa.address())
print('text:', fa.text())

