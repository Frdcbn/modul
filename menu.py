import banner,btccayon,modulesl
import pathlib
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
  select = input(putih1+"select : ")
  if select == "1":
    btccayon.main(modulesl,banner)
  if select == "0":
    print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
    sel=input(putih1+"select : ")
    if sel == "0":
      api_key=input("Api key captcha ai > ")
      with open("ckey.txt","w") as e:
        e.write(api_key)
      menu()
  else:
    print(merah1+'PILIH YANG BENER COK!')
    exit()
menu()