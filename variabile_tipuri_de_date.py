'''
Obiective curs: variabile, tipuri de date
Setup functional
Principii de baza in programare
Primul meu program Python
Print statement
Comentarii
Variabile
Cele mai uzuale tipuri de date
Type casting
Intro in operatori
Input statement
Complexitatea unui string (index, length, metode ajutatoare)
'''

print('Hello World, PYTA20!')
# print('Luni')
# print(29)

# variabile
masina = 'Volvo'            #date de tip string
an_inmatriculare = 2000     #date de tip int
pret_masina = 15000.50      #date de tip float
inmatriculata = True        #date de tip boolean

# mihai si-a cumparat o masina volvo care este inmatriculata in anul 2000
print(f'Mihai si-a cumparat o masina {masina} care este inmatriculata in anul {an_inmatriculare}')
print(f'Pretul a fost {pret_masina} de lei')

pret_masina = 10000.459
print(f'Acum pretul este de {pret_masina} de lei')

# initializari variabile - pe acelasi rand cu valori diferite sau cu aceeasi valoare la 2 variabile diferite
nota_mate, nota_fizica, nota_sport = 9, 10, 8
print('nota mate:', nota_mate)
ore_romana = ore_mate = 4

#constantele se scriu cu litera mare
GRUPA = 'PYTA 20'
print (GRUPA)

nume = 'Popescu'
prenume = 'Maria'
nume_restaurant = "Mc'Donalds"

#concatenarea stringurilor
nume_complet = nume + prenume
print(nume_complet)
varsta = 20
# Maria are 20 de ani
print(f'{prenume} are {varsta} de ani')
print(prenume + ' are ' + str(varsta) + ' de ani') #concatenam date de tip string si facem un type casting (convertim date int in date string)

pret = '15'
print(type(pret))

pret = int(pret)
print(type(pret))

meniu = input('ce meniu doresti?') #in variabila meniu salvam datele preluate de la tastatura
print(meniu)
print(type(meniu))

pret_meniu = int(input('care e pretul meniului?'))
print(pret_meniu)
print(type(pret_meniu))

# maria a mers la Mc'donalds si a cumparat un meniu mediu, iar pretul a fost de 15

print(f'{prenume} a mers la {nume_restaurant} si a cumparat un meniu {meniu}, iar pretul a fost {pret_meniu} lei ')

print(prenume + ' a mers la ' + nume_restaurant + ' si a cumparat un meniu ' + meniu + ' , iar pretul a fost ' + str(pret_meniu) + ' lei')
