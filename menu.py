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
    "22": "LANDOFBITS",
    "23": "COINSFARM",
    "24": "CRYPTO2U",
    "25": "JAMES-TRUSSY",
    "26": "COINPAY-FAUCET",
    "27": "EUROFAUCET_DE",
    "28": "TEFAUCET.ONLINE",
    "29": "OSKUT",
    "30": "EDENFAUCET",
    "31": "CRYPTOFUTURE",
    "32": "FREECLAIMFAUCET",
    "33": "CRYPTOGENZ",
    "34": "CCTIP",
}
    data=load_data(menu_dict)
    # Cetak daftar menu
    for key, value in menu_dict.items():
        print(f"{putih1}[{hijau1}{key}{putih1}]{kuning1}.{value} {putih1}( {hijau1}last run {putih1}: {hijau1}{convrt(data[key])}{putih1})")
        time.sleep(0.1)

    # Meminta input pengguna
    select = input(putih1 + "select : ")
    waktu_terakhir_dipilih = time.time()
    save(waktu_terakhir_dipilih, select, menu_dict, data)

    if select == "0":
        print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
        sel = input(putih1 + "select : ")
        if sel == "0":
            api_key = input("Api key captcha ai > ")
            with open("ckey.txt", "w") as e:
                e.write(api_key)
            menu()
        exit()
    else:
        thread_map = {
            "1": modul.btccanyon,
            "2": modul.coingax,
            "3": modul.claimsatoshi,
            "4": modul.coinfola,
            "5": modul.claimlite,
            "6": modul.simpleads,
            "7": modul.adhives,
            "8": modul.earnsolana,
            "9": modul.claim_ro,
            "10": modul.btcadspace,
            "11": modul.rushbitcoin,
            "12": modul.claimbits,
            "13": modul.ltchunt,
            "14": modul.faucetcrypto_net,
            "15": modul.faucet4u,
            "16": modul.nokofaucet,
            "17": modul.faucetspeedbtc,
            "18": modul.coinzask,
            "19": modul.tikiearn,
            "20": modul.allfaucet,
            "21": modul.bitmonk,
            "22": modul.landofbits,
            "23": modul.coinsfarm,
            "24": modul.crypto2u,
            "25": modul.james_trussy,
            "26": modul.coinpay_faucet,
            "27": modul.eurofaucet_de,
            "28": modul.tefaucet,
            "29": modul.oskut,
            "30": modul.endenfaucet,
            "31": modul.cryptofuture,
            "32": modul.freeclaimfaucet,
            "33": modul.cryptogenz,
            "34": modul.bot_tele
        }
    
        if select in thread_map:
            if '34' in select:
              print(f"{putih1}[{hijau1}1{putih1}]{kuning1}.Run bot ")
              print(f"{putih1}[{hijau1}2{putih1}]{kuning1}.Settings kata ")
              pilih=input(putih1+'Select : ')
              if pilih=="1":
                modul.bot_tele(modulesl,banner)
              if pilih == "2":
                kata=input("masukan kata pisahkan dengan koma (misal aja ini mah,nah ini yang kedua) : ")
                nama_file = "data.txt"
                if not os.path.exists(nama_file):
                    with open(nama_file, "w") as file:
                      for huruf in kata.split(","):
                        file.write(huruf + '\n')
                else:
                  with open(nama_file, 'a') as file:
                    for data in kata.split(","):
                        file.write(data + '\n')

            else:
              thread = threading.Thread(target=thread_map[select], args=(modulesl, banner))
              thread.start()
              thread.join()


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

