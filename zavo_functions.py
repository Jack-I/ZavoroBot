"""This file contains functions, which are used as "Callable" args
 in Command- and MessageHandlers in bot.py """

import logging
import random

from filtration import rand_uri  # for text generating

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def alarm(context):
    """Send the random message from Uras_speech.txt."""
    context.bot.send_message(chat_id=context.job.context, text=rand_uri())


def start(update, context):
    """Posts welcome message and activates main mission of the bot -
    sending messages with random delay.
    It launches after receiving /start command"""
    chat_id = update.message.chat_id

    # check if start was called before
    if 'job' in context.chat_data:
        update.message.reply_text('Анус себе стартани, собаня')
        return

    # first start
    context.bot.send_message(chat_id=chat_id, text="Я Юрий Завоботный! Прива, петушки.")
    interval = random.normalvariate(60, 10)
    first = random.randint(3, 25)  # delay of fist message after /start command
    # Add job to queue
    # It's very important to pass chat_id optional arg to run_repeating method
    job = context.job_queue.run_repeating(alarm, interval=interval, first=first, context=chat_id)
    context.chat_data['job'] = job

    # Add start info to log
    logger = logging.getLogger(__name__)
    logger.info("BOT STARTED by " + update.message.from_user.first_name)


def shut_up(update, context):
    """Completely stops random message posting"""

    # Check if there are no jobs in queue
    if 'job' not in context.chat_data:
        update.message.reply_text('Да молчу я, блять, молчу!')
        return

    # obtaining job from chat_data and removing it
    job = context.chat_data['job']
    job.schedule_removal()
    del context.chat_data['job']
    update.message.reply_text('LADNO')

    # Add start info to log
    logger = logging.getLogger(__name__)
    logger.info("MESSAGE POSTING WAS STOPPED by " + update.message.from_user.first_name)


def echo(update, context):
    """Replies to any reply to any bot's message.
    Context arg isn't used, but it's required for MessageHandler "Callable" argument"""
    pool = ("Нит", "Не хочу", "БИГА", "Ряба!", "Не на того напали", "*Гулкий, раскатистый звук пердежа*",
            "А ты приходи на ДКД, раз такой умный", "♠", "тому что ты пидор ёпта",
            "*Звук краткого пердка*", "*Звук газоизвержения торопливого, но не лишенного смысла*",
            "У меня набор байт, как гороховый суп")
    text = pool[random.randint(0, len(pool) - 1)]
    update.message.reply_text(text=text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper() + "!!!!1"
    context.bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def helper(update, context):
    """Lists all available commands"""
    chat_id = update.message.chat_id
    text = "Available commands:\n" \
           "/start - to make a text chaos began\n" \
           "/ORU \"message\" -> \"MESSAGE!!1\" \n" \
           "/zatknis_nahuy - to make the bot slightly quieter"
    context.bot.send_message(chat_id=chat_id, text=text)


# error logging
def error(update, context):
    """Log Errors caused by Updates."""
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# def stop(update, context):
#     context.bot.send_message(chat_id=update.message.chat_id, text="Покедова")
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                         level=logging.INFO)
#     logger = logging.getLogger(__name__)
#     logger.info("BOT STOPPED: " + str(update.message.text) )
#     updater.stop() # TODO: сделать так, чтобы работало

# обработчик неизвестных команд
# должен стоять ПОСЛЕ всех остальных обработчиков
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Не понимаю я эту команду, да и она мне, собственно, до пизды.")
    logger = logging.getLogger(__name__)
    logger.info("Unknown command: " + str(update.message.text).lstrip("/") + " from " +
                update.message.from_user.first_name)
