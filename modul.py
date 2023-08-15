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
import requests,queue,cloudscraper
from PIL import Image, ImageDraw, ImageFont
import socket
from rich.tree import Tree
from rich import print as rprint
FONT_URL = "https://github.com/stamen/toner-carto/raw/master/fonts/Arial-Unicode-Bold.ttf"  # Ganti dengan URL font yang valid
FONT_PATH = "Arial-Unicode-Bold.ttf"  # Path font yang diinginkan
hijau1 = "\033[1;92m"#Terang
kuning1 = "\033[1;93m"#Terang
putih1 = "\033[1;97m"#Terang
merah1 = "\033[1;91m"#Terang
biru1 = "\033[1;94m"#Terang
def keluar(error):
  lis=["KeyboardInterrupt"]
  error=str(error)
  if error in lis:exit()
def ua(host, user_agent, accept, content_type=None):
    headers = {
        'Host': host,
        'User-Agent': user_agent,
        'Accept': accept
    }
    if content_type:
        headers['Content-Type'] = content_type
    return headers
def parser(text):
    if len(text) <= 30:
        return text
    else:
        return text[:30] + '.' * 3
def parser_list(lis):
  filtered_list = list(filter(lambda x: x.strip(), lis))
  return filtered_list
def end():
  return ' '*40+'\r'
def status_code(req):
  print(putih1+"Response "+str(req.status_code)+' '+req.reason,end=end())
  sleep(0.7)
  print(' ',end=end())
def persen(detik):
        for detik_proses in range(detik + 1):
            persen = (detik_proses / detik) * 100
            print(f"{persen:.2f}%", end=end())
            time.sleep(1)
        print(end())
