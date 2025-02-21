faiz=1.59
vade ="36"
krediAdi="ihtiyaç kredisi"


#print (vade+12)

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
faiz=str(faiz)
print(type(faiz))




#vade=input("lütfen sayı giriniz")
vade=21
print(type(vade))
print(int(vade)+12)


# String interolation
print("yenş vade "+str(vade))
print("yeni vade {vadesayisi} ".format(vadesayisi=vade))

isim="ahmet"
metin="merhaba {name}".format(name=isim)
print(metin)


metin2=f"hoşgeldiniz{isim}"


# listeler
# dögüler
# fonksiyonlar


krediler =["ihitayaç kredisi","taşıt kredisi","konut kredisii"]
print(type(krediler))

print(krediler[0])
print(len(krediler))

dizi=["ihtiyaç kredisi",10,5.2,True]
print(dizi)

krediler.append("özel kredi")
print(krediler)

krediler.pop()# defult olarak en sondaki elemanı siler
print(krediler)

krediler.append("taşıt kredisi")
krediler.remove("taşıt kredisi")
print(krediler)

krediler.extend(["y kredisi","c kredisi"])
print(krediler)


# ofr
# i =0 i<10
for i in range(10):
    print("xx")
    print(i)
print("***********")
for i in range(5,10):
    print(i)
print("***********")

for i in range(0,10,2):
    print(i)


krediler=["ihtiyaç","taşıt","konut"]
for kredi in krediler:
    print(kredi)

# sonsuz döngü

i=0
while i<10 :
    print("x")
    i+=1
print("y")

print("*******")
while(True):
    print("x")
    break




# fonksiyonlar
fiyat=100
indirim=20

def calculate():
    print(100-20)

calculate()
calculate()
calculate()

def calculate2(fiyat,indirim):
    print(fiyat-indirim)

calculate2(100,30)


def sayhello(name):
    print(f"merhba{name}")


sayhello("ahmet")


def calculateAndReturn(price,discount):
    return price-discount
print(calculateAndReturn(200,50))