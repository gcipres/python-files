import yfinance as yf
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_SENDER = "xxx@gmail.com"
EMAIL_PASSWORD = "xxx"

EMAIL_RECEIVER = "xxx@gmail.com"

ticket_price = {
    'TSLA': 250,
    'AAPL': 180,
}

def send_mail(ticker, price, current_price):
    asunto = f"Price notificatoin: {ticker}"
    cuerpo = f"{ticker} is down to ${price} dollars, current price is ${current_price} dollars."

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = asunto

    msg.attach(MIMEText(cuerpo, 'plain'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email send: {asunto}")
    except Exception as e:
        print(f"Error to send mail: {e}")

def prices_verify():
    global ticket_price
    while ticket_price:
        tickets_to_delete = []
        for ticker, base in ticket_price.items():
            try:
                info = yf.Ticker(ticker).info
                current_price = info['regularMarketPrice']
                print(f"{ticker}: current price={current_price}, base price={base}")
                if current_price <= base:
                    send_mail(ticker, base, current_price)
                    tickets_to_delete.append(ticker)
            except Exception as e:
                print(f"Error getting data of {ticker}: {e}")
        for ticker in tickets_to_delete:
            del ticket_price[ticker]
        time.sleep(60)

if __name__ == "__main__":
    prices_verify()
