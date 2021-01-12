import re
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

url = "https://www.moneycontrol.com/broker-research/stocks.html"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
today = (date.today() - timedelta(days=1)).strftime("%b %d, %Y")

def parse_rec(rec_text):
	# tmp = rec_text.split(': |;')
	tmp = re.split('; |:', rec_text)
	call = tmp[0].split(' ',1)[0]
	cmpy = tmp[0].split(' ',1)[1]
	trgt = tmp[1].split()[-1]
	brkr = tmp[2]
	res = call + cmpy + trgt + brkr
	return "Result:" + res


# All recommendations
rec_stock = soup.select('div.Ohidden')
for cur_rec in rec_stock:

	date_txt = cur_rec.find('p').get_text()
	if (not date_txt.endswith(today)):
		continue

	rec_text = cur_rec.find_all('p')[1]
	rec_text = rec_text.get_text()
	# print(rec_text)
	print(parse_rec(rec_text))

# print(today)