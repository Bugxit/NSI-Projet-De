import random as ra
import turtle as tu
import itertools as tool
import time as ti
import math as m

tu.hideturtle()
tu.up()
tu.Screen().setup(1920,1080)

object_list = []

class Dices(tu.Turtle):

	def __init__(self, rolled_number, end_coord_x, end_coord_y):
		super().__init__(visible= False)  
		self.rolled_number = rolled_number
		self.end_coord_x = end_coord_x
		self.end_coord_y = end_coord_y

	tu.Screen().tracer(0)

	def draw_circle(self, circle_center_position_x, circle_center_position_y, radius):
		self.goto(circle_center_position_x, circle_center_position_y)
		self.dot(2*radius, 'red')

	def first_point(self, dice_corner_position_x, dice_corner_position_y, rotation, y):
			self.up()
			self.goto(dice_corner_position_x, dice_corner_position_y)
			for i in range(y):
				self.seth(rotation+i*90)
				self.forward(120)
			self.seth(rotation+y*90+45)
			self.forward(20*m.sqrt(2))

	def draw_dice(self, dice_corner_position_x,dice_corner_position_y,size, rotation,y):
		self.up()
		self.goto(dice_corner_position_x, dice_corner_position_y)
		self.down()
		self.clear()
		for i in range(4):
			self.down()
			self.seth(90*i+rotation)
			self.forward(size)
			self.up()
		if self.rolled_number in [1,3,5]:
			self.seth(rotation+45)
			self.forward(60*m.sqrt(2))
			self.draw_circle(self.xcor(), self.ycor(), 15)
		if self.rolled_number >= 2:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90*y)
			self.forward(80)
			self.draw_circle(self.xcor(), self.ycor(), 15)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90+90*y)
			self.forward(80)
			self.draw_circle(self.xcor(), self.ycor(), 15)
		if self.rolled_number >= 4:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.draw_circle(self.xcor(), self.ycor(), 15)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+45+90*y)
			self.forward(80*m.sqrt(2))
			self.draw_circle(self.xcor(), self.ycor(), 15)
		if self.rolled_number >= 6:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90*y)
			self.forward(40)
			self.draw_circle(self.xcor(), self.ycor(), 15)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90*y)
			self.forward(40)
			self.seth(rotation+90+90*y)
			self.forward(80)
			self.draw_circle(self.xcor(), self.ycor(), 15)
		tu.Screen().update()

def generate_dice(end_point, dice_value):
	object_list.append(Dices(ra.randint(1,6),end_point,0))
	for i in range(540):
		object_list[dice_value].draw_dice(-840, 540-2*i, 120, 90, 0)
		tu.Screen().update()
	for i,y,teta in tool.product(range(4),range(4),range(91)):
		if -840+(4*i+y)*120 < end_point:
			object_list[dice_value].draw_dice(-840+(4*i+y)*120, -540, 120, 90-teta, y)
		tu.Screen().update() 

for y,i in tool.product(range(9), range(16)):
	generate_dice(960-120*i, y*120)

tu.Screen().update() 
ti.sleep(5)
exit()