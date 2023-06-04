import requests,json,time
from os import system
import shutil,os
from time import sleep
from bs4 import BeautifulSoup as bs
from http.cookies import SimpleCookie
from tqdm import tqdm
from pyfiglet import figlet_format 
import pathlib
def animasi(menit):
  detik = menit * 60
  pattern_list = list("▁▃▅▇▅▃▁") * detik
  for i in range(detik):
      animasi = "".join(pattern_list[i:i+5])
      output = f"[{animasi}] - Please wait {detik//60:02d}:{detik%60:02d}"
      print(output, end='\r')
      time.sleep(1)
      detik -= 1
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
      cookies=input(hijau1+'masukan cookies mu > ')
      user_agent=input(hijau1+'masukan User-Agent mu > ')
      data = {
          'cookies': cookies,
          'user_agent': user_agent
      }
      # Menyimpan data dalam format JSON
      with open(f'data/{name}/{name}.json', 'w') as file:
          json.dump(data, file)
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
  system('clear')
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
    print(hijau1+"> "+biru1+"Account information")
    get_inf=bs(get_sl.text,'html.parser').find_all('div',{'class':'col-9 no-space'})
    for info in get_inf:
      print(hijau1+'> '+info.text.strip())
  except Exception as e:
    save_data('btccanyon')
    main()
  print(hijau1+"> "+biru1+"Start working on ptc")
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
  print(hijau1+"> "+biru1+"Start Bypassing Shortlinks")
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
        'chainfo.xyz': modulesl.chainfo,
        'flyzu.icu': modulesl.flyzu,
        'adshorti.xyz': modulesl.adshorti_xyz,
        'usalink.io': modulesl.usalink,
        'birdurls.com': modulesl.birdurl,
        'owllink.net': modulesl.owlink,
        'clickzu.icu': modulesl.clickzu_icu,
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
   except:pass
  print(hijau1+'[ '+kuning1+'√'+hijau1+' ] '+"Success bypassing all shortlinks ;)")
  print(hijau1+"> "+biru1+"Bypass faucet")
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
            pass
def coingax(modulesl,banner):
  system('clear')
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
  print(hijau1+"> "+biru1+"Account information")
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
   except:
     pass
def claimsatoshi(modulesl,banner):
  system('clear')
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
  print(hijau1+"> "+biru1+"Account information")
  for info in info:
    print(hijau1+'> '+info.text.strip().splitlines()[1]+' : '+info.text.strip().splitlines()[0])
  print(hijau1+"> "+biru1+"Start ptc")
  ptc=curl.get('https://claimsatoshi.xyz/ptc',headers=ua,cookies=cookies)
  surf=bs(ptc.text,'html.parser').find_all('div',{'class':'col-12 col-lg-4 mb-3 mb-lg-0'})
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
  print(hijau1+"> "+biru1+"Start shortlinks")
  gt_link = curl.get('https://claimsatoshi.xyz/links', headers=ua, cookies=cookies)
  gtf = bs(gt_link.text, 'html.parser')
  gt_info = gtf.find_all('div', {'class': 'col-12 col-lg-4 mb-3 mb-lg-0'})
  def process_link(link, bypass_function):
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
      process_link(link, modulesl.cuty_io)
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
      process_link(link, modulesl.link1s_net)
  print(hijau1+"> "+biru1+"Start auto faucet")
  while True:
   try:
    get_=curl.get('https://claimsatoshi.xyz/auto',headers=ua,cookies=cookies)
    token=bs(get_.text,'html.parser').find('input',{'name':'token'})['value']
    sleep(15)
    reward=curl.post('https://claimsatoshi.xyz/auto/verify',headers={"user-agent":ugentmu,"content-type":"application/x-www-form-urlencoded"},cookies=cookies,data="token="+token)
    if 'Good job!' in reward.text:
      print(f'{putih1}[{hijau1} √ {putih1}] {hijau1}'+reward.text.split('<script> Swal.fire(')[1].split(')</script>')[0].replace("'","").replace(',',''))
   except:
     break
     pass
  print(hijau1+"> "+biru1+"Start faucet")
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
    
    