sirul=str(input("Introduceti sirul de caractere format din literele mari ale alfabetului latin şi spaţiu: "))
sirul_I=''
sirul_II=''
sirul_III=''
print("Sirul initial este: ", sirul)
#a
for i in sirul:
    if (ord(i)>=65)and(ord(i)<=89):
        i=chr(ord(i)+1)
    sirul_I+=i
print('a) Sirul in care fiecare literă de la ’A’ până la ’Y’ se înlocuieşte prin următoarea literă din alfabet \n',sirul_I)
#b 
for i in sirul:
    if i=='Z':
        i="A"
    sirul_II+=i
print('b) Sirul in care fiecare literă ’Z’ se înlocuieşte prin litera ’A’ \n', sirul_II)
#c
for i in sirul:
    if i==' ':
        i="-"
    sirul_III+=i
print('c) Sirul in care fiecare spaţiu se înlocuieşte prin ’-’\n', sirul_III)