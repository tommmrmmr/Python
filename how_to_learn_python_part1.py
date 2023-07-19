"""import math


#Zadanie1. Zdefiniuj zmienną i wydrukuj ją
print("----------Zadanie 1")
wiek = 33
imie ="Tomasz"

print("Twój wiek to: ")
print(wiek)
print()

#Zadanie 2. Sprawdź jakiego typu jest zmienna imię i  wydrukuj tą informację.

print("----------Zadanie 2")
print(type(imie))
print()

#Zadanie 3. Podnieś swój wiek do potęgi wiek. Wydrukuj. Następnie wydrukuj resztę z dzielenia potęki wiek, przez wiek minus  1.
# Wydrukuj.
print("----------Zadanie 3")
print((wiek*wiek) % (wiek-1))
print()

#Zadanie 4. Zdefiniuj 3 zmienne z trzema róznymi wartościami. Zrób to wszystko w jednej lini i print każdą zawartość
print("----------Zadanie 4")
a,b,c = 1,2,3
print(c)
print(b)
print(a)
print()

#Zadanie 5. Zdefiniuj 2 zmienne. Jedno z imieniem męskim, drugie z żeńskim. Stwórz prosty program, który wydrukuje
# ostatnią literę imienia
print("----------Zadanie 5")
imie1 = "Adam"
imie2 = "Ewa"

print(imie1[-1])
print(imie2[-1])
print()

#Zadanie 6. Zdefiniuj zmienną imię3, i wydrukuj tylko drugą i trzecią literę tego imienia
print("----------Zadanie 6")
imie3 = "Arkadiusz"
print(imie3[1:3])
print()

#Zadanie 7. Wyznacz pierwiastek z 16. Załaduj niezbędną bibliotekę
print("----------Zadanie 7")
print(math.sqrt(16))
print()

#Zadanie 8. Zdefiniuj zmienną imie4. Zapisz imie z małych liter. Następnie za pomocą dostępnych w python funkcji zmień
# wielkośc liter
print("----------Zadanie 8")
imie4 = "zygfryd"
print(imie4.capitalize())
print(imie4.upper())
print(imie4.lower())

print()

#Zadanie 9. Zaczytaj dane wprowadzone z klawiatury i zapisz je w zmiennej read i wyświetl zawartość. Następnie zaczytaj
# dwie liczby i wyświetl ich zawartość
print("----------Zadanie 9")
print("Zaczytaj dane wprowadzone z klawiatury i zapisz je w zmiennej read i wyświetl zawartość. Następnie zaczytaj"
      "dwie liczby i wyświetl ich zawartość")
read = input()
print(read)
aa = input()
bb = input()
print(int(aa)+int(bb))
print()

#Zadanie 10. Wykorzystując dane z powyższego zadania. Wyświetl wartość "Mój wynik dodawania to [suma zmiennych])"
print("----------Zadanie 10")
print("Mój wynik dodawania to " , int(aa) + int(bb))
print()

# lub

print("Mój wynik dodawania t:", int(aa) + int(bb))

# Zadanie11. Napisz program, który będzie pytał Cię o imie i  bedzie wyświetlał "Hej, Cześć [imię]". Nastepnie zapyta
# "Ile masz lat?" i wyświetli w odpowiedzi "Za rok będziesz miał [lat + 1]


jmeno = input("Jak masz na imię?" + "\n")
print("Hej, Cześć", jmeno + "\n")
lat = int(input("Ile masz lat?" + "\n"))
print("Za rok będziesz miał", lat + 1, "lata")
print()


#Zadanie12. Wykonaj instrukcję warunkową "if". Zdefiniuj 2 zmienne (input) a i b Jeśli a > b to wydrukuj "a jest
print("----------Zadanie 12")
# wieksze od b". Wykorzystaj też else if a < b i a =b jako else

a = int(input("Wprowadź pierwszą liczbę" + "\n"))
b = int(input("Wprowadź drugą liczbę" + "\n"))


if (a > b):
    print(a, "jest większe od", b)
elif (a < b):
    print(a, "jest mniejsze od", b)
else:
    print(a, "jest równe", b, "\n")

#print("Wartość a ma taki typ danych", type(a))

#Zadanie 13. Bazując na wczesniejszym ćwiczeniu zrób kalkulator. Zaczytaj trzy zmienne "wybór" (gdzie będziemy wybierać
# pomiędzy używym znakiem matematycznym 1 jako mnożenie, 2 jako dzielenie, 3 jako dodawanie, 4 jako odejmowanie), l1
# jako pierwsza liczba i l2 jako druga liczba. Przekaż użytkownikowi instrukcje odnośnie jakiej cyfry dla jakiej
# czynności użyć. Wyłap też błąd jeżeli użytkownik wprowadzi błędne cyfry jako else. W przypadku dzielenia, zrób pętle
# w pętli dzielenia, jeżeli druga wartość przyjmuje wartość 0, wyświetl komunikat... "Synek.. bo jak Ci zaraz ..."
print("----------Zadanie 13")
wybor =int(input('Wprowadź na klawiaturze: 1 jako mnożenie lub 2 jako dzielenie lub 3 jako dodawanie lub'
                 ' 4 jako odejmowanie lub 5 jako potęgowanie, 6 jako reszta z dzielenia' + "\n"))

l1 = int(input("Wprowadź pierwsza wartość: "))
l2 = int(input("Wprowadź drugą wartość: "))

if (wybor == 1):
    print(l1 * l2)
elif (wybor == 2):
    if (l2 == 0):
        print("Synek.. bo jak Ci zaraz ...")
    else:
        print(l1 / l2)
elif (wybor == 3):
    print(l1 + l2)
elif (wybor == 4):
    print(l1 - l2)
elif (wybor == 5):
    print(l1 ** l2)
elif (wybor == 6):
    print(l1 % l2)
else:
    print("Wprowadzono błędny znak arytmetyczny")

#Zadanie 14. Oblicz wartość bezwzględną. -5, 4, -1, 0
print("----------Zadanie 14")


wb = int(input("Wprowadź wartość bezwzględną:" + "\n"))

if (wb > 0):
    print("Wartość bezwzględna to:", wb)
elif (wb < 0):
    #print("Wartość bezwzględna to:", wb - wb - wb)
    print("Wartość bezwzględna to:", abs(wb))
elif (wb == 0):
    print("Wartość bezwzględna to:", wb)



#Zadanie15. Sprawdź czy wprowadzona liczba jest z zakresu od 1 do 10. Użyj  alternatywy i koniunkcji i negacji.
print("----------Zadanie 14")

zakres = int(input("Wprowadź liczbę od 1 do 10" + "\n"))
if (zakres >= 1 and zakres <= 10):
    print("Dobrze!")
else:
    print("Coś nie tak" + "\n")

#Zadanie. Zrób pętle while, która powtórzy się 100x. Zdefiniuj zmienną o nazwie liczba i przypisz wartość 0. Następnie
# Zrób to samo w druga stronę
print("----------Zadanie 15")
print

liczba = 0

while (liczba <= 100):
    print(liczba)
    #liczba = liczba + 1 #zapis mniej popularny
    liczba += 1

print()
liczba = 100

while (liczba >= 0):
    print(liczba)
    #liczba = liczba + 1 #zapis mniej popularny
    liczba -= 1

#Zadanie16. Stwórz pętle, która będzie 4x sumowała liczby podane przez użytkownika. Zapisz liczbę w zmiennej x
# a wynik w wyniku, który będzie przyjmować 0.
print("----------Zadanie 16")
#Poniżej rozwiązanie bez pęttli
wynik = 0
x = int(input("Podaj liczbę" + "\n"))
wynik = wynik + x
x = int(input("Podaj liczbę" + "\n"))
wynik = wynik + x
x = int(input("Podaj liczbę" + "\n"))
wynik = wynik + x
x = int(input("Podaj liczbę" + "\n"))
wynik = wynik + x
print("Suma wszystkich wprowadzonych przez Ciebie liczb to:" ,wynik, "\n")

#poniżej rozwiązanie z pętlą (To właściwe)
print("Przykład właściwy z pętlą")
wynik = 0
i = 0
while (i < 4):
    x = int(input("Podaj liczbę" + "\n"))
    #wynik = wynik + x
    wynik += x
    i += 1
print("Suma wszystkich wprowadzonych przez Ciebie liczb to:" ,wynik, "\n")


#Zadanie16. Wykonaj to samo zadanie co powyżej używając pętli for i in range. Dodatkowo wypisz wartośc i, po każdej
# pętli
print("----------Zadanie 16")

wynik = 0
for i in range(0 , 4): #zamiast range(0, 4), mogłoby być: [0,1,2,3]
    x = int(input("Podaj liczbę" + "\n"))
    #wynik = wynik + x
    wynik += x
    print("Wartość i wynosi obecnie:" , i)

print("Suma wszystkich wprowadzonych przez Ciebie liczb to:" ,wynik, "\n")



#Zadanie17. Bazując na pętli range. Sprawdź które liczby w przedziale 0 - 1200 są parzyste. Wykorzystaj if, %.
print("----------Zadanie 17")
wynik = 0
for i in range(0 , 1200):
    if (wynik % 2 == 0):
        print(wynik, "Jest liczbą parzystą")
    wynik += 1
print()


#Zadanie 18. Pętla range. Wypisz liczby od 0 do 200, które są podzielne przez 5 ale są niepodzielne przez 7 (koniunkcja)
print("----------Zadanie 18")
wynik = 0
for i in range(0, 200):
    if (wynik % 5 == 0) and (wynik % 7 != 0):
        print("Liczba jest podzielna przez pięć i niepodzielna przez siedem:", wynik)
    wynik +=1
print()

#Zadanie 19. Pętla range. Napisz pętle range która iteruje się 3x i wyniki sumują się ze sobą. Wprowadzana liczba ma być
# dodatnia. W przypadku błędnie wprowadzonej użyj break i jakiś komunikat
print("----------Zadanie 19")
wynik = 0
for i in range(3):
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia!")
        break
    print("Aktualny wynik dodawania to:", wynik)

#Zadanie 20. Napisz pętle range która iteruje się 3x i wyniki inputu sumują się ze sobą.
# Wprowadzana liczba ma być dodatnia. W przypadku błędnie wprowadzonej użyj continue i jakiś komunikat
print("----------Zadanie 20")

wynik = 0
for i in range(3):
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia!")
        continue
    print("Aktualny wynik dodawania to:", wynik)

#Zadanie 21. Napisz pętle while, bazując na powyższym zadaniu. Pamiętaj o zdefiniowaniu zmiennej wynik i "i"
print("----------Zadanie 21")
wynik = 0
i = 0
while i<3:
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia!")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1
#Zadanie 22. Dodawanie liczb parzystych podanych przez użytkownika. Napisz program, który doda 3 parzyste liczby dodane
# przez użytkownika
wynik = 0
i = 0

while i<3:
    x = int(input("Podaj dodatnią i parzystą liczbę:"))
    if (x > 0) and (x % 2 == 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia i  parzysta!")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1
#Zadanie 23. Napisz program, który będzie się pytał o liczbe użytkownika i chcemy sprawdzić czy jest równa sekretnej
# liczbie, szukanej liczbie. Jeżeli liczba, którą podał uzytkonik jest za duża, to poinformujemy, że jest za duża,
# jak za mala to za mała w porównaniu do tej co szukamy.

# Pierwsze działające rozwiązanie
sekretnaLiczba = 69

twojaLiczba = int(input("Zgadnij sekretną liczbę. Podaj twoją liczbę: "))

if twojaLiczba == sekretnaLiczba:
    print("Brawo! zgadłeś:", twojaLiczba)
else:
    if twojaLiczba > sekretnaLiczba:
        print("Twoja liczba jest większa od Sekretnej liczby")
    else:
        if twojaLiczba < sekretnaLiczba:
            print("Twoja liczba jest mniejsza od Sekretnej liczby")
#Drugie działające rozwiązanie

i = 0
sekretnaLiczba = 69

while i<1:
    twojaLiczba = int(input("Zgadnij sekretną liczbę. Podaj twoją liczbę: "))
    if twojaLiczba == sekretnaLiczba:
        print("Brawo! zgadłeś:", twojaLiczba)

    else:
        if twojaLiczba > sekretnaLiczba:
            print("Twoja liczba jest większa od Sekretnej liczby")
            continue
        else:
            if twojaLiczba < sekretnaLiczba:
                print("Twoja liczba jest mniejsza od Sekretnej liczby")
                continue
    i += 1
# Trzecie działające rozwiązanie z Udemy
szukanaLiczba = 40
zgadywanaLiczba = 0
while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Odgadnij liczbę: "))
    if zgadywanaLiczba > szukanaLiczba:
        print("Za duża")
    elif zgadywanaLiczba < szukanaLiczba:
        print("Za mała")
    else:
        print("brawo")

#Zadanie 24. Stwórz listę, o nazwie imiona, która będzie posiadała 5 elementów (Arek, Wiola, Karol, Kuba, Adi). Stwórz
# drugą listę "liczby" z wartościami 1,54,-2,20.
# Następnie wyświetl listę imiona i zrób pętle for, która wyświetli imiona (posłuż się wartością " for imie in imiona").
# Analogicznie: stwórz drugą pętle liczby, wg instukcji: For every iteration in list liczby, print these iterations"

imiona = ["Arek", "Wiola", "Karol", "Kuba", "Adi"]
liczby = [1, 54, -2, 20]

print(imiona)

for imie in imiona:
    print(imie)

for i in liczby:
    print(i)

#Zadanie25. Bazując na listach z wcześniejszego przykładu. Wyświetl 3 element listy używając numeru do wyświetlenia
# Następnie wyświetl ten sam element używając ujemnej wartości.imiona = ["Arek", "Wiola", "Karol", "Kuba", "Adi"]
liczby = [1, 54, -2, 20]

print(imiona[2])
print(imiona[-3])



#Zadanie26. Bazując na wcześniejszych listach podmień ostatnie imie na imię Wojtek. Użyj wartości ujemnej i
# w osobnej lini dodatniej podczas  przypisywania. Wyświetl te wartości
imiona = ["Arek", "Wiola", "Karol", "Kuba", "Adi"]
liczby = [1, 54, -2, 20]


print(imiona[-1])
print(imiona[4])
imiona[-1] = "Wojtek"
print(imiona[-1])


#Zadanie27. Na podstawie listy imiona  z poprzedniego zadania, wyświetl ile elementów ma ta lista

print(len(imiona))


#Zadanie28.Na podstawie listy imiona i liczby z poprzedniego zadania, dodaj nowe imie "Tom" na końcu listy imiona.

imiona = ["Arek", "Wiola", "Karol", "Kuba", "Adi"]
liczby = [1, 54, -2, 20]

imiona.append("Tom")
print(imiona)

#Zadanie29. Rozszerz listę liczby o cztery nowe wartości 1,2,3,4

liczby.extend([1,2,3,4])
print(liczby)

#Zadanie30. Wstaw na między Arka, a Wiolę, "Antona"

imiona = ["Arek", "Wiola", "Karol", "Kuba", "Adi"]
imiona.insert(1, "Anton")
print(imiona)

#Zadanie31. Wyświetl, jaki index ma imię Karol

imiona = ["Arek", "Wiola", "Karol", "Kuba", "Adi"]
print(imiona.index("Karol"))

#Zadanie32. Posortuj listę liczby rosnąco i malejąco.

liczby = [1, 54, -2, 20]
liczby.sort()
print(liczby)
liczby.sort(reverse=True)
print(liczby)

#Zadanie33. Wyświetl wartośc minimalną w liście liczby.

liczby = [1, 54, -2, 20]
print(min(liczby))

#Zadanie34. Wyświetl wartość maksymalną w liście liczby.

print(max(liczby))

#Zadanie35. Policz i Wyświetl ile razy wystąpiła wartość 1 w liście liczby. Upewnij się, że komenda extend z zadanie 29
# działa

print(liczby)
liczby.extend([1,2,3,4])
print(liczby)
print(liczby.count(1))

#Zadanie36. Wyrzuć ostatni element z listy imiona. Upewnij się, że Tom z zadania 28 został dodany

print(imiona)
imiona.append("Tom")
print(imiona)
imiona.pop()
print(imiona)

#Zadanie37. Usuń Antona z listy imiona. Upewnij sie, że Anton w zadaniu 30 został dodany

print(imiona)
imiona.insert(1, "Anton")
print(imiona)
imiona.remove("Anton")
print(imiona)


#Zadanie38. Wyczyść listę.

print(imiona)
imiona.clear()
print(imiona)



#Zadanie39. Odwróć wartości w liście.

print(imiona)
imiona.reverse()
print(imiona)


#Zadanie40. Różnica między krotką a listą jest taka, że jak zapiszesz coś w krotce raz to nie można juz zmieniać.
#Stwórz krotkę,która będzie miała 4 wartości. 1, 42, 12, -4 i wyświetl pierwszą wartośc tej krotki

krotka = 1, 42, 12, -4
print(krotka[0])


#Zadanie 41. Stwórz słownik o nazwie "pokoje". Gdzie kluczem będzie numer pokoju hotelowego a warością imie osoby
# tymczasowo rezydującej tam. Zdefiniuj dwa numery pokoju (49 i 69), oraz dwie osoby tam rezydujące.
# Następnie wyświetl słownik pokoje, następnie podmień pierwszą wartość pokoju na nową osobę i wyświetl słownik.
# Następnie przypisz nową osobę to nieutworzonego wcześniej pokoju numer 50 i ponownie wyświetl

pokoje = {49: 'Edyta' , 69: 'Zyga'}
print(pokoje)
pokoje[49] = 'Jarosław'
print(pokoje)
pokoje[50] = "Ferka"
print(pokoje)


#Zadanie 42. Bazując na wcześniejszym zadaniu za pomocą funkcji get wyświetl osobę z 49 pokoju. Następnie za pomocą
# funkcji update dodaj pokój o numerze 400 w którym jest Jasiu Kowalski oraz pokój 555 z osobą o imieniu "Ktosik".
# Wyświetl słownik pokój.

pokoje = {49: 'Edyta' , 69: 'Zyga'}
pokoje[49] = 'Jarosław'
pokoje[50] = "Ferka"
print(pokoje.get(49))
pokoje.update({400: 'Jasiu Kowalski', 555: "Ktosik"})
print(pokoje)



#Zadanie 43. Usuń pokój 555 ze słownika za pomocą funkcji del, oraz pokój 400 za pomocą funkcji pop. Wyświetl słownik.
# Następnie za pomocą popitem usuń ostatnią wartość ze słownika. Wyświetl ponownie słowniki. Sprawdź za pomocą funkcji
# len ile pokoi zostało w słowniku (powinny 2). Następnie za pomocą funkcji clear usuń reszte wartości.
# Sprawdź czy cokolwiek zostało w słowniku pokoje (nie powinno)


pokoje = {49: 'Edyta' , 69: 'Zyga'}
pokoje[49] = 'Jarosław'
pokoje[50] = "Ferka"
pokoje.update({400: 'Jasiu Kowalski', 555: "Ktosik"})


print(pokoje)
del(pokoje[555])
print(pokoje)
pokoje.pop(400)
print(pokoje)
pokoje.popitem()
print(pokoje)
pokoje.clear()
print(pokoje)

#Zadanie 43. Wczytaj ponownie wszystkie wartość zdefiniowane w zadaniu 41. Wyświetl wynik.
# Następnie w tej samej lini ponownie zdefiniuj wszsytkich a na końcu przypisz dodatkowo Paula do pokoju numer
# 49. Wyświetl pokoje (dla pokoju 49 powinna być tylko jedna wartość (ta ostatnia)

pokoje = {49: 'Edyta' , 69: 'Zyga'}
pokoje[49] = 'Jarosław'
pokoje[50] = "Ferka"
pokoje.update({400: 'Jasiu Kowalski', 555: "Ktosik"})
print(pokoje)

pokoje = {49: 'Edyta', 69: 'Zyga', 49: 'Jarosław', 50: 'Ferka', 400: 'Jasiu Kowalski', 555: 'Ktosik', 49: "Paul"}
print(pokoje)


#Zadanie 44. Stwórz zbiór, 1,4,20 -4,20 i przypisz do zmiennej A. Wyświetl zawartość. Następnie stwórz listę (L) z takimi
# samymi elementami i krotkę (K).

A = {1, 4, 20, -4, 20}
print(A)
L = [1,4,20, -4,20]
print(L)
K = (1,4,20,  -4,20)
print(K)

#Zadanie 45. Za pomocą funkcj add, dodaj wartość 5 do zbioru. Następnie usuń tę wartość za pomocą funkcji discard.
# Wyświetl wszystko

A = {1, 4, 20, -4, 20}
print(A)
A.add(5)
print(A)
A.discard(5)
print(A)

#Zadanie 46. Przekształć listę (L) na zbiór i wyświetl wszystkie wyniki.

L = [1,4,20, -4,20]
print(L)
L = set(L)
print(L)

#Zadanie 47. Stwórz listę b = 2, 1, 25, 40, 20, przekształć na zbiór B , a następnie pokaż wspólne elementy zbioru A i B

A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(A)
print(B)
print(A&B)


#Zadanie 48. Wyświetl wszystkie elementy zbioru A i B (w jednej komendzie)

A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(A)
print(B)
print(A|B)

#Zadanie 49. Odejmij wartości ze zbioru B od  zbioru A.

A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(A)
print(B)
print(A-B)

#Zadanie 49. Odejmij wartości ze zbioru A od  zbioru B.

A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(A)
print(B)
print(B-A)

#Zadanie 50. Zrób alternatywę wykluczającą A i B. Jak odejmiemy od wszystkich elementów to co było wspólne to będzie XOR
#  (wyklucza wspólne wartości).

A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(A)
print(B)
print(A^B)

#Zadanie 51. Sprawdź czy zbiór A jest podzbiorem zbioru B.

A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(A.issubset(B))

#Zadanie 52. Stwórz zbiór C o wartościach 1,4. Sprawdź czy C jest podzbiorem A

C = {1,4}
A = {1, 4, 20, -4, 20}
b = [2,1,25,40,20]
B = set(b)
print(C.issubset(A))

#Zadanie 53. Zrób program, który stwierdzi, czy imie jest żeńskie czy męskie. Dodaj wyjątek "Kuba" jakio imię męskie

imie = input("Napisz swoje imię:")
if imie[-1] == "a":
    print("Jesteś kobietą")
elif imie == "Kuba":
    print("Jesteś mężczyzną")
else:
    print("Jesteś mężczyzną")


#Zadanie 54 zdefiniuj zmienne:
# imie = "Arkadiusz"
# wiek = 28
# plec = "mezczyzna"
# imie2 = "Wioletta"
# wiek2 = 23
# plec2 = "kobieta"
# Następnie stworz zmienną "listę gosci" (listy, w liście - wykorzystaj powyższe dane). Wyświetl listeGosci
# Wywolaj tylko imię "Arkadiusza" ze zmiennej listaGosci.
# Wywolaj "Arkadiusz", 28, "mezczyzna" z listy gości
# Wywołaj "płeć" Arkadiusza
# Wywołaj "płeć" Wioletty

imie = "Arkadiusz"
wiek = 28
plec = "mezczyzna"
imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

listaGosci = [
    [imie, wiek, plec],
    [imie2, wiek2, plec2]
]

print(listaGosci)

print(listaGosci[0][0])
print(listaGosci[0])
print(listaGosci[0][2])
print(listaGosci[1][2])

#Zadanie 55. Bazując na liście ze wczesniejszego zadania, zmień wiek Arkadiusza na 29.
# Następnie wyświetl wszystkie dane dotyczące Arkadiusza

imie = "Arkadiusz"
wiek = 28
plec = "mezczyzna"
imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

listaGosci = [
    [imie, wiek, plec],
    [imie2, wiek2, plec2]
]

listaGosci[0][1] = 29
print(listaGosci[0])

#Zadanie 56. Za pomocą funkcji append. Dodaj Karol, 26, mężczyzna. Wyświetl całą listęGości

imie = "Arkadiusz"
wiek = 28
plec = "mezczyzna"
imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

listaGosci = [
    [imie, wiek, plec],
    [imie2, wiek2, plec2]
]

listaGosci.append(["Karol", 26, "mężczyzna"])
print(listaGosci)

#Zadanie 57. Zmień listęGości na seta (ręcznie, bez kombinacji), a listy wewnętrzne na krotki (też ręcznie)
# i dodaj krotkę Kuba, 33, mężczyzna

imie = "Arkadiusz"
wiek = 28
plec = "mezczyzna"
imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

listaGosci = {
    (imie, wiek, plec),
    (imie2, wiek2, plec2)
}

listaGosci.add(("Kuba", 33, "mężczyzna"))
print(listaGosci)

#Zadanie 58. Dodaj listeGosci (krotki w secie)  (zmień tylko 2 imiona, reszte danych zostaw takie same).
# Następnie zsumuj dwie listy.
# Zrób w taki sposób, żeby Arkadiusz wyświetlił sie tylko raz. Następnie sprawdź czy ktoś nie zapisał się podwójnie
# na dwie listy (&)

imie = "Arkadiusz"
wiek = 28
plec = "mezczyzna"
imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"

listaGosci = {
    (imie, wiek, plec),
    (imie2, wiek2, plec2)
}

listaGosci.add(("Kuba", 33, "mężczyzna"))

listaGosci2 = {
    (imie, wiek, plec),
    ("W", wiek2, plec2),
    ("K", 33, "mężczyzna")
}

print(listaGosci | listaGosci2)
print(listaGosci & listaGosci2)


#Zadanie 59. Stwórz set listaGosci z trzema krotkami wewnątrz niego:
# "Arkadiusz", 28, "m" ; "Wiola", 23, "k" ; "Kuba", 32, "m".)
# Zrób jedną pętle for dla imie, wiek i plec dla listaGosci, która wyświetli w kolejnych liniach:
# Imie: wartość przypisana z listaGości
# Wiek: wartość przypisana z listaGości
# Plec: wartość przypisana z listaGości
# Imie: wartość przypisana z listaGości
# Wiek: wartość przypisana z listaGości
# Plec: wartość przypisana z listaGości
# Imie: wartość przypisana z listaGości
# Wiek: wartość przypisana z listaGości
# Plec: wartość przypisana z listaGości
# Następnie daj wolną linię \n  między każdą krotką (w pętli for)

listaGosci = {
    ("Arkadiusz", 28, "m"),
    ("Wiola", 23, "k"),
    ("Kuba", 32, "m")
}

for imie, wiek, plec in listaGosci:
    print("Imie", imie)
    print("wiek", wiek)
    print("płeć", plec)
    print("\n")

#Zadanie 60. Dodaj nową wartość numer telefonu do każdej krotki z seta listyGosci i powtórz:
# Zrób jedną pętle for dla imie, wiek, plec, telefon dla listaGosci, która wyświetli w kolejnych liniach:

listaGosci = {
    ("Arkadiusz", 28, "m", 278884585),
    ("Wiola", 23, "k", 789456123),
    ("Kuba", 32, "m", 321654987)
}

for imie, wiek, plec, telefon in listaGosci:
    print("Imie", imie)
    print("wiek", wiek)
    print("płeć", plec)
    print("telefon", telefon)
    print("\n")


#Zadanie 61. Stwórz dziennik (jako zmienna) 5 uczniów (jako słownik) i klucz jako oceny w formie ktorek. Ustaw 10 losowych ocen od
# 1 - 6
#"Arkadiusz": (1,2,3,4,5,1,2,3,4,5)
# następnie do każdej wartości dopisz identyfikator każdego ucznia składający się z 5 alfanumerycznych wartości.
# ChU7: {"Arkadiusz": (4,2,1,3,5,1,2,4,5,3)},
# Głównym celem zadania jest zagnieżdżenie czyli słownik w słowniku. Nastęnie wyświetl dziennik

dziennik = {
    "ChU7": {"Arkadiusz": (4,2,1,3,5,1,2,4,5,3)},
    "ChE2": {"Ewa": (2,1,5,4,3,1,5,2,3,4)},
    "ChJ3": {"Jan": (3,2,1,5,4,2,3,1,5,4)},
    "ChK4": {"Karol": (5,3,4,1,2,5,1,3,2,4)},
    "ChM5": {"Magda": (5,3,2,4,1,5,3,1,2,4)},
    "ChO6": {"Ola": (1,5,2,4,3,1,5,2,3,4)},
    "ChT7": {"Tomek": (2,1,5,4,3,2,4,1,3,5)},
    "ChK8": {"Kasia": (1,4,2,5,3,1,4,3,5,2)},
    "ChM9": {"Marek": (4,5,3,2,1,4,3,5,2,1)},
    "ChA0": {"Ania": (3,2,4,1,5,2,1,4,5,3)}
}

print(dziennik)

#Zadanie 62. Bazując na danych ze wcześniejszego zadania wywołaj:
#Anie z ocenami,
#Same oceny Ani
#Ostatnią ocenę Ani.
#Drugą ocenę Ewy
dziennik = {
    "ChU7": {"Arkadiusz": (4,2,1,3,5,1,2,4,5,3)},
    "ChE2": {"Ewa": (2,1,5,4,3,1,5,2,3,4)},
    "ChJ3": {"Jan": (3,2,1,5,4,2,3,1,5,4)},
    "ChK4": {"Karol": (5,3,4,1,2,5,1,3,2,4)},
    "ChM5": {"Magda": (5,3,2,4,1,5,3,1,2,4)},
    "ChO6": {"Ola": (1,5,2,4,3,1,5,2,3,4)},
    "ChT7": {"Tomek": (2,1,5,4,3,2,4,1,3,5)},
    "ChK8": {"Kasia": (1,4,2,5,3,1,4,3,5,2)},
    "ChM9": {"Marek": (4,5,3,2,1,4,3,5,2,1)},
    "ChA0": {"Ania": (3,2,4,1,5,2,1,4,5,3)}
}
print("Ania z ocenami")
print(dziennik["ChA0"])
print("Same oceny Ani: ")
print(dziennik["ChA0"]["Ania"])
print("Ostatnia ocenna Ani")
print(dziennik["ChA0"]["Ania"][1])
print("Ostatnia ocenna Ani")
print(dziennik["ChA0"]["Ania"][1])


#Zadanie 63. Przypominające. Stwórz krotkę o nazwie tuple która posiada 5 wartości od 1 do 5. Wyświetl drugą pozycję
tuple = (1, 2, 3, 4, 5)
print(tuple[1])

#Zadanie 64. Przypominające. Stwórz listę o nazwie list która posiada 5 wartości od 1 do 5. Wyświetl pierwszą pozycję
list = [1,2,3,4,5]
print(list[0])
#Zadanie 65. Przypominające. Stwórz słownik o nazwie dict która posiada 5 wartości klucza od 1 do 5 i przypisanej wartości od a do e. Wyświetl ostatnią pozycję
dict = {1:"a",2:"b",3:"c",4:"d",5:"e"}
print(dict[5])

#Zadanie 66. Przypominające. Stwórz seta o nazwie tuple która posiada 5 wartości od 1 do 5. Wyświetl zawartość całego setu, bo nie możesz odwołac się do konkretnego
set = {1,2,3,4,5}
print(set)

#Zadanie 67. Stwórz listę o nazwie listexample w której będą cztery  słowniki:
#"id":1, "name":a, "age":1
#"id":2, "name":b, "age":2
#"id":3, "name":c, "age":3
#"id":4, "name":d, "age":4
# Następnie wywołaj imie dla id4

listexample = [
    {"id":1, "name":"a", "age":1},
    {"id":2, "name":"b", "age":2},
    {"id":3, "name":"c", "age":3},
    {"id":4, "name":"d", "age":3}
]

print(listexample[3]["name"])

#Zadanie 68. Stwórz słownik oceny, który będzie zawierał dwóch uczniow (Adam i Ewa)i ich 5 ocen w postaci krotki.
# Wywołaj oceny Ewy
oceny = {
    "Ewa":(1,2,3,4,5,6),
    "Adam":(6,5,4,3,2,1)
}

print(oceny["Ewa"])



#Zadanie 69. Wykonaj pętlę for Dla każdego rekordu z zadania 68. Pętla ma działać tyle razy ile jest kluczy w oceny.
# Czyli dla imiona w oceny, wyświetl oceny-imiona. Następnie dla porównania wyświetl wysztskie oceny Ewy i Adama nie używając
# pętli

oceny = {
    "Ewa":(1,2,3,4,5,6),
    "Adam":(6,5,4,3,2,1)
}


for imiona in oceny:
    print(oceny[imiona])

print()
print(oceny["Ewa"])
print(oceny["Adam"])


#Zadanie 70. Zmodyfikuj wczesniejsze zadanie (wciąż używając pętli) w taki sposób, aby wyświetlało np.
# "Ktosik oceny: (1, 2, 3, 4, 5). Wyświetl imiona, oceny i oceny-imiona

oceny = {
    "Ewa":(1,2,3,4,5,6),
    "Adam":(6,5,4,3,2,1)
}

for imiona in oceny:
    print(imiona, "oceny", oceny[imiona])


#Zadanie 71. Stwórz listę o nazewie people z trzema imionami Ewa, Adam, Lilith. Stwórz pętla, która będzie przechodzić
# przez wszystkie elementy. Dla każdej imienia w people, wyświetl wszystkie  imiona.

people = ["Ewa",
          "Adam",
          "Lilith"
          ]
print(people)

for imiona in people:
    print(imiona)



#Zadanie 72. Zmodyfikuj oceny z zadania 68 tak, żeby tworzyły listę w której będą słowniki. I zrób pętle for,
# dla każdego imie w oceny, wyświetl wartości

oceny = [
    {"Ewa": (1,2,3,4,5,6)},
    {"Adam": (6,5,4,3,2,1)}
]

for wartosc in oceny:
    print(wartosc)
"""
#Zadanie 73. Bazując na zadaniu 67 i 70
# listexample = [
#     {"id":1, "name":"a", "age":1},
#     {"id":2, "name":"b", "age":2},
#     {"id":3, "name":"c", "age":3},
#     {"id":4, "name":"d", "age":3}
# zrób pętle w pętli. Celem twoim jest wyświetlenie:
# id 1
# name a
# age 1
#itd ....
# . Czyli dla każdej słownika w list example, (i) dla każdego klucza w wartości, wyświetl klucz i  wartości-klucz
"""
listexample = [
    {"id":1, "name":"a", "age":1},
    {"id":2, "name":"b", "age":2},
    {"id":3, "name":"c", "age":3},
    {"id":4, "name":"d", "age":3}
    ]
for słownik in listexample:
    for key in słownik:
        print(key, słownik[key])
"""
#Zadanie 74. Dla każdego słownika w słowniku (people).
# wykonuj to zadanie po kolei. Wyświetl najpierw people.
#Następnie wyświetl klucz ChU7. Otrzymamy w ten sposób poszczególny słownik.
#Następnie dla klucza w people wyświetl klucz (pętla)
#Następnie dopisz w wyświetlanej wiadomości "ID:" przed każdym kluczem.
#Następnie dopisz do wcześniejszej pętli nową pętle, gdzie dla drugiegoKlucza, (który jest de facto w tym kluczu głównym) w
# kluczu w people, wyświetl drugiKlucz i drugiKlucz w kluczu w people



