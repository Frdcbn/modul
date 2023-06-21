import requests,json,time
from os import system
import shutil,os
from time import sleep
import random
from bs4 import BeautifulSoup as bs
from http.cookies import SimpleCookie
from urllib.parse import urlparse,urlencode
from tqdm import tqdm
from pyfiglet import figlet_format 
import pathlib
from telethon import TelegramClient, sync, events
def random_sleep():
    # Menghasilkan waktu sleep acak antara 5 hingga 35 detik
    sleep_time = random.randint(5, 35)
    time.sleep(sleep_time)
def animasi(menit):
  detik = menit * 60
  pattern_list = list("▁▃▅▇▅▃▁") * detik
  for i in range(detik):
      animasi = "".join(pattern_list[i:i+5])
      output = f"[{animasi}] - Please wait {detik//60:02d}:{detik%60:02d}"
      print(output, end='\r')
      time.sleep(1)
      detik -= 1
def bot_tele(modulesl, banner):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner('BOT CCTIP')
    api_id = 9209038
    api_hash = '82d6f5d828fc5f5942e29bdfc1e01d14'
    nomor=open('nomor.txt').read().splitlines()[0]
    async def handle_new_message(event):
      message = event.message
      # Process the new message as needed
      pesan=message.text
      print(f'{putih1}[{kuning1} > {putih1}]{hijau1} {pesan}')
      id_tip=["962775809","6285122310","5796879502","1380459388","6143654908"]
      ucapan_terimakasih = open("data.txt").read().splitlines()
      ucapan = random.choice(ucapan_terimakasih)
      if 'pengguna mengumpulkan hujan Anda.' in message.text:
        if str(message.from_id.user_id) in id_tip:
         if message.mentioned:
           random_sleep()
           await message.reply(ucapan)
      if 'Berhasil sawer' in message.text:
        if str(message.from_id.user_id) in id_tip:
         if message.mentioned:
           random_sleep()
           await message.reply(ucapan)
         else:
           random_sleep()
           await message.reply("congrats")
      if 'Airdrop sejumlah ' in message.text:
        if str(message.from_id.user_id) in id_tip:
         if message.mentioned:
           random_sleep()
           await message.reply(ucapan)
         else:
           random_sleep()
           await message.reply("congrats")
      if 'users collected your rain.' in message.text:
        if str(message.from_id.user_id) in id_tip:
         if message.mentioned:
           random_sleep()
           await message.reply(ucapan)
         else:
           random_sleep()
           await message.reply("congrats")
      if 'pengguna mengumpulkan undian Anda.' in message.text:
        if str(message.from_id.user_id) in id_tip:
         if message.mentioned:
           random_sleep()
           await message.reply(ucapan)
      if message.mentioned:
          # Memeriksa apakah akun Anda di-tag dalam pesan
          if str(message.from_id.user_id) in id_tip:
             random_sleep()
             await message.reply(ucapan)  # Merespons dengan pesan "Hai juga!"
      if 'Membuat undian di ' in message.text:
       if str(message.from_id.user_id) in id_tip:
        # if message.mentioned:
           random_sleep()
           pesan=pesan.split("Kirim ")[1].split(" untuk")[0]
           await message.reply(pesan)
      if 'Membuat airdrop di ' in message.text:
       if str(message.from_id.user_id) in id_tip:
        # if message.mentioned:
           random_sleep()
           pesan=pesan.split("Kirim ")[1].split(" untuk")[0]
           await message.reply(pesan)
      if 'Giveaway sejumlah ' in message.text:
       if str(message.from_id.user_id) in id_tip:
        # if message.mentioned:
           random_sleep()
           pesan=pesan.split("Kata Kunci : `")[1].split("`")[0]
           await message.reply(pesan)
      if 'Created an airdrop in ' in message.text:
       if str(message.from_id.user_id) in id_tip:
      #   if message.mentioned:
           random_sleep()
           pesan=pesan.split("Send ")[1].split(" to")[0]
           await message.reply(pesan)
      if 'Created a draw in ' in message.text:
       if str(message.from_id.user_id) in id_tip:
     #    if message.mentioned:
           random_sleep()
           pesan=pesan.split("Send ")[1].split(" to")[0]
           await message.reply(pesan)
      if 'Create Airdrop Success!! ' in message.text:
       if str(message.from_id.user_id) in id_tip:
     #    if message.mentioned:
           random_sleep()
           pesan=pesan.split("Claim: `")[1].split("`")[0]
           await message.reply(pesan)
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
            await handle_new_message(event)

        client.start()
        client.run_until_disconnected()
