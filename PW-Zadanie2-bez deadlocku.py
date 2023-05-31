import threading
import time

blokadaA = threading.Lock()
blokadaB = threading.Lock()

def zadanie1():
    blokadaA.acquire()
    print("zadanie 1, blokuje blokadęA ")
    blokadaB.acquire()
    print("zadanie 1, blokuje blokadęA")
    blokadaA.release()
    blokadaB.release()

def zadanie2():
    blokadaB.acquire()
    print("Zadanie 2, blokuje blokadęB")
    blokadaA.acquire()
    print("Zadanie 2, blokuje blokadęA")
    blokadaB.release()
    blokadaA.release()

w1 = threading.Thread(target=zadanie1)
w2 = threading.Thread(target=zadanie2)

w1.start()
w2.start()
w1.join()
w2.join()

print("Program zakończył działanie")