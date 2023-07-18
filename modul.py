from libtmux import Server
import requests,json,time,asyncio,re
from os import system
import shutil,os
from time import sleep
import random
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
from http.cookies import SimpleCookie
from urllib.parse import urlparse,urlencode
from tqdm import tqdm
from pyfiglet import figlet_format 
import pathlib
from telethon import TelegramClient, sync, events
import subprocess
import threading
import os
import requests,queue
from PIL import Image, ImageDraw, ImageFont
import socket
FONT_URL = "https://github.com/stamen/toner-carto/raw/master/fonts/Arial-Unicode-Bold.ttf"  # Ganti dengan URL font yang valid
FONT_PATH = "Arial-Unicode-Bold.ttf"  # Path font yang diinginkan
def tiktok_downloader(url, output_name):
    try:
        server_url = 'https://musicaldown.com/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "TE": "trailers"
        }
        session = requests.Session()
        session.headers.update(headers)
        req = session.get(server_url)
        data = {}
        parse = BeautifulSoup(req.text, 'html.parser')
        input_elements = parse.find_all('input')
        for i in input_elements:
            if i.get("id") == "link_url":
                data[i.get("name")] = url
            else:
                data[i.get("name")] = i.get("value")
        post_url = server_url + "id/download"
        req_post = session.post(post_url, data=data, allow_redirects=True)
        if req_post.status_code == 302 or 'This video is currently not available' in req_post.text or 'Video is private or removed!' in req_post.text:
            print('- video private or remove')
            return 'private/remove'
        elif 'Submitted Url is Invalid, Try Again' in req_post.text:
            print('- url is invalid')
            return 'url-invalid'
        get_all_blank = BeautifulSoup(req_post.text, 'html.parser').find_all('a', attrs={'target': '_blank'})
        download_link = get_all_blank[0].get('href')
        r = requests.get(download_link)
        with open(output_name, "wb") as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return True
    except IndexError:
        return False
def receive_data1(data_queue, stop_event):
    # Menerima data dari skrip pertama
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 2222)  # Ganti dengan alamat dan port yang sesuai
    sock.bind(server_address)
    sock.listen(1)
    print('Menunggu koneksi...')
    
    while not stop_event.is_set():
        try:
            connection, client_address = sock.accept()
            data = connection.recv(1024)
            if data:
                sleep(1)
                print(f'Data diterima dari skrip pertama: {data.decode()}')
                data_queue.put(data.decode())  # Menambahkan data ke dalam queue
        except Exception as e:
            print(f'Error saat menerima data: {str(e)}')
        finally:
            if connection:
                connection.close()
def send_signal1(port, message):
  try:
    # Inisialisasi socket
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_server_address = ('localhost', 11112)
    send_sock.connect(send_server_address)

    # Mengirim pesan ke script1
    send_sock.sendall(message.encode())

    # Menutup koneksi
    send_sock.close()
    return None
  except Exception as e:
    return str(e)
def download_font_if_not_exist(font_url, font_path):
    if not os.path.exists(font_path):
        response = requests.get(font_url)
        with open(font_path, "wb") as font_file:
            font_file.write(response.content)
def text_to_image(name):
    # Konfigurasi font
    capture_command = f"tmux capture-pane -p -t {name} -J"
    text = subprocess.check_output(capture_command, shell=True).decode('utf-8')
    font_size = 30
    
    download_font_if_not_exist(FONT_URL, FONT_PATH)
    font = ImageFont.truetype(FONT_PATH, font_size)
    
    # Mendapatkan ukuran gambar berdasarkan ukuran teks
    text_width, text_height = font.getsize_multiline(text)
    
    # Membuat gambar kosong dengan latar belakang putih
    image = Image.new("RGB", (text_width, text_height), "white")
    draw = ImageDraw.Draw(image)
    
    # Menulis teks pada gambar
    draw.text((0, 0), text, font=font, fill="black")
    
    # Menyimpan gambar
    image.save(name + ".png")
    return "image berhasil di simpan"
def parse_data(data):
    parsed_data = {}
    try:
        parsed_json = json.loads(data)
        coins = parsed_json["coins"]
        for coin in coins:
            coin_name = coin["coin"]
            balance = coin["balance"]
            parsed_data[coin_name] = balance
    except (KeyError, json.JSONDecodeError) as e:
        print("Error parsing data:", str(e))
    
    return parsed_data
def create_tmux_session(session_name, script_path,fl):
  try:
    server = Server()
    session = server.new_session(session_name)
    window = session.attached_window
    pane = window.attached_pane
    pane.send_keys(f'python '+fl+' '+script_path, enter=True)
  except Exception as e:
    return str(e)
def list_sessions():
    server = Server()
    sessions = server.list_sessions()
    session_names = [str("`"+session.get("session_name")+"`") for session in sessions]
    return session_names
def kill_session(session_name):
  try:
    server = Server()
    server.kill_session(session_name)
    return "Success kill session"
  except Exception as e:
    return str(e)
def parse_rupiah_saldo(data):
    for data in data.splitlines():
     if "Saldo" in data:
         return ''.join(data.split('├└ Saldo : ')[1].split(','))
        # break
def get_balance_cctip(data):
  balance_data = {}
  lines = data.split('\n')
  for line in lines:
      if not line.startswith('Available Balance') and ':' in line and 'Try /balance' not in line:
          key, value = line.split(': ')
          balance_data[key] = value

  return balance_data
def random_sleep():
    # Menghasilkan waktu sleep acak antara 5 hingga 35 detik
    sleep_time = random.randint(3, 7)
    return sleep_time
def animasi(menit):
  detik = menit * 60
  pattern_list = list("▁▃▅▇▅▃▁") * detik
  for i in range(detik):
      animasi = "".join(pattern_list[i:i+5])
      output = f"[{animasi}] - Please wait {detik//60:02d}:{detik%60:02d}"
      print(output, end='\r')
      time.sleep(1)
      detik -= 1
c_=None
cek_p=None
def bot_tele(modulesl,banner,menu_dict,thread_map,data_queue,fl):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner('BOT CCTIP')
  api_id = 9209038
  owner=open('owner.txt').read().splitlines()[0]
  api_hash = '82d6f5d828fc5f5942e29bdfc1e01d14'
  nomor=open('nomor.txt').read().splitlines()[0]
  async def handle_new_message(event):
    global cek_p
    global c_
    #global data_queue
    message = event.message
    #print(message)
    pesan=message.text
    id_tip=["962775809","6285122310","5796879502","1380459388","6143654908","5311716983"]
    if '/command' in message.text:
      if str(message.from_id.user_id) == owner:
        await message.reply('''
  silahkan gunakan command seperti ini `/kirim_saldo nama_bot jumlah nama_coinya`
  silahkan gunakan command seperti ini `/cek_saldo nama_bot`
  ''')
    if '/kirim_saldo' in message.text:
      if  str(message.from_id.user_id) == owner:
        if ' ' not in message.text:
          await message.reply('silahkan gunakan command seperti ini `/kirim_saldo nama_bot jumlah nama_coinya`')
        else:
          name_bot=['cctip','mahawallet','payfun']
          mes=message.text.split(' ')
          #print(mes)
          if mes[1].lower() in name_bot:
            if mes[1].lower() == 'cctip':
              if mes[2].lower() == 'all':
                if len(mes) == 3:
                  await client.send_message(entity="@cctip_bot",message="🏦My Wallet")
                  sleep(1)
                  pas=await client.get_messages(entity="@cctip_bot",limit=1)
                 # if str(message.from_id.user_id) in id_tip:
                  #if 'Available Balance:' in pesan:
                  bal=get_balance_cctip(pas[0].message)
                 # print(bal)
                  for nama,jumlah in bal.items():
                    if jumlah != "0":
                      await message.reply('/tip '+jumlah+' '+nama)
                    sleep(2)
                else:
                  await client.send_message(entity="@cctip_bot",message="🏦My Wallet")
                  sleep(1)
                  pas=await client.get_messages(entity="@cctip_bot",limit=1)
                 # if str(message.from_id.user_id) in id_tip:
                  #if 'Available Balance:' in pesan:
                  bal=get_balance_cctip(pas[0].message)
                  try:
                    await message.reply('/tip '+bal[mes[3].upper()]+' '+mes[3])
                  except Exception as e:
                    await message.reply('Coin not found')
              else:
                    bal=get_balance_cctip(message.text)
                    await message.reply('/tip '+mes[2]+' '+mes[3])
            if mes[1].lower() == 'payfun':
              if mes[2].lower() == 'all':
                await client.send_message(entity="@PayFun_tip_bot",message="💰Balance")
                sleep(3)
                pas=await client.get_messages(entity="@PayFun_tip_bot",limit=1)
                saldo=pas[0].message.splitlines()[0].replace("saldo lu: Rp", "").strip()
                await message.reply('/cip '+saldo)
              else:
                await message.reply('/cip '+mes[2])
            if mes[1].lower() == 'mahawallet':
              if mes[2].lower() == 'all':
                await client.send_message(entity="@MahaWalletBot",message="💰 Saldo")
                sleep(5)
                pas=await client.get_messages(entity="@MahaWalletBot",limit=1)
              #  print(pas[0].message)
                saldo=parse_rupiah_saldo(pas[0].message)
              #  print(saldo)
                await message.reply('/kirim '+saldo)
              else:
                await message.reply('/kirim '+mes[2])
          else:
            await message.reply('''maaf seperti nya bot tip itu tidak di dukung bot tip yang di dukung
  - `CCTIP`
  - `MAHA WALLET` 
  - `PAYFUN`''')
    if '/cek_saldo' in message.text:
      if  str(message.from_id.user_id) == owner:
        if ' ' not in message.text:
          await message.reply('silahkan gunakan command seperti ini `/cek_saldo nama_bot`')
        else:
          name_bot=['cctip','mahawallet','payfun']
          mes=message.text.split(' ')
          #print(mes)
          if mes[1].lower() in name_bot:
            if mes[1].lower() == 'cctip':
              await client.send_message(entity="@cctip_bot",message="🏦My Wallet")
              sleep(2)
              pas=await client.get_messages(entity="@cctip_bot",limit=1)
              await message.reply(pas[0].message)
            if mes[1].lower() == 'payfun':
              await client.send_message(entity="@PayFun_tip_bot",message="💰Balance")
              sleep(3)
              pas=await client.get_messages(entity="@PayFun_tip_bot",limit=1)
              await message.reply(pas[0].message)
            if mes[1].lower() == 'mahawallet':
              await client.send_message(entity="@MahaWalletBot",message="💰 Saldo")
              sleep(3)
              pas=await client.get_messages(entity="@MahaWalletBot",limit=1)
              await message.reply(pas[0].message)
    if '/cek_session' in message.text:
      if  str(message.from_id.user_id) == owner:
        sessions = list_sessions()
        await message.reply("\n".join(sessions))
      else:
        await message.reply("BODO AMAT!!")
    if '/kill_session' in message.text:
      if  str(message.from_id.user_id) == owner:
        if ' ' not in message.text:
          await message.reply("gunakan command seperti ini `/kill_session nama_sesi`")
        else:
          nama=message.text.split(' ')[1]
          await message.reply(kill_session(nama))
          cek_p=False
      else:
        await message.reply("BODO AMAT!!")
    if '/menu' in message.text:
      if  str(message.from_id.user_id) == owner:
          menu_text = "\n".join(f"{str(key)}. {value.upper()}" for key, value in menu_dict.items())
          await message.reply("menu script yang ada di script MR.BADUT")
          await message.reply(menu_text)
      else:
        await message.reply("BODO AMAT!!")
    if '/gambar_sesi' in message.text:
      if  str(message.from_id.user_id) == owner:
        if ' ' not in message.text:
          await message.reply("gunakan command seperti ini `/kirim_gambar_sesi nama_sesi`")
        else:
          nama=message.text.split(' ')[1]
          if ',' in nama:
            for nama in nama.split(','):
              status=text_to_image(nama)
              if "image berhasil di simpan" in status:
                await message.reply(status)
               # image_file:
                chat = await message.get_chat()
                sent_message = await client.send_file(chat, nama+".png", caption=f"Gambar sesi {nama}")
                os.remove(nama+".png")
          status=text_to_image(nama)
          if "image berhasil di simpan" in status:
            await message.reply(status)
           # image_file:
            chat = await message.get_chat()
            sent_message = await client.send_file(chat, nama+".png", caption=f"Gambar sesi {nama}")
            os.remove(nama+".png")
            # Reply dengan gambar
          else:
            await message.reply("ERROR")
      else:
        await message.reply("BODO AMAT!!")
    if '/tiktok' in message.text:
      if  str(message.from_id.user_id) == owner:
        c_=message.peer_id.channel_id
        if ' ' not in message.text:
          await message.reply("gunakan command seperti ini `/run_script nomor_menu`")
        else:
          url=message.text.split('/tiktok ')[1]
          ua={
     # 'Host': 'www.tiktok.com',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'dnt': '1',
      'x-requested-with': 'mark.via.gp',
      'sec-fetch-site': 'none',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
      }
          nama=requests.get(url,headers=ua)
          y=bs(nama.text,'html.parser').find('title')
          if '@' in y.text:
            y=y.text.replace('@','')
          else:
            y=y.text
          output_name = y+'.mp4'  # Ganti dengan nama file output yang diinginkan
          result = tiktok_downloader(url, output_name)
          if result == True:
            await message.reply(file=output_name,message="Video telah di download")
            os.remove(output_name)
          else:
            await message.reply("Video gagal di download")
    if '/run' in message.text:
      if  str(message.from_id.user_id) == owner:
        if 'chat_id' in str(message):
          c_=message.peer_id.chat_id
        else:
          c_=message.peer_id.channel_id
        if ' ' not in message.text:
          await message.reply("gunakan command seperti ini `/run_script nomor_menu`")
        else:
          nama=message.text.split(' ')[1]
          await message.reply("Please wait")
          if cek_p == True:
            await message.reply("Maaf sepertinya ada script yang sedang menunggu cookies mohon selesaikan dulu script tersebut sebelum menjalankan yang baru")
          else:
            st=create_tmux_session(menu_dict[int(nama)].upper(), nama,fl)
            if st:
              await message.reply(st)
            else:
              await message.reply("Sukses run script di sesi "+menu_dict[int(nama)].upper())
  
      else:
        await message.reply("BODO AMAT!!")
    if c_ != None:
      if not data_queue.empty():
        inf=await client.get_entity(int(owner))
        await client.send_message(c_, f"@{inf.username} "+data_queue.get())
        cek_p=True
    if '/cookies' in message.text:
      if  str(message.from_id.user_id) == owner:
        if ' ' not in message.text:
          await message.reply("gunakan command seperti ini `/cookies nama_sesi cookies_anda$user_agent`")
        else:
          pesan=message.text
          send_signal1(1111, pesan)
          await message.reply("Data Sukses di save")
          cek_p=None
    if '/select' in message.text:
      if  str(message.from_id.user_id) == owner:
        if ' ' not in message.text:
          await message.reply("gunakan command seperti ini `/select nama_sesi nomor`")
        else:
          pesan=message.text
          send_signal1(1111, pesan)
          await message.reply("Data Sukses di kirim")
          cek_p=None
    print(f'{putih1}[{kuning1} > {putih1}]{hijau1} {pesan}')
    async def send_reply(message, reply,tim):
      async with client.action(message.chat_id, "typing"):  # Mengirim status "sedang mengetik"
          await asyncio.sleep(tim)  # Menunda selama 3 detik
          await client.send_message(message.chat_id,reply)
    if 'pengguna mengumpulkan hujan Anda.' in message.text:
      if str(message.from_id.user_id) in id_tip:
       if message.mentioned:
         pass
    if 'Berhasil sawer' in message.text:
      if str(message.from_id.user_id) in id_tip:
       if message.mentioned:
      #   random_sleep()
         pass
       else:
       #  random_sleep()
         pass
    if 'Airdrop sejumlah ' in message.text:
      if str(message.from_id.user_id) in id_tip:
       if message.mentioned:
      #   random_sleep()
         pass
       else:
       #  random_sleep()
         pass
    if 'users collected your' in message.text:
      if str(message.from_id.user_id) in id_tip:
       if message.mentioned:
        # random_sleep()
         pass
       else:
         pass
    if 'pengguna mengumpulkan undian Anda.' in message.text:
      if str(message.from_id.user_id) in id_tip:
       if message.mentioned:
       #  random_sleep()
         pass
    if 'Membuat undian di ' in message.text:
     if str(message.from_id.user_id) in id_tip:
      # if message.mentioned:
      #   random_sleep()
         pesan=pesan.split("Kirim ")[1].split(" untuk")[0]
         await send_reply(message, pesan,random_sleep())
    if 'Membuat airdrop di ' in message.text:
     if str(message.from_id.user_id) in id_tip:
      # if message.mentioned:
       #  random_sleep()
         pesan=pesan.split("Kirim ")[1].split(" untuk")[0]
         await send_reply(message, pesan,random_sleep())
    if 'Giveaway sejumlah ' in message.text:
     if str(message.from_id.user_id) in id_tip:
      # if message.mentioned:
        # random_sleep()
         pesan=pesan.split("Kata Kunci : `")[1].split("`")[0]
         await send_reply(message, pesan,random_sleep())
    if 'Created an airdrop in ' in message.text:
     if str(message.from_id.user_id) in id_tip:
         pesan=pesan.split("Send `")[1].split("` to")[0]
         await send_reply(message, pesan,random_sleep())
    if 'Created a draw in ' in message.text:
     if str(message.from_id.user_id) in id_tip:
         pesan=pesan.split("Send ")[1].split(" to")[0]
         await send_reply(message, pesan,random_sleep())
    if 'Create Airdrop Success!! ' in message.text:
     if str(message.from_id.user_id) in id_tip:
         pesan=pesan.split("Claim: `")[1].split("`")[0]
         await send_reply(message, pesan,random_sleep())
    if 'Created a giveaway in ' in message.text:
     if str(message.from_id.user_id) in id_tip:
         random_sleep()
         await message.click(text='👉Grab👈')
     #  else:
    await client.send_read_acknowledge(message.to_id, max_id=message.id)
  with TelegramClient('session/' + nomor, api_id, api_hash) as client:
      client.connect()
      if not client.is_user_authorized():
       try:
          client.send_code_request(phone_number)
          me = client.sign_in(phone_number, input(f"{putih1}MASUKAN KODE YANG KAMU TERIMA DI TELEGRAM : "))
          client.disconnect()
          bot_tele(modulesl,banner)
       except Exception as e:
         print(e)
      user = client.get_me()
      print(hijau1+"> "+kuning1+"Account information")
      print(hijau1+"> "+hijau1+f"Name {putih1}: {hijau1}{user.first_name}")
      print(hijau1+"> "+kuning1+"Start bot")
      @client.on(events.NewMessage(chats=client.get_dialogs()))
      async def main(event):
          c_=None
          await handle_new_message(event)
  
      client.start()
      client.run_until_disconnected()
