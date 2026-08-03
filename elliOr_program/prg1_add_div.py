""" aritmetik bölme ve toplama işlemi """
""" toplama işlemi"""
num1=float(input("birinci sayiyi giriniz:"))
"kullanıcıdan alınan giriş kayan noktalı sayı türüne çevrildi"
num2=float(input("ikinci sayiyi giriniz:"))
"kullanıcıdan alınan giriş kayan noktalı sayı türüne çevrildi"


sum_result=num1+num2
" sayıların toplamı değişkene atandı "
print("toplam:",num1,"+",num2,"=",sum_result)

"""  bölme işlemi """
if num2==0:
    print("bölme işlemi yapılamaz")
else:
    bol=num1/num2
    tam_bol=num1//num2
    print(f"normal bölme(/) sonucu:{bol}")
    print(f"tam bölme(//) sonucu:{tam_bol}")
