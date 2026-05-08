````md
# Binance Futures Trading Bot

This is a simple Python trading bot built for Binance Futures Testnet.  
The project supports placing MARKET and LIMIT orders using Binance Futures API.

The application is built with a clean project structure, CLI support, logging, input validation, and error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL orders
- CLI-based input using argparse
- Input validation
- Logging for API requests and errors
- Error handling for invalid inputs and API failures
- Uses Binance Futures Testnet

---

## Tech Stack

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

---

## Project Structure

```bash
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── .env
├── cli.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/salman-devs/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

Windows:
```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the root folder.

Example:

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

---

## Running the Application

### MARKET Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### LIMIT Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Logging

Logs are stored inside:

```bash
logs/trading.log
```

The log file contains:
- API request logs
- API responses
- Error logs

---

## Assumptions

- Binance Futures Testnet account is already created
- API keys are valid
- User has internet connection while placing orders

---

## Future Improvements

- Add Stop-Limit orders
- Add interactive CLI menus
- Add async support
- Add unit tests

---

## Author

Salman
````
