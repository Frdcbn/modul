#-------- import module ----------#
import requests,json,time,asyncio,re,shutil,os,random,pathlib,subprocess,traceback
from tqdm import tqdm
from os import system
from time import sleep
from bs4 import BeautifulSoup as bs
from http.cookies import SimpleCookie
from urllib.parse import urlparse,urlencode
from telethon import TelegramClient, sync, events
from rich.tree import Tree
from rich.panel import Panel
from rich import print as rprint
#----------- color ---------------#
hijau1 = "\033[1;92m"
kuning1 = "\033[1;93m"
putih1 = "\033[1;97m"
merah1 = "\033[1;91m"
biru1 = "\033[1;94m"
#----------- module ---------------#
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
  "short2url.in":modulesl.short2url,
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
def save_data(name,custom=None):
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
            data = json.load(file)
            cookies = data.get('cookies')
            user_agent = data.get('user_agent')
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
          if custom:
            data={}
            for req in custom:
              tany=input('Masukan '+req+' > ')
              data[req]=tany
            with open(f'data/{name}/{name}.json', 'w') as file:
              json.dump(data, file)
            return tany
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
def load_data(name,custom=None):
      try:
        if custom:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          data1=[]
          for req in custom:
            data1.append(data[req])
          return data
        else:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          cookies = data['cookies']
          user_agent = data['user_agent']
          return cookies, user_agent
      except FileNotFoundError:
          return None, None
def cek(name):
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/{name}/{i}.jpg')
          file_sizes.append(file_size)
      for i in range(5):
          if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
              return i
      return None
def get_answer(name,cookies,ugentmu):
      cache_control(name)
      us = {
          'accept': 'application/json, text/javascript, */*; q=0.01',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu,
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
      gt_cp = requests.post(f'https://{name}/system/libs/captcha/request.php',cookies=cookies, headers=us, data='cID=0&rT=1&tM=light')
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
          gt_im = requests.get(f'https://{name}/system/libs/captcha/request.php?cid=0&hash={hash[i]}', headers=gt,cookies=cookies, stream=True)
          status_code(gt_im)
          with open(f'cache/{name}/'+file_name, 'wb') as f:
              shutil.copyfileobj(gt_im.raw, f)
      ind = cek(name)
      answer = hash[ind]
      y = f'cID=0&pC={answer}&rT=2'
      us = {
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          'x-requested-with': 'XMLHttpRequest',
          'user-agent': ugentmu
      }
      ve = requests.post(f'https://{name}/system/libs/captcha/request.php', cookies=cookies,headers=us, data=y)
      status_code(ve)
      return answer
def ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl):
      ua = {
        "Host": host,
        'User-Agent': ugentmu,
    }
      def balance():
        get_sl = curl.get(f'https://{host}{path_ptc}', headers=ua, cookies=cookies)
        status_code(get_sl)
        return bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})[0].text.strip()
      pct = Tree("[gree] > [yellow]Start working on ptc")
      rprint(pct)
      get_ptc = curl.get(f'https://{host}{path_ptc}', headers=ua, cookies=cookies)
      status_code(get_ptc)
      get_id = bs(get_ptc.text, 'html.parser').find_all(*key_all_ptc)
      for _id in get_id:
          try:
              sesi = False
              while(sesi == False):
                  _i = _id["onclick"].split("opensite('")[1].split("','")[0]
                  key = get_ptc.text.split("var hash_key = '")[1].split("';")[0]
                  if host=='faucetofbob.xyz':
                    get_reward = curl.get(f'https://{host}/surf2.php?sid={_i}&key={key}', headers=ua, cookies=cookies)
                  else:
                    get_reward = curl.get(f'https://{host}/surf.php?sid={_i}&key={key}', headers=ua, cookies=cookies)
                  status_code(get_reward)
                  token1 = get_reward.text.split("var token = '")[1].split("';")[0]
                  secon = get_reward.text.split("var secs = ")[1].split(";")[0]
                  for i in tqdm(range(int(secon)), leave=False, desc=hijau1 + "visit > " + _id["onclick"].split("','")[1].split("');")[0]):
                      time.sleep(1)
                  answer = get_answer(name=host, cookies=cookies, ugentmu=ugentmu)
                  if answer:
                    reward = curl.post(f'https://{host}/system/ajax.php', data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}", headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, cookies=cookies)
                    status_code(reward)
                    if json.loads(reward.text)["status"] == 200:
                        gas = bs(json.loads(reward.text)["message"], "html.parser").find("div", {"class": "alert alert-success"}).text
                        print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + gas.strip())
                        print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                        sesi = True
          except Exception as e:
              print(putih1 + '├──' + hijau1 + f' {putih1}[{merah1}!{putih1}] {str(e)}')
              traceback.print_exc()
              pass
      print(putih1 + '└──' + hijau1 + ' [ ' + kuning1 + '√' + hijau1 + ' ] ' + "Success bypassing all ptc ;)")
def sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl):
      ua = {
        "Host": host,
        'User-Agent': ugentmu,
    }
      def balance():
        get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
        status_code(get_sl)
        return bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})[0].text.strip()
      get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
      if key_all_sl=='tr':
        gt_s = bs(get_sl.text, 'html.parser').find_all(key_all_sl)
      else:
        gt_s = bs(get_sl.text, 'html.parser').find_all(*key_all_sl)
      status_code(get_sl)
      token = get_sl.text.split("var token = '")[1].split("';")[0]
      sl = Tree("[green]> [yellow]Start Bypassing Shortlinks")
      rprint(sl)
      for i in gt_s:
        try:
          id = i.find(*key_button_id)
          if None == id:
              pass
          else:
            try:
              jumlah = int(i.find_all(*key_amount_sl)[1].text.split('/')[0])
            except Exception as e:
              jumlah = int(i.find(*key_amount_sl).text.split('/')[0])
            re = jumlah
            for i in range(jumlah):
              get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
              status_code(get_sl)
              token = get_sl.text.split("var token = '")[1].split("';")[0]
              status = True
              while(status == True):
                da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                answer=get_answer(name=host, cookies=cookies, ugentmu=ugentmu)
                if answer:
                  get_lk = curl.post(f'https://{host}/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf="+answer, allow_redirects=False, cookies=cookies)
                  status_code(get_lk)
                  get_lk = json.loads(get_lk.text)
                  if get_lk["status"] == 200:
                    answer = bypass_link(get_lk['shortlink'], modulesl, jumlah=[str(re), str(jumlah)])
                    if answer:
                      if 'failed to bypass' in answer:
                          break
                      else:
                        try:
                            animasi(detik=105)
                            get_sl = curl.get(answer, headers=ua, cookies=cookies)
                            status_code(get_sl)
                            sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                            print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + sukses)
                            print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                            re -= 1
                        except:
                            print(putih1 + '├──' + hijau1 + ' [ ' + merah1 + 'x' + hijau1 + ' ] ' + "invalid keys")
                        break
                    else:
                      status=False
                      break
                  if get_lk['status'] == 600:
                    print(putih1 + '├──' + hijau1 + ' [ ' + merah1 + 'x' + hijau1 + ' ] ' + "Captcha wrong", end="\r")
                  else:
                    print(putih1 + '├──' + hijau1 + ' [ ' + merah1 + 'x' + hijau1 + ' ] ' + "There seems to be something wrong with the link")
                    break
              if status==False:break
        except Exception as e:
          keluar(str(e))
          traceback.print_exc()
          pass
      print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '√' + hijau1 + ' ] ' + "Success bypassing all shortlinks ;)")
