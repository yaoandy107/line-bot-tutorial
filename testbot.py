from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('MVmYw0QniNhUwvGZOXp4qY1wiCrDclTpKDjk1CxN/TzFagcx1zvBD0p8lGOfxeXCTguB7cV9Xuge7Gya0Cvid6hBavQRioOps1GEv2Bh4DBG2v/ilAEU/8brktgr0eucqIFahMvMezVF+X5YZWppfwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('86472ce3d72be2286e0b53e75b792dfa')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()