from mrbadutmodul import modulesl,banner
import requests,json,time
from os import system
import shutil,os
from time import sleep
from bs4 import BeautifulSoup as bs
from http.cookies import SimpleCookie
from tqdm import tqdm
from pyfiglet import figlet_format 
import os

def delete_folder(folder_name):

    try:

        # Mendapatkan path lengkap folder saat ini

        current_directory = os.getcwd()

        # Menggabungkan path folder saat ini dengan nama folder yang akan dihapus

        folder_path = os.path.join(current_directory, folder_name)

        # Menghapus folder beserta isinya

        shutil.rmtree(folder_path)

        #print("Folder berhasil dihapus.")

    except Exception as e:

        #print("Terjadi kesalahan saat menghapus folder:", str(e))

# Contoh penggunaan fungsi

folder_name = 'nama_folder_yang_akan_dihapus'

delete_folder(folder_name)



def main():
  system('clear')
  banner.banner("BTCCAYON")
  def cek():
      file_sizes = []
      for i in range(5):
          file_size = os.path.getsize(f'{i}.jpg')
          file_sizes.append(file_size)
      
      while True:
          for i in range(5):
              if file_sizes[i] != file_sizes[0] and file_sizes[i] != file_sizes[i-1]:
                  return i
  def get_answer():
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
          with open(file_name, 'wb') as f:
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
  hijau1 = "\033[1;92m"#Terang
  kuning1 = "\033[1;93m"#Terang
  putih1 = "\033[1;97m"#Terang
  merah1 = "\033[1;91m"#Terang
  biru1 = "\033[1;94m"#Terang
  def save_data():
      cookies=input(hijau1+'masukan cookies mu > ')
      user_agent=input(hijau1+'masukan User-Agent mu > ')
      data = {
          'cookies': cookies,
          'user_agent': user_agent
      }
      # Menyimpan data dalam format JSON
      with open('btccanyon.json', 'w') as file:
          json.dump(data, file)
  def load_data():
      try:
          with open('btccanyon.json', 'r') as file:
              data = json.load(file)
          cookies = data['cookies']
          user_agent = data['user_agent']
          return cookies, user_agent
      except FileNotFoundError:
          return None, None
  cookies, ugentmu = load_data()
  if not os.path.exists("btccanyon.json"):
    save_data()
    main()
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
    save_data()
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
        'clks.pro': module_sl.clks_pro,
        'linksly.co': module_sl.linksly,
        'shrinkearn.com': module_sl.shrinkearn,
        'fc.lc': module_sl.fl_lc,
        'clk.sh': module_sl.clksh,
        'linksfly.me': module_sl.linksfly,
        'chainfo.xyz': module_sl.chainfo,
        'flyzu.icu': module_sl.flyzu,
        'adshorti.xyz': module_sl.adshorti_xyz,
        'usalink.io': module_sl.usalink,
        'birdurls.com': module_sl.birdurl,
        'owllink.net': module_sl.owlink,
        'clickzu.icu': module_sl.clickzu_icu,
        'zuba.link': module_sl.zuba_link,
        'mitly.us': module_sl.mitly,
        'illink.net': module_sl.illink_net,
        'exe.io': module_sl.exe_io,
        'insfly.pw': module_sl.insfly,
        'linkvor.pw': module_sl.linkvor_pw,
        'linkjust.com': module_sl.linkjust,
        'cashurl.win': module_sl.cashurl_win,
        'shorti.io': module_sl.shorti_io,
        'oii.io': module_sl.oii,
        'ex-foary.com': module_sl.ex_foary_com,
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
    token=get_sl.text.split("var token = '")[1].split("';")[0]
    answer=module_sl.RecaptchaV2('6LdzF6MlAAAAACcN9JGXW8tSs4dy1MjeKZKFJ11M',get_sl.url)
    g=json.loads(curl.post('https://btccanyon.com/system/ajax.php',headers={"User-Agent":ugentmu,"content-type":"application/x-www-form-urlencoded; charset=UTF-8","accept":"application/json, text/javascript, */*; q=0.01"},data=f"a=getFaucet&token={token}&captcha=1&challenge=false&response={answer}",cookies=cookies).text)
    if g["status"] == 200:
      gas=bs(g["message"],"html.parser").find("div",{"class":"alert alert-success"}).text
      print(hijau1+'[ '+kuning1+'>'+hijau1+' ] '+gas.strip())
      print(hijau1+'[ '+kuning1+'+'+hijau1+' ] '+balance())
      for i in tqdm (range (int(600)), leave=False,desc="Please wait..."):
            time.sleep(1)
            pass
  
