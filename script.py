class Kitap:
    def __init__(self,isim,sayfa_sayisi):
        self.isim = isim
        self.sayfa_sayisi = sayfa_sayisi
    def sayfa_ekle(self,yeni_sayfa):
        self.sayfa_sayisi +=yeni_sayfa
    def bilgi(self):
        print(f"Kitap:{self.isim} Sayfa: {self.sayfa_sayisi}")
kitap1=Kitap("harry potter",59)
kitap1.sayfa_ekle(100)
kitap1.bilgi()
class Urun:
    def __init__(self,isim,fiyat,stok):
        self.isim = isim
        self.fiyat = fiyat
        self.stok = stok
class Sepet:
    def __init__(self):
        self.urunler={}
    def urun_ekle(self,urun,adet):
        if urun.stok >= adet:
           urun.stok -= adet
           if urun in self.urunler:
               self.urunler[urun]+=adet
           else:
               self.urunler[urun]=adet
        else:
            print("Stokta yoktur!")
    def urun_sil(self,urun):
        if urun in self.urunler:
            urun.stok += self.urunler[urun]
            del self.urunler[urun]
    def toplam_tutar(self):
        toplam=0
        for urun,adet in self.urunler.items():
            toplam+=urun.fiyat * adet
            return toplam
class BankaHesabi:
    def __init__(self,isim,bakiye):
        self.isim = isim
        self.bakiye = bakiye
        self.hareket_gecmisi=[]
    def para_yatir(self,yeni_bakiye):
        yeni_bakiye += self.bakiye
        self.hareket_gecmisi.append(f"{yeni_bakiye} TL yatırıldı")

    def para_cek(self,cekilen_para):
       if   self.bakiye >= cekilen_para:
            cekilen_para -= self.bakiye
            self.hareket_gecmisi.append(f"{cekilen_para} TL çekildi")
       else:
           print("Çekmek istediğiniz para yetersiz!")

    def ozet (self):
        print("hareketler")
        for h in self.hareket_gecmisi:
            print(h)
class Arac:
    def __init__(self,marka,gunluk_fiyat,musait_mi):
        self.marka = marka
        self.gunluk_fiyat = gunluk_fiyat
        self.musait_mi = True
class Musteri:
    def __init__(self,isim,kiraladigi_araclar ):
        self.isim = isim
        self.kiraladigi_araclar =[]
    def arac_kirala(self,arac):
        if arac.musait_mi:
            arac.musait_mi = False
            self.kiraladigi_araclar.append(arac)
        else:
            print("müsait araç yok!")
    def arac_iade_et(self,arac):
        if arac in self.kiraladigi_araclar:
            arac.musait_mi = True
            self.kiraladigi_araclar.remove(arac)
class Kutuphane:
    def __init__(self,isim,yazar,durum):
        self.isim = isim
        self.yazar = yazar
        self.durum = "müsait"
class Kullanici:
    def __init__(self,isim,aldigi_kitaplar):
        self.isim = isim
        self.aldigi_kitaplar =[]
class Kutuphane:
    def __init__(self):
        self.kitaplar=[]
    def kitap_ekleme(self,kitap):
        self.kitaplar.append(kitap)
    def kitap_odunc_verme(self,kullanici,kitap):
        if kitap.durum == "müsait" and len(kullanici.aldigi_kitaplar)<2:
           kitap.durum="ödünç"
           kullanici.aldigi_kitaplar.append(kitap)
        else:
            print("kitap alınamaz!")
    def iade_alma(self,kullanici,kitap):
        if kitap in kullanici.aldigi_kitaplar:
            kitap.durum="müsait"
            kullanici.aldigi_kitaplar.remove(kitap)
class Gorev:
    def __init__(self,baslik,aciklama,tamamlandi_mi):
        self.baslik = baslik
        self.aciklama = aciklama
        self.tamamlandi_mi = False
class Kullanici:
    def __init__(self,isim,gorevler):
        self.isim = isim
        self.gorevler = []
    def gorev_ekleme(self,gorevler):
        for g in gorevler:
            if g.baslik==gorevler.baslik:
                print("bu görev zaten var !")
                return
        self.gorevler.append(gorevler)
    def gorev_sil(self,gorevler):
        for gorev in self.gorevler:
            self.gorevler.remove(gorev)
    def gorev_tamamla(self,gorevler):
        if gorevler in self.gorevler:
           gorevler.tamamlandi_mi=True





















