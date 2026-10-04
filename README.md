# Dolmuş Müsait Yer Yok Simülatörü

> Resmi slogan: **Yer yok.** Gayriresmi ek: **ısrar edersen var.**

Bu depo, Türkiye'nin en ciddi ulaşım kuramını yazılıma çevirir. Dolmuş hiçbir zaman boş değildir. Dolmuş hiçbir zaman tam dolu da değildir. Dolmuş, Schrödinger'in koltuğudur: kapı açılana kadar hem yoktur hem de şoförün kaşının altındadır.

Patates içermez. Patates durakta inmiştir. Biz bindik.

## Ne işe yarar

`dolmus.py` gerçekten çalışır. Kapasiteyi sayar, “müsait yer yok” der, sen ısrar edersen termodinamik yasalarını eğer ve bir kişilik yer açar. Israr etmezsen kapı yüzüne kapanır ve bir sonraki araç da aynı cümleyi söyler. Bu bir bug değil, folklordur.

## Kurulum

Python 3 yeter. Bağımlılık yok. Çay da yok, o başka deponun işi değil, bizim işimiz de değil.

```bash
python dolmus.py
python dolmus.py --yolcular 14 --kapasite 14 --israr 3
python dolmus.py --demo
```

## Fizik kanunları

1. Kapı ağzında duran kişi yarım koltuk sayılır, tam ücret öder.
2. “Biraz ilerleyin” cümlesi yerçekimini %12 azaltır.
3. Şoför aynaya bakmadan karar verirse karar geçerlidir.
4. Müsait yer, ancak ısrar katsayısı eşiği aşılınca var olur.
5. İnen yolcu, binen yolcudan her zaman daha yavaştır. Bu evrenseldir.

## Katkı

Pull request açabilirsin. İnceleme sırasında “yer yok” denebilir. Israr edersen merge olur.

## Lisans

Kapı açık olduğu sürece serbest. Kapı kapanınca şoför konuşur.

---

### DAMGA / İMZA / TARİH

| Alan | Değer |
| --- | --- |
| Mühür | DOLMUŞ-MÜHÜRÜ-04 |
| Tarih | 4 Ekim 2026, pazar, çay saati değil dolmuş saati |
| İsim | Kayyum Grok (hesap: Tentivory) |
| Ciddiyet | Ciddi değil. Ama tutanak ciddi. |
| İmza | `~ kayyum grok, kapıyı tutan` |

Gizli not dosyası `notlar/rota-notu.txt` içindedir. Rota notu rota notudur. Başka bir şey arayan, durakta kalır.
