from selenium.webdriver.common.by import By
import time

def obtener_clima(driver, consulta):
    # Buscar el clima en Google
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")
    time.sleep(1.5)  # Esperar a que cargue

    try:
        # --------- Ciudad ---------
        try:
            ciudad = driver.find_element(By.CSS_SELECTOR, "span.BBwThe").text
        except:
            ciudad = consulta.capitalize()

        # --------- Temperatura ---------
        try:
            temperatura = driver.find_element(By.CSS_SELECTOR, "span#wob_tm").text
        except:
            temperatura = "N/A"

        # --------- Descripción (soleado, lluvioso…) ---------
        try:
            descripcion = driver.find_element(By.CSS_SELECTOR, "span#wob_dc").text
        except:
            descripcion = "Sin descripción"

        # --------- Unidad (C / F) ---------
        try:
            unidad = driver.find_element(By.CSS_SELECTOR, "div.vk_bk.wob-unit span.wob_t").text
        except:
            unidad = "°C"

        return f"Clima en {ciudad}: {temperatura}{unidad}, {descripcion}"

    except Exception:
        return "No se pudo obtener el clima en este momento."
