#Alien Ambush Game developed using Python (Pygame)
#Author - Total Raghavender
#RollNumber - CED16I042
#Course - Interactive Computer Graphics

#Import Libraries
import sys
import pygame
import random
import math
import time

from pygame import mixer

#Initialize Pygame
pygame.init()

#Open Highscore File
file = open("High_Score.txt","r")
HS_String = file.read()
HS = int(HS_String)
file.close()

#Screen Setup
screen = pygame.display.set_mode((1200,1000))
pygame.display.set_caption("Alien Ambush")

#Spacecraft 
Spacecraft_Image = pygame.image.load('spacecraft.png')
Spacecraft_Image = pygame.transform.scale(Spacecraft_Image,(64,64))
Spacecraft_x = 568
Spacecraft_y = 900
Spacecraft_Velocity = 0

#Alien_1
Alien1_Image = pygame.image.load('alien1.png')
Alien1_Image = pygame.transform.scale(Alien1_Image,(32,32))
Alien1_x = random.randint(0,1168)
Alien1_y = random.randint(500,600)
Alien1_Velocity = 2

#Alien_2
Alien2_Image = pygame.image.load('alien2.png')
Alien2_Image = pygame.transform.scale(Alien2_Image,(64,64))
Alien2_x = random.randint(0,1136)
Alien2_y = random.randint(350,400)
Alien2_Velocity = 3.5
Alien2_Health = 2
Level_2 = "False"

#Alien_3
Alien3_Image = pygame.image.load('alien3.png')
Alien3_Image = pygame.transform.scale(Alien3_Image,(128,128))
Alien3_x = random.randint(0,1072)
Alien3_y = random.randint(150,200)
Alien3_Velocity = 5
Alien3_Health = 3
Level_3 = "False"

#Bullet
Bullet_Image = pygame.image.load('bullet.png')
Bullet_Image = pygame.transform.scale(Bullet_Image,(32,32))
Bullet_x = 0
Bullet_y = 890
Bullet_Velocity = 13
Bullet_State = "READY"

#Background Picture
Background = pygame.image.load('background_image.jpg')

#Background Music
mixer.music.load('background_music.mp3')
mixer.music.play(-1)

#Scoring System
Score = 0
Total = 0
Aliens_Killed = 0

#Timer System
Milli_Seconds_Units = 0
Milli_Seconds_Tens = 0
Milli_Seconds_Hundreds = 0
Seconds_Units = 0
Seconds_Tens = 0
Minutes_Units = 0
Minutes_Tens = 0
clock = pygame.time.Clock()
Flag = True

#Score Text
font = pygame.font.SysFont("Purisa",40)
font_1 = pygame.font.SysFont("Purisa",40)
text_w = 20
text_x = 20
text_y = 20
text_z = 80

#Timer Text
time_text = pygame.font.SysFont("Purisa",40)
time_1_text = pygame.font.SysFont("Purisa",25)
text_l = 900
text_m = 20

#Game Over Text
game_over_text_1 = pygame.font.SysFont("Purisa",70)
game_over_text_2 = pygame.font.SysFont("Purisa",50)
game_over_text_3 = pygame.font.SysFont("Purisa",25)
text_a = 125
text_b = 400
text_c = 395
text_d = 550
text_e = 800
text_f = 950

