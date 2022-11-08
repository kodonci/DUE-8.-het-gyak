class Dolgozo():
    nev = ''
    kor = None
    email = ''
    jelszo = ''

    def __int__(self, nev, kor, email, jelszo=''):
        self.nev = nev
        self.korkerdes()
        self.email = email
        self.jelszo = '123'

    def korertek(self, ertek):
        self.kor = ertek

    def korkerdes(self):
        kor = input('Kérem a korodat: ')
        hiba = True
        for i in range(len(kor)):
            if kor[i].isnumeric():
                hiba = False
                break
        if hiba:
            print('Nem érvényes kor!')
            self.kor = 0
        else:
            self.kor = kor