# people = {
#     "ChU7": {"name": "Arkadiusz", "age":22, "sex": "Male"},
#     "ChE2": {"name": "Ewa", "age":23 , "sex": "Female"},
#     "ChJ3": {"name": "Jan", "age": 24, "sex": "Male"},
#     "ChK4": {"name": "Karol", "age": 25, "sex": "Male"},
#     "ChM5": {"name": "Magda", "age": 26, "sex": "Female"},
#     "ChO6": {"name": "Ola", "age": 27, "sex":"Female"},
#     "ChT7": {"name": "Tomek", "age": 28, "sex":"Male" },
#     "ChK8": {"name": "Kasia", "age": 29, "sex": "Female"},
#     "ChM9": {"name": "Marek", "age": 30, "sex": "Male"},
#     "ChA0": {"name": "Ania",  "age": 31, "sex": "Female"},
# }

people = {
    "ChU7": {"name": "Arkadiusz", "age":22, "sex": "Male"},
    "ChE2": {"name": "Ewa", "age":23 , "sex": "Female"},
    "ChJ3": {"name": "Jan", "age": 24, "sex": "Male"},
    "ChK4": {"name": "Karol", "age": 25, "sex": "Male"},
    "ChM5": {"name": "Magda", "age": 26, "sex": "Female"},
    "ChO6": {"name": "Ola", "age": 27, "sex":"Female"},
    "ChT7": {"name": "Tomek", "age": 28, "sex":"Male" },
    "ChK8": {"name": "Kasia", "age": 29, "sex": "Female"},
    "ChM9": {"name": "Marek", "age": 30, "sex": "Male"},
    "ChA0": {"name": "Ania",  "age": 31, "sex": "Female"},

}