#Start Screen Text
start_screen_text_1 = pygame.font.SysFont("Purisa",60)
start_screen_text_2 = pygame.font.SysFont("Purisa",20)
start_screen_text_3 = pygame.font.SysFont("Purisa",18)
start_screen_text_4 = pygame.font.SysFont("Purisa",18)
start_screen_text_5 = pygame.font.SysFont("Purisa",18)
start_screen_text_6 = pygame.font.SysFont("Purisa",18)
start_screen_text_7 = pygame.font.SysFont("Purisa",18)
start_screen_text_8 = pygame.font.SysFont("Purisa",18)
start_screen_text_9 = pygame.font.SysFont("Purisa",18)
start_screen_text_10 = pygame.font.SysFont("Purisa",18)
start_screen_text_11 = pygame.font.SysFont("Purisa",18)
start_screen_text_12 = pygame.font.SysFont("Purisa",18)
start_screen_text_13 = pygame.font.SysFont("Purisa",18)
start_screen_text_14 = pygame.font.SysFont("Purisa",19)
start_screen_text_15 = pygame.font.SysFont("Purisa",22)
start_screen_text_16 = pygame.font.SysFont("Purisa",22)
start_screen_text_17 = pygame.font.SysFont("Purisa",22)
start_screen_text_18 = pygame.font.SysFont("Purisa",22)
start_screen_text_19 = pygame.font.SysFont("Purisa",23)
start_screen_text_20 = pygame.font.SysFont("Purisa",25)

#Exit Screen Text
exit_screen_text_1 = pygame.font.SysFont("Purisa",70)
exit_screen_text_2 = pygame.font.SysFont("Purisa",60)
exit_screen_text_3 = pygame.font.SysFont("Purisa",40)
exit_screen_text_4 = pygame.font.SysFont("Purisa",30)
exit_screen_text_5 = pygame.font.SysFont("Purisa",25)

#Text Colour
White = (255,255,255)

#Display Score Function
def Kills(x,y,a,b):
	kills = font.render("ALIENS KILLED : " + str(Aliens_Killed),True,White)
	screen.blit(kills,(x,y))
	best_kills = font_1.render("HIGH SCORE : " + str(HS),True,White)
	screen.blit(best_kills,(a,b))

#Display Timer Function
def Timer(x,y):
	time = time_text.render("Time : " + str(Minutes_Tens) + str(Minutes_Units) + ":" + str(Seconds_Tens) + str(Seconds_Units) ,True,White)
	screen.blit(time,(x,y))

#Display Game Over Funtion
def Game_Over(x,y,a,b,c,d):
	g_text_1 = game_over_text_1.render("GAME OVER",True,White)
	screen.blit(g_text_1,(a,b))
	g_text_2 = game_over_text_2.render("Earth just lost her best defender",True,White)
	screen.blit(g_text_2,(x,y))
	g_text_3 = game_over_text_3.render("Press Esc to Quit the Game",True,White)
	screen.blit(g_text_3,(c,d))

	#Keyboard Input
	if event.type == pygame.KEYDOWN: 	#KEY is Pressed 
		if event.key == pygame.K_ESCAPE:
			pygame.quit()

#Spacecraft Function
def Spacecraft(x,y):
	screen.blit(Spacecraft_Image,(x,y))

#Alien_1 Function
def Alien_1(x,y):
	screen.blit(Alien1_Image,(x,y))

#Alien_2 Function
def Alien_2(x,y):
	screen.blit(Alien2_Image,(x,y))

#Alien_3 Function
def Alien_3(x,y):
	screen.blit(Alien3_Image,(x,y))

#Shoot Bullet Function
def Shoot(x,y):
	global Bullet_State
	Bullet_State = "FIRE"
	screen.blit(Bullet_Image,(x+16,y+10))

#Alien_1 Collison Detection Function
def Collision_1(Alien1_x,Alien1_y,Bullet_x,Bullet_y):
	#Distance calculation between bullet and enemy using algebra
	a = math.pow(Alien1_x-Bullet_x,2)
	b = math.pow(Alien1_y-Bullet_y,2)
	s = a+b
	distance = math.sqrt(s)

	if distance < 30:
		return True

#Alien_2 Collison Detection Function
def Collision_2(Alien2_x,Alien2_y,Bullet_x,Bullet_y):
	#Distance calculation between bullet and enemy using algebra
	a = math.pow(Alien2_x-Bullet_x,2)
	b = math.pow(Alien2_y-Bullet_y,2)
	s = a+b
	distance = math.sqrt(s)

	if distance < 50:
		return True

