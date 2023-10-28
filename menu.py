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
    "faucetpayz":modul.faucetpayz,
    "nevcoin":modul.nevcoin,
    "proearn.site":modul.proearn,
    "litecoinbits":modul.litecoinbits,
    "ptctask":modul.ptctask,
    "webshort":modul.webshort,
    "lazyfaucet":modul.lazyfaucet,
    }
    micin = {
    "coinfola":modul.coinfola,
    "earnsolana":modul.earnsolana,
    "faucetspeedbtc":modul.faucetspeedbtc,
    "earnrub_pw":modul.earnrub_pw,
    "instanfaucet_xyz":modul.instanfaucet_xyz,
    "whoopyrewards":modul.whoopyrewards,
    "paidlink":modul.paidlink,
    "chillfaucet":modul.chillfaucet,
    "keforcash":modul.keforcash,
    "claimcoin_in":modul.claimcoin_in,
    #"dotfaucet":modul.dotfaucet,
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
    menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(menu.keys())]
    if len(menu_items) % 2 != 0:
        menu_items.append("")
    menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
    cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))
    select = input(putih1 + "select : ")
    if select == "0":
        print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
        print(f"{putih1}[{hijau1}1{putih1}]{biru1}.Solver Captcha Tg(@Xevil_check_bot)")
        sel = input(putih1 + "select : ")
        if sel == "0":
            api_key = input("Api key captcha ai > ")
            with open("ckey.txt", "w") as e:
                e.write(api_key)
        if sel == "1":
            api_key = input("Api key Xevil > ")
            with open("xkey.txt", "w") as e:
                e.write(api_key)
            #menu(banner,modul,modulesl)
        exit()
    if select == "1":
        menu_dict=list(Bits_Family.items())
        os.system("clear")
        banner.banner(' BITS FAMILY MENU ')
        menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(Bits_Family.keys())]
        if len(menu_items) % 2 != 0:
            menu_items.append("")
        menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
        cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))
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
        cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))
        select = input(putih1 + "select : ")
        selected_index = int(select)
        if 0 <= selected_index < len(menu_dict):
          _, selected_function = menu_dict[selected_index]
          selected_function(modulesl, banner)
        