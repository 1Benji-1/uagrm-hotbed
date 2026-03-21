import requests
from config import TELEGRAM_TOKEN


def send_message(mensaje):
    # Reemplaza esto con el @ de tu canal o el número -100...
    CHAT_ID = "-1002576388501" 
    
    # Armamos la URL exacta para tu bot
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    # Armamos el paquete con los datos que exige Telegram
    payload = {
        "chat_id": CHAT_ID,
        "text": mensaje,
        "parse_mode": "HTML" # Esto es un extra genial: te permite usar etiquetas <b> o <i> en tu mensaje
    }
    
    # Disparamos la petición a los servidores de Telegram
    try:
        respuesta = requests.post(url, data=payload)
        
        # Comprobamos si Telegram nos dio el "Ok" (Código 200)
        if respuesta.status_code == 200:
            print("✅ ¡Mensaje enviado al canal con éxito!")
        else:
            print(f"❌ Error de Telegram: {respuesta.text}")
            
    except Exception as e:
        print(f"❌ Error de conexión: {e}")

