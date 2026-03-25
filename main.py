import time
import os
from DrissionPage import ChromiumPage, ChromiumOptions
from config import USER, PASSWORD, LINK_PAGE
from scraper.login import login_page, navigation_page
from scraper.extractor import obtain_groups
from services.telegram_bot import send_message


def main():

    page = ChromiumPage()
    #page.set.window.mini()

    # Inciar sesion y navegar hasta el maestro de oferta
    result = login_page(page, USER, PASSWORD, LINK_PAGE)
    if result == "restart":
        return "restart"

    if result == "stop":
        return "stop"

    navigation_page(page)

    # Scrapear maestro de oferta
    messages = obtain_groups(page)

    # Send message to telegram
    if messages:
        for message in messages:
            send_message(message)
    else:
        print("No existen grupos cargados!")
    
    page.quit()
    return "ok"


if __name__ == "__main__":
        while True:
            try:
                result = main()

                if result == "restart":
                    print(" Reiniciando flujo...\n")
                    continue

                if result == "stop":
                    print(" Deteniendo programa")
                    break

                print("Esperando 60s...")
                time.sleep(60)
                
            except Exception as e:
                os.system("pkill -f chrome")
                continue 