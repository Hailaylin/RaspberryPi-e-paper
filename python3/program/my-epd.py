#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
sys.path.append(r'../lib')

import epd2in9
import epdconfig
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

VER = 'Beta 0.1'

try:
    print("Hailay`s e-paper on RasPi ",VER)
    
    epd = epd2in9.EPD()
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)

    font40 = ImageFont.truetype('../lib/Font.ttc', 40)
    font24 = ImageFont.truetype('../lib/Font.ttc', 24)
    font18 = ImageFont.truetype('../lib/Font.ttc', 18)
    font14 = ImageFont.truetype('../lib/Font.ttc', 14)

    ###########################################################
    ##########################上行内容##########################
    ###########################################################
    print("时间局部刷新")
    epd.init(epd.lut_partial_update)
    epd.Clear(0xFF)
    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)

    time_draw.text((5, 0), 'Hailay`s e-paper', font = font18, fill = 0)
    time_draw.text((150, 0), 'on RasPi Beta 0.1', font = font18, fill = 0)
    #line((X0,Y0,X1,Y1))
    time_draw.line((0, 20, 296, 20), fill = 0)
    time_draw.line((0, 105, 296, 105), fill = 0)

    ###########################################################
    ##########################中间内容##########################
    ###########################################################
    
    #输出音乐图像
    print("输出音乐图像")
    music_bmp = Image.open('../pic/music.bmp')
    time_image.paste(music_bmp, (232,107))

    #话语
    time_draw.text((190, 90), u'学习使我超快乐!', font = font14, fill = 0)

    ###########################################################
    ###########################下行内容#########################
    ###########################################################

    #输出闹钟图像
    print("输出闹钟图像")
    timg_bmp = Image.open('../pic/timg.bmp')
    time_image.paste(timg_bmp, (276,107))

    #输出天气:雨图像
    print("输出雨图像")
    rain_bmp = Image.open('../pic/rain-black.bmp')
    time_image.paste(rain_bmp, (254,107))



    num = 0
    while (True):
        if(num == 30):
            #30min/次全局刷新以维护墨水屏生命周期
            epd.init(epd.lut_full_update)
            epd.Clear(0xFF)
            #切换回局部刷新
            epd.init(epd.lut_partial_update)
            epd.Clear(0xFF)
            #计数归零
            num = 0
        else:
            #每分钟刷新一次时间
            #创建一个空白的矩形
            time_draw.rectangle((105, 106, 165, 128), fill = 255)
            #时间文本
            time_draw.text((5, 103), time.strftime('%y-%m-%d %H:%M %a'), font = font24, fill = 0)
            #空白矩形上文字后裁剪出局部刷新部分
            newimage = time_image.crop([105, 106, 165, 128])
            time_image.paste(newimage, (105,106))
            epd.display(epd.getbuffer(time_image))
            time.sleep(30)
            #刷新计数
            num = num + 1

    ###########停止后############
    time.sleep(1)

    print("Clear...")
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)

    print("Goto Sleep...")
    epd.sleep()

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("ctrl + c:")
    epdconfig.module_exit()
    exit()
