"""
Simple Bot to send timed Telegram messages.
Based on python-telegram-bot library
(https://github.com/python-telegram-bot/python-telegram-bot)

To create message pool you have to manually use pre_filtration.py.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs infinite.

Usage:
Basic busy-friend replacing bot. Periodically sends one short random message from your
friend's messages from your chat history. Also it can reply fixed phrases (10 available)
if someone replies to bot's message.

Available commands:
           "/start" - initiates random posting
           "/ORU somemessage" - to make bot post "SOMEMESSAGE!!1"
           "/zatknis_pozhaluysta" - to stop random posting

Notice:
    Please rename config.sample.py to config.py and fill TOKEN and PROXY variables
     with correspond values
"""

import logging  # guess why

from telegram.ext import Updater
from telegram.ext import CommandHandler  # for command recognition
from telegram.ext import MessageHandler  # for sending messages
from telegram.ext import Filters  # for echo

import zavo_functions as z  # callable functions for handlers
import config  # to store TOKEN and PROXY variables.

TOKEN = config.TOKEN
KWARGS = config.KWARGS

# TODO: на сервере в конфиге написать PROXY = None
updater = Updater(TOKEN, request_kwargs=KWARGS, use_context=True)
dispatcher = updater.dispatcher
job_q = updater.job_queue  # for tasks with delay

# more in https://github.com/python-telegram-bot/python-telegram-bot/wiki/Exception-Handling
logging.basicConfig(filename="Main.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("BOT DEPLOYED.")

# Command handlers
start_handler = CommandHandler('start', z.start, pass_args=True, pass_job_queue=True, pass_chat_data=True)
dispatcher.add_handler(start_handler)
shut_up_handler = CommandHandler('zatknis_pozhaluysta', z.shut_up, pass_chat_data=True)
dispatcher.add_handler(shut_up_handler)
caps_handler = CommandHandler('ORU', z.caps)
dispatcher.add_handler(caps_handler)
help_handler = CommandHandler('help', z.helper)
dispatcher.add_handler(help_handler)

# Message handlers
echo_handler = MessageHandler(Filters.text, z.echo)
dispatcher.add_handler(echo_handler)
unknown_handler = MessageHandler(Filters.command, z.unknown)
dispatcher.add_handler(unknown_handler)

# Error handler
dispatcher.add_error_handler(z.error)

# Start the bot
updater.start_polling()
