print("Merhaba! Vücut kitle endeksinizi kolayca hesaplayabileceğiniz BMI hesaplama aracına hoş geldimiz")
print("Aşağıdaki alanları doldurarak vücut kitle endeksinizi hesaplayabilirsiniz.")
isim = input("İsminizi girin ")
yas = int(input("Yaşınızı girin "))
boy = float(input("Boyunuzu girin "))
kilo = float(input("Kilonuzu girin "))
print(f"Merhaba {isim}! Vücut kitle endeksin hesaplandı. BMI değeriniz: {kilo / (boy * boy)}")

