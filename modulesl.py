import re,json,time,uuid
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse,urlencode
import cloudscraper
import re
import base64,random
from time import sleep
import urllib.parse
import requests
from bs4 import BeautifulSoup as bs
import concurrent.futures
# -------------------------------------------
# RecaptchaV2 BYPASS

def get_res(api, key, url):
    return requests.get(f'http://ocr.captchaai.com/in.php?key={api}&method=userrecaptcha&googlekey={key}&pageurl={url}').text

def get_ans(api, id):
    return requests.get(f'http://ocr.captchaai.com/res.php?key={api}&action=get&id={id}').text

def RecaptchaV2(key, url):
    with open('ckey.txt') as f:
        api_list = f.read().splitlines()

    while True:
        api = random.choice(api_list)
        get_res_text = get_res(api, key, url)

        if 'OK' in get_res_text:
            id = get_res_text.split('|')[1]
            start_time = time.time()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                while True:
                    time.sleep(1)  # Mengurangi waktu tunggu menjadi setengah detik

                    get_ans_text = get_ans(api, id)
                    elapsed_time = time.time() - start_time

                    if 'CAPCHA_NOT_READY' in get_ans_text:
                        print('Belum ada respon dari reCAPTCHA', end='\r')
                    elif 'OK' in get_ans_text:
                        return get_ans_text.split('|')[1]
        else:
            print('Get ID', end='\r')

# -------------------------------------------
# Hcaptcha BYPASS
def Hcaptcha(key,url):
  api=random.choice(open('2key.txt').read().splitlines())
  get_res=requests.get(f'https://2captcha.com/in.php?key={api}&method=hcaptcha&sitekey={key}&pageurl={url}').text
  if 'OK' in get_res:
    status=False
    id=get_res.split('|')[1]
    while(status==False):
      try:
        get_ans=requests.get(f'https://2captcha.com/res.php?key={api}&action=get&id={id}').text
        sleep(20)
        if 'CAPCHA_NOT_READY' in get_ans:
          print(get_ans,end='                     \r')
        if 'OK' in get_ans:
          return get_ans.split('|')[1]
          status =True
      except Exception as e:
        print(e)
        pass
  else:
    print('Api Key is no longer available : '+ api,end='\r')
