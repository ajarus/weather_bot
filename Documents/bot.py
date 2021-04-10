#mkdir bots
#cd bots
#sudo apt-get install python3-venv
#python3 -m venv my-project-env
#source my-project-env/bin/activate
#pip3 install pyTelegramBotAPI
#nano bots.py
#python3 bots.py
import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

bot = telebot.TeleBot("1627412626:AAFbE-0EosiHqIeWU8dC89ts4NKoZvSKXJU")
owm = OWM('09cda72f689ecd429972aabe60a35596')
mgr = owm.weather_manager()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp =w.temperature('celsius')['temp']
	answer = "В городе " + message.text + " сейчас " + str(temp)
	bot.send_message(message.chat.id, answer)

bot.polling()