#Alien_3 Collison Detection Function
def Collision_3(Alien3_x,Alien3_y,Bullet_x,Bullet_y):
	#Distance calculation between bullet and enemy using algebra
	a = math.pow(Alien3_x-Bullet_x,2)
	b = math.pow(Alien3_y-Bullet_y,2)
	s = a+b
	distance = math.sqrt(s)

	if distance < 70:
		return True

#Display Introduction & Rules Function
def Intro_Rules():
	s_text_1 = start_screen_text_1.render("ALIEN AMBUSH",True,White)
	screen.blit(s_text_1,(360,20))
	s_text_2 = start_screen_text_2.render("65 Million Years ago, the arrival of the First race of Aliens on Earth resulted in a Mass Extinction.",True,White)
	screen.blit(s_text_2,(5,140))
	s_text_3 = start_screen_text_3.render("30 Million Years later, the Second race of Aliens arrived on Earth. They were stronger than the First Race.",True,White)
	screen.blit(s_text_3,(5,180))
	s_text_4 = start_screen_text_4.render("About 25 Million Years later, the Third race of Aliens arrived on Earth. They were the strongest Alien Race.",True,White)
	screen.blit(s_text_4,(5,220))
	s_text_5 = start_screen_text_5.render("The 3 Alien Races decided to split the Earth into 3 parts & live seperately rather than warring over Territory.",True,White)
	screen.blit(s_text_5,(5,260))
	s_text_6 = start_screen_text_6.render("Wherever they went, they ensured that only their species thrived. This way they ruled for around 10 Million Years.",True,White)
	screen.blit(s_text_6,(5,300))
	s_text_7 = start_screen_text_7.render("About 200,000 Years back, A new species evolved on Earth. It was unlike anything the Aliens had seen.",True,White)
	screen.blit(s_text_7,(5,340))
	s_text_8 = start_screen_text_8.render("This New species developed at a rapid rate and showed signs of Intelligence. They quickly increased in number.",True,White)
	screen.blit(s_text_8,(5,380))
	s_text_9 = start_screen_text_9.render("They soon started developing weapons to defend themselves and Fight back. They started to show Resistance.",True,White)
	screen.blit(s_text_9,(5,420))
	s_text_10 = start_screen_text_10.render("The Aliens made the mistake of underestimating the abilities of this species. Soon they got together & attacked.",True,White)
	screen.blit(s_text_10,(5,460))
	s_text_11 = start_screen_text_11.render("Systematically they started eliminating all the 3 Races of Aliens. The Aliens realized that fighting back was impossible.",True,White)
	screen.blit(s_text_11,(5,500))
	s_text_12 = start_screen_text_12.render("The Aliens left Earth but swore revenge on this new species which almost exterminated them.",True,White)
	screen.blit(s_text_12,(5,540))
	s_text_13 = start_screen_text_13.render("They promised to Return & Reclaim what belonged to them.",True,White)
	screen.blit(s_text_13,(5,580))
	s_text_14 = start_screen_text_14.render("The YEAR is 2019. The Earth is under Attack from The 3 Alien Races. It is your duty to defend Earth.",True,White)
	screen.blit(s_text_14,(5,650))
	s_text_15 = start_screen_text_15.render("The Small Aliens require one bullet to be killed.",True,White)
	screen.blit(s_text_15,(300,710))
	s_text_16 = start_screen_text_16.render("The Medium Aliens require two bullets to be killed.",True,White)
	screen.blit(s_text_16,(290,740))
	s_text_17 = start_screen_text_17.render("The Big Aliens require three bullets to be killed.",True,White)
	screen.blit(s_text_17,(300,770))
	s_text_18 = start_screen_text_18.render("If any of the Big Aliens get too close, WE DIE.",True,White)
	screen.blit(s_text_18,(300,830))
	s_text_19 = start_screen_text_19.render("Use LEFT & RIGHT arrow keys to move. Use SPACE to Shoot.",True,White)
	screen.blit(s_text_19,(200,890))
	s_text_20 = start_screen_text_20.render("Press Enter to Begin the Game",True,White)
	screen.blit(s_text_20,(760,955))

