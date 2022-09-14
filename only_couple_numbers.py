import time
import webbrowser


print("programın amacı ;".capitalize()) 
print("ilk girdiğiniz sayıdan son girdiğiniz sayı arağılığındaki tek veya çift sayıları toplamak (ilk girdiğiniz sayı dahil değil)!".capitalize())
print("Eğer hangi değerlerin toplanmasını istemiyorsanız evet yazmak yerine boş bırakıp enter tuşuna basınız!".capitalize())
print(" ")
print(" ")
i =int(input("ilk sayıyı giriniz: "))
toplam=0
sayi = int(input("sayıyı giriniz(dahil) : "))
print(" ")
tek_sayilar = input("tek sayıların toplanmasını istiyorsanız evet yazınız :  ")
print(" ")
cıft_sayilar = input("çift sayıların toplanmasını istiyorsanız evet yazınız: ")

if ( tek_sayilar =="evet"):
     while(i<sayi):
          i+=1
          if(i%2==0):
               continue
          toplam= toplam + i
     print(f"tek sayıların toplamı = {toplam}")
elif(cıft_sayilar=="evet"):
     while(i<sayi):
          i+=1
          if(i%2==1):
               continue
          toplam+=i
     print("Çift sayıların toplamı :",toplam)


cıkıs= input("çıkmak istiyorsanız exit yazınız: ")

if (cıkıs=="exit"):
     print("çıkış yapılıyor")
     time.sleep(1)
     print("...")
     print("Github profilime yönlendiriliyorsunuz...")
     time.sleep(2)
webbrowser.open("https://github.com/metinz42",new=2)
time.sleep(2)
     



     
