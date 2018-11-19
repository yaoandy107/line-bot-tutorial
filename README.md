# Line Bot 教學

本教程介紹如何使用 Python LINE Bot SDK 在 Heroku 上架設一個簡單的回話機器人。
<!--more-->
如果您想以另一種語言架設範例 bot，請參閱以下  LINE Bot SDK repositories。
- [PHP](https://github.com/line/line-bot-sdk-php)
- [Go](https://github.com/line/line-bot-sdk-go)
- [Perl](https://github.com/line/line-bot-sdk-perl)
- [Ruby](https://github.com/line/line-bot-sdk-ruby)
- [Python](https://github.com/line/line-bot-sdk-python)
- [Node.js](https://github.com/line/line-bot-sdk-nodejs)

## 在你開始之前

確保您具有以下內容：

- 擁有 Line 帳號
- 擁有 [Heroku](https://www.heroku.com) 帳戶（您可以免費創建一個）

## 建立 Heroku 專案
1. 登入 Heroku 後，
  在 [Heroku](https://dashboard.heroku.com/apps) 頁面中，點選 New -> Create New App
  ![](https://i.imgur.com/Y3njp7I.png)
2. 輸入自己喜歡的 App name ，然後點擊 Create app
  ![](https://i.imgur.com/WJ85jXR.png)

## 創建 Line Bot 頻道
1. 進入 [Line 控制台](https://developers.line.me/console/)
    ![](https://i.imgur.com/vseYQt1.png)
2. 創建提供者
    ![](https://i.imgur.com/0tnYFBd.png)
3. 填入提供者名稱
    ![](https://i.imgur.com/2ne3H1F.png)
4. 點擊 Create
    ![](https://i.imgur.com/bdESW8G.png)
5. 點擊 Create Channel
    ![](https://i.imgur.com/F1nAWhK.png)
6. 填入 Bot 資訊
    ![](https://i.imgur.com/3wYFSvl.png)
7. 同意 Line 條款，並按 Create
    ![](https://i.imgur.com/WNzl4sL.png)
8. 選擇剛剛創建的 Bot
    ![](https://i.imgur.com/6ocsOBW.png)

## 設定範例機器人

按照以下步驟架設一個回話機器人。

1. 下載 [範例程式碼](https://github.com/yaoandy107/line-bot-tutorial/archive/master.zip)
2. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的機器人
    ![](https://i.imgur.com/6ocsOBW.png)
3. 開啟 webhook
![](https://i.imgur.com/nxvFPB1.png)
![](https://i.imgur.com/PzEKzdq.png)
4. 關閉預設罐頭回覆訊息
![](https://i.imgur.com/nXPRhT4.png)

5. 產生 **Channel access token**
![](https://i.imgur.com/QyxnpZB.png)
![](https://i.imgur.com/quYbPx9.png)
6. 取得 **Channel access token**
![](https://i.imgur.com/C7OTect.png)
7. 取得 **Channel secret**
![](https://i.imgur.com/IwmvyzL.png)

6. 使用編輯器開啟範例程式碼資料夾內的 app.py，將剛剛取得的 **channel secret** 和 **channel access token** 填入
  ![](https://i.imgur.com/Uz16joi.png)

## 將程式推到 Heroku 上

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 開啟剛剛下載的範例程式碼資料夾，在路徑上輸入 cmd
3. 使用終端或命令行應用程序登錄到 Heroku
    ```shell＝
    heroku login
    ```
4. 初始化 git
    ``` shell=
    $ git config --global user.name "你的名字"
    $ git config --global user.email 你的信箱
    ```
    注意：**你的名字** 和 **你的信箱** 要換成各自的 **名字** 和 **信箱**

5. 初始化 git
    ```shell＝
    git init
    ```
    注意：僅第一次使用時要輸入

6. 用 git 將資料夾與 heroku 連接
    ```shell＝
    heroku git:remote -a {HEROKU_APP_NAME}
    ```
    注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱
    
7. 輸入以下指令，將程式碼推上 Heroku，**如果有跳出錯誤請重新輸入**
    ```shell
    git add .
    git commit -m "Add code"
    git push -f heroku master
    ```
    **每當需要更新 Bot 時，請重新輸入上述指令**

## 將 Heroku 與 Line 綁定
1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
    ![](https://i.imgur.com/6ocsOBW.png)
2. 在 webhook URL 中輸入 Heroku 網址

    ```shell
    {HEROKU_APP_NAME}.herokuapp.com/callback
    ```
    ![](https://i.imgur.com/EkDhAgb.png)
    注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱

  
## 測試範例成果
1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
    ![](https://i.imgur.com/6ocsOBW.png)
2. 通過在控制台的 “Channel settings” 頁面上掃描 QR Code，將您的 Bot 添加到 LINE 的朋友中
3. 在 Line 上向您的 Bot 發送文字訊息，並確認它會學你說話

## 錯誤尋找

> 當程式遇到問題時，可查看日誌以找出錯誤

要查看您的 Bot 在 Heroku 的日誌，請按照以下步驟。

1. 如果沒登入，請先透過 Heroku CLI 登入
    ```shell
    heroku login
    ```

2. 顯示 app 日誌
    ```shell
    heroku logs --tail --app {HEROKU_APP_NAME}
    ```
    注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱。
    ```shell
    --tail                     # 持續打印日誌
    --app {HEROKU_APP_NAME}    # 指定 App
    ```

## 程式檔案解說

> 資料夾裡需含有兩份文件來讓你的程式能在 heroku 上運行

- Procfile：heroku 執行命令，web: {語言} {檔案}，這邊語言為 python，要自動執行的檔案為 app.py，因此我們改成 **web: python app.py**。
- requirements.txt：列出所有用到的套件，heroku 會依據這份文件來安裝需要套件

### app.py (主程式)
可透過修改程式裡的 handle_message() 方法內的程式碼來控制機器人的訊息回覆

![](https://i.imgur.com/DNeNbpV.png)

新版範例程式碼內附註解
如想更多了解此程式，可以去研究 Git、Python3、[Flask 套件](http://docs.jinkan.org/docs/flask/)、[Line bot sdk](https://github.com/line/line-bot-sdk-python)


## 進階操作
[官方文件](https://github.com/line/line-bot-sdk-python#api)
### 回覆訊息
只有當有訊息傳來，才能回覆訊息
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
### 主動傳送訊息
Bot 需要有開啟 push 功能才可以做，否則程式會出錯
```python
line_bot_api.push_message(push_token, 訊息物件)
```

## 訊息物件分類

[官方文件](https://developers.line.me/en/docs/messaging-api/message-types/)

修改範例程式碼中， handle_message() 方法內的程式碼，可實現多種功能

### TextSendMessage （文字訊息）
![](https://i.imgur.com/LieCFAb.png =250x)
```python
message = TextSendMessage(text='Hello, world')
line_bot_api.reply_message(event.reply_token, message)
```

### ImageSendMessage（圖片訊息）
![](https://i.imgur.com/RaH7gqo.png =250x)
```python
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

### VideoSendMessage（影片訊息）
![](https://i.imgur.com/o6cvf3o.png =250x)
```python
message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```

### AudioSendMessage（音訊訊息）
![](https://i.imgur.com/w5szZag.png =250x)
```python
message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
line_bot_api.reply_message(event.reply_token, message)
```

### LocationSendMessage（位置訊息）
![](https://i.imgur.com/tXE7Aus.png =250x)
```python
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.reply_message(event.reply_token, message)
```

### StickerSendMessage（貼圖訊息）
![](https://i.imgur.com/7x0mgK1.png =250x)
```python
message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.reply_message(event.reply_token, message)
```

### ImagemapSendMessage （組圖訊息）
![](https://i.imgur.com/MoSf2D6.png =250x)
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

### TemplateSendMessage - ButtonsTemplate （按鈕介面訊息）
![](https://i.imgur.com/41lXWjP.png =250x)
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

### TemplateSendMessage - ConfirmTemplate（確認介面訊息）
![](https://i.imgur.com/U8NDhrt.png =250x)
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

### TemplateSendMessage - CarouselTemplate
![](https://i.imgur.com/982Glgo.png =250x)
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

### TemplateSendMessage - ImageCarouselTemplate
![](https://i.imgur.com/2ys1qqc.png =250x)
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
