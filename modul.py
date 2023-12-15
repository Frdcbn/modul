#-------- import module ----------#
import requests,json,time,asyncio,re,shutil,os,random,pathlib,subprocess,traceback
from threading import Thread
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
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
#----------- color ---------------#
hijau1 = "\033[1;92m"
kuning1 = "\033[1;93m"
putih1 = "\033[1;97m"
merah1 = "\033[1;91m"
biru1 = "\033[1;94m"
#----------- module ---------------#
def Session():
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
def captcha(modulesl,html,key,key_re,url):
  answer={}
  def v3(key,url):
    answer['v3']=modulesl.RecaptchaV3ai(key,url)
  def antibot(html,key):
    answer['antibot']=modulesl.antibot(html,key)
  thread = []
  for t in [Thread(target=v3,args=(key_re,url,)), Thread(target=antibot,args=(html,key,))]:
     t.start()
     thread.append(t)
  for t in thread:
     t.join()
  return answer
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
def bypass_link(url,modulesl,jumlah=None):
  dictnya={
  "urlpay.in":modulesl.urlpay,
  "teralinks.in":modulesl.teralinks,
  "rsshort.com":modulesl.rsshort,
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
  "botfly.me":modulesl.botfly,
  "forexly.cc":modulesl.botfly,
  "goldly.cc":modulesl.botfly,
  "insurancly.cc":modulesl.botfly,
  "terafly.me":modulesl.botfly,
  "linkdam.me":modulesl.botfly,
  }
  if urlparse(url).netloc in dictnya:
    print(putih1+'├──'+'─'*56)
    if jumlah:
      print(f"├── {putih1}[{kuning1}{jumlah[0]}/{jumlah[1]}{putih1}] {kuning1} Bypassing : {hijau1}{url}")
    else:
      print(f"├── {putih1}{kuning1}Bypassing : {hijau1}{url}")
    res=dictnya[urlparse(url).netloc](url)
    if "failed to bypass" in res:
      print(putih1+'├── '+kuning1+'Status : '+merah1+res)
      print(putih1+'├──'+'─'*56)
    else:
      print(putih1+'├── '+kuning1+'Status : '+hijau1+"success")
      print(putih1+'├──'+'─'*56)
      animasi(detik=45)
      return res
  else:
    return False
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
#--------------- bits family ---------------#
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
def bits_family(modulesl,banner,host, recaptcha_key,faucet=None,path_ptc='/ptc.html',key_all_ptc=('button', {'class': 'btn btn-success btn-sm w-100 mt-1'}),path_sl='/shortlinks.html',key_all_sl=('tr'),key_button_id=('button', {'class': 'btn btn-success btn-sm'}),key_amount_sl=('b', {'class': 'badge badge-dark'}),run=None,ptc1=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner(host.upper())
    data_control(name=host)
    cookies, ugentmu = load_data(host)
    if not os.path.exists(f"data/{host}/{host}.json"):
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1)
    cookiek = SimpleCookie()
    cookiek.load(cookies)
    cookies = {k: v.value for k, v in cookiek.items()}
    ua = {
        "Host": host,
        'User-Agent': ugentmu,
    }
    curl=Session()
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
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1)
    try:
        akun = Tree("[green]> [yellow]Account information")
        get_inf = bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})
        for info in get_inf:
            akun.add('[green]> [yellow]' + info.text.strip())
        rprint(akun)
    except Exception as e:
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1)
    def balance():
        get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
        status_code(get_sl)
        return bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})[0].text.strip()
    if run == '1':
      if ptc1 == 'Off':
        print('Ptc off')
        pass
      else:
        ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl)
    if run == '2':
      sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
    if run == '3':
      if faucet=='Off':
        print('Faucet off')
        animasi(menit=1440)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1)
      rprint(Tree("[green]> [yellow]Bypass faucet"))
      if faucet:fauceturl=f'https://{host}/{faucet}'
      else:fauceturl=f'https://{host}/'
      while True:
        try:
            get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
            if 'Faucet Locked!' in get_sl.text:
              if 'You must visit' in get_sl.text:
                print(bs(get_sl.text,'html.parser').find('div',{'class':'alert alert-warning'}).text.strip())
                sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1)
              else:
                animasi(menit=1440)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1)
            if 'Just a moment...' in get_sl.text:
              save_data(host)
              bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1)
            waktu=get_sl.text.split('<h1 class="text-warning"><i class="fa fa-arrow-down"></i>')[1].split(' minutes')[0].split('every ')[1]
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
      if ptc1 == 'Off':
        print('Ptc off')
      else:
        ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl)
      sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl)
      if faucet=='Off':
        print('Faucet off')
        animasi(menit=1440)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1)
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
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1)
              else:
                animasi(menit=1440)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1)
            if 'Just a moment...' in get_sl.text:
              save_data(host)
              bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1)
            waktu=get_sl.text.split('<h1 class="text-warning"><i class="fa fa-arrow-down"></i>')[1].split(' minutes')[0].split('every ')[1]
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
def ptctask(modulesl,banner):
  bits_family(modulesl,banner,'ptctask.com', '6LcT7PYjAAAAAMTSJHtUEXXG2Zs9r18512T0CYsd')
