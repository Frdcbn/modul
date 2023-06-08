import pathlib
import threading
import os,time,datetime,json
def menu(banner,modul,modulesl):
  os.system("clear")
  hijau1 = "\033[1;92m"#Terang
  kuning1 = "\033[1;93m"#Terang
  putih1 = "\033[1;97m"#Terang
  merah1 = "\033[1;91m"#Terang
  biru1 = "\033[1;94m"#Terang
  banner.banner("MAIN MENU")
  data = load_data()
  print(f"{putih1}[{hijau1}0{putih1}]{biru1}.METHOD BYPASS (waktu: {convrt(data['0'])}")
  print(f"{putih1}[{hijau1}1{putih1}]{biru1}.BTCCAYON (waktu: {convrt(data['1'])}")
  print(f"{putih1}[{hijau1}2{putih1}]{biru1}.COINGAX (waktu: {convrt(data['2'])}")
  print(f"{putih1}[{hijau1}3{putih1}]{biru1}.CLAIMSATOSHI (waktu: {convrt(data['3'])}")
  print(f"{putih1}[{hijau1}4{putih1}]{biru1}.COINFOLA (waktu: {convrt(data['4'])}")
  print(f"{putih1}[{hijau1}5{putih1}]{biru1}.CLAIMLITE (waktu: {convrt(data['5'])}")
  print(f"{putih1}[{hijau1}6{putih1}]{biru1}.SIMPLEADS (waktu: {convrt(data['6'])}")
  print(f"{putih1}[{hijau1}7{putih1}]{biru1}.ADHIVES (waktu: {convrt(data['7'])}")
  print(f"{putih1}[{hijau1}8{putih1}]{biru1}.EARNSOLANA (waktu: {convrt(data['8'])}")
  print(f"{putih1}[{hijau1}9{putih1}]{biru1}.CLAIM.RO (waktu: {convrt(data['9'])}")
  print(f"{putih1}[{hijau1}10{putih1}]{biru1}.BTCADSPACE (waktu: {convrt(data['10'])}")
  print(f"{putih1}[{hijau1}11{putih1}]{biru1}.RUSHBITCOIN (waktu: {convrt(data['11'])}")
  print(f"{putih1}[{hijau1}12{putih1}]{biru1}.CLAIMBITS (waktu: {convrt(data['12'])}")
  print(f"{putih1}[{hijau1}13{putih1}]{biru1}.LTCHUNT (waktu: {convrt(data['13'])}")
  print(f"{putih1}[{hijau1}14{putih1}]{biru1}.FAUCETCRYPTO_NET (waktu: {convrt(data['14'])}")
  print(f"{putih1}[{hijau1}15{putih1}]{biru1}.FAUCET4U (waktu: {convrt(data['15'])}")
  print(f"{putih1}[{hijau1}16{putih1}]{biru1}.NOKOFAUCET (waktu: {convrt(data['16'])}")
  print(f"{putih1}[{hijau1}17{putih1}]{biru1}.FAUCETSPEEDBTC (waktu: {convrt(data['17'])}")
  print(f"{putih1}[{hijau1}18{putih1}]{biru1}.COINZASK (waktu: {convrt(data['18'])}")
  print(f"{putih1}[{hijau1}19{putih1}]{biru1}.TIKIEARN (waktu: {convrt(data['19'])}")
  print(f"{putih1}[{hijau1}20{putih1}]{biru1}.ALLFAUCET (waktu: {convrt(data['20'])}")
  print(f"{putih1}[{hijau1}21{putih1}]{biru1}.BITMONK (waktu: {convrt(data['21'])}")
  select = input(putih1+"select : ")
  waktu_terakhir_dipilih = time.time()
  save(waktu_terakhir_dipilih,select)
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
  if select == "4":
    thread = threading.Thread(target=modul.coinfola, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "5":
    thread = threading.Thread(target=modul.claimlite, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "6":
    thread = threading.Thread(target=modul.simpleads, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "8":
    thread = threading.Thread(target=modul.earnsolana, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "7":
    thread = threading.Thread(target=modul.adhives, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "9":
    thread = threading.Thread(target=modul.claim_ro, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "10":
    thread = threading.Thread(target=modul.btcadspace, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "11":
    thread = threading.Thread(target=modul.rushbitcoin, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "12":
    thread = threading.Thread(target=modul.claimbits, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "13":
    thread = threading.Thread(target=modul.ltchunt, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "14":
    thread = threading.Thread(target=modul.faucetcrypto_net, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "15":
    thread = threading.Thread(target=modul.faucet4u, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "16":
    thread = threading.Thread(target=modul.nokofaucet, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "17":
    thread = threading.Thread(target=modul.faucetspeedbtc, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "18":
    thread = threading.Thread(target=modul.coinzask, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "19":
    thread = threading.Thread(target=modul.tikiearn, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "20":
    thread = threading.Thread(target=modul.allfaucet, args=(modulesl,banner))
    thread.start()
    thread.join()
  if select == "21":
    thread = threading.Thread(target=modul.bitmonk, args=(modulesl,banner))
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
def save(waktu_terakhir_dipilih, select):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
    
    if not os.path.exists(file_path):
        data = {}
        for i in range(23):
            data[str(i)] = None
        with open(file_path, "w") as file:
            json.dump(data, file)
    else:
        with open(file_path, "r") as file:
            data = json.load(file)
            
    if select in data:
        data[select] = waktu_terakhir_dipilih
    else:
        data[str(select)] = waktu_terakhir_dipilih
    
    with open(file_path, "w") as file:
        json.dump(data, file)

def load_data():
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

    if not os.path.exists(file_path):
        data = {}
        for i in range(22):
            data[str(i)] = None
        with open(file_path, "w") as file:
            json.dump(data, file)
    else:
        with open(file_path, "r") as file:
            data = json.load(file)

    return data
def convrt(waktu):
 if waktu == None:
   return "-"
 else:
  return datetime.datetime.fromtimestamp(waktu).strftime('%Y-%m-%d %H:%M:%S')
def add_data(angka):
  with open('data.json') as file:
    data = json.load(file)
  data[angka] = None
  with open('data.json', 'w') as file:
      json.dump(data, file)