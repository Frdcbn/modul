import pathlib
import threading
import os
import time
import datetime
import json,sys,queue

def menu(banner,modul,modulesl):
    hijau1 = "\033[1;92m"  # Terang
    kuning1 = "\033[1;93m"  # Terang
    putih1 = "\033[1;97m"  # Terang
    merah1 = "\033[1;91m"  # Terang
    biru1 = "\033[1;94m"  # Terang
    menu_dict = {
    0: "method bypass",
    1: "adhives",
    2: "allfaucet",
    3: "bitmonk",
    4: "bot_tele",
    5: "btcadspace",
    6: "btccanyon",
    7: "claim_ro",
    8: "claimbits",
    9: "claimlite",
    10: "claimsatoshi",
    11: "clickscoin",
    12: "coinfola",
    13: "coingax",
    14: "coinpay_faucet",
    15: "coinsfarm",
    16: "coinzask",
    17: "crypto2u",
    18: "cryptofuture",
    19: "cryptogenz",
    20: "earnfree_cash",
    21: "earnsolana",
    22: "endenfaucet",
    23: "eurofaucet_de",
    24: "faucet4u",
    25: "faucetcrypto_net",
    26: "faucetpayz",
    27: "faucetspeedbtc",
    28: "freeclaimfaucet",
    29: "james_trussy",
    30: "landofbits",
    31: "ltchunt",
    32: "nokofaucet",
    33: "paid_family",
    34: "paidbucks",
    35: "rushbitcoin",
    36: "simpleads",
    37: "tefaucet",
    38: "tikiearn",
    39: "tron0x"
}
    data=load_data(menu_dict)
    if len(sys.argv) == 2:
      tele=True
      select = sys.argv[1]
      fl=sys.argv[0]
    else:
      tele=None
      os.system("clear")
      
  
      # Cetak judul banner menu
      banner.banner(' MAIN MENU ')
  
      # Muat data dari file JSON
      
      # Cetak daftar menu
      for key, value in menu_dict.items():
          print(f"{putih1}[{hijau1}{str(key)}{putih1}]{kuning1}.{value.upper()} {putih1}( {hijau1}last run {putih1}: {hijau1}{convrt(data[str(key)])}{putih1})")
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
"1":modul.adhives,
"2":modul.allfaucet,
"3":modul.bitmonk,
"4":modul.bot_tele,
"5":modul.btcadspace,
"6":modul.btccanyon,
"7":modul.claim_ro,
"8":modul.claimbits,
"9":modul.claimlite,
"10":modul.claimsatoshi,
"11":modul.clickscoin,
"12":modul.coinfola,
"13":modul.coingax,
"14":modul.coinpay_faucet,
"15":modul.coinsfarm,
"16":modul.coinzask,
"17":modul.crypto2u,
"18":modul.cryptofuture,
"19":modul.cryptogenz,
"20":modul.earnfree_cash,
"21":modul.earnsolana,
"22":modul.endenfaucet,
"23":modul.eurofaucet_de,
"24":modul.faucet4u,
"25":modul.faucetcrypto_net,
"26":modul.faucetpayz,
"27":modul.faucetspeedbtc,
"28":modul.freeclaimfaucet,
"29":modul.james_trussy,
"30":modul.landofbits,
"31":modul.ltchunt,
"32":modul.nokofaucet,
"33":modul.all_in_one,
"34":modul.paidbucks,
"35":modul.rushbitcoin,
"36":modul.simpleads,
"37":modul.tefaucet,
"38":modul.tikiearn,
"39":modul.tron0x,
}
        if select in thread_map:
            if select=='4':
              print(f"{putih1}[{hijau1}1{putih1}]{kuning1}.Run bot ")
              print(f"{putih1}[{hijau1}2{putih1}]{kuning1}.Settings id akun utama")
              pilih=input(putih1+'Select : ')
              if pilih=="1":
                c_=None
                cek_p=None
                data_queue = queue.Queue()
                stop_event = threading.Event()
                receive_thread = threading.Thread(target=modul.receive_data1, args=(data_queue, stop_event))
                receive_thread.start()
                modul.bot_tele(modulesl,banner,menu_dict,thread_map,data_queue,fl)
              if pilih == "2":
                kata=input("masukan id owner : ")
                nama_file = "owner.txt"
                with open(nama_file, "w") as file:
                  for huruf in kata.split(","):
                    file.write(huruf + '\n')
            else:
                thread = threading.Thread(target=thread_map[select], args=(modulesl, banner,tele))
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

