f = open("licznik.txt", "r+")
i = int(f.read())
# i = f(read)
# i = int
ileRazy = int(input("Wprowadź ile razy ma nastąpić inkrementacja:" + "\n"))
max = i + ileRazy
w = f.write(str(i) + "\n")

while ( i < max ):
     i += 1
     print("Wartość kontrolna:", i) #poglądowo, żeby widzieć
     f.write(str(i) + "\n")
f.close()
if (i == max):
     f = open("licznik.txt", "w+")
     f.write(str(i) + "\n")
     print("Wartość oczekiwana:", i)
f.close()