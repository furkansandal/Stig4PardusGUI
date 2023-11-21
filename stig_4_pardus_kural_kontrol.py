import sqlite3
import subprocess
import datetime
from time import sleep
import json

dizin = "/var/www/html/"

class Stig4Pardus_Kontrol():



    def __init__(self):
        self.dizin = "/var/www/html/"

    def html_uret(self):
        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ust_kisim = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>
Pardus için STIG uyumluluk ve sıkılaştırma kontrolü tüm raporlar
</title>
<style>
      /* -- import Roboto Font ---------------------------- */

/* -- You can use this tables in Bootstrap (v3) projects. -- */
/* -- Box model ------------------------------- */
*,
*:after,
*:before {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
/* -- Demo style ------------------------------- */
html,
body {
  position: relative;
  min-height: 100%;
  height: 100%;
}
html {
  position: relative;
  overflow-x: hidden;
  margin: 16px;
  padding: 0;
  min-height: 100%;
  font-size: 62.5%;
}
body {
  font-family: 'RobotoDraft', 'Roboto', 'Helvetica Neue, Helvetica, Arial', sans-serif;
  font-style: normal;
  font-weight: 300;
  font-size: 1.4rem;
  line-height: 2rem;
  letter-spacing: 0.01rem;
  color: #212121;
  background-color: #f5f5f5;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}
#demo {
  margin: 20px auto;
  max-width: 90%;
}
#demo h1 {
  font-size: 2.4rem;
  line-height: 3.2rem;
  letter-spacing: 0;
  font-weight: 300;
  color: #212121;
  text-transform: inherit;
  margin-bottom: 1rem;
  text-align: center;
}
#demo h2 {
  font-size: 1.5rem;
  line-height: 2.8rem;
  letter-spacing: 0.01rem;
  font-weight: 400;
  color: #212121;
  text-align: center;
}
.shadow-z-1 {
  -webkit-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
  -moz-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
}
/* -- Material Design Table style -------------- */
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 2rem;
  background-color: #fff;
}
.table > thead > tr,
.table > tbody > tr,
.table > tfoot > tr {
  -webkit-transition: all 0.3s ease;
  -o-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  text-align: left;
  padding: 1.6rem;
  vertical-align: top;
  border-top: 0;
  -webkit-transition: all 0.3s ease;
  -o-transition: all 0.3s ease;
  transition: all 0.3s ease;
}
.table > thead > tr > th {
  font-weight: 400;
  color: #757575;
  vertical-align: bottom;
  border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 1px solid rgba(0, 0, 0, 0.12);
}
.table .table {
  background-color: #fff;
}
.table .no-border {
  border: 0;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 0.8rem;
}
.table-bordered {
  border: 0;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 0;
  border-bottom: 1px solid #e0e0e0;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-child(odd) > td,
.table-striped > tbody > tr:nth-child(odd) > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr:hover > td,
.table-hover > tbody > tr:hover > th {
  background-color: rgba(0, 0, 0, 0.12);
}
@media screen and (max-width: 768px) {
  .table-responsive-vertical > .table {
    margin-bottom: 0;
    background-color: transparent;
  }
  .table-responsive-vertical > .table > thead,
  .table-responsive-vertical > .table > tfoot {
    display: none;
  }
  .table-responsive-vertical > .table > tbody {
    display: block;
  }
  .table-responsive-vertical > .table > tbody > tr {
    display: block;
    border: 1px solid #e0e0e0;
    border-radius: 2px;
    margin-bottom: 1.6rem;
  }
  .table-responsive-vertical > .table > tbody > tr > td {
    background-color: #fff;
    display: block;
    vertical-align: middle;
    text-align: right;
  }
  .table-responsive-vertical > .table > tbody > tr > td[data-title]:before {
    content: attr(data-title);
    float: left;
    font-size: inherit;
    font-weight: 400;
    color: #757575;
  }
  .table-responsive-vertical.shadow-z-1 {
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;
  }
  .table-responsive-vertical.shadow-z-1 > .table > tbody > tr {
    border: none;
    -webkit-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
    -moz-box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.12), 0 1px 2px 0 rgba(0, 0, 0, 0.24);
  }
  .table-responsive-vertical > .table-bordered {
    border: 0;
  }
  .table-responsive-vertical > .table-bordered > tbody > tr > td {
    border: 0;
    border-bottom: 1px solid #e0e0e0;
  }
  .table-responsive-vertical > .table-bordered > tbody > tr > td:last-child {
    border-bottom: 0;
  }
  .table-responsive-vertical > .table-striped > tbody > tr > td,
  .table-responsive-vertical > .table-striped > tbody > tr:nth-child(odd) {
    background-color: #fff;
  }
  .table-responsive-vertical > .table-striped > tbody > tr > td:nth-child(odd) {
    background-color: #f5f5f5;
  }
  .table-responsive-vertical > .table-hover > tbody > tr:hover > td,
  .table-responsive-vertical > .table-hover > tbody > tr:hover {
    background-color: #fff;
  }
  .table-responsive-vertical > .table-hover > tbody > tr > td:hover {
    background-color: rgba(0, 0, 0, 0.12);
  }
}
.table-striped.table-mc-red > tbody > tr:nth-child(odd) > td,
.table-striped.table-mc-red > tbody > tr:nth-child(odd) > th {
  background-color: #fde0dc;
}
.table-hover.table-mc-red > tbody > tr:hover > td,
.table-hover.table-mc-red > tbody > tr:hover > th {
  background-color: #f9bdbb;
}
@media screen and (max-width: 767px) {
  .table-responsive-vertical .table-striped.table-mc-red > tbody > tr > td,
  .table-responsive-vertical .table-striped.table-mc-red > tbody > tr:nth-child(odd) {
    background-color: #fff;
  }
  .table-responsive-vertical .table-striped.table-mc-red > tbody > tr > td:nth-child(odd) {
    background-color: #fde0dc;
  }
  .table-responsive-vertical .table-hover.table-mc-red > tbody > tr:hover > td,
  .table-responsive-vertical .table-hover.table-mc-red > tbody > tr:hover {
    background-color: #fff;
  }
  .table-responsive-vertical .table-hover.table-mc-red > tbody > tr > td:hover {
    background-color: #f9bdbb;
  }
}
.table-striped.table-mc-pink > tbody > tr:nth-child(odd) > td,
.table-striped.table-mc-pink > tbody > tr:nth-child(odd) > th {
  background-color: #fce4ec;
}
.table-hover.table-mc-pink > tbody > tr:hover > td,
.table-hover.table-mc-pink > tbody > tr:hover > th {
  background-color: #f8bbd0;
}
@media screen and (max-width: 767px) {
  .table-responsive-vertical .table-striped.table-mc-pink > tbody > tr > td,
  .table-responsive-vertical .table-striped.table-mc-pink > tbody > tr:nth-child(odd) {
    background-color: #fff;
  }
  .table-responsive-vertical .table-striped.table-mc-pink > tbody > tr > td:nth-child(odd) {
    background-color: #fce4ec;
  }
  .table-responsive-vertical .table-hover.table-mc-pink > tbody > tr:hover > td,
  .table-responsive-vertical .table-hover.table-mc-pink > tbody > tr:hover {
    background-color: #fff;
  }
  .table-responsive-vertical .table-hover.table-mc-pink > tbody > tr > td:hover {
    background-color: #f8bbd0;
  }
}
.table-striped.table-mc-purple > tbody > tr:nth-child(odd) > td,
.table-striped.table-mc-purple > tbody > tr:nth-child(odd) > th {
  background-color: #f3e5f5;
}
.table-hover.table-mc-purple > tbody > tr:hover > td,
.table-hover.table-mc-purple > tbody > tr:hover > th {
  background-color: #e1bee7;
}
@media screen and (max-width: 767px) {
  .table-responsive-vertical .table-striped.table-mc-purple > tbody > tr > td,
  .table-responsive-vertical .table-striped.table-mc-purple > tbody > tr:nth-child(odd) {
    background-color: #fff;
  }
  .table-responsive-vertical .table-striped.table-mc-purple > tbody > tr > td:nth-child(odd) {
    background-color: #f3e5f5;
  }
  .table-responsive-vertical .table-hover.table-mc-purple > tbody > tr:hover > td,
  .table-responsive-vertical .table-hover.table-mc-purple > tbody > tr:hover {
    background-color: #fff;
  }
  .table-responsive-vertical .table-hover.table-mc-purple > tbody > tr > td:hover {
    background-color: #e1bee7;
  }
}
.table-striped.table-mc-deep-purple > tbody > tr:nth-child(odd) > td,
.table-striped.table-mc-deep-purple > tbody > tr:nth-child(odd) > th {
  background-color: #ede7f6;
}
.table-hover.table-mc-deep-purple > tbody > tr:hover > td,
.table-hover.table-mc-deep-purple > tbody > tr:hover > th {
  background-color: #d1c4e9;
}
@media screen and (max-width: 767px) {
  .table-responsive-vertical .table-striped.table-mc-deep-purple > tbody > tr > td,
  .table-responsive-vertical .table-striped.table-mc-deep-purple > tbody > tr:nth-child(odd) {
    background-color: #fff;
  }
  .table-responsive-vertical .table-striped.table-mc-deep-purple > tbody > tr > td:nth-child(odd) {
    background-color: #ede7f6;
  }
  .table-responsive-vertical .table-hover.table-mc-deep-purple > tbody > tr:hover > td,
  .table-responsive-vertical .table-hover.table-mc-deep-purple > tbody > tr:hover {
    background-color: #fff;
  }
  .table-responsive-vertical .table-hover.table-mc-deep-purple > tbody > tr > td:hover {
    background-color: #d1c4e9;
  }
}
.t…
</style>
<script type="text/javascript">
function elementDisplay(objid){
        var obj=document.getElementById(objid);
        if(obj.style.display !='none'){
        obj.style.display='none';
        }else{
        obj.style.display='block';}
        }
