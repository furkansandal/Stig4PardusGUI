import sqlite3

class Parse():

    def __init__(self):
        self.klasor = "stig4pardus-master/stig-pardus-17.txt"

    def parcalara_ayir(self):
        d = open(self.klasor, "r").read()
        kurallara_bol = d.split("Kural_ID:")
        s0 = 0
        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        for i in kurallara_bol:
            onemlere_bol = i.split("Onem:")
            for j in onemlere_bol:
                #print(j.encode("utf-8"))
                kural_basligi_bol = j.split("Kural_Basligi:")
                for k in kural_basligi_bol:
                    aciklama_bol = k.split("Aciklama:")
                    for l in aciklama_bol:
                        aranan_icerik_bol = l.split("Aranacak_icerik:")

                        for g in aranan_icerik_bol:
                            cozum_bol = g.split("Cozum:")
                            print(cozum_bol)

                            """
                            for h in cozum_bol:
                                print(h.encode("utf-8"))
                            """
            print("------------------------------")
    def kurallari_db_ekle(self):
        d = open(self.klasor, "r").read()
        kurallara_bol = d.split("\n\n")

        con = sqlite3.connect("veriler.db")
        cur = con.cursor()
        for i in kurallara_bol:
            if i[0] == "K":
                k_id = i.split("Onem:")
                onem = k_id[1].split("Kural_Basligi:")
                kural_basligi = onem[1].split("Aciklama:")
                aciklama = kural_basligi[1].split("Aranacak_icerik:")
                aranacak_icerik = aciklama[1].split("Cozum:")
                k_id_son = k_id[0].split("Kural_ID:")[1]
                onem_son = onem[0]
                kural_basligi_son = kural_basligi[0]
                aciklama_son = aciklama[0]
                aranacak_icerik_son = aranacak_icerik[0]
                cozum_son = aranacak_icerik[1]
                while (k_id_son[0] == " "):
                    k_id_son = k_id_son[1:]
                while (onem_son[0] == " "):
                    onem_son = onem_son[1:]
                while (kural_basligi_son[0] == " "):
                    kural_basligi_son = kural_basligi_son[1:]
                while (aciklama_son[0] == " "):
                    aciklama_son = aciklama_son[1:]
                while (aranacak_icerik_son[0] == " "):
                    aranacak_icerik_son = aranacak_icerik_son[1:]
                while (cozum_son[0] == " "):
                    cozum_son = cozum_son[1:]

                #-1: son karakteri bul
                #:-1 son karakter hariç

                while (k_id_son[-1:] == " "):
                    k_id_son = k_id_son[:-1]
                while (onem_son[-1:] == " "):
                    onem_son = onem_son[:-1]
                while (kural_basligi_son[-1:] == " "):
                    kural_basligi_son = kural_basligi_son[:-1]
                while (aciklama_son[-1:] == " "):
                    aciklama_son = aciklama_son[:-1]
                while (aranacak_icerik_son[-1:] == " "):
                    aranacak_icerik_son = aranacak_icerik_son[:-1]
                while (cozum_son[-1:] == " "):
                    cozum_son = cozum_son[:-1]

                #

                while (k_id_son[-1:] == "\n"):
                    k_id_son = k_id_son[:-1]
                while (onem_son[-1:] == "\n"):
                    onem_son = onem_son[:-1]
                while (kural_basligi_son[-1:] == "\n"):
                    kural_basligi_son = kural_basligi_son[:-1]
                while (aciklama_son[-1:] == "\n"):
                    aciklama_son = aciklama_son[:-1]
                while (aranacak_icerik_son[-1:] == "\n"):
                    aranacak_icerik_son = aranacak_icerik_son[:-1]
                while (cozum_son[-1:] == "\n"):
                    cozum_son = cozum_son[:-1]


                #print(onem_son)

                cur.execute('''insert into kurallar(kural_id, onem, baslik, aciklama, aranacak_icerik, cozum) values (?, ?, ?, ?, ?, ?)''',
                            (str(k_id_son), str(onem_son), str(kural_basligi_son), str(aciklama_son), str(aranacak_icerik_son), str(cozum_son),))
                con.commit()
        con.close()




        #print(len(onemlere_bol), type(onemlere_bol[0]), onemlere_bol[0])
        """kural_basligi_bol = onemlere_bol.split("Kural_Basligi:")
            aciklama_bol = kural_basligi_bol.split("Aciklama:")
            aranan_icerik_bol = aciklama_bol.split("Aranacak_icerik:")
            cozum_bol = aranan_icerik_bol.split("Cozum:")"""
        print("--------")

        """
                            for h in cozum_bol:
                                print(h.encode("utf-8"))
        """
        print("------------------------------")



p = Parse()
p.kurallari_db_ekle() #Tüm kuralları veritabanına ekledik. Şuan için ihtiyaç yok.