def lz77(string, arama_tamponu_uzunlugu):
    dizi = strToList(string)
    ileri_tampon = dizi[arama_tamponu_uzunlugu:]
    arama_tamponu = dizi[:arama_tamponu_uzunlugu]
    kodlar = []#sıkıştırılmış verilerimizin kodlarının tutulduğu dizi
    
    #ileri tamponu küçülterek işlemlerimizi gerçekletireceğiz
    #bunun nedeni eşleşen verilerin ileri tampondan atılarak tekrar 
    #karsilastirma yapmak
    while(len(ileri_tampon) != 0):
        dizi = karsilastir(ileri_tampon, arama_tamponu)
        #karsilastir fonksiyonu a ve en olmak üzere iki adet değerin
        #olduğu bir dizi döner a-> arama tampnonunda en büyük eşleşmenin
        #başlangıç indisidir bunu kodlamada kullanacağız
        #en-> en buyuk eslesme uzunluğudur. 
        en_buyuk_eslesme = dizi[0]
        baslangic_indexi = dizi[1]
        
        kodlar.append(kodla(en_buyuk_eslesme, baslangic_indexi, arama_tamponu, ileri_tampon))
        
        #tampon kucult fonksionu ile ileri tamponumuzu küçültüyoruz
        #ve geriye eşleşmemiş veriler kalacak
        try:
            ileri_tampon = tamponKucult(ileri_tampon, en_buyuk_eslesme)
        except:
            pass
    print("   Kodlaması : "+str(kodlar))
#bu fonksiyon arama tamponu içerisindeki ileri tampon ile eşleşen
#en büyük eşleşmeyi bize verecek
def karsilastir(ileri_tampon, arama_tamponu):
    eslesme = []
    en_buyuk_eslesme = []
    
    j = len(arama_tamponu)-1 #arama tamponundan geriye doğru saymak için
    i = 0
    k = 0
    a = 0 #arama tamponundaki en büyük eşleşmenin başlangıç indexi

    #***********************************************************
    while(j>=0):
        eslesme = []
        k = j
        while(ileri_tampon[i] == arama_tamponu[k]):
            eslesme.append(ileri_tampon[i])
            k+=1
            i+=1
            if(i >= len(ileri_tampon) or k >= len(arama_tamponu) ):
                break
            
        i = 0    
        j -= 1
        if(len(en_buyuk_eslesme) < len(eslesme)):
            en_buyuk_eslesme = eslesme
            
    #***********************************************************
    
    #buradan ...
    try:
        x = arama_tamponu.index(en_buyuk_eslesme[0])
        while(x<=len(arama_tamponu)):
            if en_buyuk_eslesme==arama_tamponu[x:x+len(en_buyuk_eslesme)]:
                a=x
                break
            x+=1
    except:
        pass
    #buraya kadar olan kısmın amacı
    #arama tamponunda en büyük eşleşmenin başlangıç indexini bulmak(a)

    sonuc=[en_buyuk_eslesme, a]
    return(sonuc)
        
def kodla(en_buyuk_eslesme, baslangic_indexi, arama_tamponu, ileri_tampon):
    arakod = []

    arakod.append(len(arama_tamponu) - baslangic_indexi)#burada kodlamadaki kaç adım geriye gitmemiz
                                         #gerektiği kısımını hesaplıyoruz
    arakod.append(len(en_buyuk_eslesme))#burada kodalamadaki en eşleşmenin uzunluğunu belirtiyoruz       
    
    if(ileri_tampon != en_buyuk_eslesme):#eğer bütün elemanlar eşit değil ise koda bazı eklemeler yapıyoruz
        
        # ileri tamponda eşleşmemiş elemanlar var ise lz77 algoritmasındaki kodlamaya göre 
        #ileri tampondaki eşleşen sıralı dizinin hemen sonundaki elemanıda kodlamaya katıyoruz
        arakod.append(ileri_tampon[len(en_buyuk_eslesme)])

    elif(ileri_tampon == en_buyuk_eslesme):
        arakod.append(ileri_tampon[ileri_tampon.index(ileri_tampon[-1])])

    
    
    return arakod

def tamponKucult(ileri_tampon, en_buyuk_eslesme):
    i=0
    if(len(ileri_tampon) != 0):
        while(i<len(en_buyuk_eslesme)+1): #buradaki+1 'in sebebi kodlanırken alınan son elemanı da listeden silmektir. 
            ileri_tampon.pop(0)
            i+=1
        return ileri_tampon


def strToList(string): #algoritmanın içine liste yerine string girişi yapabilmemiz için
                       #liste fonksiyonlarını string ifadenin alması gerekir.
    liste = []
    for i in string:
        liste.append(i)
    return liste
    
#strToList Fonksiyonu lz77 nin içine de ya

print("______________________________________________________")
print()
lz77("RAMAZAN CAN GOLGEN",11)
print("______________________________________________________")
print()
lz77("abracadabraaa",7)
print("______________________________________________________")
print()
lz77("AAAAAAAAAAAAAAAAAAA",10)
print("______________________________________________________")
print()
lz77("FIRATFIRATFIRA",9)


