# CurrencyBot

**CurrencyBot** — это Telegram-бот для конвертации валют и просмотра актуальных курсов в реальном времени

---

## 🚀 Возможности

- Конвертация любой валюты в любую другую через API [exchangerate.host](https://exchangerate.host). 
- Просмотр актуальных курсов выбранных валют относительно доллара (USD)  
- Возможность добавлять или удалять валюты, которые вы хотите отслеживать 
- Актуальные курсы обновляются автоматически при запросе

---

## 🛠 Требования

- Python 3.10+  
- Aiogram 3.x  
- aiohttp  
- python-dotenv  

---

## ⚡ Установка

1. Клонируйте репозиторий:  
    ```bash
    git clone https://github.com/Ggyuiiiiiiiijhtcc/CurrencyBot.git
    cd CurrencyBot
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Создайте .env файл в корне проекта и добавьте ваш API ключ:
   ```bash
   API_KEY=ваш_ключ_с_exchangerate.host
   TOKEN = Токен_бота
4. Запустите бота:
   ```bash
   python start.py
##🔧 Настройка актуальных валют
- В файле handlers.py найдите блок, где запрашивается актуальный курс:
  ```bash
  params = {
    "access_key": os.environ.get('API_KEY'),
    "base": "USD",
    "currencies": "EUR,PLN,RUB,UAH"  # Добавляйте или удаляйте валюты здесь
  }
- Добавьте валюту: просто добавьте её код через запятую, например: "EUR,PLN,RUB,UAH,GBP"
## 💬 Примеры работы бота
1. Конвертация валют:
   ```bash
   /Convert
    Введите валюту: USD
    Введите валюту: UAH
    Введите сумму: 100
    Результат: 100 USD = 4137.00 UAH
2. Актуальные курсы:
    ```bash
   /ChangeInfo
   Доллар -> Евро : 0.92
   Доллар -> Злотый : 3.59
   Доллар -> Рубли : 92.11
   Доллар -> Гривна : 41.23

  ## 🌐 Ссылки

- [exchangerate.host](https://exchangerate.host) — сайт для получения курсов валют

  
