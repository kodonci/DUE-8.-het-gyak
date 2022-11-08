#import jelszobekeres
#jelszobekeres.jelszo_ellenorzes()
#from jelszobekeres import *

#print('A megadott jelszó:', jelszo_ellenorzes(3, True))

#szam = input('Kérek egy számot: ')
#while szamjegyek(szam, True,'Nem számot adtál meg!'):
#    szam = input('Kérek egy számot: ')

from osztaly import *

dolg0 = Dolgozo('Imre', 30, 'puporkaimre@outlook.com')

dolg1 = Dolgozo('Karesz', 45, 'bubokaroly@yahoo.com')

print(dolg0.nev)
print(dolg0.kor)
print(dolg0.email)
print(dolg0.jelszo)

print(dolg1.nev)
print(dolg1.kor)
print(dolg1.email)
print(dolg1.jelszo)