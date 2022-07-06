import time
import threading
from datetime import datetime

mutex = threading.Lock()
sp = threading.Semaphore(5)

# y = 5

def accessResource(x):
  # global y
  file = open("alpha.txt",'a+')
  # mutex.acquire()
  sp.acquire()
  print("Access requested")
  print(" ")
  # y+=1
  # print("Y: "+str(y))
  current_time = datetime.now()
  file.write(f"Current Time is {current_time.strftime('%H:%M:%S')} \n")
  file.write(f"Wrote using threadId: {threading.current_thread().ident} \n")
  file.write("Written using multithreading \n \n")
  time.sleep(2)
  file.close()
  sp.release()
  # mutex.release()

for x in range(10):
  t = threading.Thread(target=accessResource, args=(x,))
  t.start()
