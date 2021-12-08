import telebot

api_token = '1746032409:AAH1cvjANa1kgDiK03eCOjG6MDDExRzueO4'
bot = telebot.TeleBot (api_token)
@bot.message_handler(commands = "start")



def command_start(message, res=False):
	bot.send_message(message.chat.id, 'Andrey_vbot в твоем распоряжении. Напиши "help" для получения доп. информации')


@bot.message_handler(content_types=["text"])

def send_text(message):
	if message.text == "help":
		bot.send_message(message.chat.id, '''
											Чему меня научил создатель:
											"hello" - буду тебя приветствовать;
											"hdu" - расскажу как мои дела;
											"by" - жаль, будем прощаться
										   '''
										 )
	if message.text == "hello":
		bot.send_message(message.chat.id, 'Привет создатель')

	if message.text == "hdu":
		bot.send_message(message.chat.id, 'У меня отлично, я же бот :)')

	if message.text == "by":
		bot.send_message(message.chat.id, 'До скорых встреч создатель')



bot.polling(non_stop=True, interval = 0)