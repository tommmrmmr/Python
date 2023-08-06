import math

dystans = float(input("Podaj ile kilometrów przejechałeś: (w formacie np 7.2 (użyj kropki zamiast przecinka)):\n"))
print("Przejechany dystans to:", dystans, "km \n")

spalanie = float(input("Podaj spalanie tj: \nIle litrów na 100km spala twój samochów (w formacie np 7.2 (użyj kropki zamiast przecinka)): \n"))
print("Twoje spalanie to:", spalanie, "l na 100 km\n")

ile_litrów = (spalanie * dystans)/100
cena_benzyny_za_litr = float(input("Podaj cenę benzyny/diesel za 1l (w formacie np 7.2 (użyj kropki zamiast przecinka)): \n"))
cena_za_przejazd = cena_benzyny_za_litr * ile_litrów


koszt_1km = (cena_za_przejazd * 1 )/dystans
print("Spaliłeś w zaokrągleniu ", round(ile_litrów, 2), "l paliwa\n")
print("Przejazd kosztował Cię:\n" ,round(cena_za_przejazd,2), "zł (bo: ", ile_litrów, "l *", cena_benzyny_za_litr, "zł)\n")
print("Dodatkowe informacja: jeden kilometr kosztował Cię:\n",round(koszt_1km,2), "zł (bo ", cena_za_przejazd, "zł /", dystans, "zł) ")

procent_napiwku = float(input("\nPodaj procent napiwku\n"))
print("\nDolicz napiwek w wysokości", float(procent_napiwku), "%\n")
napiwek = procent_napiwku/100 * cena_za_przejazd
przejazd_z_napiwkiem = napiwek + cena_za_przejazd

print("Przejazd z napiwkiem wynosi", round(przejazd_z_napiwkiem,2), "zł (bo:", cena_za_przejazd, "zł +", napiwek, "zł)")

zaokraglona_kwota =  math.ceil(przejazd_z_napiwkiem / 10) * 10

print("\nZaokrąglij do pełnej kwoty, żeby łatwiej się rozliczyć. Kwota wynosi:", round(zaokraglona_kwota), "zł")

ile_osob = int(input("\nWprowadź ile osób zrzuca się na paliwo (jeśli tylko kierowca to wprowadź 1):\n"))

print("Cena za paliwo za jedną osobę wynosi:\n", round(zaokraglona_kwota / ile_osob), "zł\n")

x = input("\nNaciśnij dowolny przycisk aby zakończyć działanie programu:\n")
if x == True:
    print("Program kończy działanie")

# Wyłap błędy
# Prosty interface