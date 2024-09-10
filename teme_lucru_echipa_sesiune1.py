'''
Exercitiu 1
a. Defineste o variabila de tip int, numita 'latime'.
b. Defineste o variabila de tip string, numita 'descriere'.
c. Defineste 2 variabile de tip float, numite 'pret' si 'discount'.
d. Defineste o variabila de tip bool, numita 'initializat' care are valoarea True.
e. Printeaza variabilele definite la punctele anterioare.
'''

latime = 30
descriere = 'o masa de'
pret = 59.99
discount = 10
initializat = True

print(latime)
print(descriere)
print(pret)
print(discount)
print(initializat)

#exercitiu 2: Folosind o singura linie de cod, defineste 2 variabile, de tip int, cu valoarea 10

nota_mate = nota_fizica = 10

#exercitiu 3: Folosind o singura linie de cod, initializeaza/ defineste doua variabile de tip string cu valori diferite

marca, model = 'dacia' , 'duster'

'''
Exercitiu 4
Defineste doua variabile de tip string, numite 'nume', respectiv 'pret'.
Afiseaza in consola un mesaj care sa contina cele doua variabile.
'''

nume = 'colgate'
pret = '10'

print(nume + ' are pretul de ' + pret + ' lei')

'''
Exercitiu 5
Defineste doua variabile: nume (string) si varsta (int).
Folosind f-string, afiseaza in consola, o propozitie care sa contina cele doua variabile.
'''

nume = 'ionel'
varsta = 10

print(f'{nume} are varsta de {varsta} ani')

'''
Exercitiu 6
a. Defineste o variabila de tip int, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
b. Defineste o variabila de tip float, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
c. Defineste o variabila de tip string, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
d. Defineste o variabila de tip bool, afiseaz-o in consola. Afiseaza de asemenea si tipul acesteia.
'''

numar = 10
fractie = 10.5
text = 'minim'
corect =  True

print(numar)
print(type(numar))

print(fractie)
print(type(fractie))

print(text)
print(type(text))

print(corect)
print(type(corect))

'''
Exercitiu 7
a. Defineste o variabila de tip int. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de tip int de la punctul a, la tipul float si salveaza rezultatul intr-o alta variabila.
d. Afiseaza in consola tipul variabilei generate la punctul c.
'''

suprafata = 20
print(suprafata)
print(type(suprafata))

suprafata_noua=float(suprafata)
print(suprafata_noua)
print(type(suprafata_noua))

'''
Exercitiu 8
a. Defineste o variabila de tip string. Afiseaz-o in consola.
b. Afiseaza in consola tipul variabilei definite la punctul a, folosind functia type().
c. Converteste variabila de la punctul a, in int si salveaza rezultatul intr-o noua variabila.
Ruleaza programul.
Ce observi?
'''

mesaj = '15'
print(mesaj)
print(type(mesaj))

mesaj_nou = int(mesaj)
print(mesaj_nou)

'''
Exercitiu 9
Citeste de la tastatura un nume de produs.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
'''

denumire = input('cum se numeste produsul?')
print('numele produsului este ' + denumire)

'''
Exercitiu 10
Citeste de la tastatura un pret. Obliga utilizatorul sa introduca pretul ca si numar zecimal.
Salveaza rezultatul intr-o variabila.
Afiseaza un mesaj care sa contina variabila salvata.
'''

pret_unic = float(input('ce pret are produsul?'))
print('pretul produsului este: ' + str(pret_unic))


#Exercitii lucru in echipa

# variabila = zona din memoria masinii care retine date

text_nou = 'direct'
intreg_nou = 10
fractie_noua = 5.49
corect_nou = False

print(type(text_nou))
print(type(intreg_nou))
print(type(fractie_noua))
print(type(corect_nou))

fractie_noua = round(5.49)
print(fractie_noua)

print(f'{text_nou} are o valoare intreaga de {intreg_nou}, iar daca e fractie are valoarea de {fractie_noua}. Textul acesta nu este {corect_nou}')

nume_util = input('care e numele?')
prenume_util = input('care e prenumele')

complet = nume_util + prenume_util

total=len(complet)

print(f'numele lui are {total} caractere')

print('dorel')





