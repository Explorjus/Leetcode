def max_sum_of_squares(num, suma):
    
    if suma > 9 * num:  # num cyfr daje max 9 * num, więc większej sumy nie da się zrobić

        return "" 

    wynik_lat = []

    for i in range(num): # petla wykona sie tyle razy ile wynosi num
        cyfra = min(9, suma)  # największa możliwa cyfra: max 9, ale nie więcej niż zostało
        wynik_lat.append(str(cyfra)) 
        suma -= cyfra # odejmowanie od sumy zeby nie przekroczyc sumy liczby koncowej

    return "".join(wynik_lat) # Sklejamy cyfry w jeden napis, np. ["9", "8"] -> "98"

print(max_sum_of_squares(7,11))
    

    
    
        

        

        

