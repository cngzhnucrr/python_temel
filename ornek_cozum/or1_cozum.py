"""soru:
    genel terimi 
    an=5+9+13+17+21+....+(4n+1)
    olan dizinin
    ilk üç terim toplamını bulunuz.
"""
"""  çözüm 1  """
"""
n=2 
an=4*n+1
top:int=0
for i in range(n):
    an=4*(i+1)+1
    top=top+an
    if (i+1)==n:
        print(top)
        break 
"""
""" çözüm 2"""    
top:int=0
n=int(input("ilk kaç terim toplamını istiyorsunuz: "))
def a(n):
     t=n*4+1
     return t

for i in range(1,n):
    top=top+a(i)
    print(f"ilk {i} terim toplamı:{top}")
    
print(f"ilk {n} terim toplamı: {top} sonucudur.")

        