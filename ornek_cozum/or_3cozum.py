"""Problem: Aritmetik Dizi İle Müşteri İndirim AnaliziBir e-ticaret sitesi, sadakat programı kapsamında müşterilerine 
alışveriş sayılarına göre puan veriyor.Bir müşterinin kazandığı puanlar ilk alışverişten itibaren bir aritmetik dizi 
oluşturmaktadır:İlk alışverişte kazanılan puan: a_1 = 15 Her yeni alışverişte puan artış miktarı (ortak fark): d = 6 
Müşterinin toplam alışveriş sayısı: 40 (n = 40 )
Kodunuzdan şu adımları gerçekleştirmesi beklenmektedir:
1.Dizi Oluşturma Müşterinin 40 alışveriş boyunca her adimda kazandığı puanları (a_n = a_1 + (n-1)*d) hesaplayıp 
kazanilan_puanlar isimli bir listeye ekleyin.
2. Puan Segmentasyonu ve Kategorileştirmekazanilan_puanlar listesindeki her bir puanı inceleyip şu kurallara göre 
kategorilere ayırın ve ilgili yeni listelere ekleyin:
Puan 100 den küçükse: bronz_puanlar listesine ekleyin.
Puan  100 ile 200 arasında ise (100 ve 200 dahil): gumus_puanlar listesine ekleyin.
Puan 200 den büyükse: altin_puanlar listesine ekleyin.
3.Çıktı & AnalizEkrana sırasıyla şunları yazdırın:Bronz, Gümüş ve Altın kategorisine giren eleman sayılarını 
 (örneğin: "Gümüş kategoride X adet alışveriş var.").
 Müşterinin 40 alışveriş sonunda topladığı toplam puanı.Gümüş kategorideki puanların ortalamasını 
 (İpucu: Toplam / Eleman Sayısı)."""
 
 
 
 
 
a1:int=15                       #ilk alışverişte kazanılan puan 
d:int=6                         #puan artık miktarı

def a(n):                       #müşterinin her alışverişte kazandığı puan hesaplama fonksiyonu
    top=a1+(n-1)*d
    return top

kazanilan_puanlar=[]
bronz_puanlar=[]
gumus_puanlar=[]
altin_puanlar=[]

i:int=1
while i <40:
    kazanilan_puanlar.append(a(i))
    i=i+1

for i in kazanilan_puanlar:
    if i<100:
        bronz_puanlar.append(i)
    elif i>100 and i<200:
        gumus_puanlar.append(i)
    elif i>200: 
        altin_puanlar.append(i)


        