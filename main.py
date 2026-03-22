import time
from DrissionPage import ChromiumPage, ChromiumOptions
from config import USER, PASSWORD, LINK_PAGE
from scraper.login import login_page, navigation_page
from scraper.extractor import obtain_groups
from services.telegram_bot import send_message


def main():

    opciones = ChromiumOptions()
        
    # Le decimos la ruta exacta del Chrome que viene en GitHub
    opciones.set_browser_path('/usr/bin/google-chrome')
    
    opciones.set_argument('--no-sandbox')
    opciones.set_argument('--disable-dev-shm-usage')

    page = ChromiumPage(opciones)

    # Inciar sesion y navegar hasta el maestro de oferta
    login_page(page, USER, PASSWORD, LINK_PAGE)
    navigation_page(page)

    # Scrapear maestro de oferta
    messages = obtain_groups(page)

    # Send message to telegram
    for message in messages:
        send_message(message)
    
    page.quit()


if __name__ == "__main__":
    while True:
        main()
        print("Esperando 60s")
        time.sleep(60)