# #print(people)
# #print(people["ChU7"])
# for key in people:
#     print("ID:", key)
#     for drugikey in people[key]:
#         print(drugikey, ":", people[key][drugikey])

#Zadanie 75.  Dla każdego klucza w people print klucz to 'klucz, a wartość klucza to = 'klucz w people'

"""for key in people:
     print("klucz to: ", key, ", a wartość klucza to =", people[key])
"""
#11:16



#Zadanie 76. Napisz funkcję w języku Python o nazwie remove_whitespace, która przyjmuje jeden argument - string.
# Funkcja powinna zwrócić ten sam string, ale bez białych znaków (spacji) na początku i końcu.
"""
def remove_whitespace(str):
    return str.strip()

print(remove_whitespace("  Hello, World!  "))
print(remove_whitespace("   Python   "))
print(remove_whitespace("  OpenAI  "))
"""
# Zadanie przypomnienie 77.
# Przypisz do zmiennej imie wartość Wiola, następnie wyświetl tylko io
"""
imie = "Wiola"
print(imie[1:3])

"""

# Zadanie 78. Bazując na zadaniu 76 wykonaj to samo ale przypisz wartości w nawiasach do zmiennych
"""def remove_whitespace(str):
    return str.strip()

hello = "  Hello, World!  "
python = "   Python   "
openAI = "  OpenAI  "

print(remove_whitespace(hello))
print(remove_whitespace(python))
print(remove_whitespace(openAI))
"""

