import random as ra
import turtle as tu
import itertools as tool
import time as ti
import math as m

tu.Screen().tracer(0) 
tu.hideturtle()
tu.up()
tu.Screen().setup(1920,1080)

class Dices():

	def __init__(self, end_coord):
		self.end_coord = end_coord

	def draw_circle(self, circle_center_position_x, circle_center_position_y, radius):
		tu.goto(circle_center_position_x, circle_center_position_y-radius)
		tu.begin_fill()
		tu.seth(0)
		tu.circle(radius)
		tu.end_fill()

	def first_point(self, dice_corner_position_x, dice_corner_position_y, rotation):
			tu.up()
			tu.goto(dice_corner_position_x, dice_corner_position_y)
			tu.seth(rotation+45)
			tu.forward(20*m.sqrt(2))
	
	def forward_point(y):
		for i in range(y-1):
			tu.forward(80)
			tu.seth(tu.heading+90)

	def draw_dice(self, dice_corner_position_x,dice_corner_position_y,size, rotation, number_rolled,y):
		tu.up()
		tu.goto(dice_corner_position_x, dice_corner_position_y)
		tu.down()
		for i in range(4):
			tu.down()
			tu.seth(90*i+rotation)
			tu.forward(size)
			tu.up()
		if number_rolled in [1,3,5]:
			tu.seth(rotation+45)
			tu.forward(60*m.sqrt(2))
			self.draw_circle(tu.xcor(), tu.ycor(), 15)
		if number_rolled >= 2:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation)
			tu.seth(rotation)
			tu.forward(80)
			self.draw_circle(tu.xcor(), tu.ycor(), 15)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation)
			tu.seth(rotation+90)
			tu.forward(80)
			self.draw_circle(tu.xcor(), tu.ycor(), 15)
		if number_rolled >= 4:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation)
			self.draw_circle(tu.xcor(), tu.ycor(), 15)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation)
			tu.seth(rotation+45)
			tu.forward(80*m.sqrt(2))
			self.draw_circle(tu.xcor(), tu.ycor(), 15)
		if number_rolled >= 6:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation)
			tu.seth(rotation)
			tu.forward(40)
			self.draw_circle(tu.xcor(), tu.ycor(), 15)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation)
			tu.seth(rotation)
			tu.forward(40)
			tu.seth(rotation+90)
			tu.forward(80)
			self.draw_circle(tu.xcor(), tu.ycor(), 15)

def generate_dice():
	d1 = Dices((0,0))
	for i in range(1080):
		tu.clear()
		d1.draw_dice(-840, 540-i, 120, 90, number_rolled)
		tu.Screen().update()
		ti.sleep(0.001)
	for y,i,teta in tool.product(range(4),range(4),range(91)):
		tu.clear()
		d1.draw_dice(-840+i*120, -540, 120, 90-teta, number_rolled,y)
		ti.sleep(0.005)
		tu.Screen().update() 
for i in range(10):
	number_rolled = ra.randint(1,6)
	number_rolled = 6
	generate_dice()
d1 = Dices((0,0))
d1.draw_dice(0, 0, 120, 90, 6)

tu.Screen().update() 
ti.sleep(5)
exit()