from telegram.ext import Updater
import logging
import telegram
from telegram.ext import CommandHandler

TOKEN = '894277302:AAGfzF3Oh11Vy6BB_Sxyo5iT3V2wdVjhrfc'

proxy_kwargs = {'proxy_url': 'socks5h://163.172.152.192:1080'}
updater = Updater(TOKEN, request_kwargs=proxy_kwargs)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("BOT DEPLOYED.")


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Я Юрий Завоботный, прива, петушки!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
#updater.idle()