# Zadanie 79. Przypomnienie.  Zaokrąglij 4,2 do 5.
"""import math

print(math.ceil(4.2))

"""
# Zadanie przypomnienie 80. Zrób pętle, która będzie sumowała 4 kolejne wprowadzone liczby
# Podpowiedź:
# Podczas gdy i będzie mniejsze niż 4 to przypisz input "podaj liczbę jako int do zmiennej x
# a następnie dodaj do tego x wartość jeden w zmiennej wynik, oraz i też powiekszaj.
# Następnie w nowej lini Wynik dodawania to wynik
"""
wynik = 0
i = 0
while i < 4:
    x = int(input("Podaj liczbę do sumowania:"))
    wynik += x
    i += 1

print("Wynik dodawania czterech kolejnych liczb to:", wynik)
"""

# Zadanie 81. Napisz to samo co wyżej używając pętli for. Dla każdego i wewnątrz listy 4 elementowej [0,1,2,3],
# wykonaj: wprowadź input jako int w zmiennej x, następnie do wyniku dodaj wynik + x
"""
wynik = 0
i = 0
for i in [0,1,2,3]:
    x = int(input("Podaj liczbę do sumowania:"))
    wynik += x
    

print("Wynik dodawania czterech kolejnych liczb to:", wynik)
"""
# Zadanie 82. Zrób to samo używając range(0,3)
"""
wynik = 0
i = 0
for i in range(0,4):
    x = int(input("Podaj liczbę do sumowania:"))
    wynik += x

print("Wynik dodawania czterech kolejnych liczb to:", wynik)
"""
#  Zadanie 83. Zrób to samo używając w range(4)
"""
wynik = 0
i = 0
for i in range(4):
    x = int(input("Podaj liczbę do sumowania:"))
    wynik += x

print("Wynik dodawania czterech kolejnych liczb to:", wynik)
"""
# Zadanie 84. Zastąp numer 4, Twoim iminiem, i dodaj linie print(i) w pętli for i in range
"""
wynik = 0
i = 0
for i in "Tomasz":
    x = int(input("Podaj liczbę do sumowania:"))
    wynik += x
    print(i)

print("Wynik dodawania czterech kolejnych liczb to:", wynik)
"""

