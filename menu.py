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
    thread_map = {
"metode bypass":None,
"allfaucet":modul.allfaucet,
"btccanyon":modul.btccanyon,
"claimbits":modul.claimbits,
"claimlite":modul.claimlite,
"clickscoin":modul.clickscoin,
"coinfola":modul.coinfola,
"earnsolana":modul.earnsolana,
"eurofaucet_de":modul.eurofaucet_de,
"faucetcrypto_net":modul.faucetcrypto_net,
"faucetspeedbtc":modul.faucetspeedbtc,
"freeclaimfaucet":modul.freeclaimfaucet,
"james_trussy":modul.james_trussy,
"ltchunt":modul.ltchunt,
"paidtomoney":modul.all_in_one,
"rushbitcoin":modul.rushbitcoin,
"tikiearn":modul.tikiearn,
"earnrub_pw":modul.earnrub_pw,
"cryptohits":modul.cryptohits,
"instanfaucet_xyz":modul.instanfaucet_xyz,
"earn-crypto_co":modul.earn_crypto,
"earnbits_io":modul.earnbits,
#"timps_co Maintenance":modul.timps_co,
#"vie_faucet Maintenance":modul.vie_faucet,
"whoopyrewards":modul.whoopyrewards,
"cryptoearns":modul.cryptoearns,
"gulio_site":modul.gulio,
"cryptask":modul.cryptask,
"faucetpayz":modul.faucetpayz,
"nevcoin":modul.nevcoin,
"paidlink":modul.paidlink,
"faucet_mom":modul.faucet_mom,
"faucetbob":modul.faucetbob,
}
    menu_dict=list(thread_map.items())
    if len(sys.argv) == 2:
      tele=True
      select = sys.argv[1]
      fl=sys.argv[0]
    else:
      tele=None
      fl=sys.argv[0]
      os.system("clear")
      
  
      # Cetak judul banner menu
      banner.banner(' MAIN MENU ')
  
      # Muat data dari file JSON
      
      
      # Cetak daftar menu
      menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(thread_map.keys())]
      if len(menu_items) % 2 != 0:
          menu_items.append("")
      menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
      cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))

          #time.sleep(0.1)
  
      # Meminta input pengguna
      select = input(putih1 + "select : ")
    if select == "0":
        print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
        sel = input(putih1 + "select : ")
        if sel == "0":
            api_key = input("Api key captcha ai > ")
            with open("ckey.txt", "w") as e:
                e.write(api_key)
            menu(banner,modul,modulesl)
        exit()
    else:
        selected_index = int(select)
        if 0 <= selected_index < len(menu_dict):
          _, selected_function = menu_dict[selected_index]
          selected_function(modulesl, banner)