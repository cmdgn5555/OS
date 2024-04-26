import os

from datetime import datetime

#print(os.getcwd())
#
#print('__' * 50)
#
#os.chdir("C:/Users/5530/Desktop/if else yapısı")
#
#print(os.getcwd())
#
#print('__' * 50)
#
#print(os.listdir())
#
#print('__' * 50)
#
#print(os.listdir("C:/Users/5530/Desktop/video geri sarma 2"))
#
#print('__' * 50)
#
#for i in os.listdir("C:/Users/5530/Desktop/html dersleri"):
#    print(i)
#
#print('__' * 50)

# os.mkdir("denemeKlasörü")

#os.makedirs("deneme1/deneme2/deneme3")

#os.rmdir("denemeKlasörü")

#os.removedirs("deneme1")

'''
os.chdir("C:/Users/5530/Desktop/if else yapısı/deneme1")

silinecek = os.listdir()[0]

print(silinecek)

os.remove(silinecek)
'''

#os.remove("C:/Users/5530/Desktop/video geri sarma 2/kolaj1.mp4")

#os.rename("C:/Users/5530/Desktop/video geri sarma 2/kolaj2.mp4", "C:/Users/5530/Desktop/video geri sarma 2/video-film.mp4")

#os.rename("C:/Users/5530/Desktop/video geri sarma 2/kayit9.avi", "C:/Users/5530/Desktop/chatgpt sorular/123.mp4")

#os.rename("C:/Users/5530/Desktop/chatgpt sorular/123.mp4", "C:/Users/5530/Desktop/video geri sarma 2/kayit9.avi")

#print(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_atime)

#zaman = datetime.fromtimestamp(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_atime)

#print(zaman)

#print(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_birthtime)

#zaman = datetime.fromtimestamp(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_birthtime)

#print(zaman)

#print(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_mtime)
#
#zaman = datetime.fromtimestamp(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_mtime)
#
#print(zaman)

#print(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_size)
#
#zaman = datetime.fromtimestamp(os.stat("C:/Users/5530/Desktop/video geri sarma 2/reversed6.avi").st_size)
#
#print(zaman)

#print(os.stat("C:/Users/5530/Desktop/moviepy").st_mtime)
#
#zaman = datetime.fromtimestamp(os.stat("C:/Users/5530/Desktop/moviepy").st_mtime)
#
#print(zaman)

#for i in os.walk("C:/Users/5530/Desktop/chatgpt sorular/deneme klasörü"):
#    print(i)

#for gecerli_klasör, icindeki_klasörler, icindeki_dosyalar in os.walk("C:/Users/5530/Desktop/video geri sarma 2"):
#    print(f"geçerli klasör = {gecerli_klasör}\niçindeki klasörler = {icindeki_klasörler}\niçindeki dosyalar = {icindeki_dosyalar}")

#print(os.path.join('deneme1', 'deneme2', 'deneme3'))

#print(os.path.isdir("C:/Users/5530/Desktop/pytube ile youtube video indirme"))
#print(os.path.isfile("C:/Users/5530/Desktop/video belgesel/20130209 2254 - NTV.ts"))

#print(os.path.splitext("C:/Users/5530/Desktop/html dersleri/yazılar.txt"))

'''
import os

def duzenle():
    klasor = input('düzenlenecek klasör : ')
    dosyalar = []
    uzantilar = []
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor, dosya)):
                continue
            else:
                dosyalar.append(dosya)
    list_dir()

    for dosya in dosyalar:
        uzanti = dosya.split('.')[-1]
        if uzanti in uzantilar:
            continue
        else:
            uzantilar.append(uzanti)
    
    for uzanti in uzantilar:
        if os.path.isdir(os.path.join(klasor, uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor, uzanti))
    
    for dosya in dosyalar:
        uzanti = dosya.split('.')[-1]
        os.rename(os.path.join(klasor, dosya), os.path.join(klasor, uzanti, dosya))

duzenle()

'''

'''
import os
from datetime import datetime

def duzenle():
    klasor = input('düzenlenecek klasör : ')
    dosyalar = []
    tarihler = []
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor, dosya)):
                continue
            else:
                dosyalar.append(dosya)
    list_dir()

    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor, dosya)).st_mtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        if tarih in tarihler:
            continue
        else:
            tarihler.append(tarih)
    
    for tarih in tarihler:
        if os.path.isdir(os.path.join(klasor, tarih)):
            continue
        else:
            os.mkdir(os.path.join(klasor, tarih))
    
    for dosya in dosyalar:
        tarih_damgasi = os.stat(os.path.join(klasor, dosya)).st_mtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        os.rename(os.path.join(klasor, dosya), os.path.join(klasor, tarih, dosya))

duzenle()

'''
import os