# Zadanie 85. Zastąp imie wartością 15 i w ciele pętli sprawdź czy poszczególne wartości są podzielne podzielne przez 2 (i%2).
# Nie dodawaj wartości już (wynik+=x)
"""

i = 0
for i in range(15):
    x = int(input("Czy liczba jest podzielna przez 2:"))
    print("Liczba:", x)
    print(x % 2)

print("Koniec programu")
"""
# Zadanie 86. Zmodyfikuj wczesniejsze zadanie. W pętli for daj if i modulo 2 jest równe 0, wtedy wyświetl "Liczba [i]
# jest parzysta". Usuń input, ilość iteracji 80.
"""

for i in range(80):

    if i % 2 == 0:
        print("Liczba:", i, "to liczba parzysta")
    else:
        print("Liczba:", i, "to liczba nieparzysta")

print("Koniec programu")
"""
# Zadanie 87. Wypisz liczby od 0 do 200 (włącznie), które są podzielne przez 5 ale są niepodzielne przez 7

"""
for i in range(201):

    if i % 5 == 0 and i % 7 != 0:
        print("Liczba:", i, "jest podzielna przez 5 i jest niepodzielna przez 7")
    elif i % 7 == 0:
        print("Liczba", i ,"jest podzielna przez 7 i wynik to:", i/7)
    else:
        print(i, ": Pozostała liczba, która nie została wzięta pod uwagę")



print("Koniec programu")
"""