# -------------------------------------------
# RecaptchaV3 BYPASS
def RecaptchaV3(ANCHOR_URL):
    url_base = 'https://www.google.com/recaptcha/'
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = requests.Session()
    client.headers.update({
        'content-type': 'application/x-www-form-urlencoded'
    })
    matches = re.findall('([api2|enterprise]+)\/anchor\?(.*)', ANCHOR_URL)[0]
    url_base += matches[0]+'/'
    params = matches[1]
    res = client.get(url_base+'anchor', params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    params = dict(pair.split('=') for pair in params.split('&'))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(url_base+'reload', params=f'k={params["k"]}', data=post_data)
    answer = re.findall(r'"rresp","(.*?)"', res.text)[0]    
    return answer


  # -------------------------------------------
def one_method(curl,url,headers=None):
 try:
  host=urlparse(url).netloc
  final = curl.get(url,headers=headers).text
  sleep(15)
  bs4 = BeautifulSoup(final, "html.parser")
  inputs = bs4.find_all("input")
  data = urlencode({input.get("name"): input.get("value") for input in inputs})
  get_url = curl.post(f'https://{host}/links/go', headers={'x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8',"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"}, data=data).json()
  if get_url['status'] == 'success':
      return get_url["url"]
  sesi = False
 except Exception as e:
   return 'failed to bypass'
def ctrsh(url):
  try:
    url_g=url
    curl=requests.Session()
    step1=curl.get('https://sinonimos.de/?url8j='+url).text
    url=step1.split('<script>window.location.href = "')[1].split('";</script>')[0]
    status=False
    while(status==False):
      step2=curl.get(url).text
      url_p=json.loads(step2.split('var Wtpsw = ')[1].split(';')[0])
      #sleep(20)
      data=f"action=wtpsw_post_view_count&is_ajax=1&post_id={url_p['post_view_count']}&nonce={url_p['data_nonce']}"
      step3=curl.post(url_p['ajaxurl'],data=data,headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8"})
      answer=RecaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lc1s5skAAAAAGriR94-62GGlgzdn-plGUpFQ_pf&co=aHR0cHM6Ly9zaW5vbmltb3MuZGU6NDQz&hl=id&v=6MY32oPwFCn9SUKWt8czDsDw&size=invisible&cb=pyan7vozvr5o')
      step4=curl.post(url,data=f"g-recaptcha-response={answer}&validator=true",headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8"},allow_redirects=False)
      if "location" not in step4.headers:
        t=step4.text
        url=t.split('<script>window.location.href = "')[1].split('"</script>')[0].split('&tk=')[1]
        tk=urlparse(url_g)
        step5=curl.get(f'https://{tk.hostname}{tk.path}/?token='+url).text
        fl=bs(step5,'html.parser')
        lin=fl.find('form',{'id':'go-link'})['action']
        csrf=fl.find('input',{'name':'_csrfToken'})["value"]
        tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
        form=fl.find('input',{'name':'ad_form_data'})["value"]
        tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
        data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
        sleep(5)
        final=curl.post('https://'+tk.hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
        if json.loads(final.text)["status"] == "success":
          sleep(15)
          return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def try2(url):
  #try:
    curl = requests.Session()
    curl.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'})
    sesi = True
    url = curl.get(url)
    step1 = curl.post('https://'+urlparse(url.url).hostname+'/wp-admin/admin-ajax.php', data="action=remove_short_main_session", headers={'x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'}).text
    send_data = json.loads(step1)
    if send_data["success"]:
        url = send_data["data"]["alias"]
    while(sesi==True):
        curl.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'})
       # print(url)
        if "try2link.com" in url:
                break
        step1 = curl.get(url)
        send_data = curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+'/wp-admin/admin-ajax.php', data="action=remove_short_main_session", headers={'x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'})
     #   print(send_data.text)
        if "alias" and "success" in send_data.text:
            send_data = json.loads(send_data.text)
            url = send_data["data"]["alias"]
       #     print(url)
            if "try2link.com" in url:
                break
        else:
            url = BeautifulSoup(step1.text, 'html.parser').find('a', {'id':'go_d'})["href"]
    res=one_method(curl,url,headers=None)
    sleep(15)
    return res
 # except Exception as e:
  #  return "failed to bypass"
def gplinks_bypass(url: str):
  try:
   client = cloudscraper.create_scraper(allow_brotli=False)  
   domain ="https://gplinks.co/"
   referer = "https://mynewsmedia.co/"
  
   vid = client.get(url, allow_redirects= False).headers["Location"].split("=")[-1]
   url = f"{url}/?{vid}"
  
   response = client.get(url, allow_redirects=False)
   soup = BeautifulSoup(response.content, "html.parser")
      
      
   inputs = soup.find(id="go-link").find_all(name="input")
   data = { input.get('name'): input.get('value') for input in inputs }
      
   time.sleep(15)
   headers={"x-requested-with": "XMLHttpRequest"}
   bypassed_url = client.post(domain+"links/go", data=data, headers=headers).json()["url"]
   sleep(15)
   return bypassed_url
  except:
    return "failed to bypass" 
def droplink(url):
      try:
          client = requests.Session()
          res = client.get(url, timeout=5)
          ref = re.findall("action[ ]{0,}=[ ]{0,}['|\"](.*?)['|\"]", res.text)[0]
          h = {"referer": ref}
          res = client.get(url, headers=h)
          bs4 = BeautifulSoup(res.content, "html.parser")
          inputs = bs4.find_all("input")
          data = {input.get("name"): input.get("value") for input in inputs}
          h = {
              "content-type": "application/x-www-form-urlencoded",
              "x-requested-with": "XMLHttpRequest",
          }
          p = urlparse(url)
          final_url = f"{p.scheme}://{p.netloc}/links/go"
          sleep(15)
          res = client.post(final_url, data=data, headers=h).json()
          if res["status"] == "success":
              sleep(15)
              return res["url"]
          return None
      except Exception as e:
        return "failed to bypass"
def cuty_io(url):
 try:
  curl=requests.Session()
  step1=curl.get(url,headers={'User-Agent': 'XYZ/3.0'})
  token=bs(step1.text,'html.parser').find('input',{"name":"_token"})["value"]
  step2=curl.post(step1.url,data=f"_token={token}",headers={'User-Agent':'XYZ/3.0','content-type':'application/x-www-form-urlencoded'}).text
  fd=bs(step2,'html.parser')
  token=bs(step2,'html.parser').find('input',{"name":"_token"})["value"]
  answer=RecaptchaV2(key=fd.find('button',{"class":"g-recaptcha submit-button"})["data-sitekey"],url=step1.url)
  data=f"_token={token}&g-recaptcha-response={answer}"
  step3=curl.post(step1.url,data=data,headers={'User-Agent':'XYZ/3.0','content-type':'application/x-www-form-urlencoded'}).text
  sleep(15)
  fd=bs(step3,'html.parser')
  link=fd.find('form',{"id":"submit-form"})["action"]
  token=fd.find('input',{"name":"_token"})["value"]
  data=fd.find('input',{"name":"data"})["value"]
  vistor=fd.find('input',{"name":"visitor_id"})["value"]
  final=curl.post(link,data=f"_token={token}&data={urllib.parse.quote_plus(data)}&visitor_id={vistor}",headers={'User-Agent':'XYZ/3.0','content-type':'application/x-www-form-urlencoded'},allow_redirects=False)
  sleep(15)
  return final.headers['location']
 except Exception as e:
    return "failed to bypass"
def shortfly(url):
  try:
    url=urlparse(url)
    y=requests.get('https://shortsfly.me/flyinc.'+url.path,allow_redirects=False,headers={"referer":"https://shinbhu.net/things-you-should-never-do-on-an-interview-it-will-kill-your-chances/"}).headers
    sleep(15)
    return y["Location"]
  except Exception as e:
    return "failed to bypass"
def linksfly(url):
  try:
    url=urlparse(url)
    y=requests.get('https://linksfly.me/flyinc.'+url.path,allow_redirects=False,headers={"referer":"https://shinbhu.net/things-you-should-never-do-on-an-interview-it-will-kill-your-chances/"}).headers
    sleep(15)
    return y["Location"]
  except Exception as e:
    return "failed to bypass"
def exe_io(url):
 try:
  curl=requests.Session()
  step1=curl.get(url,headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"})
  tf=bs(step1.text,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f"_method=POST&_csrfToken={csrf}&extraPage=&ref=&f_n=sle&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}"
  step2=curl.post(step1.url,data=data,headers={"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  tf=bs(step2,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
  toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  ref=tf.find('input',{'name':'ref'})["value"]
  get_key=json.loads(step2.split('var app_vars = ')[1].split(';')[0])["invisible_reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=step1.url)
  data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
  step2=curl.post(step1.url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  sleep(15)
  fl=bs(step2,"html.parser")
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post('https://'+urlparse(step1.url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;',"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"})
  if json.loads(final.text)["status"] == "success":
    sleep(15)
    return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def fl_lc(url):
  try:
    curl=requests.Session()
    step1=curl.get(url)
    fd=bs(step1.text,'html.parser')
    id=fd.find('form')['id']
    url_p=fd.find('form')['action']
    form=fd.find('input',{'name':'ad_form_data'})['value']
    token=fd.find('input',{'name':'random_token'})['value']
    visitor=fd.find('input',{'name':'visitor'})['value']
    alias=fd.find('input',{'name':'alias'})["value"]
    sitkey=fd.find('button',{'class':'g-recaptcha btn btn-primary'})['data-sitekey']
    answer=RecaptchaV2(key=sitkey,url=step1.url)
    data=f'ad_form_data={urllib.parse.quote_plus(form)}&random_token={token}&visitor={visitor}&alias={alias}&g-recaptcha-response={answer}'
    step2=curl.post(url_p,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
    fd=bs(step2.text,'html.parser')
    url_p=fd.find('form')['action']
    form=fd.find('input',{'name':'ad_form_data'})['value']
    token=fd.find('input',{'name':'random_token'})['value']
    visitor=fd.find('input',{'name':'visitor'})['value']
    data=f'ad_form_data={urllib.parse.quote_plus(form)}&random_token={token}&visitor={visitor}'
    step3=curl.post(url_p,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
    fd=bs(step3.text,'html.parser')
    url_p=fd.find('form')['action']
    form=fd.find('input',{'name':'ad_form_data'})['value']
    token=fd.find('input',{'name':'random_token'})['value']
    visitor=fd.find('input',{'name':'visitor'})['value']
    tkf=fd.find('input',{'name':'_Token[fields]'})["value"]
    tku=fd.find('input',{'name':'_Token[unlocked]'})["value"]
    sitkey=fd.find('div',{'class':'g-recaptcha m-2'})['data-sitekey']
    answer=RecaptchaV2(key=sitkey,url=step3.url)
    data=f'_method=POST&ad_form_data={urllib.parse.quote_plus(form)}&random_token={token}&visitor={visitor}&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    step4=curl.post(url_p,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
    sleep(15)
    fd=bs(step4.text,'html.parser')
    form=fd.find('input',{'name':'ad_form_data'})['value']
    token=fd.find('input',{'name':'random_token'})['value']
    visitor=fd.find('input',{'name':'visitor'})['value']
    tkf=fd.find('input',{'name':'_Token[fields]'})["value"]
    tku=fd.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&ad_form_data={urllib.parse.quote_plus(form)}&random_token={token}&visitor={visitor}&ab=2&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post('https://fc.lc/links/go',data=data,headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8"})
    if json.loads(final.text)["status"] == "success":
        sleep(15)
        return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def clks_pro(url):
 if 'http://' in url:
   url=url.replace('http://','https://')
 def _main(url):
   for i in range(3):
     try:
      curl=requests.Session()
      ua={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
      get_url=curl.get(url,headers=ua)
      bs4 = BeautifulSoup(get_url.content, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      get_link=curl.post('https://mdn.lol/blog/',headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","referer":url,"content-type":"application/x-www-form-urlencoded"},data=data,allow_redirects=False)
      cek=curl.get('https://mdn.lol/?redirect_to=random',headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","referer":"https://t.co/"})
      bs4 = BeautifulSoup(cek.content, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      sitkey=bs4.find('div',{'class':'g-recaptcha'})['data-sitekey']
      data["g-recaptcha-response"]=RecaptchaV2(sitkey,cek.url)
      step1=curl.post('https://mdn.lol/?redirect_to=random',headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","referer":cek.url,"content-type":"application/x-www-form-urlencoded"},data=data,allow_redirects=False).headers['Location']
      step1=curl.post(step1,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","referer":cek.url,"content-type":"application/x-www-form-urlencoded"},data=data)
      for i in range(5):
        bs4 = BeautifulSoup(step1.content, "html.parser")
        inti=bs4.find('div',{"style":"margin: 10px 0 10px 0;position: relative;"})
        inputs = inti.find_all("input")
        data = {input.get("name"): input.get("value") for input in inputs}
        step1=curl.post(step1.url,data=data,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","referer":step1.url,"content-type":"application/x-www-form-urlencoded"},allow_redirects=False)
        res=step1.headers['location']
        if 'redirect_to=random' in step1.headers['location']:
          step1=curl.get('https://mdn.lol/?redirect_to=random',headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","referer":step1.url,"content-type":"application/x-www-form-urlencoded"})
        sleep(15)
      sleep(15)
      if '&url=' in res:
        res=res.split('&url=')
        res=res[len(res)-1]
      return res
     except:pass
 res=_main(url)
 if 'https://clks.pro/' in res:
   res=_main(url)
   return res
 else:
   return res
def shrinkme(url):
  try:
    curl=requests.Session()
    step1=curl.get(url).text
    tf=bs(step1,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
    toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    ref=tf.find('input',{'name':'ref'})["value"]
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url=url)
    data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
    step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;'}).text
    sleep(15)
    fl=bs(step2,"html.parser")
    lin=fl.find('form',{'id':'go-link'})['action']
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def shrinkearn(url):
  try:
    curl=requests.Session()
    step1=curl.get(url).text
    fl=bs(step1,'html.parser')
    url_post=fl.find('form')["action"]
    token=fl.find('input',{'name':'token'})["value"]
    ct=fl.find('input',{'name':'c_t'})["value"]
    cd=fl.find('input',{'name':'c_d'})["value"]
    alias=fl.find('input',{'name':'alias'})["value"]
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url=url)
    data=f'url={urllib.parse.quote_plus(url)}&token={urllib.parse.quote_plus(token)}&c_d={cd}&c_t={ct}&alias={alias}&g-recaptcha-response={answer}&submit='
    step2=curl.post(url_post,data=data,headers={'content-type':'application/x-www-form-urlencoded'}).text
    fl=bs(step2,'html.parser')
    url_post=fl.find('form',{'id':'getmylink'})["action"]
    token=fl.find('input',{'name':'token'})["value"]
    ct=fl.find('input',{'name':'c_t'})["value"]
    cd=fl.find('input',{'name':'c_d'})["value"]
    alias=fl.find('input',{'name':'alias'})["value"]
    data=f'token={token}&c_d={cd}&c_t={ct}&alias={alias}'
    step3=curl.post(url_post,data=data,headers={'content-type':'application/x-www-form-urlencoded'}).text
    fl=bs(step3,'html.parser')
    sleep(15)
    lin=fl.find('form',{'id':'go-link'})['action']
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    data=f'_method=POST&ad_form_data={urllib.parse.quote_plus(form)}'
    final=curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
        sleep(15)
        return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def clksh(url):
  try:
    curl=requests.Session()
    step1=curl.get(url)
    tf=bs(step1.text,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
    toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&action=continue&page=2&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
    step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded'}).text
    tf=bs(step2,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
    toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&action=continue&page=2&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
    get_key=json.loads(step2.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    resv2=RecaptchaV2(key=get_key,url=url)
    data=f'_method=POST&_csrfToken={csrf}&action=captcha&f_n=slc&g-recaptcha-response={resv2}&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
    step3=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded'}).text
    sleep(10)
    fl=bs(step3,'html.parser')
    lin=fl.find('form',{'id':'go-link'})['action']
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'}).text
    if json.loads(final)["status"] == "success":
      sleep(15)
      return json.loads(final)["url"]
  except Exception as e:
    return "failed to bypass"
def usalink(url):
  try:
    curl=requests.Session()
    url_base=urlparse(url)
    step1=curl.get('https://go.theconomy.me/'+url_base.path).text
 #   print(step1)
    fin=bs(step1,'html.parser')
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url='https://go.theconomy.me/'+url_base.path)
    csrf=fin.find('input',{'name':'_csrfToken'})["value"]
    tkf=fin.find('input',{'name':'_Token[fields]'})["value"]
    tku=fin.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    step2=curl.post('https://go.theconomy.me'+url_base.path,data=data,headers={"content-type":"application/x-www-form-urlencoded"}).text
    fl=bs(step2,'html.parser')
    lin=fl.find('form',{'id':'go-link'})['action']
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={urllib.parse.quote_plus(csrf)}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={urllib.parse.quote_plus(tkf)}&_Token%5Bunlocked%5D={urllib.parse.quote_plus(tku)}'
    sleep(15)
    final=curl.post('https://go.theconomy.me'+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
        sleep(18)
        return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def ez4short(url):
  try:
    curl=requests.Session()
    step1=curl.get(url,headers={"referer":"https://techmody.io/new-features-in-chrome-90-just-released/"})
    sleep(3)
    fl=bs(step1.text,'html.parser')
    lin=fl.find('form',{'id':'go-link'})['action']
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
        sleep(15)
        return json.loads(final.text)["url"]
  except Exception as e:
    return 'failed to bypass'
def linksly(url):
  curl=requests.Session()
  res= one_method(curl=curl,url='https://go.linksly.co'+urlparse(url).path,headers={"referer":"https://themezon.net/5-best-lookbook-wordpress-themes-for-fashion-and-creative-projects/"})
  sleep(15)
  return res
def adbitfly(url):
  try:
    curl=requests.Session()
    step1=curl.get(url,headers={"referer":"https://faucetgigs.com/processed/"}).text
    tf=bs(step1,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
    toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    ref=tf.find('input',{'name':'ref'})["value"]
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url=url)
    data=f'_method=POST&_csrfToken={csrf}&ref={ref}&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
    step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"referer":"https://faucetgigs.com/processed/"}).text
    sleep(15)
    fl=bs(step2,"html.parser")
    lin=fl.find('form',{'id':'go-link'})['action']
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def shorti_io(url):
  try:
    path=urlparse(url).path
    curl=requests.Session()
    step1=curl.get('https://blog.financeandinsurance.xyz'+path).text
    tf=bs(step1,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
    tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url='https://blog.financeandinsurance.xyz'+path)
    data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    step2=curl.post('https://blog.financeandinsurance.xyz'+path,data=data,headers={'content-type':'application/x-www-form-urlencoded'}).text
    sleep(15)
    fl=bs(step2,'html.parser')
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post('https://blog.financeandinsurance.xyz/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
        sleep(15)
        return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def ex_foary_com(url):
 try:
  curl=requests.Session()
  step1=curl.get(f'https://forex-trnd.com/blo{urlparse(url).path}?r=/blo{urlparse(url).path}',headers={"referer":"https://forex-golds.com/how-to-use-renko-charts/"})
  sleep(10)
  fl=bs(step1.text,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://forex-trnd.com/blo/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def oii(url):
 try:
  curl=requests.Session()
  step1=curl.get(url)
  tf=bs(step1.text,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  ref=tf.find('input',{'name':'ref'})["value"]
  get_key=json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["invisible_reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=step1.url)
  data=f'_method=POST&_csrfToken={csrf}&g-recaptcha-response={answer}&ref=&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
  tf=bs(step2.text,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
  toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  ref=tf.find('input',{'name':'ref'})["value"]
  get_key=json.loads(step2.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=step1.url)
  data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
  step2=curl.post(step1.url,data=data,headers={'content-type':'application/x-www-form-urlencoded;'}).text
  sleep(15)
  fl=bs(step2,"html.parser")
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post('https://'+urlparse(step1.url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
    sleep(15)
    return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def linkjust(url):
 try:
  curl=requests.Session()
  step1=curl.get(url,headers={"referer":"https://forexrw7.com/forex-trading-could-it-be-a-profitable-career-for-me/"})
  fl=bs(step1.text,"html.parser")
  sleep(5)
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post('https://'+urlparse(step1.url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
    sleep(15)
    return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def myra(url):
 try:
  curl=requests.Session()
  step1=curl.get('https://myra.x10.bz'+urlparse(url).path)
  sleep(10)
  fl=bs(step1.text,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://myra.x10.bz/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def mitly(url):
 try:
  curl=requests.Session()
  step1=curl.get(url,headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  tf=bs(step1,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  page=tf.find('input',{'name':'page'})["value"]
  sleep(1)
  data=f'_method=POST&_csrfToken={csrf}&action=continue&page=2&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  sleep(1)
  tf=bs(step2,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  page=tf.find('input',{'name':'page'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&action=continue&page=3&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  tf=bs(step2,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  get_key=json.loads(step2.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=url)
  data=f'_method=POST&_csrfToken={csrf}&action=captcha&f_n=slc&g-recaptcha-response={answer}&h-captcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':url}).text
  sleep(15)
  fl=bs(step2,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://{urlparse(url).hostname}/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def adshorti_xyz(url):
 try:
  curl=requests.Session()
  step1=curl.get(url.replace('link.',''))
  sleep(15)
  fl=bs(step1.text,"html.parser")
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post('https://'+urlparse(step1.url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
    sleep(15)
    return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def birdurl(url):
 try:
  curl=requests.Session()
  step1=curl.get(url.replace('go.',''),headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 (compatible; Googlebot/2.1;+http://google.com/bot.html"})
  sleep(10)
  fl=bs(step1.text,'html.parser')
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(urlparse(url).scheme+'://'+urlparse(url.replace('go.','')).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;','referer':step1.url,"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 (compatible; Googlebot/2.1;+http://google.com/bot.html"})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def owlink(url):
 try:
  curl=requests.Session()
  step1=curl.get(url.replace('go.',''),headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 (compatible; Googlebot/2.1;+http://google.com/bot.html"})
  sleep(10)
  fl=bs(step1.text,'html.parser')
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(urlparse(url).scheme+'://'+urlparse(url.replace('go.','')).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;','referer':step1.url,"user-agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 (compatible; Googlebot/2.1;+http://google.com/bot.html"})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def flyzu(url):
 try:
  curl=requests.Session()
  step1=curl.get('https://go.flyzu.icu'+urlparse(url).path,headers={"referer":"https://zubatecno.com/2022/09/07/7-amazing-ways-to-beat-writers-block/"}).text
  tf=bs(step1,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url='https://go.flyzu.icu'+urlparse(url).path)
  data=f'_method=POST&_csrfToken={csrf}&ref=https%3A%2F%2Fzubatecno.com%2F2022%2F09%2F07%2F7-amazing-ways-to-beat-writers-block%2F&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post('https://go.flyzu.icu'+urlparse(url).path,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':'https://go.flyzu.icu'+urlparse(url).path}).text
  sleep(15)
  fl=bs(step2,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://go.flyzu.icu/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;','referer':'https://go.flyzu.icu'+urlparse(url).path})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def web1s_info(url):
  def final(url_):
    gas=curl.get(url_)
    if 'g-recaptcha mb-2' in gas.text:
      bs4 = BeautifulSoup(gas.text, "html.parser")
      token=bs4.find('input',{'name':'_token'})['value']
      get_key=bs4.find('div',{'class':'g-recaptcha mb-2'})['data-sitekey']
      answer=RecaptchaV2(key=get_key,url=url_)
      data = f"_token={token}&g-recaptcha-response={answer}"
      gas=curl.post(url_,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
      sleep(int(gas.text.split('<div id="second">')[1].split('</div>')[0]))
      inputs = bs(gas.text,'html.parser').find_all("input")
      data = urlencode({input.get("name"): input.get("value") for input in inputs})
      gas=curl.post(gas.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
      inputs = bs(gas.text,'html.parser').find_all("input")
      data = urlencode({input.get("name"): input.get("value") for input in inputs})
      gas=curl.post(gas.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"},allow_redirects=False)
      sleep(15)
      return gas.headers['Location']
    if 'Get Link' in gas.text:
      bs4 = BeautifulSoup(gas.content, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      gas=curl.post(url_,data=data,headers={"content-type":"application/x-www-form-urlencoded"},allow_redirects=False)
      sleep(15)
      return gas.headers['Location']
    else:
      bs4 = BeautifulSoup(gas.content, "html.parser")
      inputs = bs4.find_all("input")
      data = {input.get("name"): input.get("value") for input in inputs}
      gas=curl.post(url_,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
      sleep(int(step1.text.split('<div id="second">')[1].split('</div>')[0]))
      inputs = bs(gas.text,'html.parser').find_all("input")
      data = urlencode({input.get("name"): input.get("value") for input in inputs})
      gas=curl.post(gas.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
      inputs = bs(gas.text,'html.parser').find_all("input")
      data = urlencode({input.get("name"): input.get("value") for input in inputs})
      gas=curl.post(gas.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"},allow_redirects=False)
      sleep(15)
      return gas.headers['Location']
  curl=requests.Session()
  get_url=curl.get(url)
  if 'Tiếp Tục' in get_url.text:
    return final(get_url.url)
  if 'Your link is almost ready' in get_url.text:
    def allmost(get_url):
      step1=curl.get(get_url.url)
      sleep(int(step1.text.split('<div id="second">')[1].split('</div>')[0]))
      inputs = bs(step1.text,'html.parser').find_all("input")
      data = urlencode({input.get("name"): input.get("value") for input in inputs})
      step2=curl.post(step1.url,headers={"content-type":"application/x-www-form-urlencoded"},data=data)
      step1=curl.get(step2.url)
      sleep(int(step1.text.split('<div id="second">')[1].split('</div>')[0]))
      inputs = bs(step1.text,'html.parser').find_all("input")
      data = urlencode({input.get("name"): input.get("value") for input in inputs})
      step2=curl.post(step1.url,headers={"content-type":"application/x-www-form-urlencoded"},data=data)
      return final(step2.url)
    return allmost(get_url)
  get_url=bs(get_url.text,'html.parser').find('a')['href']
  generated_uuid = uuid.uuid4()
  uuid_str = str(generated_uuid)
  step1=curl.get(get_url).text
  code=step1.split('var dirrectSiteCode = "')[1].split('"')[0]
  data=f"screen=424%20x%20942&browser=Chrome&browserVersion=86.0.4240.198&browserMajorVersion=86&mobile=false&os=Windows&osVersion=10&cookies=true&flashVersion=no%20check&code={code}&client_id={uuid_str}&pathname={urlparse(get_url).path}&href={get_url}&hostname={urlparse(get_url).netloc}"
  juml=curl.post('https://web1s.com/step',headers={"content-type":"application/x-www-form-urlencoded","referer":get_url},data=data).text
  def buat(data):
    step=curl.post('https://web1s.com/step',headers={"content-type":"application/x-www-form-urlencoded","referer":get_url},data=data)
    step=curl.post('https://web1s.com/countdown',headers={"content-type":"application/x-www-form-urlencoded","referer":get_url},data=data)
    sleep(json.loads(step.text)['timer'])
    step=curl.post('https://web1s.com/continue',headers={"content-type":"application/x-www-form-urlencoded","referer":get_url},data=data)
    return step.text
  cek=buat(data)
  if json.loads(cek)["success"] == True:
    for i in range(json.loads(juml)["total_steps"]-1):
      step2=curl.get(json.loads(cek)["url"])
      code=step2.text.split('var dirrectSiteCode = "')[1].split('"')[0]
      data=f"screen=424%20x%20942&browser=Chrome&browserVersion=86.0.4240.198&browserMajorVersion=86&mobile=false&os=Windows&osVersion=10&cookies=true&flashVersion=no%20check&code={code}&client_id={uuid_str}&pathname={urlparse(get_url).path}&href={get_url}&hostname={urlparse(get_url).netloc}"
      cek=buat(data)
      if json.loads(cek)["success"] == True:
        ceki=json.loads(cek)["url"]
    if 'app.covemarkets.com' in ceki:
      return final(ceki)
def hrshort(url):
 try:
  curl=requests.Session()
  url='https://'+url.split('url=')[1]
  res=one_method(curl,url)
  sleep(15)
  return res
 except Exception as e:
    return "failed to bypass"
def adshorti_co(url):
 try:
  curl=requests.Session()
  url=url.replace('link.','')
  res=one_method(curl,url)
  sleep(15)
  return res
 except Exception as e:
    return "failed to bypass"
def cashurl_win(url):
 try:
  curl=requests.Session()
  step1=curl.get(url)
  bs4 = BeautifulSoup(step1.content, "html.parser")
  inputs = bs4.find_all("input")
  data = urlencode({input.get("name"): input.get("value") for input in inputs})
  step2=curl.post(step1.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
  bs4 = BeautifulSoup(step2.content, "html.parser")
  inputs = bs4.find_all("input")
  data = {input.get("name"): input.get("value") for input in inputs}
  data["g-recaptcha-response"] = RecaptchaV2(json.loads(step2.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"],step2.url)
  encoded_data = urlencode(data)
  step3=curl.post(step1.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
  bs4 = BeautifulSoup(step3.content, "html.parser")
  inputs = bs4.find_all("input")
  sleep(5)
  data = urlencode({input.get("name"): input.get("value") for input in inputs})
  gas=curl.post('https://'+urlparse(step3.url).netloc+bs4.find('form',{'method':'post'})['action'],data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'},allow_redirects=False)
  if json.loads(gas.text)['status'] == "success":
    sleep(15)
    return json.loads(gas.text)['url']
 except Exception as e:
   return "failed to bypass"
def illink_net(url):
  try:
    curl=requests.Session()
    step1=curl.get('https://illink.net'+urlparse(url).path).text
    tf=bs(step1,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tokf=tf.find('input',{'name':'_Token[fields]'})["value"]
    toku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    ref=tf.find('input',{'name':'ref'})["value"]
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url=url)
    data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tokf}&_Token%5Bunlocked%5D={toku}'
    step2=curl.post('https://illink.net'+urlparse(url).path,data=data,headers={'content-type':'application/x-www-form-urlencoded;'}).text
    sleep(15)
    fl=bs(step2,"html.parser")
    lin=fl.find('form',{'id':'go-link'})['action']
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post(urlparse(url).scheme+'://illink.net'+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def mitly(url):
 try:
  curl=requests.Session()
  step1=curl.get(url,headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  tf=bs(step1,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  page=tf.find('input',{'name':'page'})["value"]
  sleep(1)
  data=f'_method=POST&_csrfToken={csrf}&action=continue&page=2&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  sleep(1)
  tf=bs(step2,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  page=tf.find('input',{'name':'page'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&action=continue&page=3&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"user-agent":"Mozilla/5.0 (Linux; Android 11; Phh-Treble vanilla Build/RQ3A.211001.001;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Safari/537.36"}).text
  tf=bs(step2,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  get_key=json.loads(step2.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=url)
  data=f'_method=POST&_csrfToken={csrf}&action=captcha&f_n=slc&g-recaptcha-response={answer}&h-captcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':url}).text
  sleep(15)
  fl=bs(step2,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://{urlparse(url).hostname}/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def linkvor_pw(url):
 try:
  url='https://g.linkvor.pw'+urlparse(url).path
  curl=requests.Session()
  res= one_method(curl,url)
  sleep(15)
  return res
 except Exception as e:
   return 'failed to bypass'
def link4m_com(url):
 try:
  curl=requests.Session()
  answer=RecaptchaV2('6LcQsTQgAAAAADNQ_pCfukfvS0i9lk4oJTVSs5bZ',url)
  data=f"g-recaptcha-response={answer}&alias={url.split('/go/')[1]}"
  final=curl.post('https://link4m.com/links/check-captcha',data=data,headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'},allow_redirects=False)
  if json.loads(final.text)["success"] == True:
    sleep(15)
    return json.loads(final.text)["url"]
 except Exception as e:
   return 'failed to bypass'
def insfly(url):
 try:
  curl=requests.Session()
  res=one_method(curl,url,headers={"referer":"https://enit.in/H3ScKu"})
  sleep(15)
  return res
 except Exception as e:
   return 'failed to bypass'
def zuba_link(url):
  try:
    curl=requests.Session()
    host=urlparse(url).netloc
    get_ref=urlparse(curl.get(url).url).netloc
    final = curl.get(url,headers={"referer":f"https://{get_ref}/?p=9%20.%20%27?session=4%27"}).text
    sleep(15)
    bs4 = BeautifulSoup(final, "html.parser")
    inputs = bs4.find_all("input")
    data = urlencode({input.get("name"): input.get("value") for input in inputs})
    get_url = curl.post(f'https://{host}/links/go', headers={'x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'}, data=data).json()
    if get_url['status'] == 'success':
        sleep(15)
        return get_url["url"]
  except Exception as e:
    return 'failed to bypass'
def shortzu_icu(url):
  try:
    curl=requests.Session()
    url="https://shortzu.icu/"+urlparse(url).path
    res=one_method(curl,url,headers={"referer":"https://earn.zubatecno.com/?p=9%20.%20%27?session=4%27"})
    sleep(15)
    return res
  except Exception as e:
    return 'failed to bypass'
def clickzu_icu(url):
  try:
    curl=requests.Session()
    url="https://clickzu.icu/"+urlparse(url).path
    res=one_method(curl,url,headers={"referer":"https://earn.battleroyal.online/?p=10%20.%20%27?session=4%27"})
    sleep(15)
    return res
  except Exception as e:
    return 'failed to bypass'
def chainfo(url):
  try:
    curl=requests.Session()
    curl.headers.update({'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'})
    step1=curl.get(url).text
    fl=bs(step1,'html.parser')
    step2=curl.post(fl.find('form',{'id':'landing'})["action"],data=f'go='+fl.find('input',{'name':'go'})["value"],headers={'content-type':'application/x-www-form-urlencoded'}).text
    verif=bs(step2,'html.parser')
    url_post=verif.find('form',{'id':'landing'})["action"]
    id=verif.find('input',{"name":"humanverification"})["value"]
    tok=verif.find('input',{"name":"newwpsafelink"})["value"]
    data=f'humanverification={id}&newwpsafelink={tok}'
    step3=curl.post(url_post,data=data,headers={'content-type':'application/x-www-form-urlencoded'})
    kd=tok + "="*divmod(len(tok),4)[1]
    isi=json.loads(base64.urlsafe_b64decode(kd).decode())["linkr"]
    step4=curl.get(isi).text
    fl=bs(step4,'html.parser')
    step5=curl.post(fl.find('form',{'id':'landing'})["action"],data=f'go='+fl.find('input',{'name':'go'})["value"],headers={'content-type':'application/x-www-form-urlencoded'}).text
    verif=bs(step5,'html.parser')
    url_post=verif.find('form',{'id':'landing'})["action"]
    id=verif.find('input',{"name":"humanverification"})["value"]
    tok=verif.find('input',{"name":"newwpsafelink"})["value"]
    data=f'humanverification={id}&newwpsafelink={tok}'
    step6=curl.post(url_post,data=data,headers={'content-type':'application/x-www-form-urlencoded'})
    kd=tok + "="*divmod(len(tok),4)[1]
    isi=json.loads(base64.urlsafe_b64decode(kd).decode())["linkr"]
    step7=curl.get(isi,allow_redirects=False).headers
    step8=curl.get(step7["location"],headers={"referer":urlparse(isi).scheme+'://'+urlparse(isi).hostname}).text
    sleep(6)
    verif_final=bs(step8,'html.parser')
    lin=verif_final.find('form',{'id':'go-link'})["action"]
    csrf=verif_final.find('input',{'name':'_csrfToken'})["value"]
    afd=urllib.parse.quote_plus(verif_final.find('input',{'name':'ad_form_data'})["value"])
    tkf=urllib.parse.quote_plus(verif_final.find('input',{'name':'_Token[fields]'})["value"])
    tku=urllib.parse.quote_plus(verif_final.find('input',{'name':'_Token[unlocked]'})["value"])
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={afd}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post(urlparse(step7["location"]).scheme+'://'+urlparse(step7["location"]).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
        sleep(15)
        return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def cbshort(url):
 try:
  curl=requests.Session()
  url=url.replace('ser2','ser3')
  res=one_method(curl,url)
  sleep(15)
  return res
 except Exception as e:
    return 'failed to bypass'
def links1s_com(url):
 try:
  curl=requests.Session()
  cek=curl.get(url)
  if 'Please check the captcha box to proceed to the destination page.' in cek.text:
    step1=curl.get(url)
    bs4 = BeautifulSoup(step1.content, "html.parser")
    inputs = bs4.find_all("input")
    data = {input.get("name"): input.get("value") for input in inputs}
    data["g-recaptcha-response"] = RecaptchaV2(json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"],step1.url)
    encoded_data = urlencode(data)
    step3=curl.post(step1.url,data=data,headers={"content-type":"application/x-www-form-urlencoded"})
    bs4 = BeautifulSoup(step3.content, "html.parser")
    inputs = bs4.find_all("input")
    sleep(15)
    data = urlencode({input.get("name"): input.get("value") for input in inputs})
    gas=curl.post('https://'+urlparse(step3.url).netloc+bs4.find('form',{'method':'post'})['action'],data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'},allow_redirects=False)
    if json.loads(gas.text)['status'] == "success":
      res= json.loads(gas.text)['url']
  else:
    res=one_method(curl,url,headers={"referer":"https://www.byboe.com/how-to-clean-brass-jewelry/","user-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"})
  sleep(15)
  return res
 except Exception as e:
    return 'failed to bypass'
def shareus(url):
 try:
  curl=requests.Session()
  res=one_method(curl,url.replace('go.',''),headers={"referer":"https://mdisk.net.in/"})
  sleep(15)
  return res
 except Exception as e:
   return 'failed to bypass'
def megaurl(url):
 try:
  curl=requests.Session()
  url_base=url.replace('go','get')
  step1=curl.get(url_base,headers={"referer":"https://app.trangchu.news/scandisk-rogue-removal-how-to-completely-remove-the-scandisk-virus-from-your-pc.html"}).text
  tf=bs(step1,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=url_base)
  data=f'_method=POST&_csrfToken={csrf}&action=captcha&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url_base,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':url_base}).text
  sleep(15)
  fl=bs(step2,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://{urlparse(url_base).hostname}/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def link1s_net(url):
  curl=requests.Session()
  res=one_method(curl,url,headers={"referer":"https://nguyenvanbao.com/danh-cho-nguoi-moi-vao-nghe-make-money-online/"})
  sleep(20)
  return res
def bitads(url):
 try:
  curl=requests.Session()
  host=urlparse(url).netloc
  final = curl.get(url).text
  sleep(15)
  bs4 = BeautifulSoup(final, "html.parser")
  inputs = bs4.find_all("input")
  data = urlencode({input.get("name"): input.get("value") for input in inputs}).replace('text=None&None=ENTER+THE+CONFIRMATION+CODE&','')
  get_url = curl.post(f'https://{host}/links/go', headers={'x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'}, data=data).json()
  if get_url['status'] == 'success':
      sleep(15)
      return get_url["url"]
 except Exception as e:
   return "failed to bypass"
def adbull(url):
 try:
  curl=requests.Session()
  step1=curl.get(url+'?ref=',headers={"referer":"https://deportealdia.live/2021/03/23/novedades-en-la-nba/"})
  sleep(10)
  fl=bs(step1.text,'html.parser')
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(urlparse(url).scheme+'://'+urlparse(url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;','referer':step1.url})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def url_namaidani(url):
 try:
  curl=requests.Session()
  step1=curl.get(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"}).text
  tf=bs(step1,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  get_key=json.loads(step1.split("<script type='text/javascript'>var app_vars=")[1].split(';</script>')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=url)
  data=f'_method=POST&_csrfToken={csrf}&action=captcha&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':url,"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"}).text
  sleep(30)
  fl=bs(step2,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://{urlparse(url).hostname}/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8','referer':url,"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def megafly(url):
 try:
  curl=requests.Session()
  url=url.replace('go.','get.')
  step1=curl.get(url)
  bs4 = BeautifulSoup(step1.content, "html.parser")
  inputs = bs4.find_all("input")
  data = {input.get("name"): input.get("value") for input in inputs}
  data["g-recaptcha-response"] = RecaptchaV2(json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"],step1.url)
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':url})
  sleep(30)
  bs4 = BeautifulSoup(step2.content, "html.parser")
  inputs = bs4.find_all("input")
  data = {input.get("name"): input.get("value") for input in inputs}
  final=curl.post(f'https://{urlparse(url).hostname}/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8','referer':url})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def kiw_app(url):
 try:
  curl=requests.Session()
  step1=curl.get(url)
  bs4 = BeautifulSoup(step1.content, "html.parser")
  inputs = bs4.find_all("input")
  data = {input.get("name"): input.get("value") for input in inputs}
  data["g-recaptcha-response"] = RecaptchaV2(json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["invisible_reCAPTCHA_site_key"],step1.url)
  step2=curl.post(url,data=data,headers={'content-type':'application/x-www-form-urlencoded;','referer':url})
  sleep(15)
  bs4 = BeautifulSoup(step2.content, "html.parser")
  inti=bs4.find('form')
  inputs = inti.find_all("input")
  data = {input.get("name"): input.get("value") for input in inputs}
  final=curl.post(f'https://{urlparse(url).hostname}/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8','referer':url})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def freeltc_top(url):
  try:
    pat=urlparse(url).path
    curl=requests.Session()
    step1=curl.get('https://short.freeltc.top'+pat).text
    tf=bs(step1,'html.parser')
    csrf=tf.find('input',{'name':'_csrfToken'})["value"]
    tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
    tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
    get_key=json.loads(step1.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
    answer=RecaptchaV2(key=get_key,url='https://short.freeltc.top'+pat)
    data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    step2=curl.post('https://short.freeltc.top'+pat,data=data,headers={'content-type':'application/x-www-form-urlencoded;'}).text
    sleep(15)
    fl=bs(step2,'html.parser')
    csrf=fl.find('input',{'name':'_csrfToken'})["value"]
    tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
    form=fl.find('input',{'name':'ad_form_data'})["value"]
    tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
    data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
    final=curl.post('https://short.freeltc.top/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
    if json.loads(final.text)["status"] == "success":
        sleep(15)
        return json.loads(final.text)["url"]
  except Exception as e:
    return "failed to bypass"
def softindex_website(url):
 try:
  curl=requests.Session()
  if '&url=' in url:
    url=url.split('&url=')
  if 'go.' in url:
    url=url.replace('go.','')
  else:
    url=url
  step1=curl.get(url)
  tf=bs(step1.text,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  ref=tf.find('input',{'name':'ref'})["value"]
  get_key=json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=step1.url)
  data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(step1.url,data=data,headers={'content-type':'application/x-www-form-urlencoded;'}).text
  sleep(15)
  fl=bs(step2,"html.parser")
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post('https://'+urlparse(step1.url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def _1short_in(url):
 try:
  curl=requests.Session()
  step1=curl.get(url)
  gt=bs(step1.text,'html.parser')
  csrf=gt.find('input',{'name':'_token'})['value']
  sitkey=gt.find('button',{'class':'btn btn-success get-link g-recaptcha'})['data-sitekey']
  answer=RecaptchaV2(sitkey,url)
  data=f"_token={csrf}&g-recaptcha-response={answer}"
  ur=gt.find('form',{'id':'getLinkForm'})['action']
  final=curl.post(ur,data=data,headers={'accept':'*/*','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8',"referer":url},allow_redirects=False).text
  if "url" in final:
    sleep(15)
    return json.loads(final)["url"]
 except Exception as e:
    return "failed to bypass"
def urlcash(url):
 try:
  curl=requests.Session()
  if '&url=' in url:
    url=url.split('&url=')
  if 'go1.' in url:
    url=url.replace('go1.','')
  else:
    url=url
  step1=curl.get(url)
  tf=bs(step1.text,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
  ref=tf.find('input',{'name':'ref'})["value"]
  get_key=json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=step1.url)
  data=f'_method=POST&_csrfToken={csrf}&ref=&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(step1.url,data=data,headers={'content-type':'application/x-www-form-urlencoded;'}).text
  sleep(15)
  fl=bs(step2,"html.parser")
  lin=fl.find('form',{'id':'go-link'})['action']
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post('https://'+urlparse(step1.url).hostname+lin,data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded;'})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def coinparty(url):
 try:
  curl=requests.Session()
  step1=curl.get('https://coinsparty.com'+urlparse(url.replace('/m','')).path)
  sleep(10)
  fl=bs(step1.text,'html.parser')
  csrf=fl.find('input',{'name':'_csrfToken'})["value"]
  tkf=fl.find('input',{'name':'_Token[fields]'})["value"]
  form=fl.find('input',{'name':'ad_form_data'})["value"]
  tku=fl.find('input',{'name':'_Token[unlocked]'})["value"]
  data=f'_method=POST&_csrfToken={csrf}&ad_form_data={urllib.parse.quote_plus(form)}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  final=curl.post(f'https://coinsparty.com/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
 except Exception as e:
    return "failed to bypass"
def trafic1s(url):
  curl=requests.Session()
  step1=curl.get(url,headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"})
  tf=bs(step1.text,'html.parser')
  csrf=tf.find('input',{'name':'_csrfToken'})["value"]
  tkf=tf.find('input',{'name':'_Token[fields]'})["value"]
  tku=tf.find('input',{'name':'_Token[unlocked]'})["value"]
 # ref=tf.find('input',{'name':'ref'})["value"]
  get_key=json.loads(step1.text.split('var app_vars = ')[1].split(';')[0])["reCAPTCHA_site_key"]
  answer=RecaptchaV2(key=get_key,url=step1.url)
  data=f'_method=POST&_csrfToken={csrf}&action=captcha&f_n=slc&g-recaptcha-response={answer}&_Token%5Bfields%5D={tkf}&_Token%5Bunlocked%5D={tku}'
  step2=curl.post(step1.url,data=data,headers={'content-type':'application/x-www-form-urlencoded;',"User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"}).text
  sleep(15)
  bs4 = BeautifulSoup(step2, "html.parser")
  inputs = bs4.find_all("input")
  data = urlencode({input.get("name"): input.get("value") for input in inputs}).replace('traffic_campaign_code=None','traffic_campaign_code=')
  final=curl.post('https://traffic1s.com/links/go',data=data,headers={'accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8','referer':url})
  if json.loads(final.text)["status"] == "success":
      sleep(15)
      return json.loads(final.text)["url"]
def gain_lk(url):
 try:
  curl=requests.Session()
  ua={
    "User-Agent":"Mozilla/5.0 (Linux; Android 10; RMX3171 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "x-requested-with":"mark.via.gp"
   }
  step1=curl.get(url).text.split('"')[1].split('"')[0]
  #print(step1)
  step2=curl.get(step1,headers={"referer":url}).text.split('url=')[1].split('"')[0]
  step3=curl.get(step2,headers={"referer":step2})
  ve=curl.get(f'https://{urlparse(step3.url).netloc}/blog/blog/validate',headers={"referer":step3.url})
  csrf=bs(step3.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
  sleep(15)
  url_=bs(step3.text,'html.parser').find('form',{'onkeydown':"return event.key !== 'Enter';"})['action']
  data=f"answer=2&csrf_token_name={csrf}"
  verif=curl.post(url_,data=data,headers={"referer":step3.url,"content-type":"application/x-www-form-urlencoded"},allow_redirects=False).headers['location']
  ref=step3.url
  for ulang in range(1):
    verif1=curl.get(verif,headers={"referer":ref}).text
    if ';google.navigateTo(parent,window,redirectUrl);})' in verif1:
      verif1=verif1.split('content="0;url=')[1].split('"')[0]
    else:
      verif1=verif1.split('"')[1].split('"')[0]
    step1=curl.get(verif1,headers={"referer":verif})
    if 'Halaman sebelumnya berusaha untuk mengarahkan Anda ke' in step1.text:
      step1=curl.get(bs(step1.text,'html.parser').find('a')['href'],headers={"referer":verif})
   # print(step1.text)
    csrf=bs(step1.text,'html.parser').find('input',{'name':'csrf_token_name'})['value']
    sleep(15)
    url_=bs(step1.text,'html.parser').find('form',{'onkeydown':"return event.key !== 'Enter';"})['action']
    data=f"answer=2&csrf_token_name={csrf}"
    verif=curl.post(url_,data=data,headers={"referer":step3.url,"content-type":"application/x-www-form-urlencoded"},allow_redirects=False).headers['location']
    #print(verif)
    ref=step1.url
  host=urlparse(verif).netloc
  final = curl.get(verif,headers={"referer":ref}).text
  sleep(5)
  bs4 = BeautifulSoup(final, "html.parser")
  inputs = bs4.find_all("input")
  data = urlencode({input.get("name"): input.get("value") for input in inputs})
  get_url = curl.post(f'https://{host}/links/go', headers={'x-requested-with':'XMLHttpRequest','content-type':'application/x-www-form-urlencoded; charset=UTF-8'}, data=data).json()
  if get_url['status'] == 'success':
    u= curl.get(get_url["url"],headers={"referer":verif},allow_redirects=False).headers['location']
    sleep(15)
    return u
 except:
   return "failed to bypass"
   pass
#print(usalink('https://link.usalink.io/GyhmT3c0'))