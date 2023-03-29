import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler,filters

# Replace 'your_bot_token' with your own bot token
bot = telegram.Bot(token='1620955534:AAF_IqirCsaLxC_yudC5FC6LAfwzAoBq0ZU')

def start(update, context):
    """Starts the bot and sends a welcome message"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!")

def get_chat_id(update, context):
    """Gets the chat ID of the current chat"""
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="The chat ID is: {}".format(chat_id))

def main():
    """Starts the bot"""
    updater = Updater('1620955534:AAF_IqirCsaLxC_yudC5FC6LAfwzAoBq0ZU',True)
    dp = updater.dispatcher

    # Add handlers for commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('get_chat_id', get_chat_id))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
