import banner,modul,modulesl
import pathlib
import threading
import os
def de():
 try:
  for hapus in open('list').read().splitlines():
    current_directory = pathlib.Path.cwd()
    file_name = hapus+'.py'
    file_path = current_directory / file_name
    file_path.unlink()
 except:pass
def menu():
  os.system("clear")
  de()
  hijau1 = "\033[1;92m"#Terang
  kuning1 = "\033[1;93m"#Terang
  putih1 = "\033[1;97m"#Terang
  merah1 = "\033[1;91m"#Terang
  biru1 = "\033[1;94m"#Terang
  banner.banner("MAIN MENU")
  print(f"{putih1}[{hijau1}0{putih1}]{biru1}.METHOD BYPASS")
  print(f"{putih1}[{hijau1}1{putih1}]{biru1}.BTCCAYON")
  print(f"{putih1}[{hijau1}2{putih1}]{biru1}.COINGAX")
  print(f"{putih1}[{hijau1}3{putih1}]{biru1}.CLAIMSATOSHI")
  select = input(putih1+"select : ")
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
  if select == "0":
    print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
    sel=input(putih1+"select : ")
    if sel == "0":
      api_key=input("Api key captcha ai > ")
      with open("ckey.txt","w") as e:
        e.write(api_key)
      menu()
    exit()
