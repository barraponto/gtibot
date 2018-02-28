'''GTI BOT Logic'''

import os
import pytz
from schedule import SCHEDULE
from telegram.ext import Updater, CommandHandler

SP_TIMEZONE = pytz.timezone('America/Sao_Paulo')
CLASS_MESSAGE = 'A {position} aula é de {class_.subject} na {class_.room}.'
ACCOUNT_MESSAGE = '''
*** CONTA DE DRIVE DA SALA ***
Usuário: `{username}`
Senha: `{password}`
'''


def get_sao_paulo_datetime(message):
    '''Gets message datetime localized for São Paulo.'''
    # message.date is localized to the server, let's UTC it
    utc_datetime = message.date.astimezone(pytz.utc)
    # now let's essepê it
    return utc_datetime.astimezone(SP_TIMEZONE)


def google_account(bot, update):
    '''Informs the credentials for class google account'''
    update.message.reply_text(ACCOUNT_MESSAGE.format(
        username=os.environ.get('GOOGLE_ACCOUNT_USERNAME'),
        password=os.environ.get('GOOGLE_ACCOUNT_PASSWORD'),
    ), parse_mode='markdown')


def classroom(bot, update):
    '''Tells the class name and room for the day.'''
    sp_datetime = get_sao_paulo_datetime(update.message)
    next_classes = SCHEDULE[sp_datetime.weekday()]
    message = ' '.join([
        CLASS_MESSAGE.format(class_=next_classes[0], position='primeira'),
        CLASS_MESSAGE.format(class_=next_classes[1], position='segunda')
    ])
    update.message.reply_text(message)


updater = Updater(os.environ.get('TELEGRAM_API_KEY'))
updater.dispatcher.add_handler(CommandHandler('sala', classroom))
updater.dispatcher.add_handler(CommandHandler('conta', google_account))
updater.start_polling()
updater.idle()
