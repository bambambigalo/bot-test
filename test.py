
import telebot

bot = telebot.TeleBot("1099773673:AAHnJWAwcJzMh7_4kNg6V5oOV0HeZBBy8QA")

@bot.message_handler(commands = ["start"])
def start_messages(message):
	bot.send_massage(message.chat.id, "huli ti mne pishesh?/start")

	bot.polling()