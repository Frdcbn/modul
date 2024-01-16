import pathlib
import threading
import os
import time
import datetime
import json,sys,queue
from rich.panel import Panel
from rich import print as cetak
def menu(banner,modul,modulesl):
    hijau1 = "\033[1;92m"  # Terang
    kuning1 = "\033[1;93m"  # Terang
    putih1 = "\033[1;97m"  # Terang
    merah1 = "\033[1;91m"  # Terang
    biru1 = "\033[1;94m"  # Terang
    Bits_Family ={
    "btccanyon":modul.btccanyon,
    "claimbits":modul.claimbits,
    "claimlite":modul.claimlite,
    "ltchunt":modul.ltchunt,
    "rushbitcoin":modul.rushbitcoin,
    #"earn-crypto_co":modul.earn_crypto,
    "earnbits_io":modul.earnbits,
    "nevcoin":modul.nevcoin,
    "proearn.site":modul.proearn,
    "litecoinbits":modul.litecoinbits,
    "ptctask":modul.ptctask,
    "earnbitmoon_club":modul.earnbitmoon,
    "earnbitmoon_xyz":modul.earnbitmoon_xyz,
    }
    micin = {
    #"coinfola":modul.coinfola,
    #"earnsolana":modul.earnsolana,
    "faucetspeedbtc":modul.faucetspeedbtc,
    "whoopyrewards":modul.whoopyrewards,
    #"chillfaucet":modul.chillfaucet,
    "keforcash":modul.keforcash,
    "claimcoin_in":modul.claimcoin_in,
    "coinpayz":modul.coinpayz,
    "wildfaucet":modul.wildfaucet,
    "liteearn":modul.liteearn,
    #"cryptofuture":modul.cryptofuture,
    #"freeltc":modul.freeltc,
    "insfaucet":modul.insfaucet,
    "cryptoviefaucet":modul.cryptoviefaucet,
    "claimcash":modul.claimcash,
    "bitupdate":modul.bitupdate,
    "queenofferwall":modul.queenofferwall,
    "hatecoin":modul.hatecoin,
    "nobitafc":modul.nobitafc,
    #"tartaria_faucet":modul.tartaria_faucet,
    #"1xbitcoins":modul._1xbitcoins,
    #"feyorra":modul.feyorra,
    #"claim88":modul.claim88,
    "claimcoins":modul.claimcoins,
    "litefaucet":modul.litefaucet,
    #"claimfreetrx_online(BTC)":modul.claimfreetrx,
    "earncryptowrs":modul.earncryptowrs,
    "tokenmix_pro":modul.tokenmix_pro,
    "kiddyearner":modul.kiddyearner,
    "cryptoearns":modul.cryptoearns,
    "autofaucet_org":modul.autofaucet_org,
    "autoclaim_in":modul.autoclaim_in,
    "autobitco_in":modul.autobitco_in,
    }
    menu={
      "settings":None,
      "bits family":None,
      "micin family":None
    }
    menu_dict = list(Bits_Family.items()) + list(micin.items())
    tele=None
    fl=sys.argv[0]
    os.system("clear")
    banner.banner(' MAIN MENU ')
    cetak(Panel('sekarang ada metode baru yaitu scrape api kalian ke settings lalu setting api key dari scrape api untuk link web api keynya https://www.scraperapi.com/ dan ini terdapat limit kalian cek api key secara berkala ketika sudah limit ganti api keynya'.center(80), width=70, title="[bold green] PENGUMUMAN PENTING", padding=(0, 2), style="bold white"))
    menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(menu.keys())]
    if len(menu_items) % 2 != 0:
        menu_items.append("")
    menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
    cetak(Panel(menu_content, width=70, title="[bold green]Menu Bot", padding=(0, 2), style="bold white"))
    select = input(putih1 + "select : ")
    if select == "0":
        print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
        print(f"{putih1}[{hijau1}1{putih1}]{biru1}.Solver Captcha Tg(@Xevil_check_bot)")
        print(f"{putih1}[{hijau1}2{putih1}]{biru1}.Scraper api")
        print(f"{putih1}[{hijau1}3{putih1}]{biru1}.Set jeda setelah berhasil membypass shortlinks")
        print(f"{putih1}[{hijau1}4{putih1}]{biru1}.Set multi bypass shortlinks dapat mempercepat proses")
        sel = input(putih1 + "select : ")
        if sel == "0":
            api_key = input("Api key captcha ai > ")
            with open("ckey.txt", "w") as e:
                e.write(api_key)
        elif sel == "1":
            api_key = input("Api key Xevil > ")
            with open("xkey.txt", "w") as e:
                e.write(api_key)
        elif sel == "2":
            api_key = input("Api key > ")
            with open("sca.txt", "w") as e:
                e.write(api_key)
            #menu(banner,modul,modulesl)
        elif sel == "3":
          if os.path.exists('settings.json'):
            data=json.loads(open('settings.json').read())
          else:
            data={"timer":None,"multi":None}
          data["timer"]=input('masukan angka, ini di hitung dalam detik dan ini akan di random contoh 45,160 ini akan acak mulai dari 45 sampai 60 pisahkan dengan koma : ')
          with open('settings.json','w') as f:
            json.dump(data, f)
        elif sel == "4":
          if os.path.exists('settings.json'):
            data=json.loads(open('settings.json').read())
          else:
            data={"timer":None,"multi":None}
          data["multi"]=input('aktifkan mode multi bypass shortlinks? y/n: ').lower()
          with open('settings.json','w') as f:
            json.dump(data, f)
        exit()
    if select == "1":
        menu_dict=list(Bits_Family.items())
        os.system("clear")
        banner.banner(' BITS FAMILY MENU ')
        menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(Bits_Family.keys())]
        if len(menu_items) % 2 != 0:
            menu_items.append("")
        menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
        cetak(Panel(menu_content, width=70, title="[bold green]Menu Bot", padding=(0, 2), style="bold white"))
        select = input(putih1 + "select : ")
        selected_index = int(select)
        if 0 <= selected_index < len(menu_dict):
          _, selected_function = menu_dict[selected_index]
          selected_function(modulesl, banner)
    if select == "2":
        menu_dict=list(micin.items())
        os.system("clear")
        banner.banner(' MICIN FAMILY MENU ')
        menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(micin.keys())]
        if len(menu_items) % 2 != 0:
            menu_items.append("")
        menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
        cetak(Panel(menu_content, width=70, title="[bold green]Menu Bot", padding=(0, 2), style="bold white"))
        select = input(putih1 + "select : ")
        selected_index = int(select)
        if 0 <= selected_index < len(menu_dict):
          _, selected_function = menu_dict[selected_index]
          selected_function(modulesl, banner)
        