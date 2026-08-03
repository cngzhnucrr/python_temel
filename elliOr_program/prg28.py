"""Özyineleme (recursion) kullanarak bir sayının faktöriyelini hesaplayan bir Python programı yazın.
Negatif olmayan bir tam sayının ( n ) faktöriyeli, ( n )'den küçük veya ( n )'e eşit olan tüm pozitif tam sayıların çarpımıdır.
 ( n! ) ile gösterilir ve şu şekilde tanımlanır:
Örneğin:
 1 olarak tanımlanır.
Faktöriyeller matematikte, özellikle de kombinatorik ve olasılık alanlarında, 
bir dizi elemanın kaç farklı şekilde sıralanabileceğini veya seçilebileceğini hesaplamak için yaygın olarak kullanılır."""


"""
fac:int=0
say:int=1
i:int=0
while i<n :
    fac=(n-i)
    say=say*fac
    i+=1
print(say)
"""
def fc(n):             # fonskiyon tanımlıyoruz 
    say:int=1          # değer atamalarını ve tanımları lokalde yapıyoruz 
    i:int=0
    if n==0:           # 0! şartına özel atama yapıyoruz ki program çökmesin 
        say=1
    else:
        while i<n:
            say*=(n-i) # faktöriyel işlemini burada tamamlıyoruz
            i+=1
    return say

print(fc(6))           # fonksiyonu çağırarak işi bitiriyoruz 