hijau1 = "\033[1;92m"#Terang
kuning1 = "\033[1;93m"#Terang
putih1 = "\033[1;97m"#Terang
merah1 = "\033[1;91m"#Terang
biru1 = "\033[1;94m"#Terang
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
def save_data(name):
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
            data = json.load(file)
            cookies = data.get('cookies')
            user_agent = data.get('user_agent')
            if user_agent:
                print(f'{putih1}[{kuning1} ~ {putih1}] {hijau1}User-Agent sudah ada tetap update User-Agent? jika User-Agent sudah di update tetap cf gunakan User-Agent : XYZ/3.0')
                jawab = input('y/n : '.lower())
                if jawab == 'y':
                  user_agent = input(hijau1 + 'Masukkan User-Agent mu > ')
                cookies = input(hijau1 + 'Masukkan cookies mu > ')
            else:
                user_agent = input(hijau1 + 'Masukkan User-Agent mu > ')
            data = {
                'cookies': cookies,
                'user_agent': user_agent
            }
            with open(f'data/{name}/{name}.json', 'w') as file:
                json.dump(data, file)
          #  return cookies, user_agent
    except FileNotFoundError:
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
def btccanyon(modulesl,banner):
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
    save_data('btccanyon')
    btccanyon(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://btccanyon.com/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('btccanyon')
    btccanyon(modulesl,banner)
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
def claimlite(modulesl,banner):
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
    save_data('claimlite')
    claimlite(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://claimlite.club/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('claimlite')
    claimlite(modulesl,banner)
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
def rushbitcoin(modulesl,banner):
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
    save_data('rushbitcoin')
    rushbitcoin(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://rushbitcoin.com/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('rushbitcoin')
    rushbitcoin(modulesl,banner)
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
     save_data('rushbitcoin')
     rushbitcoin(modulesl,banner)
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
def claimbits(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  nama_host="claimbits"
  host="claimbits.net"
  banner.banner(nama_host.upper())
  data_control(''+nama_host+'')
  def save_data(name):
    try:
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
    save_data(nama_host)
    claimbits(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    if 'Balance' not in get_sl.text:
      save_data(nama_host)
      claimbits(modulesl,banner)
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(nama_host)
    claimbits(modulesl,banner)
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
     save_data(nama_host)
     claimbits(modulesl,banner)
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
     save_data(nama_host)
     claimbits(modulesl,banner)
def ltchunt(modulesl,banner):
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
    save_data(nama_host)
    ltchunt(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/shortlinks.html',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(nama_host)
    ltchunt(modulesl,banner)
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
     save_data(nama_host)
     ltchunt(modulesl,banner)
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
def coinzask(modulesl,banner):
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
    save_data(nama_host)
    coinzask(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
  }
  curl=requests.Session()
  get_sl=curl.get('https://'+host+'/',headers=ua,cookies=cookies)
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data(nama_host)
    coinzask(modulesl,banner)
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
     save_data(nama_host)
     coinzask(modulesl,banner)
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
def coingax(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coingax')
  banner.banner('COINGAX')
  cookies, ugentmu = load_data('coingax')
  if not os.path.exists("data/coingax/coingax.json"):
    save_data('coingax')
    coingax(modulesl,banner)
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
    save_data('coingax')
    coingax(modulesl,banner)
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
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
          
    if 'Shortsfly - Mid' in name:
      for i in range(int(jumlah)):
        link=li.find('a',{'class':'btn btn-success w-100'})['href']
        get_links=curl.get(link,headers=ua,cookies=cookies,allow_redirects=False).headers['Location']
        print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Try to bypass : '+get_links,end='\r')
        answer=modulesl.shortfly(get_links)
        if 'failed to bypass' in answer:
          print(f'{putih1}[{merah1} ! {putih1}] {hijau1}Failed to bypass',end='\r')
        else:
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
          reward = curl.get(answer,headers=ua,cookies=cookies)
          print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("text: '")[1].split("your balance',")[0]+'your balance')
   except Exception as e:pass
  exit()
def crypto2u(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('crypto2u')
  banner.banner('CRYPTO2U')
  cookies, ugentmu = load_data('crypto2u')
  if not os.path.exists("data/crypto2u/crypto2u.json"):
    save_data('crypto2u')
    crypto2u(modulesl,banner)
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
    save_data('crypto2u')
    crypto2u(modulesl,banner)
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
                      reward = curl.get(answer, headers=ua, cookies=cookies)
                      dahs=curl.get('https://crypto2u.xyz/dashboard',headers=ua,cookies=cookies)
                      fd=bs(dahs.text,'html.parser').find_all('div',{'class':'col-xl-4 col-lg-6 col-md-6 col-sm-6 col-xs-12'})
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}' + fd[0].text.strip().splitlines()[0]+' : '+fd[0].text.strip().splitlines()[1]+'                                         ')
      except Exception as e:pass
  exit()
def claimsatoshi(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('claimsatoshi')
  banner.banner('CLAIMSATOSHI')
  cookies, ugentmu = load_data('claimsatoshi')
  if not os.path.exists("data/claimsatoshi/claimsatoshi.json"):
    save_data('claimsatoshi')
    claimsatoshi(modulesl,banner)
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
    save_data('claimsatoshi')
    claimsatoshi(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-xl-3 col-sm-6'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[1]+' : '+info.text.strip().splitlines()[0])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://claimsatoshi.xyz/ptc',headers=ua,cookies=cookies)
  surf=bs(ptc.text,'html.parser').find_all('div',{'class':'col-12 col-lg-4 mb-3 mb-lg-0'})
  if 'Website Available' not in ptc.text:
    save_data('claimsatoshi')
    claimsatoshi(modulesl,banner)
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
  print(hijau1+"> "+kuning1+"Start faucet")
  #<h2 class="card-title text-white">49/50</h2>
  ulang=bs(curl.get('https://claimsatoshi.xyz/faucet',headers=ua,cookies=cookies).text,'html.parser').find_all('h2',{'class':'card-title text-white'})
  ulang=ulang[len(ulang)-1].text.split('/')[0]
  for ulang in range(int(ulang)):
    faucet=curl.get('https://claimsatoshi.xyz/faucet',headers=ua,cookies=cookies)
    bs4 = bs(faucet.text, "html.parser")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    data["captcha"]="recaptchav2"
    answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',faucet.url)
    data["g-recaptcha-response"]=answer
    verify=curl.post('https://claimsatoshi.xyz/faucet/verify',data=data,headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"})
    if 'firewall' in verify.url:
      bs4 = bs(verify.text, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      data["captcha"]="recaptchav2"
      answer=modulesl.RecaptchaV2('6LduER0gAAAAAN1zeqcxdU3FxDAwgOI7PhMGUzR0',faucet.url)
      data["g-recaptcha-response"]=answer
      gas=curl.post('https://claimsatoshi.xyz/firewall/verify',data=data,headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"})
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
    animasi(5)
  exit()
def coinfola(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinfola')
  banner.banner('COINFOLA')
  cookies, ugentmu = load_data('coinfola')
  if not os.path.exists("data/coinfola/coinfola.json"):
    save_data('coinfola')
    coinfola(modulesl,banner)
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
  #  print(dahs.text)
    if 'Balance' not in dahs.text:
      save_data('coinfola')
      coinfola(modulesl,banner)
  except Exception as e:
    save_data('coinfola')
    coinfola(modulesl,banner)
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
def simpleads(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('simpleads')
  banner.banner('SIMPLEADS')
  cookies, ugentmu = load_data('simpleads')
  if not os.path.exists("data/simpleads/simpleads.json"):
    save_data('simpleads')
    simpleads(modulesl,banner)
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
    if 'Balance' not in dahs.text:
      save_data('simpleads')
      simpleads(modulesl,banner)
  except Exception as e:
    save_data('simpleads')
    simpleads(modulesl,banner)
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
     save_data('simpleads')
     simpleads(modulesl,banner)
  exit()
def adhives(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('adhives')
  banner.banner('ADHIVES')
  cookies, ugentmu = load_data('adhives')
  if not os.path.exists("data/adhives/adhives.json"):
    save_data('adhives')
    adhives(modulesl,banner)
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
    if 'Balance' not in dahs.text:
      save_data('adhives')
      adhives(modulesl,banner)
  except Exception as e:
    save_data('adhives')
    adhives(modulesl,banner)
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
              link=i.find('a',{'class':'card shadow text-decoration-none text-dark'})['href']
              for ulang in range(int(y)):
                  get_links = curl.get('https://adhives.com' + link, headers=ua, cookies=cookies, allow_redirects=False).headers['Location']
                  print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end='\r')
                  answer = providers[provider](get_links)
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
    except Exception as e:
      pass
  exit()
def coinsfarm(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinsfarmers')
  banner.banner('COINSFARMERS')
  cookies, ugentmu = load_data('coinsfarmers')
  if not os.path.exists("data/coinsfarmers/coinsfarmers.json"):
    save_data('coinsfarmers')
    adhives(modulesl,banner)
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
    if 'Balance' not in dahs.text:
      save_data('coinsfarmers')
      coinsfarm(modulesl,banner)
  except Exception as e:
    save_data('coinsfarmers')
    coinsfarm(modulesl,banner)
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
                  reward = curl.get(answer, headers=ua, cookies=cookies)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  elif 'Congratulations.' in reward.text:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0]+'       ')
    except Exception as e:
      pass
  exit()
def earnsolana(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('earnsolana')
  banner.banner('EARNSOLANA')
  cookies, ugentmu = load_data('earnsolana')
  if not os.path.exists("data/earnsolana/earnsolana.json"):
    save_data('earnsolana')
    earnsolana(modulesl,banner)
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
    save_data('earnsolana')
    earnsolana(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://earnsolana.xyz/ptc',headers=ua,cookies=cookies)
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
def cryptogenz(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('cryptogenz')
  banner.banner('CRYPTOGENZ')
  cookies, ugentmu = load_data('cryptogenz')
  if not os.path.exists("data/cryptogenz/cryptogenz.json"):
    save_data('cryptogenz')
    cryptogenz(modulesl,banner)
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
    save_data('cryptogenz')
    cryptogenz(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://cryptogenz.fun/ptc',headers=ua,cookies=cookies)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
  for ptc in ptc:
   try:
    name=ptc.find('h5',{'class':'card-title'}).text
    link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
    print(f'{putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end='\r')
    visit=curl.get(link,headers=ua,cookies=cookies)
    sleep(int(visit.text.split('var timer = ')[1].split(';')[0]))
    csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LfFYXcmAAAAANLF2BRgquqqDLTFFcFL1Qt18i9Q',link)
    data=f"captcha=recaptchav2&g-recaptcha-response={answer}&csrf_token_name={csrf}"
    verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://cryptogenz.fun/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        
        services = {
    "Shortsfly": modulesl.shortfly,
    "Linksfly": modulesl.linksfly,
 #   "Cpmicu": None,
    "Gainlink": modulesl.gain_lk,
    "Shrinkearn": modulesl.shrinkearn,
    "Ctrsh": modulesl.ctrsh,
    "Shrinkme": modulesl.shrinkme,
    "Usalink": modulesl.usalink,
    "Trylink": modulesl.try2,
    "Birdurl": modulesl.birdurl,
    "Owllink": modulesl.owlink,
    "Cuty": modulesl.cuty_io,
    "Short.i": modulesl.shorti_io
      }
        
        if name in services:
            for ulang in range(jumlah):
                url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = services[name](url)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
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
def coinpay_faucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinpay-faucet')
  banner.banner('COINPAY-FAUCET')
  cookies, ugentmu = load_data('coinpay-faucet')
  if not os.path.exists("data/coinpay-faucet/coinpay-faucet.json"):
    save_data('coinpay-faucet')
    coinpay_faucet(modulesl,banner)
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
    save_data('coinpay-faucet')
    coinpay_faucet(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://coinpay-faucet.com/links',headers=ua,cookies=cookies).text
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
def james_trussy(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('james-trussy')
  banner.banner('JAMES-TRUSSY')
  cookies, ugentmu = load_data('james-trussy')
  if not os.path.exists("data/james-trussy/james-trussy.json"):
    save_data('james-trussy')
    james_trussy(modulesl,banner)
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
    save_data('james-trussy')
    james_trussy(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://james-trussy.com/links',headers=ua,cookies=cookies).text
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
def freeclaimfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('freeclaimfaucet')
  banner.banner('freeclaimfaucet')
  cookies, ugentmu = load_data('freeclaimfaucet')
  if not os.path.exists("data/freeclaimfaucet/freeclaimfaucet.json"):
    save_data('freeclaimfaucet')
    freeclaimfaucet(modulesl,banner)
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
    save_data('freeclaimfaucet')
    freeclaimfaucet(modulesl,banner)
  info=bs(dash.text,'html.parser').find('div',{'class':'mt-3 text-3xl font-semibold text-white'})
  print(hijau1+"> "+kuning1+"Account information")
  print(hijau1+'> Your Balance : '+info.text.strip())
  print(hijau1+"> "+kuning1+"Start bypass ptc")
  ptc=curl.get('https://freeclaimfaucet.com/ptc',headers=ua,cookies=cookies)
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
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
        jumlah = int(i.find('span').text.split('/')[0])
        services = {
    'ctr.sh': modulesl.ctrsh,
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
 #   token=info.find('input',{'name':'token'})['value']
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
def eurofaucet_de(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('eurofaucet.de')
  banner.banner('EUROFAUCET.DE')
  cookies, ugentmu = load_data('eurofaucet.de')
  if not os.path.exists("data/eurofaucet.de/eurofaucet.de.json"):
    save_data('eurofaucet.de')
    eurofaucet_de(modulesl,banner)
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
    save_data('eurofaucet.de')
    eurofaucet_de(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass ptc")
  ptc=curl.get('https://eurofaucet.de/ptc',headers=ua,cookies=cookies)
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
def tefaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('tefaucet.online')
  banner.banner('TEFAUCET.ONLINE')
  cookies, ugentmu = load_data('tefaucet.online')
  if not os.path.exists("data/tefaucet.online/tefaucet.online.json"):
    save_data('tefaucet.online')
    tefaucet(modulesl,banner)
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
    save_data('tefaucet.online')
    tefaucet(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass ptc")
  ptc=curl.get('http://tefaucet.online/ptc',headers=ua,cookies=cookies)
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
  print(hijau1+"> "+kuning1+"Start faucet")
  mad=curl.get('http://tefaucet.online/faucet',headers=ua,cookies=cookies)
  f=bs(mad.text,'html.parser').find_all('div',{'class':'col-md-6 col-xl-3 mb-3 mb-xl-3'})
  jumlah=int(f[len(f)-1].text.strip().split('/')[0])
  for i in range(jumlah):
    faucet=curl.get("http://tefaucet.online/faucet",headers=ua,cookies=cookies)
    if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6LfO_NgkAAAAALPup3qKwQtj3hQ1wUDP53ELBYxe',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("http://tefaucet.online/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
    faucet=curl.get("http://tefaucet.online/faucet",headers=ua,cookies=cookies)
    fd=bs(faucet.text,'html.parser')
    csrf=fd.find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LfO_NgkAAAAALPup3qKwQtj3hQ1wUDP53ELBYxe',faucet.url)
    data=f"csrf_token_name={csrf}&captcha=recaptchav2&recaptchav3=&g-recaptcha-response={answer}"
    reward=curl.post('http://tefaucet.online/faucet/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data=data)
    #print(reward.text)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
    animasi(3)
  print(hijau1+"> "+kuning1+"Start mad faucet")
  mad=curl.get('http://tefaucet.online/madfaucet',headers=ua,cookies=cookies)
  f=bs(mad.text,'html.parser').find_all('div',{'class':'col-md-6 col-xl-3 mb-3 mb-xl-3'})
  jumlah=int(f[len(f)-1].text.strip().split('/')[0])
  for i in range(jumlah):
    faucet=curl.get("http://tefaucet.online/madfaucet",headers=ua,cookies=cookies)
    if 'firewall' in faucet.url:
      info=bs(faucet.text,'html.parser')
      csrf=info.find('input',{'name':'csrf_token_name'})['value']
      answer=modulesl.RecaptchaV2('6LfO_NgkAAAAALPup3qKwQtj3hQ1wUDP53ELBYxe',faucet.url)
      data=f"g-recaptcha-response={answer}&captchaType=recaptchav2&csrf_token_name={csrf}"
      gas=curl.post("http://tefaucet.online/firewall/verify",headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu},data=data,cookies=cookies)
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
    faucet=curl.get("http://tefaucet.online/madfaucet",headers=ua,cookies=cookies)
    fd=bs(faucet.text,'html.parser')
    csrf=fd.find('input',{'name':'csrf_token_name'})['value']
    answer=modulesl.RecaptchaV2('6LfO_NgkAAAAALPup3qKwQtj3hQ1wUDP53ELBYxe',faucet.url)
    data=f"csrf_token_name={csrf}&captcha=recaptchav2&recaptchav3=&g-recaptcha-response={answer}"
    reward=curl.post('http://tefaucet.online/madfaucet/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data=data)
    #print(reward.text)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   # animasi(5)
    sleep(5)
  exit()
def bitmonk(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('bitmonk')
  banner.banner('BITMONK')
  cookies, ugentmu = load_data('bitmonk')
  if not os.path.exists("data/bitmonk/bitmonk.json"):
    save_data('bitmonk')
    bitmonk(modulesl,banner)
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
    save_data('bitmonk')
    bitmonk(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('p',{'class':'text-uppercase fw-medium text-muted text-truncate mb-0'})
  info1=bs(dash.text,'html.parser').find_all('span',{'class':'counter-value'})
  del info[len(info)-2]
  del info1[len(info1)-2]
  print(hijau1+"> "+kuning1+"Account information")
  for inf in range(3):
    print(hijau1+'> '+info[inf].text.strip()+' : '+info1[inf]['data-target'])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://bitmonk.me/ptc',headers=ua,cookies=cookies)
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
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Yahoo! Reward Credited Successfully!' in reward:
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split("<div class='alert alert-success alert-border-left alert-dismissible  alert-borderless'>")[1].split('</div>')[0])
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  #exit()
 
  exit()
def claim_ro(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('claim_ro')
  banner.banner('CLAIM_RO')
  cookies, ugentmu = load_data('claim_ro')
  if not os.path.exists("data/claim_ro/claim_ro.json"):
    save_data('claim_ro')
    claim_ro(modulesl,banner)
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
    save_data('claim_ro')
    claim_ro(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://claimro.com/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data('claim_ro')
    claim_ro(modulesl,banner)
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
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
def faucetcrypto_net(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucetcrypto_net')
  banner.banner('FAUCETCRYPTO_NET')
  cookies, ugentmu = load_data('faucetcrypto_net')
  if not os.path.exists("data/faucetcrypto_net/faucetcrypto_net.json"):
    save_data('faucetcrypto_net')
    faucetcrypto_net(modulesl,banner)
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
    save_data('faucetcrypto_net')
    faucetcrypto_net(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'d-flex d-lg-flex d-md-block align-items-center'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://faucetcrypto.net/ptc',headers=ua,cookies=cookies)
  if 'ads available' not in ptc.text:
    save_data('faucetcrypto_net')
    faucetcrypto_net(modulesl,banner)
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
    if 'Good job!' in verify.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
        save_data('faucetcrypto_net')
        faucetcrypto_net(modulesl,banner)
        pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucetcrypto.net/links',headers=ua,cookies=cookies).text
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
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
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
def faucetspeedbtc(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucetspeedbtc')
  banner.banner('FAUCETSPEEDBTC')
  cookies, ugentmu = load_data('faucetspeedbtc')
  if not os.path.exists("data/faucetspeedbtc/faucetspeedbtc.json"):
    save_data('faucetspeedbtc')
    faucetspeedbtc(modulesl,banner)
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
    save_data('faucetspeedbtc')
    faucetspeedbtc(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
 # print(hijau1+"> "+kuning1+"Start ptc")
  
  
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucetspeedbtc.com/links',headers=ua,cookies=cookies).text
  fd=bs(get_links,'html.parser')
  link=fd.find_all('div',{'class':'col-lg-3'})
  for i in link:
    try:
        name = i.find('h4').text
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
def faucet4u(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('faucet4u')
  banner.banner('FAUCET4U')
  cookies, ugentmu = load_data('faucet4u')
  if not os.path.exists("data/faucet4u/faucet4u.json"):
    save_data('faucet4u')
    faucet4u(modulesl,banner)
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
    save_data('faucet4u')
    faucet4u(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://faucet4u.com/links',headers=ua,cookies=cookies).text
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
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
def tikiearn(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('tikiearn')
  banner.banner('TIKIEARN')
  cookies, ugentmu = load_data('tikiearn')
  if not os.path.exists("data/tikiearn/tikiearn.json"):
    save_data('tikiearn')
    tikiearn(modulesl,banner)
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
    save_data('tikiearn')
    tikiearn(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'media-body'})
  print(hijau1+"> "+kuning1+"Account information")
  del info[0]
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://tikiearn.com/ptc',headers=ua,cookies=cookies)
  #print(ptc.text)
  if 'ads available' not in ptc.text:
    save_data('tikiearn')
    tikiearn(modulesl,banner)
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
        save_data('tikiearn')
        tikiearn(modulesl,banner)
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
                    reward = curl.get(answer, headers=ua, cookies=cookies).text
                    if 'Good job!' in reward:
                        print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(f'{putih1}[{merah1} x {putih1}] {hijau1}invalid keys',end='\r')
    except Exception as e:pass
  exit()
def allfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('allfaucet')
  banner.banner('ALLFAUCET')
  cookies, ugentmu = load_data('allfaucet')
  if not os.path.exists("data/allfaucet/allfaucet.json"):
    save_data('allfaucet')
    allfaucet(modulesl,banner)
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
    save_data('allfaucet')
    allfaucet(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'invoice-box'})
  print(hijau1+"> "+kuning1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[0]+' : '+info.text.strip().splitlines()[1])
 # exit()
  print(hijau1+"> "+kuning1+"Start ptc")
  ptc=curl.get('https://allfaucet.xyz/ptc',headers=ua,cookies=cookies)
  if 'Ads Available' not in ptc.text:
    save_data('allfaucet')
    allfaucet(modulesl,banner)
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
        save_data('allfaucet')
        allfaucet(modulesl,banner)
        pass
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  get_links=curl.get('https://allfaucet.xyz/links',headers=ua,cookies=cookies).text
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
                sleep(10)
                if 'failed to bypass' in answer:
                    print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                else:
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
def btcadspace(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('btcadspace')
  banner.banner('BTCADSPACE')
  cookies, ugentmu = load_data('btcadspace')
  if not os.path.exists("data/btcadspace/btcadspace.json"):
    save_data('btcadspace')
    btcadspace(modulesl,banner)
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
      save_data('btcadspace')
      btcadspace(modulesl,banner)
  except Exception as e:
    save_data('btcadspace')
    btcadspace(modulesl,banner)
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
                  url = curl.get('https://btcadspace.com' + i.find('a', {'class': 'card shadow text-decoration-none text-dark'})['href'], headers=ua, cookies=cookies, allow_redirects=False).headers['location']
                  answer = bypass_func(url)
                  if 'failed to bypass' in answer:
                      print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
                  else:
                      get_reward = curl.get(answer, headers=ua, cookies=cookies)
                      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("message: '")[1].split("'")[0])
        except Exception as e:
          pass
  print(hijau1+"> "+kuning1+"Bypass faucet")
  k="6LdN-eIZAAAAAJJg4yaUbAvIvZZS85Zfa8j9XuXx"
  while True:
   try:
    get_ucet=curl.get('https://btcadspace.com/faucet',headers=ua, cookies=cookies)
    csrf=bs(get_ucet.text,'html.parser').find('input',{'name':'csrfToken'})['value']
    answer=modulesl.RecaptchaV2(key=k,url=get_ucet.url)
    data=f"csrfToken={csrf}&g-recaptcha-response={answer}&claim="
    reward=curl.post(get_ucet.url,data=data,headers={"content-type":"application/x-www-form-urlencoded","User-Agent":ugentmu,'Host':'btcadspace.com'},cookies=cookies)
    print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split("message: '")[1].split("'")[0])
    animasi(15)
   except Exception as e:
    save_data('btcadspace')
    btcadspace(modulesl,banner)
def nokofaucet(modulesl,banner):
  def save_datan(name):
      auth=input(hijau1+'masukan auth mu > ')
      id_claim=input(hijau1+'masukan id_claim mu > ')
      data = {
          'auth': auth,
          'id_claim': id_claim
      }
      # Menyimpan data dalam format JSON
      with open(f'data/{name}/{name}.json', 'w') as file:
          json.dump(data, file)
  def load_datan(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          auth = data['auth']
          id_claim = data['id_claim']
          return auth, id_claim
      except FileNotFoundError:
          return None, None
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('nokofaucet')
  banner.banner('NOKOFAUCET')
  auth, id_claim = load_datan('nokofaucet')
  if not os.path.exists("data/nokofaucet/nokofaucet.json"):
    save_datan('nokofaucet')
    nokofaucet(modulesl,banner)
  curl=requests.Session()
  ua={
  "accept":"application/json, text/plain, */*",
  "authorization":auth
  }
  try:
    print(hijau1+"> "+kuning1+"Account information")
    get_user=json.loads(curl.get('https://api.nokofaucet.com/api/auth/me',headers=ua).text)
    print(hijau1+'> '+"Username : "+get_user["username"]+' | Email : '+get_user["email"])
    print(hijau1+'> '+"Balance : "+str(get_user["balance"])+' | Energy : '+str(get_user["energy"]))
  except Exception as e:
    save_datan('nokofaucet')
    nokofaucet(modulesl,banner)
  print(hijau1+"> "+kuning1+"Start bypass shortlinks")
  sl=curl.get('https://api.nokofaucet.com/api/shortlink/getPagnigation?keyword=&page=1&perPage=30&sortDate=undefined&sortBy=undefined&paginationVersion=2',headers=ua)
  methods = {
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
  for data in json.loads(sl.text)["data"]:
    name=data['title']
    jumlah=data['remain_view']
    url=data['url']
    for method, bypass_func in methods.items():
        try:
          if method in name:
              for jun in range(jumlah):
                answer = bypass_func(url)
                if 'failed to bypass' in answer:
                  pass
                else:
                  reward=curl.get('https://api.nokofaucet.com/api/shortlink/view/'+answer.split('user/short-link/')[1],headers=ua)
                  print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+json.loads(reward.text)["message"]+'               ')
        except Exception as e:pass
  print(hijau1+"> "+kuning1+"Start bypass faucet")
  for i in range(int(get_user["remain_claim"])):
    reward=json.loads(curl.patch('https://api.nokofaucet.com/api/user/claim/'+id_claim,headers=ua).text)
    if 'successfully' in reward['message']:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward['message'])
      animasi(5)
    else:
      animasi(5)
  exit()
def landofbits(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('landofbits')
  banner.banner('LANDOFBITS')
  cookies, ugentmu = load_data('landofbits')
  if not os.path.exists("data/landofbits/landofbits.json"):
    save_data('landofbits')
    landofbits(modulesl,banner)
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
    save_data('landofbits')
    landofbits(modulesl,banner)
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
              reward = curl.get(answer, headers=ua, cookies=cookies)
              if 'Good job!' in reward.text:
                print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Good job! '+reward.text.split("text: '")[1].split("',")[0])
   except Exception as e:pass
  exit()
def oskut(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  def save_datan(name):
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
            data = json.load(file)
            cookies = data.get('email')
       #     user_agent = data.get('user_agent')
            cookies = input(hijau1 + 'Masukkan email mu > ')
            data = {
                'email': cookies,
            }
            with open(f'data/{name}/{name}.json', 'w') as file:
                json.dump(data, file)
          #  return cookies, user_agent
    except FileNotFoundError:
        cookies = input(hijau1 + 'Masukkan email mu > ')
        data = {
            'email': cookies,
       #     'user_agent': user_agent
        }
        with open(f'data/{name}/{name}.json', 'w') as file:
            json.dump(data, file)
        return cookies
  def load_datan(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          cookies = data['email']
      #    user_agent = data['user_agent']
          return cookies
      except FileNotFoundError:
          return None, None
  banner.banner('OSKUT')
  cookies= load_datan('oskut')
  if not os.path.exists("data/oskut/oskut.json"):
    save_datan('oskut')
    oskut(modulesl,banner)
  curl=requests.Session()
  step1=curl.get('https://oscut.fun/')
  fd=bs(step1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  data=f"wallet={cookies}&csrf_token_name={fd}"
  step2=curl.post('https://oscut.fun/auth/login',data=data,headers={"content-type":"application/x-www-form-urlencoded"})
  if 'Login Success' in step2.text:
    print(f'{putih1}[{hijau1} √ {putih1}] Login Success')
    print('1.BTC')
    print('2.USDT')
    curen=input('Select : ')
    if curen == '1':
      cur='btc'
    if curen == '2':
      cur='usdt'
    get_links=curl.get('https://oscut.fun/links/currency/'+cur)
    gt=bs(get_links.text,'html.parser').find_all('div',{'class':'col-sm-6'})
    for link in gt:
      jumlah=int(link.find('span').text.split('/')[0])
      name=link.find('h4').text
      li=link.find('a',{'class':'btn btn-primary waves-effect waves-light'})['href']
      services = {
      'Clks': modulesl.clks_pro,
      'Try2link': modulesl.try2,
      'Linksfly': modulesl.linksfly,
      'Shortsfly': modulesl.shortfly,
      'Clk': modulesl.clksh,
      'Owllink': modulesl.owlink
      }
      if name in services:
        for ulang in range(jumlah):
            url = curl.get(li,allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = services[name](url)
            if 'failed to bypass' in answer:
                print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
            else:
                reward = curl.get(answer)
              #  print(reward.text)
                if 'Success!' in reward.text:
               #   html: '0.00000009 BTC has been sent to your FaucetPay account!',
                  print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Success! '+reward.text.split("html: '")[1].split("',")[0])
def cryptofuture(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  def save_data(name):
    try:
        dir_path = f'data/{name}'
        os.makedirs(dir_path, exist_ok=True)  # Membuat direktori jika belum ada

        file_path = f'{dir_path}/{name}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
        else:
            email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
    except FileNotFoundError:
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
    save_data('cryptofuture')
    cryptofuture(modulesl,banner)
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
  #    print(name)
  #    print(li)
   #   print(jumlah)
      services = {
    #  'Clks': modulesl.clks_pro,
   #   'Try2link': modulesl.try2,
      'LinksFly': modulesl.linksfly,
      'ShortsFly.me': modulesl.shortfly,
      'Usalink': modulesl.usalink,
     # 'Clk': modulesl.clksh,
     # 'Owllink': modulesl.owlink
      }
      if name in services:
        for ulang in range(jumlah):
            url = curl.get(li,allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = services[name](url)
            if 'failed to bypass' in answer:
                print(f'{putih1}[{merah1} x {putih1}] {hijau1}failed to bypass',end='\r')
            else:
                reward = curl.get(answer)
              #  print(reward.text)
                if 'Success!' in reward.text:
               #   html: '0.00000009 BTC has been sent to your FaucetPay account!',
                  print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Success! '+reward.text.split("html: '")[1].split("',")[0])
def endenfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  def save_data(name):
    try:
        dir_path = f'data/{name}'
        os.makedirs(dir_path, exist_ok=True)  # Membuat direktori jika belum ada

        file_path = f'{dir_path}/{name}.json'
        
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
                email = data.get('email')
        else:
            email = input('Masukkan email mu > ')
        
        data = {
            'email': email
        }

        with open(file_path, 'w') as file:
            json.dump(data, file)

        return email
    except FileNotFoundError:
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
    save_data('edenfaucet')
    endenfaucet(modulesl,banner)
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
        reward=curl.get(answer)
       # print(reward.text)
      #  print(reward.text)
        if 'Success!' in reward.text:
            print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}Success! '+reward.text.split("html: '")[1].split("',")[0])