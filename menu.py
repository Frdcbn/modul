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
"adhives":modul.adhives,
"allfaucet":modul.allfaucet,
"bot_tele":modul.bot_tele,
"btcadspace":modul.btcadspace,
"btccanyon":modul.btccanyon,
"claimbits":modul.claimbits,
"claimlite":modul.claimlite,
"claimsatoshi":modul.claimsatoshi,
"clickscoin":modul.clickscoin,
"coinfola":modul.coinfola,
"coinpay_faucet":modul.coinpay_faucet,
#"coinzask":modul.coinzask,
"earnfree_cash":modul.earnfree_cash,
"earnsolana":modul.earnsolana,
"eurofaucet_de":modul.eurofaucet_de,
"faucetcrypto_net":modul.faucetcrypto_net,
"faucetspeedbtc":modul.faucetspeedbtc,
"freeclaimfaucet":modul.freeclaimfaucet,
"james_trussy":modul.james_trussy,
"ltchunt":modul.ltchunt,
"nokofaucet":modul.nokofaucet,
"paid_family":modul.all_in_one,
"paidbucks":modul.paidbucks,
"rushbitcoin":modul.rushbitcoin,
"tefaucet":modul.tefaucet,
"tikiearn":modul.tikiearn,
"cryptoscoop_online":modul.cryptoscop,
"earnrub_pw":modul.earnrub_pw,
"cryptohits":modul.cryptohits,
"instanfaucet_xyz":modul.instanfaucet_xyz,
"coinsmash_xyz":modul.coinsmash,
"earn-crypto_co":modul.earn_crypto,
"earnbits_io":modul.earnbits,
"timps_co":modul.timps_co,
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

# If the number of menu items is odd, add an empty string to make it even
      if len(menu_items) % 2 != 0:
          menu_items.append("")
      
      # Create two columns for the menu
      menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
      
      # Display the menu panel
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
        
            if select=='3':
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
              #  global fl
                modul.bot_tele(modulesl,banner,menu_dict,thread_map,data_queue,fl)
              if pilih == "2":
                kata=input("masukan id owner : ")
                nama_file = "owner.txt"
                with open(nama_file, "w") as file:
                  for huruf in kata.split(","):
                    file.write(huruf + '\n')
            else:
             #   global menu_dict
                selected_index = int(select)
                if 0 <= selected_index < len(menu_dict):
                  _, selected_function = menu_dict[selected_index]
                  selected_function(modulesl, banner, tele)