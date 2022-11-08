def hossz(jelszo, jelszohossz):
    hiba = False
    if len(jelszo) < jelszohossz:
        print(f'Nem elég hosszú a beírt jelszó! (minimum {jelszohossz} karakter)')
        hiba = True
    return hiba


def szamjegyek(jelszo, kellszam, uzenet):
    if kellszam:
        hiba = True
        for i in range(len(jelszo)):
            if jelszo[i].isnumeric():
                hiba = False
                break
        if hiba:
            print(uzenet)
        return hiba
    else:
        hiba = False
        return hiba


def nagybetu(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].isupper():
            hiba = False
            break
    if hiba:
        print('A jelszó nem tartalmaz nagybetűt!')
    return hiba


def kisbetu(jelszo):
    hiba = True
    for i in range(len(jelszo)):
        if jelszo[i].islower():
            hiba = False
            break
    if hiba:
        print('A jelszó nem tartalmaz kisbetűt!')
    return hiba


def jelszo_ellenorzes(jelszohossz, kellszam):
    hibakod = 1
    while hibakod != 0:
        hibakod = 0
        psw = input('Kérek egy jelszót: ')
        if hossz(psw, jelszohossz):
            hibakod += 1
        if szamjegyek(psw, kellszam):
            hibakod += 1
        if nagybetu(psw):
            hibakod += 1
        if kisbetu(psw):
            hibakod += 1
    print('\nSikerült jó jelszót választania!')
    return psw


def jelszokeres():
    jelszo1 = jelszo_ellenorzes()
    jelszo2 = input('\nKérem ismételten a jelszót!')
    probalkozas = 1

    while jelszo1 != jelszo2:
        if probalkozas == 4:
            break
        jelszo2 = input('\nNem egyforma a két jelszó! Ismét add meg a jelszót: ')
        probalkozas += 1

    if probalkozas == 4:
        print("\nNem sikerült jelszót választani, a regisztrációnak vége!")
    else:
        print('\nJelszavak egyeznek, sikeres jelszóbeírás, sikeres regisztráció!')
    with open('jelszo.txt', 'a', encoding='utf-8') as user:
        user.write(';' + jelszo1)


def felhasznalo():
    print("\nA következőkben a regisztrációra kerül sor. Ehhez szükség lesz egy e-mail címre és egy jelszóra.")
    felhasznalonev = input("\nKérem az e-mail címedet: ")

    while '@' not in felhasznalonev or '.' not in felhasznalonev or ' ' in felhasznalonev:
        print("Nem megfelelő az e-mail címed!")
        felhasznalonev = input("\nKérem az e-mail címedet: ")
    with open('jelszo.txt', 'w', encoding='utf-8') as user:
        user.write('\n' + felhasznalonev)


def beleptetes():
    print('BELÉPTETÉS')
    with open('jelszo.txt', 'r', encoding='utf-8') as fajl:
        user_fajl = fajl.readlines()
        for sor in fajl:
            user_fajl.append((sor.strip().split(';')))

    user = input('Kérem a felhasználónevet: ')
    van = False
    i = 0
    for i in range(len(user_fajl)):
        if user_fajl[i][0] == user:
            van = True
            break
    if van:
        jelszo = input('Kérem a jelszót: ')
        probalkozas = 1
        while jelszo != user_fajl[i][1]:
            if probalkozas == 3:
                break
            print('Nem megfelelő jelszó!')
            jelszo = input('Kérem ismét a jelszót: ')
            probalkozas += 1
            if probalkozas == 3:
                print('Belépés sikertelen! Túl sok próbálkozás!')
            else:
                print('Sikeres belépés!')
    else:
        print('Nincs ilyen felhasználó!')


# Program indul
if __name__ == '__main__':
    felhasznalo()
    jelszokeres()
    beleptetes()