#for i in dir(os):
#    print(i)

#print(os.name)

#print(os.getcwd())
#
#print('__' * 30)
#
#os.chdir("C:/Users/5530/Desktop/video belgesel")
#
#print(os.getcwd())
#
#for i in os.listdir():
#    print(i)
#
#print('__' * 30)
#
#print(os.listdir()[8])

#print(os.getcwd())

#os.chdir("C:/Users/5530/Desktop/os deneme klasörü")
#
#print(os.getcwd())

#os.rmdir("C:/Users/5530/Desktop/os deneme klasörü/abc")

#os.remove("C:/Users/5530/Desktop/os deneme klasörü/abcde.txt")

#os.chdir("C:/Users/5530/Desktop/os deneme klasörü")

#print(os.listdir(os.curdir))

#print(os.listdir(".."))

#os.startfile("C:/Users/5530/Desktop/os deneme klasörü/abc")
#
#os.startfile("C:/Users/5530/Desktop/os deneme klasörü/12345.txt")

#os.mkdir("hello/merhaba/selam")

#os.mkdir("C:/Users/5530/Desktop/video belgesel/yeni klasör/newfolder")

#os.makedirs("C:/Users/5530/Desktop/video belgesel/1/2/3/4/5")

#os.mkdir("boş klasör")

#os.makedirs("ülkeler/şehirler/ilçeler/mahalleler")

#os.rename("123", "98765")

#os.rename("abcde.txt", "xyz.txt")

#os.rename("C:/Users/5530/Desktop/os deneme klasörü/xyz.txt", "C:/Users/5530/Desktop/video belgesel/merhaba.txt")

#os.rename("C:/Users/5530/Desktop/os deneme klasörü/ülkeler", "C:/Users/5530/Desktop/video belgesel/deneme klasör")

#os.rename("C:/Users/5530/Desktop/os deneme klasörü/New York City - My visit on the year 2022.avi", "C:/Users/5530/Desktop/video belgesel/new video.mp4")

#os.rmdir("C:/Users/5530/Desktop/os deneme klasörü/ülkeler/şehirler/ilçeler")

#os.rmdir("C:/Users/5530/Desktop/os deneme klasörü/ülkeler/şehirler/ilçeler")

#os.removedirs("C:/Users/5530/Desktop/os deneme klasörü/ülkeler/şehirler/ilçeler/mahalleler")

#os.removedirs("C:/Users/5530/Desktop/os deneme klasörü/ülkeler/şehirler/ilçeler")

#os.removedirs("C:/Users/5530/Desktop/os deneme klasörü/abc/xyz123")

#print(os.stat("C:/Users/5530/Desktop/video belgesel/Street Videos (march-2020).mp4"))

#print(os.path.split("C:/Users/5530/Desktop/chatgpt sorular"))

#print(os.path.split("C:/Users/5530/Desktop/os deneme klasörü/ülkeler/şehirler/ilçeler"))

#print(os.path.splitext("C:/Users/5530/Desktop/os deneme klasörü/12345.txt"))

#print(os.path.splitext("C:/Users/5530/Desktop/video belgesel/from street level.mp4"))

#print(os.path.join('selam','merhaba','hello','world'))

#print(os.path.join("C:/Users/5530/Desktop/chatgpt sorular", "deneme1", "deneme2"))

#print(os.getcwd())
#
#os.chdir("C:/Users/5530/Desktop/os deneme klasörü")
#
#print(os.getcwd())

#for i in os.listdir():
#    if i.endswith(".mp4"):
#        print(i)

#for i in os.listdir():
#    if i.startswith("W"):
#        print(i)

#for i in os.listdir():
#    if i.capitalize():
#        print(i)

#liste = []
#for i in os.listdir():
#    sayı = i.count('2000')
#    liste.append(sayı)
#
#print(sum(liste))

#for i in os.listdir():
#    print(i)
#
#os.startfile("C:/Users/5530/Desktop/video belgesel/June visit 2021.mp4")

#os.mkdir("C:/Users/5530/Desktop/os deneme klasörü/ekle klasörü")

#os.rename("C:/Users/5530/Desktop/video.mp4", "C:/Users/5530/Desktop/os deneme klasörü/ekle klasörü/deneme.mp4")

#os.makedirs("C:/Users/5530/Desktop/os deneme klasörü/video klasörü1/video klasörü2/video klasörü3")

