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

line_bot_api = LineBotApi('N2GpmrsY58aYsKnZdK3kds71H+S9ENOLGCfG6J/lzdTZFankDggZBUdqWOyEPSqg9bVH2xw7ISvMU9vGZzTP/gEk1smuhTRqy3XVvwex1eevd8zIIZNfuo5DKDHz3slU0QvjmMvWZLurbu0BlEIUiAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d1870fbf70dd66d23a02eb791e2a7ab1')


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