from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        return

    if msg in ['Hi', 'hi', '嗨', '你好']:                                      # rule-based
        r = '嗨！簡貝貝'
    elif msg in ['Love you', '愛你', '愛泥', '愛尼', '愛妳', '愛你辣']:           # NLP natural language processing
        r = '偶也愛你辣'
    elif msg in ['吃了嗎', '吃飯了嗎', '餓嗎', '寶貝餓了嗎', '寶貝要吃什麼']:
        r = '餓扁了幫我外送'
    elif msg in ['飲料', '要喝飲料嗎', '好想喝飲料', '好渴']:
        r = '奶綠加小芋圓'
    elif msg in ['早餐', 'breakfast']:
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
    elif msg in ['寶貝在幹嘛']:
        r = '乾妳屁毛'
    elif msg in ['寶貝', 'baby', '水水']:
        r = '我還是你寶貝嗎'
    elif msg in ['當然囉', '當然是啊', '當然', '是啊']:
        r = '那就好小胖呆'
    elif msg in ['寶貝到囉', '寶貝到家囉', '寶貝到家了']:
        r = '快ㄑ洗澡澡'
    elif msg in ['我在騎車', '騎車', '騎車中']:
        r = '66以下，不然殺人'
    elif msg in ['我去牽車車', '我去牽車', '我把車牽過來']:
        r = '好慢吶～～'
    elif msg in ['排位', '寶貝要不要打排位', '要不要打排位', '寶貝貝要不要打排位']:
        r = '我不跟銅牌玩誒'
    elif msg in ['好可愛', '好可愛！']:
        r = '你更可愛'
    elif msg in ['咬你喔']:
        r = '來咩！！！！'
    elif msg in ['我難過', '我好難過', '我心情不好']:
        r = '寶貝鼻要難過有我在'
    elif msg in ['吵架', '來吵架啊', '來吵架']:
        r = '你很狗屎'
    elif msg in ['我想你', '我好想你']:
        r = 'me2 快來找我'
    elif msg in ['寶貝早安']:
        r = '早餐要吃什麼':
    elif msg in ['早餐要吃什麼']:
        r = '我先問的你先說辣'
    elif msg in ['哈哈哈哈']:
        r = '沒那麼好笑吧'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()