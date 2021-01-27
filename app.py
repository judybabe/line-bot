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
    msg = event.message.text
    r = '蛤～'

    if msg in ['Hi', 'hi', '嗨', '你好']:
        r = '嗨！簡貝貝'
    elif msg in ['Love you', '愛你', '愛泥', '愛尼', '愛妳']:
        r = '偶也愛你辣'
    elif msg in ['吃了嗎', '吃飯了嗎', '餓嗎', '寶貝餓了嗎']:
        r = '餓扁了幫我外送'
    elif msg in ['飲料', '要喝飲料嗎', '好想喝飲料', '好渴']:
        r = '奶綠加小芋圓'
    elif msg in ['早餐', '早餐要吃什麼', 'breakfast']:
        r = '麵線大辣油像菜沙茶多'
    elif msg in ['午餐', '午餐要吃什麼', 'lunch']:
        r = '鍋媽'
    elif msg in ['晚餐要吃什麼', '晚餐']:
        r = '卡地夫松阪豬'
    elif msg in ['軟爛', '軟']:
        r = '你才軟'
    elif msg in ['要不要去卡地夫吃飯']:
        r = '衝'
    elif msg in ['晚安', '寶貝晚安', '寶貝貝晚安']:
        r = '簡嘉寶晚安'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()