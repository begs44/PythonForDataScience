##################################################
# PYTHON ALIŞTIRMALAR
##################################################

########################################
# Soru 1: Veri Yapılarının Tiplerini İnceleme
########################################
# Veri yapılarının tiplerini inceleyiniz.

x = 8
type(x)  # int

y = 3.2
type(y)  # float

z = 8j + 18
type(z)  # complex

a = "Hello World"
type(a)  # string

b = True
type(b)  # boolean

c = 23 < 22
type(c)  # boolean

l = [1, 2, 3, 4]
type(l)  # list
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)  # dictionary

t = ("Machine Learning", "Data Science")
type(t)  # tuple
# Değiştirilemez
# Kapsayıcı
# Sıralı

s = {"Python", "Machine Learning", "Data Science"}
type(s)  # set
# Değiştirilebilir.
# Sırasız + Eşsiz
# Kapsayıcı

########################################
# Soru 2: String İfadeyi Düzenleme
########################################
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data info information, and information into insight."
text.upper().replace(", ", " ").replace(".", " ").split()

########################################
# Soru 3: Liste Üzerinde İşlemler
########################################
# Verilen liste için aşağıdaki görevleri yapınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu indexteki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
new_lst = lst[0:4]
new_lst

# Adım 4: Sekizinci index'teki elemanı silin.
lst.pop(8)
lst

# Adım 5: Yeni bir eleman ekleyiniz.
lst.append("J")
lst

# Adım 6: Sekizinci index'e "N" elemanını tekrar ekleyin.
lst.insert(8, "N")

########################################
# Soru 4: Sözlük (Dictionary) Üzerinde İşlemler
########################################
# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1: Key değerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy": ["England", 13]})
dict

dict["Daisy"][1] = 14
dict

# Adım 4: Key değeri Ahmet, value değeri [Turkey, 24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
dict

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
dict

########################################
# Soru 5: Tek ve Çift Sayıları Ayıran Fonksiyon
########################################
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları
# ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def func(list):
     çift_list = []
     tek_list = []

     for i in list:
          if i % 2 == 0:
               çift_list.append(i)
          else:
               tek_list.append(i)

     return çift_list, tek_list

çift, tek = func(l)  # Orijinal koddaki func(1) hatası func(l) olarak mantıksal düzeltildi.

########################################
# Soru 6: Enumerate İle Öğrenci Dereceleri
########################################
# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken
# son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumerate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, x in enumerate(ogrenciler):
     if i < 3:
          i += 1
          print("Mühendislik Fakültesi", i, ".öğrenci:", x)
     else:
          i -= 2
          print("Tıp Fakültesi", i, ". öğrenci:", x)

########################################
# Soru 7: Zip Kullanarak Ders Bilgilerini Bastırma
########################################
# Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve
# kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
     print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

########################################
# Soru 8: Küme (Set) Kapsama ve Fark İşlemleri
########################################
# Aşağıda 2 adet set verilmiştir. Sizden istenilen; eğer 1. küme 2. kümeyi kapsıyor ise ortak elemanlarını,
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume(set1, set2):
     if set1.issuperset(set2):
          print(set1.intersection(set2))
     else:
          print(set2.difference(set1))

kume(kume1, kume2)
kume(kume2, kume1)