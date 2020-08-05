import argparse
from yedek_siniflar.stig_4_pardus_kural_kontrol import *

versiyon = "1.0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--kontrol", "-k", help="Kontrol İşlemini Başlatmak İçin Bu Parametreyi Verin",action="store_true")
    parser.add_argument("-v", "--versiyon", help="Versiyon Kontrol Etmek İçin Bu Parametreyi Verin", action="store_true")

    # Read arguments from the command line
    args = parser.parse_args()

    # Check for --widt"
    if args.kontrol is None and args.versiyon is None:
        parser.print_help()
    else:
        if args.versiyon:
            print("Uygulama versiyonu:" , versiyon)
            quit()
        if args.kontrol:
            nesne = Stig4Pardus_Kontrol()
            nesne.kontrol()