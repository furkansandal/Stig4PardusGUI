import sqlite3
import subprocess
import datetime
from time import sleep
import json

class Stig4Pardus_Kontrol():

    def output_kontrol(self):
        dosya = open("output.txt", "r").readlines()
        print("Kontrol edilen adet: " + str(len(dosya)))
        gecen = 0
        kalan = 0
        hata = 0
        for i in dosya:
            detay = i.split("\n")[0].split(" ")

            if detay[1] == "Gecti":
                gecen = gecen + 1
            elif detay[1] == "Kaldi":
                kalan = kalan + 1
            else:
                hata = hata + 1
        print("Geçen: " , gecen, " Kalan: ", kalan, " Hatalı: ", hata)
        tarih = datetime.datetime.now()
        con = sqlite3.connect("veriler.db")
        cur = con.cursor()
        cur.execute('''insert into kontroller(tarih, basarili_adet, basarisiz_adet) values(?, ?, ?)''',
                    (str(tarih), str(gecen), str(kalan),))
        con.commit()
        kontrol = cur.execute('''select kontroller_id from kontroller where tarih = ?''', (str(tarih),)).fetchone()[0]

        for i in dosya:
            i = i.split("\n")[0]
            kural_id = i.split(" ")[0]
            durum = i.split(" ")[1]
            if durum == "Gecti":
                durum = 1
            elif durum == "Kaldi":
                durum = 0
            else:
                continue
            cur.execute(
                '''insert into kontroller_detay(kontroller_id, durum, kural_id) values (?, ?, ?)''',
                (str(kontrol),str(durum), str(kural_id),))
            con.commit()

        con.close()

    def run_command(self, command): #komut çalıştırdığımız fonksiyom
        p = subprocess.Popen(command,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True) #subprocess sınıfını kullandık ve out error olarak subprocess pipe ı oluşturdul.
        # Buffer boş olana kadar subprocess ten stdout aldık.
        for line in iter(p.stdout.readline, b''):
            if line:  # Boş satıları zıplayalım :)
                yield line

        while p.poll() is None:
            sleep(.1)  # CPU-cycle larına yakalanmayalım...
        # Boş STDERR buffer
        err = p.stderr.read()
        if p.returncode != 0:
            # run_command() fonksiyonu STDERR yakalarsa eğer;
            print("Hata: " + str(err.decode("utf-8").split("\n")[0]))

    def html_uret(self):
        print(1)
    def json_uret(self):
        con = sqlite3.connect("veriler.db")
        cur = con.cursor()

        data = {}
        sayac_kontroller = 0
        kontrol = cur.execute('''select * from kontroller order by tarih desc''').fetchall()
        #print(kontrol)
        for i in kontrol:
            kontroller_id = i[0]
            tarih = i[1]
            basarili_adet = i[2]
            basarisiz_adet = i[3]
            kontrol_detay = cur.execute('''select * from kontroller_detay where kontroller_id = ? order by durum desc''', (kontroller_id,)).fetchall()
            liste = []
            for j in kontrol_detay:
                kural_id = j[3]
                durum = j[2]

                kural_detay = cur.execute('''select * from kurallar where kural_id = ?''', (str(kural_id),)).fetchone()


                onem = kural_detay[2]
                baslik = kural_detay[3]
                aciklama = kural_detay[4]
                aranacak_icerik = kural_detay[5]
                cozum = kural_detay[6]
                liste.append({
                    'kural_id' : kural_id,
                    'durum' : durum,
                    'onem' : onem,
                    'baslik' : baslik,
                    'aciklama' : aciklama,
                    'aranacak_icerik' : aranacak_icerik,
                    'cozum' : cozum
                })

            data["sonuclar"] = []
            data["sonuclar"].append({
                'kontroller_id': kontroller_id,
                'tarih': tarih,
                'basarili_adet': basarili_adet,
                'basarisiz_adet': basarisiz_adet,
                'durum_detay' : liste
            })
        with open('dump_all.json', 'w') as dosya_ciktisi_json:
            json.dump(data, dosya_ciktisi_json)
        print(data)

    def kontrol(self):
        for line in self.run_command("sudo bash 8.sh"):
            try:
                veri = line.decode("utf-8").split("\n")[0]
                print(veri)
            except Exception as hata:
                print(line)
        self.output_kontrol()
        self.json_uret()
        #print("Veritabanına ekliyorum...")





baslat = Stig4Pardus_Kontrol().json_uret() #nesnemiz.
#baslat.kontrol() #tüm kontrolleri gerçekleştirdik.
#baslat.output_kontrol() #sadece output okuyup veritabanına eklemek.