from bs4 import BeautifulSoup
import requests
import time
import datetime
import pywhatkit
import schedule

#Seleccionar algo que necesitemos de la web
url = requests.get("https://articulo.mercadolibre.com.ar/MLA-1352202198-mouse-mad-catz-gaming-rat2-_JM#position=17&search_layout=stack&type=item&tracking_id=1b34bf61-6669-4a63-86b5-9999341261c2")

#Crear un archivo html
soup = BeautifulSoup(url.content,"html.parser")

#Tipo de etiqueta 
result = soup.find("span",{"class": "andes-money-amount__fraction"})
print(result)

#Separar el texto
price_result_text = float(result.text)
print(price_result_text)

#Precio deseado
price_desired = 15.000

if price_result_text < price_desired:
    current_hour = datetime.datetime.now().hour
    current_minute_plus_one = datetime.datetime.now().minute + 1

    if current_minute_plus_one > 59:
        current_minute_plus_one = 0
        current_hour = current_hour + 1
        if current_hour > 23:
            current_hour = 0
    
    #Contacto
    phone_to_send = input("Ingrese un numero de telefono de WhatsApp (con +)")
    #send_to_contact = pywhatkit.sendwhatmsg(phone_to_send, "Oferta activa!", current_hour, current_minute_plus_one,15,True,2)

    #Grupo
    id_group = input("Ingrese el id del grupo de WhatsApp")
    send_to_group = pywhatkit.sendwhatmsg_to_group(id_group, "Oferta activa en el grupo!", current_hour, current_minute_plus_one,15,True,2)
else:
    print("El articulo no esta en descuento!")

#Programar una hora para comprobacion de la oferta
schedule.every().day.at("09:00").do(send_to_group)

while True:
    schedule.run_pending()
    time.sleep(1)