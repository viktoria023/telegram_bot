# import everything
import re
from flask import Flask, request
import telegram
from telebot.credentials import bot_token, URL
from telebot.controls import get_response

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# start the flask app
app = Flask(__name__)


@app.route("/bot", methods=["POST"])
async def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode("utf-8").decode()
    # for debugging purposes only
    print("got text message :", text)

    # here we call our super AI
    response = get_response(text)

    # now just send the message back
    # notice how we specify the chat and the msg we reply to
    await bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return "ok"


@app.route("/set_webhook", methods=["GET", "POST"])
async def set_webhook():
    print("{URL}/bot".format(URL=URL))
    s = bot.setWebhook("{URL}/bot".format(URL=URL))
    result = await s
    print(result)
    if result:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route("/")
def index():
    return "."


if __name__ == "__main__":
    app.run(threaded=True)
