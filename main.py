import socket # импортируем библиотеки
import requests

def getIP ( domainName ): # данная функция использует библиотеку сокет для получения IP

    try:
        ip = socket.gethostbyname(domainName)
        return ip

    except:
        return "[Error]: ip not found!"

def getServerName ( siteName ): # данная функция, берет из HTTP заголовков имя сервера по средством requests

    try:
        content = requests.get( siteName )
        server = content.headers['Server']
        return server

    except:
        return "[Error]: Server not found"

import modules.siteName

            +-----------------------------------------+

"""
# выводим список некоторых команд
print(r"""

            +-----------------------------------------+
            | [exit] -- exit ;)                                        |
            | [back] -- back on main menu               |
            | [modules] -- show modules                 |
            +-----------------------------------------+

""")



def setModule (): # функция направлена на выбор и использование модулей

    moduleNum = input("[Enter module num]: ")

    if moduleNum == "1":

        try:
            domain = input ( "[Enter domain]: " ) # запрашиваем у пользователя имя сайта
            ipSite = getIPaddr(domain) # отправляем имя нашему модулю

            print("-" * 60)
            print("[IP] == [{0}]".format(ipSite))
            print("-" * 60)

        except:
            print( "[Error]: Domain or ip not found!" )


    elif moduleNum == "2":

        try:
            site = input ( "[Enter domain]: " )
            url = "http://" + site
            server = getServer(url)

            print("-" * 60)
            print("[Server] == [{0}]".format(server))
            print("-" * 60)

        except:
            print( "[Error]: Domain or server not found!" )


    comand()

def comand (): # функция направлена на исполнение выбранной пользователем команды

    comand = input("[$] --> ")

    if comand == "exit": exit( "Close program... " )
    elif comand == "back": print(comand())
    elif comand == "modules":

        print ( modulesList )
        print ( setModule () )

    else:

        print ( "[Error]: Comand not found!" )
        print ( comand () )


print(comand())s
print ("by MishaproGaming")
