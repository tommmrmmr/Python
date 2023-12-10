from time import sleep

pytania = ['Co jest w katalogu /',
           'Co jest w katalogu /bin',
           'Co jest w katalogu /etc ',
           'Co jest w katalogu /home',
           'Co jest w katalogu /opt',
           'Co jest w katalogu /tmp',
           'Co jest w katalogu /usr',
           'Co jest w katalogu /var',
           'Co jest w katalogu /boot ',
           'Co jest w katalogu /cdrom',
           'Co jest w katalogu /cgroup',
           'Co jest w katalogu /dev',
           'Co jest w katalogu /etc',
           'Co jest w katalogu /export',
           'Co jest w katalogu /lib ',
           'Co jest w katalogu /lib64',
           'Co jest w katalogu /lost+found',
           'Co jest w katalogu /media',
           'Co jest w katalogu /mnt',
           'Co jest w katalogu /opt',
           'Co jest w katalogu /proc',
           'Co jest w katalogu /root',
           'Co jest w katalogu /sbin ',
           'Co jest w katalogu /selinux',
           'Co jest w katalogu /srv',
           'Co jest w katalogu /srv/www',
           'Co jest w katalogu /srv/ftp	',
           'Co jest w katalogu /sys ',





           ]

print("Baza pytań to:", len(pytania))
odpowiedzi = ['Root, `/`: Jest to katalog główny, który zawiera wszystkie inne katalogi i pliki w systemie³.',
              'Binaries and other executable programs, Katalog /bin w systemie Red Hat Enterprise Linux (RHEL) zawiera binaria użytkowników, programy wykonywalne i powszechne polecenia systemowe, które są używane przez wszystkich użytkowników w systemie. Zawiera takie polecenia jak ls, pwd, cat, mkdir, cd, mv, cp, du, df, tar, rpm, wc, history i inne.',
              'System cofiguration files. `/etc`: Zawiera pliki konfiguracyjne systemu',
              'home directories. `/home`: Zawiera katalogi domowe użytkowników',
              'optional or third party software. `/opt`: Zarezerwowany dla wszystkich oprogramowań i pakietów dodatkowych, które nie są częścią domyślnej instalacji',
              'temporary space, typically cleared od reboot. `/tmp`: Zawiera tymczasowe pliki i katalogi, które są tworzone podczas działania instancji serwera',
              'user related programs. `/usr`: Zawiera aplikacje i pliki używane przez użytkowników, a nie aplikacje i pliki używane przez system',
              'variable data, most notably log files. `/var`: Zawiera pliki, które mogą zmieniać rozmiar, takie jak pliki buforowania i pliki dziennika',
              'files needed to boot the operating system. `/boot`: Zawiera wszystkie pliki związane z rozruchem, takie jak grub.conf, obraz vmlinuz, czyli jądro itp',
              'mount point for CD-ROMSs. `/cdrom` lub `/mnt/cdrom`: Reprezentuje punkt montowania CD lub DVD',
              'control group hierarchy.  /cgroup`: Umożliwia organizowanie procesów w hierarchicznie uporządkowane grupy - cgroups',
              'device files, typically controlled by the operating system and the system administators. `/dev`: Zawiera pliki urządzeń',
              'system config files. ',
              'shared file systems. `/export`: Zwykle używany do udostępniania plików za pomocą NFS',
              'system libraries. Zawierają biblioteki współdzielone niezbędne do uruchomienia plików binarnych w `/bin` i `/sbin`',
              'sys lib, 64bit. Zawierają biblioteki współdzielone niezbędne do uruchomienia plików binarnych w `/bin` i `/sbin`',
              'used by the file system to store recovered files after a file system check has been performed. /lost+found`: Używany do przechowywania plików odzyskanych podczas sprawdzania systemu plików',
              'used to mount removable media like CD-ROMS. `/media`: Używany do montowania urządzeń wymiennych, takich jak pendrivey, dyski zewnętrzne itp',
              'used to mount external file systems. `/mnt`: Używany do montowania systemów plików',
              'optional or third party software. ',
              'provides info about running processes. `/proc`: Zawiera informacje o systemie i procesach',
              'home directory for the root account. `/root`: Jest to katalog domowy użytkownika root',
              'system administration binaries. `/sbin`: Zawiera pliki binarne niezbędne do uruchomienia systemu, przywrócenia, odzyskania lub naprawy systemu',
              'used to display information about SELinux. `/selinux`: Jeśli SELinux jest włączony, ten katalog zawiera pliki związane z SELinux',
              'contains data which is served by the system. `/srv`: Może zawierać dane serwisowe dostarczane przez ten system',
              'web servers files. Są to katalogi, które mogą zawierać dane dla serwerów WWW',
              'FTP files',
              'Used to display and sometimes configure the devices known to the Linux kernel. `/sys`: Zawiera informacje o urządzeniach, sterownikach i niektórych częściach jądra',





              ]








# i = 0
# while i < len(pytania):
#     nowe_pytanie = pytania[i]
#     print(f"Pytanie {i+1}: {nowe_pytanie}")
#     odpowiedz = input("Wprowadź odpowiedź: " + "\n")
#     print(f"Twoja odpowiedź: {odpowiedz}")
#     print(f"Prawidłowa odpowiedź: {odpowiedzi[i]}")
#     i += 1

i = 0
while i < len(pytania):
    nowe_pytanie = pytania[i]
    print("Pytanie", i+1, ":", nowe_pytanie)
    odpowiedz = input("Wprowadź odpowiedź: " + "\n")
    print("Twoja odpowiedź:", odpowiedz)
    print("Prawidłowa odpowiedź:", odpowiedzi[i], "\n")
    i += 1

sure = input("Naciśnij dowolny przycisk aby zakończyć działanie programu")
if sure == True:
    print("Kończymy program...")
