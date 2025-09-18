# CurrencyBot

**CurrencyBot** is a Telegram bot for currency conversion and viewing real-time exchange rates.

---

## 🚀 Features

- Convert any currency to any other using the [exchangerate.host](https://exchangerate.host) API.  
- View real-time exchange rates of selected currencies against the US Dollar (USD).  
- Ability to add or remove currencies you want to track.  
- Exchange rates are updated automatically upon request.

---

## 🛠 Requirements

- Python 3.10+  
- Aiogram 3.x  
- aiohttp  
- python-dotenv  

---

## ⚡ Installation

1. Clone the repository:  
```bash
git clone https://github.com/Ggyuiiiiiiiijhtcc/CurrencyBot.git
cd CurrencyBot
```

2. Install dependencies:  
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your API key and bot token:  
```env
API_KEY=your_exchangerate_host_key
TOKEN=your_telegram_bot_token
```

4. Run the bot:  
```bash
python start.py
```

---

## 🔧 Configuring Tracked Currencies

- In `handlers.py`, locate the block where current exchange rates are requested:  
```python
params = {
    "access_key": os.environ.get('API_KEY'),
    "base": "USD",
    "currencies": "EUR,PLN,RUB,UAH"  # Add or remove currencies here
}
```

- To add a currency: add its code separated by a comma, e.g., `"EUR,PLN,RUB,UAH,GBP"`  
- To remove a currency: delete its code from the list.

---

## 💬 Bot Usage Examples

1. Currency conversion:  
```
/Convert
Enter currency: USD
Enter currency: UAH
Enter amount: 100
Result: 100 USD = 4137.00 UAH
```

2. View current exchange rates:  
```
/ChangeInfo
Dollar -> Euro : 0.92
Dollar -> Zloty : 3.59
Dollar -> Rubles : 92.11
Dollar -> Hryvnia : 41.23
```

---

## 🌐 Links

- [exchangerate.host](https://exchangerate.host) — source for currency exchange rates

---

## ⚠️ Important

- A **valid API key** from [exchangerate.host](https://exchangerate.host) is required for the bot to work.  
- Do **not** commit your `.env` file with API keys or tokens to a public repository.

---

## 🗑️ Author

[Ggyuiiiiiiiijhtcc](https://github.com/Ggyuiiiiiiiijhtcc)

---

## 🗒 License

MIT