#Display Start Screen Function
def Start_Screen():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
			#Keyboard Input
			if event.type == pygame.KEYDOWN: 	#KEY is Pressed 
				if event.key == pygame.K_RETURN:
					intro = False
			screen.fill((0,0,0))
			screen.blit(Background,(0,0))
			Intro_Rules()
			pygame.display.update()

#Display Exit Screen Funtion
def Exit_Screen():
	e_text_1 = exit_screen_text_1.render("GAME OVER",True,White)
	screen.blit(e_text_1,(395,200))
	e_text_2 = exit_screen_text_2.render("CONGRATULATIONS",True,White)
	screen.blit(e_text_2,(280,350))
	e_text_3 = exit_screen_text_3.render("You have successfully defended the Earth.",True,White)
	screen.blit(e_text_3,(125,650))
	e_text_4 = exit_screen_text_4.render("The Aliens will Return.",True,White)
	screen.blit(e_text_4,(410,760))
	e_text_5 = exit_screen_text_5.render("Press Esc to Quit the Game",True,White)
	screen.blit(e_text_5,(800,950))

	#Keyboard Input
	if event.type == pygame.KEYDOWN: 	#KEY is Pressed 
		if event.key == pygame.K_ESCAPE:
			pygame.quit()

Start_Screen()
#Infinite Loop 

