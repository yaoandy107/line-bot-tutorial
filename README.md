# Line Bot 教學

本教程介紹如何使用 Python LINE Bot SDK 在 Heroku 上架設一個簡單的學舌鳥機器人。

如果您想以另一種語言架設範例 bot，請參閱以下  LINE Bot SDK repositories。
- [PHP](https://github.com/line/line-bot-sdk-php)
- [Go](https://github.com/line/line-bot-sdk-go)
- [Perl](https://github.com/line/line-bot-sdk-perl)
- [Ruby](https://github.com/line/line-bot-sdk-ruby)
- [Python](https://github.com/line/line-bot-sdk-python)
- [Node.js](https://github.com/line/line-bot-sdk-nodejs)

## 在你開始之前

確保您具有以下內容：

- 在 Line 的控制台為您的機器人創建了一個頻道 [#教學](https://developers.line.me/en/docs/messaging-api/getting-started/)
- 一個 [Heroku](https://www.heroku.com) 的帳戶（您可以免費創建一個）

## 架設範例機器人

按照以下步驟架設一個學舌鳥機器人。


1. 登入 Heroku 後，
  在 [Heroku](https://dashboard.heroku.com/apps) 頁面中，點選 New -> Create New App
  ![](https://i.imgur.com/Y3njp7I.png)
2. 輸入自己喜歡的 App name ，然後點擊 Create app
  ![](https://i.imgur.com/WJ85jXR.png)
3. 下載 [範例程式碼](https://github.com/yaoandy107/line-bot-tutorial/archive/master.zip)
4. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的機器人
  ![](https://i.imgur.com/n3bQym2.png)
5. 取得 **channel secret** 和 **channel access token**，如果沒有內容，請點 Issue
  ![](https://i.imgur.com/entIggx.png)
6. 使用編輯器開啟範例程式碼資料夾內的 app.py，填入 **channel secret** 和 **channel access token**
  ![](https://i.imgur.com/Uz16joi.png)
7. 並使用 Heroku CLI 將程式部署到 Heroku 上面 （請參考 [使用 Heroku CLI](#使用-heroku-cli)）
8. 使用以下 URL 格式在控制台中輸入 webhook URL 
  `{HEROKU_APP_NAME}.herokuapp.com/callback`
  注意：{HEROKU_APP_NAME} 是步驟2中的應用程序名稱
9. 通過在控制台的 “Channel settings” 頁面上掃描 QR Code，將您的機器人添加到 LINE 的朋友中
10. 在 Line 上向您的機器人發送文字訊息，並確認它使用相同的訊息進行回應

## 使用 Heroku CLI

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 開啟範例程式碼資料夾，在路徑上輸入 cmd
3. 使用終端或命令行應用程序登錄到 Heroku
```shell＝
heroku login
```
4. 初始化 git
``` shell=
$ git config --global user.name "你的名字"
$ git config --global user.email 你的信箱
```
5. 將資料夾初始成 git 空間
```shell＝
git init
```
6. 用 git 將資料夾與 heroku 連接
```shell＝
heroku git:remote -a {HEROKU_APP_NAME}
```
    注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱
7. 將資料夾底下所有檔案加入 git 清單，如跳出錯誤訊息請重新執行
```shell
git add .
```
8. 儲存記錄點，如跳出錯誤訊息請詳讀
```shell
git commit -m "Init"
```
    注意："Init" 可使用任意文字替換，其為此紀錄點的敘述
9. 將在 git 清單中的檔案上傳到 heroku，請確認訊息是否顯示成功
```shell
git push heroku master
```
**每當需要更新 Bot 時，請重新執行 7、8、9 步驟**

第一次操作完請回到 [架設範例機器人](#架設範例機器人) 第 5 項繼續接下來的步驟
## 檢查你的日誌
```
當成是遇到問題時，可查看日誌以找出錯誤
```
要查看您的機器人在 Heroku 的日誌，請按照以下步驟。

1. 如果沒登入，請先透過 Heroku CLI 登入
```shell
heroku login
```

2. 顯示 app 日誌
```shell
heroku logs --tail --app {HEROKU_APP_NAME}
```
注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱。
​    
    --tail    # 持續打印日誌
    --app {HEROKU_APP_NAME}    # 指定 App

## 程式解說
```
資料夾裡需含有兩份文件來讓你的程式能在 heroku 上運行
```
- Procfile：heroku 執行命令，web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 **web: python app.py**。
- requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件

### app.py
可透過修改程式裡的 handle_message() 方法內的程式碼來達成不同的回覆效果。

![](https://i.imgur.com/DNeNbpV.png)

新版範例程式碼內附註解
如想更多了解此程式，可以去研究 Python3、[Flask 套件](http://docs.jinkan.org/docs/flask/)、[Line bot sdk](https://github.com/line/line-bot-sdk-python)


## 更多花樣
[官方文件](https://github.com/line/line-bot-sdk-python#api)
### 基本操作
#### 回應訊息
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
#### 主動傳送訊息
bot 需要有 push 功能才可以做，否則會出錯
```python
line_bot_api.push_message(push_token, 訊息物件)
```

### 傳送訊息物件

[官方文件](https://devdocs.line.me/en/#send-message-object)

修改範例程式碼中， handle_message() 方法內的程式碼，可實現多種功能

#### TextSendMessage （文字訊息）
```python
message = TextSendMessage(text='Hello, world')
line_bot_api.reply_message(event.reply_token, message)
```
#### ImageSendMessage（圖片訊息）
```python
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

#### VideoSendMessage（影片訊息）
```python
message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

#### AudioSendMessage（音訊訊息）
```python
message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
line_bot_api.reply_message(event.reply_token, message)
```
#### LocationSendMessage（位置訊息）
```python
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.reply_message(event.reply_token, message)
```

#### StickerSendMessage（貼圖訊息）
```python
message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.reply_message(event.reply_token, message)
```

#### ImagemapSendMessage
```python
message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://example.com/',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - ButtonsTemplate （按鈕介面訊息）
```python
message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - ConfirmTemplate（確認介面訊息）
```python
message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - CarouselTemplate
```python
message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```

#### TemplateSendMessage - ImageCarouselTemplate
```python
message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