def litecoinbits(modulesl,banner):
  bits_family(modulesl,banner,'litecoinbits.com', '6LfE8WgnAAAAAFqYciThoOD3f8VVLaLXnwTmQlWr',path_sl='/?page=shortlinks',path_ptc='/?page=ptc')
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
def proearn(modulesl,banner):
  bits_family(modulesl,banner,'proearn.site', '6LcXEsIaAAAAAKEMIqgfoqCiBrHGAjmkfwgkfcQr',faucet='Off',ptc1='Off')
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
  curl=Session()
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
def faucetpayz(modulesl,banner):
  bits_family(modulesl,banner,'faucetpayz.com', '6Lfl5TQoAAAAAMVgZSFFFj7OUojEHgcO2tqfaRC0')
#--------------- vie family ---------------#
def vie_script(modulesl,banner,url,key_re,ptc=False,short=False,faucet=False,auto=False,link=None,name_key=None):
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
  curl=Session()
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
    if 'shortlinks' not in get_links.text.lower():
      save_data(name=host)
      vie_script(modulesl,banner,url,key_re,ptc, short,faucet,auto)
    else:
      fd=bs(get_links.text,'html.parser')
      if link:
        link=fd.find_all('div',{'class':link})
      else:
        link=fd.find_all('div',{'class':'col-lg-3'})
      for i in link:
        try:
            jumlah = i.find('span',{'class':'badge badge-info'}).text.split('/')
            re=int(jumlah[0])
            for ulang in range(int(jumlah[0])):
              try:
                for ytta in range(5):
                 try:
                  if 'pre_verify' in i.find('a')["href"]:
                    status=True
                    while(status==True):
                      url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies)
                      status_code(url)
                      ans=modulesl.antibot(url,key='alert alert-warning text-center',name_key=name_key)
                      if ans!='WRONG_RESULT':
                        data='antibotlinks=+'+ans+'&'
                        if 'csrf_token_name' in url.text:
                          csrf=bs(url.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
                          data=data+'csrf_token_name='+csrf+'&'
                        elif 'token' in url.text:
                          token=bs(url.text,'html.parser').find('input',{'name':'token'})['value']
                          data=data+'token='+token
                        url = curl.post(i.find('a')["href"].replace('pre_verify','go'), headers={'Host':host,'User-Agent':ugentmu,'content-type':'application/x-www-form-urlencoded','referer':i.find('a')["href"]},data=data, cookies=cookies,allow_redirects=False)
                        status_code(url)
                        status=False
                  else:
                    url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
                  status_code(url)
                  url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
                  answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah[1]])
                  if answer==False:break
                  if 'failed to bypass' in answer:
                      pass
                  else:
                      if urlparse(answer).netloc =='earnsolana.xyz':
                        answer=answer.replace('back','verify')
                      reward = curl.get(answer, headers=ua, cookies=cookies)
                      status_code(reward)
                      if 'Good job!' in reward.text:
                          print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                      else:
                          print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
                  re-=1
                  break
                 except Exception as e:
                  keluar(str(e))
                  pass
                if answer==False:break
              except Exception as e:
                keluar(str(e))
                pass
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
def keforcash(modulesl,banner):
  url='https://keforcash.com'
  key_re='6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn'
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
  curl=Session()
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
    link=fd.find_all('div',{'class':'col-12 col-md-6 col-xl-4'})
    for i in link:
      try:
          #name = i.find('h4').text
          jumlah = i.find('p',{'class':'mx-auto text-primary'}).text.split('/')
          re=int(jumlah[0])
          for ulang in range(int(jumlah[0])):
            try:
              url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
              status_code(url)
              url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
              answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah[1]])
              if answer==False:
                break
              if 'failed to bypass' in answer:
                  pass
              else:
                  if urlparse(answer).netloc =='earnsolana.xyz':
                    answer=answer.replace('back','verify')
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
      except Exception as e:
          keluar(str(e))
          pass
    print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
def claimcoin_in(modulesl,banner):
  vie_script(modulesl,banner,url="https://claimcoin.in/",key_re="6LfO65QlAAAAAE4tUQ1uwmXFMW1TvT5QxEDtrK25",ptc=False,short=True,faucet=False,auto=True)
