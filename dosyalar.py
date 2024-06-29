'''
    # exe, görsel, metin vs. vs. => Bizler python komutları aracılığı ile dosyaları okuyabiliriz.
    Birinci yötem: Metin Olan Dosyaları Okumak
    İkinci Yöntem: Metin Olmayan Dosyaları Okumak (Görseller)
'''

'''
    Dosya Açmak İçin Gerekli Olan Komut => open()
    open() İçerisine birden fazla argman kabül eder.
    1. Argüman => Hangi dosyayı açmak istiyorsanız o dosyanın yolu. Bunu yazarken string veri türünü kullan. 
    2. Argüman => Bu metin/metin olmayan dosyayı açmak istiyorsanız tanımlanan dosya açma kiplerini/modlarını kullanın.
                  --------------------- Dosya Açma Modları--------------------  
                  1 => Okuma Modu (Metin Dosyaları) => Read (Okumak) --> 'r'
                  2 => Yazma Modu (Metin Dosyaları) => Write (Yazmak) --> 'w'
                  3 => Ekleme Modu (Metin Dosyaları) => Add (Eklemek) -->  'a'
    3. Argüman => Eğer Metin dosyası açacaksınız bunun hakgi karakter ailesine sahip olduğunu belirtmeniz gerekir.
    
    with open("metin.txt", 'r', encoding='utf-8') as dosya:
        print(dosya.read())
    
'''
# Sistemdeki dosyalara erişim sağlayan bir kütüphanedir.
import os
import random
resimler = os.listdir('resimler')
secim = random.choice(resimler)
print(secim)

