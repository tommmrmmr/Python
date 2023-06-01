import threading
import time


def increment_counter(repetitions, delay, thread_name, lock, finished_flag):
    counter = 0  # Inicjalizacja licznika dla każdego wątku

    for _ in range(repetitions):
        with lock:
            if counter >= repetitions:
                break
            counter += 1
            print(f"{thread_name}: Aktualna wartość licznika: {counter}")
        time.sleep(delay)

    # Sprawdzenie, czy wartość została już zapisana przez inny wątek
    if not finished_flag.is_set():
        # Zapisz wartość licznika do pliku
        with open("licznik.txt", "w") as file:
            file.write(f"{thread_name}: Wartość licznika: {counter}\n")
        # Ustaw flagę, że wartość została zapisana
        finished_flag.set()


# Inicjalizacja pliku z wartością początkową licznika
with open("licznik.txt", "w") as file:
    file.write("0\n")

# Wprowadzenie liczby powtórzeń przez użytkownika
repetitions = int(input("Podaj liczbę powtórzeń inkrementacji: "))

# Wprowadzenie opóźnień dla poszczególnych wątków
delay_thread1 = float(input("Podaj opóźnienie dla Wątku 1 (w sekundach): "))
delay_thread2 = float(input("Podaj opóźnienie dla Wątku 2 (w sekundach): "))

# Tworzenie blokady i flagi
lock = threading.Lock()
finished_flag = threading.Event()

# Tworzenie wątków
thread1 = threading.Thread(target=increment_counter, args=(repetitions, delay_thread1, "Wątek 1", lock, finished_flag))
thread2 = threading.Thread(target=increment_counter, args=(repetitions, delay_thread2, "Wątek 2", lock, finished_flag))

# Uruchamianie wątków
thread1.start()
thread2.start()

# Czekanie na zakończenie wątków
thread1.join()
thread2.join()

# Odczytanie wartości licznika po zakończeniu wyścigu
with open("licznik.txt", "r") as file:
    content = file.read()
    print("Wartość licznika po zakończeniu wyścigu:", content)
