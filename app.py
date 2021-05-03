from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('raVqlbyRQ0KtvfKL4iAKJP+L5VFGb7DzOP9coZHdbJQyQ5FvZjuJJdzOk+Xr5CrABO46sg1lKCQvxGDz4rYUDl9DgGG139q53LL/X6OZpxmj6J6iQeDNcx4dawBom/RvA6rGp8gTtwCJbgmIM+DL2QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('45c06d01972da29095427e473e6285ac')

# 監聽所有來自 /callback 的 Post Request
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

def searchKey(msg):
    word = {'聯成':'成人補習班',
            '台中停水':'台中點此連結:https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html',
            '桃園停水':'桃園點此連結:https://wateroff.water.gov.tw/city/%E6%A1%83%E5%9C%92%E5%B8%82/index.html',
            '美女':'陳羽捷',
            '朱家':'個個臥虎長龍',
            'ubike':'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json/?page=0&size=700',
            '東海大學':'AI智慧大學'}
    
    return word.get(msg,'不知道你說什麼')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    msg = event.message.text#接收訊息
    msg = searchKey(msg)#收到什麼送什麼
    
    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
