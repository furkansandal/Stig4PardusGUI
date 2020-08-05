import argparse
from stig_4_pardus_kural_kontrol import *

versiyon = "1.0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--kontrol", "-k", help="Kontrol İşlemini Başlatmak İçin Bu Parametreyi Verin",action="store_true")
    parser.add_argument("--versiyon", "-v", help="Versiyon Kontrol Etmek İçin Bu Parametreyi Verin", action="store_true")
    parser.add_argument("--dizin", "-d", help="Log Dizini Değiştirmek İçin Bu Parametreyi Verin (Boş bırakırsanız: /var/www/html/ e kayıt eder)")

    args = parser.parse_args()

    if not args.kontrol and not args.versiyon:
        parser.print_help()
    else:
        if args.versiyon:
            print("Uygulama versiyonu:" , versiyon)
            quit()
        if args.kontrol:
            if args.dizin is not None:
                dizin = args.dizin
            else:
                dizin = "/var/www/html/"
            #print(dizin)
            nesne = Stig4Pardus_Kontrol()
            nesne.kontrol(dizin)