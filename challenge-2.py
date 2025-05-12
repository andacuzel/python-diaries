ad = input("adınızı girin ")
yas = int(input("yaşınızı girin "))
if yas < 0:
    print(f"Merhaba {ad}, Yaşınız 0'dan küçük olamaz. Lütfen tekrar deneyin.")
elif yas > 100: 
    print(f"Merhaba {ad} Yaşınız 100'den büyük olamaz")
else:
    print(f"Merhaba {ad}, hoş geldiniz")

boy = float(input("Boyunuzu girin - örnek: 1.70 "))
kilo = float(input("kilonuzu girin "))
bmi = kilo / (boy * boy)
print(f"Sevgili {ad} vücut kitle endeksin hesaplandı. BMI değerin = {bmi}")
if bmi < 18.5:
    print("BMI verinize göre vücut tipiniz: Zayıf")
    print("Vücut tipinize göre makale önerimiz: https://www.nhs.uk/live-well/eat-well/ ")
elif bmi < 25:
    print("BMI verinize göre vücut tipiniz: Normal")
    print("Sağlıklı beslenmeye devam ederek bu değerleri koruyabilmek için ipuçları: https://www.cdc.gov/healthyweight/index.html")
elif bmi < 30: 
    print("BMI verinize göre vücut tipiniz: Fazla kilolu")
    print("Fazla kilolular için egzersiz rehberi: https://www.healthline.com/health/fitness-exercises-for-beginners ")
else:
    print("BMI verinize göre vücut tipiniz: Obez") 
    print("Dünyada her 8 kişiden biri obez. Bu oranı düşürmek elimizde. Sizin için detaylı bilgi: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight")
    
    

 
