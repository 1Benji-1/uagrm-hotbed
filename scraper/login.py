import time
import random

def login_page(page, user, password, link):

    page.get(link)

    page.wait.load_start()

    page.ele('#txtUsuario').input(user)
    time.sleep(random.uniform(0.5, 1.5))

    page.ele('#txtContrasena').input(password)

    print("Esperando captcha...")

    # Esperar a que el botón se habilite
    while True:
        btn = page.ele('#btnIngresar')
        
        if btn and btn.attr('disabled') is None:
            print("Botón habilitado ✅")
            break
        
        time.sleep(0.5)

    time.sleep(1)

    print("Haciendo click...")
    page.run_js("document.getElementById('btnIngresar').click()")


def navigation_page(page):

    buttom_select = page.ele('xpath://tr[contains(., "BOLETA INSC.")]//a')
    buttom_select.click()

    page.wait.load_start()

    buttom_menu = page.ele('xpath://li[contains(., "Menú Actual")]//a')
    buttom_menu.click()

    page.wait.load_start()

    buttom_menu_other_services = page.ele('xpath://li[contains(., "Otros Servicios")]//a')
    buttom_menu_other_services.click()

    page.wait.load_start()

    buttom_oferted_teacher = page.ele('.glyphicon glyphicon-book')
    buttom_oferted_teacher.click()

    page.wait.load_start()

    buttom_all = page.ele('#rbCupo_2')
    buttom_all.click()

    button_all_signatures = page.ele('#cbxTmat')
    button_all_signatures.click()

    time.sleep(1)

    button_show_grups = page.ele('#btnVerGrupo')
    button_show_grups.click()

    

