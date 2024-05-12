import pywhatkit

def send_message(telefono,mensaje,hora,minuto):
    pywhatkit.sendwhatmsg("+593"+telefono,mensaje,int(hora),int(minuto))