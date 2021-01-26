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

line_bot_api = LineBotApi('SaWwjJ/jLmkTT4TXZn4EVsRp0/kg+98pU21Za7I7JQ0ZnxiFRTGNXdK0Bt4+mJK2764XiAJ8YeTxaod4l5XhTsIIRvShB2piYB2bLjsmDQvHSLcW6C/LR3vc49Q1ppG0a6rSOVHK5MFtPEakGRZWSAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8df46cc5aef3c510b05f236d235161bc')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()