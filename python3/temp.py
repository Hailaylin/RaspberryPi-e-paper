
    print("0.初始化与刷新")
    epd.init(epd.lut_full_update)
    epd.Clear(0xFF)
	

	
    #渲染上层标题
    print("1.渲染上层标题")
    #生成画布，255=白色
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    #创建绘制对象
    draw = ImageDraw.Draw(Himage)
    
    draw.text((5, 0), 'Hailay`s e-paper', font = font18, fill = 0)
    draw.text((150, 0), u'on RasPi Beta 0.0', font = font18, fill = 0)
    #line((X0,Y0,X1,Y1))
    draw.line((0, 20, 296, 20), fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(5)
