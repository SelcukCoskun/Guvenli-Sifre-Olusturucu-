import random

print("Güvenli ve Rastgele Şifre Oluşruma Programimiza Hoş Geldiniz.")

karakterler = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
    "q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",
    "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",
    "W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","#",
    "$","%","&","'","(",")","*","+","-",",",".","/",";",":","~"
]
k=0
while k==0:                                                                #Sonsuz döngüye aldım. while True şeklindede alınabilirmiş.
  uzunluk=int(input(("Şifreniz kaç karakter olsun=")))

  sifre=""                                                                 #Boş şifre oluşturdum.

  for i in range(uzunluk):
         sifre=sifre+random.choice(karakterler)                            #Boş şifreye ekleme yaparak şifremi doldurdum.

  print(sifre)

  yeni=input("Yeni şifre istiyormusunuz?y/n=")
  if yeni=="n" or yeni=="N":                                               #Daha fazla şifre istiyormu diye,kontrol ettim.
       break                                                               #NO yani Hayır derse döngüyü sonlandırdım.
