def main():
    predefined_hosts = {'host1', 'Hoat5', 'Host22', 'Host31', 'Host1', 'Host2', 'Host3' }  # Zdefiniowana lista hostów
    user_hosts = set()

    print("Wprowadź listę hostów do sprawdzenia, każdy w nowej linii (aby zakończyć, pozostaw puste pole i wciśnij Enter):")
    while True:
        user_input = input().strip()
        if not user_input:
            break
        user_hosts.add(user_input)

    common_hosts = user_hosts.intersection(predefined_hosts)
    if common_hosts:
        print("\nHosty, które znajdują się zarówno w Twojej liście, jak i w zdefiniowanych:")
        for host in common_hosts:
            print(host)
    else:
        print("\nNie znaleziono wspólnych hostów.")


if __name__ == "__main__":
    main()


print()
print()
x = input("Naciśnij dowolny klawisz")
if x is True:
    print()
