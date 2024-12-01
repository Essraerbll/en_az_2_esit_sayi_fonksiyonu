### Sayıların Eşit Olup Olmadığını Kontrol Etme
Bu proje, verilen 5 sayıdan en az iki tanesinin birbirine eşit olup olmadığını kontrol eden 3 farklı çözüm yolunu içermektedir.
Aşağıda her bir çözüm yolunun açıklamaları ve nasıl çalıştığına dair bilgiler bulunmaktadır.

### Çözüm Yolu 1:
Bu yöntemde, sayılar bir listeye eklenir ve her bir sayı için count fonksiyonu kullanılarak sayılar arasındaki tekrarlar kontrol edilir.
Eğer bir sayı birden fazla kez geçiyorsa, "En az iki sayı birbirine eşittir." mesajı döndürülür.

### Çözüm Yolu 2:
Bu yöntemde, her bir sayı çiftini kontrol etmek için iç içe döngüler kullanılır.
Eğer herhangi bir iki sayı eşitse, "En az iki sayı birbirine eşittir." mesajı yazdırılır.

### Çözüm Yolu 3:
Bu yöntemde, verilen sayılar bir listeye dönüştürülür ve bir set'e dönüştürülerek tekrarlar kontrol edilir.
Eğer liste uzunluğu set'in uzunluğuna eşit değilse, en az iki sayı eşittir.
