
nums = [1, 4, 6,5 ,45, 3, 6, 7, 4, 2]
freq = {}
        
for num in nums:

    freq[num] = freq.get(num, 0) + 1 #get pobiera warosc ze slownika ale moze przez zapisac przez "="
                        #num jest kluczem a 0 waroscia ktora zostanie domyslnie przypisana 
                        #+1 dodaje nawet do zera aby liczyc ilosc wystapien
        
max_frequency = 0
total_frequencies = 0
        
for frequency in freq.values():
    
    if frequency > max_frequency:
        max_frequency = frequency
        total_frequencies = frequency
    
    elif frequency == max_frequency:
        total_frequencies += frequency
print(freq)
print(total_frequencies)

