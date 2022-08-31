#Start


import webbrowser
import time



print("Merhaba Hoşgeldiniz Ehliyet alabilirmiyim sorusuna cevap arıyorsanız doğru yerdesiniz")
print("lütfen aşağıya bilgilerinizi doğru giriniz yaş bilgisini girerken rakamları kullanınız".upper())
print(("programmer : Metin Öztaş"))
isim = input("isim : ")
yas = int(input("yaş : "))
egitim = input("eğitim düzeyiniz : ")

if (yas>=18) and (egitim == "lise"):
    print(isim.capitalize(),"ehliyet alabilirsin.")
elif (yas>=18) and (egitim == "üniversite"):
    print(isim.capitalize(),"ehliyet alabilirsin")
elif (yas<18) and (egitim=="ortaokul"):
    print(isim.capitalize(),"yaş ve eğitim durumunuzdan kaynaklı ehliyet alamıyorsun.")
elif (yas<18) and (egitim=="ilkokul"):
    print(isim.capitalize(),"yaş ve eğitim durumunuzdan kaynaklı ehliyet alamıyorsun.") 
elif (yas<18) :
    print(isim.capitalize(),"yaşın ehliyet almaya yetmiyor.")
elif (egitim=="ortaokul"):
    print(isim.capitalize(),"eğitim düzeyinden dolayı ehliyet alamazsınız.")
elif (egitim=="ilkokul"):
    print(isim.capitalize(),"eğitim düzeyinden dolayı ehliyet alamazsınız.")
else:
    print("Bilgileri kontrol ediniz yanlış veya eksik tuşladınız.")

cıkıs =int(input("çıkış için 1 e basınız: "))
if (cıkıs==1):
    print("çıkış yaptınız")
    time.sleep(1)
    print("Github profilime yönlendiriliyorsunuz...")
    time.sleep(2)
webbrowser.open("https://github.com/metinz42",new=2)
time.sleep(2)           # Delay for 2 second

# Stop
    


  

    
      
