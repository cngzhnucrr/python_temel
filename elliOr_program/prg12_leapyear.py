# artık yılı kontrol eden program

"""
ARTIK YIL 

Artık yıl, Vikipedi verilerine göre 365 gün yerine 366 gün süren yıldır. 
Normalde 28 gün olan şubat ayına bir gün eklenmesiyle oluşur ve şubat 
29 gün çeker

Bir yılın 4 sayısına kalansız bölünmesi gerekir 
(Örneğin: 2016, 2020, 2024 yılları gibi).
Sonu çift sıfır (100'ün katı) olan yıllardan 
sadece 400 sayısına kalansız bölünebilenler artık yıldır 
(Örneğin: 2000 yılı artık yıldır ancak 1900 yılı artık yıl değildir).
"""

yil=int(input("lütfen yıl giriniz:"))

if(yil % 400==0)and (yil%100==0):
    print("{0} artık yıldır ".format(yil))

elif (yil%4==0) and (yil%100 !=0):
    print("{0} artık yıldır ".format(yil))

else:
    print("{0} artık yıl değildir".format(yil))