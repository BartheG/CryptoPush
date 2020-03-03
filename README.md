# CryptoPush

## Install

```bash
pip3 install -r requirements.txt
```
You must create a private.py file which will be use to get specific informations like private key or email to send.
See Configuration part for more informations.

## Usage

```bash
python3 cryptopush.py
```

## Configuration private.py (Example)

**Configuration of the sender mail server**
mailconfig = {
	'addr':"sendermail@mail.com",
	'password':"123456789",
	'host':"smtp.gmail.com",
	'port':587}

**Configuration of the message**
messageconfig = {
	"mail":"receivermail@mail.com",
	"message":"Message to send"
}

**Configuration of the sender sms server**
smsconfig = {
	"apikey":"apikey987689",
	"apisecret":"privatekey6789087",
	"message":"Message to send",
	"from":"+xxxxxxxxxxx",
	"to":"+xxxxxxxxxxx"
}