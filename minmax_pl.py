#Przypisanie poniżej dwóch wartości None do zmiennej jest jednym ze sposobów zresetowania jej do pierwotnego, pustego stanu.
largest = None
smallest = None
#Włączenie "wiecznej" pętli poniżej
while True:
    #Warunek przerwania działania pętli
    num = input("Enter a number: ")
    if num == "done":
        break
    #Warunek kiedy ma liczyć
    try:
        num = int(num)
    #Jeśli błędna wartość wystąpi, zostanie pominięta i zostanie wydrukowany o tym komunikat
    except:
        print ("Invalid input")
        continue
    #Wynajdowanie wartości najmniejszej zaczynając od stanu pustego
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    #Wynajdowanie wartości największej zaczynając od stanu pustego
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
#Drukowanie obydwu liczb: Najmniejszej i Największej z określeniem ich
print("Maximum is", largest)
print("Minimum is", smallest)
    