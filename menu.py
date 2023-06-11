import pathlib
import threading
import os
import time
import datetime
import json

def menu(banner,modul,modulesl):
    os.system("clear")
    hijau1 = "\033[1;92m"  # Terang
    kuning1 = "\033[1;93m"  # Terang
    putih1 = "\033[1;97m"  # Terang
    merah1 = "\033[1;91m"  # Terang
    biru1 = "\033[1;94m"  # Terang

    # Cetak judul banner menu
    banner.banner(' MAIN MENU ')

    # Muat data dari file JSON
    menu_dict = {
    "0": "METHOD BYPASS",
    "1": "BTCCAYON",
    "2": "COINGAX",
    "3": "CLAIMSATOSHI",
    "4": "COINFOLA",
    "5": "CLAIMLITE",
    "6": "SIMPLEADS",
    "7": "ADHIVES",
    "8": "EARNSOLANA",
    "9": "CLAIM.RO",
    "10": "BTCADSPACE",
    "11": "RUSHBITCOIN",
    "12": "CLAIMBITS",
    "13": "LTCHUNT",
    "14": "FAUCETCRYPTO_NET",
    "15": "FAUCET4U",
    "16": "NOKOFAUCET",
    "17": "FAUCETSPEEDBTC",
    "18": "COINZASK",
    "19": "TIKIEARN",
    "20": "ALLFAUCET",
    "21": "BITMONK",
    "22": "OSKUT",
    "23": "LANDOFBITS",
    "24": "COINSFARM",
    "25": "CRYPTO2U",
    "26": "JAMES-TRUSSY",
    "27": "COINPAY-FAUCET",
    "28": "EUROFAUCET_DE",
}
    data=load_data(menu_dict)
    # Cetak daftar menu
    for key, value in menu_dict.items():
        print(f"{putih1}[{hijau1}{key}{putih1}]{biru1}.{value} (waktu: {convrt(data[key])})")

    # Meminta input pengguna
    select = input(putih1 + "select : ")
    waktu_terakhir_dipilih = time.time()
    save(waktu_terakhir_dipilih, select, menu_dict, data)

    if select == "1":
      thread = threading.Thread(target=modul.btccanyon, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "2":
      thread = threading.Thread(target=modul.coingax, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "3":
      thread = threading.Thread(target=modul.claimsatoshi, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "4":
      thread = threading.Thread(target=modul.coinfola, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "5":
      thread = threading.Thread(target=modul.claimlite, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "6":
      thread = threading.Thread(target=modul.simpleads, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "8":
      thread = threading.Thread(target=modul.earnsolana, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "7":
      thread = threading.Thread(target=modul.adhives, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "9":
      thread = threading.Thread(target=modul.claim_ro, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "10":
      thread = threading.Thread(target=modul.btcadspace, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "11":
      thread = threading.Thread(target=modul.rushbitcoin, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "12":
      thread = threading.Thread(target=modul.claimbits, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "13":
      thread = threading.Thread(target=modul.ltchunt, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "14":
      thread = threading.Thread(target=modul.faucetcrypto_net, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "15":
      thread = threading.Thread(target=modul.faucet4u, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "16":
      thread = threading.Thread(target=modul.nokofaucet, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "17":
      thread = threading.Thread(target=modul.faucetspeedbtc, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "18":
      thread = threading.Thread(target=modul.coinzask, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "19":
      thread = threading.Thread(target=modul.tikiearn, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "20":
      thread = threading.Thread(target=modul.allfaucet, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "21":
      thread = threading.Thread(target=modul.bitmonk, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "22":
      thread = threading.Thread(target=modul.oskut, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "23":
      thread = threading.Thread(target=modul.landofbits, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "24":
      thread = threading.Thread(target=modul.coinsfarm, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "25":
      thread = threading.Thread(target=modul.crypto2u, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "26":
      thread = threading.Thread(target=modul.james_trussy, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "27":
      thread = threading.Thread(target=modul.coinpay_faucet, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "28":
      thread = threading.Thread(target=modul.eurofaucet_de, args=(modulesl,banner))
      thread.start()
      thread.join()
    if select == "0":
      print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
      sel=input(putih1+"select : ")
      if sel == "0":
        api_key=input("Api key captcha ai > ")
        with open("ckey.txt","w") as e:
          e.write(api_key)
        menu()
      exit()

def save(waktu_terakhir_dipilih, select, menu_dict, data):
    file_path = "data.json"

    if not os.path.exists(file_path):
        data = {}
        for key in menu_dict.keys():
            data[str(key)] = None
    else:
        with open(file_path, "r") as file:
            data = json.load(file)

    if select in data:
        data[select] = waktu_terakhir_dipilih
    else:
        max_key = max(map(int, data.keys())) if data else -1
        new_key = str(max_key + 1)
        data[new_key] = waktu_terakhir_dipilih

    with open(file_path, "w") as file:
        json.dump(data, file)


def load_data(menu_dict):
    file_path = "data.json"

    if not os.path.exists(file_path):
        data = {}
        for key in menu_dict.keys():
            data[str(key)] = None
        with open(file_path, "w") as file:
            json.dump(data, file)
    else:
        with open(file_path, "r") as file:
            data = json.load(file)

        # Tambahkan entri baru ke data jika ada menu baru yang ditambahkan
        for key in menu_dict.keys():
            if key not in data:
                data[key] = None
            elif data[key] == '':
                data[key] = None

    return data

def convrt(waktu):
    if waktu is None:
        return "-"
    else:
        return datetime.datetime.fromtimestamp(waktu).strftime('%Y-%m-%d %H:%M:%S')

