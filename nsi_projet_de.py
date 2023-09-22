import random as ra
import turtle as tu
import itertools as tool
import time as ti
import math as m

tu.hideturtle()
tu.Screen().setup(1920,1080)
canvas = tu.Screen().getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

object_list = []

class Dices(tu.Turtle):

	tu.Screen().tracer(0)

	def __init__(self, rolled_number, end_coord_x, end_coord_y):
		super().__init__(visible=False)  
		self.rolled_number = rolled_number
		self.end_coord_x = end_coord_x
		self.end_coord_y = end_coord_y

	def draw_circle(self, circle_center_position_x, circle_center_position_y, diameter):
		self.goto(circle_center_position_x, circle_center_position_y)
		self.dot(diameter, 'black')

	def first_point(self, dice_corner_position_x, dice_corner_position_y, rotation, y):
		self.up()
		self.goto(dice_corner_position_x, dice_corner_position_y)
		for i in range(y):
			self.seth(rotation+i*90)
			self.forward(120)
		self.seth(rotation+y*90+45)
		self.forward(20*m.sqrt(2))

	def Point_One_Three_Five(self, dice_corner_position_x,dice_corner_position_y,size, rotation,y):
		if self.rolled_number in [1,3,5]:
			self.seth(rotation+45)
			self.forward(60*m.sqrt(2))
			self.draw_circle(self.xcor(), self.ycor(), 30)
			
	def Point_two(self, dice_corner_position_x,dice_corner_position_y,size, rotation,y):
		if self.rolled_number >= 2:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90*y)
			self.forward(80)
			self.draw_circle(self.xcor(), self.ycor(), 30)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90+90*y)
			self.forward(80)
			self.draw_circle(self.xcor(), self.ycor(), 30)
			
	def Point_four(self, dice_corner_position_x,dice_corner_position_y,size, rotation,y):
		if self.rolled_number >= 4:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.draw_circle(self.xcor(), self.ycor(), 30)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+45+90*y)
			self.forward(80*m.sqrt(2))
			self.draw_circle(self.xcor(), self.ycor(), 30)
			
	def Point_six(self, dice_corner_position_x,dice_corner_position_y,size, rotation,y):
		if self.rolled_number >= 6:
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90*y)
			self.forward(40)
			self.draw_circle(self.xcor(), self.ycor(), 30)
			self.first_point(dice_corner_position_x, dice_corner_position_y, rotation, y)
			self.seth(rotation+90*y)
			self.forward(40)
			self.seth(rotation+90+90*y)
			self.forward(80)
			self.draw_circle(self.xcor(), self.ycor(), 30)
			
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
		self.Point_One_Three_Five(dice_corner_position_x,dice_corner_position_y,size, rotation,y)
		self.Point_two(dice_corner_position_x,dice_corner_position_y,size, rotation,y)
		self.Point_four(dice_corner_position_x,dice_corner_position_y,size, rotation,y)
		self.Point_six(dice_corner_position_x,dice_corner_position_y,size, rotation,y)
		tu.Screen().update()

def generate_dice(end_coord_x, end_coord_y, dice_value):
	object_list.append(Dices(ra.randint(1,6),end_coord_x,end_coord_y))
	for i in range(round(abs(540-end_coord_y)/2)):
		object_list[dice_value].draw_dice(-840, 540-2*i, 120, 90, 0)
		tu.Screen().update()
	for i,y,teta in tool.product(range(4),range(4),range(91)):
		if -840+(4*i+y)*120 < end_coord_x:
			object_list[dice_value].draw_dice(-840+(4*i+y)*120, end_coord_y, 120, 90-teta, y)
		tu.Screen().update() 

for y,i in tool.product(range(9), range(16)):
	generate_dice(960-120*i, y*120-540, 16*y+i)

tu.Screen().update() 
ti.sleep(5)
exit()