hijau1 = "\033[1;92m"#Terang
kuning1 = "\033[1;93m"#Terang
putih1 = "\033[1;97m"#Terang
merah1 = "\033[1;91m"#Terang
biru1 = "\033[1;94m"#Terang
def send_signal(port, message):
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_server_address = ('localhost', 2222)
    send_sock.connect(send_server_address)

    # Mengirim pesan ke script1
    send_sock.sendall(message.encode())

    # Menutup koneksi
    send_sock.close()
def receive_signal(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 11112)
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print("Menunggu sinyal...")
        sleep(1)
        try:
            # Menerima koneksi dari pengirim
            connection, client_address = sock.accept()

            try:
                # Menerima pesan
                message = connection.recv(1024).decode()

                # Menghandle pesan yang diterima
                if message == None:
                    pass
                else:
                    sock.close()
                    return message
            finally:
                # Menutup koneksi
                sock.close()
        except socket.timeout:
            sock.close()
            return None

    # Return None jika tidak ada pesan masuk dalam waktu 5 detik
    return None
def cache_control(name):
  main_folder = 'cache'
  sub_folder = name
  main_folder_path = pathlib.Path(main_folder)
  if not main_folder_path.exists():
      main_folder_path.mkdir()
  sub_folder_path = main_folder_path / sub_folder
  if not sub_folder_path.exists():
      sub_folder_path.mkdir()
def data_control(name):
  main_folder = 'data'
  sub_folder = name
  main_folder_path = pathlib.Path(main_folder)
  if not main_folder_path.exists():
      main_folder_path.mkdir()
  sub_folder_path = main_folder_path / sub_folder
  if not sub_folder_path.exists():
      sub_folder_path.mkdir()
def save_data(tele,name=None):
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
            data = json.load(file)
            cookies = data.get('cookies')
            user_agent = data.get('user_agent')
            print(tele)
            if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim cookies dan User-Agent anda pisahkan dengan dolar($) contoh : `/cookies nama_sesi csrf=xxx$Mozillaxxx`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                cookies,user_agent=mes.split(name.upper()+' ')[1].split('$')
            else:
                print(f'{putih1}[{kuning1} ~ {putih1}] {hijau1}User-Agent sudah ada tetap update User-Agent? jika User-Agent sudah di update tetap cf gunakan User-Agent : XYZ/3.0')
                jawab = input('y/n : '.lower())
                if jawab == 'y':
                  user_agent = input(hijau1 + 'Masukkan User-Agent mu > ')
                cookies = input(hijau1 + 'Masukkan cookies mu > ')
            data = {
                'cookies': cookies,
                'user_agent': user_agent
            }
            with open(f'data/{name}/{name}.json', 'w') as file:
                json.dump(data, file)
          #  return cookies, user_agent
    except FileNotFoundError:
          if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim cookies dan User-Agent anda pisahkan dengan dolar($) contoh : `/cookies nama_sesi csrf=xxx$Mozillaxxx`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                cookies,user_agent=mes.split(name.upper()+' ')[1].split('$')
          else:
              cookies = input(hijau1 + 'Masukkan cookies mu > ')
              user_agent = input(hijau1 + 'Masukkan User-Agent mu > ')
          data = {
              'cookies': cookies,
              'user_agent': user_agent
          }
          with open(f'data/{name}/{name}.json', 'w') as file:
              json.dump(data, file)
          return cookies, user_agent