#os.rename("C:/Users/5530/Desktop/abc1.avi", "C:/Users/5530/Desktop/os deneme klasörü/video klasörü1/deneme1.avi")

#os.rename("C:/Users/5530/Desktop/abc2.avi", "C:/Users/5530/Desktop/os deneme klasörü/video klasörü1/video klasörü2/deneme2.avi")

#os.rename("C:/Users/5530/Desktop/abc3.mp4", "C:/Users/5530/Desktop/os deneme klasörü/video klasörü1/video klasörü2/video klasörü3/deneme1.avi")

#os.replace("C:/Users/5530/Desktop/os deneme klasörü/98765", "C:/Users/5530/Desktop/os deneme klasörü/324")

#os.replace("C:/Users/5530/Desktop/os deneme klasörü/12345.txt", "C:/Users/5530/Desktop/os deneme klasörü/abcde.txt")

#os.replace("C:/Users/5530/Desktop/os deneme klasörü/abcde.txt", "C:/Users/5530/Desktop/os deneme klasörü/324/deneme.txt")

#os.replace("C:/Users/5530/Desktop/os deneme klasörü/324/deneme.txt", "C:/Users/5530/Desktop/os deneme klasörü/abcde.txt")

#os.remove("C:/Users/5530/Desktop/os deneme klasörü/silinecek.txt")

#os.rmdir("C:/Users/5530/Desktop/os deneme klasörü/324")

#os.rmdir("C:/Users/5530/Desktop/os deneme klasörü/ülkeler")

#os.makedirs("ülkeler/şehirler/ilçeler/mahalleler")

#os.removedirs("ülkeler/şehirler/ilçeler/mahalleler")

#from datetime import datetime
#
#print(os.stat("C:/Users/5530/Desktop/video belgesel/20130209 2254 - NTV.ts"))
#
#print()

#dosya = os.stat("C:/Users/5530/Desktop/video belgesel/20130209 2254 - NTV.ts")
#dosya2 = os.stat("C:/Users/5530/Desktop/video belgesel/video belgeseli.mpg")
#print(datetime.fromtimestamp(dosya.st_atime))
#print()
#print(datetime.fromtimestamp(dosya.st_birthtime))
#print()
#print(datetime.fromtimestamp(dosya.st_mtime))
#print()
#print("dosyanın gb boyutu =", ((dosya.st_size / 1024) / 1024) / 1024)
#print()
#print("dosyanın gb boyutu =", ((dosya2.st_size / 1024) / 1024) / 1024)

#print(os.system("dir"))
#print(os.system("date"))

'''
def tarama(arama, current):
    for öge in os.listdir():
        if os.path.isdir(öge):
            os.chdir(öge)
            tarama(arama, os.getcwd())
            os.chdir(current)
        if arama in öge:
            print(öge, '-->', os.getcwd())

arama = input("aramak isteğiniz şey : ")

tarama(arama, os.getcwd())

'''

#def sil(file):
#    for file in os.listdir():
#        if os.path.isdir(file):
#            continue
#        else:
#            os.remove(file)
#

#silinecek_dosya = input("silinecek dosyanın yolunu giriniz : ")

#sil(silinecek_dosya)

#def klasör_isim_degis(klasör, yeni_adı):
#    for klasör in os.listdir():
#        if os.path.isfile(klasör):
#            continue
#        else:
#            os.rename(klasör, yeni_adı)



#ismi_degisecek_klasör = input("lütfen ismi değişecek olan klasörün yolunu giriniz :")

#yeni_isim = input('lütfen klasörün yeni ismini giriniz : ')

#klasör_isim_degis(ismi_degisecek_klasör, yeni_isim)

#def dosya_isim_degis(dosya, yeni_adı):
#    for dosya in os.listdir():
#        if os.path.isfile(dosya):
#            os.rename(dosya, yeni_adı)


#ismi_degisecek_dosya = input("lütfen ismi değişecek olan dosyanın yolunu giriniz : ")

#yeni_isim = input("lütfen dosyanın yeni ismini giriniz : ")

#dosya_isim_degis(ismi_degisecek_dosya, yeni_isim)
            

#def klasör_olustur(klasör_yolu, klasör_adı):
#    if klasör_adı not in os.listdir():
#        os.mkdir(os.path.join(klasör_yolu, klasör_adı))


#eklenecek_klasörün_yolu = input('eklenecek klasörün yolunu giriniz : ')
#
#klasör_isim = input('klasör ismi giriniz : ')
#
#klasör_olustur(eklenecek_klasörün_yolu, klasör_isim)


