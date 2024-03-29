#-------- import module ----------#
import requests,json,time,asyncio,re,shutil,os,random,pathlib,subprocess,traceback,base64,string
from threading import Thread
from tqdm import tqdm
from os import system
from time import sleep
from bs4 import BeautifulSoup as bs
from http.cookies import SimpleCookie
from urllib.parse import urlparse,urlencode,unquote
from telethon import TelegramClient, sync, events
from rich.tree import Tree
from rich.panel import Panel
from rich import print as rprint
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from concurrent.futures import ThreadPoolExecutor
from rich import print as cetak
#----------- color ---------------#
hijau1 = "\033[1;92m"
kuning1 = "\033[1;93m"
putih1 = "\033[1;97m"
merah1 = "\033[1;91m"
biru1 = "\033[1;94m"
#----------- module ---------------#
def settings():
  if os.path.exists('settings.json'):
    data=json.loads(open('settings.json').read())
    if data['multi']=='n':data['multi']=None
    return data
  else:return {"timer":"45,160","multi":None}
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
  "clicksfly.me":modulesl.clicksfly_me,
  "clk.asia":modulesl.clickfly,
  #"revcut.net":modulesl.revcut,
  #"slfly.net":modulesl.revcut,
  #"inlinks.online":modulesl.bitss,
  #"bitss.sbs":modulesl.bitss,
  "v2p.icu":modulesl.v2picu,
  "adbits.pro":modulesl.v2picu,
  "adbits.xyz":modulesl.v2picu,
  "adbx.pro":modulesl.v2picu,
  "kyshort.xyz":modulesl.kyshort,
  "teralinks.in":modulesl.teralinks,
  # "rsshort.com":modulesl.rsshort,
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
  "link.birdurls.com":modulesl.birdurl,
  "oko.sh":modulesl.clksh,
  #"":modulesl.coinparty,
  #"ctr.sh":modulesl.ctrsh,
  #"easycut.io":modulesl.ctrsh,
  "cuty.io":modulesl.cuty_io,
  #"clks.pro":modulesl.clks_pro,
  "droplink.co":modulesl.droplink,
  "ex-foary.com":modulesl.ex_foary_com,
  "exe.io":modulesl.exe_io,
  "ez4short.com":modulesl.ez4short,
  "fc-lc.xyz":modulesl.fl_lc,
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
  "mitly.us":modulesl.mitly,
  #"oii.io":modulesl.oii,
  "link.owllink.net":modulesl.owlink,
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
    print(putih1+'┣━━'+'━'*56)
    if jumlah:
      print(f"┣━━ {putih1}[{kuning1}{jumlah[0]}/{jumlah[1]}{putih1}] {kuning1} Bypassing : {hijau1}{url}")
    else:
      print(f"┣━━ {putih1}{kuning1}Bypassing : {hijau1}{url}")
    res=dictnya[urlparse(url).netloc](url)
    if "failed to bypass" in res:
      print(putih1+'┣━━ '+kuning1+'Status : '+merah1+res)
      print(putih1+'┣━━'+'━'*56)
    else:
      print(putih1+'┣━━ '+kuning1+'Status : '+hijau1+"success")
      print(putih1+'┣━━'+'━'*56)
      if settings():
        ju=random.randint(int(settings()['timer'].split(',')[0]),int(settings()['timer'].split(',')[1]))
        animasi(detik=ju)
      else:
        animasi(detik=random.randint(45,160))
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
def icon_c(modulesl,host,curl,cookies,ugentmu):
  for i in range(5):
   try:
    id_=''.join(random.sample(string.ascii_letters + string.digits, 16))
    headers={
      "Host": host,
      "User-Agent": ugentmu,
      "X-Requested-With": "XMLHttpRequest",
      "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary"+id_,
      "Accept": "*/*",
      "Origin": "https://earnbitmoon.club",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://earnbitmoon.club/"}
    data_bs=base64.b64encode(json.dumps({"i":1,"a":1,"t":"dark","ts":int(time.time() * 1000)}).encode()).decode()
    dataq={"payload":data_bs}
    boundary = "----WebKitFormBoundary"+id_
    payload = ''
    for key, value in dataq.items():
        payload += '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'.format(boundary, key, value)
    payload += '--{}--'.format(boundary)
    get_bs=curl.post(f'https://{host}/system/libs/captcha/request.php',headers=headers,cookies=cookies,data=payload)
    if get_bs.status_code == 200:
      img_h={
      "Host": host,
      "User-Agent": ugentmu,
      "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
      "X-Requested-With": "mark.via.gq",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "no-cors",
      "Sec-Fetch-Dest": "image"}
      py=base64.b64encode(json.dumps({"i":1,"ts":int(time.time() * 1000)}).encode()).decode()
      get_g=curl.get(f'https://{host}/system/libs/captcha/request.php?payload='+py,headers=img_h,cookies=cookies)
      if get_g.status_code==200:
          answer=modulesl.rscaptcha(base64.b64encode(get_g.content).decode('utf-8'))
          #print(answer)
          if answer=="ERROR_CAPTCHA_UNSOLVABLE":
            pass
          else:
            answer=answer.split(':')
            id_=''.join(random.sample(string.ascii_letters + string.digits, 16))
            headers={
              "Host": host,
              "User-Agent": ugentmu,
              "X-Requested-With": "XMLHttpRequest",
              "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary"+id_,
              "Accept": "*/*",
              "Origin": "https://earnbitmoon.club",
              "Sec-Fetch-Site": "same-origin",
              "Sec-Fetch-Mode": "cors",
              "Sec-Fetch-Dest": "empty",
              "Referer": "https://earnbitmoon.club/"}
            data_bs=base64.b64encode(json.dumps({"i":1,"x":int(answer[0]),"y":int(answer[1]),"w":320,"a":2,"ts":int(time.time() * 1000)}).encode()).decode()
            dataq={"payload":data_bs}
            boundary = "----WebKitFormBoundary"+id_
            payload = ''
            for key, value in dataq.items():
                payload += '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'.format(boundary, key, value)
            payload += '--{}--'.format(boundary)
            get_bs=curl.post(f'https://{host}/system/libs/captcha/request.php',headers=headers,cookies=cookies,data=payload)
            status_code(get_bs)
            if get_bs.status_code==200:
              return answer
   except Exception as e:
     print(e)
def ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl,icon):
      ua = {
        "Host": host,
        'User-Agent': ugentmu,
    }
      def balance():
        get_sl = curl.get(f'https://{host}{path_ptc}', headers=ua, cookies=cookies)
        status_code(get_sl)
        return bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})[0].text.strip()
      pct = Tree("[gree] > [yellow]Start working on ptc",guide_style="bold bright_white")
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
                  if icon:
                    answer = icon_c(modulesl, host, curl, cookies, ugentmu)
                    answer=answer[0]+","+answer[1]+",320"
                    data=f"a=proccessPTC&data={_i}&token={token1}&ic-hf-id=1&ic-hf-se={answer}&ic-hf-hp="
                    #print(data)
                  else:
                    answer = get_answer(name=host, cookies=cookies, ugentmu=ugentmu)
                    data=f"a=proccessPTC&data={_i}&token={token1}&captcha-idhf=0&captcha-hf={answer}"
                  if answer:
                    reward = curl.post(f'https://{host}/system/ajax.php', data=data, headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, cookies=cookies)
                    #print(reward.text)
                    status_code(reward)
                    if json.loads(reward.text)["status"] == 200:
                        gas = bs(json.loads(reward.text)["message"], "html.parser").find("div", {"class": "alert alert-success"}).text
                        print(putih1 + '  ┣━━' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + gas.strip())
                        print(putih1 + '  ┗━━' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                        sesi = True
          except Exception as e:
              print(putih1 + '┣━━' + hijau1 + f' {putih1}[{merah1}!{putih1}] {str(e)}')
              traceback.print_exc()
              pass
      print(putih1 + '┗━━' + hijau1 + ' [ ' + kuning1 + '√' + hijau1 + ' ] ' + "Success bypassing all ptc ;)")
def sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl,icon):
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
      sl = Tree("[green]> [yellow]Start Bypassing Shortlinks",guide_style="bold bright_white")
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
              for gej in range(3):
                get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
                status_code(get_sl)
                token = get_sl.text.split("var token = '")[1].split("';")[0]
                status = True
                while(status == True):
                  da = id["onclick"].split("goShortlink('")[1].split("');")[0]
                  if icon:
                      answer = icon_c(modulesl, host, curl, cookies, ugentmu)
                      #print(answer)
                      answer=answer[0]+","+answer[1]+",320"
                      data=f"a=getShortlink&data={da}&token={token}&ic-hf-id=1&ic-hf-se={answer[0]},{answer[1]},320&ic-hf-hp="
                      #print(data)
                  else:
                      answer = get_answer(name=host, cookies=cookies, ugentmu=ugentmu)
                      data=f"a=getShortlink&data={da}&token={token}&captcha-idhf=0&captcha-hf="+answer
                  if answer:
                    get_lk = curl.post(f'https://{host}/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=data, allow_redirects=False, cookies=cookies)
                    status_code(get_lk)
                    get_lk = json.loads(get_lk.text)
                    if get_lk["status"] == 200:
                      answer = bypass_link(get_lk['shortlink'], modulesl, jumlah=[str(re), str(jumlah)])
                      if answer:
                        if 'failed to bypass' in answer:
                            ulang=True
                            break
                        else:
                          try:
                              get_sl = curl.get(answer, headers=ua, cookies=cookies)
                              status_code(get_sl)
                              sukses = bs(get_sl.text, 'html.parser').find("div", {"class": "alert alert-success mt-0"}).text
                              print(putih1 + '┃  ┣━━' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + sukses)
                              print(putih1 + '┃  ┗━━' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                              re -= 1
                          except:
                              print(putih1 + '┃  ┗━━' + hijau1 + ' [ ' + merah1 + 'x' + hijau1 + ' ] ' + "invalid keys")
                          ulang=False
                          break
                      else:
                        status=False
                        break
                    if get_lk['status'] == 600:
                      print(putih1 + '┣━━' + hijau1 + ' [ ' + merah1 + 'x' + hijau1 + ' ] ' + "Captcha wrong", end="\r")
                    else:
                      print(putih1 + '┣━━' + hijau1 + ' [ ' + merah1 + 'x' + hijau1 + ' ] ' + "There seems to be something wrong with the link")
                      ulang=False
                      break
                if status==False:break
                elif ulang:
                  pass
                else:break
        except Exception as e:
          keluar(str(e))
          traceback.print_exc()
          pass
      print(putih1 + '┣━━' + hijau1 + ' [ ' + kuning1 + '√' + hijau1 + ' ] ' + "Success bypassing all shortlinks ;)")
def bits_family(modulesl,banner,host, recaptcha_key,faucet=None,path_ptc='/ptc.html',key_all_ptc=('button', {'class': 'btn btn-success btn-sm w-100 mt-1'}),path_sl='/shortlinks.html',key_all_sl=('tr'),key_button_id=('button', {'class': 'btn btn-success btn-sm'}),key_amount_sl=('b', {'class': 'badge badge-dark'}),run=None,ptc1=None,icon=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner.banner(host.upper())
    data_control(name=host)
    cookies, ugentmu = load_data(host)
    if not os.path.exists(f"data/{host}/{host}.json"):
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1,icon)
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
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1,icon)
    try:
        akun = Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
        get_inf = bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})
        for info in get_inf:
            akun.add('[green]> [yellow]' + info.text.strip())
        rprint(akun)
    except Exception as e:
        save_data(host)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1,icon)
    def balance():
        get_sl = curl.get(f'https://{host}{path_sl}', headers=ua, cookies=cookies)
        status_code(get_sl)
        return bs(get_sl.text, 'html.parser').find_all('div', {'class': 'col-9 no-space'})[0].text.strip()
    if run == '1':
      if ptc1 == 'Off':
        print('Ptc off')
        pass
      else:
        ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl,icon)
    if run == '2':
      sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl,icon)
    if run == '3':
      if faucet=='Off':
        print('Faucet off')
        animasi(menit=1440)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1,icon=icon)
      rprint(Tree("[green]> [yellow]Bypass faucet",guide_style="bold bright_white"))
      if faucet:fauceturl=f'https://{host}/{faucet}'
      else:fauceturl=f'https://{host}/'
      while True:
        try:
            get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
            if 'Faucet Locked!' in get_sl.text:
              if 'You must visit' in get_sl.text:
                print(bs(get_sl.text,'html.parser').find('div',{'class':'alert alert-warning'}).text.strip())
                sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl,icon)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1,icon=icon)
              else:
                animasi(menit=1440)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1,icon=icon)
            if 'Just a moment...' in get_sl.text:
              save_data(host)
              bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1,icon)
            status_code(get_sl)
            if 'You can claim again in' in get_sl.text:
                tim = int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0]) * 60
                get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
                waktu=get_sl.text.split('claimTime">')[1].split(' ')[0]
                for i in tqdm(range(int(tim)), leave=False, desc="Please wait..."):
                    time.sleep(1)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            if icon:
              answer = icon_c(modulesl, host, curl, cookies, ugentmu)
              answer=answer[0]+","+answer[1]+",320"
              data=f"a=getFaucet&token={token}&captcha=3&challenge=false&response=false&ic-hf-id=1&ic-hf-se={answer[0]},{answer[1]},314.623&ic-hf-hp="
              #print(data)
            else:
              answer = modulesl.RecaptchaV2(recaptcha_key, get_sl.url)
              data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}"
            g = curl.post(f'https://{host}/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=data, cookies=cookies)
            status_code(g)
            g = json.loads(g.text)
            if g["status"] == 200:
                gas = bs(g["message"], "html.parser").find("div", {"class": "alert alert-success"}).text
                print(putih1 + '┣━━' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + gas.strip())
                print(putih1 + '┣━━' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
                waktu=get_sl.text.split('claimTime">')[1].split(' ')[0]
                dtk=random.randint(45,160)
                for i in tqdm(range(int(waktu)*60+dtk), leave=False, desc="Please wait..."):
                    time.sleep(1)
            else:
              gas = bs(g["message"], "html.parser").text
              print(putih1 + '┣━━' + hijau1 + f' {putih1}[{merah1}!{putih1}] '+gas)
        except Exception as e:
            print(putih1 + '┣━━' + hijau1 + f' {putih1}[{merah1}!{putih1}] {str(e)}')
            pass
    if run == '0':
      if ptc1 == 'Off':
        print('Ptc off')
      else:
        ptc(modulesl,banner,host,cookies,ugentmu,path_ptc,key_all_ptc,curl,icon)
      sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl,icon)
      if faucet=='Off':
        print('Faucet off')
        animasi(menit=1440)
        bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1,icon=icon)
      rprint(Tree("[green]> [yellow]Bypass faucet",guide_style="bold bright_white"))
      if faucet:fauceturl=f'https://{host}/{faucet}'
      else:fauceturl=f'https://{host}/'
      while True:
        try:
            get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
            if 'Faucet Locked!' in get_sl.text:
              if 'more Shortlinks today to be able to Roll & Win FREE Coins!' in get_sl.text:
                print(bs(get_sl.text,'html.parser').find('div',{'class':'alert alert-warning'}).text.strip())
                sl(modulesl,banner,host,cookies,ugentmu,path_sl,key_all_sl,key_button_id,key_amount_sl,curl,icon)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1,icon=icon)
              else:
                animasi(menit=1440)
                bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run='0',ptc1=ptc1,icon=icon)
            if 'Just a moment...' in get_sl.text:
              save_data(host)
              bits_family(modulesl,banner,host, recaptcha_key,faucet,path_ptc,key_all_ptc,path_sl,key_all_sl,key_button_id,key_amount_sl,run,ptc1,icon)
            #waktu=get_sl.text.split('<h1 class="text-warning"><i class="fa fa-arrow-down"></i>')[1].split(' minutes')[0].split('every ')[1]
            status_code(get_sl)
            if 'You can claim again in' in get_sl.text:
                tim = int(get_sl.text.split('You can claim again in <span id="claimTime">')[1].split(' minutes</span>')[0]) * 60
                for i in tqdm(range(int(tim)), leave=False, desc="Please wait..."):
                    time.sleep(1)
            token = get_sl.text.split("var token = '")[1].split("';")[0]
            if icon:
              answer = icon_c(modulesl, host, curl, cookies, ugentmu)
              answer=answer[0]+","+answer[1]+",320"
              data=f"a=getFaucet&token={token}&captcha=3&challenge=false&response=false&ic-hf-id=1&ic-hf-se={answer[0]},{answer[1]},314.623&ic-hf-hp="
              #print(data)
            else:
              answer = modulesl.RecaptchaV2(recaptcha_key, get_sl.url)
              data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}"
            g = curl.post(f'https://{host}/system/ajax.php', headers={"User-Agent": ugentmu, "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "accept": "application/json, text/javascript, */*; q=0.01"}, data=data, cookies=cookies)
            status_code(g)
            g = json.loads(g.text)
            if g["status"] == 200:
                gas = bs(g["message"], "html.parser").find("div", {"class": "alert alert-success"}).text
                print(putih1 + '┣━━' + hijau1 + ' [ ' + kuning1 + '>' + hijau1 + ' ] ' + gas.strip())
                print(putih1 + '┣━━' + hijau1 + ' [ ' + kuning1 + '+' + hijau1 + ' ] ' + balance())
                get_sl = curl.get(fauceturl, headers=ua, cookies=cookies)
                waktu=get_sl.text.split('claimTime">')[1].split(' ')[0]
                dtk=random.randint(45,160)
                for i in tqdm(range(int(waktu)*60+dtk), leave=False, desc="Please wait..."):
                    time.sleep(1)
            else:
              gas = bs(g["message"], "html.parser").text
              print(putih1 + '┣━━' + hijau1 + f' {putih1}[{merah1}!{putih1}] '+gas)
        except Exception as e:
            print(putih1 + '┣━━' + hijau1 + f' {putih1}[{merah1}!{putih1}] {str(e)}')
            pass
def earnbitmoon(modulesl,banner):
  bits_family(modulesl,banner,'earnbitmoon.club', '6LdzF6MlAAAAACcN9JGXW8tSs4dy1MjeKZKFJ11M',icon=True)
def earnbitmoon_xyz(modulesl,banner):
  bits_family(modulesl,banner,'earnbitmoon.xyz', '6LeVUbEhAAAAALxHCVnXYISpTvOS4sIj_SB6DQOU')
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
def earnbits(modulesl,banner):
  bits_family(modulesl,banner,host='earnbits.io', recaptcha_key='6LcJO3YnAAAAAODSQdQry4sVyosh5BT6YuYXQfW4',key_all_ptc=('button',{'class':'btn btn-success btn-sm w-100 mt-1'}),key_all_sl=('div',{'class':'col-xl-2 col-lg-3 col-sm-4 col-12 mb-4'}),key_button_id=('button',{'class':'btn btn-success btn-sm'}),key_amount_sl=('span', {'class': 'badge bg-label-info mb-4'}))
def nevcoin(modulesl,banner):
  bits_family(modulesl,banner,'nevcoins.club', '6Lfq4b4ZAAAAALs8lVypMYqUH5E8esL8B78wkA0Y',faucet='/claim.html',path_ptc='/ptc.html',key_all_ptc=('button', {'class': 'btn btn-success btn-sm w-100 mt-1'}),path_sl='/shortlinks.html',key_all_sl='tr',key_button_id=('button', {'class': 'btn btn-success btn-sm'}),key_amount_sl=('b', {'class': 'badge badge-dark'}))
#--------------- vie family ---------------#
def vie_script(modulesl,banner,url,key_re,ptc=False,short=False,faucet=False,auto=False,link=None,name_key=None,bal=None):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse(url).netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    vie_script(modulesl,banner,url,key_re,ptc,short,faucet,auto,link,name_key,bal)
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
  if 'Welcome Back !' not in dash.text:
    save_data(name=host)
    vie_script(modulesl,banner,url,key_re,ptc,short,faucet,auto,link,name_key,bal)
  if bal:
    info=bs(dash.text,'html.parser').find_all('div',{'class':bal})
  else:
    info=bs(dash.text,'html.parser').find_all('div',{'class':'card mini-stats-wid'})
  akun=Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  if ptc == True:
    rprint(Tree("[green]> [yellow]Start ptc",guide_style="bold bright_white"))
    ptc=curl.get(f'https://{host}/ptc',headers=ua,cookies=cookies)
    status_code(ptc)
    if 'ads available' not in ptc.text:
      save_data(name=host)
      vie_script(modulesl,banner,url,key_re,ptc,short,faucet,auto,link,name_key,bal)
    ptc=bs(ptc.text,'html.parser').find_all('div',{'class':'col-sm-6'})
    for ptc in ptc:
     try:
      name=ptc.find('h5',{'class':'card-title'}).text
      link=ptc.find('button',{'class':'btn btn-primary btn-block'})["onclick"].split("window.location = '")[1].split("'")[0]
      visit=curl.get(link,headers=ua,cookies=cookies)
      status_code(visit)
      print(putih1+'┣━━'+hijau1+f' {putih1}[{kuning1} ~ {putih1}] {kuning1}View : '+parser(name),end=end())
      animasi(detik=int(visit.text.split('var timer = ')[1].split(';')[0]))
      bs4 = bs(visit.text, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      data["captcha"]="recaptchav2"
      data["g-recaptcha-response"]=modulesl.RecaptchaV2(key_re,visit.url)
      verify=curl.post(link.replace('view','verify'),data=data,headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies)
      status_code(verify)
      if 'Good job!' in verify.text:
        print(putih1+'┣━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+verify.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
     except Exception as e:
        keluar(str(e))
        pass
    print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more ptc!')
  if short == True:
    rprint(Tree("[green]> [yellow]Start bypass shortlinks",guide_style="bold bright_white"))
    get_links=curl.get(f'https://{host}/links',headers=ua,cookies=cookies)
    status_code(get_links)
    if get_links.status_code!=200:
      save_data(name=host)
      vie_script(modulesl,banner,url,key_re,ptc,short,faucet,auto,link,name_key,bal)
    else:
      fd=bs(get_links.text,'html.parser')
      if link:
        link=fd.find_all('div',{'class':link})
      else:
        link=fd.find_all('div',{'class':'col-lg-3'})
      def run(i):
        try:
            try:
              jumlah = i.find('span',{'class':'badge badge-info'}).text.split('/')
              re=int(jumlah[0])
            except Exception as e:
              jumlah=[99,99]
              re=99
              pass
            yt_=0
            for ulang in range(int(jumlah[0])):
              try:
                for ytta in range(3):
                 try:
                  if 'pre_verify' in i.find('a')["href"]:
                    status=True
                    while(status==True):
                      url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies)
                      status_code(url)
                      ans=modulesl.antibot(url,key='alert alert-warning text-center',name_key=name_key)
                      if ans=='WRONG_RESULT' or ans=='ERROR_CAPTCHA_UNSOLVABLE':
                        pass
                      else:
                        data='antibotlinks=+'+ans+'&'
                        if 'csrf_token_name' in url.text:
                          csrf=bs(url.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
                          data=data+'csrf_token_name='+csrf+'&'
                        elif 'token' in url.text:
                          token=bs(url.text,'html.parser').find('input',{'name':'token'})['value']
                          data=data+'token='+token
                        url = curl.post(i.find('a')["href"].replace('pre_verify','go'), headers={'Host':host,'User-Agent':ugentmu,'content-type':'application/x-www-form-urlencoded','referer':i.find('a')["href"]},data=data, cookies=cookies,allow_redirects=False)
                        status_code(url)
                        if 'location.href' in url.text:
                          status=False
                  else:
                    url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
                  status_code(url)
                  url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
                  answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah[1]])
                  if answer==False:
                    yt_+=1
                    break
                  elif 'failed to bypass' in answer:
                      yt_+=1
                      pass
                  else:
                      if urlparse(answer).netloc =='earnsolana.xyz':
                        answer=answer.replace('back','verify')
                      reward = curl.get(answer, headers=ua, cookies=cookies)
                      status_code(reward)
                      if 'Good job!' in reward.text:
                          print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                      else:
                          print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
                  re-=1
                  break
                 except Exception as e:
                  keluar(str(e))
                  pass
                if answer==False:break
                if yt_==3:break
              except Exception as e:
                keluar(str(e))
                pass
        except Exception as e:
            keluar(str(e))
            pass
      if settings()['multi']:
        
          with ThreadPoolExecutor(max_workers=7) as executor:
            futures = [executor.submit(run, i) for i in link]
      else:
        for i in link:
          run(i)
      print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  if auto == True:
    rprint(Tree("[green]> [yellow]Start auto faucet",guide_style="bold bright_white"))
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
        print(putih1+'┣━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
     except Exception as e:
       print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy!')
       break
       #exit()
  if faucet == True:
    rprint(Tree("[green]> [yellow]Start faucet",guide_style="bold bright_white",))
    faucet=curl.get(f'https://{host}/faucet',headers=ua,cookies=cookies)
    status_code(faucet)
    jumlah=bs(faucet.text,'html.parser').find_all('p',{'class':'lh-1 mb-1 font-weight-bold'})
    if 'Please click on the Anti-Bot links in the following order' in faucet.text:
      print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}maaf faucet memiliki anti bot saat ini belum ada metode bypass untuk anti bot')
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
        print(putih1+'┣━━'+hijau1+f' {putih1}[{str(re)}/{jum[1]}{hijau1} √ {putih1}] {hijau1}'+faucet.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
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
        print(putih1+'┣━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}Sukses bypass firewall')
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
    keforcash(modulesl,banner)
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
    keforcash(modulesl,banner)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-lg-6 col-md-6 col-sm-12 col-xl-3'})
  akun=Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
  for info in info:
    akun.add('[green]> [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[green]> [yellow]Start bypass shortlinks",guide_style="bold bright_white"))
  get_links=curl.get(f'https://{host}/links',headers=ua,cookies=cookies)
  status_code(get_links)
  if 'links available' not in get_links.text.lower():
    save_data(name=host)
    keforcash(modulesl,banner)
  fd=bs(get_links.text,'html.parser')
  link=fd.find_all('div',{'class':'col-12 col-md-6 col-xl-4'})
  def run(i):
    try:
        #name = i.find('h4').text
        jumlah = i.find('p',{'class':'mx-auto text-primary'}).text.split('/')
        re=int(jumlah[0])
        for ulang in range(int(jumlah[0])):
          try:
            url = curl.get(i.find('a')["href"], headers=ua, cookies=cookies, allow_redirects=False)
            status_code(url)
            url=url.text.split('<script> location.href = "')[1].split('"; </script>')[0]
            answer = bypass_link(url,modulesl,jumlah=[str(re),jumlah[0]])
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
                    print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> swal(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                else:
                    print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
            re-=1
          except Exception as e:
            keluar(str(e))
            pass
    except Exception as e:
        keluar(str(e))
        pass
  if settings()['multi']:
    
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, i) for i in link]
  else:
    for i in link:
      run(i)
    print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
def claimcoin_in(modulesl,banner):
  vie_script(modulesl,banner,url="https://claimcoin.in/",key_re="6LfO65QlAAAAAE4tUQ1uwmXFMW1TvT5QxEDtrK25",ptc=False,short=True,faucet=False,auto=True)
def claimbitco_in(modulesl,banner):
  vie_script(modulesl,banner,url="https://claimbitco.in/",key_re="6LfO65QlAAAAAE4tUQ1uwmXFMW1TvT5QxEDtrK25",ptc=False,short=True,faucet=False,auto=True)
def cryptobigpay(modulesl,banner):
  vie_script(modulesl,banner,url="https://cryptobigpay.online/",key_re="6LfO65QlAAAAAE4tUQ1uwmXFMW1TvT5QxEDtrK25",ptc=False,short=True,faucet=False,auto=True,bal='col-md-4')
def whoopyrewards(modulesl,banner):
  vie_script(modulesl,banner,url="https://whoopyrewards.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False,link='col-lg-4')
def liteearn(modulesl,banner):
  vie_script(modulesl,banner,url="https://liteearn.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
def cryptoviefaucet(modulesl,banner):
  vie_script(modulesl,banner,url="https://cryptoviefaucet.com",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=False)
def bitupdate(modulesl,banner):
  vie_script(modulesl,banner,url="https://bitupdate.info",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True,name_key='div')
def litefaucet(modulesl,banner):
  vie_script(modulesl,banner,url="https://litefaucet.in",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def almasat(modulesl,banner):
  vie_script(modulesl,banner,url="https://almasat.net",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
def allfaucets(modulesl,banner):
  vie_script(modulesl,banner,url="https://allfaucets.site",key_re="6Led1EonAAAAACHrCJ0RlPfwK8rDXJk1Wr2ItTNn",ptc=False,short=True,faucet=False,auto=True)
#--------------- vie new family ---------------#
def insfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://insfaucet.xyz/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    insfaucet(modulesl,banner)
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
    insfaucet(modulesl,banner)
  get_info=bs(dash.text,"html.parser").find_all('div',{"class":"col-sm-6 layout-spacing"})
  akun=Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
  for info in get_info:
    akun.add("[green]> [yellow]"+info.text.strip().replace("\n"," : "))
  rprint(akun)
  rprint(Tree("[green]> [yellow]Shortlinks",guide_style="bold bright_white"))
  sl=curl.get(f'https://{host}/links',headers=hd,cookies=cookies)
  status_code(sl)
  sl=bs(sl.text,"html.parser").find_all("div",{"class":"col-sm-4 layout-spacing"})
  def run(sl):
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
              print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
            re-=1
            break
        except:pass
      if answer==False:break
   except Exception as e:
     keluar(str(e))
     pass
  if settings()['multi']:
    
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, sl) for sl in sl]
  else:
    for sl in sl:
      run(sl)
  print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
def onlyfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://onlyfaucet.com/").netloc
  data_control(host)
  banner.banner(host.upper())
  cookies, ugentmu = load_data(host)
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(name=host)
    onlyfaucet(modulesl,banner)
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
    onlyfaucet(modulesl,banner)
  get_info=bs(dash.text,"html.parser").find_all('div',{"class":"col-sm-6 layout-spacing"})
  akun=Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
  for info in get_info:
    akun.add("[green]> [yellow]"+info.text.strip().replace("\n"," : "))
  rprint(akun)
  rprint(Tree("[green]> [yellow]Shortlinks",guide_style="bold bright_white"))
  sl=curl.get(f'https://{host}/links',headers=hd,cookies=cookies)
  status_code(sl)
  sl=bs(sl.text,"html.parser").find_all("div",{"class":"col-sm-4 layout-spacing"})
  def run(sl):
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
              print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
            re-=1
            break
        except:pass
      if answer==False:break
   except Exception as e:
     keluar(str(e))
     pass
  if settings()['multi']:
    
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, sl) for sl in sl]
  else:
    for sl in sl:
      run(sl)
  print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
#--------------- bithub family ---------------#
def kiddyearner(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://kiddyearner.com").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    kiddyearner(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  dash=curl.get('https://kiddyearner.com/dashboard',headers=headers)
  status_code(dash)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'col-lg-6 col-xl-4'})
  akun=Tree("[gree] > [yellow]Account information",guide_style="bold bright_white")
  for info in info:
    v=info.text.strip().splitlines()
    akun.add("[green] > [yellow]"+v[len(v)-1]+" [white]:[green] "+v[0]+" "+v[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start Shortlinks",guide_style="bold bright_white"))
  links=curl.get('https://kiddyearner.com/links',headers=headers)
  status_code(links)
  if links.status_code==403:
    save_data(host)
    kiddyearner(modulesl,banner)
  link=bs(links.text,'html.parser').find_all('div',{'class':'col-lg-6'})
  def run(lin):
      jumlah=lin.find_all('div',{'class':'pil me-2'})[1].text.strip().split('/')[0]
      url=lin.find('a',{'class':'claim-btn text-white w-100'})['href']
      re=int(jumlah)
      for i in range(re):
        try:
          for ytta in range(5):
            try:
              get_links=curl.get(url,headers=headers,allow_redirects=False)
              if get_links.status_code==403:
                save_data(host)
                kiddyearner(modulesl,banner)
              status_code(get_links)
              if 'location.href' in get_links.text:
                answer=bypass_link(get_links.text.split('location.href = "')[1].split('";')[0],modulesl,jumlah=[str(re),jumlah])
                if answer:
                  if 'failed to bypass' in answer:pass
                  else:
                    get_next=curl.get(answer,headers=headers,allow_redirects=False)
                    status_code(get_next)
                    get_reward=curl.get(get_next.headers['location'],headers=headers)
                    #print(get_reward.text)
                    status_code(get_reward)
                    if 'success' in get_reward.text:
                      print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}success '+get_reward.text.split("title: '")[1].split("'")[0])
                      re-=1
                    else:
                      print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
                break
            except Exception as e:
              keluar(str(e))
              pass
        except Exception as e:
          keluar(str(e))
          pass
  if settings()['multi']:
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, i) for i in link]
  else:
    for i in link:
      run(i)
def cryptoearns(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://cryptoearns.com").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    cryptoearns(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  dash=curl.get('https://cryptoearns.com/dashboard',headers=headers)
  status_code(dash)
  info=bs(dash.text,'html.parser').find_all('div',{'class':'finance_card'})
  akun=Tree("[gree] > [yellow]Account information",guide_style="bold bright_white")
  for info in info:
    v=info.text.strip().splitlines()
    akun.add("[green] > [yellow]"+v[len(v)-1]+" [white]:[green] "+v[0])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start Shortlinks",guide_style="bold bright_white"))
  links=curl.get('https://cryptoearns.com/links',headers=headers)
  status_code(links)
  if links.status_code==403:
    save_data(host)
    cryptoearns(modulesl,banner)
  link=bs(links.text,'html.parser').find_all('div',{'class':'col-lg-6'})
  def run(lin):
      jumlah=lin.find_all('div',{'class':'pil me-2'})[1].text.strip().split('/')[0]
      url=lin.find('a',{'class':'claim-btn text-white w-100'})['href']
      re=int(jumlah)
      for i in range(re):
        try:
          for ytta in range(5):
            try:
              get_links=curl.get(url,headers=headers,allow_redirects=False)
              if get_links.status_code==403:
                save_data(host)
                cryptoearns(modulesl,banner)
              status_code(get_links)
              if 'location.href' in get_links.text:
                answer=bypass_link(get_links.text.split('location.href = "')[1].split('";')[0],modulesl,jumlah=[str(re),jumlah])
                if answer:
                  if 'failed to bypass' in answer:pass
                  else:
                    get_next=curl.get(answer,headers=headers,allow_redirects=False)
                    status_code(get_next)
                    get_reward=curl.get(get_next.headers['location'],headers=headers)
                    #print(get_reward.text)
                    status_code(get_reward)
                    if 'success' in get_reward.text:
                      print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}success '+get_reward.text.split("title: '")[1].split("'")[0])
                      re-=1
                    else:
                      print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
                break
            except Exception as e:
              keluar(str(e))
              pass
        except Exception as e:
          keluar(str(e))
          pass
  if settings()['multi']:
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, i) for i in link]
  else:
    for i in link:
      run(i)
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
  akun=Tree("[gree] > [yellow]Account information",guide_style="bold bright_white")
  for info in info:
    akun.add('[gree] > [yellow]'+info.text.strip().splitlines()[0]+' [white]: [yellow]'+info.text.strip().splitlines()[1])
  rprint(akun)
  rprint(Tree("[gree] > [yellow]Start bypass shortlinks",guide_style="bold bright_white"))
  get_links=curl.get('https://faucetspeedbtc.com/links',headers=ua,cookies=cookies)
  status_code(get_links)
  fd=bs(get_links.text,'html.parser')
  if 'Links' not in get_links.text:
    save_data('faucetspeedbtc')
    faucetspeedbtc(modulesl,banner)
  link=fd.find_all('div',{'class':'col-md-6 col-xl-4'})
  def run(i):
    try:
        if 'h5' not in str(i):pass
        else:
          name = i.find('h5').text
          jumlah = int(i.find('span').text.split('/')[0])
          re=jumlah
          for ulang in range(jumlah):
            for uli in range(5):
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
                  #print(reward)
                  if 'Approved!' in reward:
                      print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'", "").replace(',', ''))
                      re-=1
                  else:
                      print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}invalid keys')
            if answer==False:break
    except Exception as e:
      keluar(str(e))
      pass
  if settings()['multi']:
    
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, i) for i in link]
  else:
    for i in link:
      run(i)
  print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} ! {putih1}] {hijau1}'+'No more shortlinks!')
  rprint(Tree("[gree] > [yellow]Start auto faucet",guide_style="bold bright_white"))
  while True:
    try:
      get_=curl.get('https://faucetspeedbtc.com/auto',headers=ua,cookies=cookies)
      status_code(get_)
      token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
      animasi(detik=60)
      reward=curl.post('https://faucetspeedbtc.com/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
      status_code(reward)
      print(putih1+'┣━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+'Good job! 8 tokens has been added to your balance success')
    except:
      print(putih1+'┗━━'+hijau1+f' {putih1}[{merah1} x {putih1}] {hijau1}not enough energy')
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
  def run(bp):
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
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+sukses.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
                  re-=1
      except Exception as e:
       print(td+str(e))
   except Exception as e:
     print(td+str(e))
  if settings()['multi']:
    
      with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run, i) for i in sli]
  else:
    for i in sli:
      run(i)
def claimcoins(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://claimcoins.net/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    claimcoins(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  login=curl.get(f'https://claimcoins.net/links/currency/ltc',headers=headers)
  if login.status_code==200:
    print(hijau1+'Login Success')
    get_sl=curl.get('https://claimcoins.net/links/currency/ltc',headers=headers)
    for dt in bs(get_sl.text,'html.parser').find_all('script'):
      if 'var' and 'split' in str(dt):
        print(dt.text)
        print(modulesl.run_js('test',dt.text.replace('eval','console.log')))
        #modulesl.run_js()
    #print(get_sl.text)
    exit()
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body text-center'})
    def run(sl):
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
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
         except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
    if settings()['multi']:
      
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in data_sl]
    else:
      for i in data_sl:
        run(i)
    get_sl=curl.get('https://claimcoins.net/links/withdraw/LTC',headers=headers)
    print(putih1+'┣━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_sl.text.split("html: '")[1].split("',")[0])
  else:
    save_data(host)
    claimcoins(modulesl,banner)
def tokenmix_pro(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://tokenmix.pro/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    tokenmix_pro(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":"tokenmix.pro",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu,
    "content-type":"application/json",
    "referer":"https://tokenmix.pro/dashboard/sl",
  }
  get_info=curl.post('https://tokenmix.pro/infos/dashboard_info',headers=headers).json()
  if get_info['success']:
    akun=Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
    akun.add('[green]> Email [white]: [yellow]'+get_info['user']['email'])
    akun.add('[green]> Balance [white]: [yellow]'+get_info['user']['coins'])
    rprint(akun)
    rprint(Tree("[green]> [yellow]Start shortlinks",guide_style="bold bright_white"))
    get_sl=curl.post('https://tokenmix.pro/infos/auth_page_info',headers=headers,data=json.dumps({"page":"sl"})).json()
    def run(sl):
     try:
      jumlah=sl['views24Hours']
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
        try:
          get_link=curl.post('https://tokenmix.pro/user/generateSl',headers=headers,data=json.dumps({"slId":sl['_id'],"vote":None,"type":None}),allow_redirects=False).json()
          if get_link['success']:
            get_link=get_link['shortenedUrl']
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'succuss' in get_reward.url:
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+unquote(get_reward.url).split('=')[1])
                re-=1
                break
        except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
    if settings()['multi']:
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in get_sl['sls']]
    else:
      for i in get_sl['sls']:
        run(i)
    exit()
  else:
    save_data(host)
    tokenmix_pro(modulesl,banner)
def autofaucet_org(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://autofaucet.org/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    autofaucet_org(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":"autofaucet.org",
    "User-Agent":ugentmu,
  }
  dash=curl.get('https://autofaucet.org/dashboard',headers=headers,cookies=cookies)
  if 'Welcome back' not in dash.text:
    save_data(host)
    autofaucet_org(modulesl,banner)
  fd=bs(dash.text,'html.parser')
  koin=fd.find_all('div',{'class':'col item'})
  name=fd.find('p',{'class':'username'})
  akun=Tree("[white]> [green]Account information",guide_style="bold bright_white")
  akun.add('[yellow]Welcome back [white] : [green] '+name.text)
  rprint(akun)
  info=[]
  for i in koin:
   try:
    info.append("[yellow]"+i.text.strip().splitlines()[0].upper()+' [white]: [green]'+i.text.strip().splitlines()[2])
   except:pass
  menu_items = [f"[yellow][[white]{str(index)}[yellow]] {info[index]}      " for index in range(len(info))]
  menu_content = "\n".join(menu_items[i] + (menu_items[i + 1] if i + 1 < len(menu_items) else "") for i in range(0, len(menu_items), 2))
  cetak(Panel(menu_content, width=70, title="[bold green]Your Balance", padding=(0, 4), style="bold white"))
  get_sl=curl.get('https://autofaucet.org/dashboard/shortlinks',headers=headers,cookies=cookies)
  ak=Tree("[white]> [green]Start shortlinks",guide_style="bold bright_white")
  cg=bs(get_sl.text,'html.parser')
  fct=cg.find('p',{"class":"amount"})
  ak.add('[white]> [green]Your FCT Tokens [white]: [yellow]'+fct.text)
  rprint(ak)
  sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'item'})
  del sl[0]
  del sl[0]
  del sl[0]
  def run(sl):
    jumlah=int(sl.find('span',{'id':'views'}).text.strip().split('/')[0])
    re=jumlah
    url='https://autofaucet.org'+sl.find('form')['action']
    value=sl.find('input',{'name':'hh'})['value']
    for jum in range(jumlah):
      for i in range(3):
        headers_p={
          "Host":"autofaucet.org",
          "content-type":"application/x-www-form-urlencoded",
          "User-Agent":ugentmu,
        }
        data="hh="+value
        get_url=curl.post(url,headers=headers_p,cookies=cookies,data=data,allow_redirects=False).headers['Location']
        answer=bypass_link(get_url,modulesl,jumlah=[str(re),str(jumlah)])
        if answer:
          if 'failed to bypass' in answer:
            pass
          else:
            get_reward=curl.get(answer,headers=headers,cookies=cookies)
            if 'successfully' in get_reward.text:
              print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+bs(get_reward.text,'html.parser').find('div',{'class':'alert alert-success'}).text.strip())
            re-=1
            break
        else:
          break
  if settings()['multi']:
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in sl]
  else:
      for i in sl:
        run(i)
def autoclaim_in(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://autoclaim.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    autoclaim_in(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":"autoclaim.in",
    "User-Agent":ugentmu,
  }
  dash=curl.get('https://autoclaim.in/dashboard',headers=headers,cookies=cookies)
  if 'Welcome back' not in dash.text:
    save_data(host)
    autoclaim_in(modulesl,banner)
  fd=bs(dash.text,'html.parser')
  koin=fd.find_all('div',{'class':'col details'})
  name=fd.find('p',{'class':'username'})
  akun=Tree("[white]> [green]Account information",guide_style="bold bright_white")
  akun.add('[yellow]Welcome back [white] : [green] '+name.text)
  rprint(akun)
  info=[]
  for i in koin:
    info.append("[yellow]"+i.text.strip().splitlines()[0].upper()+' [white]: [green]'+i.text.strip().splitlines()[2])
  menu_items = [f"[yellow][[white]{str(index)}[yellow]] {item.split(': ')[0]}: {item.split(': ')[1]}      " for index, item in enumerate(info)]
  menu_content = "\n".join(menu_items[i] + (menu_items[i + 1] if i + 1 < len(menu_items) else "") for i in range(0, len(menu_items), 2))
  cetak(Panel(menu_content, width=70, title="[bold green]Your Balance", padding=(0, 4), style="bold white"))
  get_sl=curl.get('https://autoclaim.in/dashboard/shortlinks',headers=headers,cookies=cookies)
  ak=Tree("[white]> [green]Start shortlinks",guide_style="bold bright_white")
  cg=bs(get_sl.text,'html.parser')
  fct=cg.find('p',{"class":"amount"})
  ak.add('[white]> [green]Your FCT Tokens [white]: [yellow]'+fct.text)
  rprint(ak)
  sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'item'})
  del sl[0]
  del sl[0]
  del sl[0]
  def run(sl):
    jumlah=int(sl.find('span',{'id':'views'}).text.strip().split('/')[0])
    re=jumlah
    url='https://autoclaim.in'+sl.find('form')['action']
    value=sl.find('input',{'name':'hh'})['value']
    for jum in range(jumlah):
      for i in range(3):
        headers_p={
          "Host":"autoclaim.in",
          "content-type":"application/x-www-form-urlencoded",
          "User-Agent":ugentmu,
        }
        data="hh="+value
        get_url=curl.post(url,headers=headers_p,cookies=cookies,data=data,allow_redirects=False).headers['Location']
        answer=bypass_link(get_url,modulesl,jumlah=[str(re),str(jumlah)])
        if answer:
          if 'failed to bypass' in answer:
            pass
          else:
            get_reward=curl.get(answer,headers=headers,cookies=cookies)
            if 'successfully' in get_reward.text:
              print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+bs(get_reward.text,'html.parser').find('div',{'class':'alert alert-success'}).text.strip())
            re-=1
            break
        else:
          break
  if settings()['multi']:
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in sl]
  else:
      for i in sl:
        run(i)
def autobitco_in(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://autobitco.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    autobitco_in(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":"autobitco.in",
    "User-Agent":ugentmu,
  }
  dash=curl.get('https://autobitco.in/dashboard',headers=headers,cookies=cookies)
  if 'Welcome back' not in dash.text:
    save_data(host)
    autobitco_in(modulesl,banner)
  fd=bs(dash.text,'html.parser')
  koin=fd.find_all('div',{'class':'col details'})
  name=fd.find('p',{'class':'username'})
  akun=Tree("[white]> [green]Account information",guide_style="bold bright_white")
  akun.add('[yellow]Welcome back [white] : [green] '+name.text)
  rprint(akun)
  info=[]
  for i in koin:
    info.append("[yellow]"+i.text.strip().splitlines()[0].upper()+' [white]: [green]'+i.text.strip().splitlines()[2].replace(' ',''))
  menu_items = [f"[yellow][[white]{str(index)}[yellow]] {item.split(': ')[0]}: {item.split(': ')[1]}      " for index, item in enumerate(info)]
  menu_content = "\n".join(menu_items[i] + (menu_items[i + 1] if i + 1 < len(menu_items) else "") for i in range(0, len(menu_items), 2))
  cetak(Panel(menu_content, width=70, title="[bold green]Your Balance", padding=(0, 4), style="bold white"))
  get_sl=curl.get('https://autobitco.in/dashboard/shortlinks',headers=headers,cookies=cookies)
  ak=Tree("[white]> [green]Start shortlinks",guide_style="bold bright_white")
  cg=bs(get_sl.text,'html.parser')
  fct=cg.find('p',{"class":"amount"})
  ak.add('[white]> [green]Your FCT Tokens [white]: [yellow]'+fct.text)
  rprint(ak)
  sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'item'})
  del sl[0]
  del sl[0]
  del sl[0]
  def run(sl):
    jumlah=int(sl.find('span',{'id':'views'}).text.strip().split('/')[0])
    re=jumlah
    url='https://autobitco.in'+sl.find('form')['action']
    value=sl.find('input',{'name':'hh'})['value']
    for jum in range(jumlah):
      for i in range(3):
        headers_p={
          "Host":"autobitco.in",
          "content-type":"application/x-www-form-urlencoded",
          "User-Agent":ugentmu,
        }
        data="hh="+value
        get_url=curl.post(url,headers=headers_p,cookies=cookies,data=data,allow_redirects=False).headers['Location']
        answer=bypass_link(get_url,modulesl,jumlah=[str(re),str(jumlah)])
        if answer:
          if 'failed to bypass' in answer:
            pass
          else:
            get_reward=curl.get(answer,headers=headers,cookies=cookies)
            if 'successfully' in get_reward.text:
              print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+bs(get_reward.text,'html.parser').find('div',{'class':'alert alert-success'}).text.strip())
            re-=1
            break
        else:
          break
  if settings()['multi']:
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in sl]
  else:
      for i in sl:
        run(i)
def shortfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://shortfaucet.com/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['wallet'])
    shortfaucet(modulesl,banner)
  wallet=load_data(host,custom=['wallet'])['wallet']
  while True:
      url_host='shortfaucet.com'
      try:
        curl=Session()
        ua_g = {
          'Host': url_host,
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        }
        ua_p = {
          'Host': url_host,
          'origin': 'https://'+url_host,
          'content-type': 'application/x-www-form-urlencoded',
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        url=f"https://{url_host}/"
        get_data=curl.get('https://shortfaucet.com/',headers=ua_g)
        # print(get_data.text)
        # exit()
        parser=bs(get_data.text,'html.parser')
        sesi=parser.find('input',{'name':'session-token'})['value']
        key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
        atb=modulesl.antibot(get_data,name_key='div',key='modal-title w-100 text-center')
        answer=modulesl.RecaptchaV2(key,url)
        data=f'session-token={sesi}&address={wallet}&antibotlinks=+{atb}&captcha=recaptcha&g-recaptcha-response={answer}&login=Verify+Captcha'
        send_data=curl.post(url,headers=ua_p,data=data)
        #print(send_data.text)
        for ulang in range(10):
          get_sl=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g,allow_redirects=False)
          #print(get_sl.headers)
          an=bypass_link(get_sl.headers['location'],modulesl)
          if an:
            if 'failed to bypass' in an:
              pass
            else:
              #print(an)
              get_data=curl.get(an.replace('www.',''),headers=ua_g)
              #print(get_data.text)
              # <div class="alert alert-success fade show" role="alert">                              <i class="fas fa-money-bill-wave"></i> 2 satoshi was sent to your <a href="https://faucetpay.io/page/user-admin" target="_blank">FaucetPay Account</a>
              #           <button type="button" class="close d-none" data-dismiss="alert" aria-label="Close">                                                                                 <span aria-hidden="true">&times;</span>
              #           </button>                                                             </div>
              if 'alert alert-danger fade show' in get_data.text:
                print(kuning1+' > '+merah1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-danger fade show'}).text.strip().splitlines()[0])
              else:
                print(kuning1+' > '+hijau1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-success fade show'}).text.strip().splitlines()[0])
              break
          else:
            send_data=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g)
        if ulang==9:
          print('shortlinks limit')
          exit()
      except Exception as e:
        pass
def satoshitap(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://satoshitap.com/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['wallet'])
    satoshitap(modulesl,banner)
  wallet=load_data(host,custom=['wallet'])['wallet']
  while True:
      url_host='satoshitap.com'
      try:
        curl=Session()
        ua_g = {
          'Host': url_host,
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        }
        ua_p = {
          'Host': url_host,
          'origin': 'https://'+url_host,
          'content-type': 'application/x-www-form-urlencoded',
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        url=f"https://{url_host}/"
        get_data=curl.get('https://satoshitap.com/',headers=ua_g)
        # print(get_data.text)
        # exit()
        parser=bs(get_data.text,'html.parser')
        sesi=parser.find('input',{'name':'session-token'})['value']
        key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
        atb=modulesl.antibot(get_data,name_key='div',key='modal-title w-100 text-center')
        answer=modulesl.RecaptchaV2(key,url)
        data=f'session-token={sesi}&address={wallet}&antibotlinks=+{atb}&captcha=recaptcha&g-recaptcha-response={answer}&login=Verify+Captcha'
        send_data=curl.post(url,headers=ua_p,data=data)
        #print(send_data.text)
        for ulang in range(10):
          get_sl=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g,allow_redirects=False)
          #print(get_sl.headers)
          an=bypass_link(get_sl.headers['location'],modulesl)
          if an:
            if 'failed to bypass' in an:
              pass
            else:
              #print(an)
              get_data=curl.get(an.replace('www.',''),headers=ua_g)
              #print(get_data.text)
              # <div class="alert alert-success fade show" role="alert">                              <i class="fas fa-money-bill-wave"></i> 2 satoshi was sent to your <a href="https://faucetpay.io/page/user-admin" target="_blank">FaucetPay Account</a>
              #           <button type="button" class="close d-none" data-dismiss="alert" aria-label="Close">                                                                                 <span aria-hidden="true">&times;</span>
              #           </button>                                                             </div>
              if 'alert alert-danger fade show' in get_data.text:
                print(kuning1+' > '+merah1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-danger fade show'}).text.strip().splitlines()[0])
              else:
                print(kuning1+' > '+hijau1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-success fade show'}).text.strip().splitlines()[0])
              break
          else:
            send_data=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g)
        if ulang==9:
          print('shortlinks limit')
          exit()
      except Exception as e:
        pass
def esledz(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://esledz.pl/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['wallet'])
    esledz(modulesl,banner)
  wallet=load_data(host,custom=['wallet'])['wallet']
  while True:
      url_host=host
      try:
        curl=Session()
        ua_g = {
          'Host': url_host,
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        }
        ua_p = {
          'Host': url_host,
          'origin': 'https://'+url_host,
          'content-type': 'application/x-www-form-urlencoded',
          'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        url=f"https://{url_host}/"
        get_data=curl.get('https://esledz.pl/',headers=ua_g)
        # print(get_data.text)
        # exit()
        parser=bs(get_data.text,'html.parser')
        sesi=parser.find('input',{'name':'session-token'})['value']
        key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
        atb=modulesl.antibot(get_data,name_key='div',key='modal-title w-100 text-center')
        answer=modulesl.RecaptchaV2(key,url)
        data=f'session-token={sesi}&address={wallet}&antibotlinks=+{atb}&captcha=recaptcha&g-recaptcha-response={answer}&login=Verify+Captcha'
        send_data=curl.post(url,headers=ua_p,data=data)
        #print(send_data.text)
        for ulang in range(10):
          get_sl=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g,allow_redirects=False)
          #print(get_sl.headers)
          an=bypass_link(get_sl.headers['location'],modulesl)
          if an:
            if 'failed to bypass' in an:
              pass
            else:
              #print(an)
              get_data=curl.get(an,headers=ua_g)
              #print(get_data.text)
              # <div class="alert alert-success fade show" role="alert">                              <i class="fas fa-money-bill-wave"></i> 2 satoshi was sent to your <a href="https://faucetpay.io/page/user-admin" target="_blank">FaucetPay Account</a>
              #           <button type="button" class="close d-none" data-dismiss="alert" aria-label="Close">                                                                                 <span aria-hidden="true">&times;</span>
              #           </button>                                                             </div>
              print(kuning1+' > '+hijau1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-success fade show'}).text.strip().splitlines()[0])
              animasi(detik=60)
              break
          else:
            send_data=curl.get(url+send_data.text.split("""onclick="$(location).attr('href','""")[1].split("')")[0],headers=ua_g)
        if ulang==9:
          print('shortlinks limit')
          exit()
      except Exception as e:
        pass
def faucet_imatic_gr(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://faucet.imatic.gr/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['wallet'])
    faucet_imatic_gr(modulesl,banner)
  wallet=load_data(host,custom=['wallet'])['wallet']
  url_host='faucet.imatic.gr'
  while True:
    try:
      curl=Session()
      ua_g = {
        'Host': url_host,
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      }
      ua_p = {
        'Host': url_host,
        'origin': 'https://'+url_host,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      url=f"https://{url_host}/"
      get_data=curl.get('https://faucet.imatic.gr/',headers=ua_g)
      for ulang in range(10):
        get_sl=curl.get(url+get_data.text.split("""$(location).attr('href','""")[1].split("');return false;")[0],headers=ua_g,allow_redirects=False)
        #print(get_sl.headers)
        an=bypass_link(get_sl.headers['location'],modulesl)
        #print(an)
        if an:
          if 'failed to bypass' in an:
            pass
          else:
            get_data=curl.get(an,headers=ua_g)
            parser=bs(get_data.text,'html.parser')
            sesi=parser.find('input',{'type':'text'})['name']
            key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
            atb=modulesl.antibot(get_data)
            answer=modulesl.RecaptchaV2(key,url)
            data=f'{sesi}={wallet}&g-recaptcha-response={answer}&antibotlinks=+{atb}'
            send_data=curl.post(url,headers=ua_p,data=data)
            #print(send_data.text)
            if 'alert alert-danger fade show' in get_data.text:
                print(kuning1+' > '+merah1+bs(get_data.text,'html.parser').find('div',{'class':'alert alert-danger fade show'}).text.strip().splitlines()[0])
            else:
              print(kuning1+' > '+hijau1+bs(send_data.text,'html.parser').find('div',{'class':'alert alert-success'}).text.strip().splitlines()[0])
            break
        else:
          get_data=curl.get(url,headers=ua_g)
      if ulang==9:
        print('shortlinks limit')
        exit()
    except Exception as e:
      pass
def tronmaster(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://tronmaster.online/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host,custom=['wallet'])
    tronmaster(modulesl,banner)
  wallet=load_data(host,custom=['wallet'])['wallet']
  url_host='tronmaster.online'
  while True:
    try:
      curl=Session()
      ua_g = {
        'Host': url_host,
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      }
      ua_p = {
        'Host': url_host,
        'origin': 'https://'+url_host,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
      }
      url=f"https://{url_host}/"
      get_data=curl.get('https://tronmaster.online/',headers=ua_g)
      #print(get_data.text)
      for ulang in range(10):
        get_sl=curl.get(url+get_data.text.split("""$(location).attr('href','""")[1].split("');return false;")[0],headers=ua_g,allow_redirects=False)
        #print(get_sl.headers)
        an=bypass_link(get_sl.headers['location'],modulesl)
        if an:
          if 'failed to bypass' in an:
            pass
          else:
            get_data=curl.get(an,headers=ua_g)
            parser=bs(get_data.text,'html.parser')
            sesi=parser.find('input',{'type':'text'})['name']
            key=parser.find('div',{'class':'g-recaptcha'})['data-sitekey']
            atb=modulesl.antibot(get_data)
            answer=modulesl.RecaptchaV2(key,url)
            data=f'{sesi}={wallet}&g-recaptcha-response={answer}&antibotlinks=+{atb}'
            send_data=curl.post(url,headers=ua_p,data=data)
            #print(send_data.text)
            print(kuning1+' > '+hijau1+bs(send_data.text,'html.parser').find('div',{'class':'alert alert-success'}).text.strip().splitlines()[0])
            break
        else:
          get_data=curl.get(url,headers=ua_g)
      if ulang==9:
        print('shortlinks limit')
        exit()
    except Exception as e:
      pass
def chillfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://chillfaucet.in/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    chillfaucet(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  login=curl.get(f'https://{host}/',headers=headers)
  if 'https://chillfaucet.in/auth/logout' in login.text:
    print('Login Success')
    selet=bs(login.text,'html.parser').find_all('a',{'class':'d-flex align-items-center btn btn-outline border text-warning'})
    urt=0
    links=[]
    for i in selet:
      print(str(urt)+'.'+i['href'])
      urt+=1
      links.append(i['href'])
    select=links[int(input(' > '))]
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://chillfaucet.in/").netloc
    data_control(host)
    banner.banner(host.upper())
    get_links=curl.get(select,headers=headers)
    #print(get_links.text)
    link=bs(get_links.text,'html.parser').find_all('div',{'class':'col-sm-6 layout-spacing'})
    for lin in link:
      #<a href="https://onlyfaucet.com/links/go/5/LTC" class="btn btn-primary waves-effect waves-light" >Claim <span class="badge badge-info">10/10</span></a>print(i)
      jumlah=lin.find('a').find('span').text.strip().split('/')[0]
      re=int(jumlah)
      for i in range(re):
        for ulng in range(5):
          try:
            gt_l=curl.get(lin.find('a')['href'],headers=headers,allow_redirects=False).headers['location']
            if 'https://chillfaucet.in/links/currency/' in gt_l:
              cek=curl.get(lin.find('a')['href'],headers=headers)
              if 'You still have uncompleted shortlink, cancel it?' in cek.text:
                gt_l=curl.get(lin.find('a')['href'].replace('go','cancel'),headers=headers,allow_redirects=False).headers['location']
                gt_l=curl.get(gt_l,headers=headers,allow_redirects=False).headers['location']
            answer=bypass_link(gt_l,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'success' in get_reward.text:
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
          except Exception as e:
            keluar(str(e))
            pass
  else:
    save_data(host)
    chillfaucet(modulesl,banner)
def freeltc_o(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://freeltc.online/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    freeltc_o(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  login=curl.get(f'https://freeltc.online/links/currency/ltc',headers=headers)
  if 'Logout' in login.text:
    print(hijau1+'Login Success')
    get_sl=curl.get('https://freeltc.online/links/currency/ltc',headers=headers)
    data_sl=bs(get_sl.text,'html.parser').find_all('div',{'class':'card card-body text-center'})
    def run(sl):
     #try:
      jumlah=int(sl.find('span',{'class':'badge badge-info'}).text.split('/')[0])
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
         #try:
          get_link=curl.get(sl.find('a')['href'],headers=headers,allow_redirects=False)
          if 'https://freeltc.online/links/currency/' in get_link.headers['location']:
              cek=curl.get(sl.find('a')['href'],headers=headers)
              if 'You still have uncompleted shortlink, cancel it?' in cek.text:
                gt_l=curl.get(sl.find('a')['href'].replace('go','cancel'),headers=headers,allow_redirects=False).headers['location']
                get_link=curl.get(gt_l,headers=headers,allow_redirects=False).headers['location']
          answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
          if answer:
            if 'failed to bypass' in answer:
              pass
            else:
              get_reward=curl.get(answer,headers=headers)
              if 'Success!' in get_reward.text:
                print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
              re-=1
          break
    #     except Exception as e:
    #       keluar(str(e))
    #       pass
    # except Exception as e:
    #       keluar(str(e))
    #       pass
    if settings()['multi']:
      
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in data_sl]
    else:
      for i in data_sl:
        run(i)
    get_sl=curl.get('https://freeltc.online/links/withdraw/LTC',headers=headers)
    print(putih1+'┣━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_sl.text.split("html: '")[1].split("',")[0])
  else:
    save_data(host)
    freeltc_o(modulesl,banner)
def proinfinity(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://proinfinity.fun/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    proinfinity(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"application/json, text/plain, */*",
    "content-type":"application/json",
    "User-Agent":ugentmu
  }
  login=curl.post(f'https://proinfinity.fun/infos/global_info',headers=headers).json()
  if login['success']:
    akun=Tree("[green]> [yellow]Account information",guide_style="bold bright_white")
    akun.add('[green]> Email [white]: [yellow]'+login['user']['email'])
    akun.add('[green]> Balance [white]: [yellow]'+login['user']['coins'])
    rprint(akun)
    rprint(Tree("[green]> [yellow]Start shortlinks",guide_style="bold bright_white"))
    get_sl=curl.post('https://proinfinity.fun/infos/auth_page_info',headers=headers,data=json.dumps({"page":"sl"})).json()
    def run(sl):
     try:
      print(sl)
      jumlah=sl['views24Hours']
      re=jumlah
      for u in range(jumlah):
       for ytta in range(5):
        try:
          get_link=curl.post('https://proinfinity.fun/user/generateSl',headers=headers,data=json.dumps({"slId":sl['_id'],"vote":None,"type":None}),allow_redirects=False).json()
          if get_link['success']:
            get_link=get_link['shortenedUrl']
            answer=bypass_link(get_link,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'success' in get_reward.url:
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+unquote(get_reward.url).split('=')[1])
                re-=1
                break
        except Exception as e:
          keluar(str(e))
          pass
     except Exception as e:
          keluar(str(e))
          pass
    if settings()['multi']:
        with ThreadPoolExecutor(max_workers=5) as executor:
          futures = [executor.submit(run, i) for i in get_sl['sls']]
    else:
      for i in get_sl['sls']:
        run(i)
    exit()
  else:
    save_data(host)
    proinfinity(modulesl,banner)
def bitfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://bitfaucet.net/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    bitfaucet(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  login=curl.get(f'https://{host}/',headers=headers)
  if 'https://bitfaucet.net/auth/logout' in login.text:
    print('Login Success')
    selet=bs(login.text,'html.parser').find_all('a')
    urt=0
    links=[]
    for i in selet:
      if 'links/' in i['href']:
        print(str(urt)+'.https://bitfaucet.net'+i['href'])
        urt+=1
        links.append('https://bitfaucet.net'+i['href'])
    select=links[int(input(' > '))]
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://bitfaucet.net/").netloc
    data_control(host)
    banner.banner(host.upper())
    get_links=curl.get(select,headers=headers)
    #print(get_links.text)
    link=bs(get_links.text,'html.parser').find_all('div',{'class':'col-sm-6 layout-spacing'})
    for lin in link:
      #<a href="https://onlyfaucet.com/links/go/5/LTC" class="btn btn-primary waves-effect waves-light" >Claim <span class="badge badge-info">10/10</span></a>print(i)
      jumlah=lin.find('a').find('span').text.strip().split('/')[0]
      re=int(jumlah)
      for i in range(re):
        for ulng in range(5):
          try:
            gt_l=curl.get(lin.find('a')['href'],headers=headers,allow_redirects=False).headers['location']
            if 'https://bitfaucet.net/links/currency/' in gt_l:
              cek=curl.get(lin.find('a')['href'],headers=headers)
              if 'You still have uncompleted shortlink, cancel it?' in cek.text:
                gt_l=curl.get(lin.find('a')['href'].replace('go','cancel'),headers=headers,allow_redirects=False).headers['location']
                gt_l=curl.get(gt_l,headers=headers,allow_redirects=False).headers['location']
            answer=bypass_link(gt_l,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'success' in get_reward.text:
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
          except Exception as e:
            keluar(str(e))
            pass
  else:
    save_data(host)
    bitfaucet(modulesl,banner)
def satoshifaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://satoshifaucet.io/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    satoshifaucet(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  login=curl.get(f'https://{host}/',headers=headers)
  if 'https://satoshifaucet.io/auth/logout' in login.text:
    print('Login Success')
    selet=bs(login.text,'html.parser').find_all('a')
    urt=0
    links=[]
    for i in selet:
      if 'links/' in i['href']:
        print(str(urt)+'.https://satoshifaucet.io'+i['href'])
        urt+=1
        links.append('https://satoshifaucet.io'+i['href'])
    select=links[int(input(' > '))]
    os.system('cls' if os.name == 'nt' else 'clear')
    host=urlparse("https://satoshifaucet.io/").netloc
    data_control(host)
    banner.banner(host.upper())
    get_links=curl.get(select,headers=headers)
    #print(get_links.text)
    link=bs(get_links.text,'html.parser').find_all('div',{'class':'col-sm-6 layout-spacing'})
    for lin in link:
      #<a href="https://onlyfaucet.com/links/go/5/LTC" class="btn btn-primary waves-effect waves-light" >Claim <span class="badge badge-info">10/10</span></a>print(i)
      jumlah=lin.find('a').find('span').text.strip().split('/')[0]
      re=int(jumlah)
      for i in range(re):
        for ulng in range(5):
          try:
            gt_l=curl.get(lin.find('a')['href'],headers=headers,allow_redirects=False).headers['location']
            if 'https://satoshifaucet.io/links/currency/' in gt_l:
              cek=curl.get(lin.find('a')['href'],headers=headers)
              if 'You still have uncompleted shortlink, cancel it?' in cek.text:
                gt_l=curl.get(lin.find('a')['href'].replace('go','cancel'),headers=headers,allow_redirects=False).headers['location']
                gt_l=curl.get(gt_l,headers=headers,allow_redirects=False).headers['location']
            answer=bypass_link(gt_l,modulesl,jumlah=[str(re),str(jumlah)])
            if answer:
              if 'failed to bypass' in answer:
                pass
              else:
                get_reward=curl.get(answer,headers=headers)
                if 'success' in get_reward.text:
                  print(putih1+'┃  ┗━━'+hijau1+f' {putih1}[{hijau1} √ {putih1}] {hijau1}'+get_reward.text.split("html: '")[1].split("',")[0])
                re-=1
            break
          except Exception as e:
            keluar(str(e))
            pass
  else:
    save_data(host)
    satoshifaucet(modulesl,banner)
def larvelfaucet(modulesl,banner):
  os.system('cls' if os.name == 'nt' else 'clear')
  host=urlparse("https://larvelfaucet.com/").netloc
  data_control(host)
  banner.banner(host.upper())
  if not os.path.exists(f"data/{host}/{host}.json"):
    save_data(host)
    larvelfaucet(modulesl,banner)
  cookies, ugentmu = load_data(host)
  cookiek = SimpleCookie()
  cookiek.load(cookies)
  cookies = {k: v.value for k, v in cookiek.items()}
  curl=Session()
  curl.cookies.update(cookies)
  headers={
    "Host":host,
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":ugentmu
  }
  sl=curl.get('https://larvelfaucet.com/short-urls',headers=headers,cookies=cookies)
  if 'https://larvelfaucet.com/logout' not in sl.text:
    save_data(host)
    larvelfaucet(modulesl,banner)
  tokn=bs(sl.text,'html.parser').find('input',{'name':'_token'})['value']
  akun=Tree("[white]> [green]Account information",guide_style="bold bright_white")
  akun.add('[yellow]Balance [white] : [green] '+bs(sl.text,'html.parser').find('a',{'class':'btn btn-lg btn-default'}).text.strip())
  rprint(akun)
  sli=bs(sl.text,'html.parser').find_all('div',{'class':'col-md-4 col-lg-3 pb-3'})
  rprint(Tree("[white]> [green]Start Shortlinks",guide_style="bold bright_white"))
  for link in sli:
    try:
      while True:
        id_=link.find('button',{'class':'btn btn-lg btn-block bg-success text-center short-url rounded-0'})['data-id']
        s=curl.post('https://larvelfaucet.com/short-urls/get_link',data=f'id={id_}&_token={tokn}',headers={
        "Host": "larvelfaucet.com",
        "X-T-EVNT": "1",
        "X-CSRF-TOKEN": tokn,
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept": "*/*",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://larvelfaucet.com/short-urls"
    },cookies=cookies).json()
        if s['success']:
          answer=bypass_link(s['goto'],modulesl)
          if answer:
              get_reward=curl.get(answer,cookies=cookies)
              if 'Your account have been credited' in get_reward.text:
                print(bs(get_reward.text,'html.parser').find('div',{'class':'alert alert-success alert-dismissable fade show'}).text.strip())
          elif answer==None:
            break
          else:
            break
        else:break
    except Exception as e:pass
  exit()
#--------------- off ---------------#
