from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

import os
import json
from linebot.models import *
import re
import weather
line_bot_api = LineBotApi(os.environ['Channel_access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

line_bot_api.push_message('U973285e89a0d95987a98f8cae9816116',TextSendMessage(text="bot 啟動"))



def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        message = event.message.text
        if re.match('告訴我秘密',message):
          
            image_message = ImageSendMessage(
                original_content_url='https://www.cwb.gov.tw//Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-2022-04-22-07-10.jpg',
                preview_image_url='https://www.cwb.gov.tw//Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-2022-04-22-07-10.jpg'
            )
            line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='雲層圖 : 2022/04/22 7:10 '),image_message])
        
        if re.match('雲層圖',message):
            loc = weather.crawler('雲層')
            image_message = ImageSendMessage(
                original_content_url=loc['source'],
                preview_image_url=loc['source']
            )
            line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='雲層圖 : '+loc['time']),image_message])
            
        if re.match('雷達圖',message):
            loc = weather.crawler('雷達')
            image_message = ImageSendMessage(
                original_content_url=loc['source'],
                preview_image_url=loc['source']
            )
            line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='雷達圖 : '+loc['time']),image_message])
            
        if re.match('雨量圖',message):
            loc = weather.crawler('雨量')
            image_message = ImageSendMessage(
                original_content_url=loc['source'],
                preview_image_url=loc['source']
            )
            line_bot_api.reply_message(event.reply_token, [TextSendMessage(text='雨量圖 : '+loc['time']),image_message])
        
        if '幫助' or '協助' or '救援' in message:
            flex_message = FlexSendMessage(
                alt_text='回復',
                contents={
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "請問需要甚麼協助?",
                        "weight": "bold",
                        "size": "xl"
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": []
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                              {
                                "type": "text",
                                "text": "119救護專線",
                                "color": "#666666",
                                "size": "xxl",
                                "flex": 1
                              },
                              {
                                "type": "text",
                                "text": "如欲相當危急情況請直接撥打119",
                                "wrap": True,
                                "color": "#aaaaaa",
                                "size": "md",
                                "flex": 5
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                              {
                                "type": "text",
                                "color": "#666666",
                                "size": "xxl",
                                "text": "1999專線"
                              },
                              {
                                "type": "text",
                                "wrap": True,
                                "color": "#aaaaaa",
                                "size": "md",
                                "flex": 5,
                                "text": "排水道溢、淹水事件處理"
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                          "type": "postback",
                          "data": "website",
                          "label": "防災資訊網"
                        }
                      },
                      {
                        "type": "button",
                        "style": "primary",
                        "height": "sm",
                        "action": {
                          "type": "postback",
                          "label": "搜尋附近超商",
                          "data": "shop"
                        }
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "postback",
                          "label": "天氣資訊",
                          "data": "weather"
                        },
                        "height": "sm",
                        "style": "primary"
                      }
                    ],
                    "flex": 0
                  }
                } #json貼在這裡
            )
            line_bot_api.reply_message(event.reply_token, flex_message)
            # buttons_template_message = TemplateSendMessage(
            #     alt_text='這個看不到',
            #     template=ButtonsTemplate(
            #         thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
            #         title='行銷搬進大程式',
            #         text='選單功能－TemplateSendMessage',
            #         actions=[
            #             PostbackTemplateAction(
            #                 label='台北市',
            #                 text='台北市',
            #                 data='台北市'
            #             ),
            #             MessageAction(
            #                 label='光明正大傳資料',
            #                 text='我就是資料'
            #             ),
            #             URIAction(
            #                 label='行銷搬進大程式',
            #                 uri='https://marketingliveincode.com/'
            #             )
            #         ]
            #     )
            # )   
            
            #line_bot_api.reply_message(event.reply_token, buttons_template_message)
            
        # elif isinstance(event, PostbackEvent):
        #     back_button = TemplateSendMessage(
        #         alt_text='Buttons template',
        #         template=ButtonsTemplate(
        #             title='Menu',
        #             text='請選擇美食類別',
        #             actions=[
        #                 PostbackTemplateAction(  # 將第一步驟選擇的地區，包含在第二步驟的資料中
        #                     label='火鍋',
        #                     text='火鍋',
        #                 ),
        #                 PostbackTemplateAction(
        #                     label='早午餐',
        #                     text='早午餐',
        #                 ),
        #                 PostbackTemplateAction(
        #                     label='約會餐廳',
        #                     text='約會餐廳',
        #                 )
        #             ]
        #         )
        #     )
        #     line_bot_api.reply_message(event.reply_token,back_button)
            
    
    
    @handler.add(PostbackEvent)
    def handle_postback(event):
        
        if event.postback.data == 'weather':
            flex_message = FlexSendMessage(
                alt_text='天氣圖',
                contents={
                "type": "carousel",
                "contents": [
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://images-ext-1.discordapp.net/external/WoJuPRxYtTb4ejt4DRtbucvimqyS62-c0FVHMPFo3jA/https/www.cwb.gov.tw/Data/radar/CV1_3600_202204221320.png?width=670&height=670",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "雷達圖",
                          "weight": "bold",
                          "size": "sm",
                          "wrap": True
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "spacing": "sm",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "雷達回波圖",
                                  "wrap": True,
                                  "color": "#8c8c8c",
                                  "size": "xs",
                                  "flex": 5
                                }
                              ]
                            },
                            {
                              "type": "button",
                              "action": {
                                "type": "message",
                                "text": "雷達圖",
                                "label": "點擊"
                              },
                              "style": "primary",
                              "margin": "xs"
                            }
                          ]
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://images-ext-1.discordapp.net/external/UgGWHyP51NXUResMezeSaQhtgKucKaMf8mg6jdHSpUM/https/www.cwb.gov.tw/Data/rainfall/2022-04-22_1300.QZJ8.jpg?width=670&height=670",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "雨量圖",
                          "weight": "bold",
                          "size": "sm",
                          "wrap": True
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "spacing": "sm",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "當日累積雨量圖",
                                  "wrap": True,
                                  "color": "#8c8c8c",
                                  "size": "xs",
                                  "flex": 5
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "type": "button",
                          "action": {
                            "type": "message",
                            "label": "點擊",
                            "text": "雨量圖"
                          },
                          "margin": "xs",
                          "style": "primary",
                          "gravity": "bottom"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  },
                  {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                      "type": "image",
                      "url": "https://www.cwb.gov.tw//Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-2022-04-22-13-20.jpg",
                      "size": "full",
                      "aspectMode": "cover",
                      "aspectRatio": "320:213"
                    },
                    "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "text": "雲層圖",
                          "weight": "bold",
                          "size": "sm"
                        },
                        {
                          "type": "box",
                          "layout": "vertical",
                          "contents": [
                            {
                              "type": "box",
                              "layout": "baseline",
                              "spacing": "sm",
                              "contents": [
                                {
                                  "type": "text",
                                  "text": "衛星雲層圖",
                                  "wrap": True,
                                  "color": "#8c8c8c",
                                  "size": "xs",
                                  "flex": 5
                                }
                              ]
                            }
                          ]
                        },
                        {
                          "type": "button",
                          "action": {
                            "type": "message",
                            "label": "點擊",
                            "text": "雲層圖"
                          },
                          "margin": "xs",
                          "style": "primary"
                        }
                      ],
                      "spacing": "sm",
                      "paddingAll": "13px"
                    }
                  }
                ]
              } #json貼在這裡
            )
            line_bot_api.reply_message(event.reply_token, flex_message)
            
            
        if event.postback.data == 'website':
            flex_message = FlexSendMessage(
                alt_text='網站',
                contents={
                  "type": "bubble",
                  "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                      "type": "uri",
                      "uri": "http://linecorp.com/"
                    },
                    "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRltmqSrLh0aFnRDRNZ3LnNLsZlD43r2NEW8zIB0p9xUesn3PdWiPjNwG5OYAW5ZUVm4aY&usqp=CAU"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "防災資訊網",
                        "weight": "bold",
                        "size": "xl"
                      }
                    ]
                  },
                  "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "label": "水利署防災資訊網",
                          "uri": "https://fhy.wra.gov.tw/fhyv2/"
                        },
                        "margin": "xs",
                        "height": "sm",
                        "style": "secondary"
                      },
                      {
                        "type": "button",
                        "style": "secondary",
                        "action": {
                          "type": "uri",
                          "label": "中央氣象局",
                          "uri": "https://www.cwb.gov.tw/V8/C/"
                        },
                        "margin": "xs",
                        "height": "sm",
                        "position": "relative",
                        "gravity": "bottom"
                      },
                      {
                        "type": "button",
                        "style": "secondary",
                        "height": "sm",
                        "action": {
                          "type": "uri",
                          "uri": "https://dmap.ncdr.nat.gov.tw/1109/map/",
                          "label": "3D災害潛勢地圖"
                        },
                        "margin": "xs"
                      },
                      {
                        "type": "button",
                        "action": {
                          "type": "uri",
                          "uri": "https://246.swcb.gov.tw/",
                          "label": "土石流防災資訊網"
                        },
                        "margin": "xs",
                        "style": "secondary",
                        "height": "sm"
                      }
                    ],
                    "flex": 0
                  }
                }
            )
            line_bot_api.reply_message(event.reply_token, flex_message)
          
            
        
        # elif event.postback.data == 'datetime_postback':
        #     line_bot_api.reply_message(
        #         event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
        # elif event.postback.data == 'date_postback':
        #     line_bot_api.reply_message(
        #         event.reply_token, TextSendMessage(text=event.postback.params['date']))
                
    @handler.add(MessageEvent, message=LocationMessage)
    def handle_location_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            LocationSendMessage(
                title='Location', address=event.message.address,
                latitude=event.message.latitude, longitude=event.message.longitude
            )
        )
    # @handler.add(MessageEvent, message=TextMessage)
    # def handle_message(event):
        
    
    
        

    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
            }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
        }