#def klasör_olustur_ve_baska_dizine_gönder(klasör_yolu, klasör_adı, gidecegi_klasör_yolu, yeni_adı):
#    if klasör_adı not in os.listdir():
#        os.mkdir(os.path.join(klasör_yolu, klasör_adı))
#        os.rename(os.path.join(klasör_yolu, klasör_adı), os.path.join(gidecegi_klasör_yolu, yeni_adı))


#eklenecek_klasörün_yolu = input('eklenecek klasörün yolunu giriniz : ')
#
#klasör_isim = input('klasör ismi giriniz : ')
#
#gidecegi_yer = input('klasörün gideceği dizinin yolunu giriniz : ')
#
#yeni_ismi = input('klasörün yeni adını giriniz : ')
#
#klasör_olustur_ve_baska_dizine_gönder(eklenecek_klasörün_yolu, klasör_isim, gidecegi_yer, yeni_ismi)
        

#def dosyayı_yada_klasörü_baska_dizine_adını_degistirerek_gönder(yolu, adı, gideceği_yerin_yolu, yeni_adı):
#    if adı in os.listdir():
#        os.rename(os.path.join(yolu, adı), os.path.join(gideceği_yerin_yolu, yeni_adı))
#    else:
#        print('dosya yada klasör bulunamadı!')

    
#dosya_yada_klasörün_yolu = input('lütfen gönderilecek dosya yada klasörün yolunu giriniz : ')
#öge = input('lütfen gönderilecek dosya yada klasörün adını giriniz : ')
#gidecegi_dizinin_yolu = input('lütfen dosyanın gideceği dizinin yolunu giriniz : ')
#ögenin_yeni_adı = input('lütfen dosyanın yeni adını giriniz : ')
#
#dosyayı_yada_klasörü_baska_dizine_adını_degistirerek_gönder(dosya_yada_klasörün_yolu, öge, gidecegi_dizinin_yolu, ögenin_yeni_adı)
        


#def klasörler_olustur(folder_path,folder1, folder2, folder3, folder4, folder5):
#    if folder1 not in os.listdir():
#        os.makedirs(os.path.join(folder_path, folder1))
#        os.chdir(os.path.join(folder_path, folder1))
#
#    if folder2 not in os.getcwd():
#        os.makedirs(os.path.join(folder_path, folder1, folder2))
#        os.chdir(os.path.join(folder_path, folder1, folder2))
#
#    if folder3 not in os.getcwd():
#        os.makedirs(os.path.join(folder_path, folder1, folder2, folder3))
#        os.chdir(os.path.join(folder_path, folder1, folder2, folder3))
#
#    if folder4 not in os.getcwd():
#        os.makedirs(os.path.join(folder_path, folder1, folder2, folder3, folder4))
#        os.chdir(os.path.join(folder_path, folder1, folder2, folder3, folder4))
#
#    if folder5 not in os.getcwd():
#        os.makedirs(os.path.join(folder_path, folder1, folder2, folder3, folder4, folder5))
        


#klasör_yolu = input('lütfen klasörlerin oluşturulacağı yolu giriniz : ')
#
#klasör1 = input('lütfen bir klasör adı giriniz : ')
#klasör2 = input('lütfen bir klasör adı giriniz : ')
#klasör3 = input('lütfen bir klasör adı giriniz : ')
#klasör4 = input('lütfen bir klasör adı giriniz : ')
#klasör5 = input('lütfen bir klasör adı giriniz : ')
#
#klasörler_olustur(klasör_yolu, klasör1, klasör2, klasör3, klasör4, klasör5)
        

#def dosya_durum_bilgisi(path, file):
#    if file in os.listdir(path):
#        bilgi = os.stat(os.path.join(path, file))
#        print(bilgi)


#dosya_yolu = input("dosyanın yolunu giriniz : ")
#dosya = input("lütfen durum bilgisini öğrenmek istediğiniz dosyanın adını giriniz : ")
#
#dosya_durum_bilgisi(dosya_yolu, dosya)
        

#def klasör_sil(path, folder):
#    if folder in os.listdir(path):
#        if len(os.listdir(folder)) != 0:
#            pass
#        else:
#            os.rmdir(os.path.join(path, folder))


#klasör_yolu = input("lütfen silinecek klasörün yolunu giriniz : ")
#klasör = input('lütfen silinecek klasörün adını giriniz : ')

#klasör_sil(klasör_yolu, klasör)



        



















            
















            




















 
 









            




