</script>
</head>
<body>
  <div id="demo">
  <center><img src="data:image/png;base64,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" border="0" width="220"/></center>
    <h1>Pardus için STIG uyumluluk ve sıkılaştırma raporu</h1>
    <h2>Rapor Üretim Tarihi: """ + tarih +"""
    </h2>
"""
        alt_kisim = """
</body>
</html>
    """
        try:
            con = sqlite3.connect("veriler.db")
            cur = con.cursor()
            kontrol = cur.execute('''select * from kontroller order by tarih desc''').fetchall()
            dosya = open(self.dizin+"/STIG4Pardus_"+tarih+".html", "w")
            dosya.write(ust_kisim)
            # print(kontrol)
            for i in kontrol:
                kontroller_id = i[0]
                tarih = i[1]
                basarili_adet = i[2]
                basarisiz_adet = i[3]

                ic_ust = """
<div class="table-responsive-vertical shadow-z-1" onclick="elementDisplay('""" + str(kontroller_id) + """')"><table id="table0" class="table table-hover table-mc-light-blue">
            <thead>
                <tr>
                      <th><font style="font-weight:bold;">Tarih: """ + str(tarih) + """</font></th>
                      <th><font style="font-weight:bold;" color="green" >Geçti: """ + str(basarili_adet) + """</font></th>
                      <th><font style="font-weight:bold;" color="red" >Kaldı: """ + str(basarisiz_adet) + """</font></th>
                      <th style="text-align:right"><font style="font-weight:bold;">(Detaylar için Tıklayın)</font></th>
                </tr>
            </thead>
  </table>
  </div>
        <div class="table-responsive-vertical shadow-z-1" id=\"""" + str(kontroller_id) + """\" style="display: none;">
            <!-- Table starts here -->
            <table id="table" class="table table-hover table-mc-light-blue">
            <thead>
                <tr>
                      <th><font style="font-weight:bold;">Kural ID</font></th>
                      <th><font style="font-weight:bold;">Kural Başlığı</font></th>
                      <th><font style="font-weight:bold;">Öncelik</font></th>
                      <th><font style="font-weight:bold;">Durum</font></th>
                </tr>
            </thead>
            <tbody>
                """
                dosya.write(ic_ust)
                kontrol_detay = cur.execute(
                    '''select * from kontroller_detay where kontroller_id = ? order by durum desc''',
                    (kontroller_id,)).fetchall()

                for j in kontrol_detay:
                    kural_id = j[3]
                    durum = j[2]

                    if int(durum) == 1:
                        renk = "green"
                        yazi = "GEÇTİ"
                    else:
                        renk = "#FE4365"
                        yazi = "KALDI"

                    kural_detay = cur.execute('''select * from kurallar where kural_id = ?''',
                                              (str(kural_id),)).fetchone()

                    onem = kural_detay[2]
                    baslik = kural_detay[3]
                    aciklama = kural_detay[4]
                    aranacak_icerik = kural_detay[5]
                    cozum = kural_detay[6]

                    ic_orta = (
                        (
                            (
                                (
                                    """
<tr><td data-title="ID">"""
                                    + str(kural_id)
                                    + """</td>
<td data-title="ID">"""
                                    + str(baslik)
                                    + """</td>
<td data-title="ID">"""
                                    + str(onem)
                                    + """</td>
<td data-title="ID"><font color=\""""
                                    + renk
                                )
                                + """\">"""
                            )
                            + yazi
                        )
                        + """</font></td></tr>

                    """
                    )
                    dosya.write(ic_orta)

                    """
                    liste.append({
                        'kural_id': kural_id,
                        'durum': durum,
                        'onem': onem,
                        'baslik': baslik,
                        'aciklama': aciklama,
                        'aranacak_icerik': aranacak_icerik,
                        'cozum': cozum
                    })
                """
                ic_alt = """
</tbody>
</table>
</div>
"""
                dosya.write(ic_alt)
                """
                data["sonuclar"].append({
                    'kontroller_id': kontroller_id,
                    'tarih': tarih,
                    'basarili_adet': basarili_adet,
                    'basarisiz_adet': basarisiz_adet,
                    'durum_detay': liste
                })"""
                        # ('/var/www/html/dump_all'+str(datetime.datetime.now())+'.json', 'w')
            dosya.write(alt_kisim)
            dosya.close()
                # print(data)
        except Exception as hata:
            print("Yazılımcı ile iletişime geçin, hata(html): ", hata)

    def output_kontrol(self):
        try:
            dosya = open("output.txt", "r").readlines()
            print(f"Kontrol edilen adet: {len(dosya)}")
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
            tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            con = sqlite3.connect("veriler.db")
            cur = con.cursor()
            cur.execute(
                '''insert into kontroller(tarih, basarili_adet, basarisiz_adet) values(?, ?, ?)''',
                (tarih, str(gecen), str(kalan)),
            )
            con.commit()
            kontrol = cur.execute(
                '''select kontroller_id from kontroller where tarih = ?''',
                (tarih,),
            ).fetchone()[0]

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
        except Exception as hata:
            print("Yazılımcı ile iletişime geçin, hata(output_kontrol): ", hata)

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

    def json_uret(self):
        try:
            con = sqlite3.connect("veriler.db")
            cur = con.cursor()

            data = {"sonuclar": []}
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

                data["sonuclar"].append({
                    'kontroller_id': kontroller_id,
                    'tarih': tarih,
                    'basarili_adet': basarili_adet,
                    'basarisiz_adet': basarisiz_adet,
                    'durum_detay' : liste
                })

                #(dizin+'dump_all_'+str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))+'.json', 'w')
            with open(f'{self.dizin}/dump_all_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.json', 'w') as dosya_ciktisi_json:
                json.dump(data, dosya_ciktisi_json)
                #print(data)
        except Exception as hata:
            print("Yazılımcı ile iletişime geçin, hata(json): ", hata)

    def kontrol(self, x):
        try:
            self.dizin = str(x)
            print ("Başlıyoruz...")
            print ("Scriptler Çalıştırılıyor...")

            for line in self.run_command("sudo bash stig4pardus_bash_kontrol"):
                try:
                    veri = line.decode("utf-8").split("\n")[0]
                    #print(veri)
                except Exception as hata:
                    print(line)
            print("Output Kontrol...")
            self.output_kontrol()
            print("JSON Üretiliyor...", dizin, "Konumuna...")
            self.json_uret()
            print("HTML Üretiliyor...", dizin, "Konumuna...")
            self.html_uret()
            print("Tüm işlemler tamam!")

        except Exception as hata:
            print("Yazılımcı ile iletişime geçin, hata(kontrol): ", hata)
        #print("Veritabanına ekliyorum...")


#baslat = Stig4Pardus_Kontrol().kontrol("/var/www/html/xx") #nesnemiz.
#baslat.kontrol() #tüm kontrolleri gerçekleştirme
#baslat.output_kontrol() #sadece output okuyup veritabanına eklemek.