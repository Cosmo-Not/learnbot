from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
from datetime import datetime, date, time

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

now = datetime.now()

def const(bot, update):
    user_text = update.message.text
    user_text_list = user_text.split()
    try:
        planet_class = getattr(ephem, user_text_list[1].capitalize())
        planet_instance = planet_class(f'{now.year}/{now.month}/{now.day}')
        print(ephem.constellation(planet_instance))
        update.message.reply_text(f'Планета находится в созвездии: {ephem.constellation(planet_instance)}')
    except AttributeError:
        print("Не знаю такой планеты :(")
        update.message.reply_text("Не знаю такой планеты :(")

def greet_user(bot, update):
    user_text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                                            update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", const))


    mybot.start_polling()
    mybot.idle()

main()