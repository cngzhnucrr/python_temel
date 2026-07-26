""" soru2:
   Problem: Aritmetik Dizi Filtreleme ve Analiz 
   Bir aritmetik dizinin ilk terimi a_1 = 7 ve ortak farkı d = 4'tür 
   (a_n = a_1 + (n-1)d).
   Bu dizinin ilk 100 terimini inceleyen bir Python programı yazın. 
   Kodunuz şu adımları gerçekleştirmelidir:
       Dizi Oluşturma: 
       İlk 100 terimi hesaplayıp aritmetik_dizi isimli bir listeye kaydedin.
       Koşullu Filtreleme: Bu listedeki elemanlardan 3 ile tam bölünebilen ancak 5 ile tam bölünemeyen sayıları
       ayıklayıp hedef_terimler adlı yeni bir listeye ekleyin.
       Çıktı & Analiz:Filtrelenen terimlerin listesini,Bu koşula uyan kaç tane terim olduğunu
       Bu terimlerin toplamını ekrana yazdırın.
    
    """
a1:int =7
d:int=4


def a(n):
    gen_ter=a1+(n-1)*d
    return gen_ter

i:int=1 
aritmetik_dizi=[]
while len(aritmetik_dizi)<100:
    i=i+1
    aritmetik_dizi.append(a(i))

hedef_terimler=[]

a:int=0
while a<100:
   for t in aritmetik_dizi:
        if t%3==0:
            if t%5!=0:
                print("python üçe tam bölüneni ve 5 e bölünemeyeni buldu",t)
                hedef_terimler.append(t)
                a=a+1
                
