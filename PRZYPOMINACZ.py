from datetime import datetime
from dateutil.relativedelta import relativedelta

def pobierz_date():
    while True:
        data = input("Podaj datę w formacie dd/mm/yyyy lub wpisz 'd' dla dzisiejszej daty: ")
        if data.lower() == 'd':
            return datetime.now()
        else:
            try:
                return datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Niepoprawny format daty. Spróbuj ponownie.")

# Pobieranie daty od użytkownika
dzisiaj = pobierz_date()

# Formatowanie daty do formatu dzień/miesiąc/rok
dzisiaj_format = dzisiaj.strftime('%d/%m/%Y')
print(f"Dzisiaj: {dzisiaj_format}")

# Obliczanie dat przypomnień
drugie_przypomnienie = dzisiaj + relativedelta(days=1)
trzecie_przypomnienie = drugie_przypomnienie + relativedelta(days=2)
czwarte_przypomnienie = trzecie_przypomnienie + relativedelta(weeks=1)
piate_przypomnienie = czwarte_przypomnienie + relativedelta(weeks=2)
szoste_przypomnienie = piate_przypomnienie + relativedelta(months=1)
siodme_przypomnienie = szoste_przypomnienie + relativedelta(months=3)
osme_przypomnienie = siodme_przypomnienie + relativedelta(months=6)
dziewiate_przypomnienie = osme_przypomnienie + relativedelta(years=1)
dziesiate_przypomnienie = dziewiate_przypomnienie + relativedelta(years=2)
jedenaste_przypomnienie = dziesiate_przypomnienie + relativedelta(years=3)
dwunaste_przypomnienie = jedenaste_przypomnienie + relativedelta(years=4)

# Wyświetlanie dat przypomnień
print(f"Drugie przypomnienie: {drugie_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Trzecie przypomnienie: {trzecie_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Czwarte przypomnienie: {czwarte_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Piąte przypomnienie: {piate_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Szóste przypomnienie: {szoste_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Siódme przypomnienie: {siodme_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Ósme przypomnienie: {osme_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Dziewiąte przypomnienie: {dziewiate_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Dziesiąte przypomnienie: {dziesiate_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Jedenaste przypomnienie: {jedenaste_przypomnienie.strftime('%d/%m/%Y')}")
print(f"Dwunaste przypomnienie: {dwunaste_przypomnienie.strftime('%d/%m/%Y')}")

# Funkcja kończąca działanie programu
x = input("Naciśnij dowolny przycisk aby zakończyć działanie programu")
if x:
    print("Kończymy program...")