def whoopyrewards(modulesl,banner):
  vie_script(modulesl,banner,url="https://whoopyrewards.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False,link='col-lg-4')
def liteearn(modulesl,banner):
  vie_script(modulesl,banner,url="https://liteearn.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
def cryptoviefaucet(modulesl,banner):
  vie_script(modulesl,banner,url="https://cryptoviefaucet.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
def claimcash(modulesl,banner):
  vie_script(modulesl,banner,url="https://claimcash.cc",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def bitupdate(modulesl,banner):
  vie_script(modulesl,banner,url="https://bitupdate.info",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True,name_key='div')
def litefaucet(modulesl,banner):
  vie_script(modulesl,banner,url="https://litefaucet.in",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def queenofferwall(modulesl,banner):
  vie_script(modulesl,banner,url="https://queenofferwall.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
def hatecoin(modulesl,banner):
  vie_script(modulesl,banner,url="https://hatecoin.me",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def nobitafc(modulesl,banner):
  vie_script(modulesl,banner,url="https://nobitafc.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def coin_4u(modulesl,banner):
  vie_script(modulesl,banner,url="https://coin-4u.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
#--------------- vie new family ---------------#
def chillfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://chillfaucet.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    chillfaucet(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  hd=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
  ua_p=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","application/x-www-form-urlencoded")
  curl=Session()
  dash=curl.get(f"https://{host}/dashboard",headers=hd,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(name=host)
    chillfaucet(modulesl,banner)
  get_info=bs(dash.text,"html.parser").find_all('div',{"class":"col-sm-6 layout-spacing"})
  akun=Tree("[green]> [yellow]Account information")
  for info in get_info:
    akun.add("[green]> [yellow]"+info.text.strip().replace("\n"," : "))
  rprint(akun)
  rprint(Tree("[green]> [yellow]Shortlinks"))
  sl=curl.get(f'https://{host}/links',headers=hd,cookies=cookies)
  status_code(sl)
  sl=bs(sl.text,"html.parser").find_all("div",{"class":"col-sm-4 layout-spacing"})
  for sl in sl:
   try:
    url=sl.find("center").find('a')["href"]
    jumlah=sl.find("span",{"class":"badge span-warning text-warning text-center"}).text.strip().split('/')
    re=int(jumlah[0])
    name=sl.find("h5").text
    for juml in range(int(jumlah[0])):
      for i in range(5):
       try:
        gt_links=curl.get(url,headers=hd,cookies=cookies,allow_redirects=False)
        status_code(gt_links)
        gt_links=gt_links.text.split('<script> location.href = "')[1].split('"; </script>')[0]
        answer=bypass_link(gt_links,modulesl,jumlah=[str(re),jumlah[1]])
        if answer==False:
          break
        if 'failed to bypass' in answer:
          pass
        else:
          reward=curl.get(answer,headers=hd,cookies=cookies)
          status_code(reward)
          if 'Good job!' in reward.text:
            print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
          re-=1
          break
       except:pass
      if answer==False:break
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
def insfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://insfaucet.xyz/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    chillfaucet(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  hd=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
  ua_p=ua(host,ugentmu,"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","application/x-www-form-urlencoded")
  curl=Session()
  dash=curl.get(f"https://{host}/dashboard",headers=hd,cookies=cookies)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data(name=host)
    chillfaucet(modulesl,banner)
  get_info=bs(dash.text,"html.parser").find_all('div',{"class":"col-sm-6 layout-spacing"})
  akun=Tree("[green]> [yellow]Account information")
  for info in get_info:
    akun.add("[green]> [yellow]"+info.text.strip().replace("\n"," : "))
  rprint(akun)
  rprint(Tree("[green]> [yellow]Shortlinks"))
  sl=curl.get(f'https://{host}/links',headers=hd,cookies=cookies)
  status_code(sl)
  sl=bs(sl.text,"html.parser").find_all("div",{"class":"col-sm-4 layout-spacing"})
  for sl in sl:
   try:
    url=sl.find("center").find('a')["href"]
    jumlah=sl.find("span",{"class":"badge span-warning text-warning text-center"}).text.strip().split('/')
    re=int(jumlah[0])
    name=sl.find("h5").text
    for juml in range(int(jumlah[0])):
      for ytta in range(5):
        try:
          gt_links=curl.get(url,headers=hd,cookies=cookies,allow_redirects=False)
          status_code(gt_links)
          gt_links=gt_links.text.split('<script> location.href = "')[1].split('"; </script>')[0]
          answer=bypass_link(gt_links,modulesl,jumlah=[str(re),jumlah[1]])
          if answer==False:
            break
          if 'failed to bypass' in answer:
            pass
          else:
            reward=curl.get(answer,headers=hd,cookies=cookies)
            status_code(reward)
            if 'Good job!' in reward.text:
              print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
            re-=1
            break
        except:pass
      if answer==False:break
   except Exception as e:
     keluar(str(e))
     pass
  print(putih1+'└──'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
#--------------- bithub family ---------------#
# captcha fields
# hcaptcha => hc
# rscaptcha => rs
# recaptchav2 => rev2
# recaptchav3 => rev3
# antibotlinks => atb
def bithub_family(modulesl,banner,url, captcha, key_cp=None,key_info=None,ptc=None,sl=None,auto=None,key_jumlah=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse(url).netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    bithub_family(modulesl,banner,url, captcha, key_cp,key_info,ptc,sl,auto,key_jumlah)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  ua={
    "Host":host,
    'User-Agent': ugentmu,
    
  }
  curl=Session()
  curl.headers.update(ua)
  curl.cookies.update(cookies)
  dash=curl.get(url+'/dashboard')
  if 'balance' not in dash.text.lower():
    save_data(name=host)
    bithub_family(modulesl,banner,url, captcha, key_cp,key_info,ptc,sl,auto,key_jumlah)
  akun=Tree("[gree] > [yellow] Account information")
  for info in bs(dash.text,'html.parser').find_all(*key_info):
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[1]+' [white]: [yellow]'+info.text.strip().splitlines()[0])
  rprint(akun)
  if ptc:
    rprint(Tree("[gree] > [yellow] Start ptc"))
    get_ptc=curl.get(url+'/ptc')
    if 'available' not in get_ptc.text.lower():
      save_data(name=host)
      bithub_family(modulesl,banner,url, captcha, key_cp,key_info,ptc,sl,auto,key_jumlah)
    ads=bs(get_ptc.text,'html.parser').find_all(*ptc)
    for ad in ads:
     try:
      view=curl.get(ad.find('button')['onclick'].split("'")[1].split("'")[0])
      animasi(detik=int(view.text.split('var timer = ')[1].split(';')[0]))
      bs4 = bs(view.text, "html.parser")
      inputs = bs4.find_all("input")
      data = "&".join([f"{input.get('name')}={input.get('value')}" for input in inputs])
      if captcha=='hc':
        answer=modulesl.hcaptcha(key_cp,ad.find('button')['onclick'].split("'")[1].split("'")[0])
        data='captcha=hcaptcha&'+data+'&h-captcha-response='+answer
      if captcha=='rev2':
        answer=modulesl.RecaptchaV2(key_cp,ad.find('button')['onclick'].split("'")[1].split("'")[0])
        data='captcha=recaptchav2&'+data+'&g-recaptcha-response='+answer
      verify=curl.post(ad.find('button')['onclick'].split("'")[1].split("'")[0].replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"})
      if 'Good job!' in verify.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
      # if captcha=='rs':
      #   cache_control(host)
      #   print('https://rscaptcha.com/captcha/getimage?token='+bs4.find('input',{'name':'rscaptcha_token'})['value'])
      #   get_img=requests.get('https://rscaptcha.com/captcha/getimage?token='+bs4.find('input',{'name':'rscaptcha_token'})['value'],headers = {"Host": "rscaptcha.com","user-Agent": ugentmu,"Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "no-cors","Sec-Fetch-Dest": "image","referer":host}, stream=True)
      #   status_code(get_img)
      #   with open(f'cache/{host}/cache.png', 'wb') as f:
      #       shutil.copyfileobj(get_img.raw, f)
      #   #answer=modulesl.RecaptchaV2(key_cp,ad.find('button')['onclick'].split("'")[1].split("'")[0])
      #   #data='captcha=rscaptcha&'+data+'&rscaptcha_response='+answer
     except Exception as e:
          keluar(str(e))
          pass
  if sl:
    rprint(Tree("[gree] > [yellow] Start shortlinks"))
    sll=curl.get(url+'/links')
    if 'available' and 'shortlinks' not in sll.text.lower():
      save_data(name=host)
      bithub_family(modulesl,banner,url, captcha, key_cp,key_info,ptc,sl,auto,key_jumlah)
    status_code(sll)
    links=bs(sll.text,'html.parser').find_all(*sl)
    url1=url
    for link in links:
      try:
        if url1=='https://1xbitcoins.com':
          jumlah=link.find(*key_jumlah)['data-view']
          re=int(jumlah)
        if url1=='https://feyorra.top':
          jumlah=link.find_all(*key_jumlah)[1].text.strip().split('/')[1]
          re=int(jumlah)
        elif key_jumlah:
          jumlah=link.find(*key_jumlah).text.strip().split('/')[1]
          re=int(jumlah)
        else:
          jumlah=link.find('span',{'class':'badge badge-info'}).text.strip().split('/')[1]
          re=int(jumlah)
        for i in range(re):
          try:
            for ytta in range(5):
              try:
                url = curl.get(link.find('a')["href"],allow_redirects=False)
                status_code(url)
                url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
                answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah])
                if answer==False:
                  break
                if 'failed to bypass' in answer:
                    pass
                else:
                    reward = curl.get(answer)
                    status_code(reward)
                    if 'Good job!' in reward.text:
                        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                    else:
                        print(putih1+'├──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
                re-=1
                break
              except Exception as e:
                  keluar(str(e))
                  pass
            if answer==False:
                      break
          except Exception as e:
              keluar(str(e))
              pass
      except Exception as e:
          keluar(str(e))
          pass
  if auto:
    rprint(Tree("[green]> [yellow]Start auto faucet"))
    while True:
     try:
      get_=curl.get(f'https://{host}/auto')
      status_code(get_)
      bs4 = bs(get_.text, "html.parser")
      inputs = bs4.find_all("input")
      data = "&".join([f"{input.get('name')}={input.get('value')}" for input in inputs])
      animasi(detik=int(get_.text.split('let timer = ')[1].split(',')[0]))
      reward=curl.post(f'https://{host}/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},data=data)
      status_code(reward)
      if 'Good job!' in reward.text:
        print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
     except Exception as e:
       print(putih1+'└──'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy!')
       break
  exit()
def tartaria_faucet(modulesl,banner):
  bithub_family(modulesl,banner,'https://tartaria-faucet.net', captcha='hc', key_cp='5bba62cc-f41b-47cd-8927-dc2e576e3a5c',key_info=('div',{'class':'col-md-6 col-xl-3'}),ptc=('div',{'class':'col-lg-6 col-xl-4'}),sl=('div',{'class':'card-lg claim-card'}),auto=True)
def feyorra(modulesl,banner):
  bithub_family(modulesl,banner,'https://feyorra.top', captcha='hc', key_cp='5bba62cc-f41b-47cd-8927-dc2e576e3a5c',key_info=('div',{'class':'col-lg-3 col-md-6'}),sl=('div',{'class':'col-md-6 col-lg-4 mb-3 mb-lg-0'}),key_jumlah=('span',{'class':'badge bg-info'}))
def _1xbitcoins(modulesl,banner):
  bithub_family(modulesl,banner,'https://1xbitcoins.com', captcha='hc', key_cp='5bba62cc-f41b-47cd-8927-dc2e576e3a5c',key_info=('div',{'class':'col-lg-4'}),sl=('div',{'class':'viewads_heading'}),key_jumlah=('a',{'class':'view_ads_click'}))
#--------------- other family ---------------#
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
  curl=Session()
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
def coinpayz(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('coinpayz')
  banner.banner('COINPAYZ')
  cookies, ugentmu = load_data('coinpayz')
  if not os.path.exists("data/coinpayz/coinpayz.json"):
    save_data('coinpayz')
    coinpayz(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  headers = {
    'Host': 'coinpayz.xyz',
    'User-Agent': ugentmu,
  }
  curl=Session()
  curl.headers.update(headers)
  curl.cookies.update(cookies)
  td=f'{putih1}[ {merah1}× {putih1}] {hijau1}> {putih1}'
  dash=curl.get('https://coinpayz.xyz/dashboard',headers=headers)
  status_code(dash)
  if 'Balance' not in dash.text:
    save_data('coinpayz')
    coinpayz(modulesl,banner)
  print(td+'Account information')
  ds=bs(dash.text,'html.parser').find('div',class_='flex-grow-1')
  print(td+ds.text.strip().replace('\n',' : '))
  print(td+'start shortlinks')
  sl=curl.get('https://coinpayz.xyz/links')
  status_code(sl)
  sli=bs(sl.text,'html.parser').find_all('div',class_='card card-body text-center bg-metallic')
  for bp in sli:
   try:
    jumlah=int(bp.find('span',class_='badge badge-soft-info font-size-12').text.strip().split('/')[0])
    link=bp.find('a',class_='btn btn-info waves-effect waves-light')['href']
    re=jumlah
    for i in range(jumlah):
      try:
            get_links=curl.get(link,allow_redirects=False)
            status_code(get_links)
            links=get_links.text.split('<script> location.href = "')[1].split('";')[0]
            answer=bypass_link(links,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed' in answer:
                pass
              else:
                sukses=curl.get(answer)
                status_code(sukses)
                if 'Good job!' in sukses.text:
                  print(hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+sukses.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
                  re-=1
      except Exception as e:
       print(td+str(e))
   except Exception as e:
     print(td+str(e))
def wildfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  data_control('wildfaucet')
  banner.banner('WILDFAUCET')
  cookies, ugentmu = load_data('wildfaucet')
  if not os.path.exists("data/wildfaucet/wildfaucet.json"):
    save_data('wildfaucet')
    wildfaucet(modulesl,banner)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  headers = {
    'Host': 'wildfaucet.com',
    'User-Agent': ugentmu,
  }
  curl=Session()
  curl.headers.update(headers)
  curl.cookies.update(cookies)
  get_key=curl.get('https://wildfaucet.com/dash/').text.split("var apiKey = '")[1].split("';var")[0]
  data={'api_key':get_key}
  dash=curl.post('https://wildfaucet.com/em-assets/themes/default/dash/',data=data)
  if 'Balance' not in dash.text:
    save_data('wildfaucet')
    wildfaucet(modulesl,banner)
  info=bs(dash.text,'html.parser').find('div',class_='balance')
  akun=Tree("[green] > [yellow]Account information")
  akun.add('[yellow]'+info.text.strip().replace('\n',' : ').split('Satoshi : Withdrawal :  :  :  : Buy Balance')[0].replace(' : ',' [white]:[yellow] ')+' Satoshi')
  rprint(akun)
  rprint(Tree("[green] > [yellow]Start shortlinks"))
  sl=curl.post('https://wildfaucet.com/em-assets/themes/default/earn/sortlink/',data=data)
  links=bs(sl.text,'html.parser').find_all('div',class_='em_short')
  for link in links:
    jumlah=link.find('a').text.strip().split('Claim (')[1].split('/')
    if jumlah[0] != '0':
      jumlah=int(eval(jumlah[1].split(')')[0]+'-'+jumlah[0]))
    else:
      jumlah=int(jumlah[1].split(')')[0])
    re=jumlah
    url=link.find('a',class_='btn')['href']
    for i in range(jumlah):
     try:
      uri=curl.get(url,allow_redirects=False)
      uri=uri.headers['location']
      answer=bypass_link(uri,modulesl,jumlah=[str(re),str(jumlah)])
      if answer:
        if 'failed to bypass' in answer:pass
        else:
          get_reward=curl.get(answer)
          dash=curl.post('https://wildfaucet.com/em-assets/themes/default/earn/sortlink/',data=data)
          info=bs(dash.text,'html.parser').find('div',class_='balance')
          rprint(Tree('[white]├── [yellow]'+info.text.strip().replace('\n',' : ').split('Satoshi : Withdrawal :  :  :  : Buy Balance')[0].replace(' : ',' [white]:[yellow] ')+' Satoshi'))
          re-=1
     except Exception as e:
       pass
def earnsolana(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://earnsolana.xyz/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    earnsolana(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  #email=input('email > ')
  curl=Session()
  headers={
    "Host":"earnsolana.xyz",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0"
  }
  headers_p={
    "Host":"earnsolana.xyz",
    "User-Agent":"XYZ/3.0",
    "content-type":"application/x-www-form-urlencoded"
  }
  login=curl.get('https://earnsolana.xyz/?r=1548',headers=headers)
  csrf=bs(login.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  auth=curl.post('https://earnsolana.xyz/auth/login',data=f'wallet={email}&csrf_token_name={csrf}',headers=headers_p)
  if 'Success!' in auth.text:
    print(hijau1+'Login Success')
    url=bs(auth.text,'html.parser').find_all('a',{'class':'collapse-item'})
    url_sl=[]
    url_f=[]
    for url in url:
      if 'faucet' in url['href']:
        url_f.append(url['href'])
      if 'links' in url['href']:
        url_sl.append(url['href'])
    for i in range(len(url_sl)):
      print(str(i)+'.'+url_sl[i].split('https://earnsolana.xyz/links/currency/')[1].upper())
    currency=input('select > ')
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://earnsolana.xyz/").netloc
    banner.banner(host.upper())
    get_sl=curl.get(url_sl[int(currency)],headers=headers)
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body bg-dark text-center text-white'})
    for sl in data_sl:
     try:
      jumlah=int(sl.find('span',{'class':'badge badge-light'}).text.split('/')[0])
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
         try:
          get_link=curl.get(sl.find('a')['href'],headers=headers,allow_redirects=False)
          #print(get_link.text)
          if 'location.href' in get_link.text:
            get_link=get_link.text.split(' <script> location.href = "')[1].split('"; </script>')[0]
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'Success!' in get_reward.text:
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
         except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
def cryptofuture(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://cryptofuture.co.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    cryptofuture(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  #email=input('email > ')
  curl=Session()
  headers={
    "Host":"cryptofuture.co.in",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0"
  }
  headers_p={
    "Host":"cryptofuture.co.in",
    "User-Agent":"XYZ/3.0",
    "content-type":"application/x-www-form-urlencoded"
  }
  login=curl.get('https://cryptofuture.co.in/?r=5471',headers=headers)
  csrf=bs(login.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  auth=curl.post('https://cryptofuture.co.in/auth/login',data=f'wallet={email}&csrf_token_name={csrf}',headers=headers_p)
  if 'Success!' in auth.text:
    print(hijau1+'Login Success')
    url=bs(auth.text,'html.parser').find_all('a',{'class':'collapse-item'})
    url_sl=[]
    url_f=[]
    for url in url:
      if 'faucet' in url['href']:
        url_f.append(url['href'])
      if 'links' in url['href']:
        url_sl.append(url['href'])
    for i in range(len(url_sl)):
      print(str(i)+'.'+url_sl[i].split('https://CryptoFuture.co.in/links/currency/')[1].upper())
    currency=input('select > ')
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://cryptofuture.co.in/").netloc
    banner.banner(host.upper())
    get_sl=curl.get(url_sl[int(currency)],headers=headers)
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body bg-dark text-center text-white'})
    for sl in data_sl:
     try:
      jumlah=int(sl.find('span',{'class':'badge badge-info'}).text.split('/')[0])
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
         try:
          get_link=curl.get(sl.find('a')['href'],headers=headers,allow_redirects=False)
          #print(get_link.text)
          if 'location.href' in get_link.text:
            get_link=get_link.text.split(' <script> location.href = "')[1].split('"; </script>')[0]
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'Success!' in get_reward.text:
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
         except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
def freeltc(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://freeltc.fun/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    freeltc(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  #email=input('email > ')
  curl=Session()
  headers={
    "Host":"freeltc.fun",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0"
  }
  headers_p={
    "Host":"freeltc.fun",
    "User-Agent":"XYZ/3.0",
    "content-type":"application/x-www-form-urlencoded"
  }
  login=curl.get('https://freeltc.fun/?r=7583',headers=headers)
  csrf=bs(login.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  auth=curl.post('https://freeltc.fun/auth/login',data=f'wallet={email}&csrf_token_name={csrf}',headers=headers_p)
  if 'Success!' in auth.text:
    print(hijau1+'Login Success')
    url=bs(auth.text,'html.parser').find_all('a',{'class':'collapse-item'})
    url_sl=[]
    url_f=[]
    for url in url:
      if 'faucet' in url['href']:
        url_f.append(url['href'])
      if 'links' in url['href']:
        url_sl.append(url['href'])
    for i in range(len(url_sl)):
      print(str(i)+'.'+url_sl[i].split('https://freeltc.fun/links/currency/')[1].upper())
    currency=input('select > ')
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://freeltc.fun/").netloc
    banner.banner(host.upper())
    get_sl=curl.get(url_sl[int(currency)],headers=headers)
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body bg-dark text-center text-white'})
    for sl in data_sl:
     try:
      jumlah=int(sl.find('span',{'class':'badge badge-info'}).text.split('/')[0])
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
         try:
          get_link=curl.get(sl.find('a')['href'],headers=headers,allow_redirects=False)
          #print(get_link.text)
          if 'location.href' in get_link.text:
            get_link=get_link.text.split(' <script> location.href = "')[1].split('"; </script>')[0]
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'Success!' in get_reward.text:
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
         except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
def claimcoins(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://claimcoins.net/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    claimcoins(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  #email=input('email > ')
  curl=Session()
  headers={
    "Host":"claimcoins.net",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0"
  }
  headers_p={
    "Host":"claimcoins.net",
    "User-Agent":"XYZ/3.0",
    "content-type":"application/x-www-form-urlencoded"
  }
  login=curl.get('https://claimcoins.net/',headers=headers)
  #print(login.text)
  #csrf=bs(login.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  auth=curl.post('https://claimcoins.net/auth/login',data=f'wallet={email}',headers=headers_p)
  if 'Success!' in auth.text:
    print(hijau1+'Login Success')
    get_sl=curl.get('https://claimcoins.net/links/currency/ltc',headers=headers)
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body text-center'})
    for sl in data_sl:
     try:
      jumlah=int(sl.find('span',{'class':'badge badge-info'}).text.split('/')[0])
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
         try:
          get_link=curl.get(sl.find('a')['href'],headers=headers,allow_redirects=False)
          #print(get_link.text)
          if 'location.href' in get_link.text:
            get_link=get_link.text.split('location.href = "')[1].split('";')[0]
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'Success!' in get_reward.text:
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
         except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
    get_sl=curl.get('https://claimcoins.net/links/withdraw/LTC',headers=headers)
    print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_sl.text.split("html: '")[1].split("',")[0])
def claim88(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://claim88.fun/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    claim88(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  #email=input('email > ')
  curl=Session()
  headers={
    "Host":"claim88.fun",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"XYZ/3.0"
  }
  headers_p={
    "Host":"claim88.fun",
    "User-Agent":"XYZ/3.0",
    "content-type":"application/x-www-form-urlencoded"
  }
  login=curl.get('https://claim88.fun/',headers=headers)
  csrf=bs(login.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  auth=curl.post('https://claim88.fun/auth/login',data=f'wallet={email}&csrf_token_name={csrf}',headers=headers_p)
  if 'Success!' in auth.text:
    print(hijau1+'Login Success')
    url=bs(auth.text,'html.parser').find_all('a',{'class':'collapse-item'})
    url_sl=[]
    url_f=[]
    for url in url:
      if 'faucet' in url['href']:
        url_f.append(url['href'])
      if 'links' in url['href']:
        url_sl.append(url['href'])
    for i in range(len(url_sl)):
      print(str(i)+'.'+url_sl[i].split('https://claim88.fun/links/currency/')[1].upper())
    currency=input('select > ')
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://claim88.fun/").netloc
    banner.banner(host.upper())
    get_sl=curl.get(url_sl[int(currency)],headers=headers)
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body bg-dark text-center text-white'})
    for sl in data_sl:
     try:
      jumlah=int(sl.find('span',{'class':'badge badge-info'}).text.split('/')[0])
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
         try:
          get_link=curl.get(sl.find('a')['href'],headers=headers,allow_redirects=False)
          #print(get_link.text)
          if 'location.href' in get_link.text:
            get_link=get_link.text.split(' <script> location.href = "')[1].split('"; </script>')[0]
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'Success!' in get_reward.text:
                  print(putih1+'├──'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
         except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
def freeltc_online(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://freeltc.online/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    freeltc_online(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  while True:
    try:
      curl=Session()
      ua_g = {
        'Host': 'freeltc.online',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      }
      ua_p = {
        'Host': 'freeltc.online',
        'origin': 'https://freeltc.online',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      url="https://freeltc.online/"
      get_data=curl.get(url,headers=ua_g)
      parser=bs(get_data.text,'html.parser')
      sesi=parser.find('input',{'name':'session-token'})['value']
      key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
      answer=modulesl.RecaptchaV2(key,url)
      data=f'session-token={sesi}&address={email}&antibotlinks=&captcha=recaptcha&g-recaptcha-response={answer}&login=Verify+Captcha'
      send_data=curl.post(url,headers=ua_p,data=data)
      for ulang in range(10):
        get_sl=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g,allow_redirects=False)
        an=bypass_link(get_sl.headers['location'],modulesl)
        if an:
          if 'failed to bypass' in an:
            pass
          else:
            get_data=curl.get(an,headers=ua_g)
            print(kuning1+' > '+hijau1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-success fade show'}).text.strip().splitlines()[0])
            animasi(detik=60)
            break
        else:
          send_data=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g)
      if ulang==9:
        exit('shortlinks limit')
    except Exception as e:
      pass
def claimfreetrx(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://claimfreetrx.online/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['email'])
    claimfreetrx(modulesl,banner)
  email = load_data(host,custom=['email'])["email"]
  while True:
    try:
      curl=Session()
      ua_g = {
        'Host': 'claimfreetrx.online',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      }
      ua_p = {
        'Host': 'claimfreetrx.online',
        'origin': 'https://claimfreetrx.online',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      url="https://claimfreetrx.online/"
      get_data=curl.get(url,headers=ua_g)
      parser=bs(get_data.text,'html.parser')
      sesi=parser.find('input',{'name':'session-token'})['value']
      key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
      answer=modulesl.RecaptchaV2(key,url)
      data=f'session-token={sesi}&address={email}&antibotlinks=&captcha=recaptcha&g-recaptcha-response={answer}&login=Verify+Captcha'
      send_data=curl.post(url,headers=ua_p,data=data)
      for ulang in range(10):
        get_sl=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g,allow_redirects=False)
        an=bypass_link(get_sl.headers['location'],modulesl)
        if an:
          if 'failed to bypass' in an:
            pass
          else:
            get_data=curl.get(an,headers=ua_g)
            print(kuning1+' > '+hijau1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-success fade show'}).text.strip().splitlines()[0])
            animasi(detik=60)
            break
        else:
          send_data=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g)
      if ulang==9:
        exit('shortlinks limit')
    except Exception as e:
      pass