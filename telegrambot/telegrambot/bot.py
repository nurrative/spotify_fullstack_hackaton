from telegram.ext import Updater, CommandHandler
from django.conf import settings
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6103860602:AAFMlm-Ja_ycv4QuFe7edTmptX32Uw2BV5w'
BOT_USERNAME: Final = '@shophaka_bot'



keyboard = telebot.types.InlineKeyboardMarkup()    #эти кнопки за нас не пишут
b1 = telebot.types.InlineKeyboardButton('ДА', callback_data='yes')
b2 =telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(b1,b2)


yes_sticker = 'CAACAgIAAxkBAAEIBW5kBYbQ08iWUanhn-Nvy59HyxAXfAACEwADwDZPE6qzh_d_OMqlLgQ'
no_sticker = 'CAACAgIAAxkBAAEIBXxkBYbdwMjR9yGSlRxfm4jvxntX2wACDgADwDZPEyNXFESHbtZlLgQ'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет, я бот! Рада вам помочь!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Попробуйте написать что-нибудь, и я постараюсь ответить!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Это пользовательская команда, вы можете добавить сюда любой текст.')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'Привет' in processed:
        return 'Здраствуйте'

    if 'Как твои дела?' in processed:
        return 'Я отлично,спасибо'

    if 'можно список продуктов?' in processed:
        return 'Конечно!'

    return 'Я вас не понимаю'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')


    if message_type == 'group':
   
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return  
    else:
        response: str = handle_response(text)

    
    print('Bot:', response)
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    
    app.add_error_handler(error)

    print('Polling...')
    

    app.run_polling(poll_interval=5)





TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот.")


def main():
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    # Добавьте другие обработчики команд

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
