nums = [1,2,3]

kwadraty = []

for x in nums:  
    kwadraty.append(x * x) #mnozy kaza liczbe przez siebie dzieki temu wszystko jest kwadratem

kwadraty.sort()

ile_minusow = len(kwadraty) // 2 #okresla liczbe minusow w liscie

wynik = 0
for i in range(len(kwadraty)):  
    if i < ile_minusow: #najmniejsze liczby musza dostac minus 
        wynik -= kwadraty[i]
    else: #najwieksze nie moge dostac minusu zeby wynik byl jak najwiekszy
        wynik += kwadraty[i]

print(wynik)
	