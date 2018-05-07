

import threading
import time
from random import randint
 
# Definizione del lock
threadLock = threading.Lock()
 
class MyThread (threading.Thread):
   def __init__(self, nome, durata):
      threading.Thread.__init__(self)
      self.nome = nome
      self.durata = durata
      
   def run(self):
      print ("Thread '" + self.name + "' avviato.\n")
      # Acquisizione del lock
      threadLock.acquire()
      print ("- Thread '" + self.name + "' acquisizione Lock per una durata di " + str(self.durata) + " sec.\n")
      time.sleep(self.durata)
      print ("Thread '" + self.name + "' terminato e rilascio Lock.\n")
      # Rilascio del lock
      threadLock.release()
 
# Creazione dei thread
thread1 = MyThread("Thread#1", randint(1,5))
thread2 = MyThread("Thread#2", randint(1,5))
thread3 = MyThread("Thread#3", randint(1,5))
 
# Avvio dei thread
thread1.start()
thread2.start()
thread3.start()
 
# Join
thread1.join()
thread2.join()
thread3.join()
 
# Fine dello script
print("Fine")

