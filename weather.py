# https://www.google.co.in/search?q=weather+in+nanded
# user agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 
# span id = wob_tm
from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    query = "nanded"
    url =f'https://www.google.co.in/search?q=weather+in+nanded'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
    temp = r.html.find('span#wob_tm', first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text 
    desc = r.html.find('span#wob_dc', first= True).text 
    return temp+" " + unit+" "+ desc

