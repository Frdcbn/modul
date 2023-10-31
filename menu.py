import pathlib
import threading
import os
import time
import datetime
import json,sys,queue
from rich.panel import Panel
from rich import print as cetak
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'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'))))
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
    "coinpayz":modul.coinpayz,
    "wildfaucet":modul.wildfaucet,
    "liteearn":modul.liteearn,
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
        