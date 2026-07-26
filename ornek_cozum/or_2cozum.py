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
a1:int =7                       #dizinin ilk terimini tanımlayıp ilk değer ataması yaptık
d:int=4                         #ortak farkı integer türünde tanımlayıp ilk değer ataması yaptık


def a(n):                       #dizinin genel terimi için fonksiyon yapısı kurduk
    gen_ter=a1+(n-1)*d          #genel terimin yapısını oluşturduk 
    return gen_ter              #genel terimin ürettiği sonucu dışa döndürdük

i:int=1                         #döngü için sayac ayarladık
aritmetik_dizi=[]               #genel terimden üreteceğimiz her değeri kaydetmek için liste tanımladık
while len(aritmetik_dizi)<100:  #ilk 100 eleman için döngü kuralı tanımladık
    aritmetik_dizi.append(a(i)) #genel terimden üretilen her elemanı listeye ekledik
    i=i+1

hedef_terimler=[]               #kuralın geçerli olduğu elemanları eklemek için yeni bir liste tanımladık
for t in aritmetik_dizi:        #kuralı uygulamak için önceki listede oluştutulan elemanları listeyi tarayacak şekilde döngüye aldık
    if t%3==0:                  #3ile tam bölünebilen elemanlar 
        if t%5!=0:              #5 ile tam bölünemeyen elemanlar
            hedef_terimler.append(t) #kuralı sağlayan elemanları listeye ekle dedik
