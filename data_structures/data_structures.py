##################################################
# VERİ YAPILARI (DATA STRUCTURES)
##################################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set

########################################
# Veri Yapılarına Giriş ve Hızlı Özet
########################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
type(3 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter", "Age": 36}
type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.

########################################
# Sayılar (Numbers): Int, Float, Complex
########################################

a = 5
b = 10.5

a * 3
a / 7
a * b / 10
a ** 2

##############################
# Tipleri değiştirmek
##############################

int(b)
float(a)

int(a * b / 10)

c = a * b / 10

int(c)

########################################
# Karakter Dizileri (Strings)
########################################

print("John")
print('John')

name = "John"
name = 'John'

##############################
# Çok satırlı karakter dizileri
##############################

long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

##############################
# Karakter dizilerinin elemanlarına erişmek
##############################

name
name[0]
name[3]

##############################
# Karakter dizilerinde slice işlemi
##############################

name[0:2]

long_str[0:10]

##############################
# String içerisinde karakter sorgulamak
##############################

long_str
"veri" in long_str
"Veri" in long_str
"bool" in long_str

########################################
# String (Karakter Dizisi) Metodları
########################################

dir(str)

##############################
# Len
##############################

name = "john"
type(name)
type(len)

len(name)
len("bengüsu")
len("python")

##############################
# Upper() & lower(): Küçük-büyük dönüşümleri
##############################

"python".upper()
"python".lower()

# type(upper)

##############################
# Replace: Karakter değiştirir
##############################

hi = "Hello AI Era"
hi.replace("l", "p")

##############################
# Split: Böler
##############################

"Hello AI Era".split()

##############################
# Strip: Kırpar
##############################

"ofofof".strip()
"ofofof".strip("o")

##############################
# Capitalize: İlk harfi büyütür
##############################

"foo".capitalize()

########################################
# Liste (List)
########################################
# - Değiştirilebilir.
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "c", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])
type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]

########################################
# Liste Metodları (List Methods)
########################################

dir(notes)

##############################
# Len: Boyut bilgisi
##############################

len(notes)
len(not_nam)

##############################
# Append: Eleman ekler
##############################

notes.append(100)

##############################
# Pop: İndexe göre siler
##############################

notes.pop(0)

##############################
# Insert: İndexe ekler
##############################

notes.insert(2, 99)

########################################
# Sözlük (Dictionary)
########################################
# - Değiştirilebilir.
# - Sırasız. (3.7 sürümünden sonra sıralı)
# - Kapsayıcı.
# - Key-value formatında çalışır.

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["REG"]
dictionary["CART"][1]

##############################
# Key sorgulama
##############################

"REG" in dictionary

##############################
# Key'e göre value'ya erişmek
##############################

dictionary["REG"]
dictionary.get("REG")

##############################
# Value değiştirmek
##############################

dictionary["REG"] = ["YSA", 10]

##############################
# Tüm key'lere erişmek
##############################

dictionary.keys()

##############################
# Tüm value'lara erişmek
##############################

dictionary.values()

##############################
# Tüm çiftleri tuple halinde listeye çevirme
##############################

dictionary.items()

##############################
# Key-value değerini güncellemek
##############################

dictionary.update({"REG": 11})

##############################
# Yeni key-value eklemek
##############################

dictionary.update({"RF": 10})

########################################
# Demet (Tuple)
########################################
# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

# t[0] = 99  # Tuple değiştirilemez olduğu için hata verir.

t = list(t)
t[0] = 99
t = tuple(t)

########################################
# Set
########################################
# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

##############################
# Difference(): İki kümenin farkı
##############################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)

# set2'de olup set1'de olmayanlar.
set2.difference(set1)

##############################
# Symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
##############################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

##############################
# Intersection(): İki kümenin kesişimi
##############################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

##############################
# Union(): İki kümenin birleşimi
##############################

set1.union(set2)
set2.union(set1)

##############################
# Isdisjoint(): İki kümenin kesişimi boş mu?
##############################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)

##############################
# Issubset(): Bir küme diğer kümenin alt kümesi mi?
##############################

set1.issubset(set2)
set2.issubset(set1)

##############################
# Issuperset(): Bir küme diğer kümeyi kapsıyor mu?
##############################

set2.issuperset(set1)
set1.issuperset(set2)