# lz78
def lz78(dizi):
    sozluk = {}
    kodlar = []
    veri = str(dizi)
    tutucu = ""
    indis = 0
    for i in veri:
        arakod = []
        if (i not in sozluk.values()):
            sozluk[indis] = i
            indis += 1
            arakod.append(0)
            arakod.append(i)

        if (len(arakod) != 0):
            kodlar.append(arakod)
    i = 0
    while (i < len(veri)):
        arakod = []
        tutucu = veri[i]
        while (tutucu in sozluk.values() and i != len(veri) - 1):
            i += 1
            tutucu += veri[i]
        else:
            sozluk[indis] = tutucu
            indis += 1
            arakod.append(indisGetir(sozluk, tutucu[:-1]))
            arakod.append(indisGetir(sozluk, tutucu[-1]))

        i += 1
        kodlar.append(arakod)

    return kodlar


def yazdir(dizi):
    a = []
    for i in dizi:
        for j in i:
            a.append(j)
    print(*a, sep="")


def indisGetir(sozluk, deger):
    for k, v in sozluk.items():
        if v == deger:
            return k


yazdir(lz78("FIRAT FIRAT FIRAT FIRAT FIRAT FIRAT FIRAT"))
yazdir(lz78("RAMAZAN CAN GÖLGEN RAMAZAN CAN GÖLGEN"))

