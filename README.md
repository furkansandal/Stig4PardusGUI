![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/furkansandal/stig4pardusgui) ![GitHub language count](https://img.shields.io/github/languages/count/furkansandal/stig4pardusgui) [![GitHub issues](https://img.shields.io/github/issues/furkansandal/stig4pardusgui)](https://github.com/furkansandal/Stig4PardusGUI/issues?q=is:open%20is:issue) [![GitHub closed issues](https://img.shields.io/github/issues-closed/furkansandal/stig4pardusgui)](https://github.com/furkansandal/Stig4PardusGUI/issues?q=is:issue%20is:closed) ![GitHub last commit](https://img.shields.io/github/last-commit/furkansandal/stig4pardusgui) ![GitHub](https://img.shields.io/github/license/furkansandal/stig4pardusgui) [![GitHub followers](https://img.shields.io/github/followers/furkansandal?style=social)](https://github.com/furkansandal) [![Twitter Follow](https://img.shields.io/twitter/follow/furkan_sandal?style=social)](https://twitter.com/furkan_sandal) [![Keybase PGP](https://img.shields.io/keybase/pgp/furkansandal)](https://keybase.io/furkansandal) 
# Stig4Pardus Arayüz ve Konsol Geliştirmesi

Selamlar! **Stig4Pardus** uygulaması için (https://github.com/ciari/stig4pardus) bash ten Python'a çevirilmesi özellikler eklenmesi ve daha kullanılır hale getirilmesi hedeflenmektedir. Cli versiyonu tamamlanmıştır. 

- Tüm kurallar text dosyasında değil. Kurallar dahilinde veriler.db SQLite veritabanında kurallar tablosunda kayıt altına alınmıştır.
- Tüm tarama sonuçları toplu biçimde /var/www/html/ klasörü içerisinde HTML ve JSON raporları olarak çıktı vermektedir.
- Tüm taramalar veriler.db SQLite veritabanında kontroller ve kontroller_detay tablosunda kayıt altına alınmaktadır.


# Kullanım Klavuzu

   Yapılması gereken ilk işlemler gerekli python paketlerinin kurulumudur. İsterseniz virtualenv oluşturabilir, isterseniz direk Python paketleri üzerine kurulum yapabilirsiniz.
Cihazınızda Python3.x ve üstü kurulu olması gerekmektedir.
   
Arayüz kurulumu istiyorsanız aşağıdaki kurulumları yapmanız gerekmektedir.

    sudo apt-get install python3-pip
    sudo python3 -m pip -r requirements.txt

Gerekli kurulumları tamamladık. Eğer arayüz kullanmayacaksanız buradan devam edebilirsiniz. Kullanma kılavuzuna bakmak için;

     sudo python3 start.py --help


Versiyon kontrol için

    sudo python3 start-cli.py --versiyon
veya

    sudo python3 start-cli.py -v
    
Çalıştırmak için ise;

    sudo python3 start-cli.py --kontrol
    
 veya
 

    sudo python3 start-cli.py -k


olarak programı çalıştırabilirsiniz.

## Çalışan Özellikler

Tüm Linux ve Unix tabanlı işletim sistemlerinde çalışır durumdadır. Python3.x sürümünün kurulu olması yeterlidir.
- Tüm scriptlerin bash ile tetiklenmesi.
- Tüm scriptlerin çalıştırılması
- Kurallara SQLite veritabanında ulaşılabilir
- Tüm taramalar SQLite veritabanında kayıt altına alınmaktadır.
- Tüm taramaların raporlar HTML ve JSON formatında /var/www/html  dizinine kayıt edilmektedir.

## Güncelleme Detayları

### v0.1
- Ana tasarım yapıldı.
- Sadece bash scripti tetiklendi
- Bash logları kayıt altına alındı programımızda takip edildi.
### v0.2
- Script çalıştıktan sonra /var/log/stig4pardus/ dizininde bulunan oluşturulan son 2 Log kaydının otomatik olarak açılması eklendi ancak şuan için pasif. son_eklenen_log_getir.py sınıfı üzerine eklemeler yapıldı.
### v1.0
- Cli versiyonu tamamlanmıştır.
- Script çalıştıktan sonra /var/www/html klasörüne kayıt etmektedir. v1.1 güncellemesi ile komut çalışma sırasında girilen argüman klasörüne, boş ise belirleyeceğimiz statik dizine kayıt edecektir.
- Tüm kurallar veriler.db SQLite veritabanına eklenmiştir.
- Tüm kontroller SQLite veritabanında kayıt altına alınıyor.
- HTML düzenli rapor hazırlanmıştır.
- JSON formatında rapor hazırlanmıştır.