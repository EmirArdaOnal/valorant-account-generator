# Valorant Account Creator Bot
While using this account generator, the user is solely responsible for any issues that may arise. Responsibility cannot be attributed to me. This is merely a sample sharing.

CAPTCHA Solver extensions or codes will not be provided. You should handle CAPTCHA issues on your own.

## 📜 Tanım

**Valorant Account Creator Bot** otomatik olarak Valorant web sitesine giderek hesap oluşturan ve Discord webhook'u ile bu bilgileri paylaşan bir Selenium botudur. Özellikle çok sayıda hesap oluşturmak isteyen kullanıcılar için idealdir.

## 🚀 Özellikler

- **Captcha Solver Desteği**: Captcha çözmek için bir Chrome uzantısı kullanır.
- **Otomatik Bilgi Girişi**: Rastgele e-posta, kullanıcı adı, doğum tarihi ve şifre oluşturur.
- **Discord Webhook Entegrasyonu**: Oluşturulan hesap bilgilerini belirttiğiniz Discord webhook'una gönderir.
- **Hata Yönetimi**: Hata durumlarını kontrol eder ve gerektiğinde tekrar dener.

## 🛠️ Gereksinimler

- Python 3.x
- Selenium
- ChromeDriver
- Pillow
- Captcha Solver uzantısı

### Gerekli Kütüphanelerin Kurulumu

```sh
pip install selenium requests
```

## 💻 Kurulum ve Kullanım

### 1. Projeyi Klonlayın

```sh
git clone https://github.com/EmirArdaOnal/valorant-account-generator.git
cd valorant-account-creator-bot
```

### 2. Gerekli Kütüphaneleri Yükleyin

```sh
pip install selenium requests
```

### 3. ChromeDriver'ı İndirin ve Kurun

[ChromeDriver](https://sites.google.com/chromium.org/driver/) indirip, `PATH` değişkenine ekleyin.

### 4. Captcha Solver Uzantısını Ekleyin

Captcha solver uzantısını indirin ve `captcha/solver.crx` yoluna koyun.

### 5. `webhook_url` Değerini Ayarlayın

Discord webhook URL'nizi kod içindeki `webhook_url` değişkenine ekleyin.

### 6. Betiği Çalıştırın

```sh
python valorant_account_creator.py
```

### Örnek

Betiği çalıştırdığınızda, bot aşağıdaki adımları gerçekleştirecektir:

1. Valorant web sitesine gidip "Hemen Oyna" butonuna tıklar.
2. Rastgele bir e-posta adresi girerek hesap oluşturma sürecini başlatır.
3. Rastgele bir doğum tarihi girer.
4. Rastgele bir kullanıcı adı ve şifre oluşturur.
5. Kullanıcı adı, şifre ve e-posta bilgilerini Discord webhook'a gönderir.
6. "Kabul Et" butonuna tıklayıp, CAPTCHA doğrulamasını kontrol eder.
7. İşlem başarılı olduğunda veya hata durumunda gerekli işlemleri yapar.

---
