from bs4 import BeautifulSoup
import requests
import time
# from telegramBot import telegram_bot
# from telegramBot import token
from telegramBot import send_mes_to_bot

files=open("web.txt")
user = files.readline()
files.close()

#"Закаленное в боях"
#"После полевых испытаний"
#"Поношенное"
#"Немного поношенное"
#"Прямо с завода"
k=1
while True:
    flag = False
    if (flag == False):     #парсим сайт (неонуар)
        url_neo = "https://market.csgo.com/item/2735515991-480085569-M4A4%20%7C%20%D0%9D%D0%B5%D0%BE%D0%BD%D1%83%D0%B0%D1%80%20(%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%BB%D0%B5%D0%B2%D1%8B%D1%85%20%D0%B8%D1%81%D0%BF%D1%8B%D1%82%D0%B0%D0%BD%D0%B8%D0%B9)/"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }
        req_neo = requests.get(url_neo, headers = headers)
        src_neo = req_neo.text
        # with open("index.html", "w") as file:
        #     file.write(src)
        #
        # with open("index.html") as file:
        #     src = file.read()
        neo = BeautifulSoup(src_neo, 'html.parser')    #данные неонуар


        neo_noir_quality = neo.findAll(class_="sameitem-quality")  #характеристики неонура
        neo_noir_float = neo.findAll(class_="sameitem-floatnum")
        neo_noir_price = neo.findAll(class_="ibutton ibutton-buy")
        neo_noir_href = neo.findAll(class_="sameitem-col sameitem-title")
    ####
        for i in range (len(neo_noir_price)):   #вывод характеристик + ссылки на неонуар
            href = neo_noir_href[i + 1].get("href").rstrip().lstrip()
            quality = neo_noir_quality[i].text.rstrip().lstrip()
            Float = float(neo_noir_float[i].text.rstrip().lstrip()[0:-1])
            price = float(neo_noir_price[i].text.rstrip().lstrip().replace(" ", ""))

            if (quality == "Прямо с завода" and price <= 3000 and Float <=2):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")
    ####
        #закончил парсить сайт неонуар


    if (flag == False):     #парсим сайт (император)
        url_imp = "https://market.csgo.com/item/3221976797-188530139-M4A4%20%7C%20%D0%98%D0%BC%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%20(%D0%97%D0%B0%D0%BA%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%B2%20%D0%B1%D0%BE%D1%8F%D1%85)/"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }
        req_imp = requests.get(url_imp, headers = headers)
        src_imp = req_imp.text

        imp = BeautifulSoup(src_imp, 'html.parser')    #данные


        imp_quality = imp.findAll(class_="sameitem-quality")  #характеристики
        imp_float = imp.findAll(class_="sameitem-floatnum")
        imp_price = imp.findAll(class_="ibutton ibutton-buy")
        imp_href = imp.findAll(class_="sameitem-col sameitem-title")

        for i in range (len(imp_price)):   #вывод характеристик + ссылки
            href = imp_href[i + 1].get("href").rstrip().lstrip()
            quality = imp_quality[i].text.rstrip().lstrip()
            Float = float(imp_float[i].text.rstrip().lstrip()[0:-1])
            price = float(imp_price[i].text.rstrip().lstrip().replace(" ", ""))

            if (quality == "Прямо с завода"  and price <= 7000  and Float <= 1.5):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")



    if (flag == False):     #парсим сайт (M4A4 азимов)
        url_m4azimov = "https://market.csgo.com/item/310779511-480085569-M4A4+%7C+%D0%90%D0%B7%D0%B8%D0%BC%D0%BE%D0%B2+%28%D0%97%D0%B0%D0%BA%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5+%D0%B2+%D0%B1%D0%BE%D1%8F%D1%85%29/"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }
        req_m4azimov = requests.get(url_m4azimov, headers = headers)
        src_m4azimov = req_m4azimov.text

        m4azimov = BeautifulSoup(src_m4azimov, 'html.parser')    #данные


        m4azimov_quality = m4azimov.findAll(class_="sameitem-quality")  #характеристики
        m4azimov_float = m4azimov.findAll(class_="sameitem-floatnum")
        m4azimov_price = m4azimov.findAll(class_="ibutton ibutton-buy")
        m4azimov_href = m4azimov.findAll(class_="sameitem-col sameitem-title")

        for i in range (len(m4azimov_price)):   #вывод характеристик + ссылки
            href = m4azimov_href[i + 1].get("href").rstrip().lstrip()
            quality = m4azimov_quality[i].text.rstrip().lstrip()
            Float = float(m4azimov_float[i].text.rstrip().lstrip()[0:-1])
            price = float(m4azimov_price[i].text.rstrip().lstrip().replace(" ", ""))

            if ((quality == "Закаленное в боях"  and price <= 2800 and Float <= 45.5) or (quality == "После полевых испытаний"  and price <= 9500 and Float <= 24.5)):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")




    if (flag == False):     #парсим сайт (AWP азимов)
        url_AWPazimov = "https://market.csgo.com/item/360479494-188530139-AWP%20%7C%20%D0%90%D0%B7%D0%B8%D0%BC%D0%BE%D0%B2%20(%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%BB%D0%B5%D0%B2%D1%8B%D1%85%20%D0%B8%D1%81%D0%BF%D1%8B%D1%82%D0%B0%D0%BD%D0%B8%D0%B9)/"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }
        req_AWPazimov = requests.get(url_AWPazimov, headers = headers)
        src_AWPazimov = req_AWPazimov.text

        AWPazimov = BeautifulSoup(src_AWPazimov, 'html.parser')    #данные


        AWPazimov_quality = AWPazimov.findAll(class_="sameitem-quality")  #характеристики
        AWPazimov_float = AWPazimov.findAll(class_="sameitem-floatnum")
        AWPazimov_price = AWPazimov.findAll(class_="ibutton ibutton-buy")
        AWPazimov_href = AWPazimov.findAll(class_="sameitem-col sameitem-title")

        for i in range (len(AWPazimov_price)):   #вывод характеристик + ссылки
            href = AWPazimov_href[i + 1].get("href").rstrip().lstrip()
            quality = AWPazimov_quality[i].text.rstrip().lstrip()
            Float = float(AWPazimov_float[i].text.rstrip().lstrip()[0:-1])
            price = float(AWPazimov_price[i].text.rstrip().lstrip().replace(" ", ""))

            if ( quality == "Закаленное в боях" and price <= 5000 and Float >= 88):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")



    if (flag == False):     #парсим сайт (AWP redLine)
        url_AWPred = "https://market.csgo.com/item/4620290820-188530139-AWP+%7C+%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F+%D0%BB%D0%B8%D0%BD%D0%B8%D1%8F+%28%D0%9D%D0%B5%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BF%D0%BE%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%29/"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }
        req_AWPred = requests.get(url_AWPred, headers = headers)
        src_AWPred = req_AWPred.text

        AWPred = BeautifulSoup(src_AWPred, 'html.parser')    #данные


        AWPred_quality = AWPred.findAll(class_="sameitem-quality")  #характеристики
        AWPred_float = AWPred.findAll(class_="sameitem-floatnum")
        AWPred_price = AWPred.findAll(class_="ibutton ibutton-buy")
        AWPred_href = AWPred.findAll(class_="sameitem-col sameitem-title")

        for i in range (len(AWPred_price)):   #вывод характеристик + ссылки
            href = AWPred_href[i + 1].get("href").rstrip().lstrip()
            quality = AWPred_quality[i].text.rstrip().lstrip()
            Float = float(AWPred_float[i].text.rstrip().lstrip()[0:-1])
            price = float(AWPred_price[i].text.rstrip().lstrip().replace(" ", ""))

            if (quality == "Немного поношенное" and price <= 4000 and Float <= 11):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")



    if (flag == False):     #парсим сайт (AK-47 redLine)
        url_AK47red = "https://market.csgo.com/item/4516651892-188530139-AK-47%20%7C%20%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B8%D1%8F%20(%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%BE%D0%BB%D0%B5%D0%B2%D1%8B%D1%85%20%D0%B8%D1%81%D0%BF%D1%8B%D1%82%D0%B0%D0%BD%D0%B8%D0%B9)/"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }

        req_AK47red = requests.get(url_AK47red, headers = headers)
        src_AK47red = req_AK47red.text

        AK47red = BeautifulSoup(src_AK47red, 'html.parser')    #данные


        AK47red_quality = AK47red.findAll(class_="sameitem-quality")  #характеристики
        AK47red_float = AK47red.findAll(class_="sameitem-floatnum")
        AK47red_price = AK47red.findAll(class_="ibutton ibutton-buy")
        AK47red_href = AK47red.findAll(class_="sameitem-col sameitem-title")

        for i in range (len(AK47red_price)):   #вывод характеристик + ссылки
            href = AK47red_href[i + 1].get("href").rstrip().lstrip()
            quality = AK47red_quality[i].text.rstrip().lstrip()
            Float = float(AK47red_float[i].text.rstrip().lstrip()[0:-1])
            price = float(AK47red_price[i].text.rstrip().lstrip().replace(" ", ""))

            if (quality == "После полевых испытаний" and price <= 1100 and Float <= 16):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")



    if (flag == False):     #парсим сайт (Glock18 Vogue)
        url_GlockVogue = "https://market.csgo.com/item/3956670323-902658099-StatTrak%E2%84%A2+Glock-18+%7C+Vogue+%28%D0%9F%D1%80%D1%8F%D0%BC%D0%BE+%D1%81+%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4%D0%B0%29"
        headers = {
            "accept": "*/*",
            "user-agent": user
        }
        req_GlockVogue = requests.get(url_GlockVogue, headers = headers)
        src_GlockVogue = req_GlockVogue.text

        GlockVogue = BeautifulSoup(src_GlockVogue, 'html.parser')    #данные


        GlockVogue_quality = GlockVogue.findAll(class_="sameitem-quality")  #характеристики
        GlockVogue_float = GlockVogue.findAll(class_="sameitem-floatnum")
        GlockVogue_price = GlockVogue.findAll(class_="ibutton ibutton-buy")
        GlockVogue_href = GlockVogue.findAll(class_="sameitem-col sameitem-title")

        for i in range (len(GlockVogue_price)):   #вывод характеристик + ссылки
            href = GlockVogue_href[i + 1].get("href").rstrip().lstrip()
            quality = GlockVogue_quality[i].text.rstrip().lstrip()
            Float = float(GlockVogue_float[i].text.rstrip().lstrip()[0:-1])
            price = float(GlockVogue_price[i].text.rstrip().lstrip().replace(" ", ""))

            if (quality == "Прямо с завода" and price >= 1700 and price <= 2000 and Float <= 1.5):
                send_mes_to_bot("https://market.csgo.com" + href)
                print(quality, Float, price, "https://market.csgo.com" + href, sep = "  ")
    k += 1
    print("следующая итерация:", k)



    time.sleep(100)
