import webbrowser
import glob
import os

log_dizini = "/var/log/stig4pardus/"


class Son_Eklenen_Sinif():

    def duzenleme_getir(self):
        try:
            # print(1)
            files_path = os.path.join("../", '*')
            return sorted(
                glob.iglob(files_path), key=os.path.getctime, reverse=True
            )
        except Exception as hata:
            print(hata)


    def baslat(self,files):
        if len(files) > 1:
            webbrowser.open_new_tab(log_dizini + str(files[0]))
            webbrowser.open_new_tab(log_dizini + str(files[1]))
