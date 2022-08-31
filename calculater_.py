from cgitb import reset
from pdb import Restart
import time
import webbrowser


print(""" Hesap makinesi""")


sayi1 = int(input("sayı1 giriniz :  "))
sayi2 = int(input("sayı2 giriniz :  "))
print(""" 
Toplama için 1 e basınız
Çıkarma için 2 ye basınız
Bölme için 3 e basınız
Çarpma için 4 e basınız
""")
islem = int(input("İşlem seçiniz :  "))

if (islem!=1,2,3,4):
    while(islem!=1) and (islem!=2) and (islem!=3) and (islem!=4):
     islem = int(input("İşlem seçiniz :  "))
     print("Yanlış tuşlama")

if (islem==1):
    print("Sonuç =  ",sayi1+sayi2)    
elif (islem==2):
    print("Sonuç = ",sayi1-sayi2)    
elif (islem==3):
    print("Sonuç = ",sayi1/sayi2)   
elif (islem==4):
    print("Sonuç = ",sayi1*sayi2)    
else:
    print("HATALI TUŞLAMA!")
time.sleep(2)

print("Çıkış yapılıyor...")
time.sleep(1)
print("Github profilime yönlendiriliyorsunuz")
time.sleep(2)
print("...")
print(webbrowser.open("https://github.com/metinz42") ,new=2)
time.sleep(1)







    



