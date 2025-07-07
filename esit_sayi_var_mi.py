#birinci cozum yolu :

""" def list(sayi1, sayi2, sayi3, sayi4, sayi5):
    sayilar=[sayi1, sayi2, sayi3, sayi4, sayi5]
    for i in sayilar:
        if sayilar.count(i) > 1:
            return "En az iki sayi birbirine esittir."
    return 
   
print(list(1,5,3,2,4))  """


#ikinci cozum yolu :

""" def list(sayi1, sayi2, sayi3, sayi4, sayi5):
    sayilar=[sayi1, sayi2, sayi3, sayi4, sayi5]

    for i in range(5):
        for j in range(i+1, 5):
            if sayilar[i]==sayilar[j]:
                print("En az iki sayi birbirine esittir.")
    return

list(1,2,3,4,3) """


#ucuncu cozum yolu :

""" def list(sayi1, sayi2, sayi3, sayi4, sayi5):
    sayilar=[sayi1, sayi2, sayi3, sayi4, sayi5]

    if len(sayilar) != len(set(sayilar)):
        print("En az iki sayi birbirine esittir.")
    else:
        return

list(1,2,3,4,3) """

#dorduncu cozum yolu :
def list(sayi1, sayi2, sayi3, sayi4, sayi5):
    sayilar = [sayi1, sayi2, sayi3, sayi4, sayi5]
    esitsayilar = set()

    for i in range(len(sayilar)):
        if sayilar[i] in esitsayilar:
            print("En az iki sayi birbirine esittir.")
            return
        esitsayilar.add(sayilar[i])
    
    print("Tum sayilar birbirinden farklidir.")

list(1, 2, 3, 4, 5)
list(1, 2, 3, 4, 3)
# Beşinci çözüm yolu:
def list(sayi1, sayi2, sayi3, sayi4, sayi5):
    sayilar = [sayi1, sayi2, sayi3, sayi4, sayi5]
    esitsayilar = set()

    for i in range(len(sayilar)):
        if sayilar[i] in esitsayilar:
            print("En az iki sayi birbirine esittir.")
            return
        esitsayilar.add(sayilar[i])

    print("Tum sayilar birbirinden farklidir.")
list(1, 2, 3, 4, 5)
list(1, 2, 3, 4, 3)
# Altıncı çözüm yolu:
def list(sayi1, sayi2, sayi3, sayi4, sayi5):
    sayilar = [sayi1, sayi2, sayi3, sayi4, sayi5]
    esitsayilar = set()

    for i in range(len(sayilar)):
        if sayilar[i] in esitsayilar:
            print("En az iki sayi birbirine esittir.")
            return
        esitsayilar.add(sayilar[i])

    print("Tum sayilar birbirinden farklidir.")
