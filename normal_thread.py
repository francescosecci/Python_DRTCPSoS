

from threading import Thread
import time
 
class MyThread (Thread):
   def __init__(self, nome, durata):
      Thread.__init__(self)
      self.nome = nome
      self.durata = durata
   def run(self):
      print ("Thread '" + self.name + "' avviato con un timer di "+ str(self.durata) +" sec.\n")
      time.sleep(self.durata)
      print ("Thread '" + self.name + "' terminato.\n")

from random import randint

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