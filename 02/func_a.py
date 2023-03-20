import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

#DRY: Don't Repeat yourself

def square(length):

	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(90)


for i in range(500):
	square(200)
	my_turtle.right(11)



turtle.done()


# print(list(range(100)))

# for i in range(100):
# 	print("hello")