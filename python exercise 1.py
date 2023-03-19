   # Python Alıştırmalar Ödevi #
###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
# Veri Yapıları : Sayısal(int,float,complex),string,boolen,tuple,set

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

#Liste yapısı : kapsayıcıdır, değiştirilebilir ve sıralıdır
l = [1, 2, 3, 4,"String",3.2, False]
type(l)

#dictionary(sözlük) yapısı : key-value çiftlerinden oluşur, sırasız,kapsayıcı,değiştirilebilirdir ama key değeri unique tir.
d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

#tuple yapısı: sözlüklere kapsayıcılık ve sıralı olma yönünden  benzer ama değişitirilemez
t = ("Machine Learning", "Data Science")
type(t)
t[0]

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text.upper()
text.upper().replace(","," ").replace("."," ").split()

# tüm harfleri kucuk harfe cevirmek istediğimizde ise
text.lower()

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

#listenin eleman sayısını bulmak için
len(lst)

#sıfırıncı ve onuncu index'teki elemanları çağırmak için
lst[0]
lst[10]

#Sıfırıncı ve onuncu indexi tek listede istersek
[lst[0], lst[10]]
[lst[0] + lst[10]]

#Verilen liste üzerinden ["D","A","T","A"] listesi oluşturmak
lst[0:4]

#Sekizinci index'teki elemanı silin.
lst.pop(8)
lst

#Yeni bir eleman ekleyin.
lst.append("miuul")

# Adım 6: Sekizinci index'e  "N" elemanını tekrar eklemek için (hangi indexe alacağım, hangi nesneyi alacağım?)
lst.insert(8,"N")

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız. (dict = {key: value} çiftinden oluşur)
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

#Key değerlerine erişiniz.
dict.keys()
#  Value'lara erişiniz.
dict.values()

# Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.(güncellemek için update)
dict.update({"Daisy": ["England",13]})

# Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"AHMET": ["TURKEY",24]})

#Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
l = [2,13,18,93,22]
#fonksiyon yazalım

cift=[]
tek=[]
def sayı(liste):
    for i in liste:
        if i % 2 ==0:
            cift.append(i)
        else:
            tek.append(i)
    return cift,tek

 cift,tek = sayı(l)

#List Comp ile yapmak istersek

cift_sayı = [i for i in l if i % 2 == 0]
tek_sayı = [i for i in l if i % 2 != 0]

#----------------------------------------

cift_sayilar=[]
tek_sayilar=[]
[cift_sayilar.append(i) if i % 2 == 0  else tek_sayilar.append(i) for i in l  ]

#ikisini bir listede ayrı listeler halinde görmek istersek:
tum_sayılar =[[],[]]
[tum_sayılar[0].append(i) if i % 2 == 0  else tum_sayılar[1].append(i) for i in l  ]

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
#Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
#enumarete kullanarak çözümü
for i,name in enumerate(ogrenciler):
    if i < 3:
        i+=1
        print("Mühendislik Fakültesi", i, ". Ogrencisi:",name)

    else:
        i-=2
        print("Tıp Fakültesi", i , ". Ogrencisi:",name)

# Enumerate kullanmadan çözümü:

for i in range(len(ogrenciler)):
    if i < 3:
        print("Mühendislik Fakültesi", i+1 , ". Ogrencisi:", ogrenciler[i])

    else:
        print("Tıp Fakültesi", i-2 , ". Ogrencisi:", ogrenciler[i])


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
#Kredisi ...  olan ...  kodlu dersin kontenjanı ... kişidir."

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

# list(zip(kredi,ders_kodu,kontenjan))
# zip(kredi,ders_kodu,kontenjan)

for krd,kod,kont in zip(kredi,ders_kodu,kontenjan):
    print(f"Kredisi {krd}  olan {kod}  kodlu dersin kontenjanı {kont} kişidir.")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
#Eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

#Fonksiyon yazalım

def kumeler(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


kumeler(kume1,kume2)