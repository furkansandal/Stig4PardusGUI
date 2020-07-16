#!venv python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from main_gui import Ui_MainWindow
from islem_detay_gui import Ui_Form
import subprocess
from time import sleep

#Detay sınıfımız eğer splash olarak açmak istersek;
class DetaySinif(QWidget):


    def __init__(self):
        super().__init__()

        self.ui = Ui_Form() #islem_detay_gui deki sınıfımızı oluşturdul.
        self.ui.setupUi(self) #nesnenin setup fonksiyonunu çalıştırdık.

    def guncelle_label(self, yazi): #ortadaki label'ı güncellemek istersek eğer guncelle_label(text) gönderimi yapabilirsiniz.
        self.ui.label.setText(yazi)



class BaslaticiSinif(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.sayi = 0 QT testi sırasında kullanıldı şuan boş.

    def run_command(self, command): #komut çalıştırdığımız fonksiyom
        p = subprocess.Popen(command,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True) #subprocess sınıfını kullandık ve out error olarak subprocess pipe ı oluşturdul.
        # Buffer boş olana kadar subprocess ten stdout aldık.
        for line in iter(p.stdout.readline, b''):
            if line:  # Boş satıları zıplayalım :)
                yield line
        # This ensures the process has completed, AND sets the 'returncode' attr
        while p.poll() is None:
            sleep(.1)  # CPU-cycle larına yakalanmayalım...
        # Boş STDERR buffer
        err = p.stderr.read()
        if p.returncode != 0:
            # run_command() fonksiyonu STDERR yakalarsa eğer;
            print("Hata: " + str(err.decode("utf-8").split("\n")[0]))

    def calistir(self):
        print(self.ui.secilenVeri.currentText()) #buton çalışma testi seçili olan veriyi sadece print et

    def teksefer(self):
        self.ui.sure.setEnabled(False) #tek sefer seçili olursa süreyi devre dışı bırak


    def surekli(self):
        self.ui.sure.setEnabled(True) #sürekli seçeneği seçilirse sure text alanını aktif ettik.


    def tamamini_calistir(self):
        print("tamamı başladı")
        #QMessageBox.about(self, "Title", "Message")
        #self.detay = DetaySinif()
        #self.detay.show()
        #self.sayi = self.sayi + 1
        dosya = open("log.txt", "w") #tüm çıktıları log.txt ye kayıt edelim.
        #for line in self.run_command("ping 8.8.8.8 -c 6"):
        for line in self.run_command("sudo bash /usr/lib/stig4pardus/stig4pardus -s"):
            try:
                veri = line.decode("utf-8").split("\n")[0]
                print(veri)
                self.ui.cikti_label.setText(veri)
                dosya.write(veri + "\n")
                QApplication.processEvents()
            except Exception as hata:
                print(line)

        self.ui.cikti_label.setText("İşlem tamamlandı... Logları kontrol ediniz...")
        dosya.close()
        QApplication.processEvents()



uygulama = QApplication([])
pencere = BaslaticiSinif()
pencere.show()
uygulama.exec_()