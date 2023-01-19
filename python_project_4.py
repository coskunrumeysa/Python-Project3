# Firstly , introduce who writeen this program.
__author__ = "Rumeysa Coskun"

# Secondly, define 4  variable .

isim =input("Lutfen isminizi giriniz:")
soyisim =input("Lutfen soyisminizi giriniz:")
yas= int(input("Lutfen yasınızı giriniz:"))
il =input("Lutfen yasadiginiz ili giriniz:")
adres ="A Sokak"
ilkharf="r"


#Thirdly , we want to leran type the variable and length of variable.

print("İsim veri tipi :",type(isim))
print("Soy isim veri tipi :", type(soyisim))
print("Yas veri tipi :", type(yas))
print("İl veri tipi :", type(il))
print("Adres veri tip :", type(adres))
print("İlk harf veri tip:", type(ilkharf))

# Fourthly we want to learn legth of value of variables.

print("İsim degiskenini degeriin uzunlugu :", len(isim))
print("Soy isim degiskenini degeriin uzunlugu :", len(soyisim))

#print("Yas degiskenini degeriin uzunlugu :", len(yas)) , int variable asnt any length.

print("İl degiskenini degeriin uzunlugu :", len(il))
print("Adres degiskenini degeriin uzunlugu : ", len(adres))
print("İlk harf degiskenini degeriin uzunlugu : ", len(ilkharf))

#Print summutaion of te variable length.

print("Sum legth of isim,soyisim ve adres", len(isim)+len(soyisim)+len(adres))

#Print a function etried variable print.

def ozluluk_bilgi(isim, soyisim ,il):
    print("Girdiginz   :",isim)
    print("Girdiginiz :",soyisim)
    print("Girdiginiz sehir:" ,il)
ozluluk_bilgi(isim,soyisim,il)

# İf we want to use one line comment using # symbol.

""" 
 if we want to use multiple line
  comment using these symbols.
  
"""

if isim=="rumeysa":
    print("Hosgeldiniz:",isim,"hanım")

elif isim=="rümeysa":
    print("osgeldiniz:" ,isim,"hanım")

else:
    print("Lutfen ya rumeysa ya rümeysa ismini giriiz.")

print("Rumeysa Coskun"\n)