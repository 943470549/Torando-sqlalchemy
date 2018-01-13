# -*- coding: utf-8 -*-
import gc
import os,json
fpath = r'D:\log\22001400255343328\test.txt'
def openfile(path):
    with open(path, 'r') as f:
        for line in f.readlines():
            print (line)
            gc.collect()
    with open(path, 'a') as fw:
        fw.write('sss')
def dump_object():
    with open(fpath, 'wb') as f:
        d=dict(name='1',age=2)
        json.dump(d,f)
def get_object():
    with open(fpath, 'rb') as f:
        d=json.load(f)
        print d
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
s = Student('aa',1)
print(json.dumps(s,default=lambda obj:obj.__dict__))


if __name__=='__main__':
#   openfile(fpath)
#   print (os.path.abspath('.'))
#    os.rename(fpath, 'a.py')
#    dump_object()
#    get_object()
    print(' ')