![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/furkansandal/stig4pardusgui) ![GitHub language count](https://img.shields.io/github/languages/count/furkansandal/stig4pardusgui) [![GitHub issues](https://img.shields.io/github/issues/furkansandal/stig4pardusgui)](https://github.com/furkansandal/Stig4PardusGUI/issues?q=is:open%20is:issue) [![GitHub closed issues](https://img.shields.io/github/issues-closed/furkansandal/stig4pardusgui)](https://github.com/furkansandal/Stig4PardusGUI/issues?q=is:issue%20is:closed) ![GitHub last commit](https://img.shields.io/github/last-commit/furkansandal/stig4pardusgui) ![GitHub](https://img.shields.io/github/license/furkansandal/stig4pardusgui) [![GitHub followers](https://img.shields.io/github/followers/furkansandal?style=social)](https://github.com/furkansandal) [![Twitter Follow](https://img.shields.io/twitter/follow/furkan_sandal?style=social)](https://twitter.com/furkan_sandal) [![Keybase PGP](https://img.shields.io/keybase/pgp/furkansandal)](https://keybase.io/furkansandal) 
# Stig4Pardus Arayüz ve Geliştirmesi

Selamlar! **Stig4Pardus** uygulaması için (https://github.com/ciari/stig4pardus) bash ten Python'a çevirilmesi özellikler eklenmesi ve daha kullanılır hale getirilmesi hedeflenmektedir.


# Dosyalar

   Yapılması gereken ilk işlemler gerekli python paketlerinin kurulumudur. İsterseniz virtualenv oluşturabilir, isterseniz direk Python paketleri üzerine kurulum yapabilirsiniz.
Cihazınızda Python3.7 ve üstü kurulu olması gerekmektedir.
   

> sudo apt-get install python3-pip
> 
> sudo python3.7 -m pip -r requirements.txt
> 
> sudo python3.7 start.py

olarak programı çalıştırabilirsiniz.

## Çalışan Özellikler

Stig4Pardus kurulu olan sistemler için çalışır durumdadır. Kurulu değilse program çalışacak ancak işlem yapamayacaksınız.

- Tüm scriptlerin bash ile tetiklenmesi.

## Güncelleme Detayları

### v0.1
- Ana tasarım yapıldı.
- Sadece bash scripti tetiklendi
- Bash logları kayıt altına alındı programımızda takip edildi.
### v0.2
- Script çalıştıktan sonra /var/log/stig4pardus/ dizininde bulunan oluşturulan son 2 Log kaydının otomatik olarak açılması eklendi ancak şuan için pasif. son_eklenen_log_getir.py sınıfı üzerine eklemeler yapıldı.