def bits_family(modulesl,banner,host, recaptcha_key,faucet=None,path_ptc='/ptc.html',key_all_ptc=('button', {'class': 'btn btn-success btn-sm w-100 mt-1'}),path_sl='/shortlinks.html',key_all_sl=('tr'),key_button_id=('button', {'class': 'btn btn-success btn-sm'}),key_amount_sl=('b', {'class': 'badge badge-dark'}),run=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner(host.upper())
    data_control(name=host)
    cookies, ugentmu = load_data(host)
    if not os.path.exists(f"data/{host}/{host}.json"):
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run)
    cookiek = SimpleCookie()
    cookiek.load(cookies)
    cookies = {k: v.value for k, v in cookiek.items()}
    ua = {
        "Host": host,
        'User-Agent': ugentmu,
    }
    curl = requests.Session()
    get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
    status_code(get_sl)
    if run is None:
      menu=['Run all','Run ptc','Run shortlinks','Run faucet']
      for i in range(len(menu)):
        print(putih1+'[ '+hijau1+str(i)+putih1+' ] '+putih1+menu[i])
      run=input(putih1+'[ '+kuning1+'?'+putih1+' ] '+ 'Input » ')
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner(host.upper())
    if 'Account Balance' not in get_sl.text:
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run)
    try:
        akun = Tree("[green]> [yellow]Account information")
        get_inf = bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})
        for info in get_inf:
            akun.add('[green]> [yellow]' + info.text.strip())
        rprint(akun)
    except Exception as e:
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run)
    def balance():
        get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
        status_code(get_sl)
        return bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})[0].text.strip()
    if run == '1':
      ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl)
    if run == '2':
      sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
    if run == '3':
      if faucet=='Off':
        print('Faucet off')
        exit()
      rprint(Tree("[green]> [yellow]Bypass faucet"))
      if faucet:fauceturl=f'https://{host}/{faucet}'
      else:fauceturl=f'https://{host}/'
      while True:
        try:
            get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
            if 'Faucet Locked!' in get_sl.text:
              if 'more Shortlinks today to be able to Roll & Win FREE Coins!' in get_sl.text:
                print(bs(get_sl.text,'html.parser').find('div',{'class':'alert alert-warning'}).text.strip())
                sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0')
              else:
                animasi(menit=1440)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0')
            waktu=get_sl.text.split('every ')[1].split(' minutes')[0]
            if 'Just a moment...' in get_sl.text:
              save_data(host)
              bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run)
            status_code(get_sl)
            if 'You can claim again in' in get_sl.text:
                tim = int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0]) * 60
                for i in tqdm(range(int(tim)), leave=False, desc="Please wait..."):
                    time.sleep(1)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            answer = modulesl.RecaptchaV2(recaptcha_key, get_sl.url)
            g = curl.post(f'https://{host}/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}", cookies=cookies)
            status_code(g)
            g = json.loads(g.text)
            if g["status"] == 200:
                gas = bs(g["message"], "html.parser").find("div", {"class": "alert alert-success"}).text
                print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + gas.strip())
                print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                for i in tqdm(range(int(waktu)*60), leave=False, desc="Please wait..."):
                    time.sleep(1)
            else:
              gas = bs(g["message"], "html.parser").text
              print(putih1 + '├──' + hijau1 + f' {putih1}[{merah1}!{putih1}] '+gas)
        except Exception as e:
            print(putih1 + '├──' + hijau1 + f' {putih1}[{merah1}!{putih1}] {str(e)}')
            pass
    if run == '0':
      ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl)
      sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
      if faucet=='Off':
        print('Faucet off')
        exit()
      rprint(Tree("[green]> [yellow]Bypass faucet"))
      if faucet:fauceturl=f'https://{host}/{faucet}'
      else:fauceturl=f'https://{host}/'
      while True:
        try:
            get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
            if 'Faucet Locked!' in get_sl.text:
              if 'more Shortlinks today to be able to Roll & Win FREE Coins!' in get_sl.text:
                print(bs(get_sl.text,'html.parser').find('div',{'class':'alert alert-warning'}).text.strip())
                sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0')
              else:
                animasi(menit=1440)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0')
            waktu=get_sl.text.split('every ')[1].split(' minutes')[0]
            if 'Just a moment...' in get_sl.text:
              save_data(host)
              bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run)
            status_code(get_sl)
            if 'You can claim again in' in get_sl.text:
                tim = int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0]) * 60
                for i in tqdm(range(int(tim)), leave=False, desc="Please wait..."):
                    time.sleep(1)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            answer = modulesl.RecaptchaV2(recaptcha_key, get_sl.url)
            g = curl.post(f'https://{host}/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}", cookies=cookies)
            status_code(g)
            g = json.loads(g.text)
            if g["status"] == 200:
                gas = bs(g["message"], "html.parser").find("div", {"class": "alert alert-success"}).text
                print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + gas.strip())
                print(putih1 + '├──' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                for i in tqdm(range(int(waktu)*60), leave=False, desc="Please wait..."):
                    time.sleep(1)
            else:
              gas = bs(g["message"], "html.parser").text
              print(putih1 + '├──' + hijau1 + f' {putih1}[{merah1}!{putih1}] '+gas)
        except Exception as e:
            print(putih1 + '├──' + hijau1 + f' {putih1}[{merah1}!{putih1}] {str(e)}')
            pass
def btccanyon(modulesl,banner):
  bits_family(modulesl,banner,'btccanyon.com', '6LdzF6MlAAAAACcN9JGXW8tSs4dy1MjeKZKFJ11M',faucet='Off')
def claimlite(modulesl,banner):
  bits_family(modulesl,banner,'claimlite.club', '6Leen-YUAAAAAFsd9t6qwRGyF8fLf6kixqicahQj')
def rushbitcoin(modulesl,banner):
  bits_family(modulesl,banner,'rushbitcoin.com', '6LfokMEUAAAAAEwBx23jh3mlghwTF7VJqbN9fERK')
def claimbits(modulesl,banner):
  bits_family(modulesl,banner,'claimbits.net', '6Lf6q3okAAAAAOO5I84xHj2g8cWRb-cNwsTnMHBa',faucet='faucet.html')
def ltchunt(modulesl,banner):
  bits_family(modulesl,banner,'ltchunt.com', '6Ld28FEkAAAAAHU7Z8ddeMVLzt4CAIzITn9g7ENZ',faucet='Off')
def faucetbob(modulesl,banner):
  bits_family(modulesl,banner,'faucetofbob.xyz', '6LcXEsIaAAAAAKEMIqgfoqCiBrHGAjmkfwgkfcQr',faucet='Off')
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
    
  }
  curl=requests.Session()
  try:
    dahs=curl.get('https://coinfola.com/account',headers=ua,cookies=cookies)
    status_code(dahs)
  except Exception as e:
    save_data('coinfola')
    coinfola(modulesl,banner)
  if 'Balance' not in dahs.text:
      save_data('coinfola')
      coinfola(modulesl,banner)
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
  ua["content-type"]="application/x-www-form-urlencoded"
  for i in gt:
    try:
      #print(i)
      y=[i for i in i.text.strip().splitlines() if i][2].replace(' ','')
      #print(y)
      if 'clicksremaining' in y:
        y=y.split('clicksremaining')[0]
      if 'clickremaining' in y:
        y=y.split('clickremaining')[0]
      link=i.find('a',{'class':'card shadow text-decoration-none shortlink'})['data-id']
      #answer = bypass_link(url)
      re=int(y)
      for ulang in range(int(y)):
          get_links = curl.post('https://coinfola.com/shortlinks#!', headers=ua, cookies=cookies,data='csrfToken=&go='+link, allow_redirects=False)
          status_code(get_links)
          #print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}Bypassing : '+get_links,end=end())
          answer = bypass_link(get_links.headers['location'],modulesl,jumlah=[str(re),y])
          if answer:
            if 'failed to bypass' in answer:
                pass
            else:
              animasi(detik=105)
              reward = curl.get(answer, headers=ua, cookies=cookies)
              if 'Congratulations.' in reward.text:
                  _1 = reward.text.split("message: 'You")[1].split("tickets.'")[0]
                  _2 = reward.text.split("message: 'Congratulations.")[1].split("credited.'")[0]
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Congratulations. ' + _2 + ' credited. & You ' + _1 + ' tickets.')
                  re-=1
    except Exception as e:
      keluar(str(e))
      pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://earnsolana.xyz/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('earnsolana')
    earnsolana(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-sm-3'})
  akun=Tree("[gree] > [yellow]Account information")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start ptc"))
  ptc=curl.get('https://earnsolana.xyz/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data('earnsolana')
    earnsolana(modulesl,banner)
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
    save_data('earnsolana')
    earnsolana(modulesl,banner)
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
                animasi(detik=20)
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://freeclaimfaucet.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('freeclaimfaucet')
    freeclaimfaucet(modulesl,banner)
  info=bs(dash.text,'html.parser').find('div',{'class':'mt-3 text-3xl font-semibold text-white'})
  akun=Tree("[green]> [yellow]Account information")
  akun.add('[green]> [yellow]Your Balance [white]: [yellow]'+info.text.strip())
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass ptc"))
  ptc=curl.get('https://freeclaimfaucet.com/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data('freeclaimfaucet')
    freeclaimfaucet(modulesl,banner)
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
    save_data('freeclaimfaucet')
    freeclaimfaucet(modulesl,banner)
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://faucetcrypto.net/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('faucetcrypto_net')
    faucetcrypto_net(modulesl,banner)
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
    save_data('faucetcrypto_net')
    faucetcrypto_net(modulesl,banner)
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
                  save_data('faucetcrypto_net')
                  faucetcrypto_net(modulesl,banner)
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://faucetspeedbtc.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('faucetspeedbtc')
    faucetspeedbtc(modulesl,banner)
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
    save_data('faucetspeedbtc')
    faucetspeedbtc(modulesl,banner)
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://tikiearn.com/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('tikiearn')
    tikiearn(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('h5',{'class':'mb-0 text-truncate font-size-15'})
  akun=Tree("[gree] > [yellow]Account information")
  akun.add('[gree] > [yellow]Balance [white]: [yellow]'+info[1].text.strip())
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start ptc"))
  ptc=curl.get('https://tikiearn.com/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  if 'ads available' not in ptc.text:
    save_data('tikiearn')
    tikiearn(modulesl,banner)
  ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-3'})
  for ptc in ptc:
   try:
      name=ptc.find('h4').text.strip()
      link=ptc.find('button')["onclick"].split("window.location = '")[1].split("'")[0]
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+parser(name),end='\r')
      visit=curl.get(link,headers=ua,cookies=cookies)
      csrf=bs(visit.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
      token=bs(visit.text,'html.parser').find('input',{'name':'token'})['value']
      status_code(visit)
      animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
      answer=modulesl.RecaptchaV2('6LcpH6omAAAAAPgjFK9i2npoqAvZLh-_L9M9t8Ds',link)
      data=f"captcha=recaptchav2&recaptchav3=&g-recaptcha-response={answer}&csrf_token_name={csrf}&token={token}"
      headers = {
    "Host": "tikiearn.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX3171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
    "Referer": visit.url
  }
      verify=curl.post(link.replace('view','verify'),data=data,headers=headers,cookies=cookies)
      status_code(verify)
      if 'Good job!' in verify.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except Exception as e:
        keluar(str(e))
        save_data('tikiearn')
        tikiearn(modulesl,banner)
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
    
  }
  curl=requests.Session()
  dash=curl.get('https://allfaucet.xyz/dashboard',headers=ua,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('allfaucet')
    allfaucet(modulesl,banner)
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
    save_data('allfaucet')
    allfaucet(modulesl,banner)
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
        save_data('allfaucet')
        allfaucet(modulesl,banner)
        pass
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks"))
  get_links=curl.get('https://allfaucet.xyz/links',headers=ua,cookies=cookies)
  status_code(get_links)
  if 'Links Available' not in get_links.text:
    save_data('allfaucet')
    allfaucet(modulesl,banner)
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
def paid_family(url,sitkey,email,modulesl):
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
    for links in link:
     try:
      li=links.find('a')['href']
      lis= [element.strip() for element in links.text.strip().splitlines()]
      name=lis[0]
      jumlah=int(lis[10].split(' /')[0])
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
def all_in_one(modulesl,banner):
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
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner('ALL IN ONE PAID FAMILY')
  cookies= load_data('all_in_one')
  if not os.path.exists("data/all_in_one/all_in_one.json"):
    save_data('all_in_one')
    all_in_one(modulesl,banner)
  print(hijau1+"> "+kuning1+"Start bypass paidtomoney.com")
  paid_family('https://paidtomoney.com/',"6LfZswEVAAAAAHXORtki0EFzDZZIV02Wo0krcxRo",cookies,modulesl)
def bitscript_family(url,modulesl,banner,key_links,bal=None):
  host=urlparse(url).netloc
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper())
  data_control(host)
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    bitscript_family(url,modulesl,banner,key_links,bal)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  try:
    dahs=curl.get(url+'account',headers=ua,cookies=cookies)
  except Exception as e:
    save_data(host)
    bitscript_family(url,modulesl,banner,key_links,bal)
  status_code(dahs)
  if 'Balance' not in dahs.text:
    save_data(host)
    bitscript_family(url,modulesl,banner,key_links,bal)
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
def cryptohits(modulesl,banner):
  bitscript_family("https://cryptohits.io/",modulesl,banner,"card shadow text-decoration-none","balance-left")
def clickscoin(modulesl,banner):
  url="https://clickscoin.com/"
  host=urlparse(url).netloc
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper())
  data_control(host)
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    clickscoin(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  try:
    dahs=curl.get(url+'account',headers=ua,cookies=cookies)
    status_code(dahs)
    if 'Balance' not in dahs.text:
      save_data(host)
      clickscoin(modulesl,banner)
  except Exception as e:
      save_data(host)
      clickscoin(modulesl,banner)
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
    save_data(name=host)
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
    save_data(name=host)
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
      save_data(name=host)
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
      bs4 = bs(visit.text, "html.parser")
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
    if 'links available' not in get_links.text.lower():
      save_data(name=host)
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
      bs4 = bs(get_.text, "html.parser")
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
      bs4 = bs(faucet.text, "html.parser")
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
def earnrub_pw(modulesl,banner):
  vie_script(modulesl,banner,url="https://earnrub.pw/",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=True,short=True,faucet=True,auto=True)
def whoopyrewards(modulesl,banner):
  vie_script(modulesl,banner,url="https://whoopyrewards.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
def faucet_mom(modulesl,banner):
  vie_script(modulesl,banner,url="https://faucet.mom",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def instanfaucet_xyz(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://insfaucet.xyz/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    instanfaucet_xyz(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  hd=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
  ua_p=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","application/x-www-form-urlencoded")
  curl=requests.Session()
  dash=curl.get("https://insfaucet.xyz/dashboard",headers=hd,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(name=host)
    instanfaucet_xyz(modulesl,banner)
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
def eurofaucet_de(modulesl,banner):
  vie_script(modulesl,banner,url="https://eurofaucet.de/",key_re="6Lcza1QmAAAAAInStIpZuJYEOm-89v4zKNzglgU9",ptc=True,short=True,faucet=True,auto=True)
def gulio(modulesl,banner):
  vie_script(modulesl,banner,url="https://gulio.site/",key_re="6Lcza1QmAAAAAInStIpZuJYEOm-89v4zKNzglgU9",ptc=False,short=True,faucet=False,auto=True)
def cryptask(modulesl,banner):
  vie_script(modulesl,banner,url="https://cryptask.xyz/",key_re="6Lcza1QmAAAAAInStIpZuJYEOm-89v4zKNzglgU9",ptc=False,short=True,faucet=False,auto=True)
def james_trussy(modulesl,banner):
  vie_script(modulesl,banner,"https://james-trussy.com/","6Ler3E4kAAAAABUDc4UE9UWO7k_n2JydShddSpCO",ptc=False,short=True,faucet=False,auto=True)
def earn_crypto(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner("EARN_CRYPTO")
  data_control('earn_crypto')
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'cache/earn_crypto/{i}.jpg')
          file_sizes.append(file_size)
      for i in range(5):
          if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
              return i
      return None
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
      print(gt_cp.text)
      status_code(gt_cp)
      hash = eval(gt_cp.text)
      gt = {
          'user-agent': ugentmu,
          'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
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
    save_data('earn_crypto')
    earn_crypto(modulesl,banner)
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
    save_data('earn_crypto')
    earn_crypto(modulesl,banner)
  try:
    akun=Tree("[green] > [yellow]Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      akun.add('[green]> [yellow]'+info.text.strip())
    rprint(akun)
  except Exception as e:
    save_data('earn_crypto')
    earn_crypto(modulesl,banner)
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
      print(answer)
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
                          animasi(detik=105)
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
def earnbits(modulesl,banner):
  bits_family(modulesl,banner,host='earnbits.io', recaptcha_key='6LcJO3YnAAAAAODSQdQry4sVyosh5BT6YuYXQfW4',key_all_ptc=('button',{'class':'btn btn-success btn-sm w-100 mt-1'}),key_all_sl=('div',{'class':'col-xl-2 col-lg-3 col-sm-4 col-12 mb-4'}),key_button_id=('button',{'class':'btn btn-success btn-sm'}),key_amount_sl=('span', {'class': 'badge bg-label-info mb-4'}))
def nevcoin(modulesl,banner):
  bits_family(modulesl,banner,'nevcoins.club', '6Lfq4b4ZAAAAALs8lVypMYqUH5E8esL8B78wkA0Y',faucet='/claim.html',path_ptc='/ptc.html',key_all_ptc=('button', {'class': 'btn btn-success btn-sm w-100 mt-1'}),path_sl='/shortlinks.html',key_all_sl='tr',key_button_id=('button', {'class': 'btn btn-success btn-sm'}),key_amount_sl=('b', {'class': 'badge badge-dark'}))
def timps_co(modulesl,banner):
  def save_data(name,inp=False):
    if inp!=False:
      user_agent=inp
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
             data = json.load(file)
             cookies = data.get('auth')
             user_agent = data.get('data')
             if inp == False:
              cookies = input(hijau1 + 'Masukkan data mu > ')
              parsed_json = json.loads(cookies)
              hasil = json.dumps(parsed_json, indent=2)
              data = {
              #    'auth': cookies,
                  'data': hasil
              }
              with open(f'data/{name}/{name}.json', 'w') as file:
                  json.dump(data, file)
              return hasil
    except FileNotFoundError:
          if inp ==False:
              user_agent = input(hijau1 + 'Masukkan data mu > ')
              parsed_json = json.loads(user_agent)
              hasil = json.dumps(parsed_json, indent=2)
          data = {
              'data': hasil
          }
          with open(f'data/{name}/{name}.json', 'w') as file:
              json.dump(data, file)
          return user_agent
  def load_data(name):
      try:
          with open(f'data/{name}/{name}.json', 'r') as file:
              data = json.load(file)
          user_agent = data['data']
          parsed_json = json.loads(user_agent)
          formatted_json = json.dumps(parsed_json, indent=2)
          return formatted_json
      except FileNotFoundError:
          return None, None
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://timpsco.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  print(f"{hijau1}> {kuning1}1{putih1}. {hijau1}Start auto faucet")
  print(f"{hijau1}> {kuning1}2{putih1}. {hijau1}Start faucet")
  print(f"{hijau1}> {kuning1}3{putih1}. {hijau1}Start bypass shortlinks")
  print(f"{hijau1}> {kuning1}4{putih1}. {hijau1}Start bypass ptc wall")
  print(f"{hijau1}> {kuning1}5{putih1}. {hijau1}Start bypass ptc iframe")
  print(f"{hijau1}> {kuning1}6{putih1}. {hijau1}Start all")
  select=input(f"{hijau1}> {kuning1}select {putih1}: ")
  if select == '6':
    select=['1','2','3','4','5']
  os.system('cls' if os.name == 'nt' else 'clear')
  banner.banner(host.upper())
  data = load_data(host)
  refreshToken=data
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host,inp=False)
    timps_co(modulesl,banner)
  curl=requests.Session()
  auth=json.loads(data)["variables"]["input"]["token"]
  get_user={"operationName":"getUser","variables":{},"query":"query getUser {\n  getUser {\n    id\n    balance\n    credits\n    username\n    email\n    admin\n    status\n    createAt\n    log\n    xp\n    level\n    next_level\n    bonus_level\n    address_fp\n    bonus_loyalty\n    total_earn\n    statistics_earn {\n      id\n      clicks\n      total\n      __typename\n    }\n    __typename\n  }\n}\n"}
  ptc_wall={"operationName":"getAdsPtcWall","variables":{"offset":0,"limit":50},"query":"query getAdsPtcWall($offset: Int, $limit: Int) {\n  getAdsPtcWall(offset: $offset, limit: $limit) {\n    Ads {\n      id\n      title\n      description\n      url\n      duration\n      reward\n      __typename\n    }\n    total\n    __typename\n  }\n}\n"}
  urlbase='https://timpsco.in/graphql'
  hd={"authorization":auth,"content-type":"application/json"}
  try:
    refresh=curl.post(urlbase,headers=hd,data=json.dumps(json.loads(data))).json()
    if refresh["data"]["refreshToken"] == None:
      auth=auth
    else:
      auth=refresh["data"]["refreshToken"]["token"]
      hasil={"operationName":"refreshToken","variables":{"input":{"token":refresh["data"]["refreshToken"]["token"],"refresh_token":refresh["data"]["refreshToken"]['refresh_token']}},"query":"mutation refreshToken($input: TokenInput) {\n  refreshToken(input: $input) {\n    token\n    refresh_token\n    __typename\n  }\n}\n"}
      save_data(tele=None,name=host,inp=hasil)
    hd={"authorization":auth,"content-type":"application/json","referer":"https://timpsco.in/dashboard"}
    dash=curl.post(urlbase,headers=hd,data=json.dumps(get_user)).json()["data"]["getUser"]
  except Exception as e:
    save_data(tele=None,name=host,inp=False)
    timps_co(modulesl,banner)
  akun=Tree('[green]> [yellow]Account information')
  akun.add("[green]> [yellow]Username [white]: [green]"+dash['username'].capitalize())
  akun.add("[green]> [yellow]Balance [white]: [green]"+str(dash['balance']))
  akun.add("[green]> [yellow]Credits [white]: [green]"+str(dash['credits']))
  akun.add("[green]> [yellow]Status [white]: [green]"+str(dash['status']))
  akun.add("[green]> [yellow]Level [white]: [green]"+str(dash['level']))
  rprint(akun)
  if '5' in select:
    rprint(Tree('[green]> [yellow]Start ptc iframe'))
    hd["referer"]="https://timpsco.in/surf-ads"
    hd["accept"]="*/*"
    hd["user-agent"]="Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
    while True:
     try:
      get_ads=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getAdsIframe","variables":{},"query":"query getAdsIframe {\n  getAdsIframe {\n    Ads {\n      id\n      title\n      description\n      url\n      duration\n      reward\n      __typename\n    }\n    total\n    __typename\n  }\n}\n"})).json()["data"]["getAdsIframe"]["Ads"]
      if len(get_ads) == 0 :break
      tipe=type(get_ads)
      if str(tipe)=="<class 'list'>":
        get_ads=get_ads[0]
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+parser(get_ads['description'].strip().splitlines()[0]),end=end())
      persen(get_ads['duration'])
      answer=modulesl.RecaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeYZ-klAAAAAAK1EqWByGrbLomW6Z8LPuCuZWoO&co=aHR0cHM6Ly90aW1wc2NvLmluOjQ0Mw..&hl=id&type=image&v=lLirU0na9roYU3wDDisGJEVT&theme=light&size=invisible&badge=bottomright&cb=h86erc1sf0c')
      print(answer)
      verify=curl.post(urlbase,headers=hd,data=json.dumps(      {"operationName":"earnAds","variables":{"id":get_ads["id"],"token":answer},"query":"mutation earnAds($id: ID!, $token: String) {\n  earnAds(id: $id, token: $token) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    result\n    notification\n    __typename\n  }\n}\n"})).json()
      print(verify)
      res=verify["data"]['earnAds']['user']
      if res!=None:
        print(putih1+'├──'+'─'*56)
        sukses=Tree('[white]├── [green]> [yellow]Succes ptc iframe')
        sukses.add('[green]Balance [white]> [yellow]'+str(res["balance"]))
        sukses.add('[green]level [white]> [yellow]'+str(res["level"]))
        rprint(sukses)
     except Exception as e:
       keluar(str(e))
       pass
    print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc iframe!')
  if '4' in select:
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
  if '3' in select:
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
    print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  if '1' in select:
    rprint(Tree('[green]> [yellow]Start auto faucet'))
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
  if '2' in select:
    print(f"{hijau1}> {kuning1}1{putih1}. {hijau1}Random Coin (Bawaan web)")
    print(f"{hijau1}> {kuning1}2{putih1}. {hijau1}Target Coin (BruteForce)")
    pilih=input(f"{hijau1}> {kuning1}select {putih1}: ")
    if pilih == '2':
      crypto_dict = {
      "DigiByte": "digibyte",
      "USD Coin": "usd-coin",
      "Solana": "solana",
      "Shiba Inu": "shiba-inu",
      "Dogecoin": "dogecoin",
      "TRON": "tron",
      "Polygon": "matic-network",
      "Litecoin": "litecoin",
      "XRP": "ripple",
      "Ethereum": "ethereum",
      "Bitcoin": "bitcoin",
      "Zcash": "zcash",
      "Aave": "aave",
      "Binance USD": "binance-usd",
      "Dash": "dash",
      "BNB": "binancecoin",
      "Tether": "tether",
      "Bitcoin Cash": "bitcoin-cash"
      }
      nomor=0
      value=list(crypto_dict.values())
      for nama,values in crypto_dict.items():
        print(f"{hijau1}> {kuning1}{str(nomor)}{putih1}. {hijau1}{nama}")
        nomor+=1
      select=input(f"{hijau1}> {kuning1}select {putih1}: ")
      select = value[int(select)]
    refresh=curl.post(urlbase,headers=hd,data=json.dumps(json.loads(refreshToken))).json()
    if refresh["data"]["refreshToken"] == None:
      auth=auth
    else:
      auth=refresh["data"]["refreshToken"]["token"]
      hasil={"operationName":"refreshToken","variables":{"input":{"token":refresh["data"]["refreshToken"]["token"],"refresh_token":refresh["data"]["refreshToken"]['refresh_token']}},"query":"mutation refreshToken($input: TokenInput) {\n  refreshToken(input: $input) {\n    token\n    refresh_token\n    __typename\n  }\n}\n"}
      save_data(tele=None,name=host,inp=hasil)
    hd={"authorization":auth,"content-type":"application/json","referer":"https://timpsco.in/autofaucet"}
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner(host.upper()+' all Faucet')
    while True:
      hd={"authorization":auth,"content-type":"application/json","referer":"https://timpsco.in/faucet"}
      faucet_game=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"earnRollGame","variables":{"token":"token_recaptcha"},"query":"mutation earnRollGame($token: String) {\n  earnRollGame(token: $token) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    result\n    luckyNumber\n    notification\n    __typename\n  }\n}\n"})).json()
      #print(str(faucet_game))
      if "'luckyNumber': None," in str(faucet_game):
        get_bal=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getUserCoins","variables":{},"query":"query getUserCoins {\n  getUserCoins {\n    id\n    sigla\n    balance\n    id_coin\n    id_user\n    user_address {\n      address\n      network\n      __typename\n    }\n    __typename\n  }\n}\n"})).json()
        print(putih1+'├──'+hijau1+f' {kuning1}Claim {putih1}> {hijau1} Faucet                      ')
        print(putih1+'├──'+hijau1+f' {kuning1}Message {putih1}> failed to claim the faucet you have to wait for the timer to finish      ')
        for coin in get_bal["data"]["getUserCoins"]:
          print(putih1+'├──'+hijau1+f' {kuning1}'+coin["id_coin"]+f' {putih1}> {hijau1}'+str(coin["balance"]))
      else:
        get_bal=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getUserCoins","variables":{},"query":"query getUserCoins {\n  getUserCoins {\n    id\n    sigla\n    balance\n    id_coin\n    id_user\n    user_address {\n      address\n      network\n      __typename\n    }\n    __typename\n  }\n}\n"})).json()
        res=faucet_game["data"]["earnRollGame"]["result"].split(" ")
        
        print(putih1+'├──'+hijau1+f' {kuning1}Claim {putih1}> {hijau1} Faucet                      ')
        print(putih1+'├──'+hijau1+f' {kuning1}Message {putih1}> {hijau1}{res[0]} You win {res[1]} TIMPS                      ')
        for coin in get_bal["data"]["getUserCoins"]:
          print(putih1+'├──'+hijau1+f' {kuning1}'+coin["id_coin"]+f' {putih1}> {hijau1}'+str(coin["balance"]))
      refresh=curl.post(urlbase,headers=hd,data=json.dumps(json.loads(refreshToken))).json()
      if refresh["data"]["refreshToken"] == None:
        auth=auth
      else:
        auth=refresh["data"]["refreshToken"]["token"]
        hasil={"operationName":"refreshToken","variables":{"input":{"token":refresh["data"]["refreshToken"]["token"],"refresh_token":refresh["data"]["refreshToken"]['refresh_token']}},"query":"mutation refreshToken($input: TokenInput) {\n  refreshToken(input: $input) {\n    token\n    refresh_token\n    __typename\n  }\n}\n"}
        save_data(tele=None,name=host,inp=hasil)
      hd={"authorization":auth,"content-type":"application/json","referer":"https://timpsco.in/dashboard/lucky-game"}
      status = False
      while(status==False):
        if pilih == '2':
          fauct=None
          while True:
            faucet_game=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getTypeCoinLuckyGame","variables":{},"query":"query getTypeCoinLuckyGame {\n  getTypeCoinLuckyGame {\n    id\n    name\n    sigla\n    value\n    image\n    earn\n    id_coin\n    price\n    clicks\n    __typename\n  }\n}\n"})).json()["data"]["getTypeCoinLuckyGame"]
            for coin in faucet_game:
              if coin['earn'] != 0:
                if select == coin['id_coin']:
                  fauct={
            "operationName": "earnLuckyGame",
            "variables": {
              "input": {
                "id": coin["id"],
                "sigla": coin['sigla'],
                "earn": coin['earn'],
                "id_coin": coin['id_coin'],
                "price": coin['price'],
                "token_recaptcha": "asdasdasda"
              }
            },
            "query": "mutation earnLuckyGame($input: TypeCoinLuckyGameInput) {\n  earnLuckyGame(input: $input) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    result\n    luckyNumber\n    notification\n    __typename\n  }\n}\n"
            }
                  break
            if fauct is not None:
              break
        elif pilih == '1':
            faucet_game=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getTypeCoinLuckyGame","variables":{},"query":"query getTypeCoinLuckyGame {\n  getTypeCoinLuckyGame {\n    id\n    name\n    sigla\n    value\n    image\n    earn\n    id_coin\n    price\n    clicks\n    __typename\n  }\n}\n"})).json()["data"]["getTypeCoinLuckyGame"]
            for coin in faucet_game:
              if coin['earn'] != 0:
                  fauct={
            "operationName": "earnLuckyGame",
            "variables": {
              "input": {
                "id": coin["id"],
                "sigla": coin['sigla'],
                "earn": coin['earn'],
                "id_coin": coin['id_coin'],
                "price": coin['price'],
                "token_recaptcha": "asdasdasda"
              }
            },
            "query": "mutation earnLuckyGame($input: TypeCoinLuckyGameInput) {\n  earnLuckyGame(input: $input) {\n    user {\n      id\n      balance\n      credits\n      username\n      email\n      admin\n      status\n      createAt\n      log\n      xp\n      level\n      next_level\n      bonus_level\n      address_fp\n      bonus_loyalty\n      total_earn\n      statistics_earn {\n        id\n        clicks\n        total\n        __typename\n      }\n      __typename\n    }\n    result\n    luckyNumber\n    notification\n    __typename\n  }\n}\n"
            }
                  break
        faucet_game=curl.post(urlbase,headers=hd,data=json.dumps(fauct)).json()
        if 'error' in str(faucet_game):
          print(putih1+'├──'+hijau1+f' {kuning1}Message {putih1}> '+faucet_game["errors"][0]['message'],end=end())
        else:
          print(putih1+'├──'+'─'*56)
          get_bal=curl.post(urlbase,headers=hd,data=json.dumps({"operationName":"getUserCoins","variables":{},"query":"query getUserCoins {\n  getUserCoins {\n    id\n    sigla\n    balance\n    id_coin\n    id_user\n    user_address {\n      address\n      network\n      __typename\n    }\n    __typename\n  }\n}\n"})).json()
          print(putih1+'├──'+hijau1+f' {kuning1}Claim {putih1}> {hijau1} Faucet Game                      ')
          print(putih1+'├──'+hijau1+f' {kuning1}Message {putih1}> {hijau1} Ok                      ')
          for coin in get_bal["data"]["getUserCoins"]:
            print(putih1+'├──'+hijau1+f' {kuning1}'+coin["id_coin"]+f' {putih1}> {hijau1}'+str(coin["balance"]))
          status=True
      animasi(menit=30)
      print(putih1+'├──'+'─'*56)
def vie_faucet(modulesl,banner):
  def save_data(name,inp=False):
    if inp!=False:
      user_agent=inp
    try:
        with open(f'data/{name}/{name}.json', 'r') as file:
             data = json.load(file)
             cookies = data.get('auth')
             user_agent = data.get('data')
             if inp == False:
              cookies = input(hijau1 + 'Masukkan auth mu > ')
              data = {
              #    'auth': cookies,
                  'data': cookies
              }
              with open(f'data/{name}/{name}.json', 'w') as file:
                  json.dump(data, file)
              return cookies
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
              user_agent = input(hijau1 + 'Masukkan auth mu > ')
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
  host=urlparse("https://viefaucet.com/").netloc
  data_control(host)
  banner.banner(host.upper())
  auth = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(tele=None,name=host,inp=False)
    vie_faucet(modulesl,banner)
  curl=requests.Session()
  headers={
    "Host":"api.viefaucet.com",
    "accept":"application/json, text/plain, */*",
    "authorization":auth,
    "User-Agent":"XYZ/3.0"
  }
  try:
    dash=curl.get("https://api.viefaucet.com/api/user/me",headers=headers).json()["user"]
  except Exception as e:
    save_data(tele=None,name=host,inp=False)
    vie_faucet(modulesl,banner)
    
  akun=Tree('[green]> [yellow]Account information')
  akun.add("[green]> [yellow]Username [white]:[green] "+dash["username"])
  akun.add("[green]> [yellow]Balance [white]:[green] "+str(dash["balance"]))
  akun.add("[green]> [yellow]Level [white]:[green] "+str(dash["level"]))
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start shortlinks"))
  sl=curl.get("https://api.viefaucet.com/api/link",headers=headers).json()["links"]
  for link in sl:
   try:
    _id=link["_id"]
    jumlah=link['maxView']
    re=jumlah
    for jum in range(jumlah):
      get_link=curl.get("https://api.viefaucet.com/api/link/"+_id,headers={
    "Host":"api.viefaucet.com",
    "accept":"application/json, text/plain, */*",
    "authorization":auth,
    "User-Agent":"XYZ/3.0",
    "referer":"https://viefaucet.com/app/link"
  }).json()
      
      if 'Oops! You are clicking too fast'in str(get_link):sleep(15)
      if 'msg'in str(get_link):break
      answer=bypass_link(get_link["result"],modulesl,jumlah=[str(re),str(jumlah)])
      if answer==False:break
      elif 'failed to bypass' in answer:pass
      else:
        animasi(detik=105)
        id_answer=answer.split('/app/link/')[1]
        reward=curl.post('https://api.viefaucet.com/api/link/verify',data=json.dumps({"secret":id_answer}),headers={
    "Host":"api.viefaucet.com",
    "accept":"application/json, text/plain, */*",
    "authorization":auth,
    "User-Agent":"XYZ/3.0",
    "content-type":"application/json"
  }).json()
        print(putih1+'├── '+hijau1+reward["msg"])
        re-=1
    sleep(5)
   except Exception as e:
     keluar(str(e))
     pass
def cryptoearns(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://cryptoearns.com/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    cryptoearns(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    'User-Agent': ugentmu,
    
  }
  curl=requests.Session()
  dash=curl.get('https://cryptoearns.com/dashboard',headers=ua,cookies=cookies)
  if "Account Balance" not in dash.text:
    save_data(host)
    cryptoearns(modulesl,banner)
  status_code(dash)
  akun=Tree("[green]> [yellow]Account information")
  info=bs(dash.text,'html.parser').find_all('div',{'class':'finance_card'})
  for info in info:
    info_text=info.text.strip().replace('\n',' : ')
    akun.add("[green]> [yellow]"+info_text.split(":")[1].strip() + " [white]: [yellow]" + info_text.split(":")[0].strip())
  rprint(akun)
  ptc=curl.get('https://cryptoearns.com/ptc',headers=ua,cookies=cookies)
  status_code(ptc)
  rprint(Tree("[gree] > [yellow]Start ptc"))
  ads=bs(ptc.text,'html.parser').find_all('div',{'class':'col-lg-6'})
  for ads in ads:
   try:
    if 'window.location' not in str(ads):pass
    else:
      name=parser(ads.find('h5').text.strip())
      url=ads.find('button',{'class':'claim-btn w-100 text-white'})['onclick'].split("= '")[1].split("'")[0]
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end=' '*20+'\r')
      view=curl.get(url,headers=ua,cookies=cookies)
      status_code(view)
      token=bs(view.text,'html.parser').find('input',{'name':'token'})['value']
      animasi(detik=int(view.text.split('let timer = ')[1].split(';')[0]))
      answer=modulesl.RecaptchaV2('6Lf0_KonAAAAAPgw0s0gneoF_o-_pQ-BY9PdOfVa',url)
      ua["content-type"]="application/x-www-form-urlencoded"
      data=f"captcha=recaptchav2&g-recaptcha-response={answer}&ci_csrf_token=&token={token}"
      reward=curl.post(url.replace('view','verify'),headers=ua,cookies=cookies,data=data)
      status_code(reward)
      if 'Good job!' in reward.text:
        print(putih1+'├── '+hijau1+"Good job! "+reward.text.split("text: '")[1].split("balance',")[0]+"balance.")
   except Exception as e:
    keluar(str(e))
    pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  ptc=curl.get('https://cryptoearns.com/ptc/ptcwindow',headers=ua,cookies=cookies)
  status_code(ptc)
  rprint(Tree("[gree] > [yellow]Start ptc window"))
  ads=bs(ptc.text,'html.parser').find_all('div',{'class':'col-lg-6'})
  for ads in ads:
   try:
    if 'window.location' not in str(ads):pass
    else:
      name=parser(ads.find('h5').text.strip())
      url=ads.find('button',{'class':'claim-btn w-100 text-white'})['onclick'].split("= '")[1].split("'")[0]
      print(putih1+'├──'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+name,end=' '*20+'\r')
      view=curl.get(url,headers=ua,cookies=cookies)
      status_code(view)
      token=bs(view.text,'html.parser').find('input',{'name':'token'})['value']
      animasi(detik=int(view.text.split('startview(')[1].split(',')[0]))
      answer=modulesl.RecaptchaV2('6Lf0_KonAAAAAPgw0s0gneoF_o-_pQ-BY9PdOfVa',url)
      ua["content-type"]="application/x-www-form-urlencoded"
      ua["referer"]=url
      data=f"captcha=recaptchav2&g-recaptcha-response={answer}&ci_csrf_token=&token={token}"
      reward=curl.post(url.replace('wview','verifywindow'),headers=ua,cookies=cookies,data=data)
      status_code(reward)
      if 'Good job!' in reward.text:
        print(putih1+'├── '+hijau1+"Good job! "+reward.text.split("text: '")[1].split("balance',")[0]+"balance.")
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc window!')
  sl=curl.get('https://cryptoearns.com/links',headers=ua,cookies=cookies)
  status_code(sl)
  rprint(Tree("[gree] > [yellow]Start shortlinks"))
  sl=bs(sl.text,'html.parser').find_all('div',{'class':'col-lg-6'})
  for sl in sl:
   try:
    url=sl.find('a')['href']
    jumlah=int(sl.find_all('div',{'class':'pil me-2'})[1].text.strip().split('/')[0])
    re=jumlah
    for ulang in range(re):
      link=curl.get(url,headers=ua,cookies=cookies,allow_redirects=False).text.split('<script> location.href = "')[1].split('"; </script>')[0]
      answer=bypass_link(link,modulesl,jumlah=[str(re),str(jumlah)])
      if answer==False:break
      if answer=="failed to bypass":pass
      else:
        animasi(detik=105)
        reward=curl.get(answer,headers=ua,cookies=cookies)
        status_code(reward)
        if 'Good job!' in reward.text:
          print(putih1+'├── '+hijau1+"Good job! "+reward.text.split("text: '")[1].split("balance',")[0]+"balance.")
          re-=1
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet"))
  while True:
   try:
    auto=curl.get('https://cryptoearns.com/auto',headers=ua,cookies=cookies)
    status_code(auto)
    animasi(detik=int(auto.text.split('let timer = ')[1].split(',')[0]))
    data="token="+bs(auto.text,'html.parser').find('input',{'name':'token'})['value']
    ua["content-type"]="application/x-www-form-urlencoded"
    verify=curl.post('https://cryptoearns.com/auto/verify',headers=ua,cookies=cookies,data=data)
    if 'Good job!' in verify.text:
          print(putih1+'├── '+hijau1+"Good job! "+verify.text.split("text: '")[1].split("balance',")[0]+"balance.")
   except Exception as e:
      keluar(str(e))
      break
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more auto faucet!')
def faucetpayz(modulesl,banner):
  bits_family(modulesl,banner,'faucetpayz.com', '6Lfl5TQoAAAAAMVgZSFFFj7OUojEHgcO2tqfaRC0')
def paidlink(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://paidlink.pro/").netloc
  data_control(host)
  banner.banner(host.upper())
  email = load_data(host,custom=['email'])["email"]
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    paidlink(modulesl,banner)
  curl=requests.Session()
  headers={
    "Host":"paidlink.pro",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0"
  }
  get=curl.get('https://paidlink.pro/referral/9265',headers=headers)
  ua={
    "Host":"paidlink.pro",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0",
    "content-type":"application/x-www-form-urlencoded"
  }
  login=curl.post('https://paidlink.pro/login',data='email='+email,headers=ua)
  if 'invite your friend and earn 25% commission' in login.text:
    print(hijau1+'Login success ✓')
    bsi=bs(login.text,'html.parser')
    coin=bsi.find_all('td')
    data_coins=[]
    for coins in coin:
      if '/change-coin/' in str(coins):
        data_coins.append(coins)
    i=0
    for coins in data_coins:
      print(putih1+'[ '+hijau1+str(i)+putih1+' ] '+putih1+coins.find('img')['alt'])
      i+=1
    run=int(input(putih1+'[ '+kuning1+'?'+putih1+' ] '+ 'Input » '))
    change=curl.get('https://paidlink.pro'+data_coins[run].find('a')['href'],headers=headers)
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://paidlink.pro/").netloc
    data_control(host)
    banner.banner(host.upper())
    get_all_sl=bs(change.text,'html.parser').find_all('div',{'class':'col-md-3'})
    rprint(Tree("[green]> [yellow]Start bypass shortlinks"))
    for sl in get_all_sl:
      try:
        if 'reward' in sl.text:
          jumlah=int(sl.find('span',{'class':'desc'}).text.split('views left : ')[1].split('/')[0])
          url=sl.find('a',{'class':'btn btn-primary'})['href']
          re=jumlah
          for jum in range(jumlah):
            get_url=curl.get('https://paidlink.pro/'+url,headers=headers,allow_redirects=False).headers['location']
            answer=bypass_link(get_url,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if answer=='failed to bypass':
                pass
              else:
                animasi(detik=105)
                get_reward=curl.get(answer,headers=headers)
                if 'You have successfully completed the shortlink' in get_reward.text:
                  print(putih1+'├── '+hijau1+bs(get_reward.text,'html.parser').find('div',{'class':'alert alert-success alert-dismissible'}).text.strip())
      except Exception as e:
        keluar(str(e))
        pass