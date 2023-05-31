# Web Scrapping con Python - Envio de notificacion de oferta desde ecommerce hacia WhatsApp

## Developer 
Ezequiel M. Tartaglia

## Link de youtube
- Link: https://youtu.be/q3IMcrZidBg

## Modulos requeridos
```
pip install BeautifulSoup 
pip install requests
pip install time
pip install datetime
pip install pywhatkit
pip install schedule
```
## Funcionamiento

1. Seleccionar un producto (el URL).
2. Parsear su estructura a HTML y elegir el fragmento deseado. (en este caso el precio)
3. Crear una condicion para disparar la notificacion. (cuando enviara el mensaje)
4. Elegir si enviara a contacto o grupo.
5. Organizar un schedule job para ejecutarlo diariamente. (opcional)

- Nota: Cada vez que se envie el mensaje la informacion de envio se guardara en el archivo `PyWhatKit_DB.txt` con el siguiente formato

```
    Date: dd/mm/yyyy (fecha de envio)
    Time: hh:mm (hora del envio)
    Phone Number: +541234567891 (numbero de telefono o id de grupo)
    Message: Oferta activa! (mensaje enviado)
```

