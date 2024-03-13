from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import random
import string
import requests
import json

def run_bot():
    extension_path = "captcha\solver.crx"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Chrome ayarları ve eklenti yolu
    chrome_options = Options()
    chrome_options.add_extension(extension_path)

    # Chrome tarayıcısını başlat
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # Tarayıcı penceresini tam ekran yap

    # Web sitesine git
    driver.get("https://playvalorant.com/tr-tr/")

    # Bekleyici oluştur ve 5 saniye bekleyin
    wait = WebDriverWait(driver, 5)

    # "HEMEN OYNA" bağlantısını bul ve tıkla
    xpath_hemen_oyna = "//div[@class='_2ufF-mwQT8vFKXiFr6RXs2 riotbar-account-anonymous-link-wrapper']//a[@data-testid='riotbar:account:button-play-now']"
    element_hemen_oyna = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_hemen_oyna)))
    element_hemen_oyna.click()

    # "HESAP OLUŞTUR" düğmesini bul ve tıkla
    xpath_hesap_olustur = "//span[contains(@class, 'PrimaryButton-module--label-text--qK7Ui') and text()='HESAP OLUŞTUR']"
    element_hesap_olustur = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_hesap_olustur)))
    element_hesap_olustur.click()

    # E-posta adresi alanını bul ve rastgele e-posta gir
    xpath_email = "//input[@data-testid='riot-signup-email']"
    email_input = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_email)))
    random_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@gene.com"
    email_input.send_keys(random_email)

    # "Kayıt Ol" düğmesini bul ve tıkla
    xpath_kayit_ol = "//button[@data-testid='btn-signup-submit']"
    element_kayit_ol = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_kayit_ol)))
    element_kayit_ol.click()

    # Gün, ay ve yıl aralığı belirle
    min_year = 1978
    max_year = 2005
    birth_year = random.randint(min_year, max_year)
    birth_month = random.randint(1, 12)
    if birth_month in [1, 3, 5, 7, 8, 10, 12]:
        birth_day = random.randint(1, 31)
    elif birth_month in [4, 6, 9, 11]:
        birth_day = random.randint(1, 30)
    else:
        if birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0):
            birth_day = random.randint(1, 29)
        else:
            birth_day = random.randint(1, 28)

    # Doğum günü alanlarını bul ve değerlerini gir
    day_input = driver.find_element(By.XPATH, "//input[@name='birth_date_day']")
    month_input = driver.find_element(By.XPATH, "//input[@name='birth_date_month']")
    year_input = driver.find_element(By.XPATH, "//input[@name='birth_date_year']")

    day_input.clear()
    day_input.send_keys(str(birth_day))

    month_input.clear()
    month_input.send_keys(str(birth_month))

    year_input.clear()
    year_input.send_keys(str(birth_year))

    # Kayıt ol düğmesini bul ve tıkla
    element_kayit_ol = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_kayit_ol)))
    element_kayit_ol.click()

    # Rastgele kullanıcı adı oluşturma fonksiyonu
    def generate_username():
        prefix = "Ware"  
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) 
        return prefix + random_name  

    # Kullanıcı adı alanını bul ve rastgele kullanıcı adını yaz
    xpath_username = "//input[@data-testid='riot-signup-username']"
    username_input = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_username)))
    random_username = generate_username()
    username_input.send_keys(random_username)

    # Kayıt ol düğmesini bul ve tıkla
    element_kayit_ol = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_kayit_ol)))
    element_kayit_ol.click()

    # Rastgele şifre oluşturma fonksiyonu
    def generate_password():
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=24))  
        return random_password  

    # Şifre alanlarını bul ve rastgele şifreyi yaz
    xpath_password = "//input[@name='password']"
    password_input = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_password)))
    password = generate_password()
    password_input.send_keys(password)

    # Şifreyi onaylama alanlarını bul ve aynı şifreyi yaz
    xpath_confirm_password = "//input[@name='password-confirm']"
    confirm_password_input = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_confirm_password)))
    confirm_password_input.send_keys(password)

    # Kayıt ol düğmesini bul ve tıkla
    element_kayit_ol = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_kayit_ol)))
    element_kayit_ol.click()

    time.sleep(1)

    # JavaScript kodunu tanımla
    scroll_down_script = "document.getElementById('tos-scrollable-area').scrollTop = document.getElementById('tos-scrollable-area').scrollHeight"

    # JavaScript kodunu çalıştırarak scroll alanını en aşağıya kaydır
    driver.execute_script(scroll_down_script)

    # Checkbox'u bul
    checkbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tos-checkbox")))

    # Checkbox'u tıkla
    checkbox.click()

    # Kabul Et butonunun XPath'ini belirleyin
    xpath_kabul_et = "//button[@data-testid='btn-accept-tos']"

    # Kabul Et butonunu bulun
    btn_kabul_et = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_kabul_et)))

    # Kabul Et butonuna tıklayın
    btn_kabul_et.click()

# Kabul Et butonuna tıklayın
    btn_kabul_et.click()

    # Webhook işlemi
    webhook_url = ''

    # Kullanıcı adı, şifre ve e-posta
    kullanici_adi = random_username
    sifre = password
    eposta = random_email

    # Embed içeriği
    embed = {
        "title": "Yeni Kullanıcı Oluşturuldu",
        "description": "Aşağıda yeni kullanıcı bilgileri bulunmaktadır:",
        "color": 65280,  # Renk kodu (Yeşil)
        "fields": [
            {
                "name": "Kullanıcı Adı:",
                "value": kullanici_adi
            },
            {
                "name": "Şifre:",
                "value": sifre
            },
            {
                "name": "E-posta:",
                "value": eposta
            },
            {
                "name": "reis",
                "value": f"{random_username}:{password}"
            }
        ]
    }

    # Webhook isteği için JSON verisi oluştur
    payload = {
        "embeds": [embed]
    }

    # Discord Webhook'a POST isteği gönder
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    # İsteğin durumunu kontrol et
    if response.status_code == 204:
        print('Mesaj başarıyla gönderildi.')
    else:
        print(f'Mesaj gönderilirken bir hata oluştu. Durum kodu: {response.status_code}')



    while True:
        current_url = driver.current_url
        if current_url == "https://playvalorant.com/tr-tr/download/":
            print("İndirme sayfası bulundu. Tarayıcı kapatılacak.")
            driver.quit()
            break

        # Oyunu indir butonunun varlığını kontrol et
        download_button_xpath = "//h2[contains(@class, 'DownloadClient-module--title--FMT4b') and contains(text(), 'OYUNU İNDİR')]"
        download_button_elements = driver.find_elements(By.XPATH, download_button_xpath)
        if download_button_elements:
            print("OYUNU İNDİR butonu bulundu. Tarayıcı kapatılacak.")
            driver.quit()  # Tarayıcıyı kapat
            break  # Döngüyü sonlandır

        else:
            while True:
                error_message_xpath = "//p[@data-testid='error-message' and contains(text(), 'CAPTCHA seçimi hatalı')]"
                error_message_elements = driver.find_elements(By.XPATH, error_message_xpath)
                if error_message_elements:
                    print("CAPTCHA seçimi hatalı. Lütfen tekrar dene.")
                    btn_kabul_et.click()
                else:
                    print("Hata yok gibi.")
                    break  # İç içe döngüyü sonlandır

# 20 defa işlemi tekrar et
for _ in range(20):
    run_bot()
    time.sleep(2)  # Her işlemden sonra 2 saniye bekle