# Zadanie 88.Zrób ponownie pętle for dla 3 elementów. Zapisz w zmiennej  dodawane liczby. Wyświetl
# "Podaj dodatnią liczbę:". Jeśli liczba będzie większa niż zero dodaj wynik do liczby. Wyświetl aktualny wynik
"""
wynik = 0
i = 0

for i in range(3):
    x = int(input("Podaj dodatnią liczbę: "))
    if x > 0:
        wynik += x
    print("Aktualny wynik to:",  wynik)
"""
# Zadanie 89. Bazując na wczesniejszym zadaniu. Rozszerz program o wartość else, gdzie zastosujesz break i jakiś
# komentarz o nieprawidłowej wartości.
"""
wynik = 0
i = 0

for i in range(3):
    x = int(input("Podaj dodatnią liczbę: "))
    if x > 0:
        wynik += x
    else:
        print("wprowadziłes nieprawidłową liczbę")
        break
    print("Aktualny wynik to:",  wynik)

"""
# Zadanie 90. Bazując na wczesniejszym zadaniu zastąp break przez wyrażenie continue.

"""
wynik = 0
i = 0

for i in range(3):
    x = int(input("Podaj dodatnią liczbę: "))
    if x > 0:
        wynik += x
    else:
        print("wprowadziłes nieprawidłową liczbę")
        continue
    print("Aktualny wynik to:",  wynik)

"""

