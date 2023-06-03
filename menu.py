from mrbadut_modul import banner,btccayon
import os
def menu():
  os.system("clear")
  hijau1 = "\033[1;92m"#Terang
  kuning1 = "\033[1;93m"#Terang
  putih1 = "\033[1;97m"#Terang
  merah1 = "\033[1;91m"#Terang
  biru1 = "\033[1;94m"#Terang
  banner.banner("MAIN MENU")
  print(f"{putih1}[{hijau1}1{putih1}]{biru1}.BTCCAYON")
  select = input(putih1+"select : ")
  if select == "1":
    btccayon.main()
  else:
    print(merah1+'PILIH YANG BENER COK!')
    exit()