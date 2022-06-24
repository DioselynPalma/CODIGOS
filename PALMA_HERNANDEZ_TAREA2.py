Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import queue
import random
import sys
 
queue_time = queue.Queue()
 
print("Guardando elementos en la cola...")
for i in range (5):
    random_time = random.randint(1, 100)
    queue_time.put(random_time)
    print("Numero %d agregado a la cola" % random_time)
 
print("Leyendo elementos de la cola...")
while True:
    if queue_time.empty() == False:
        time_read = queue_time.get()
        print("Numero %d leido de la cola" % time_read)
    else:
        print("La cola esta vacia!!")
        break

SyntaxError: multiple statements found while compiling a single statement