# Zadanie 91. Bazujac na wczesniejszym zadaniu zastąp for przez while gdzie i jest mniejsze niż 3.
# Pamiętaj o powiększeniu iteracji w while

"""
wynik = 0
i = 0

while i < 3:
    x = int(input("Podaj dodatnią liczbę: "))
    if x > 0:
        wynik += x
    else:
        print("wprowadziłes nieprawidłową liczbę")
        continue
    print("Aktualny wynik to:",  wynik)
    i += 1

"""

# Zadanie 92. Napisz program, który doda kolejne 3 parzyste liczby dodanie.
"""
wynik = 0
i = 0

while i < 3:
    x = int(input("Podaj dodatnią liczbę: "))
    if x > 0 and x % 2 == 0:
        wynik += x
    else:
        print("wprowadziłes nieprawidłową liczbę")
        continue
    print("Aktualny wynik to:",  wynik)
    i += 1
"""

# Zadanie 93. Napisz program, który będzie się pytał o liczbę użytkownika i  czy jest ona równa sekretnej szukanej liczbie.
# Jeżeli ta liczba będzie za duża do użytkownik powinien dostać informacje, jeżeli za mała też. Jeżeli trafi to powinien
# zostać poinformowany o tym.





# if sekretna_liczba < propozycja:
#     print("Przestrzeliłeś - próbuj dalej")
#
# elif sekretna_liczba > propozycja:
#     print("ooooo Panie, co tak słabo, próbój dalej")
#
# else:
#     print("Brawo, trafiłeś sekretną liczbę")
"""
sekretna_liczba = 69

i = 0
while i < 1:
    propozycja = int(input("podaj sekretną liczbę:"))
    if sekretna_liczba < propozycja:
        print("Przestrzeliłeś - próbuj dalej")

    elif sekretna_liczba > propozycja:
        print("ooooo Panie, co tak słabo, próbuj dalej")

    else:
        print("Brawo, trafiłeś sekretną liczbę")
        i += 1
"""
"""
# Version 2
sekretna_liczba = 69
propozycja = 0


while sekretna_liczba != propozycja:
    propozycja = int(input("podaj sekretną liczbę:"))
    if sekretna_liczba < propozycja:
        print("Przestrzeliłeś - próbuj dalej")

    elif sekretna_liczba > propozycja:
        print("ooooo Panie, co tak słabo, próbuj dalej")

    else:
        print("Brawo, trafiłeś sekretną liczbę")
"""
# Zadanie 94. Stówrz listę o nazwie imiona, gdzie będzie 5 elementów. Oraz listę o nazwie liczby gdzie będą cztery wartości,
 # następnie zrób listę mieszana, gdzie będą cztery warttości int/str/int/str. Wyświetl wszystkie listy