def load_data(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          cookies = data['cookies']
          user_agent = data['user_agent']
          return cookies, user_agent
      except FileNotFoundError:
          return None, None
def btccanyon(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("BTCCANYON")
  data_control('btccanyon')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/btccanyon/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('btccanyon')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://btccanyon.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://btccanyon.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/btccanyon/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://btccanyon.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('btccanyon')
  if not os.path.exists("data/btccanyon/btccanyon.json"):
    save_data(tele,'btccanyon')
    btccanyon(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'btccanyon')
    btccanyon(modulesl,banner,tele)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,'btccanyon')
    btccanyon(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://btccanyon.com/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://btccanyon.com/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
  del get_id[0]
  for _id in get_id:
   sesi=False
   while(sesi==False):
    _i=_id["onclick"].split("opensite('")[1].split("','")[0]
    key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
    get_reward=curl.get(f'https://btccanyon.com/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
    token1=get_reward.text.split("var token = '")[1].split("';")[0]
    secon=get_reward.text.split("var secs = ")[1].split(";")[0]
    for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
            time.sleep(1)
            pass
    answer=get_answer()
    reward=json.loads(curl.post('https://btccanyon.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
    if reward["status"] == 200:
      gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      sesi=True
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      providers = {
        'clks.pro': modulesl.clks_pro,
        'linksly.co': modulesl.linksly,
        'shrinkearn.com': modulesl.shrinkearn,
        'fc.lc': modulesl.fl_lc,
        'clk.sh': modulesl.clksh,
        'linksfly.me': modulesl.linksfly,
        'shortsfly.me': modulesl.shortfly,
        'chainfo.xyz': modulesl.chainfo,
        'flyzu.icu': modulesl.flyzu,
        'adshorti.xyz': modulesl.adshorti_xyz,
        'usalink.io': modulesl.usalink,
        'birdurls.com': modulesl.birdurl,
        'owllink.net': modulesl.owlink,
        'clickzu.icu': modulesl.clickzu_icu,
        'shortzu.icu': modulesl.shortzu_icu,
        'zuba.link': modulesl.zuba_link,
        'mitly.us': modulesl.mitly,
        'illink.net': modulesl.illink_net,
        'exe.io': modulesl.exe_io,
        'insfly.pw': modulesl.insfly,
        'linkvor.pw': modulesl.linkvor_pw,
        'linkjust.com': modulesl.linkjust,
        'cashurl.win': modulesl.cashurl_win,
        'shorti.io': modulesl.shorti_io,
        'oii.io': modulesl.oii,
        'ex-foary.com': modulesl.ex_foary_com,
      }
      if any(provider in name for provider in providers):
        provider = next(provider for provider in providers if provider in name)
        for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
            get_sl = curl.get('https://btccanyon.com/shortlinks.html', headers=ua, cookies=cookies)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            status = True
            while(status==True):
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                get_lk = json.loads(curl.post('https://btccanyon.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                if get_lk["status"] == 200:
                    answer = providers[provider](get_lk['shortlink'])
                    if 'failed to bypass' in answer:
                        print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                    if answer:
                        try:
                            get_sl = curl.get(answer, headers=ua, cookies=cookies)
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                            print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                        except:
                            print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                    break
                if get_lk['status'] == 600:
                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                else:
                  print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                  break
   except Exception as e:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://btccanyon.com/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LdzF6MlAAAAACcN9JGXW8tSs4dy1MjeKZKFJ11M',get_sl.url)
    g=json.loads(curl.post('https://btccanyon.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="Please wait..."):
            time.sleep(1)
def faucetgigs(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("FAUCETGIGS")
  data_control('faucetgigs')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/faucetgigs/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('faucetgigs')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://faucetgigs.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://faucetgigs.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/faucetgigs/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://faucetgigs.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('faucetgigs')
  if not os.path.exists("data/faucetgigs/faucetgigs.json"):
    save_data(tele,'faucetgigs')
    faucetgigs(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://faucetgigs.com/?page=shortlinks',headers=ua,cookies=cookies)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'faucetgigs')
    faucetgigs(modulesl,banner,tele)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,'faucetgigs')
    faucetgigs(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://faucetgigs.com/?page=ptc',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://faucetgigs.com/?page=ptc',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  for _id in get_id:
   if 'Reward' not in _id:
     pass
   else:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://btccanyon.com/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://btccanyon.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://faucetgigs.com/?page=shortlinks',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  for i in gt_s:
     try:
      name=i.find('td',{'class':'align-middle'}).text
      id=i.find('button',{'class':'btn btn-success btn-sm'})
     # print(name)
      if None == id:
        pass
      else:
        providers = {
          'clks.pro': modulesl.clks_pro,
          'linksly.co': modulesl.linksly,
          'shrinkearn.com': modulesl.shrinkearn,
          'fc.lc': modulesl.fl_lc,
          'clk.sh': modulesl.clksh,
          'linksfly.me': modulesl.linksfly,
          'shortsfly.me': modulesl.shortfly,
          'chainfo.xyz': modulesl.chainfo,
          'flyzu.icu': modulesl.flyzu,
          'adshorti.xyz': modulesl.adshorti_xyz,
          'usalink.io': modulesl.usalink,
          'birdurls.com': modulesl.birdurl,
          'owllink.net': modulesl.owlink,
          'clickzu.icu': modulesl.clickzu_icu,
          'shortzu.icu': modulesl.shortzu_icu,
          'zuba.link': modulesl.zuba_link,
          'mitly.us': modulesl.mitly,
          'illink.net': modulesl.illink_net,
          'exe.io': modulesl.exe_io,
          'insfly.pw': modulesl.insfly,
          'linkvor.pw': modulesl.linkvor_pw,
          'linkjust.com': modulesl.linkjust,
          'cashurl.win': modulesl.cashurl_win,
          'shorti.io': modulesl.shorti_io,
          'oii.io': modulesl.oii,
          'ex-foary.com': modulesl.ex_foary_com,
        }
        if any(provider in name for provider in providers):
          provider = next(provider for provider in providers if provider in name)
          for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
              get_sl = curl.get('https://faucetgigs.com/?page=shortlinks', headers=ua, cookies=cookies)
              token = get_sl.text.split("var token = '")[1].split("';")[0]
              status = True
              while(status==True):
                  da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                  get_lk = json.loads(curl.post('https://faucetgigs.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                  if get_lk["status"] == 200:
                      answer = providers[provider](get_lk['shortlink'])
                      if 'failed to bypass' in answer:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                      if answer:
                          try:
                              get_sl = curl.get(answer, headers=ua, cookies=cookies)
                              sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                              print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                              print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                          except:
                              print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                      break
                  if get_lk['status'] == 600:
                      print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                  else:
                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                    break
     except Exception as e:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
   try:
    get_sl=curl.get('https://faucetgigs.com/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    y=get_answer()
    g=json.loads(curl.post('https://faucetgigs.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&challenge=false&response=false",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser")
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.text.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
   except Exception as e:
     pass
def claimlite(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("CLAIMLITE")
  data_control('claimlite')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/claimlite/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('claimlite')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://claimlite.club/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://claimlite.club/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/claimlite/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://claimlite.club/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('claimlite')
  if not os.path.exists("data/claimlite/claimlite.json"):
    save_data(tele,'claimlite')
    claimlite(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'claimlite')
    claimlite(modulesl,banner,tele)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,'claimlite')
    claimlite(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://claimlite.club/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://claimlite.club/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
 # del get_id[0]
  for _id in get_id:
   sesi=False
   while(sesi==False):
    _i=_id["onclick"].split("opensite('")[1].split("','")[0]
    key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
    get_reward=curl.get(f'https://claimlite.club/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
    token1=get_reward.text.split("var token = '")[1].split("';")[0]
    secon=get_reward.text.split("var secs = ")[1].split(";")[0]
    for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
            time.sleep(1)
            pass
    answer=get_answer()
    reward=json.loads(curl.post('https://claimlite.club/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
    if reward["status"] == 200:
      gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      sesi=True
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      providers = {
        'clks': modulesl.clks_pro,
        'adshort': modulesl.adshorti_xyz,
        'ctr': modulesl.ctrsh,
        'ez4short': modulesl.ez4short,
        'usalink': modulesl.usalink,
        'bitads': modulesl.bitads,
        'shrinkme': modulesl.shrinkme,
        'chainfo': modulesl.chainfo,
        'cuty': modulesl.cuty_io,
        'exe': modulesl.exe_io,
        'oii': modulesl.oii,
        'try2link': modulesl.try2,
      }
      if any(provider in name for provider in providers):
        provider = next(provider for provider in providers if provider in name)
        for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
            get_sl = curl.get('https://claimlite.club/shortlinks.html', headers=ua, cookies=cookies)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            status = True
            while(status==True):
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                get_lk = json.loads(curl.post('https://claimlite.club/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                if get_lk["status"] == 200:
                    answer = providers[provider](get_lk['shortlink'])
                    if 'failed to bypass' in answer:
                        print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                    if answer:
                        try:
                            get_sl = curl.get(answer, headers=ua, cookies=cookies)
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                            print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                        except:
                            print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                    break
                if get_lk['status'] == 600:
                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                else:
                  print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                  break
   except Exception as e:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://claimlite.club/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Leen-YUAAAAAFsd9t6qwRGyF8fLf6kixqicahQj',get_sl.url)
    g=json.loads(curl.post('https://claimlite.club/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def rushbitcoin(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("RUSHBITCOIN")
  data_control('rushbitcoin')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/rushbitcoin/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('rushbitcoin')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://rushbitcoin.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://rushbitcoin.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/rushbitcoin/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://rushbitcoin.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data('rushbitcoin')
  if not os.path.exists("data/rushbitcoin/rushbitcoin.json"):
    save_data(tele,'rushbitcoin')
    rushbitcoin(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'rushbitcoin')
    rushbitcoin(modulesl,banner,tele)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,'rushbitcoin')
    rushbitcoin(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://rushbitcoin.com/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://rushbitcoin.com/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
 # del get_id[0]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://rushbitcoin.com/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://rushbitcoin.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,'rushbitcoin')
     rushbitcoin(modulesl,banner,tele)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  websites = {
    'shrinkme.link': modulesl.shrinkme,
    'Gainl': modulesl.gain_lk,
    'exe.io': modulesl.exe_io,
    'adshort.co': modulesl.adshorti_co,
    'Clks': modulesl.clks_pro,
    'Shrinlearn': modulesl.shrinkearn,
    'Adshorti': modulesl.adshorti_xyz,
  }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://rushbitcoin.com/shortlinks.html', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://rushbitcoin.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                break
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                          break
    except:
        pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://rushbitcoin.com/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LfokMEUAAAAAEwBx23jh3mlghwTF7VJqbN9fERK',get_sl.url)
    g=json.loads(curl.post('https://rushbitcoin.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(420)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def claimbits(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  nama_host="claimbits"
  host="claimbits.net"
  banner.banner(nama_host.upper())
  data_control(''+nama_host+'')
  def save_data(tele,name):
    try:
            if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim cookies dan User-Agent anda pisahkan dengan dolar($) contoh : `/cookies nama_sesi csrf=xxx$Mozillaxxx`")
              mes=receive_signal(1111)
              if "CLAIMBITS" in mes:
                cookies,user_agent=mes.split('CLAIMBITS ')[1].split('$')
            else:
              cookies = input(hijau1 + 'Masukkan cookies mu > ')
              user_agent = input(hijau1 + 'Masukkan User-Agent mu > ')
            data = {
                'cookies': cookies,
                'user_agent': user_agent
            }
            with open(f'data/{name}/{name}.json', 'w') as file:
                json.dump(data, file)
          #  return cookies, user_agent
    except FileNotFoundError:
        if tele == True:
            send_signal(1111,f"`{name.upper()}` mengirim request input, kirim cookies dan User-Agent anda pisahkan dengan dolar($) contoh : `/cookies nama_sesi csrf=xxx$Mozillaxxx`")
            mes=receive_signal(1111)
            if "CLAIMBITS" in mes:
              cookies,user_agent=mes.split('CLAIMBITS ')[1].split('$')
        cookies = input(hijau1 + 'Masukkan cookies mu > ')
        user_agent = input(hijau1 + 'Masukkan User-Agent mu > ')
        data = {
            'cookies': cookies,
            'user_agent': user_agent
        }
        with open(f'data/{name}/{name}.json', 'w') as file:
            json.dump(data, file)
        return cookies, user_agent
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/claimlite/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/'+nama_host+f'/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control(nama_host)
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/'+nama_host+'/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data(''+nama_host+'')
  if not os.path.exists('data/'+nama_host+'/'+nama_host+'.json'):
    save_data(tele,nama_host)
    claimbits(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://claimbits.net/faucet.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    if 'Balance' not in get_sl.text:
      save_data(tele,nama_host)
      claimbits(modulesl,banner,tele)
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,nama_host)
    claimbits(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
 # del get_id[0]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://'+host+f'/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,nama_host)
     claimbits(modulesl,banner,tele)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  websites = {
    'shrinkearn.com': modulesl.shrinkearn,
    'linksfly.me': modulesl.linksfly,
    'mitly.us': modulesl.mitly,
    'url.namaidani.com': modulesl.url_namaidani,
    'oii.io': modulesl.oii,
    'FC.LC': modulesl.fl_lc,
    'megaurl.in': modulesl.megaurl,
    'ExE': modulesl.exe_io,
    'ex-foary.com': modulesl.ex_foary_com,
    'clks.pro': modulesl.clks_pro,
    'adshort.co': modulesl.adshorti_co,
    'cuty.io': modulesl.cuty_io,
    'link1s.com': modulesl.links1s_com,
  }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://'+host+'/shortlinks.html', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                break
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                          break
    except Exception as e:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
   try:
    get_sl=curl.get('https://claimbits.net/faucet.html',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Lf6q3okAAAAAOO5I84xHj2g8cWRb-cNwsTnMHBa',get_sl.url)
    g=json.loads(curl.post('https://'+host+'/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
   except Exception as e:
     print('Cloudflare!!')
     save_data(tele,nama_host)
     claimbits(modulesl,banner,tele)
def ltchunt(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  nama_host="ltchunt"
  host="ltchunt.com"
  banner.banner(nama_host.upper())
  data_control(''+nama_host+'')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/'+nama_host+f'/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control(nama_host)
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/'+nama_host+'/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data(''+nama_host+'')
  if not os.path.exists('data/'+nama_host+'/'+nama_host+'.json'):
    save_data(tele,nama_host)
    ltchunt(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,nama_host)
    ltchunt(modulesl,banner,tele)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,nama_host)
    ltchunt(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
  del get_id[0]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://'+host+f'/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,nama_host)
     ltchunt(modulesl,banner,tele)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  websites = {
    'shortsfly.me': modulesl.shortfly,
    'flyzu.icu': modulesl.flyzu,
    'linksfly.me': modulesl.linksfly,
    'usalink.io': modulesl.usalink,
    'shortzu.icu': modulesl.shortzu_icu,
    'zuba.link': modulesl.zuba_link,
    'shorti.io': modulesl.shorti_io,
    'clk.sh': modulesl.clksh,
    'clickzu.icu': modulesl.clickzu_icu,
    'kiw.app': modulesl.kiw_app,
    'shrinkearn.com': modulesl.shrinkearn,
    'clks.pro': modulesl.clks_pro,
    'fc.lc': modulesl.fl_lc,
    'exe.io': modulesl.exe_io,
    'illink.net': modulesl.illink_net,
    'birdurls.com': modulesl.birdurl,
    'adshorti.xyz': modulesl.adshorti_xyz,
    'owllink.net': modulesl.owlink,
    'linksly.co': modulesl.linksly,
    'chainfo.xyz': modulesl.chainfo,
    'linkjust.com': modulesl.linkjust,
    'link1s.com': modulesl.links1s_com,
    'megaurl.io': modulesl.megaurl,
    'mitly.us': modulesl.mitly,
    'cashurl.win': modulesl.cashurl_win,
    'megafly.in': modulesl.megafly,
    'oii.io': modulesl.oii,
    'ex-foary.com': modulesl.ex_foary_com,
    'linkvor.pw': modulesl.linkvor_pw,
    'insfly.pw': modulesl.insfly,
  }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://'+host+'/shortlinks.html', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                break
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                          break
    except Exception as e:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://'+host+'/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Ld28FEkAAAAAHU7Z8ddeMVLzt4CAIzITn9g7ENZ',get_sl.url)
    g=json.loads(curl.post('https://'+host+'/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def coinzask(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  nama_host="coinzask"
  host="coinzsack.com"
  banner.banner(nama_host.upper())
  data_control(''+nama_host+'')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/'+nama_host+f'/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control(nama_host)
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          with open('cache/'+nama_host+'/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y).text
      return answer
  cookies, ugentmu = load_data(''+nama_host+'')
  if not os.path.exists('data/'+nama_host+'/'+nama_host+'.json'):
    save_data(tele,nama_host)
    coinzask(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/',headers=ua,cookies=cookies)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,nama_host)
    coinzask(modulesl,banner,tele)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(tele,nama_host)
    coinzask(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start working on ptc")
  get_ptc=curl.get('https://'+host+'/?page=ptc',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://'+host+'/?page=ptc',headers=ua,cookies=cookies)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
  del get_id[len(get_id)-1]
  for _id in get_id:
   try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://'+host+f'/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,nama_host)
     coinzask(modulesl,banner,tele)
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/?page=shortlinks',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[len(gt_s)-1]
  del gt_s[0]
  del gt_s[0]
  print(hijau1+"> "+kuning1+"Start Bypassing Shortlinks")
  websites = {
                'Softindex.website': modulesl.softindex_website,
                'Linksfly.me': modulesl.linksfly,
                'Clks.pro': modulesl.clks_pro,
                'Exe.io': modulesl.exe_io,
                'Shorti.io': modulesl.shorti_io,
                'Urlcash.click': modulesl.urlcash,
               # 'Panylink.com': modulesl.panylink,
                'Coinsparty.com': modulesl.coinparty,
                'Usalink.io': modulesl.usalink,
                'Birdurls.com': modulesl.birdurl,
                'Adshorti.xyz': modulesl.adshorti_xyz
            }
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
            if name in websites:
                for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
                    get_sl = curl.get('https://'+host+'/?page=shortlinks', headers=ua, cookies=cookies)
                    token = get_sl.text.split("var token = '")[1].split("';")[0]
                    status = True
                    while status == True:
                        da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                        get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                        if get_lk["status"] == 200:
                            answer = websites[name](get_lk["shortlink"])
                            if "failed to bypass" == answer:
                                print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"failed to bypass",end="\r")
                            if "" == answer:
                                pass
                            else:
                                time.sleep(10)
                                get_sl = curl.get(answer, headers=ua, cookies=cookies)
                                try:
                                    sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                                    print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+sukses)
                                    print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
                                except:
                                    print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                                break
                        if get_lk['status'] == 600:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                        else:
                          print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                          break
    except Exception as e:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+kuning1+"Bypass faucet")
  while True:
    get_sl=curl.get('https://'+host+'/',headers=ua,cookies=cookies)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LepbFEkAAAAABh_KcuF9g1cZwKv48HnBVBqtYEm',get_sl.url)
    g=json.loads(curl.post('https://'+host+'/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
def coingax(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coingax')
  banner.banner('COINGAX')
  cookies, ugentmu = load_data('coingax')
  if not os.path.exists("data/coingax/coingax.json"):
    save_data(tele,'coingax')
    coingax(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"coingax.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dahs=curl.get('https://coingax.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dahs.text:
    save_data(tele,'coingax')
    coingax(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('div',{'class':'col-xl-3 col-lg-6 col-md-6 col-sm-6 col-xs-12'})
  print(hijau1+"> "+kuning1+"Account information")
  for i in fd:
    print(hijau1+'> '+i.text.strip().splitlines()[0]+' : '+i.text.strip().splitlines()[1])
  link=curl.get('https://coingax.com/links',headers=ua,cookies=cookies)
  fd=bs(link.text,'html.parser').find_all('div',{'class':'col-md-6 col-lg-4 mb-3 mb-lg-0'})
  for li in fd:
   try:
    name=li.text.strip().splitlines()[0]
    jumlah=li.text.strip().splitlines()[6].split('Available ')[1].split('/')[0]
    if 'Cuty - Easy' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        answer=modulesl.cuty_io(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
          sleep(105)
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
          
    if 'Shortsfly - Mid' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        sleep()
        answer=modulesl.shortfly(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
          sleep(105)
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
    if 'Linksfly - Mid' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        answer=modulesl.linksfly(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
          sleep(105)
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
   except Exception as e:pass
  exit()
def crypto2u(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('crypto2u')
  banner.banner('CRYPTO2U')
  cookies, ugentmu = load_data('crypto2u')
  if not os.path.exists("data/crypto2u/crypto2u.json"):
    save_data(tele,'crypto2u')
    crypto2u(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"crypto2u.xyz",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dahs=curl.get('https://crypto2u.xyz/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dahs.text:
    save_data(tele,'crypto2u')
    crypto2u(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('div',{'class':'col-xl-4 col-lg-6 col-md-6 col-sm-6 col-xs-12'})
  print(hijau1+"> "+kuning1+"Account information")
  for i in fd:
    print(hijau1+'> '+i.text.strip().splitlines()[0]+' : '+i.text.strip().splitlines()[1])
  link=curl.get('https://crypto2u.xyz/links',headers=ua,cookies=cookies)
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  fd=bs(link.text,'html.parser').find_all('div',{'class':'col-md-6 col-lg-4 mb-3 mb-lg-0'})
  bypass_functions = {
    'Clks': modulesl.clks_pro,
    'LinksFly': modulesl.linksfly,
    'CLK': modulesl.clksh,
    'ShrinkEarn': modulesl.shrinkearn,
    'CTR': modulesl.ctrsh,
    'Ez4Short': modulesl.ez4short,
    'Try2Link': modulesl.try2,
    'Owl Link': modulesl.owlink,
    'EXE': modulesl.exe_io,
    'LinkJust': modulesl.linkjust,
    'USA Link': modulesl.usalink,
    'FCLC': modulesl.fl_lc,
    'Cuty': modulesl.cuty_io,
  }
  for li in fd:
      try:
          name = li.find('h5',{'class':'card-title text-center'}).text
          jumlah = li.find('span',{'class':'ms-auto badge badge-primary'}).text.split('/')[0]
          for i in range(int(jumlah)):
              link = li.find('button')['onclick'].split("window.open('")[1].split("', '")[0]
              if name in bypass_functions:
                  get_links = curl.get(link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : ' + get_links, end='\r')
                  answer = bypass_functions[name](get_links)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass', end='\r')
                  else:
                      sleep(105)
                      reward = curl.get(answer, headers=ua, cookies=cookies)
                      dahs=curl.get('https://crypto2u.xyz/dashboard',headers=ua,cookies=cookies)
                      fd=bs(dahs.text,'html.parser').find_all('div',{'class':'col-xl-4 col-lg-6 col-md-6 col-sm-6 col-xs-12'})
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}' + fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1]+'                                         ')
      except Exception as e:pass
  exit()
def claimsatoshi(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('claimsatoshi')
  banner.banner('CLAIMSATOSHI')
  cookies, ugentmu = load_data('claimsatoshi')
  if not os.path.exists("data/claimsatoshi/claimsatoshi.json"):
    save_data(tele,'claimsatoshi')
    claimsatoshi(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"claimsatoshi.xyz",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://claimsatoshi.xyz/dashboard',headers=ua,cookies=cookies)
  if 'Current Balance' not in dash.text:
    save_data(tele,'claimsatoshi')
    claimsatoshi(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-xl-3 col-sm-6'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[1]+' : '+info.text.strip().splitlines()[0])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://claimsatoshi.xyz/ptc',headers=ua,cookies=cookies)
  surf=bs(ptc.text,'html.parser').find_all('div',{'class':'col-12 col-lg-4 mb-3 mb-lg-0'})
  if 'Website Available' not in ptc.text:
    save_data(tele,'claimsatoshi')
    claimsatoshi(modulesl,banner,tele)
  for surf in surf:
    url=surf.find('button',{'class':'btn btn-one bg-dark btn-block'})['onclick'].split("window.location = '")[1].split("'")[0]
    name=surf.find('h2',{'class':'card-title'}).text.strip()
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    surf1=curl.get(url,headers=ua,cookies=cookies)
    sleep(int(surf1.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(surf1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',url)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(url.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
  print(hijau1+"> "+kuning1+"Start shortlinks")
  gt_link = curl.get('https://claimsatoshi.xyz/links', headers=ua, cookies=cookies)
  gtf = bs(gt_link.text, 'html.parser')
  gt_info = gtf.find_all('div', {'class': 'col-12 col-lg-4 mb-3 mb-lg-0'})
  def process_link(link, bypass_function,sl=None):
    try:
      lik = link.find('a')["href"]
      get_info = [i for i in link.text.strip().splitlines() if i]
      for i in range(int(get_info[4].split('/')[0].split('Claim ')[1])):
        get_lik = curl.get(lik, headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_lik,end='\r')
        answer = bypass_function(get_lik)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
        else:
          sleep(105)
          reward = curl.get(answer, headers=ua, cookies=cookies).text
          #print(reward)
          if 'Good job!' in reward:
            print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
          else:
            print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:
      pass
  for link in gt_info:
    if 'cbshort[Easy]' in link.text:
      process_link(link, modulesl.cbshort)
    elif 'Ez4short' in link.text:
      process_link(link, modulesl.ez4short)
    elif 'linksfly' in link.text:
      process_link(link, modulesl.linksfly)
    elif 'shortfly' in link.text:
      process_link(link, modulesl.shortfly)
    elif 'usalink' in link.text:
      process_link(link, modulesl.usalink)
    elif 'link1s' in link.text:
      process_link(link, modulesl.links1s_com)
    elif 'Shareus' in link.text:
      process_link(link, modulesl.shareus)
    elif 'Cuttyio' in link.text:
      process_link(link, modulesl.cuty_io)
    elif 'flyzu' in link.text:
      process_link(link, modulesl.flyzu)
    elif 'Shrinkearn' in link.text:
      process_link(link, modulesl.shrinkearn)
    elif 'droplink' in link.text:
      process_link(link, modulesl.droplink)
    elif 'Clksh' in link.text:
      process_link(link, modulesl.clksh)
    elif 'Hrshort' in link.text:
      process_link(link, modulesl.hrshort)
    elif 'Birdurls' in link.text:
      process_link(link, modulesl.birdurl)
    elif 'Owlink' in link.text:
      process_link(link, modulesl.owlink)
    elif 'Megaurl' in link.text:
      process_link(link, modulesl.megaurl)
    elif 'Mitly' in link.text:
      process_link(link, modulesl.mitly)
    elif 'link1snet' in link.text:
      process_link(link, modulesl.link1s_net,sl=5)
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://claimsatoshi.xyz/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(15)
    reward=curl.post('https://claimsatoshi.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
      break
      pass
  exit()
def coinfola(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinfola')
  banner.banner('COINFOLA')
  cookies, ugentmu = load_data('coinfola')
  if not os.path.exists("data/coinfola/coinfola.json"):
    save_data(tele,'coinfola')
    coinfola(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"coinfola.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://coinfola.com/account',headers=ua,cookies=cookies)
  except Exception as e:
    save_data(tele,'coinfola')
    coinfola(modulesl,banner,tele)
  if 'Balance' not in dahs.text:
      save_data(tele,'coinfola')
      coinfola(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-hover table-striped'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://coinfola.com/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  providers = {
    "Clks":modulesl.clks_pro,
    "GainLink":modulesl.gain_lk,
    "Try2Link":modulesl.try2,
    "Clk":modulesl.clksh,
    "ShortsFly":modulesl.shortfly,
    "ShrinkEarn":modulesl.shrinkearn,
    "LinksFly":modulesl.linksfly,
    "Usalink":modulesl.usalink,
    "Chainfo":modulesl.chainfo,
    "Fclc":modulesl.fl_lc,
    "Shrinkme":modulesl.shrinkme,
    "Shorti":modulesl.shorti_io,
    "eXeio":modulesl.exe_io,
    "Cuty":modulesl.cuty_io,
    "AdBitFly":modulesl.adbitfly,
    "Oii":modulesl.oii,
    "Zuba":modulesl.zuba_link,
    "ClickZu":modulesl.clickzu_icu,
    "FlyZu":modulesl.flyzu,
    "Linkvor":modulesl.linkvor_pw,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
    #  print(i)
      for provider in providers:
          if provider in name:
              print(name)
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://coinfola.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  sleep(105)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      _1 = reward.text.split("message: 'You")[1].split("tickets.'")[0]
                      _2 = reward.text.split("message: 'Congratulations.")[1].split("credited.'")[0]
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+'Congratulations. ' + _2 + ' credited. & You ' + _1 + ' tickets.')
    except Exception as e:
      pass
  exit()
def simpleads(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('simpleads')
  banner.banner('SIMPLEADS')
  cookies, ugentmu = load_data('simpleads')
  if not os.path.exists("data/simpleads/simpleads.json"):
    save_data(tele,'simpleads')
    simpleads(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"simpleads.io",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://simpleads.io/account',headers=ua,cookies=cookies)
  except Exception as e:
    save_data(tele,'simpleads')
    simpleads(modulesl,banner,tele)
  if 'Balance' not in dahs.text:
      save_data(tele,'simpleads')
      simpleads(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://simpleads.io/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  providers = {
    "linksfly":modulesl.linksfly,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      for provider in providers:
          if provider in name:
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://simpleads.io' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  sleep(105)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
    except Exception as e:
      pass
  print(hijau1+"> "+kuning1+"Start bypass faucet")
  while True:
   try:
    faucet=curl.get('https://simpleads.io/faucet',headers=ua,cookies=cookies)
    csrf=bs(faucet.text,'html.parser').find('input',{'name':'csrfToken'})['value']
    answer=modulesl.RecaptchaV2('6Lee4w0kAAAAAEjQzK7OARMkmpiCf_9eOo9WFsHJ',faucet.url)
    data=f"csrfToken={csrf}&g-recaptcha-response={answer}"
    reward=curl.post(faucet.url,data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'success' in reward.text:
            print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
            animasi(3)
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1} Cloudflare!!')
     save_data(tele,'simpleads')
     simpleads(modulesl,banner,tele)
  exit()
def adhives(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('adhives')
  banner.banner('ADHIVES')
  cookies, ugentmu = load_data('adhives')
  if not os.path.exists("data/adhives/adhives.json"):
    save_data(tele,'adhives')
    adhives(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"adhives.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://adhives.com/account',headers=ua,cookies=cookies)
  except Exception as e:
    save_data(tele,'adhives')
    adhives(modulesl,banner,tele)
  if 'Balance' not in dahs.text:
      save_data(tele,'adhives')
      adhives(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://adhives.com/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  providers = {
    "Linksfly":modulesl.linksfly,
    "Shortsfly":modulesl.shortfly,
    "Shrinkearn":modulesl.shrinkearn,
    "Clks":modulesl.clks_pro,
    "Fc":modulesl.fl_lc,
    "Cuty":modulesl.cuty_io,
    "Oii":modulesl.oii,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      for provider in providers:
          if provider in name:
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://adhives.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  sleep(105)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
    except Exception as e:
      pass
  exit()
def coinsfarm(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinsfarmers')
  banner.banner('COINSFARMERS')
  cookies, ugentmu = load_data('coinsfarmers')
  if not os.path.exists("data/coinsfarmers/coinsfarmers.json"):
    save_data(tele,'coinsfarmers')
    coinsfarm(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"coinsfarmers.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://coinsfarmers.com/account',headers=ua,cookies=cookies)
  except Exception as e:
    save_data(tele,'coinsfarmers')
    coinsfarm(modulesl,banner,tele)
  if 'Balance' not in dahs.text:
      save_data(tele,'coinsfarmers')
      coinsfarm(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get('https://coinsfarmers.com/shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  providers = {
    'LinksFly': modulesl.linksfly,
    'Shortsfly': modulesl.shortfly,
    'Usalink': modulesl.usalink,
    'Fc.lc': modulesl.fl_lc,
    'Birdurls': modulesl.birdurl,
    'Owllink': modulesl.owlink,
    'Cuty': modulesl.cuty_io,
    'Exe.io': modulesl.exe_io,
    'Insfly': modulesl.insfly,
    'Hrshort': modulesl.hrshort,
    'Clks.pro': modulesl.clks_pro,
    'Shorti': modulesl.shorti_io,
  }
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
  #    print(name)
      for provider in providers:
          if provider in name:
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':'card shadow text-decoration-none'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://coinsfarmers.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  sleep(105)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0]+'       ')
    except Exception as e:
      pass
  exit()
def earnsolana(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('earnsolana')
  banner.banner('EARNSOLANA')
  cookies, ugentmu = load_data('earnsolana')
  if not os.path.exists("data/earnsolana/earnsolana.json"):
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"earnsolana.xyz",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://earnsolana.xyz/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://earnsolana.xyz/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6Lem2pIjAAAAAESScDYn7ChChD9JS7pqa0d7TUUL',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://earnsolana.xyz/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
            'ShrinkEarn': modulesl.shrinkearn,
            'ShrinkMe': modulesl.shrinkme,
            'Ez4Short': modulesl.ez4short,
            'LinksFly': modulesl.linksfly,
            'ShortsFly.me': modulesl.shortfly,
            'Usalink': modulesl.usalink,
            'LinksLy': modulesl.linksly,
            'Clk': modulesl.clksh,
            'Clks.pro': modulesl.clks_pro,
        }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://earnsolana.xyz/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(30)
    reward=curl.post('https://earnsolana.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     exit()
  exit()
def cryptogenz(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('cryptogenz')
  banner.banner('CRYPTOGENZ')
  cookies, ugentmu = load_data('cryptogenz')
  if not os.path.exists("data/cryptogenz/cryptogenz.json"):
    save_data(tele,'cryptogenz')
    cryptogenz(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"cryptogenz.fun",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://cryptogenz.fun/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'cryptogenz')
    cryptogenz(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://cryptogenz.fun/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'cryptogenz')
    cryptogenz(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
    "Shortsfly": modulesl.shortfly,
    "Linksfly": modulesl.linksfly,
    "Gainlink": modulesl.gain_lk,
    "Shrinkearn": modulesl.shrinkearn,
    "Ctrsh": modulesl.ctrsh,
    "Shrinkme": modulesl.shrinkme,
    "Usalink": modulesl.usalink,
    "Trylink": modulesl.try2,
    "Birdurl": modulesl.birdurl,
    "Owllink": modulesl.owlink,
    "Cuty": modulesl.cuty_io,
    "Short.i": modulesl.shorti_io,
    "Linkvor(very easy)": modulesl.linkvor_pw
      }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://cryptogenz.fun/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('https://cryptogenz.fun/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     exit()
  exit()
def coinpay_faucet(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinpay-faucet')
  banner.banner('COINPAY-FAUCET')
  cookies, ugentmu = load_data('coinpay-faucet')
  if not os.path.exists("data/coinpay-faucet/coinpay-faucet.json"):
    save_data(tele,'coinpay-faucet')
    coinpay_faucet(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"coinpay-faucet.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://coinpay-faucet.com/dashboard',headers=ua,cookies=cookies)
  if 'firewall' in dash.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6LdtJxUiAAAAAC8KYAgOUIqTwCee5g2r-YpeeU6D',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("https://coinpay-faucet.com/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
  if 'Balance' not in dash.text:
    save_data(tele,'coinpay-faucet')
    coinpay_faucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://coinpay-faucet.com/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'coinpay-faucet')
    coinpay_faucet(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
        'HOT- shortsfly.me': modulesl.shortfly,
        'HOT- linksfly.me': modulesl.linksfly,
        'exe.io': modulesl.exe_io,
        'shorti.io': modulesl.shorti_io,
        'cuty.io': modulesl.cuty_io,
        'usalink.io': modulesl.usalink,
        'owllink.net': modulesl.owlink,
        'birdurls.com': modulesl.birdurl,
        'illink.net': modulesl.illink_net,
        'clks.pro': modulesl.clks_pro,
        'ex-foary.com': modulesl.ex_foary_com,
        'shrinkme.link': modulesl.shrinkme,
        'INSFLY': modulesl.insfly,
        }
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://coinpay-faucet.com/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('https://coinpay-faucet.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
def james_trussy(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('james-trussy')
  banner.banner('JAMES-TRUSSY')
  cookies, ugentmu = load_data('james-trussy')
  if not os.path.exists("data/james-trussy/james-trussy.json"):
    save_data(tele,'james-trussy')
    james_trussy(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"james-trussy.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  faucet=curl.get('https://james-trussy.com/faucet',headers=ua,cookies=cookies)
  if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6Ler3E4kAAAAABUDc4UE9UWO7k_n2JydShddSpCO',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("https://james-trussy.com/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
  dash=curl.get('https://james-trussy.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'james-trussy')
    james_trussy(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://james-trussy.com/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'james-trussy')
    james_trussy(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
    'CRTSH': modulesl.ctrsh,
    'FCLC': modulesl.fl_lc,
    'BirdUrl': modulesl.birdurl,
    'LinksFly': modulesl.linksfly,
    'USALink': modulesl.usalink,
    'IlLink': modulesl.illink_net,
    'Cuty': modulesl.cuty_io,
    'Exe': modulesl.exe_io,
    'OwlLink': modulesl.owlink
      }
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                  #  print(reward)
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    faucet=curl.get('https://james-trussy.com/faucet',headers=ua,cookies=cookies)
    if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6Ler3E4kAAAAABUDc4UE9UWO7k_n2JydShddSpCO',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("https://james-trussy.com/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
    get_=curl.get('https://james-trussy.com/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('https://james-trussy.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
   #  exit()
  print(hijau1+"> "+kuning1+"Start faucet")
  faucet=curl.get('https://james-trussy.com/faucet',headers=ua,cookies=cookies)
  jumlah=bs(faucet.text,'html.parser').find_all('p',{'class':'lh-1 mb-1 font-weight-bold'})
  jum=int(jumlah[len(jumlah)-1].text.split('/')[0])
  for i in range(jum):
    faucet=curl.get('https://james-trussy.com/faucet',headers=ua,cookies=cookies)
    info=bs(faucet.text,'html.parser')
    csrf=info.find('input',{'name':'csrf_token_name'})['value']
    token=info.find('input',{'name':'token'})['value']
    answer=modulesl.RecaptchaV2('6Ler3E4kAAAAABUDc4UE9UWO7k_n2JydShddSpCO','https://james-trussy.com/faucet')
    data=f"csrf_token_name={csrf}&token={token}&captcha=recaptchav2&recaptchav3=&g-recaptcha-response={answer}"
    faucet=curl.post('https://james-trussy.com/faucet/verify',data=data,headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},cookies=cookies)
    if 'Good job!' in faucet.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+faucet.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
    animasi(1)
    faucet=curl.get('https://james-trussy.com/faucet',headers=ua,cookies=cookies)
    if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6Ler3E4kAAAAABUDc4UE9UWO7k_n2JydShddSpCO',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("https://james-trussy.com/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
def freeclaimfaucet(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('freeclaimfaucet')
  banner.banner('freeclaimfaucet')
  cookies, ugentmu = load_data('freeclaimfaucet')
  if not os.path.exists("data/freeclaimfaucet/freeclaimfaucet.json"):
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"freeclaimfaucet.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  faucet=curl.get('https://freeclaimfaucet.com/faucet',headers=ua,cookies=cookies)
  if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6LcTwH0dAAAAADeD8cRAHIRmwKrS3JNbSh30QWFx',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("https://freeclaimfaucet.com/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
  dash=curl.get('https://freeclaimfaucet.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find('div',{'class':'mt-3 text-3xl font-semibold text-white'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> Your Balance : '+info.text.strip())
  print(hijau1+"> "+kuning1+"Start bypass ptc")
  ptc=curl.get('https://freeclaimfaucet.com/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LcTwH0dAAAAADeD8cRAHIRmwKrS3JNbSh30QWFx',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://freeclaimfaucet.com/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
    'ctr.sh': modulesl.ctrsh,
    'fc.lc': modulesl.fl_lc,
    'shrinkearn': modulesl.shrinkearn,
    'owlink': modulesl.owlink,
    'clk.sh': modulesl.clksh,
    'clks.pro': modulesl.clks_pro,
    'linksfly': modulesl.linksfly,
    'shortsfly': modulesl.shortfly,
      }
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                  #  print(reward)
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start faucet")
  faucet=curl.get('https://freeclaimfaucet.com/faucet',headers=ua,cookies=cookies)
  jumlah=bs(faucet.text,'html.parser').find_all('p',{'class':'lh-1 mb-1 font-weight-bold'})
  jum=int(jumlah[len(jumlah)-1].text.split('/')[0])
  for i in range(jum):
    faucet=curl.get('https://freeclaimfaucet.com/faucet',headers=ua,cookies=cookies)
    info=bs(faucet.text,'html.parser')
    csrf=info.find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LcTwH0dAAAAADeD8cRAHIRmwKrS3JNbSh30QWFx','https://freeclaimfaucet.com/faucet')
    data=f"csrf_token_name={csrf}&captcha=recaptchav2&g-recaptcha-response={answer}"
    faucet=curl.post('https://freeclaimfaucet.com/faucet/verify',data=data,headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},cookies=cookies)
    if 'Good job!' in faucet.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+faucet.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
    animasi(4)
    faucet=curl.get('https://freeclaimfaucet.com/faucet',headers=ua,cookies=cookies)
    if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6LcTwH0dAAAAADeD8cRAHIRmwKrS3JNbSh30QWFx',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("https://freeclaimfaucet.com/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
def eurofaucet_de(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('eurofaucet.de')
  banner.banner('EUROFAUCET.DE')
  cookies, ugentmu = load_data('eurofaucet.de')
  if not os.path.exists("data/eurofaucet.de/eurofaucet.de.json"):
    save_data(tele,'eurofaucet.de')
    eurofaucet_de(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"eurofaucet.de",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://eurofaucet.de/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'eurofaucet.de')
    eurofaucet_de(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://eurofaucet.de/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data(tele,'eurofaucet.de')
    eurofaucet_de(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6Lcza1QmAAAAAInStIpZuJYEOm-89v4zKNzglgU9',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://eurofaucet.de/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'eurofaucet.de')
    eurofaucet_de(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
     #   print(i)
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
        'shorti': modulesl.adshorti_xyz,
        'try2': modulesl.try2,
        'linksfly': modulesl.linksfly,
        'shortsfly': modulesl.shortfly,
        'owl': modulesl.owlink,
        'illink': modulesl.illink_net,
        'chain': modulesl.chainfo,
        }

        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                  #  print(reward)
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://eurofaucet.de/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('https://eurofaucet.de/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
def tefaucet(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('tefaucet.online')
  banner.banner('TEFAUCET.ONLINE')
  cookies, ugentmu = load_data('tefaucet.online')
  if not os.path.exists("data/tefaucet.online/tefaucet.online.json"):
    save_data(tele,'tefaucet.online')
    tefaucet(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"tefaucet.online",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('http://tefaucet.online/dashboard',headers=ua,cookies=cookies)
  #print(dash.text)
  if 'Balance' not in dash.text:
    save_data(tele,'tefaucet.online')
    tefaucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass ptc")
  ptc=curl.get('http://tefaucet.online/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data(tele,'tefaucet.online')
    tefaucet(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LfO_NgkAAAAALPup3qKwQtj3hQ1wUDP53ELBYxe',link)
    data=f"captcha=recaptchav2&recaptchav3=&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('http://tefaucet.online/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'tefaucet.online')
    tefaucet(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
      #  print(i)
        name = i.find('h4').text
      #  print(name)
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
    'clks.pro': modulesl.clks_pro,
    'shortsfly.me': modulesl.shortfly,
    'linksfly.me': modulesl.linksfly,
    'ctr.sh': modulesl.ctrsh,
    'insfly.pw': modulesl.insfly,
    'ez4short': modulesl.ez4short,
    'owllink': modulesl.owlink,
    'fc.lc': modulesl.fl_lc,
    'linksly': modulesl.linksly,
    'clk.sh': modulesl.clksh,
    'shrinkme.io': modulesl.shrinkme,
    'ex-foary.com': modulesl.ex_foary_com,
    'megaurl.in': modulesl.megaurl,
    'birdurl': modulesl.birdurl,
    'illink': modulesl.illink_net,
    'exe.io': modulesl.exe_io,
    'usalink': modulesl.usalink,
    'oii.io': modulesl.oii,
    'cuty.io': modulesl.cuty_io,
    'chainfo': modulesl.chainfo,
    'link1s': modulesl.links1s_com,
    }
        if name.lower()in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name.lower()](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                  #  print(reward)
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('http://tefaucet.online/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('http://tefaucet.online/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
def bitmonk(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('bitmonk')
  banner.banner('BITMONK')
  cookies, ugentmu = load_data('bitmonk')
  if not os.path.exists("data/bitmonk/bitmonk.json"):
    save_data(tele,'bitmonk')
    bitmonk(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"bitmonk.me",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://bitmonk.me/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'bitmonk')
    bitmonk(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('p',{'class':'text-uppercase fw-medium text-muted text-truncate mb-0'})
  info1=bs(dash.text,'html.parser').find_all('span',{'class':'counter-value'})
  del info[len(info)-2]
  del info1[len(info1)-2]
  print(hijau1+"> "+kuning1+"Account information")
  for inf in range(3):
    print(hijau1+'> '+info[inf].text.strip()+' : '+info1[inf]['data-target'])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://bitmonk.me/ptc',headers=ua,cookies=cookies)
  if 'ADS AVAILABLE' not in ptc.text:
    save_data(tele,'bitmonk')
    bitmonk(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-lg-3 col-12'})
  del ptc[len(ptc)-1]
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'mb-1 mt-4'}).text
    link=ptc.find('a',{'class':'btn btn-ghost-success w-100'})["href"]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('timer = ')[1].split(';')[0]))
    answer=modulesl.RecaptchaV2('6LdENSgiAAAAANbejljfkV7QwobwVWD3QeGGuwwp',link)
    bs4 = bs(visit.text, "html.parser")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    data['g-recaptcha-response']=answer
    verify=curl.post(link.replace('view','claim'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'coins Has Been Credited To Your Wallet!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split("<div class='alert alert-success alert-border-left alert-dismissible  alert-borderless'>")[1].split('</div>')[0])
   except:
        pass
 # exit()
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://bitmonk.me/shortlinks',headers=ua,cookies=cookies).text
  if 'LINKS AVAILABLE' not in ptc.text:
    save_data(tele,'bitmonk')
    bitmonk(modulesl,banner,tele)
 # print(get_links)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-xxl-3 col-sm-6 project-card'})
  for i in link:
    try:
        name = i.find('h5').text
        jumlah = int(i.find('div',{'class':'flex-shrink-0'}).text.strip().split('/')[0])
        services = {
            'clks': modulesl.clks_pro,
            'ShrinkEarn': modulesl.shrinkearn,
            'BirdURLs': modulesl.birdurl,
            'UrlCash': modulesl.urlcash,
            'Shrinkme': modulesl.shrinkme,
           # 'Adbully': modulesl.adbull,
            'FC-LC': modulesl.fl_lc,
            'Clk.sh': modulesl.clksh,
            'Owllink': modulesl.owlink,
            'Usalink': modulesl.usalink,
            'Linksfly': modulesl.linksfly,
            'try2link': modulesl.try2,
            'HRshort': modulesl.hrshort,
            'Linksly': modulesl.linksly,
            'exe.io': modulesl.exe_io,
            'Cuty': modulesl.cuty_io,
            'Mitly': modulesl.mitly,
            'Illink': modulesl.illink_net,
            'AdShort': modulesl.adshorti_co,
            'Shorti io': modulesl.shorti_io,
            'namaidanicom': modulesl.url_namaidani,
            'AdBull': modulesl.adbull,
            'coinsparty': modulesl.coinparty,
            'Namaidani': modulesl.url_namaidani,
        }
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a',{'target':'_blank'})["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<a href="')[1].split('">')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Yahoo! Reward Credited Successfully!' in reward:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split("<div class='alert alert-success alert-border-left alert-dismissible  alert-borderless'>")[1].split('</div>')[0])
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  #exit()
 
  exit()
def claim_ro(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('claim_ro')
  banner.banner('CLAIM_RO')
  cookies, ugentmu = load_data('claim_ro')
  if not os.path.exists("data/claim_ro/claim_ro.json"):
    save_data(tele,'claim_ro')
    claim_ro(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"claimro.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://claimro.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'claim_ro')
    claim_ro(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://claimro.com/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data(tele,'claim_ro')
    claim_ro(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LdAqlAgAAAAAGqPveMFEw3mhkHDVh-rOdyclZAQ',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://claimro.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
            'ctr.sh': modulesl.ctrsh,
            'fc.lc': modulesl.fl_lc,
            'birdsurl': modulesl.birdurl,
            'linksfly': modulesl.linksfly,
            'shortsfly': modulesl.shortfly,
            'clk.sh': modulesl.clksh,
            'owllink': modulesl.owlink,
            'shrinkearn': modulesl.shrinkearn,
            'insfly': modulesl.insfly,
            'clks.pro': modulesl.clks_pro,
        }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
def faucetcrypto_net(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucetcrypto_net')
  banner.banner('FAUCETCRYPTO_NET')
  cookies, ugentmu = load_data('faucetcrypto_net')
  if not os.path.exists("data/faucetcrypto_net/faucetcrypto_net.json"):
    save_data(tele,'faucetcrypto_net')
    faucetcrypto_net(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"faucetcrypto.net",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://faucetcrypto.net/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'faucetcrypto_net')
    faucetcrypto_net(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'d-flex d-lg-flex d-md-block align-items-center'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://faucetcrypto.net/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data(tele,'faucetcrypto_net')
    faucetcrypto_net(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    token=bs(visit.text,'html.parser').find('input',{'name':'token'})['value']
    answer=modulesl.RecaptchaV2('6LfY3WQhAAAAAJ4gw6l_9zKOw50G0har2R8pVt0_',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}&token={token}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'ads available' not in verify.text:
      save_data(tele,'faucetcrypto_net')
      faucetcrypto_net(modulesl,banner,tele)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
        save_data(tele,'faucetcrypto_net')
        faucetcrypto_net(modulesl,banner,tele)
        pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucetcrypto.net/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'faucetcrypto_net')
    faucetcrypto_net(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
    'ShrinkEarn': modulesl.shrinkearn,
    'Shrinkme': modulesl.shrinkme,
    'Linksfly': modulesl.linksfly,
    'Shortsfly': modulesl.shortfly,
    'Try2link': modulesl.try2,
    'OwlLink': modulesl.owlink,
    'IlLink': modulesl.illink_net,
    'BirdURLs': modulesl.birdurl,
    'Link1s': modulesl.links1s_com,
    'Link1s.net': modulesl.link1s_net,
    'Droplink': modulesl.droplink,
    'Ez4short': modulesl.ez4short,
    'ExFoary': modulesl.ex_foary_com,
    'ExeIO': modulesl.exe_io,
    'Clk.sh': modulesl.clksh,
    'ChaINfo': modulesl.chainfo,
    'Usalink': modulesl.usalink,
    'Mitly': modulesl.mitly,
    'MegaUrl': modulesl.megaurl,
    'Web1sTraffic2': modulesl.web1s_info,
    'Web1s': modulesl.web1s_info,
    'Web1sNormal2': modulesl.web1s_info,
    'Web1sNormal3': modulesl.web1s_info,
    'Freeltc': modulesl.freeltc_top,
    'Shortzu': modulesl.shortzu_icu,
    'Clickzu': modulesl.clickzu_icu,
    'Shorti': modulesl.shorti_io,
    'Linksly': modulesl.linksly,
    }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'links available' not in reward:
                      save_data(tele,'faucetcrypto_net')
                      faucetcrypto_net(modulesl,banner,tele)
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://faucetcrypto.net/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('https://faucetcrypto.net/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
def faucetspeedbtc(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucetspeedbtc')
  banner.banner('FAUCETSPEEDBTC')
  cookies, ugentmu = load_data('faucetspeedbtc')
  if not os.path.exists("data/faucetspeedbtc/faucetspeedbtc.json"):
    save_data(tele,'faucetspeedbtc')
    faucetspeedbtc(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"faucetspeedbtc.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://faucetspeedbtc.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'faucetspeedbtc')
    faucetspeedbtc(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucetspeedbtc.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  if 'Links' not in get_links:
    save_data(tele,'faucetspeedbtc')
    faucetspeedbtc(modulesl,banner,tele)
  link=fd.find_all('div',{'class':'col-md-6 col-xl-4'})
  for i in link:
    try:
        name = i.find('h5').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
    'Shrinkearn': modulesl.shrinkearn,
    '1Short': modulesl._1short_in,
    'Shrinkme': modulesl.shrinkme,
    'Linksfly': modulesl.linksfly,
    'Shortsfly': modulesl.shortfly,
    'Try2link': modulesl.try2,
    'OwlLink': modulesl.owlink,
    'IlLink': modulesl.illink_net,
    'BirdURLs': modulesl.birdurl,
    'Link1s': modulesl.links1s_com,
    'Link1s.net': modulesl.link1s_net,
    'Droplink': modulesl.droplink,
    'Ez4short': modulesl.ez4short,
    'ExFoary': modulesl.ex_foary_com,
    'ExeIO': modulesl.exe_io,
    'Clk.sh': modulesl.clksh,
    'ChaINfo': modulesl.chainfo,
    'Usalink': modulesl.usalink,
    'Mitly': modulesl.mitly,
    'MegaUrl': modulesl.megaurl,
    'Web1sTraffic2': modulesl.web1s_info,
    'Web1s': modulesl.web1s_info,
    'Web1sNormal2': modulesl.web1s_info,
    'Web1sNormal3': modulesl.web1s_info,
    'Freeltc': modulesl.freeltc_top,
    'Shortzu': modulesl.shortzu_icu,
    'Clickzu': modulesl.clickzu_icu,
    'Shorti': modulesl.shorti_io,
    'Linksly': modulesl.linksly,
    }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://faucetspeedbtc.com/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(30)
    reward=curl.post('https://faucetspeedbtc.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! 4 tokens has been added to your balance success')
   except:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
def faucet4u(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucet4u')
  banner.banner('FAUCET4U')
  cookies, ugentmu = load_data('faucet4u')
  if not os.path.exists("data/faucet4u/faucet4u.json"):
    save_data(tele,'faucet4u')
    faucet4u(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"faucet4u.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://faucet4u.com/dashboard',headers=ua,cookies=cookies)
  #print(dash.text)
  if 'Balance' not in dash.text:
    save_data(tele,'faucet4u')
    faucet4u(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucet4u.com/links',headers=ua,cookies=cookies).text
  if 'links available' not in get_links:
    save_data(tele,'faucet4u')
    faucet4u(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
    'ShrinkEarn': modulesl.shrinkearn,
    'Link4M': modulesl.link4m_com,
    'Shrinkme': modulesl.shrinkme,
    'LinksFly': modulesl.linksfly,
    'ShortsFly': modulesl.shortfly,
    'Try2link': modulesl.try2,
    'OwlLink': modulesl.owlink,
    'IlLink': modulesl.illink_net,
    'BirdURLs': modulesl.birdurl,
    'Link1s': modulesl.links1s_com,
    'Link1s.net': modulesl.link1s_net,
    'DropLink': modulesl.droplink,
    'Ez4Short': modulesl.ez4short,
    'ExFoary': modulesl.ex_foary_com,
    'ExeIO': modulesl.exe_io,
    'ClkSh': modulesl.clksh,
    'ChaINfo': modulesl.chainfo,
    'Usalink': modulesl.usalink,
    'Mitly': modulesl.mitly,
    'MegaUrl': modulesl.megaurl,
    'Web1sTraffic2': modulesl.web1s_info,
    'Web1s': modulesl.web1s_info,
    'Web1sNormal2': modulesl.web1s_info,
    'Web1sNormal3': modulesl.web1s_info,
    'Freeltc': modulesl.freeltc_top,
    'Shortzu': modulesl.shortzu_icu,
    'Clickzu': modulesl.clickzu_icu,
    'Shorti': modulesl.shorti_io,
    'Linksly': modulesl.linksly,
    }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
def tikiearn(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('tikiearn')
  banner.banner('TIKIEARN')
  cookies, ugentmu = load_data('tikiearn')
  if not os.path.exists("data/tikiearn/tikiearn.json"):
    save_data(tele,'tikiearn')
    tikiearn(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"tikiearn.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://tikiearn.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'tikiearn')
    tikiearn(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  print(hijau1+"> "+kuning1+"Account information")
  del info[0]
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://tikiearn.com/ptc',headers=ua,cookies=cookies)
  #print(ptc.text)
  if 'ads available' not in ptc.text:
    save_data(tele,'tikiearn')
    tikiearn(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-3'})
  for ptc in ptc:
   try:
      name=ptc.find('h4').text.strip()
      link=ptc.find('button')["onclick"].split("window.location = '")[1].split("'")[0]
      print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
      visit=curl.get(link,headers=ua,cookies=cookies)
      sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
      answer=modulesl.RecaptchaV2('6LcpH6omAAAAAPgjFK9i2npoqAvZLh-_L9M9t8Ds',link)
      csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
      token=bs(visit.text,'html.parser').find('input',{'name':'token'})['value']
      data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}&token={token}"
      verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
      if 'Good job!' in verify.text:
        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
        save_data(tele,'tikiearn')
        tikiearn(modulesl,banner,tele)
        pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://tikiearn.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
 # print(link)
  for i in link:
    try:
        name = i.find('h4').text.strip()
        jumlah = int(i.find('span',{'class':'badge badge-info'}).text.split('/')[0])
        
        services = {
    'ShrinkEarn': modulesl.shrinkearn,
    'Myra': modulesl.myra,
    'Try2Link': modulesl.try2,
    'Linksfly': modulesl.linksfly,
    'Cuty.io': modulesl.cuty_io,
    'FcLc': modulesl.fl_lc,
    'Clk.sh': modulesl.clksh,
    'CbShort': modulesl.cbshort,
    'HrShort': modulesl.hrshort,
    'BirdUrl': modulesl.birdurl,
    'Exe.io': modulesl.exe_io,
    'MegaUrl': modulesl.megaurl,
    'Oii.io': modulesl.oii,
    }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
def allfaucet(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('allfaucet')
  banner.banner('ALLFAUCET')
  cookies, ugentmu = load_data('allfaucet')
  if not os.path.exists("data/allfaucet/allfaucet.json"):
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"allfaucet.xyz",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://allfaucet.xyz/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'invoice-box'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
 # exit()
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://allfaucet.xyz/ptc',headers=ua,cookies=cookies)
  if 'Ads Available' not in ptc.text:
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    #  print(ptc)
      name=ptc.find('h5',{'class':'card-title'}).text.strip()
      link=ptc.find('button')["onclick"].split("window.location = '")[1].split("'")[0]
      print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
      visit=curl.get(link,headers=ua,cookies=cookies)
      sleep(int(visit.text.split('let timer = ')[1].split(';')[0]))
      csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
      token=bs(visit.text,'html.parser').find('input',{'name':'token'})['value']
      answer=modulesl.RecaptchaV2('6Lcb3bkfAAAAAC1ZGV7QlVQyE7iyVr2jq6nvmvcN',link)
      data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}&token={token}"
      verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
      if 'Good job!' in verify.text:
        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! '+verify.text.split("text: '")[1].split("',")[0])
   except Exception as e:
        save_data(tele,'allfaucet')
        allfaucet(modulesl,banner,tele)
        pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://allfaucet.xyz/links',headers=ua,cookies=cookies).text
  if 'Links available' not in get_links:
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'link-block'})
 # print(link)
  services = {
    'Shrinkearn': modulesl.shrinkearn,
    'Shrinkme': modulesl.shrinkme,
    'Exe': modulesl.exe_io,
    'Clk': modulesl.clksh,
    'Megaurl': modulesl.megaurl,
    'Usalink': modulesl.usalink,
    'Linkfly': modulesl.linksfly,
    'Shortfly': modulesl.shortfly,
    'Shortsfly1': modulesl.shortfly,
    }
  for i in link:
    try:
        name = i.find('span',{'class':'link-name'}).text.strip()
        jumlah = int(i.find('span',{'class':'link-rmn'}).text.split('/')[0])
        if name in services:
            shortlink_func = services[name]
            for _ in range(jumlah):
                csrf=fd.find('input',{'name':'csrf_token_name'})['value']
                token=fd.find('input',{'name':'token'})['value']
                data=f"csrf_token_name={csrf}&token={token}"
                url = curl.post(i.find('form')["action"], headers={'content-type':'application/x-www-form-urlencoded'}, data=data,cookies=cookies, allow_redirects=False).text.split('location.href = "')[1].split('"; </script>')[0]
                answer = shortlink_func(url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        reward_msg = reward.split("text: '")[1].split("',")[0]
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! '+reward_msg)
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
                get_links=curl.get('https://allfaucet.xyz/links',headers=ua,cookies=cookies).text
                fd=bs(get_links,'html.parser')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://allfaucet.xyz/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(10)
    reward=curl.post('https://allfaucet.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! '+reward.text.split("text: '")[1].split("',")[0])
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
def btcadspace(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('btcadspace')
  banner.banner('BTCADSPACE')
  cookies, ugentmu = load_data('btcadspace')
  if not os.path.exists("data/btcadspace/btcadspace.json"):
    save_data(tele,'btcadspace')
    btcadspace(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"btcadspace.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  try:
    dash=curl.get('https://btcadspace.com/account',headers=ua,cookies=cookies)
  #  print(dash.text)
    if 'Main Balance' not in dash.text:
      save_data(tele,'btcadspace')
      btcadspace(modulesl,banner,tele)
  except Exception as e:
    save_data(tele,'btcadspace')
    btcadspace(modulesl,banner,tele)
  fd=bs(dash.text,'html.parser').find_all('div',{'class':'col-md-4 stretch-card grid-margin mt-3'})
  print(hijau1+"> "+kuning1+"Account information")
  for i in fd:
    print(hijau1+'> '+i.text.strip().replace('    ','').splitlines()[0]+' : '+i.text.strip().replace('    ','').splitlines()[1])
  print(hijau1+"> "+kuning1+"Bypass shortlinks")
  get_links=curl.get('https://btcadspace.com/shortlinks',headers=ua, cookies=cookies)
  gas=bs(get_links.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  methods = {
    'Linksfly': modulesl.linksfly,
    'Shortsfly': modulesl.shortfly,
    'Ctr': modulesl.ctrsh,
    'Usalink': modulesl.usalink,
    'Cuty': modulesl.cuty_io,
    'Clks': modulesl.clks_pro,
    'Shrinkearn': modulesl.shrinkearn,
    'Bitads': modulesl.bitads,
    'Ex foary': modulesl.ex_foary_com,
    'Exe.io': modulesl.exe_io,
    'Web1s': modulesl.web1s_info,
  }
  for i in gas:
      info = [i for i in i.text.strip().replace('            ', '').splitlines() if i]
      jumlah = info[2].split(' clicks remaining')[0]
      for method, bypass_func in methods.items():
        try:
          if method in info[0]:
              for jun in range(int(jumlah)):
                  url = curl.get('https://btcadspace.com' + i.find('a', {'class': 'card shadow text-decoration-none'})['href'], headers=ua, cookies=cookies, allow_redirects=False).headers['location']
                  answer = bypass_func(url)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  else:
                      sleep(105)
                      get_reward = curl.get(answer, headers=ua, cookies=cookies)
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("message: '")[1].split("'")[0])
        except Exception as e:
          pass
  
def nokofaucet(modulesl,banner,tele=None):
  def save_datan(tele,name):
      if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim auth : `/cookies nama_sesi auth`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                auth=mes.split(name.upper()+' ')[1]
      else:
        auth=input(hijau1+'masukan auth mu > ')
      data = {
          'auth': auth,
      }
      # Menyimpan data dalam format JSON
      with open(f'data/{name}/{name}.json', 'w') as file:
          json.dump(data, file)
  def load_datan(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          auth = data['auth']
          return auth
      except FileNotFoundError:
          return None, None
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('nokofaucet')
  banner.banner('NOKOFAUCET')
  auth = load_datan('nokofaucet')
  if not os.path.exists("data/nokofaucet/nokofaucet.json"):
    save_datan(tele,'nokofaucet')
    nokofaucet(modulesl,banner,tele)
  curl=requests.Session()
  ua={
  "accept":"application/json, text/plain, */*",
  "authorization":auth
  }
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_user=json.loads(curl.get('https://api.nokofaucet.com/api/auth/me',headers=ua).text)
    _id1=get_user["_id"]
    print(hijau1+'> '+"Username : "+get_user["username"]+' | Email : '+get_user["email"])
    print(hijau1+'> '+"Balance : "+str(get_user["balance"])+' | Energy : '+str(get_user["energy"]))
  except Exception as e:
    save_datan(tele,'nokofaucet')
    nokofaucet(modulesl,banner,tele)
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  sl=curl.get('https://api.nokofaucet.com/api/shortlink/getPagnigation?keyword=&page=1&perPage=50&sortDate=undefined&sortBy=undefined&paginationVersion=2',headers=ua)
  methods = {
    '1Short.io': modulesl.shorti_io,
    'Bitads.pro': modulesl.bitads,
    'ShortFly': modulesl.shortfly,
    'LinksFly': modulesl.linksfly,
    'Linkvor': modulesl.linkvor_pw,
    'Try2link': modulesl.try2,
    'Cutty': modulesl.cuty_io,
    'Srinkearn': modulesl.shrinkearn,
    'Shrinkme': modulesl.shrinkme,
    'Clk.sh': modulesl.clksh,
    'Link1s': modulesl.links1s_com,
    'Freeltc.top': modulesl.freeltc_top,
    'Usalink': modulesl.usalink,
    'Web 1s normal': modulesl.web1s_info,
  }
  for data in sl.json()["data"]:
    name=data['title']
    jumlah=data['remain_view']
    _id=data['_id']
    for method, bypass_func in methods.items():
        try:
          if method in name:
               for jun in range(jumlah):
                url=curl.get('https://api.nokofaucet.com/api/shortlink/generate/'+_id,headers=ua).json()
                if 'url' in str(url):
                  answer = bypass_func(url["url"])
             #     print(answer)
                  if 'failed to bypass' in answer:
                    pass
                  else:
                    sleep(15)
                    key=answer.split('https://nokofaucet.com/user/short-link/')[1]
                    reward=curl.post("https://api.nokofaucet.com/api/shortlink/verify-shortlink",headers=ua,data={"key":key})
                    print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+json.loads(reward.text)["message"]+'               ')
        except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass faucet")
  for i in range(int(get_user["remain_claim"])):
    reward=curl.patch('https://api.nokofaucet.com/api/user/claim/'+_id1,headers=ua).json()
    print(reward)
    if 'successfully' in reward['message']:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward['message'])
      animasi(5)
    else:
      animasi(5)
  exit()
def landofbits(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('landofbits')
  banner.banner('LANDOFBITS')
  cookies, ugentmu = load_data('landofbits')
  if not os.path.exists("data/landofbits/landofbits.json"):
    save_data(tele,'landofbits')
    landofbits(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"landofbits.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://landofbits.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'landofbits')
    landofbits(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-lg-3 col-md-6'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[1]+' : '+info.text.strip().splitlines()[0])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  link=curl.get('https://landofbits.com/links',headers=ua,cookies=cookies)
  link=bs(link.text,'html.parser').find_all('div',{'class':'col-md-6 col-lg-4 mb-3 mb-lg-0'})
  services = {
    'Oii (Easy)': modulesl.oii,
    'FCLC (Easy)': modulesl.fl_lc,
    'LinksFly': modulesl.linksfly,
    'USALink': modulesl.usalink,
    'EXE (Easy)': modulesl.exe_io,
    'Cuty (Easy)': modulesl.cuty_io,
    'Web1s': modulesl.web1s_info,
    'Traffic1s': modulesl.trafic1s,
    '1short': modulesl._1short_in,
    'Shortsfly': modulesl.shortfly
  }
  for link in link:
   try:
    name=link.find('h5',{'class':'c_title text-center'}).text
    jumlah=int(link.find('a',{'class':'btn btn-one w-100 waves-effect waves-light'}).text.split('Claim ')[1].split('/')[0])
    link=link.find('a',{'class':'btn btn-one w-100 waves-effect waves-light'})['href']
    if name in services:
      for ulang in range(jumlah):
          url = curl.get(link, headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
          answer = services[name](url)
          if 'failed to bypass' in answer:
              print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
          else:
              sleep(105)
              reward = curl.get(answer, headers=ua, cookies=cookies)
              if 'Good job!' in reward.text:
                print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Good job! '+reward.text.split("text: '")[1].split("',")[0])
   except Exception as e:pass
  exit()
def cryptofuture(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  def save_data(tele,name):
    try:
        dir_path = f'data/{name}'
        os.makedirs(dir_path, exist_ok=True)  # Membuat direktori jika belum ada

        file_path = f'{dir_path}/{name}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
        if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim email faucetpay contoh : `/cookies nama_sesi email_fp`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                email=mes.split(name.upper()+' ')[1]
        else:
            email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
    except FileNotFoundError:
        if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim email faucetpay contoh : `/cookies nama_sesi email_fp`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                email=mes.split(name.upper()+' ')[1]
        else:
          email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
  def load_data(name):
    try:
        file_path = f'data/{name}/{name}.json'
        
        if os.path.isfile(file_path):  # Memeriksa apakah file ada, bukan direktori
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
                return email
        else:
            return None
    except FileNotFoundError:
        return None
  banner.banner('CRYPTOFUTURE')
  cookies= load_data('cryptofuture')
  if not os.path.exists("data/cryptofuture/cryptofuture.json"):
    save_data(tele,'cryptofuture')
    cryptofuture(modulesl,banner,tele)
  curl=requests.Session()
  step1=curl.get('https://CryptoFuture.co.in/?r=25876')
  fd=bs(step1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  data=f"wallet={cookies}&csrf_token_name={fd}"
  step2=curl.post('https://cryptofuture.co.in/auth/login',data=data,headers={"content-type":"application/x-www-form-urlencoded"})
  if 'Login Success' in step2.text:
    print(f'{putih1}[{hijau1} √ {putih1}] Login Success')
    options = {
    '1': 'LTC',
    '2': 'BNB',
    '3': 'BCH',
    '4': 'DOGE',
    '5': 'ETH',
    '6': 'FEY',
    '7': 'SOL',
    '8': 'TRX',
    '9': 'ZEC'
    }
    if tele==True:
      menu_text = "\n".join(f"{key}. {value}" for key, value in options.items())
      name="cryptofuture"
      send_signal(1111,f"`{name.upper()}` mengirim request input, Pilihan kripto : \n`{menu_text}`")
      mes=receive_signal(1111)
      if name.upper() in mes:
        user_input=mes.split(name.upper()+' ')[1]
    else:
      print('Pilihan kripto:')
      for key, value in options.items():
          print(f'{key}. {value}')
      user_input = input('Pilih kripto yang diinginkan: ')
    selected_crypto = options.get(user_input).lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner('CRYPTOFUTURE')
    get_links=curl.get('https://cryptofuture.co.in/links/currency/'+selected_crypto)
    gt=bs(get_links.text,'html.parser').find_all('div',{'class':'col-sm-6'})
    for link in gt:
      jumlah=int(link.find('span').text.split('/')[0])
      name=link.find('h4').text
      li=link.find('a',{'class':'btn btn-primary waves-effect waves-light'})['href']
      services = {
      'LinksFly': modulesl.linksfly,
      'ShortsFly.me': modulesl.shortfly,
      'Usalink': modulesl.usalink,
      }
      if name in services:
        for ulang in range(jumlah):
            url = curl.get(li,allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = services[name](url)
            if 'failed to bypass' in answer:
                print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
            else:
                reward = curl.get(answer)
                if 'Success!' in reward.text:
                  print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Success! '+reward.text.split("html: '")[1].split("',")[0])
def endenfaucet(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  def save_data(tele,name):
    try:
        dir_path = f'data/{name}'
        os.makedirs(dir_path, exist_ok=True)  # Membuat direktori jika belum ada

        file_path = f'{dir_path}/{name}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
        if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim email faucetpay contoh : `/cookies nama_sesi email_fp`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                email=mes.split(name.upper()+' ')[1]
        else:
            email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
    except FileNotFoundError:
        if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim email faucetpay contoh : `/cookies nama_sesi email_fp`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                email=mes.split(name.upper()+' ')[1]
        else:
          email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
  def load_data(name):
    try:
        file_path = f'data/{name}/{name}.json'
        
        if os.path.isfile(file_path):  # Memeriksa apakah file ada, bukan direktori
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
                return email
        else:
            return None
    except FileNotFoundError:
        return None
  banner.banner('EDENFAUCET')
  cookies= load_data('edenfaucet')
 # print(cookies)
  if not os.path.exists("data/edenfaucet/edenfaucet.json"):
    save_data(tele,'edenfaucet')
    endenfaucet(modulesl,banner,tele)
  curl=requests.Session()
  step1=curl.get('https://edenfaucet.com/?r=170')
  fd=bs(step1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  data=f"wallet={cookies}&csrf_token_name={fd}"
  step2=curl.post('https://edenfaucet.com/auth/login',data=data,headers={"content-type":"application/x-www-form-urlencoded"})
  if 'Login Success' in step2.text:
    print(f'{putih1}[{hijau1} √ {putih1}] Login Success')
    get_links=curl.get('https://edenfaucet.com/links/currency/doge')
  #  print(get_links.text)
    link=bs(get_links.text,'html.parser')
    jumlah=int(link.find('span',{'class':'badge badge-info'}).text.split('/')[0])
   # print(jumlah)
    for ulang in range(jumlah):
      get_links=curl.get('https://edenfaucet.com/links/go/1/DOGE',allow_redirects=False).headers['location']
      if 'https://edenfaucet.com/links/currency/DOGE' in get_links:
        get_links=curl.get('https://edenfaucet.com/links/reopen',allow_redirects=False).headers['location']
      answer=modulesl.gain_lk(get_links)
      #print(answer)
      if 'failed to bypass' in answer:
        pass
      else:
        sleep(105)
        reward=curl.get(answer)
       # print(reward.text)
      #  print(reward.text)
        if 'Success!' in reward.text:
            print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Success! '+reward.text.split("html: '")[1].split("',")[0])
def paid_family(url,sitkey,email,services,modulesl,tele):
  curl=requests.Session()
  login=curl.get(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"})
  frc=bs(login.text,'html.parser').find('input',{'name':'frsc'})['value']
  answer=modulesl.RecaptchaV2(key=sitkey,url=url)
  data=f"frsc={frc}&guest_email={email}&captcha=recaptchaV2&g-recaptcha-response={answer}&Guest_Login=Guest_Login"
  login=curl.post(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/x-www-form-urlencoded"},data=data)
  if 'user' in login.url:
    print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Login Success!!                                  ')
    link=bs(login.text,'html.parser').find_all('tr')
    del link[0]
    for links in link:
      li=links.find('a')['href']
      lis= [element.strip() for element in links.text.strip().splitlines()]
      name=lis[0]
      jumlah=int(lis[9].split('/')[0])
      if name in services:
        for ulang in range(jumlah):
       #   while True:
            url = curl.get(li,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"},allow_redirects=False).text.split('<script>location.href = "')[1].split('";</script>')[0]
            answer = services[name](url)
            if 'failed to bypass' in answer:
                print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
            else:
                sleep(105)
                reward = curl.get(answer,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"})
                if 'Well done :)' in reward.text:
                  sukses=bs(reward.text,'html.parser').find('div',{'class':'alert alert-success d-flex'}).text
                  print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+sukses)
                if 'Error!!' in reward.text:
                  sukses=bs(reward.text,'html.parser').find('div',{'class':'alert alert-danger d-flex'}).text
                 # if 'Error!! Shortlink Failed!' in sukses:
                  #  print(f'{putih1}[{merah1} x {putih1}] {merah1}'+sukses,end='\r')
               #   else:
                 #   print(f'{putih1}[{merah1} x {putih1}] {merah1}'+sukses)
                  #  break
def all_in_one(modulesl,banner,tele=None):
  def save_data(tele,name):
    try:
        dir_path = f'data/{name}'
        os.makedirs(dir_path, exist_ok=True)  # Membuat direktori jika belum ada

        file_path = f'{dir_path}/{name}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
        if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim email faucetpay contoh : `/cookies nama_sesi email_fp`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                email=mes.split(name.upper()+' ')[1]
        else:
            email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
    except FileNotFoundError:
        if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim email faucetpay contoh : `/cookies nama_sesi email_fp`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                email=mes.split(name.upper()+' ')[1]
        else:
          email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
  def load_data(name):
    try:
        file_path = f'data/{name}/{name}.json'
        
        if os.path.isfile(file_path):  # Memeriksa apakah file ada, bukan direktori
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
                return email
        else:
            return None
    except FileNotFoundError:
        return None
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner('ALL IN ONE PAID FAMILY')
  cookies= load_data('all_in_one')
  if not os.path.exists("data/all_in_one/all_in_one.json"):
    save_data(tele,'all_in_one')
    all_in_one(modulesl,banner,tele)
  service = {
      'Try2link.com': modulesl.try2,
      'Shrinkearn.com': modulesl.shrinkearn,
      'Usalink.io': modulesl.usalink,
      'Clk.sh': modulesl.clksh,
      'Linksfly.me': modulesl.linksfly,
      'Shortsfly.me': modulesl.shortfly,
      'Shorti.io': modulesl.shorti_io,
      'Oii.io': modulesl.oii,
      'Illink.net': modulesl.illink_net,
      'Owllink.net': modulesl.owlink,
      'Birdurls.com': modulesl.birdurl,
      'Fc.lc': modulesl.fl_lc,
      'Exe.io': modulesl.exe_io
  }
  print(hijau1+"> "+kuning1+"Start bypass liteearn.com")
  paid_family('https://liteearn.com/',"6Lejju8UAAAAAMCxObwhQJliWyTUXwEcUc43KOiQ",cookies,service,modulesl,tele)
  service = {
      'Try2link.com': modulesl.try2,
      'Shrinkearn.com': modulesl.shrinkearn,
      'Clk.sh': modulesl.clksh,
      'Linksfly.me': modulesl.linksfly,
      'Shortsfly.me': modulesl.shortfly,
      'Shorti.io': modulesl.shorti_io,
      'Oii.io': modulesl.oii,
      'Illink.net': modulesl.illink_net,
      'Owllink.net': modulesl.owlink,
      'Birdurls.com': modulesl.birdurl,
      'Fc.lc': modulesl.fl_lc,
      'Exe.io': modulesl.exe_io
  }
  print(hijau1+"> "+kuning1+"Start bypass paidtomoney.com")
  paid_family('https://paidtomoney.com/',"6LfZswEVAAAAAHXORtki0EFzDZZIV02Wo0krcxRo",cookies,service,modulesl,tele)
  service = {
      'Try2link.com': modulesl.try2,
      'Shrinkearn.com': modulesl.shrinkearn,
      'Usalink.io': modulesl.usalink,
      'Clk.sh': modulesl.clksh,
      'Linksfly.me': modulesl.linksfly,
      'Shortsfly.me': modulesl.shortfly,
      'Shorti.io': modulesl.shorti_io,
      'Oii.io': modulesl.oii,
      'Illink.net': modulesl.illink_net,
      'Owllink.net': modulesl.owlink,
      'Birdurls.com': modulesl.birdurl,
      'Fc.lc': modulesl.fl_lc,
      'Exe.io': modulesl.exe_io
  }
  print(hijau1+"> "+kuning1+"Start bypass cryptosfaucet.top")
  paid_family('https://cryptosfaucet.top/',"6Lea9VImAAAAADHt5Lp2LqCt0vOHfab86HnThbl8",cookies,service,modulesl,tele)
def bitscript_family(url,services,modulesl,banner,key_links,tele):
  host=urlparse(url).netloc
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper())
  data_control(host)
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele,host)
    bitscript_family(url,services,modulesl,banner,key_links,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dahs=curl.get(url+'account',headers=ua,cookies=cookies)
 # print(dahs.text)
  if 'Balance' not in dahs.text:
    save_data(tele,host)
    bitscript_family(url,services,modulesl,banner,key_links,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  print(hijau1+'> '+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  link=curl.get(url+'shortlinks',headers=ua,cookies=cookies)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  providers=services
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
    #  print(i)
      for provider in providers:
          if provider in name:
           #   print(name)
              y=[i for i in i.text.strip().splitlines() if i][2]
              if 'clicks remaining' in y:
                y=y.split(' clicks remaining')[0].replace(' ','')
              if 'click remaining' in y:
                y=y.split(' click remaining')[0].replace(' ','')
              link=i.find('a',{'class':key_links})['href']
              for ulang in range(int(y)):
                  get_links = curl.get(url+ link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
        #          print(reward.text)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies)
                    if 'Congratulations.' in reward.text:
                      _1 = reward.text.split("message: '")[1].split("'")[0]
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+_1)
    except Exception as e:
      pass
def earnfree_cash(modulesl,banner,tele=None):
  services={
      'LinksFly': modulesl.linksfly,
      'MegaURL': modulesl.megaurl,
      'ShrinkEarn': modulesl.shrinkearn,
      'Ctr.sh': modulesl.ctrsh,
      'Ex-Foary': modulesl.ex_foary_com,
      'illink': modulesl.illink_net,
      'Usalink': modulesl.usalink,
      "Clks":modulesl.clks_pro,
      "Clk.sh":modulesl.clksh,
     # 'Chl': None,
      'BirdUrls': modulesl.birdurl,
      'Adshort': modulesl.adshorti_co,
      'OwlLink': modulesl.owlink,
      'Fc.Lc': modulesl.fl_lc,
      'Cuty': modulesl.cuty_io,
     # 'Flyadvip': None,
      'Exe': modulesl.exe_io,
      'Mitly': modulesl.mitly,
      'Shorti': modulesl.shorti_io
  }
  bitscript_family('https://earnfree.cash/',services,modulesl,banner,"card shadow text-decoration-none",tele)
  exit()
def paidbucks(modulesl,banner,tele=None):
  services={
      'Linksfly': modulesl.linksfly,
      'MegaURL': modulesl.megaurl,
      'ShrinkEarn': modulesl.shrinkearn,
      'Ctr.sh': modulesl.ctrsh,
      'Ex-Foary': modulesl.ex_foary_com,
      'illink': modulesl.illink_net,
      'Usalink': modulesl.usalink,
     # 'Chl': None,
      'BirdUrls': modulesl.birdurl,
   #   'Adshort': None,
      'OwlLink': modulesl.owlink,
      'Fclc': modulesl.fl_lc,
      'Cuty': modulesl.cuty_io,
     # 'Flyadvip': None,
      'Exe': modulesl.exe_io,
      'Mitly': modulesl.mitly,
      'Clksh': modulesl.clksh,
      'Shorti': modulesl.shorti_io
  }
  bitscript_family('https://paidbucks.xyz/',services,modulesl,banner,"card shadow text-decoration-none text-dark",tele)
def clickscoin(modulesl,banner,tele=None):
  url="https://clickscoin.com/account"
  host=urlparse(url).netloc
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper())
  data_control(host)
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele,host)
    clickscoin(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  try:
    dahs=curl.get(url+'/account',headers=ua,cookies=cookies)
    if 'Balance' not in dahs.text:
      save_data(tele,host)
      clickscoin(modulesl,banner,tele)
  except Exception as e:
      save_data(tele,host)
      clickscoin(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('div',{'class':'info-area'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> '+fd[0].text.strip().splitlines()[2]+' : '+fd[0].text.strip().splitlines()[0])
  link=curl.get("https://clickscoin.com/shortlinks",headers=ua,cookies=cookies)
 # print(link.text)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-xl-3 col-md-6'})
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  providers={
    'TRAFFIC1S': modulesl.trafic1s,
  #  'EARNNOW': None,
    'SHORTSFLY': modulesl.shortfly,
    'CLK.SH': modulesl.clksh,
    'LINKS FLY.INC': modulesl.linksfly,
 #   'CLICKSFLY': None,
    'SHRINKEARN': modulesl.shrinkearn,
    'EZ4SHORT': modulesl.ez4short,
  #  'ADLINKCLICK': None,
    'COINSPARTY': modulesl.coinparty,
    'LINK1SCOM': modulesl.links1s_com,
    'DROPLINK': modulesl.droplink,
    'FCLC': modulesl.fl_lc,
    'MEGAURL': modulesl.megaurl,
    'LINKSLY': modulesl.linksly,
  #  'SHORTANO': None,
    'LINK1SNET': modulesl.link1s_net,
    'ADSHORT': modulesl.adshorti_co,
   # 'TMEARN': None,
   # 'CLICKSCOIN': None,
  #  'PROMO-VISITS': None,
    '1SHORT': modulesl._1short_in,
 #   'DASH-FREE': None,
 #   'RAINURL': None,
    'OWLLINK': modulesl.owlink,
    'EXFOARY': modulesl.ex_foary_com,
    'MITLY': modulesl.mitly,
    'MEGAFLY': modulesl.megafly,
 #   'FIRE-LINK': None,
    'ILLINK': modulesl.illink_net,
 #   'LINKFLY': None,
 #   'GTLINK': None,
    'BIRDURLS': modulesl.birdurl,
    'TRY2LINK': modulesl.try2,
  #  'SNOWURL': None,
   # 'SHORTIT': None
  }

  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
   #   print([i for i in i.text.strip().splitlines() if i])
      for provider in providers:
          if provider in name:
           #   print(name)
              y=[i for i in i.text.strip().splitlines() if i]
              link=i.find('a')['href']
            #  print(link)
              for ulang in range(int(y[3])):
                  get_links = curl.get("https://clickscoin.com"+ link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
        #          print(reward.text)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies)
                    if 'Congratulations.' in reward.text:
                      _1 = reward.text.split("message: '")[1].split("'")[0]
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+_1)
    except Exception as e:
      pass
def tron0x(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('tron0x')
  banner.banner('TRON0X')
  cookies, ugentmu = load_data('tron0x')
  if not os.path.exists("data/tron0x/tron0x.json"):
    save_data(tele,'tron0x')
    tron0x(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"tron0x.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://tron0x.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'tron0x')
    tron0x(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://tron0x.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
    "Exe": modulesl.exe_io,
    "Mega Fly": modulesl.megafly,
    "Mega URL": modulesl.megaurl,
    "Owl Link": modulesl.owlink,
    "Il Link": modulesl.illink_net,
    "Bird Urls": modulesl.birdurl,
    "Fc.lc": modulesl.fl_lc,
    "Shorti": modulesl.shorti_io,
    "Clk.sh": modulesl.clksh,
    "Try2link": modulesl.try2,
    "Link1s": modulesl.links1s_com,
    "Shrinkme": modulesl.shrinkme,
    "Cuty": modulesl.cuty_io,
    "LinksFly": modulesl.linksfly,
    "Shrink Earn": modulesl.shrinkearn,
    "Clks": modulesl.clks_pro,
    "Bitads": modulesl.bitads,
    "Ctr.sh": modulesl.ctrsh,
    "USA Link": modulesl.usalink
  }
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://tron0x.com/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(60)
    reward=curl.post('https://tron0x.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(f'{putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     exit()
  exit()
def faucetpayz(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucetpayz')
  banner.banner('FAUCETPAYZ')
  cookies, ugentmu = load_data('faucetpayz')
  if not os.path.exists("data/faucetpayz/faucetpayz.json"):
    save_data(tele,'faucetpayz')
    faucetpayz(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":"faucetpayz.com",
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  dash=curl.get('https://faucetpayz.com/dashboard',headers=ua,cookies=cookies)
  if 'Balance' not in dash.text:
    save_data(tele,'faucetpayz')
    faucetpayz(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucetpayz.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
          "Shortsfly":modulesl.shortfly,
          "Linksfly":modulesl.linksfly,
    }
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
                    sleep(105)
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
