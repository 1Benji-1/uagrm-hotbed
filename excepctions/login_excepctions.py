import re, time

def exception_button(page, message):
    if "Contraseña incorrecta" in message:
        page.quit()
        print("Credenciales incorrectos")
        return "stop"

    elif "Captcha inválido" in message:
        page.quit()
        print("Captcha inválido!!")
        return "restart"

    elif "Ya ingresó al sistema de inscripción web." in message:
        page.quit()
        print("Ya ingresó al sistema, espere")

        match = re.search(r'\d+', message)
        number = int(match.group()) if match else 0

        time.sleep(number + 10)
        return "restart"

    else:
        page.quit()
        print(message)
        print("Error desconocido")
        return "stop"


def exception_checkbox(page, ele):
    print("HACIENDO CLICK EN EL CHECKBOX")
    if not ele.attr('checked'):
        try:
            ele.click()
        except:
            page.run_js("document.querySelector('.cb-lb input').click()")