imiona = ["Kasia", "Basia" ,"Zosia" ,"Tosia" ,"Euglena"]
liczby = [2,3,4,5]
mieszana = [imiona[1],liczby[1],imiona[2],liczby[2]]
# print(mieszana)
# print(type(mieszana))

 # Zadanie 95. Stwórz pętle. Dla każdego imienia znajdującego się w liście imiona, wyświetl każde imie
"""
for imie in imiona:
    print(imie)
"""
 # Zadanie 96. Wyświetl pierwsze imie z listy imiona, wyświetl ostatnie imie na dwa sposoby, oraz 4 pozycję z listy imiona
# print(imiona[1])
# print(imiona[4])
# print(imiona[-1])


 # Zadanie 97. Podmień ostatnie imie w liście imiona na imię "Wojtek". Następnie wyświetl ostatni element listy
# print(imiona)
imiona[4] = "Wojtekk"

# print(imiona)

 #  Zadanie 98. Sprawdź poprzez print czy Wojtek (jest) w imiona. Następnie zrób warunek: jeśli Wojtek jest w imiona,
#  wyświetl "Cześć Wojtku"
# print("Wojtek" in imiona)

# if "Wojtek" in imiona:
#     print("Cześć Wojtku")

imiona[4] = "Wojtek"

# if "Wojtek" in imiona:
#     print("Cześć Wojtku")


# Zadanie 99, Sprawdź czy jeżeli 2 nie jest w liczbach wyświetl "Nie ma liczby 2". W pozostałym wypadku
# "Liczba 2 w liście liczby się znajduje".
#
# if 2 not in liczby:
#     print("Nie ma 2 w liczby")
# else:
#     print("Liczba 2 w liście liczby się znajduje ")
#

# Zadanie 100. Wykonaj operaację. Wyświetl wynik 3* liczby. Następnie wyśwetl trzy nowe liczby dodane do listy liczby.
# Nie twórz nowej listy, uzyj tylko print
#
# print(3 * liczby)
# print( [1,2,3] + liczby)