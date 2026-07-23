'''
ARİTMETİK DİZİ PROBLEMİ

Problem:
İlk terimi a_1 = 3 ve ortak farkı d = 5 olan bir aritmetik dizinin:

İlk 10 terimini listeleyin.

terimini a_15 bulun.

İlk 15 terimin toplamını (S_15) hesaplayın.

Formüller:

Genel Terim: a_n = a_1 + (n - 1)d

Toplam Formülü: S_n = n/2 * (a_1 + a_n)
'''
'ilk terim'
a_1=3
'artış miktarı'
d=5

n=10

a_10=a_1+(n-1)*d
print("10.terim:", a_10)

s_10= (n/2)*(a_1+a_10)
print("ilk 10 terim toplamı:",s_10)

n=15
a_15=a_1+(n-1)*d
print("15.terim:", a_15)

s_15= (n/2)*(a_1+a_15)
print("ilk 15 terim toplamı:",s_15)