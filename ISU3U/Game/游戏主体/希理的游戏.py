print('Welcome to my game!\nby希理\n')
#库导入
import pygame,os,random,time
from pygame.locals import *
from sys import exit

#游戏设置
#background_image_filename = "sushiplate.jpg"
#mouse_image_filename = 'fugu.png'
#pygame.init()
#font = pygame.font.SysFont("arial",40)
#sfont = pygame.font.SysFont("arial",20)

play = 'Y'#初始化play数据
reset = 'Y'#初始化reset数据
while play == 'Y' or play == 'y':#确定是否玩
	if reset == 'Y' or reset == 'y':#确定是否重设设定 #游戏个人设置，默认设置
		#游戏个人设置
		custom_setting = ''#初始化个性设定
		while not(custom_setting == 'Y' or custom_setting == 'N' or custom_setting == 'y' or custom_setting == 'n'):#是否需要个性设定
			custom_setting = 'N' #input('Do you want custom settings?(default=N)(Y or N)\n')
			if custom_setting == '':
				custom_setting = 'N'
			if custom_setting == 'N' or custom_setting =='n':#不需要个性设定
				screen_size = (720,480)
				WD = 'W'
				BS = 3
				TS = 4
				TW = 5
				CS = 'N'
			elif custom_setting == 'Y' or custom_setting == 'y':#需要个性设定
				
				RP = -1#初始化RP数据
				screen_size = (1920,1080)#初始化screen_size数据
				while RP == -1:# or '2' or '3':#分辨率(RP)设置
					RP = input('What is your resolution?(default= 480p)\n1: 1080p\n2: 720p\n3: 480p\n')
					if RP == '':#字符转数字
						RP = 3
					elif RP == '1' or RP=='2'or RP=='3':
						RP = int(RP)
					else:
						RP = -1
					
					if RP == 1:#确定分辨率
						screen_size = (1920,1080)
					elif RP == 2:
						screen_size = (1280,720)
					elif RP == 3:
						screen_size = (720,480)
		#			print(screen_size)#分辨率测试
				
				WD = ''
				while not(WD == 'F' or WD == 'W' or WD == 'f' or WD == 'w'):#是否要全屏
					WD = input('Do you want a full screen or a window?(default=W)(F or W)\n')
					if WD == '':
						WD = 'W'
				
				BS = -1#初始化BS
				while not(BS > 0):#球速(BS)设定(可能要改默认速度
					BS = input('What Ball Speed do you want?(1-7)(default = 3)\n')
					if BS == '':
						BS = 3
					elif BS.isdigit():
						if int(BS)<=7 and int(BS)>=1:
							BS = int(BS)
						else:
							BS = -1
					else:
						BS = -1
		#			print(BS)#球速测试
				
				TS = -1#初始化板速
				while not(TS > 0):#板速(TS)设定(可能要改默认速度
					TS = input('What Table Speed do you want?(1-10)(default = 4)\n')
					if TS == '':
						TS = 4
					elif TS.isdigit():
						if int(TS)<=10 and int(TS)>=1:
							TS = int(TS)
						else:
							TS = -1
					else:
						TS = -1
		#			print(TS)#板速测试

				TW = -1#初始化板长
				while not(TW > 0):#板长(TW)设定
					TW = input('How wide do you want the Table?(1-10)(default = 5)\n')
					if TW == '':
						TW = 5
					elif TW.isdigit():
						if int(TW)<=10 and int(TW)>=1:
							TW = int(TW)
						else:
							TW = -1
					else:
						TW = -1
		#			print(TW)#板速测试
				#TW = (screen_size[0]//70)*TW
				CS = ''#初始化CS
				while not(CS == 'Y' or CS == 'N' or CS == 'y' or CS == 'n'):#是否进行自定义方块
					CS = input('Do you want to customize the block?(default=Y)(Y or N)\n')
					if CS == '':
						CS = 'Y'
						
		#以适屏重设
		TW = (screen_size[0]//50)*TW
		BS = (screen_size[0]//1000+1)*BS
		TS = (screen_size[0]//350)*TS
		
	#游戏初始化
	os.system('cls')#清屏
	pygame.mixer.pre_init(44100,16,2,8192)#声音模块初始化
	pygame.init()#游戏主体初始化
	if WD == 'W' or WD == 'w':#设置分辨率和是否全屏
		screen = pygame.display.set_mode(screen_size,0,32)#窗口化
	else:
		screen = pygame.display.set_mode(screen_size,FULLSCREEN,32)#全屏
	pygame.display.set_caption("希理的游戏")#游戏名初始化
	Frames = pygame.time.Clock()#初始化帧数时钟
	TT = 'N'#初始化板回状态
	TL = screen_size[0]//2#板的默认位置
	Table = Rect((0,0),(TW,screen_size[1]//150))#板的矩形
	Table.center = (TL,screen_size[1]-screen_size[1]//20)#默认板的位置
	Ball = Rect((0,0),(5,5))#球的矩形
	Ball.center = (screen_size[0]//2,screen_size[1]//4*3)#默认球的位置
	BV = random.choice((-1,1))#球左右随机方向
	XS = BV*BS#球X速
	YS = -BS#球Y速
	pygame.mouse.set_visible(False)#鼠标不可见

	start_surface = pygame.font.SysFont("arial",40).render("Press any key to start the Game!",False,(255,255,255))#字体初始化
	lost_surface = pygame.font.SysFont("arial",40).render("YOU ARE LOST!!!!!",False,(255,255,255))
	win_surface = pygame.font.SysFont("arial",40).render("YOU ARE WIN!!!!!",False,(255,255,255))
	Note_surface = pygame.font.SysFont("arial",20).render('Click the mouse to create a block   Press any key to leave the page',False,(255,255,255))
	
	pygame.mixer.music.load("music.mp3")#声音初始化
	lostsound = pygame.mixer.Sound("lost.ogg")
	winsound = pygame.mixer.Sound("win.ogg")
#	background = pygame.image.load(background_image_filename).convert()
#	mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
	
	#计算方块列表
	pygame.mixer.music.play(-1)
	CNX=10
	CNY=5
	CWX = screen_size[0]//(CNX+1)
	CLX = (CWX*2)//3
	CWLY = (screen_size[1]//2)//(CNY*2+1)
	rect = []
	if CS == 'N' or CS == 'n':#默认方块列表
		for Fx in range(0,CNX):
			for Fy in range(0,CNY):
				left = (CWX*2//3)+Fx*CWX
				top = CWLY+Fy*2*CWLY 
				width = CLX
				height = CWLY
				rect.append(Rect((left,top),(width,height)))
				#print(Fx,Fy)
	else:#自定义方块列表
		exit_flag = False#默认不关闭窗口
		pygame.mouse.set_visible(True)
		while True:
			for event in pygame.event.get():
				if event.type == MOUSEBUTTONDOWN:
					mx,my = pygame.mouse.get_pos()
					newrect = Rect((0,0),(CLX,CWLY))
					newrect.center = (mx,my)
					if my < screen_size[1]*2//3 and newrect.collidelist(rect)==-1:
						rect.append(newrect)
				if event.type == QUIT:#退出事件
					exit()
				if event.type == KEYDOWN:#按键事件
					if len(rect) !=0:
						exit_flag = True
						
			if exit_flag:#关闭窗口事件
				break
			
			pygame.draw.line(screen,(255,255,255),(0,screen_size[1]*2//3+CWLY//2),(screen_size[0],screen_size[1]*2//3+CWLY//2))
			for Drect in rect:#画方块
				pygame.draw.rect(screen,(255,255,255),Drect)
			screen.blit(Note_surface,(screen_size[0]//2-Note_surface.get_width()//2,screen_size[1]*3//4))
			pygame.display.update()
		pygame.mouse.set_visible(False)
	#print(CWX,CLX,CWLY)
	#print(rect)#方块数据检查
	
	#游戏前停止页面

	exit_flag = False
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:#退出事件
				exit()
			if event.type == KEYDOWN:#按键事件
				exit_flag = True
		screen.fill((0,0,0))
		screen.blit(start_surface,(screen_size[0]//2-start_surface.get_width()//2,screen_size[1]//2-start_surface.get_height()))
		if exit_flag:
			break
		pygame.display.update()
		
	#游戏进程
	exit_flag = False#默认不关闭窗口
	move = {K_LEFT:0,K_RIGHT:0}
	while True:#游戏循环开始
		
		Frames_number = Frames.tick(100)#帧数限制
		
		#获取事件
		for event in pygame.event.get():
			if event.type == QUIT:#退出事件
				exit()
			if event.type == KEYDOWN:#按键事件
				if event.key == K_ESCAPE:#关闭窗口
					exit_flag = True
				if event.key in move:#按下键盘
					move[event.key] = 1
			if event.type == KEYUP:#放开键盘
				if event.key in move:
					move[event.key] = 0
		
		if exit_flag:#关闭窗口事件
			pygame.quit()
			break
			
		#计算板移动距离
		if TL-TS*move[K_LEFT] > TW//2+Ball.width//2:
			TL -= TS*move[K_LEFT]
			if TT == 'Y':#球跟着板动
				Ball.centerx -= TS*move[K_LEFT]
		else:
			TL = TW//2+1
		if TL+TS*move[K_RIGHT] < screen_size[0]-TW//2-Ball.width//2:
			TL += TS*move[K_RIGHT]
			if TT == 'Y':
				Ball.centerx += TS*move[K_RIGHT]
		else:
			TL = screen_size[0]-TW//2-1
		Table.centerx = TL
		#print(TL)#移动距离测试
		#print(Table)
		
		#球的运动运算
		if TT == 'Y':#跳出板回
			if time.time()-PT > 0.5:
				TT = 'N'
				Ball.centery -= screen_size[1]//100+5
		else:	
			if Table.colliderect(Ball):#触碰板
				YS = -YS
				TT = 'Y'
				PT = time.time()
				
		if TT == 'N':#运动模块
		
			for n in range (0,len(rect)):#触碰方块
				Drect = rect[n]
				if Drect.colliderect(Ball):
					BCX = Ball.centerx
					BCY = Ball.centery
					DCX = Drect.centerx
					DCY = Drect.centery
					
					U = (DCY-BCY)*Drect.width
					D = (BCY-DCY)*Drect.width
					L = (DCX-BCX)*Drect.height
					R = (BCX-DCX)*Drect.height
					H = sorted([U,D,L,R])[3]
					#Clip = Drect.clip(Ball)
					#RU = Rect(Drect.left,Drect.top,Drect.width,Drect.height//2)
					#RL = Rect(Drect.left,Drect.top,Drect.width//2,Drect.height)
					#RR = Rect((Drect.left+Drect.right)//2,Drect.top,Drect.width//2+1,Drect.height)
					#RB = Rect(Drect.left,(Drect.top+Drect.bottom)//2,Drect.width,Drect.height//2+1)
					#if RU.contains(Clip) and Ball.centery > Drect.centery:	
					#	YS = -YS
					#if RL.contains(Clip) and Ball.centerx < Drect.centerx:
					#	XS = -XS
					#if RR.contains(Clip) and Ball.centerx > Drect.centerx:
					#	XS = -XS
					#if RB.contains(Clip) and Ball.centery < Drect.centery:
					#	YS = -YS
					if H==U:#上
						YS = -YS
					if H==D:#下
						YS = -YS
					if H==L:#左
						XS = -XS
					if H==R:#右
						XS = -XS
					rect.pop(n)
					break
					
			if Ball.right >= screen_size[0]:#触碰右边
				XS = -XS
			if Ball.left <= 0:#触碰左边
				XS = -XS
			if Ball.top <= 0:#触碰上面
				YS = -YS
			if Ball.bottom >= screen_size[1]:#触碰下面（输）
				screen.fill((0,0,0,0))
				pygame.mixer.music.fadeout(1000)
				while True:
					if lostsound.get_num_channels() == 0:
						lostsound.play()
					for event in pygame.event.get():
						if event.type == QUIT:#退出事件
							exit()
						if event.type == KEYDOWN:#按键事件
							exit_flag = True
					screen.blit(lost_surface,(screen_size[0]//2-lost_surface.get_width()//2,screen_size[1]//2-lost_surface.get_height()//2))
					if exit_flag:
						break
					pygame.display.update()
			
		
		if TT == 'N':
			Ball.center = (Ball.centerx + XS,Ball.centery + YS)
		
	
		#绘图
		screen.fill((0,0,0))#填充黑色
		for Drect in rect:#画方块
			pygame.draw.rect(screen,(255,255,255),Drect)
		pygame.draw.rect(screen,(255,255,255),Table)#画板
		pygame.draw.rect(screen,(255,255,255),Ball)#画球
		
		if len(rect) == 0:#赢
			screen.fill((0,0,0))
			pygame.mixer.music.fadeout(1000)
			while True:
				if winsound.get_num_channels() == 0:
					winsound.play()
				for event in pygame.event.get():
					if event.type == QUIT:#退出事件
						exit()
					if event.type == KEYDOWN:#按键事件
						exit_flag = True
				screen.blit(win_surface,(screen_size[0]//2-win_surface.get_width()//2,screen_size[1]//2-win_surface.get_height()//2))
				if exit_flag:
					break
				pygame.display.update()
		
		pygame.display.update()#刷新
		
		
	
	play = ''#初始化play数据
	while not(play == 'Y' or play == 'N' or play == 'y' or play == 'n'):#还想再玩吗
		play = 'Y' #input("Do you want to play again?(default=Y)(Y or N)\n")
		if play == '':
			play = 'Y'
		if play == 'N':
			exit()
		elif play == 'Y':
			reset = ''#初始化reset数据
			while not(reset == 'Y' or reset == 'N' or reset == 'y' or reset == 'n'):#要重设设定吗
				reset = input("Do you want to reset your setting?(default=N)(Y or N)\n")
				if reset == '':
					reset = 'N'
