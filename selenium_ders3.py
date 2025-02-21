# sınıflar==> claslar
# modüller
# paketler

class  Human:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "str yapısından geldim "
    def talk(Self,sentence):
        print(f"Human: {sentence}")
    def walk(Self):
        print("Human is walking.")


# instance == örnek
human1=Human("ahmet")
human1.walk()
human1.talk("ahmet")

human2=Human("mehmet")
human2.talk("selam")
human2.walk()
print(human2)
