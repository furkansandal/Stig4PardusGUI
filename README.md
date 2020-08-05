![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/furkansandal/stig4pardusgui) ![GitHub language count](https://img.shields.io/github/languages/count/furkansandal/stig4pardusgui) [![GitHub issues](https://img.shields.io/github/issues/furkansandal/stig4pardusgui)](https://github.com/furkansandal/Stig4PardusGUI/issues?q=is:open%20is:issue) [![GitHub closed issues](https://img.shields.io/github/issues-closed/furkansandal/stig4pardusgui)](https://github.com/furkansandal/Stig4PardusGUI/issues?q=is:issue%20is:closed) ![GitHub last commit](https://img.shields.io/github/last-commit/furkansandal/stig4pardusgui) ![GitHub](https://img.shields.io/github/license/furkansandal/stig4pardusgui) [![GitHub followers](https://img.shields.io/github/followers/furkansandal?style=social)](https://github.com/furkansandal) [![Twitter Follow](https://img.shields.io/twitter/follow/furkan_sandal?style=social)](https://twitter.com/furkan_sandal) [![Keybase PGP](https://img.shields.io/keybase/pgp/furkansandal)](https://keybase.io/furkansandal) 
# Stig4Pardus Arayüz ve Konsol Geliştirmesi

Selamlar! **Stig4Pardus** uygulaması için (https://github.com/ciari/stig4pardus) bash ten Python'a çevirilmesi özellikler eklenmesi ve daha kullanılır hale getirilmesi hedeflenmektedir. Cli versiyonu tamamlanmıştır. 

- Tüm kurallar text dosyasında değil. Kurallar dahilinde veriler.db SQLite veritabanında kurallar tablosunda kayıt altına alınmıştır.![Stig4Pardus Veritabanı Kurallar](https://furkansandal.com/havelsanapps/gorseller/veritabani_kurallar.png)
- Tüm tarama sonuçları toplu biçimde /var/www/html/ klasörü içerisinde HTML ve JSON raporları olarak çıktı vermektedir.![Stig4Pardus Rapor](https://furkansandal.com/havelsanapps/gorseller/html_output.png)
![Stig4Pardus Json Rapor](https://furkansandal.com/havelsanapps/gorseller/json_sonuc.png)
- Tüm taramalar veriler.db SQLite veritabanında kontroller ve kontroller_detay tablosunda kayıt altına alınmaktadır.![Stig4Pardus Kontroller DB](https://furkansandal.com/havelsanapps/gorseller/veritabani_kontroller.png) ![Stig4Pardus Kontroller Detay](https://furkansandal.com/havelsanapps/gorseller/veritabani_kontroller_detay.png)
- Tüm tarama sonuçları istenilen konuma -d --dizin argümanı ile çıkarılabilir.![Dizin seçeneği](https://furkansandal.com/havelsanapps/gorseller/dizin.png)


# Kullanım Kılavuzu

   Yapılması gereken ilk işlemler gerekli python paketlerinin kurulumudur. İsterseniz virtualenv oluşturabilir, isterseniz direk Python paketleri üzerine kurulum yapabilirsiniz.
Cihazınızda Python3.x ve üstü kurulu olması gerekmektedir.
   
Dosyaları indirelim.

    wget https://github.com/furkansandal/Stig4PardusGUI/archive/master.zip
    unzip master.zip
    cd Stig4PardusGUI-master

Arayüz kurulumu istiyorsanız aşağıdaki kurulumları yapmanız gerekmektedir. Kullanmayacaksanız bu adımı atlayabilirsiniz.

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


olarak programı çalıştırabilirsiniz. Ayrıca raporları istediğiniz konuma çıkarmak için ise

    sudo python3 start-cli.py -k -d /var/log/stig4pardus/
girişi yapabilir /var/log/stig4pardus/ yerine istediğiniz konumu girebilirsiniz.

## Çalışan Özellikler

Tüm Linux ve Unix tabanlı işletim sistemlerinde çalışır durumdadır. Python3.x sürümünün kurulu olması yeterlidir.
- Tüm scriptlerin bash ile tetiklenmesi.
- Tüm scriptlerin çalıştırılması
- Kurallara SQLite veritabanında ulaşılabilir
- Tüm taramalar SQLite veritabanında kayıt altına alınmaktadır.
- Tüm taramaların raporlar HTML ve JSON formatında /var/www/html  dizinine kayıt edilmektedir.
- Tüm raporlar istediğiniz dizine kayıt edilebilmektedir. --dizin konum veya -d konum olarak giriş verebilirsiniz. Boş bıraktığınız taktirde /var/www/html e kayıt edilecektir.

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
### v1.1
- -d --dizin seçeneği ile devamına ekleyeceğiniz konum bilgisiyle istediğiniz yere rapor çıkışı sağlayabilirsiniz. Örnek kullanım `sudo python3 start_cli.py -k -d /root/loglar`
- -h --help bilgisi eklendi. Argüman girilmediği takdirde help bilgisi otomatik olarak çalışacaktır.![Stig4Pardus Help](https://furkansandal.com/havelsanapps/gorseller/help.png)