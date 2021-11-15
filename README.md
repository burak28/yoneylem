# yoneylem
Yon eylem **z** fonksiyonu için **min** ve **max** değerini bulmaya yarayan algoritmadır.
## Grafik Yöntem
Fonksiyon girdi olarak **z** fonksiyonunun katsayılarını ve eşitsizliklerin katsayılarını alır.
Return olarak herhangi bir değer döndürmez. Console ekranına **z** değernin **min** ve **max** değerini yazdırır.
Fonksiyonların koordinat sisteminin 1.bölgesinde taralı alanı gösterir.

Örnek olarak:

- z = 6x1 + 8x2

- 7x1 + 3x2 <= 21
- 6x1 + 7x2 <= 42
- x1 <= 3
- x2 <= 4

Fonksiyona verilmesi gereken 1.girdi z fonksiyonunun katsayılarıdır. [6, 8]
Fonksiyona verilmesi gereken 2.girdi eşitsizliklerin oluşturduğu katsayılar matrisidir.

matrix: [[7, 3, 21, 1],
         [6, 7, 42, 1],
         [1, 0, 3, 1],
         [0, 1, 4, 1],]
         
Satırların sonundaki 1 değeri <= veya >= olduğunu göstermektedir.

- <= -> 1 
- \>= -> 0
