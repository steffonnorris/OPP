class karealan():
    def __init__(self,yükseklik=1,genişlik=1) -> None:
        self.yükseklik=yükseklik
        self.genişlik=genişlik
    def Hesapla(self):
        return self.yükseklik * self.genişlik

Kare1 = karealan(15,10)
print(Kare1.Hesapla())