# import everything
import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, bot_user_name, URL

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# start the flask app
# app = Flask(__name__)

import logging
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

# Set your bot token here
TOKEN = "your_telegram_bot_token_here"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


# Define a command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your test bot.")


# Define a message handler
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"You said: {update.message.text}")


def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()


# @app.route("/{}".format(TOKEN), methods=["POST"])
# def respond():
#     # retrieve the message in JSON and then transform it to Telegram object
#     update = telegram.Update.from_json(request.get_json(force=True), bot)

#     chat_id = update.message.chat.id
#     msg_id = update.message.message_id

#     # Telegram understands UTF-8, so encode text for unicode compatibility
#     text = update.message.text.encode("utf-8").decode()
#     # for debugging purposes only
#     print("got text message :", text)
#     # the first time you chat with the bot AKA the welcoming message
#     if text == "/start":
#         # print the welcoming message
#         bot_welcome = """
#        Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ to generate cool looking avatars based on the name you enter so please enter a name and the bot will reply with an avatar for your name.
#        """
#         # send the welcoming message
#         bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

#     else:
#         try:
#             # clear the message we got from any non alphabets
#             text = re.sub(r"\W", "_", text)
#             # create the api link for the avatar based on http://avatars.adorable.io/
#             url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
#             # reply with a photo to the name the user sent,
#             # note that you can send photos by url and telegram will fetch it for you
#             bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
#         except Exception:
#             # if things went wrong
#             bot.sendMessage(
#                 chat_id=chat_id,
#                 text="There was a problem in the name you used, please enter different name",
#                 reply_to_message_id=msg_id,
#             )

#     return "ok"


# @app.route("/set_webhook", methods=["GET", "POST"])
# def set_webhook():
#     s = bot.setWebhook("{URL}{HOOK}".format(URL=URL, HOOK=TOKEN))
#     if s:
#         return "webhook setup ok"
#     else:
#         return "webhook setup failed"


# @app.route("/")
# def index():
#     return "."


if __name__ == "__main__":
    # app.run(threaded=True)
    main()
