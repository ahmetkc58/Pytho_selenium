import matematik
import random
from selenium import webdriver
sayi1=10
sayi2=5

a=random.randint(10,20)
print(a)
print(matematik.toplama(sayi1,sayi2))

print(matematik.bölme(sayi1,sayi2))


chromDriver =webdriver.Chrome()