running = True
while running:

	#Make Background
	screen.fill((0,0,0))

	#Draw Background Image
	screen.blit(Background,(0,0))

	#Set FPS
	clock.tick(60)
	
	#CountUP Timer 
	if Milli_Seconds_Units < 9:
		if Milli_Seconds_Tens < 9:
			Milli_Seconds_Units += 1
	if Milli_Seconds_Units == 9 and Milli_Seconds_Tens < 9:
		Milli_Seconds_Units = 0
		Milli_Seconds_Tens += 1
	elif Milli_Seconds_Tens == 9 and Milli_Seconds_Hundreds < 1:
		Milli_Seconds_Tens = 0
		Milli_Seconds_Hundreds += 1

	if Milli_Seconds_Hundreds == 1:	
		if Seconds_Units < 9:
			Seconds_Units += 1
			Milli_Seconds_Hundreds = 0
		else:
			Seconds_Units = 0
			Seconds_Tens += 1
			Milli_Seconds_Hundreds = 0

	if Seconds_Tens == 6:	
		if Minutes_Units < 9:
			Minutes_Units += 1
			Seconds_Tens = 0
		else:
			Minutes_Units = 0
			Minutes_Tens += 1
			Seconds_Tens = 0

	if Minutes_Tens == 6:	
		Seconds_Unit = 0
		Seconds_Tens = 0
		Minutes_Units = 0
		Minutes_Tens = 0

	if Flag:
		Timer(text_l,text_m)	
							
	#If Red Cross Button is pressed, Close the window
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#Keyboard Input
		if event.type == pygame.KEYDOWN: 	#KEY is Pressed 
			if event.key == pygame.K_LEFT:
				Spacecraft_Velocity = -7
			if event.key == pygame.K_RIGHT:
				Spacecraft_Velocity = 7
			if event.key == pygame.K_SPACE :
				if Bullet_State is "READY":	
					Bullet_x = Spacecraft_x	
					Shoot(Bullet_x,Bullet_y)

		if event.type == pygame.KEYUP:		#KEY is Let Go
			if event.key == pygame.K_LEFT:
				Spacecraft_Velocity = 0
			if event.key == pygame.K_RIGHT:	
				Spacecraft_Velocity = 0

	#Move Alien_1
	Alien1_x += Alien1_Velocity
	if Alien1_x <= 0:
		Alien1_Velocity = 2
	elif Alien1_x >= 1168:
		Alien1_Velocity = -2

	#Move Spacecraft
	Spacecraft_x += Spacecraft_Velocity
	if Spacecraft_x <= 0:
		Spacecraft_x = 0
	elif Spacecraft_x >= 1136:
		Spacecraft_x = 1136

	#Move Bullet
	if Bullet_y <= 0:
		Bullet_y = 900
		Bullet_State = "READY"
	if Bullet_State is "FIRE":
		Shoot(Bullet_x,Bullet_y)
		Bullet_y -= Bullet_Velocity

	#Alien_1 Collision
	collision_1 = Collision_1(Alien1_x,Alien1_y,Bullet_x,Bullet_y)
	if collision_1:
		Bullet_y = 890
		Bullet_State = "READY"
		Score += 1
		Total += 1
		Aliens_Killed += 1
		Alien1_x = random.randint(0,1166)
		Alien1_y = random.randint(500,600)

	#Alien_2 Draw, Move & Collision
	if Score >= 1:
		Alien1_x = 1800
		Alien1_y = 1800
		Level_2 = "True"
	
	if Level_2 == "True":
		Alien_2(Alien2_x,Alien2_y)
		Alien2_x += Alien2_Velocity

		if Alien2_x <= 0:
			Alien2_Velocity = 3.5
			Alien2_y -= 100

		elif Alien2_x >= 1136:
			Alien2_Velocity = -3.5
			Alien2_y += 100
						
		collision_2 = Collision_2(Alien2_x,Alien2_y,Bullet_x,Bullet_y)
		if collision_2:
			Bullet_y = 890
			Alien2_Health -= 1
			Bullet_State = "READY"
			Score += 1			

			if Alien2_Health == 0:	
				Total += 1
				Aliens_Killed += 1			
				Alien2_Health = 2
				Alien2_x = random.randint(0,1136)
				Alien2_y = random.randint(350,400)

	#Alien_3 Draw, Move & Collision
	if Total >= 2:
		Alien2_x = 1800
		Alien2_y = 1800
		Level_3 = "True"
	
	if Level_3 == "True":
		Alien_3(Alien3_x,Alien3_y)
		Alien3_x += Alien3_Velocity

		if Alien3_y > 650:
			Spacecraft_x = 1800
			Spacecraft_y = 1800
			Alien1_x = 1800
			Alien1_y = 1800
			Alien2_x = 1800
			Alien2_y = 1800
			Alien3_x = 1800
			Alien3_y = 1800
			Flag = False
			Game_Over(text_a,text_b,text_c,text_d,text_e,text_f)

		if Alien3_x <= 0:
			Alien3_Velocity = 5
			Alien3_y += 50
		elif Alien3_x >= 1072:
			Alien3_Velocity = -5
			Alien3_y += 50

		collision_3 = Collision_3(Alien3_x,Alien3_y,Bullet_x,Bullet_y)
		if collision_3:
			Bullet_y = 890
			Alien3_Health -= 1
			Bullet_State = "READY"
			Score += 1			

			if Alien3_Health == 0:	
				Total += 1
				Aliens_Killed += 1		
				Alien3_Health = 3
				Alien3_x = random.randint(0,1072)
				Alien3_y = random.randint(150,200)

	#Quit After Killing 15 Aliens
	if Aliens_Killed == 3:
		Spacecraft_x = 1800
		Spacecraft_y = 1800
		Alien1_x = 1800
		Alien1_y = 1800
		Alien2_x = 1800
		Alien2_y = 1800
		Alien3_x = 1800
		Alien3_y = 100
		Flag = False
		Exit_Screen()

	#Update Highscore File
	if(Aliens_Killed > HS):
		file = open("High_Score.txt","w")
		file.write(str(Aliens_Killed))	
		
	#Call Functions to Draw
	Spacecraft(Spacecraft_x,Spacecraft_y)
	Alien_1(Alien1_x,Alien1_y)
	Kills(text_w,text_x,text_y,text_z)
	pygame.display.update()

pygame.quit()
#End of Infinite Loop
