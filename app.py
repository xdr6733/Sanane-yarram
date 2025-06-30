#!/usr/bin/env python
# -*- coding: utf-8 -*-

TOKEN = "7863131130:AAEZDX4nElVLvfzPyXdfQFG_EKivj1o4c4c"

çıkarşuşarkıyıbatuflex = "\033[35m"
yatak = "\033[36m"
hackerhıhı = "\033[100m"
dev = "\033[101m"
batu = "\033[94m"
hehe = "\033[0m"

import os
import time
import io
import threading
import requests
import json
from datetime import datetime, date
from bs4 import BeautifulSoup

from flask import Flask
import telebot
from telebot import types

os.system('clear')
print(f"{dev}Dev: @batukurucu{hehe}")

hackerbatu = """⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀
... [ASCII Art Content Omitted for Brevity] ...
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

class Batuflex:
    def __init__(self):
        # Initialize bot with fixed token
        self.batuHeker = telebot.TeleBot(TOKEN)
        print(f"{batu}{hackerbatu}{hehe}")
        print(f"{hackerhıhı} 🚀 BOT BAŞLADI 🚀 {hehe}")
        self.hekirBatuHekir = {}
        self.cistakHacker = {
            "Ad Soyad": {"url": "http://api.prymx.fun/apiler/adsoyad.php", "params": ["ad", "soyad", "il"], "method": "GET"},
            "TC Bilgi": {"url": "http://api.prymx.fun/apiler/tc.php", "params": ["tc"], "method": "GET"},
            "Aile": {"url": "http://api.prymx.fun/apiler/aile.php", "params": ["tc"], "method": "GET"},
            "Sulale": {"url": "http://api.prymx.fun/apiler/sulale.php", "params": ["tc"], "method": "GET"},
            "GSM TC": {"url": "http://api.prymx.fun/apiler/gsmtc.php", "params": ["gsm"], "method": "GET"},
            "TC GSM": {"url": "http://api.prymx.fun/apiler/tcgsm.php", "params": ["tc"], "method": "GET"},
            "SGK": {"url": "http://api.prymx.fun/apiler/sgk.php", "params": ["tc"], "method": "GET"},
            "Tapu": {"url": "http://api.prymx.fun/apiler/tapu.php", "params": ["tc"], "method": "GET"},
            "IP": {"url": "https://ipinfo.io", "params": ["ip"], "method": "GET"},
            "IBAN": {"url": "https://hesapno.com/mod_coz_iban.php", "params": ["iban"], "method": "POST"},
            "Burç Sorgu": {"url": "http://api.prymx.fun/apiler/tc.php", "params": ["tc"], "method": "GET"},
            "Hayat Bilgisi": {"url": "http://api.prymx.fun/apiler/tc.php", "params": ["tc"], "method": "GET"},
            "Site Ekran Görüntüsü": {"url": "https://api.pikwy.com/", "params": ["url"], "method": "GET", "screenshot": True},
            "sms bomber": {"url": "https://prymx.store/apiler/sms.php", "params": ["gsm"], "method": "GET", "ignore_response": True}
        }
        self.RESPONSE_LENGTH_THRESHOLD = 1000
        self.kardeşimAşkımYatSoySok()

    def is_subscribed(self, user_id):
        # Check subscription for channels: @batutool and channel with id -1002558059383
        channels = ["@batutool", "@ynbatuk"]
        for channel in channels:
            try:
                member = self.batuHeker.get_chat_member(channel, user_id)
                if member.status in ["left", "kicked"]:
                    return False
            except Exception:
                return False
        return True

    def send_subscription_keyboard(self, chat_id):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_batutool = types.InlineKeyboardButton(text="📢  @batutool", url="https://t.me/batutool")
        btn_channel = types.InlineKeyboardButton(text="🌐  Kanal", url="https://t.me/ynbatuk")
        btn_check = types.InlineKeyboardButton(text="✅  Kontrol Et", callback_data="check_subscription")
        markup.row(btn_batutool, btn_channel)
        markup.add(btn_check)
        self.batuHeker.send_message(chat_id, "💡 Lütfen aşağıdaki kanallara katılın ve üyelik durumunu kontrol etmek için **Kontrol Et** butonuna basın!", reply_markup=markup)

    def kardeşimAşkımYatSoy(self):
        saat = datetime.now().hour
        if saat < 12:
            return "Günaydın"
        elif saat < 18:
            return "Tünaydın"
        else:
            return "İyi akşamlar"

    def soylikSelamSok(self):
        markup = types.InlineKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(text=f"🔹 {anahtar}", callback_data=anahtar) for anahtar in self.cistakHacker.keys()]
        markup.add(*buttons)
        return markup

    def hekirHıhıSok(self, mesaj):
        cid = mesaj.chat.id
        self.hekirBatuHekir[cid] = {}
        gselam = self.kardeşimAşkımYatSoy()
        self.batuHeker.send_message(cid, f"👋 {gselam}! 🎉 Sorgu Bot'una hoş geldiniz. Lütfen aşağıdaki menüden bir seçeneğe tıklayın:", reply_markup=self.soylikSelamSok())

    def kardeşimAşkımYatSoySok(self, mesaj=None):
        @self.batuHeker.message_handler(commands=['start'])
        def basla(m):
            user_id = m.from_user.id
            cid = m.chat.id
            if not self.is_subscribed(user_id):
                self.send_subscription_keyboard(cid)
                return
            self.hekirHıhıSok(m)

        @self.batuHeker.callback_query_handler(func=lambda c: True)
        def callback(c):
            user_id = c.from_user.id
            cid = c.message.chat.id
            if c.data == "check_subscription":
                if self.is_subscribed(user_id):
                    try:
                        self.batuHeker.delete_message(cid, c.message.message_id)
                    except Exception:
                        pass
                    self.batuHeker.send_message(cid, "🎉 Tebrikler, gerekli kanallara abone olmuşsunuz. Ana menü aşağıdadır:", reply_markup=self.soylikSelamSok())
                    self.batuHeker.answer_callback_query(c.id, "✅ Üyelik kontrolü başarılı!")
                else:
                    self.batuHeker.answer_callback_query(c.id, "❌ Üyelik kontrolü başarısız, lütfen tüm kanallara abone olun.")
                    self.send_subscription_keyboard(cid)
                return

            if not self.is_subscribed(user_id):
                self.batuHeker.answer_callback_query(c.id, "❌ Lütfen önce tüm kanallara abone olun.")
                self.send_subscription_keyboard(cid)
                return

            secim = c.data
            self.hekirBatuHekir[cid] = {"selected_api": secim, "step": 0, "params": {}}
            if secim == "sms bomber":
                self.batuHeker.send_message(cid, "🧾 Lütfen 5 ile başlayan numarayı giriniz:")
            elif secim in ["IBAN", "IP", "Burç Sorgu", "Hayat Bilgisi", "Site Ekran Görüntüsü"]:
                pr = ("💳 Lütfen IBAN bilgisini giriniz:" if secim == "IBAN" else
                      ("🌐 Lütfen IP adresini giriniz:" if secim == "IP" else
                       ("🧾 Lütfen TC numaranızı giriniz:" if secim in ["Burç Sorgu", "Hayat Bilgisi"] else
                        "🔗 Lütfen site URL'sini giriniz:")))
                self.batuHeker.send_message(cid, pr)
            else:
                ilk = self.cistakHacker[secim]["params"][0]
                self.soySok(cid, ilk)

        @self.batuHeker.message_handler(func=lambda m: True)
        def mesaj_isle(m):
            user_id = m.from_user.id
            cid = m.chat.id
            if not self.is_subscribed(user_id):
                self.send_subscription_keyboard(cid)
                return
            txt = m.text.strip()
            if cid not in self.hekirBatuHekir or "selected_api" not in self.hekirBatuHekir[cid]:
                self.batuHeker.send_message(cid, "ℹ️ Lütfen /start yazın.")
                return
            secim = self.hekirBatuHekir[cid]["selected_api"]
            if secim == "sms bomber":
                if not txt.startswith("5"):
                    self.batuHeker.send_message(cid, "⚠️ Numara geçersiz, lütfen 5 ile başlayan numara giriniz.")
                    return
                self.hekirBatuHekir[cid]["params"]["gsm"] = txt
                self.sisSok(cid)
            elif secim in ["IBAN", "IP", "Burç Sorgu", "Hayat Bilgisi", "Site Ekran Görüntüsü"]:
                key = "iban" if secim == "IBAN" else ("ip" if secim == "IP" else ("tc" if secim in ["Burç Sorgu", "Hayat Bilgisi"] else "url"))
                self.hekirBatuHekir[cid]["params"][key] = txt
                self.sisSok(cid)
            else:
                state = self.hekirBatuHekir[cid]
                adım = state.get("step", 0)
                reqs = self.cistakHacker[secim]["params"]
                cur = reqs[adım]
                if cur == "il" and txt == "İl Bilmiyorum":
                    state["params"][cur] = ""
                else:
                    state["params"][cur] = txt
                state["step"] += 1
                if state["step"] >= len(reqs):
                    self.sisSok(cid)
                else:
                    nextp = reqs[state["step"]]
                    self.soySok(cid, nextp)

    def soySok(self, cid, param):
        if param == "il":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            markup.add("İl Bilmiyorum")
            self.batuHeker.send_message(cid, f"🏙️ Lütfen 'il' bilgisini gir veya 'İl Bilmiyorum' deyin:", reply_markup=markup)
        else:
            self.batuHeker.send_message(cid, f"📝 Lütfen '{param}' bilgisini gir:")

    def sisSok(self, cid):
        secim = self.hekirBatuHekir[cid]["selected_api"]
        parms = self.hekirBatuHekir[cid]["params"]
        info = self.cistakHacker.get(secim)
        method = info.get("method", "GET")
        url = info["url"]
        try:
            if secim == "IP":
                full_url = f"https://ipinfo.io/{parms.get('ip','')}/json"
                resp = requests.get(full_url)
            elif secim == "IBAN":
                iban_val = parms.get("iban", "")
                cookies = {'PHPSESSID': 'jthkuejr3j9f6jetegjnfp1ou2'}
                headers = {'User-Agent': 'Mozilla/5.0'}
                resp = requests.post(url, cookies=cookies, headers=headers, data={'iban': iban_val, 'x': '84', 'y': '29'})
                soup = BeautifulSoup(resp.text, 'html.parser')
                def gn(tag, d=""):
                    return tag.next_sibling.strip() if tag and tag.next_sibling else d
                res = {
                    'Banka Adı': gn(soup.find('b', string='Ad:')),
                    'Banka Kodu': gn(soup.find('b', string='Kod:'))
                }
                mesaj = "\n".join([f"{k}: {v}" for k, v in res.items()])
                self.batuHeker.send_message(cid, f"📄 {mesaj}")
                self.hekirBatuHekir.pop(cid, None)
                return
            elif secim == "Site Ekran Görüntüsü":
                url_input = parms.get("url", "")
                sp = {'tkn': '125', 'd': '3000', 'u': url_input, 'fs': '0', 'w': '1280', 'h': '1200', 's': '100', 'z': '100', 'f': 'jpg', 'rt': 'jweb'}
                hdr = {'User-Agent': 'Mozilla/5.0'}
                r = requests.get("https://api.pikwy.com/", params=sp, headers=hdr)
                ds = r.json()
                iurl = ds.get("iurl")
                if iurl:
                    ir = requests.get(iurl)
                    photo = io.BytesIO(ir.content)
                    photo.name = "ekran_goruntusu.jpg"
                    self.batuHeker.send_photo(cid, photo, caption="📸 Site ekran görüntüsü hazır!")
                else:
                    self.batuHeker.send_message(cid, "⚠️ Görüntü URL'si alınamadı!")
                self.hekirBatuHekir.pop(cid, None)
                return
            elif secim == "sms bomber":
                gsm_num = parms.get("gsm", "")
                full_url = f"{url}?gsm={gsm_num}"
                requests.get(full_url)
                self.batuHeker.send_message(cid, "🚀 SMS bomber işlemi başlatıldı!")
                self.hekirBatuHekir.pop(cid, None)
                return
            else:
                if method == "GET":
                    resp = requests.get(url, params=parms)
                else:
                    resp = requests.request(method, url, params=parms)
            resp.raise_for_status()
            if secim in ["Burç Sorgu", "Hayat Bilgisi"]:
                ddata = resp.json()
                if "data" in ddata and ddata["data"]:
                    rec = ddata["data"][0]
                    dob_str = rec.get("DOGUMTARIHI", "")
                    zodiac = "Bilinmiyor"
                    age = "Bilinmiyor"
                    if dob_str:
                        try:
                            parts = dob_str.split('.')
                            if len(parts) >= 3:
                                day = int(parts[0])
                                month = int(parts[1])
                                year = int(parts[2])
                                zodiac = self.compute_zodiac(day, month)
                                bdate = date(year, month, day)
                                today = date.today()
                                age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
                        except Exception:
                            zodiac = "Bilinmiyor"
                    if secim == "Burç Sorgu":
                        mesaj = f"💫 Doğum Tarihiniz: {dob_str}\n👉 Burcunuz: {zodiac}"
                    else:
                        mn = {1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}
                        try:
                            if dob_str and len(parts) >= 3:
                                fdob = f"{day} {mn.get(month,month)} {year}"
                            else:
                                fdob = dob_str
                        except Exception:
                            fdob = dob_str
                        mesaj = (f"📋 {rec.get('ADI','Bilinmiyor')} {rec.get('SOYADI','Bilinmiyor')}, {rec.get('TC','')} TC kimlik numaralıdır. "
                                 f"Doğum tarihi {fdob} olarak kaydedilmiştir ve yaklaşık {age} yaşındadır. "
                                 f"Burcu {zodiac} olup, babası {rec.get('BABAADI','Bilinmiyor')} (TC: {rec.get('BABATC','')}) ve annesi "
                                 f"{rec.get('ANNEADI','Bilinmiyor')} (TC: {rec.get('ANNETC','')}) kayıtlıdır. "
                                 f"İkamet {rec.get('NUFUSIL','Bilinmiyor')}/{rec.get('NUFUSILCE','Bilinmiyor')} ve uyruk {rec.get('UYRUK','Bilinmiyor')}.")
                    self.batuHeker.send_message(cid, mesaj)
                else:
                    self.batuHeker.send_message(cid, "⚠️ Veri alınamadı. Lütfen geçerli bir TC girin.")
            else:
                ddata = resp.json()
                pretty = json.dumps(ddata, indent=4, ensure_ascii=False)
                if len(pretty) > self.RESPONSE_LENGTH_THRESHOLD:
                    fname = f"{secim.replace(' ', '_')}_.txt"
                    with open(fname, "w", encoding="utf-8") as f:
                        f.write(pretty)
                    with open(fname, "rb") as f:
                        self.batuHeker.send_document(cid, f, caption="📄 Yanıt dosyası:")
                else:
                    self.batuHeker.send_message(cid, f"📋 Sorgu Sonucu:\n\n<pre>{pretty}</pre>", parse_mode="HTML")
        except Exception as ex:
            self.batuHeker.send_message(cid, f"❌ API isteğinde hata meydana geldi.")
        self.hekirBatuHekir.pop(cid, None)
        self.batuHeker.send_message(cid, "✅ İşlem tamamlandı. Yeni sorgu için /start yazın.")

    def compute_zodiac(self, day, month):
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Koç"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Boğa"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "İkizler"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Yengeç"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Aslan"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Başak"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Terazi"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Akrep"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Yay"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Oğlak"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Kova"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "Balık"
        else:
            return "Bilinmiyor"

    def waitForSok(self):
        while True:
            try:
                requests.get("https://www.google.com", timeout=5)
                break
            except requests.RequestException:
                time.sleep(5)

    def run(self):
        while True:
            try:
                self.batuHeker.polling(none_stop=True)
            except Exception as e:
                print("Internet kopdu, yeniden bağlanıyor...")
                self.waitForSok()
                os.system("clear")
                print(f"{batu}{hackerbatu}{hehe}")
                print(f"{hackerhıhı} 🚀 BOT BAŞLADI 🚀 {hehe}")
                time.sleep(2)

# Flask API integration
app = Flask(__name__)
bot_instance = Batuflex()

def run_bot():
    bot_instance.run()

# Start the bot in a background thread (bot remains active independently of API requests)
threading.Thread(target=run_bot, daemon=True).start()

@app.route("/")
def index():
    return "bot aktif"

if __name__ == "__main__":
    # For local testing you can use debug mode. When deployed to Render.com Gunicorn will start this app.
    app.run(host="0.0.0.0", port=5000)
