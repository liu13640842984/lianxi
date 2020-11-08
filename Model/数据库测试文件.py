#coding=UTF-8
from Model.HaHa import *
haha = HaHa()

for i in haha.query(HaHa):
    print(i.id)