def bypass_link(url,modulesl,jumlah):
  dictnya={
  "1short.info":modulesl._1short_in,
  "adbitfly.com":modulesl.adbitfly,
  "adbull.me":modulesl.adbull,
  "adshort.co":modulesl.adshorti_co,
  "bitads.pro":modulesl.bitads,
  "ser2.crazyblog.in":modulesl.cbshort,
  "m.pkr.pw":modulesl.cashurl_win,
  "nx.chainfo.xyz":modulesl.chainfo,
  #"":modulesl.clickzu_icu,
  "link.adshorti.xyz":modulesl.adshorti_xyz,
  "go.birdurls.com":modulesl.birdurl,
  "oko.sh":modulesl.clksh,
  #"":modulesl.coinparty,
  "ctr.sh":modulesl.ctrsh,
  "cuty.io":modulesl.cuty_io,
 # "clks.pro":modulesl.clks_pro,
  "droplink.co":modulesl.droplink,
  "ex-foary.com":modulesl.ex_foary_com,
  "exe.io":modulesl.exe_io,
  "ez4short.com":modulesl.ez4short,
  "fc-lc.com":modulesl.fl_lc,
  "flyzu.icu":modulesl.flyzu,
  "link.freeltc.top":modulesl.freeltc_top,
  "gplinks.co":modulesl.gplinks_bypass,
  "ser7.crazyblog.in":modulesl.hrshort,
  "go.illink.net":modulesl.illink_net,
  "insfly.pw":modulesl.insfly,
  "kiiw.icu":modulesl.kiw_app,
  "link1s.net":modulesl.link1s_net,
  "link4m.com":modulesl.link4m_com,
  "linkjust.com":modulesl.linkjust,
  "link1s.com":modulesl.links1s_com,
  "linksfly.me":modulesl.linksfly,
  "urlsfly.me":modulesl.urlsfly,
  "linksly.co":modulesl.linksly,
  "link4.pw":modulesl.linkvor_pw,
  "go.megafly.in":modulesl.megafly,
  "go.megaurl.in":modulesl.megaurl,
  "mitly.us":modulesl.mitly,
  "oii.io":modulesl.oii,
  "go.owllink.net":modulesl.owlink,
  "go.sigmalinks.in":modulesl.shareus,
  "shortsfly.me":modulesl.shortfly,
  "wefly.me":modulesl.wefly,
  "link.shorti.io":modulesl.shorti_io,
  #"":modulesl.shortzu_icu,
  "tii.la":modulesl.shrinkearn,
  "shrinke.me":modulesl.shrinkme,
  "go.softindex.website":modulesl.softindex_website,
  "traffic1s.com":modulesl.trafic1s,
  "try2link.com":modulesl.try2,
  "url.namaidani.net":modulesl.url_namaidani,
  "url.namaidani.com":modulesl.url_namaidani,
  "go.urlcash.site":modulesl.urlcash,
  "link.usalink.io":modulesl.usalink,
  "zuba.link":modulesl.zuba_link,
  "sl-2.askpaccosi.com":modulesl.sl_ask,
  "panylink.com":modulesl.panylink,
  }
  if urlparse(url).netloc in dictnya:
    print(putih1+'├──'+'─'*56)
    print(f"├── {putih1}[{kuning1}{jumlah[0]}/{jumlah[1]}{putih1}] {kuning1} Bypassing : {hijau1}{url}")
    res=dictnya[urlparse(url).netloc](url)
    if "failed to bypass" in res:
      print(putih1+'├── '+kuning1+'Status : '+merah1+res)
      print(putih1+'├──'+'─'*56)
    else:
      print(putih1+'├── '+kuning1+'Status : '+hijau1+"success")
      print(putih1+'├──'+'─'*56)
      return res
  else:
    return False
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
def animasi(menit=None,detik=None):
  if menit:
    detik = menit * 60
  if detik:
    detik=detik
  pattern_list = list("▁▃▅▇▅▃▁") * detik
  for i in range(detik):
      animasi = "".join(pattern_list[i:i+5])
      output = f"{hijau1}[{kuning1}{animasi}{hijau1}] {putih1}- {hijau1}Please wait {hijau1}{detik//60:02d}:{detik%60:02d}"
      print(output, end=' '*20+'\r')
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
def save_data(tele,name):
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
            data = json.load(file)
            cookies = data.get('cookies')
            user_agent = data.get('user_agent')
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://btccanyon.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://btccanyon.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
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
      ve = requests.post('https://btccanyon.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
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
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'btccanyon')
    btccanyon(modulesl,banner,tele)
  try:
    akun=Tree("[green] > [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,'btccanyon')
    btccanyon(modulesl,banner,tele)
  pct=Tree("[gree] > [yellow]Start working on ptc")
  rprint(pct)
  get_ptc=curl.get('https://btccanyon.com/ptc.html',headers=ua,cookies=cookies)
  status_code(get_ptc)
  def balance():
    get_sl=curl.get('https://btccanyon.com/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
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
    status_code(get_reward)
    token1=get_reward.text.split("var token = '")[1].split("';")[0]
    secon=get_reward.text.split("var secs = ")[1].split(";")[0]
    for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
            time.sleep(1)
            pass
    answer=get_answer()
    reward=curl.post('https://btccanyon.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies)
    status_code(reward)
    if json.loads(reward.text)["status"] == 200:
      gas=bs(json.loads(reward.text)["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
      sesi=True
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  sl=Tree("[green]> [yellow]Start Bypassing Shortlinks")
  rprint(sl)
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
      re=jumlah
      for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
          get_sl = curl.get('https://btccanyon.com/shortlinks.html', headers=ua, cookies=cookies)
          status_code(get_sl)
          token = get_sl.text.split("var token = '")[1].split("';")[0]
          status = True
          while(status==True):
              da = id["onclick"].split("goShortlink('")[1].split("');")[0]
              gt_lk = curl.post('https://btccanyon.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies)
              status_code(gt_lk)
              get_lk=json.loads(gt_lk.text)
              if get_lk["status"] == 200:
                  answer = bypass_link(get_lk['shortlink'],modulesl,jumlah=[str(re),str(jumlah)])
                  if answer==False:break
                  if 'failed to bypass' in answer:pass
                  if answer:
                      try:
                          get_sl = curl.get(answer, headers=ua, cookies=cookies)
                          status_code(get_sl)
                          sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
                          re-=1
                      except:
                          print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"invalid keys")
                  break
              if get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
              else:
                print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                break
   except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  faucet=Tree("[green] > [yellow]Bypass faucet")
  rprint(faucet)
  while True:
    get_sl=curl.get('https://btccanyon.com/',headers=ua,cookies=cookies)
    status_code(get_sl)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LdzF6MlAAAAACcN9JGXW8tSs4dy1MjeKZKFJ11M',get_sl.url)
    gt=curl.post('https://btccanyon.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies)
    status_code(gt)
    g=json.loads(gt.text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://claimlite.club/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://claimlite.club/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
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
      ve = requests.post('https://claimlite.club/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
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
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'claimlite')
    claimlite(modulesl,banner,tele)
  try:
    akun=Tree("[green]> [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,'claimlite')
    claimlite(modulesl,banner,tele)
  ptc=Tree("[green]> [yellow]Start working on ptc")
  rprint(ptc)
  get_ptc=curl.get('https://claimlite.club/ptc.html',headers=ua,cookies=cookies)
  status_code(get_ptc)
  def balance():
    get_sl=curl.get('https://claimlite.club/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
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
    status_code(get_reward)
    token1=get_reward.text.split("var token = '")[1].split("';")[0]
    secon=get_reward.text.split("var secs = ")[1].split(";")[0]
    for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
            time.sleep(1)
            pass
    answer=get_answer()
    reward=curl.post('https://claimlite.club/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies)
    status_code(reward)
    if json.loads(reward.text)["status"] == 200:
      gas=bs(json.loads(reward.text)["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
      sesi=True
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  sl=Tree("[green]> [yellow]Start Bypassing Shortlinks")
  rprint(sl)
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
      re=jumlah
      for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
          get_sl = curl.get('https://claimlite.club/shortlinks.html', headers=ua, cookies=cookies)
          status_code(get_sl)
          token = get_sl.text.split("var token = '")[1].split("';")[0]
          status = True
          while(status==True):
              da = id["onclick"].split("goShortlink('")[1].split("');")[0]
              get_lk = curl.post('https://claimlite.club/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies)
              status_code(get_lk)
              get_lk=json.loads(get_lk.text)
              if get_lk["status"] == 200:
                answer = bypass_link(get_lk['shortlink'], modulesl, jumlah=[str(re), str(jumlah)])
                if answer == False:
                    break
                elif 'failed to bypass' in answer:
                    pass
                else:
                    try:
                        get_sl = curl.get(answer, headers=ua, cookies=cookies)
                        status_code(get_sl)
                        sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                        print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                        print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
                        re-=1
                    except:
                        print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"invalid keys")
                break
              if get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
              else:
                print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                break
   except Exception as e:
    keluar(str(e))
    pass
  print(putih1+'├──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  rprint(Tree("[green]> [yellow]Bypass faucet"))
  while True:
    get_sl=curl.get('https://claimlite.club/',headers=ua,cookies=cookies)
    status_code(get_sl)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Leen-YUAAAAAFsd9t6qwRGyF8fLf6kixqicahQj',get_sl.url)
    g=curl.post('https://claimlite.club/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies)
    status_code(g)
    g=json.loads(g.text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://rushbitcoin.com/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://rushbitcoin.com/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
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
      ve = requests.post('https://rushbitcoin.com/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
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
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'rushbitcoin')
    rushbitcoin(modulesl,banner,tele)
  try:
    akun=Tree("[green]> [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,'rushbitcoin')
    rushbitcoin(modulesl,banner,tele)
  rprint(Tree("[green]> [yellow]Start working on ptc"))
  get_ptc=curl.get('https://rushbitcoin.com/ptc.html',headers=ua,cookies=cookies)
  status_code(get_ptc)
  def balance():
    get_sl=curl.get('https://rushbitcoin.com/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
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
      status_code(get_reward)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://rushbitcoin.com/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     keluar(str(e))
     print(hijau1+'[ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,'rushbitcoin')
     rushbitcoin(modulesl,banner,tele)
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  rprint(Tree("[green]> [yellow]Start Bypassing Shortlinks"))
  for i in gt_s:
    try:
        name = i.find('td', {'class': 'align-middle'}).text
        id = i.find('button', {'class': 'btn btn-success btn-sm'})
        if None == id:
            pass
        else:
          jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
          re=jumlah
          for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
              get_sl = curl.get('https://rushbitcoin.com/shortlinks.html', headers=ua, cookies=cookies)
              status_code(get_sl)
              token = get_sl.text.split("var token = '")[1].split("';")[0]
              status = True
              while status == True:
                  da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                  get_lk = json.loads(curl.post('https://rushbitcoin.com/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                  if get_lk["status"] == 200:
                      answer = bypass_link(get_lk["shortlink"],modulesl,jumlah=[str(re),str(jumlah)])
                      if answer == False:
                          break
                      if "failed to bypass" == answer:pass
                      else:
                          time.sleep(10)
                          get_sl = curl.get(answer, headers=ua, cookies=cookies)
                          status_code(get_sl)
                          try:
                              sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                              print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                              print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
                          except:
                              print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                          break
                  if get_lk['status'] == 600:
                    print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                  else:
                    print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                    break
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  rprint(Tree("[green]> [yellow]Bypass faucet"))
  while True:
    get_sl=curl.get('https://rushbitcoin.com/',headers=ua,cookies=cookies)
    status_code(get_sl)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LfokMEUAAAAAEwBx23jh3mlghwTF7VJqbN9fERK',get_sl.url)
    g=curl.post('https://rushbitcoin.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies)
    status_code(g)
    g=json.loads(g.text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
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
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
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
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://claimbits.net/faucet.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  try:
    akun=Tree("[green]> [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    if 'Balance' not in get_sl.text:
      save_data(tele,nama_host)
      claimbits(modulesl,banner,tele)
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,nama_host)
    claimbits(modulesl,banner,tele)
  rprint(Tree("[green]> [yellow]Start working on ptc"))
  get_ptc=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
  def balance():
    get_sl=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
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
      status_code(get_reward)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(putih1+'├──'+hijau1+f' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(putih1+'├──'+hijau1+f' [ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     keluar(str(e))
     print(putih1+'└──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,nama_host)
     claimbits(modulesl,banner,tele)
  print(putih1+'└──'+hijau1+f' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  rprint(Tree("[green]> [yellow]Start Bypassing Shortlinks"))
  for i in gt_s:
    try:
      name = i.find('td', {'class': 'align-middle'}).text
      id = i.find('button', {'class': 'btn btn-success btn-sm'})
      if None == id:
          pass
      else:
        jumlah=(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0]))
        re=jumlah
        for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
            get_sl = curl.get('https://'+host+'/shortlinks.html', headers=ua, cookies=cookies)
            status_code(get_sl)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            status = True
            while status == True:
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                if get_lk["status"] == 200:
                    answer = bypass_link(get_lk["shortlink"],modulesl,jumlah=[str(re),str(jumlah)])
                    if answer==False:break
                    if "failed to bypass" == answer:pass
                    else:
                        time.sleep(10)
                        get_sl = curl.get(answer, headers=ua, cookies=cookies)
                        status_code(get_sl)
                        try:
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(putih1+'├──'+hijau1+f' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                            print(putih1+'├──'+hijau1+f' [ '+kuning1+'+'+hijau1+' ] '+balance())
                            re-=1
                        except:
                            print(putih1+'├──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                        break
                if get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                else:
                  print(putih1+'├──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                  break
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  rprint(Tree("[green]> [yellow]Bypass faucet"))
  while True:
   try:
    get_sl=curl.get('https://claimbits.net/faucet.html',headers=ua,cookies=cookies)
    status_code(get_sl)
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
      print(putih1+'├──'+hijau1+f' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'└──'+hijau1+f' [ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
   except Exception as e:
     print('Cloudflare!!')
     keluar(str(e))
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://'+host+f'/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
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
      ve = requests.post('https://'+host+'/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
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
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,nama_host)
    ltchunt(modulesl,banner,tele)
  try:
    akun=Tree("[green]> [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,nama_host)
    ltchunt(modulesl,banner,tele)
  rprint(Tree("[green]> [yellow]Start working on ptc"))
  get_ptc=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
  status_code(get_ptc)
  def balance():
    get_sl=curl.get('https://'+host+'/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
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
      status_code(get_reward)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=json.loads(curl.post('https://'+host+'/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies).text)
      if reward["status"] == 200:
        gas=bs(reward["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(putih1+'├──'+hijau1+f' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(putih1+'├──'+hijau1+f' [ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
   except Exception as e:
     print(putih1+'└──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"session expired log out dan login ulang")
     save_data(tele,nama_host)
     ltchunt(modulesl,banner,tele)
  print(putih1+'└──'+hijau1+f' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  rprint(Tree("[green]> [yellow]Start Bypassing Shortlinks"))
  for i in gt_s:
    try:
      name = i.find('td', {'class': 'align-middle'}).text
      id = i.find('button', {'class': 'btn btn-success btn-sm'})
      if None == id:
          pass
      else:
        jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
        re=jumlah
        for j in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
            get_sl = curl.get('https://'+host+'/shortlinks.html', headers=ua, cookies=cookies)
            status_code(get_sl)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            status = True
            while status == True:
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                get_lk = json.loads(curl.post('https://'+host+'/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies).text)
                if get_lk["status"] == 200:
                    answer = bypass_link(get_lk["shortlink"],modulesl,jumlah=[str(re),str(jumlah)])
                    if answer==False:break
                    if "failed to bypass" == answer:pass
                    else:
                        time.sleep(10)
                        get_sl = curl.get(answer, headers=ua, cookies=cookies)
                        status_code(get_sl)
                        try:
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(putih1+'├──'+hijau1+f' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                            print(putih1+'├──'+hijau1+f' [ '+kuning1+'+'+hijau1+' ] '+balance())
                            re-=1
                        except:
                            print(putih1+'├──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"invalid keys",end="\r")
                        break
                if get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
                else:
                  print(putih1+'├──'+hijau1+f' [ '+merah1+'x'+hijau1+' ] '+"There seems to be something wrong with the link")
                  break
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  rprint(Tree("[green]> [yellow]Bypass faucet"))
  while True:
    get_sl=curl.get('https://'+host+'/',headers=ua,cookies=cookies)
    status_code(get_sl)
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
      print(putih1+'├──'+hijau1+f' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+f' [ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(300)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
#offf
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
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://'+host+'/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light').text
      hash = eval(gt_cp)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://claimsatoshi.xyz/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Current Balance' not in dash.text:
    save_data(tele,'claimsatoshi')
    claimsatoshi(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-xl-3 col-sm-6'})
  akun=Tree("[green]> [yellow]Account information")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[1]+' [white]:[yellow] '+info.text.strip().splitlines()[0])
  rprint(akun)
  rprint(Tree("[green]> [yellow]Start ptc"))
  ptc=curl.get('https://claimsatoshi.xyz/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  surf=bs(ptc.text,'html.parser').find_all('div',{'class':'col-12 col-lg-4 mb-3 mb-lg-0'})
  if 'Website Available' not in ptc.text:
    save_data(tele,'claimsatoshi')
    claimsatoshi(modulesl,banner,tele)
  for surf in surf:
   try:
    url=surf.find('button',{'class':'btn btn-one bg-dark btn-block'})['onclick'].split("window.location = '")[1].split("'")[0]
    name=surf.find('h2',{'class':'card-title'}).text.strip()
    print(putih1+'├──'+hijau1+f' [{kuning1} ~ {putih1}] {kuning1}View : '+parser(name),end='\r')
    surf1=curl.get(url,headers=ua,cookies=cookies)
    status_code(surf1)
    animasi(detik=int(surf1.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(surf1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',url)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(url.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    status_code(verify)
    print(putih1+'├──'+hijau1+f' [{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     keluar(str(e))
     pass
  rprint(Tree("[green]> [yellow]Start shortlinks"))
  gt_link = curl.get('https://claimsatoshi.xyz/links', headers=ua, cookies=cookies)
  gtf = bs(gt_link.text, 'html.parser')
  gt_info = gtf.find_all('div', {'class': 'col-12 col-lg-4 mb-3 mb-lg-0'})
  for link in gt_info:
    try:
      lik = link.find('a')["href"]
      get_info = [i for i in link.text.strip().splitlines() if i]
      #print(get_info)
      jumlah=int(get_info[4].split('/')[0].split('Claim ')[1])
      re=jumlah
      for i in range(int(get_info[4].split('/')[0].split('Claim ')[1])):
        get_lik = curl.get(lik, headers=ua, cookies=cookies, allow_redirects=False)
        status_code(get_lik)
        get_lik=get_lik.text.split('<script> location.href = "')[1].split('"; </script>')[0]
        print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_lik,end='\r')
        answer = bypass_link(get_lik,modulesl,jumlah=[str(re),str(jumlah)])
        if answer==False:
           break
        if 'failed to bypass' in answer:
          pass
        else:
          animasi(detik=105)
          reward = curl.get(answer, headers=ua, cookies=cookies).text
          if 'Good job!' in reward:
            print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
            re-=1
          else:
            print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
      keluar(str(e))
      pass
  rprint("[green]> [yellow]Start auto faucet")
  while True:
   try:
    get_=curl.get('https://claimsatoshi.xyz/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=15)
    reward=curl.post('https://claimsatoshi.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    if 'Good job!' in reward.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
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
    
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://coinfola.com/account',headers=ua,cookies=cookies)
    status_code(dahs)
  except Exception as e:
    save_data(tele,'coinfola')
    coinfola(modulesl,banner,tele)
  if 'Balance' not in dahs.text:
      save_data(tele,'coinfola')
      coinfola(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-hover table-striped'})
  akun=Tree("[green]> [yellow]Account information")
  akun.add('[green]> [yellow]'+fd[0].text.strip().splitlines()[0]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[1])
  akun.add('[green]> [yellow]'+fd[0].text.strip().splitlines()[4]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[5])
  akun.add('[green]> [yellow]'+fd[0].text.strip().splitlines()[8]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[9])
  rprint(akun)
  link=curl.get('https://coinfola.com/shortlinks',headers=ua,cookies=cookies)
  status_code(link)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-3'})
  rprint(Tree("[green]> [yellow]Start bypass shortlinks"))
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
    #  print(i)
      y=[i for i in i.text.strip().splitlines() if i][2]
      if 'clicks remaining' in y:
        y=y.split(' clicks remaining')[0].replace(' ','')
      if 'click remaining' in y:
        y=y.split(' click remaining')[0].replace(' ','')
      link=i.find('a',{'class':'card shadow text-decoration-none'})['href']
      #answer = bypass_link(url)
      re=int(y)
      for ulang in range(int(y)):
          get_links = curl.get('https://coinfola.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
          #print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end=end())
          answer = bypass_link(get_links,modulesl,jumlah=[str(re),y])
          if answer==False:
                break
          if 'failed to bypass' in answer:
              pass
          else:
            animasi(detik=105)
            reward = curl.get(answer, headers=ua, cookies=cookies)
            if 'Congratulations.' in reward.text:
                _1 = reward.text.split("message: 'You")[1].split("tickets.'")[0]
                _2 = reward.text.split("message: 'Congratulations.")[1].split("credited.'")[0]
                print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Congratulations. ' + _2 + ' credited. & You ' + _1 + ' tickets.')
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
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
    
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://adhives.com/account',headers=ua,cookies=cookies)
    status_code(dahs)
  except Exception as e:
    save_data(tele,'adhives')
    adhives(modulesl,banner,tele)
  if 'Balance' not in dahs.text:
      save_data(tele,'adhives')
      adhives(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
  akun = Tree("[green]> [yellow]Account information")
  akun.add('[green]> [yellow]'+fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1])
  akun.add('[green]> [yellow]'+fd[0].text.strip().splitlines()[4]+' : '+fd[0].text.strip().splitlines()[5])
  rprint(akun)
  link=curl.get('https://adhives.com/shortlinks',headers=ua,cookies=cookies)
  status_code(link)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-6 mt-4'})
  sl = Tree("[green]> [yellow]Start bypass shortlinks")
  rprint(sl)
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      y=[i for i in i.text.strip().splitlines() if i][2]
      if 'clicks remaining' in y:
        y=y.split(' clicks remaining')[0].replace(' ','')
      if 'click remaining' in y:
        y=y.split(' click remaining')[0].replace(' ','')
      link=i.find('a',{'class':'card shadow text-decoration-none'})['href']
      re=int(y)
      for ulang in range(int(y)):
          get_links = curl.get('https://adhives.com' + link, headers=ua, cookies=cookies, allow_redirects=False)
          status_code(get_links)
          get_links=get_links.headers['Location']
          print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
          answer = bypass_link(get_links,modulesl,jumlah=[str(re),y])
          if answer == False:
            break
          if 'failed to bypass' in answer:pass
          else:
            animasi(detik=105)
            reward = curl.get(answer, headers=ua, cookies=cookies)
            status_code(reward)
            if 'Congratulations.' in reward.text:
                print(putih1+'├──'+hijau1+f'{hijau1} ✓ '+reward.text.split("message: '")[1].split("'")[0])
                re-=1
    except Exception as e:
      keluar(str(e))
      pass
  print(f'└──{merah1} ! {putih1} {hijau1}'+'No more shortlinks!')
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://earnsolana.xyz/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-sm-3'})
  akun=Tree("[gree] > [yellow]Account information")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start ptc"))
  ptc=curl.get('https://earnsolana.xyz/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'card-body'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button')["onclick"].split("window.location = '")[1].split("'")[0]
    print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end=end())
    visit=curl.get(link,headers=ua,cookies=cookies)
    status_code(visit)
    animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6Lem2pIjAAAAAESScDYn7ChChD9JS7pqa0d7TUUL',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    status_code(verify)
    if 'Good job!' in verify.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://earnsolana.xyz/links',headers=ua,cookies=cookies)
  #print(get_links.text)
  if 'links available' not in get_links.text:
    save_data(tele,'earnsolana')
    earnsolana(modulesl,banner,tele)
  fd=bs(get_links.text,'html.parser')
  link=fd.find_all('div',{'class':'card card-body text-center'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span',{'class':"badge badge-info"}).text.split('/')[0])
        re=jumlah
        for ulang in range(jumlah):
            url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
            status_code(url)
            url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),str(jumlah)])
            if answer==False:break
            if 'failed to bypass' in answer:
                pass
            else:
                animasi(detik=105)
                reward = curl.get(answer, headers=ua, cookies=cookies)
                status_code(reward)
                reward=reward.text
                if 'Good job!' in reward:
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    re-=1
                else:
                    print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
        keluar(str(e))
        pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    get_=curl.get('https://earnsolana.xyz/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=30)
    reward=curl.post('https://earnsolana.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    if 'Good job!' in reward.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://coinpay-faucet.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'coinpay-faucet')
    coinpay_faucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  akun=Tree("[green]> [yellow]Account information")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://coinpay-faucet.com/links',headers=ua,cookies=cookies)
  if 'links available' not in get_links.text:
    save_data(tele,'coinpay-faucet')
    coinpay_faucet(modulesl,banner,tele)
  fd=bs(get_links.text,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        re=jumlah
        for ulang in range(jumlah):
          url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
          status_code(url)
          url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
          answer = bypass_link(url,modulesl,jumlah=[str(re),str(jumlah)])
          if answer==False:break
          if 'failed to bypass' in answer:
              pass
          else:
              animasi(detik=105)
              reward = curl.get(answer, headers=ua, cookies=cookies)
              status_code(reward)
              reward=reward.text
              if 'Good job!' in reward:
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                  re-=1
              else:
                  print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
        keluar(str(e))
        pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    get_=curl.get('https://coinpay-faucet.com/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=60)
    reward=curl.post('https://coinpay-faucet.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    if 'Good job!' in reward.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
  exit()
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://freeclaimfaucet.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find('div',{'class':'mt-3 text-3xl font-semibold text-white'})
  akun=Tree("[green]> [yellow]Account information")
  akun.add('[green]> [yellow]Your Balance [white]: [yellow]'+info.text.strip())
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass ptc"))
  ptc=curl.get('https://freeclaimfaucet.com/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    status_code(visit)
    animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LcTwH0dAAAAADeD8cRAHIRmwKrS3JNbSh30QWFx',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    status_code(verify)
    if 'Good job!' in verify.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://freeclaimfaucet.com/links',headers=ua,cookies=cookies)
  status_code(get_links)
  if 'links available' not in get_links.text:
    save_data(tele,'freeclaimfaucet')
    freeclaimfaucet(modulesl,banner,tele)
  fd=bs(get_links.text,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        re=jumlah
        for ulang in range(jumlah):
            url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
            status_code(url)
            url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),str(jumlah)])
            if answer==False:break
            if 'failed to bypass' in answer:
                pass
            else:
                reward = curl.get(answer, headers=ua, cookies=cookies)
                status_code(reward)
                reward=reward.text
                if 'Good job!' in reward:
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    re-=1
                else:
                    print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
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
    
  }
  curl=requests.Session()
  dash=curl.get('http://tefaucet.online/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'tefaucet.online')
    tefaucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  akun=Tree("[gree] > [yellow]Account information")
  for info in info:
    akun.add('[gree] > [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass ptc"))
  ptc=curl.get('http://tefaucet.online/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data(tele,'tefaucet.online')
    tefaucet(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    status_code(visit)
    animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LfO_NgkAAAAALPup3qKwQtj3hQ1wUDP53ELBYxe',link)
    data=f"captcha=recaptchav2&recaptchav3=&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    status_code(verify)
    if 'Good job!' in verify.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
    keluar(str(e))
    pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('http://tefaucet.online/links',headers=ua,cookies=cookies)
  status_code(get_links)
  if 'links available' not in get_links.text:
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
        re=jumlah
        for ulang in range(jumlah):
            url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
            status_code(url)
            url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),str(jumlah)])
            if answer==False:break
            if 'failed to bypass' in answer:
                pass
            else:
                animasi(detik=105)
                reward = curl.get(answer, headers=ua, cookies=cookies)
                status_code(reward)
                reward=reward.text
                if 'Good job!' in reward:
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    re-=1
                else:
                    print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    get_=curl.get('http://tefaucet.online/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=60)
    reward=curl.post('http://tefaucet.online/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    if 'Good job!' in reward.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
     keluar(str(e))
     print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://faucetcrypto.net/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'faucetcrypto_net')
    faucetcrypto_net(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'d-flex d-lg-flex d-md-block align-items-center'})
  akun=Tree("[gree] > [yellow]Account information")
  for info in info:
    akun.add('[gree] > [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://faucetcrypto.net/links',headers=ua,cookies=cookies)
  status_code(get_links)
  get_links=get_links.text
  if 'links available' not in get_links:
    save_data(tele,'faucetcrypto_net')
    faucetcrypto_net(modulesl,banner,tele)
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        re=int(jumlah)
        for ulang in range(jumlah):
            ur = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
            status_code(ur)
            url=ur.text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah])
            if answer==False:break
            if 'failed to bypass' in answer:pass
            else:
                animasi(detik=105)
                reward = curl.get(answer, headers=ua, cookies=cookies)
                status_code(reward)
                reward=reward.text
                if 'links available' not in reward:
                  save_data(tele,'faucetcrypto_net')
                  faucetcrypto_net(modulesl,banner,tele)
                if 'Good job!' in reward:
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    re-=1
                else:
                    print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    get_=curl.get('https://faucetcrypto.net/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=60)
    reward=curl.post('https://faucetcrypto.net/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    if 'Good job!' in reward.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except:
     print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://faucetspeedbtc.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'faucetspeedbtc')
    faucetspeedbtc(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  akun=Tree("[gree] > [yellow]Account information")
  for info in info:
    akun.add('[gree] > [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://faucetspeedbtc.com/links',headers=ua,cookies=cookies)
  status_code(get_links)
  fd=bs(get_links.text,'html.parser')
  if 'Links' not in get_links.text:
    save_data(tele,'faucetspeedbtc')
    faucetspeedbtc(modulesl,banner,tele)
  link=fd.find_all('div',{'class':'col-md-6 col-xl-4'})
  for i in link:
    try:
        if 'h5' not in str(i):pass
        else:
          name = i.find('h5').text
          jumlah = int(i.find('span').text.split('/')[0])
          re=jumlah
          for ulang in range(jumlah):
              ur = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
              status_code(ur)
              url=ur.text.split('<script> location.href = "')[1].split('"; </script>')[0]
              answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah])
              if answer==False:break
              if 'failed to bypass' in answer:pass
              else:
                  animasi(detik=105)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  status_code(reward)
                  reward=reward.text
                  if 'Good job!' in reward:
                      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                      re-=1
                  else:
                      print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
      keluar(str(e))
      pass
    
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    get_=curl.get('https://faucetspeedbtc.com/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=60)
    reward=curl.post('https://faucetspeedbtc.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! 8 tokens has been added to your balance success')
   except:
     print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
     break
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://tikiearn.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'tikiearn')
    tikiearn(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('h5',{'class':'text-muted mb-0 font-size-15'})
  akun=Tree("[gree] > [yellow]Account information")
  akun.add('[gree] > [yellow]Balance [white]: [yellow]'+info[1].text.strip())
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start ptc"))
  ptc=curl.get('https://tikiearn.com/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data(tele,'tikiearn')
    tikiearn(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-3'})
  for ptc in ptc:
   try:
      name=ptc.find('h4').text.strip()
      link=ptc.find('button')["onclick"].split("window.location = '")[1].split("'")[0]
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
      visit=curl.get(link,headers=ua,cookies=cookies)
      status_code(visit)
      animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
      answer=modulesl.RecaptchaV2('6LcpH6omAAAAAPgjFK9i2npoqAvZLh-_L9M9t8Ds',link)
      answer1=modulesl.RecaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcdeZwkAAAAABfgNLd6v3Ew8Ak6Py1kVwZsJ5A_&co=aHR0cHM6Ly90aWtpZWFybi5jb206NDQz&hl=id&v=pCoGBhjs9s8EhFOHJFe8cqis&size=invisible&cb=dkc97yvnj2gs')
      csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
      token=bs(visit.text,'html.parser').find('input',{'name':'token'})['value']
      data=f"captcha=recaptchav2&recaptchav3={answer1}&g-recaptcha-response={answer}&csrf_token_name={csrf}&token={token}"
      verify=curl.post(link.replace('view','verify'),data=data,headers={"Host":"tikiearn.com","User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
      status_code(verify)
      if 'Good job!' in verify.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
        keluar(str(e))
        save_data(tele,'tikiearn')
        tikiearn(modulesl,banner,tele)
        pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://tikiearn.com/links',headers=ua,cookies=cookies)
  status_code(get_links)
  fd=bs(get_links.text,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text.strip()
        jumlah = int(i.find('span',{'class':'badge badge-info'}).text.split('/')[0])
        re=int(jumlah)
        for ulang in range(jumlah):
            url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
            status_code(url)
            url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah])
            if answer==False:break
            if 'failed to bypass' in answer:pass
            else:
                animasi(detik=105)
                reward = curl.get(answer, headers=ua, cookies=cookies)
                print(reward.url)
                print(reward.headers)
                status_code(reward)
                reward=reward.text
                if 'Good job!' in reward:
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    re-=1
                else:
                    print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://allfaucet.xyz/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'invoice-box'})
  akun=Tree("[green]> [yellow]Account information")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
 # exit()
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start ptc"))
  ptc=curl.get('https://allfaucet.xyz/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'Ads Available' not in ptc.text:
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
      name=ptc.find('h5',{'class':'card-title'}).text.strip()
      link=ptc.find('button')["onclick"].split("window.location = '")[1].split("'")[0]
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
      visit=curl.get(link,headers=ua,cookies=cookies)
      status_code(visit)
      animasi(detik=int(visit.text.split('let timer = ')[1].split(';')[0]))
      csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
      token=bs(visit.text,'html.parser').find('input',{'name':'token'})['value']
      answer=modulesl.RecaptchaV2('6Lcb3bkfAAAAAC1ZGV7QlVQyE7iyVr2jq6nvmvcN',link)
      data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}&token={token}"
      verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
      status_code(verify)
      if 'Good job!' in verify.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! '+verify.text.split("text: '")[1].split("',")[0])
   except Exception as e:
        keluar(str(e))
        save_data(tele,'allfaucet')
        allfaucet(modulesl,banner,tele)
        pass
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://allfaucet.xyz/links',headers=ua,cookies=cookies)
  status_code(get_links)
  if 'Links Available' not in get_links.text:
    save_data(tele,'allfaucet')
    allfaucet(modulesl,banner,tele)
  fd=bs(get_links.text,'html.parser')
  link=fd.find_all('div',{'class':'link-block'})
  for i in link:
    try:
        name = i.find('span',{'class':'link-name'}).text.strip()
        jumlah = int(i.find('span',{'class':'link-rmn'}).text.split('/')[0])
        re=int(jumlah)
        for _ in range(jumlah):
            csrf=fd.find('input',{'name':'csrf_token_name'})['value']
            token=fd.find('input',{'name':'token'})['value']
            data=f"csrf_token_name={csrf}&token={token}"
            url = curl.post(i.find('form')["action"], headers={'content-type':'application/x-www-form-urlencoded'}, data=data,cookies=cookies, allow_redirects=False)
            status_code(url)
            url=url.text.split('location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah])
            if answer==False:break
            if 'failed to bypass' in answer:pass
            else:
                animasi(detik=105)
                reward = curl.get(answer, headers=ua, cookies=cookies)
                status_code(reward)
                reward=reward.text
                if 'Good job!' in reward:
                    reward_msg = reward.split("text: '")[1].split("',")[0]
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! '+reward_msg)
                    re-=1
                else:
                    print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
            get_links=curl.get('https://allfaucet.xyz/links',headers=ua,cookies=cookies)
            status_code(get_links)
            fd=bs(get_links.text,'html.parser')
    except Exception as e:
      keluar(str(e))
      pass
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    get_=curl.get('https://allfaucet.xyz/auto',headers=ua,cookies=cookies)
    status_code(get_)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    animasi(detik=10)
    reward=curl.post('https://allfaucet.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    status_code(reward)
    if 'Good job!' in reward.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! '+reward.text.split("text: '")[1].split("',")[0])
   except Exception as e:
     keluar(str(e))
     print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
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
    
  }
  curl=requests.Session()
  try:
    dash=curl.get('https://btcadspace.com/account',headers=ua,cookies=cookies)
    status_code(dash)
    if 'Main Balance' not in dash.text:
      save_data(tele,'btcadspace')
      btcadspace(modulesl,banner,tele)
  except Exception as e:
    save_data(tele,'btcadspace')
    btcadspace(modulesl,banner,tele)
  fd=bs(dash.text,'html.parser').find_all('div',{'class':'col-md-4 stretch-card grid-margin mt-3'})
  akun=Tree("[green]> [yellow]Account information")
  for i in fd:
    akun.add('[green]> [yellow]'+i.text.strip().replace('    ','').splitlines()[0]+' [white]: [yellow]'+i.text.strip().replace('    ','').splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Bypass shortlinks"))
  get_links=curl.get('https://btcadspace.com/shortlinks',headers=ua, cookies=cookies)
  status_code(get_links)
  gas=bs(get_links.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  for i in gas:
      info = [i for i in i.text.strip().replace('            ', '').splitlines() if i]
      jumlah = info[2].split(' clicks remaining')[0]
      re=int(jumlah)
      for jun in range(int(jumlah)):
        try:
          url = curl.get('https://btcadspace.com' + i.find('a', {'class': 'card shadow text-decoration-none'})['href'], headers=ua, cookies=cookies, allow_redirects=False)
          status_code(url)
          url=url.headers['location']
          answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah])
          if answer==False:break
          if 'failed to bypass' in answer:pass
          else:
              animasi(detik=105)
              get_reward = curl.get(answer, headers=ua, cookies=cookies)
              status_code(get_reward)
              print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("message: '")[1].split("'")[0])
              re-=1
        except Exception as e:
          keluar(str(e))
          pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
#fix dulu coy
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
    akun=Tree("[green]> [yellow]Account information")
    get_user=json.loads(curl.get('https://api.nokofaucet.com/api/auth/me',headers=ua).text)
    _id1=get_user["_id"]
    akun.add("[green]> [yellow]Username [white]: [yellow]"+get_user["username"]+' [white]| [yellow]Email [white]: [yellow]'+get_user["email"])
    akun.add("[green]]> [yellow]]Balance [white]: [yellow]"+str(get_user["balance"])+' [white]| [yellow]Energy [white]: [yellow]'+str(get_user["energy"]))
  except Exception as e:
    save_datan(tele,'nokofaucet')
    nokofaucet(modulesl,banner,tele)
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
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
                    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+json.loads(reward.text)["message"]+'               ')
        except Exception as e:
            keluar(str(e))
            pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlink!')
  exit()
def paid_family(url,sitkey,email,modulesl,tele):
  curl=requests.Session()
  login=curl.get(url,headers={"Host":urlparse(url).netloc,"User-Agent":"XYZ/3.0"})
  status_code(login)
  frc=bs(login.text,'html.parser').find('input',{'name':'frsc'})['value']
  answer=modulesl.RecaptchaV2(key=sitkey,url=url)
  data=f"frsc={frc}&guest_email={email}&captcha=recaptchaV2&g-recaptcha-response={answer}&Guest_Login=Guest_Login"
  login=curl.post(url,headers={"Host":urlparse(url).netloc,"User-Agent":"XYZ/3.0","content-type":"application/x-www-form-urlencoded"},data=data)
  status_code(login)
  host=urlparse(url).netloc
  if 'user' in login.url:
    rprint(Tree(f'[green] > [white][ [green]√ [white]][green] Login Success!!                                  '))
    link=bs(login.text,'html.parser').find_all('tr')
    del link[0]
    for links in link:
     try:
      li=links.find('a')['href']
      lis= [element.strip() for element in links.text.strip().splitlines()]
      name=lis[0]
      jumlah=int(lis[9].split('/')[0])
      re=jumlah
      for ulang in range(jumlah):
            url = curl.get(li,headers={"Host":host,"User-Agent":"XYZ/3.0"},allow_redirects=False).text.split('<script>location.href = "')[1].split('";</script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),str(jumlah)])
            if answer==False:break
            if 'failed to bypass' in answer:pass
            else:
                animasi(detik=105)
                reward = curl.get(answer,headers={"Host":host,"User-Agent":"XYZ/3.0"})
                if 'Well done :)' in reward.text:
                  sukses=bs(reward.text,'html.parser').find('div',{'class':'alert alert-success d-flex'}).text
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+sukses)
                  re-=1
                if 'Error!!' in reward.text:
                  sukses=bs(reward.text,'html.parser').find('div',{'class':'alert alert-danger d-flex'}).text
                  print(putih1+'├──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+sukses)
                  re-=1
     except Exception as e:
       keluar(str(e))
       pass
#fix dulu coy
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
  print(hijau1+"> "+kuning1+"Start bypass liteearn.com")
  paid_family('https://liteearn.com/',"6Lejju8UAAAAAMCxObwhQJliWyTUXwEcUc43KOiQ",cookies,modulesl,tele)
  print(hijau1+"> "+kuning1+"Start bypass paidtomoney.com")
  paid_family('https://paidtomoney.com/',"6LfZswEVAAAAAHXORtki0EFzDZZIV02Wo0krcxRo",cookies,modulesl,tele)
#--------------
def bitscript_family(url,modulesl,banner,key_links,tele,bal=None):
  host=urlparse(url).netloc
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper())
  data_control(host)
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele,host)
    bitscript_family(url,modulesl,banner,key_links,tele,bal)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  dahs=curl.get(url+'account',headers=ua,cookies=cookies)
  status_code(dahs)
  if 'Balance' not in dahs.text:
    save_data(tele,host)
    bitscript_family(url,modulesl,banner,key_links,tele,bal)
  if bal != None:
    fd=bs(dahs.text,'html.parser').find_all('div',{'class':bal})
    akun=Tree("[green]> [yellow]Account information")
    akun.add(hijau1+'[green]> [yellow]'+fd[0].text.strip().splitlines()[1]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[0])
    akun.add(hijau1+'[green]> [yellow]'+fd[1].text.strip().splitlines()[1]+' [white]: [yellow]'+fd[1].text.strip().splitlines()[0])
  else:
    fd=bs(dahs.text,'html.parser').find_all('table',{'class':'table table-striped'})
    akun=Tree("[green]> [yellow]Account information")
    akun.add(hijau1+'[green]> [yellow]'+fd[0].text.strip().splitlines()[0]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[1])
    akun.add(hijau1+'[green]> [yellow]'+fd[0].text.strip().splitlines()[4]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[5])
  rprint(akun)
  link=curl.get(url+'shortlinks',headers=ua,cookies=cookies)
  status_code(link)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-lg-4 mt-4'})
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      y=[i for i in i.text.strip().splitlines() if i][2]
      if 'clicks remaining' in y:
        y=y.split(' clicks remaining')[0].replace(' ','')
      if 'click remaining' in y:
        y=y.split(' click remaining')[0].replace(' ','')
      link=i.find('a',{'class':key_links})['href']
      re=int(y)
      for ulang in range(int(y)):
          get_links = curl.get(url+ link, headers=ua, cookies=cookies, allow_redirects=False)
          status_code(get_links)
          get_links=get_links.headers['Location']
          print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end=end())
          answer = bypass_link(get_links,modulesl,jumlah=[str(re),str(y)])
          if answer==False:break
          if 'failed to bypass' in answer:pass
          else:
            animasi(detik=105)
            reward = curl.get(answer, headers=ua, cookies=cookies)
            status_code(reward)
            if 'Congratulations.' in reward.text:
              _1 = reward.text.split("message: '")[1].split("'")[0]
              print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+_1)
              re-=1
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  exit()
def cryptohits(modulesl,banner,tele=None):
  bitscript_family("https://cryptohits.io/",modulesl,banner,"card shadow text-decoration-none",tele,"balance-left")
def earnfree_cash(modulesl,banner,tele=None):
  bitscript_family('https://earnfree.cash/',modulesl,banner,"card shadow text-decoration-none",tele)
  exit()
def paidbucks(modulesl,banner,tele=None):
  bitscript_family('https://paidbucks.xyz/',modulesl,banner,"card shadow text-decoration-none",tele)
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
    
  }
  curl=requests.Session()
  try:
    dahs=curl.get(url+'/account',headers=ua,cookies=cookies)
    status_code(dahs)
    if 'Balance' not in dahs.text:
      save_data(tele,host)
      clickscoin(modulesl,banner,tele)
  except Exception as e:
      save_data(tele,host)
      clickscoin(modulesl,banner,tele)
  fd=bs(dahs.text,'html.parser').find_all('div',{'class':'info-area'})
  akun=Tree("[gree] > [yellow]Account information")
  akun.add('[gree] > [yellow]'+fd[0].text.strip().splitlines()[2]+' [white]: [yellow]'+fd[0].text.strip().splitlines()[0])
  link=curl.get("https://clickscoin.com/shortlinks",headers=ua,cookies=cookies)
  status_code(link)
 # print(link.text)
  gt=bs(link.text,'html.parser').find_all('div',{'class':'col-xl-3 col-md-6'})
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  for i in gt:
    try:
      name = i.text.strip().splitlines()[0]
      y=[i for i in i.text.strip().splitlines() if i]
      link=i.find('a')['href']
      re=int(y[3])
      for ulang in range(int(y[3])):
          get_links = curl.get("https://clickscoin.com"+ link, headers=ua, cookies=cookies, allow_redirects=False)
          status_code(get_links)
          get_links=get_links.headers['Location']
          answer = bypass_link(get_links,modulesl,jumlah=[str(re),y[3]])
          if answer == False:
            break
          if 'failed to bypass' in answer:
              pass
          else:
            animasi(detik=105)
            reward = curl.get(answer, headers=ua, cookies=cookies)
            status_code(reward)
            if 'Congratulations.' in reward.text:
              _1 = reward.text.split("message: '")[1].split("'")[0]
              print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+_1)
              re-=1
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
def vie_script(modulesl,banner,url,key_re,ptc=False,short=False,faucet=False,auto=False):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse(url).netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele=None,name=host)
    vie_script(modulesl,banner,url,key_re,ptc, short,faucet,auto)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  dash=curl.get(f'https://{host}/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele=None,name=host)
    vie_script(modulesl,banner,url,key_re,ptc, short,faucet,auto)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  akun=Tree("[green]> [yellow]Account information")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  if ptc == True:
    rprint(Tree("[green]> [yellow]Start ptc"))
    ptc=curl.get(f'https://{host}/ptc',headers=ua,cookies=cookies)
    status_code(ptc)
    if 'ads available' not in ptc.text:
      save_data(tele=None,name=host)
      vie_script(modulesl,banner,url,key_re,ptc, short,faucet,auto)
    ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
    for ptc in ptc:
     try:
      name=ptc.find('h5',{'class':'card-title'}).text
      link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
      visit=curl.get(link,headers=ua,cookies=cookies)
      status_code(visit)
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+parser(name),end=end())
      animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
      bs4 = BeautifulSoup(visit.text, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      data["captcha"]="recaptchav2"
      data["g-recaptcha-response"]=modulesl.RecaptchaV2(key_re,visit.url)
      verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
      status_code(verify)
      if 'Good job!' in verify.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
     except Exception as e:
        keluar(str(e))
        pass
    print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  if short == True:
    rprint(Tree("[green]> [yellow]Start bypass shortlinks"))
    get_links=curl.get(f'https://{host}/links',headers=ua,cookies=cookies)
    status_code(get_links)
    if 'links available' not in get_links.text:
      save_data(tele=None,name=host)
      vie_script(modulesl,banner,url,key_re,ptc, short,faucet,auto)
    if 'pre_verify' in get_links.url:
      print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}maaf shortlinks memiliki anti bot saat ini belum ada metode bypass untuk anti bot')
    else:
      fd=bs(get_links.text,'html.parser')
      link=fd.find_all('div',{'class':'col-lg-3'})
      for i in link:
        try:
            name = i.find('h4').text
            jumlah = i.find('span').text.split('/')
            re=int(jumlah[0])
            for ulang in range(int(jumlah[0])):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
                status_code(url)
                url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah[1]])
                if answer==False:
                  break
                if 'failed to bypass' in answer:
                    pass
                else:
                    animasi(detik=105)
                    reward = curl.get(answer, headers=ua, cookies=cookies)
                    status_code(reward)
                    if 'Good job!' in reward.text:
                        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
                re-=1
        except Exception as e:
            keluar(str(e))
            pass
      print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  if auto == True:
    rprint(Tree("[green]> [yellow]Start auto faucet"))
    while True:
     try:
      get_=curl.get(f'https://{host}/auto',headers=ua,cookies=cookies)
      status_code(get_)
      bs4 = BeautifulSoup(get_.text, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      animasi(detik=int(get_.text.split('let timer = ')[1].split(',')[0]))
      reward=curl.post(f'https://{host}/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data=data)
      status_code(reward)
      if 'Good job!' in reward.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
     except Exception as e:
       print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy!')
       break
       #exit()
  if faucet == True:
    rprint(Tree("[green]> [yellow]Start faucet"))
    faucet=curl.get(f'https://{host}/faucet',headers=ua,cookies=cookies)
    status_code(faucet)
    jumlah=bs(faucet.text,'html.parser').find_all('p',{'class':'lh-1 mb-1 font-weight-bold'})
    if 'Please click on the Anti-Bot links in the following order' in faucet.text:
      print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}maaf faucet memiliki anti bot saat ini belum ada metode bypass untuk anti bot')
      exit()
    jum=jumlah[len(jumlah)-1].text.split('/')
    re=int(jum[0])
    for i in range(int(jum[0])):
      faucet=curl.get(f'https://{host}/faucet',headers=ua,cookies=cookies)
      status_code(faucet)
      bs4 = BeautifulSoup(faucet.text, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      data["captcha"]="recaptchav2"
      data["g-recaptcha-response"]=modulesl.RecaptchaV2(key_re,faucet.url)
      faucet=curl.post(f'https://{host}/faucet/verify',data=data,headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},cookies=cookies)
      status_code(faucet)
      if 'Good job!' in faucet.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{str(re)}/{jum[1]}{hijau1} √ {putih1}] {hijau1}'+faucet.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
      re-=1
      animasi(menit=int(jumlah[0].text))
      faucet=curl.get(f'https://{host}/faucet',headers=ua,cookies=cookies)
      status_code(faucet)
      if 'firewall' in faucet.url:
        info=bs(faucet.text,'html.parser')
        csrf=info.find('input',{'name':'csrf_token_name'})['value']
        answer=modulesl.RecaptchaV2(key_re,faucet.url)
        data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
        gas=curl.post(f"https://{host}/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
        status_code(gas)
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
  exit()
def cryptoscop(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://cryptoscoop.online/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele=None,name=host)
    cryptoscop(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  hd=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
  ua_p=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","application/x-www-form-urlencoded")
  curl=requests.Session()
  dash=curl.get(f'https://cryptoscoop.online/dashboard',headers=hd,cookies=cookies)
  status_code(dash)
  if 'Coin Balance' not in dash.text:
    save_data(tele=None,name=host)
    cryptoscop(modulesl,banner,tele)
  info=bs(dash.text,"html.parser").find("div",{"class":"col-8 p-4"}).text.strip().splitlines()
  akun=Tree("[gree] > [yellow]Account information")
  akun.add("[gree] > [yellow]"+info[1]+' [white]: [yellow]'+info[0])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Ptc"))
  ptc=curl.get(f'https://cryptoscoop.online/ptc',headers=hd,cookies=cookies)
  status_code(ptc)
  ptc=bs(ptc.text,"html.parser").find_all("div",{"class":"col-12 col-lg-3 col-xl-3"})
  for ptc in ptc:
   try:
    name=parser(ptc.find("p",{"class":"mb-4 text-dark font-size-14"}).text)
    url=ptc.find("a")["onclick"].split("window.location = '")[1].split("'")[0]
    view=curl.get(url,headers=hd,cookies=cookies)
    status_code(view)
    print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end=' '*20+'\r')
    animasi(detik=int(view.text.split("var timer = ")[1].split(";")[0]))
    csrf=bs(view.text,"html.parser").find("input",{"name":"csrf_token_name"})["value"]
    answer=modulesl.RecaptchaV2("6LcwWM8mAAAAAG477PUv-DUINczEel-bejrD2iYH",url)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    reward=curl.post(url.replace("view","verify"),headers=ua_p,data=data,cookies=cookies)
    status_code(reward)
    if 'Good job!' in reward.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
   except Exception as e:
     keluar(str(e))
     pass
   # exit()
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  rprint(Tree("[gree] > [yellow]Shortlinks"))
  sl=curl.get(f'https://cryptoscoop.online/links',headers=hd,cookies=cookies)
  status_code(sl)
  sl=bs(sl.text,"html.parser").find_all("div",{"class":"card-body"})
  del sl[:7]
  for sl in sl:
   try:
    url=sl.find("a")["href"]
    jumlah=sl.find("h5").text.strip().split('/')
    name=sl.find("h4").text
    re=int(jumlah[0])
    for juml in range(int(jumlah[0])):
      verify=curl.get(url,headers=hd,cookies=cookies)
      status_code(verify)
      csrf=bs(verify.text,"html.parser").find("input",{"name":"csrf_token_name"})["value"]
      answer=modulesl.RecaptchaV2("6LcwWM8mAAAAAG477PUv-DUINczEel-bejrD2iYH",url)
      data=f"csrf_token_name={csrf}&captcha=recaptchav2&g-recaptcha-response={answer}"
      gt_links=curl.post(url.replace("pre_verify","go"),headers=ua_p,cookies=cookies,data=data,allow_redirects=False)
      status_code(gt_links)
      gt_links=gt_links.text.split('<script> location.href = "')[1].split('"; </script>')[0]
      answer=bypass_link(gt_links,modulesl,jumlah=[str(re),jumlah[0]])
      if answer==False:
        break
      if 'failed to bypass' in answer:
        pass
      else:
        animasi(detik=105)
        reward=curl.get(answer,headers=hd,cookies=cookies)
        status_code(reward)
        if 'Good job!' in reward.text:
          print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
      re-=1
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Faucet"))
  while True:
   try:
    faucet=curl.get(f'https://cryptoscoop.online/bonusclaim',headers=hd,cookies=cookies)
    status_code(faucet)
    csrf=bs(faucet.text,"html.parser").find("input",{"name":"csrf_token_name"})["value"]
    answer=modulesl.RecaptchaV2("6LcwWM8mAAAAAG477PUv-DUINczEel-bejrD2iYH",faucet.url)
    data=f"csrf_token_name={csrf}&captcha=recaptchav2&g-recaptcha-response={answer}"
    faucet=curl.post(f'https://cryptoscoop.online/bonusclaim/verify',headers=ua_p,cookies=cookies,data=data)
    status_code(faucet)
    if 'Good job!' in faucet.text:
      print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+faucet.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
      animasi(menit=5)
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more energy!')
def earnrub_pw(modulesl,banner,tele=None):
  vie_script(modulesl,banner,url="https://earnrub.pw/",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=True,short=True,faucet=True,auto=True)
def instanfaucet_xyz(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://insfaucet.xyz/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele=None,name=host)
    instanfaucet_xyz(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  hd=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
  ua_p=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","application/x-www-form-urlencoded")
  curl=requests.Session()
  dash=curl.get("https://insfaucet.xyz/dashboard",headers=hd,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(tele=None,name=host)
    instanfaucet_xyz(modulesl,banner,tele)
  get_info=bs(dash.text,"html.parser").find_all('div',{"class":"col-sm-4 layout-spacing"})
  akun=Tree("[green]> [yellow]Account information")
  for info in get_info:
    akun.add("[green]> [yellow]"+info.text.strip().replace("\n"," : "))
  rprint(akun)
  rprint(Tree("[green]> [yellow]Shortlinks"))
  sl=curl.get(f'https://insfaucet.xyz/links',headers=hd,cookies=cookies)
  status_code(sl)
  sl=bs(sl.text,"html.parser").find_all("div",{"class":"card card-body text-center"})
  for sl in sl:
   try:
    url=sl.find("a")["href"]
    jumlah=sl.find("span",{"class":"badge span-warning text-warning text-center"}).text.strip().split('/')
    re=int(jumlah[0])
    name=sl.find("h4").text
    for juml in range(int(jumlah[0])):
      gt_links=curl.get(url,headers=hd,cookies=cookies,allow_redirects=False)
      status_code(gt_links)
      gt_links=gt_links.text.split('<script> location.href = "')[1].split('"; </script>')[0]
      answer=bypass_link(gt_links,modulesl,jumlah=[str(re),jumlah[1]])
      if answer==False:
        break
      if 'failed to bypass' in answer:
        pass
      else:
        animasi(detik=105)
        reward=curl.get(answer,headers=hd,cookies=cookies)
        status_code(reward)
        if 'Good job!' in reward.text:
          print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
          re-=1
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[green]> [yellow]Start auto faucet"))
  while True:
     try:
      get_=curl.get(f'https://{host}/auto',headers=hd,cookies=cookies)
      status_code(get_)
      token=bs(get_.text,"html.parser").find("input",{"name":"token"})["value"]
      animasi(detik=int(get_.text.split('let timer = ')[1].split(',')[0]))
      reward=curl.post(f'https://{host}/auto/verify',headers=ua_p,cookies=cookies,data="token="+token)
      status_code(reward)
      if 'Good job!' in reward.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
     except Exception as e:
       print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
       exit()
def eurofaucet_de(modulesl,banner,tele=None):
  vie_script(modulesl,banner,url="https://eurofaucet.de/",key_re="6Lcza1QmAAAAAInStIpZuJYEOm-89v4zKNzglgU9",ptc=True,short=True,faucet=True,auto=True)
def james_trussy(modulesl,banner,tele=None):
  vie_script(modulesl,banner,"https://james-trussy.com/","6Ler3E4kAAAAABUDc4UE9UWO7k_n2JydShddSpCO",ptc=False,short=True,faucet=False,auto=True)
def coinsmash(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("COINSMASH")
  data_control('coinsmash')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/coinsmash/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('coinsmash')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://coinsmash.xyz/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://coinsmash.xyz/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
          with open('cache/coinsmash/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://coinsmash.xyz/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
      return answer
  cookies, ugentmu = load_data('coinsmash')
  if not os.path.exists("data/coinsmash/coinsmash.json"):
    save_data(tele,'coinsmash')
    coinsmash(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://coinsmash.xyz/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'coinsmash')
    coinsmash(modulesl,banner,tele)
  try:
    akun=Tree("[green] > [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,'coinsmash')
    coinsmash(modulesl,banner,tele)
  def balance():
    get_sl=curl.get('https://coinsmash.xyz/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_sl=curl.get('https://coinsmash.xyz/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  del gt_s[0]
  del gt_s[len(gt_s)-1]
  sl=Tree("[green]> [yellow]Start Bypassing Shortlinks")
  rprint(sl)
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
      re=jumlah
      for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
          get_sl = curl.get('https://coinsmash.xyz/shortlinks.html', headers=ua, cookies=cookies)
          status_code(get_sl)
          token = get_sl.text.split("var token = '")[1].split("';")[0]
          status = True
          while(status==True):
              da = id["onclick"].split("goShortlink('")[1].split("');")[0]
              gt_lk = curl.post('https://coinsmash.xyz/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies)
              status_code(gt_lk)
              get_lk=json.loads(gt_lk.text)
              if get_lk["status"] == 200:
                  answer = bypass_link(get_lk['shortlink'],modulesl,jumlah=[str(re),str(jumlah)])
                  if answer==False:break
                  elif 'failed to bypass' in answer:pass
                  else:
                      try:
                          get_sl = curl.get(answer, headers=ua, cookies=cookies)
                          status_code(get_sl)
                          sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
                          re-=1
                      except:
                          print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"invalid keys")
                  break
              elif get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
              else:
                mes=bs(get_lk["message"],'html.parser').text
                print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+mes)
                break
   except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  faucet=Tree("[green] > [yellow]Bypass faucet")
  rprint(faucet)
  while True:
    get_sl=curl.get('https://coinsmash.xyz/',headers=ua,cookies=cookies)
    status_code(get_sl)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LcqrGcjAAAAABdweI_Bxc7sHIJq5qGrgGKP78Hb',get_sl.url)
    gt=curl.post('https://coinsmash.xyz/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies)
    status_code(gt)
    g=json.loads(gt.text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
def earn_crypto(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("EARN_CRYPTO")
  data_control('earn_crypto')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/earn_crypto/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('earn_crypto')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://earn-crypto.co/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://earn-crypto.co/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
          with open('cache/earn_crypto/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://earn-crypto.co/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
      return answer
  cookies, ugentmu = load_data('earn_crypto')
  if not os.path.exists("data/earn_crypto/earn_crypto.json"):
    save_data(tele,'earn_crypto')
    earn_crypto(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://earn-crypto.co/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'earn_crypto')
    earn_crypto(modulesl,banner,tele)
  try:
    akun=Tree("[green] > [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,'earn_crypto')
    earn_crypto(modulesl,banner,tele)
  pct=Tree("[gree] > [yellow]Start working on ptc")
  rprint(pct)
  get_ptc=curl.get('https://earn-crypto.co/ptc.html',headers=ua,cookies=cookies)
  status_code(get_ptc)
  def balance():
    get_sl=curl.get('https://earn-crypto.co/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-primary btn-sm w-100 mt-1'})
  for _id in get_id:
    try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://earn-crypto.co/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      status_code(get_reward)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=curl.post('https://earn-crypto.co/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies)
      status_code(reward)
      if json.loads(reward.text)["status"] == 200:
        gas=bs(json.loads(reward.text)["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
    except Exception as e:
      keluar(e)
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://earn-crypto.co/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  sl=Tree("[green]> [yellow]Start Bypassing Shortlinks")
  rprint(sl)
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle text-center'}).text
    id=i.find('button',{'class':'btn btn-primary btn-sm'})
    if None == id:
      pass
    else:
      jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
      re=jumlah
      for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
          get_sl = curl.get('https://earn-crypto.co/shortlinks.html', headers=ua, cookies=cookies)
          status_code(get_sl)
          token = get_sl.text.split("var token = '")[1].split("';")[0]
          status = True
          while(status==True):
              da = id["onclick"].split("goShortlink('")[1].split("');")[0]
              gt_lk = curl.post('https://earn-crypto.co/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies)
              status_code(gt_lk)
              get_lk=json.loads(gt_lk.text)
              if get_lk["status"] == 200:
                  answer = bypass_link(get_lk['shortlink'],modulesl,jumlah=[str(re),str(jumlah)])
                  if answer==False:break
                  elif 'failed to bypass' in answer:pass
                  else:
                      try:
                          get_sl = curl.get(answer, headers=ua, cookies=cookies)
                          status_code(get_sl)
                          sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
                          re-=1
                      except:
                          print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"invalid keys")
                  break
              elif get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
              else:
                mes=bs(get_lk["message"],'html.parser').text
                print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+mes)
                break
                  
   except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  faucet=Tree("[green] > [yellow]Bypass faucet")
  rprint(faucet)
  while True:
    get_sl=curl.get('https://earn-crypto.co/',headers=ua,cookies=cookies)
    status_code(get_sl)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6Lc9J-khAAAAAD5unMlGLyhInd7zy4QqG-DOHeTm',get_sl.url)
    gt=curl.post('https://earn-crypto.co/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies)
    status_code(gt)
    g=json.loads(gt.text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(3600)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
def earnbits(modulesl,banner,tele=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("EARNBITS")
  data_control('earnbits')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/earnbits/{i}.jpg')
          file_sizes.append(file_size)
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
      cache_control('earnbits')
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post('https://earnbits.io/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
          'sec-ch-ua-platform': '"Android"',
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
      }
      
      file_names = []
      for i in range(5):
          file_name = f'{i}.jpg'
          file_names.append(file_name)
          gt_im = requests.get(f'https://earnbits.io/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
          with open('cache/earnbits/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek()
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post('https://earnbits.io/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
      return answer
  cookies, ugentmu = load_data('earnbits')
  if not os.path.exists("data/earnbits/earnbits.json"):
    save_data(tele,'earnbits')
    earnbits(modulesl,banner,tele)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  get_sl=curl.get('https://earnbits.io/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  if 'Account Balance' not in get_sl.text:
    save_data(tele,'earnbits')
    earnbits(modulesl,banner,tele)
  try:
    akun=Tree("[green] > [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data(tele,'earnbits')
    earnbits(modulesl,banner,tele)
  pct=Tree("[gree] > [yellow]Start working on ptc")
  rprint(pct)
  get_ptc=curl.get('https://earnbits.io/ptc.html',headers=ua,cookies=cookies)
  status_code(get_ptc)
  def balance():
    get_sl=curl.get('https://earnbits.io/ptc.html',headers=ua,cookies=cookies)
    status_code(get_sl)
    return bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})[0].text.strip()
  get_id=bs(get_ptc.text,'html.parser').find_all('button',{'class':'btn btn-success btn-sm w-100 mt-1'})
  del get_id[0]
  for _id in get_id:
    try:
     sesi=False
     while(sesi==False):
      _i=_id["onclick"].split("opensite('")[1].split("','")[0]
      key=get_ptc.text.split("var hash_key = '")[1].split("';")[0]
      get_reward=curl.get(f'https://earnbits.io/surf.php?sid={_i}&key={key}',headers=ua,cookies=cookies)
      status_code(get_reward)
      token1=get_reward.text.split("var token = '")[1].split("';")[0]
      secon=get_reward.text.split("var secs = ")[1].split(";")[0]
      for i in tqdm (range (int(secon)), leave=False,desc=hijau1+"visit > "+_id["onclick"].split("','")[1].split("');")[0]):
              time.sleep(1)
              pass
      answer=get_answer()
      reward=curl.post('https://earnbits.io/system/ajax.php',data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}",headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},cookies=cookies)
      status_code(reward)
      if json.loads(reward.text)["status"] == 200:
        gas=bs(json.loads(reward.text)["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
        print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
        print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
        sesi=True
    except Exception as e:
      keluar(e)
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all ptc ;)")
  get_sl=curl.get('https://earnbits.io/shortlinks.html',headers=ua,cookies=cookies)
  status_code(get_sl)
  token=get_sl.text.split("var token = '")[1].split("';")[0]
  gt_s=bs(get_sl.text,'html.parser').find_all('tr')
  sl=Tree("[green]> [yellow]Start Bypassing Shortlinks")
  rprint(sl)
  for i in gt_s:
   try:
    name=i.find('td',{'class':'align-middle'}).text
    id=i.find('button',{'class':'btn btn-success btn-sm'})
    if None == id:
      pass
    else:
      jumlah=int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])
      re=jumlah
      for i in range(int(i.find_all('b', {'class': 'badge badge-dark'})[1].text.split('/')[0])):
          get_sl = curl.get('https://earnbits.io/shortlinks.html', headers=ua, cookies=cookies)
          status_code(get_sl)
          token = get_sl.text.split("var token = '")[1].split("';")[0]
          status = True
          while(status==True):
              da = id["onclick"].split("goShortlink('")[1].split("');")[0]
              gt_lk = curl.post('https://earnbits.io/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf={get_answer()}", allow_redirects=False, cookies=cookies)
              status_code(gt_lk)
              get_lk=json.loads(gt_lk.text)
              if get_lk["status"] == 200:
                  answer = bypass_link(get_lk['shortlink'],modulesl,jumlah=[str(re),str(jumlah)])
                  if answer==False:break
                  elif 'failed to bypass' in answer:pass
                  else:
                      try:
                          get_sl = curl.get(answer, headers=ua, cookies=cookies)
                          status_code(get_sl)
                          sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+sukses)
                          print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
                          re-=1
                      except:
                          print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"invalid keys")
                  break
              elif get_lk['status'] == 600:
                  print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+"Captcha wrong",end="\r")
              else:
                mes=bs(get_lk["message"],'html.parser').text
                print(putih1+'├──'+hijau1+' [ '+merah1+'x'+hijau1+' ] '+mes)
                break
                  
   except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+' [ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  faucet=Tree("[green] > [yellow]Bypass faucet")
  rprint(faucet)
  while True:
    get_sl=curl.get('https://earnbits.io/',headers=ua,cookies=cookies)
    status_code(get_sl)
    if 'You can claim again in' in get_sl.text:
      tim=int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0])*60
      for i in tqdm (range (int(tim)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
            pass
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=modulesl.RecaptchaV2('6LcJO3YnAAAAAODSQdQry4sVyosh5BT6YuYXQfW4',get_sl.url)
    gt=curl.post('https://earnbits.io/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies)
    status_code(gt)
    g=json.loads(gt.text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(putih1+'├──'+hijau1+' [ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(putih1+'├──'+hijau1+' [ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="└── Please wait..."):
            time.sleep(1)
def timps_co(modulesl,banner,tele=None):
  def save_data(tele,name,inp=False):
    if inp!=False:
      user_agent=inp
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
            data = json.load(file)
            cookies = data.get('auth')
            user_agent = data.get('data')
            if tele == True:
              send_signal(1111,f"`{name.upper()}` mengirim request input, kirim cookies dan User-Agent anda pisahkan dengan dolar($) contoh : `/cookies nama_sesi csrf=xxx$Mozillaxxx`")
              mes=receive_signal(1111)
              #print(mes)
              if name.upper() in mes:
                cookies,user_agent=mes.split(name.upper()+' ')[1].split('$')
            else:
              #  print(f'{putih1}[{kuning1} ~ {putih1}] {hijau1}User-Agent sudah ada tetap update User-Agent? jika User-Agent sudah di update tetap cf gunakan User-Agent : XYZ/3.0')
             #   jawab = input('y/n : '.lower())
           #     if jawab == 'y':
               #   user_agent = input(hijau1 + 'Masukkan auth mu > ')
               if inp == False:
                cookies = input(hijau1 + 'Masukkan data mu > ')
            data = {
            #    'auth': cookies,
                'data': user_agent
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
           #   cookies = input(hijau1 + 'Masukkan auth mu > ')
            if inp ==False:
              user_agent = input(hijau1 + 'Masukkan data mu > ')
          data = {
              'data': user_agent
          }
          with open(f'data/{name}/{name}.json', 'w') as file:
              json.dump(data, file)
          return user_agent
  def load_data(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          user_agent = data['data']
          return user_agent
      except FileNotFoundError:
          return None, None
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://timpsco.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  data = load_data(host)
  refreshToken=data
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele=None,name=host)
    timps_co(modulesl,banner,tele)
  curl=requests.Session()
  auth=json.loads(data)["variables"]["input"]["token"]
  get_user={"operationName":"getUser","variables":{},"query":"query getUser {\n  getUser {\n    id\n    balance\n    credits\n    username\n    email\n    admin\n    status\n    createAt\n    log\n    xp\n    level\n    next_level\n    bonus_level\n    address_fp\n    bonus_loyalty\n    total_earn\n    statistics_earn {\n      id\n      clicks\n      total\n      __typename\n    }\n    __typename\n  }\n}\n"}
  ptc_wall={"operationName":"getAdsPtcWall","variables":{"offset":0,"limit":50},"query":"query getAdsPtcWall($offset: Int, $limit: Int) {\n  getAdsPtcWall(offset: $offset, limit: $limit) {\n    Ads {\n      id\n      title\n      description\n      url\n      duration\n      reward\n      __typename\n    }\n    total\n    __typename\n  }\n}\n"}
  urlbase='https://timpsco.in/graphql'
  hd={"authorization":auth,"content-type":"application/json"}
  refresh=curl.post(urlbase,headers=hd,data=json.dumps(json.loads(data))).json()
  if refresh["data"]["refreshToken"] == None:
    auth=auth
  else:
    auth=refresh["data"]["refreshToken"]["token"]
    hasil={"operationName":"refreshToken","variables":{"input":{"token":refresh["data"]["refreshToken"]["token"],"refresh_token":refresh["data"]["refreshToken"]['refresh_token']}},"query":"mutation refreshToken($input: TokenInput) {\n  refreshToken(input: $input) {\n    token\n    refresh_token\n    __typename\n  }\n}\n"}
    save_data(tele=None,name=host,inp=hasil)
  hd={"authorization":auth,"content-type":"application/json","referer":"https://timpsco.in/dashboard"}
  dash=curl.post(urlbase,headers=hd,data=json.dumps(get_user)).json()["data"]["getUser"]
  akun=Tree('[green]> [yellow]Account information')
  akun.add("[green]> [yellow]"+dash['username'].capitalize())
  akun.add("[green]> [yellow]"+str(dash['balance']))
  akun.add("[green]> [yellow]"+str(dash['credits']))
  akun.add("[green]> [yellow]"+str(dash['status']))
  akun.add("[green]> [yellow]"+str(dash['level']))
  rprint(akun)
  rprint(Tree('[green]> [yellow]Start ptc wall'))
  ptc_wall=curl.post(urlbase,headers=hd,data=json.dumps(ptc_wall)).json()["data"]["getAdsPtcWall"]["Ads"]
  for ptc in ptc_wall:
   try:
    view=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getAdsPtcWallID","variables":{"id":ptc["id"]},"query":"query getAdsPtcWallID($id: ID!) {\n  getAdsPtcWallID(id: $id) {\n    id\n    title\n    description\n    url\n    duration\n    reward\n    __typename\n  }\n}\n"})).json()["data"]["getAdsPtcWallID"]
    print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+parser(view['description'].strip().splitlines()[0]),end=end())
    sleep(1)
    #animasi(detik=view['duration'])
    hd["referer"]="https://timpsco.in/view-ad/"+ptc["id"]
    verify=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"earnAdsPtcWall","variables":{"id":ptc["id"]},"query":"mutation earnAdsPtcWall($id: ID!) {\n  earnAdsPtcWall(id: $id) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    result\n    validate {\n      id_ad\n      __typename\n    }\n    notification\n    __typename\n  }\n}\n"})).json()
    res=verify["data"]['earnAdsPtcWall']['user']
    if res!=None:
      print(putih1+'├──'+'─'*56)
      sukses=Tree('[white]├── [green]> [yellow]Succes ptc wall')
      sukses.add('[green]Balance [white]> [yellow]'+str(res["balance"]))
      sukses.add('[green]level [white]> [yellow]'+str(res["level"]))
      rprint(sukses)
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc wall!                             ')
  rprint(Tree('[green]> [yellow]Start ptc iframe'))
  while True:
   try:
    get_ads=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getAdsIframe","variables":{},"query":"query getAdsIframe {\n  getAdsIframe {\n    Ads {\n      id\n      title\n      description\n      url\n      duration\n      reward\n      __typename\n    }\n    total\n    __typename\n  }\n}\n"})).json()["data"]["getAdsIframe"]["Ads"]
    if len(get_ads) == 0 :break
    tipe=type(get_ads)
    if str(tipe)=="<class 'list'>":
      get_ads=get_ads[0]
    
    print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+parser(get_ads['description'].strip().splitlines()[0]),end=end())
    sleep(1)
    hd["referer"]="https://timpsco.in/surf-ads"
    verify=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"earnAds","variables":{"id":get_ads["id"]},"query":"mutation earnAds($id: ID!) {\n  earnAds(id: $id) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    result\n    notification\n    __typename\n  }\n}\n"})).json()
    res=verify["data"]['earnAds']['user']
    if res!=None:
      print(putih1+'├──'+'─'*56)
      sukses=Tree('[white]├── [green]> [yellow]Succes ptc wall')
      sukses.add('[green]Balance [white]> [yellow]'+str(res["balance"]))
      sukses.add('[green]level [white]> [yellow]'+str(res["level"]))
      rprint(sukses)
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc iframe!')
  rprint(Tree('[green]> [yellow]Start shortlinks'))
  get_sl=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getShortLinkAll","variables":{"offset":0,"limit":50,"status":1},"query":"query getShortLinkAll($offset: Int, $limit: Int, $status: Int) {\n  getShortLinkAll(offset: $offset, limit: $limit, status: $status) {\n    short_link {\n      id\n      site\n      link_refe\n      destination_link\n      api\n      value\n      view\n      createAt\n      like\n      status\n      rating\n      adult\n      total_views\n      __typename\n    }\n    total\n    __typename\n  }\n}\n"})).json()["data"]["getShortLinkAll"]["short_link"]
  for sl in get_sl:
    #print(sl)
    jumlah=sl["view"]
    id=sl["id"]
    re=jumlah
    for ulang in range(jumlah):
     try:
      gt_sl=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"createShortLink","variables":{"id":id},"query":"mutation createShortLink($id: ID!) {\n  createShortLink(id: $id)\n}\n"})).json()["data"]["createShortLink"]
      answer=bypass_link(gt_sl,modulesl,jumlah=[str(re),jumlah])
      if answer==False:break
      elif 'failed to bypass' in answer:pass
      else:
        animasi(detik=105)
        path=urlparse(answer).path.split('/short-link/')[1]
        verif={"operationName":"validateClick","variables":{"key":path},"query":"mutation validateClick($key: String) {\n  validateClick(key: $key) {\n    msg\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    shortLinkValidClick {\n      id_short_link\n      value\n      __typename\n    }\n    notification\n    __typename\n  }\n}\n"}
        hd["referer"]=answer
        reward=curl.post(urlbase,headers=hd,data=json.dumps(verif)).json()["data"]['validateClick']
        if reward["msg"] == 'ok':
          dash=reward['user']
          print(putih1+'├──'+hijau1+f' {kuning1}Message {putih1}> {hijau1}'+str(reward["msg"].capitalize())+'                         ')
          print(putih1+'├──'+hijau1+f' {kuning1}Balance {putih1}> {hijau1}'+str(dash["balance"]))
          print(putih1+'├──'+hijau1+f' {kuning1}level {putih1}> {hijau1}'+str(dash["level"]))
          re-=1
     except Exception as e:
       keluar(str(e))
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc shortlinks!')
  rprint(Tree('[green]> [yellow]Payout Boost'))
  multi={1:"1x",2:"2x",3:"3x",4:"4x",5:"5x",6:"6x",7:"7x"}
  for nomor,value in multi.items():
    print(f"{hijau1}> {kuning1}{str(nomor)}{putih1}. {hijau1}{value}")
  select=input(f"{hijau1}> {kuning1}select {putih1}: ")
  rprint(Tree('[green]> [yellow]Select Currencies'))
  get_coin=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getTypeCoinAll","variables":{},"query":"query getTypeCoinAll {\n  getTypeCoinAll {\n    id\n    name\n    sigla\n    value\n    image\n    id_coin\n    price_change_percentage_24h\n    pool_full\n    pool_total\n    network {\n      minimum_withdrawal_usd\n      network\n      description\n      contract\n      decimal_token\n      __typename\n    }\n    decimal_token\n    __typename\n  }\n}\n"})).json()["data"]["getTypeCoinAll"]
  nomor=0
  for coin in get_coin:
    print(f"{hijau1}> {kuning1}{str(nomor)}{putih1}. {hijau1}"+coin["name"])
    nomor+=1
  print(f"{putih1}[ {kuning1}! {putih1}]{hijau1}Jika ingin memilih coin lebih dari 1 pisah dengan koma contoh : 3,2,7,5")
  coin=input(f"{hijau1}> {kuning1}select {putih1}: ")
  if ',' in coin:
    coin=coin.split(',')
  else:
    coin=coin.split()
  data=[]
  for coin in coin:
    info=get_coin[int(coin)]
    id=info["id"]
    id_coin=info["id_coin"]
    value=info["value"]
    data.append({"id":id,"id_coin":id_coin,"value":value})
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper()+' Auto Faucet')
  data={"operationName":"autoClaim","variables":{"mult":int(select),"input":data},"query":"mutation autoClaim($mult: Int, $input: [TypeCoinInput]) {\n  autoClaim(mult: $mult, input: $input) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    coin {\n      sigla\n      name\n      value\n      id_coin\n      __typename\n    }\n    __typename\n  }\n}\n"}
  rprint(Tree('[green]> [yellow]Start auto faucet'))
  while True:
    animasi(menit=1)
    refresh=curl.post(urlbase,headers=hd,data=json.dumps(json.loads(refreshToken))).json()
    if refresh["data"]["refreshToken"] == None:
      auth=auth
    else:
      auth=refresh["data"]["refreshToken"]["token"]
      hasil={"operationName":"refreshToken","variables":{"input":{"token":refresh["data"]["refreshToken"]["token"],"refresh_token":refresh["data"]["refreshToken"]['refresh_token']}},"query":"mutation refreshToken($input: TokenInput) {\n  refreshToken(input: $input) {\n    token\n    refresh_token\n    __typename\n  }\n}\n"}
      save_data(tele=None,name=host,inp=hasil)
    hd={"authorization":auth,"content-type":"application/json","referer":"https://timpsco.in/autofaucet"}
    auto=curl.post(urlbase,headers=hd,data=json.dumps(data))
    if 'Your balance is not enough!' in str(auto.text):
      print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'Your balance is not enough!                             ')
      break
    get_bal=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getUserCoins","variables":{},"query":"query getUserCoins {\n  getUserCoins {\n    id\n    sigla\n    balance\n    id_coin\n    id_user\n    user_address {\n      address\n      network\n      __typename\n    }\n    __typename\n  }\n}\n"})).json()
    print(putih1+'├──'+hijau1+f' {kuning1}Message {putih1}> {hijau1} Ok                      ')
    for coin in get_bal["data"]["getUserCoins"]:
      print(putih1+'├──'+hijau1+f' {kuning1}'+coin["id_coin"]+f' {putih1}> {hijau1}'+str(coin["balance"]))
    print(putih1+'├──'+'─'*56)
    
  
  
  
  
  
  
  
  
  