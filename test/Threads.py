import os,time,threading
print ('Process (%s) start...' %os.getpid())
balence=0
lock=threading.Lock()
def change(n):
    global balence
    balence = balence+n
    balence = balence-n
def run(n):
    for i in range(10000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()
t1=threading.Thread(target=run,args=(5,))
t2=threading.Thread(target=run,args=(6,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balence)
if __name__=='__main__':
    print(' ')