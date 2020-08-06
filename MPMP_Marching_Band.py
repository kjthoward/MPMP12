import tkinter as Tkinter
import tkinter.filedialog as tkFileDialog
import time
#used to draw grids
import turtle

#put number of "factors" (or marching band orientation combinations needed) here
target=10

#CHANGE THIS TO FALSE TO NOT SHOW PLOTS
#IF DOING TARGET>10 THIS SHOULD BE FALSE ELSE IT TAKES AGES!!!
plot=True

#Problem is just simple "how many factors are there"
def get_factors(n):
    factors=[]
    for i in range(1, n+1):
        if n % i == 0:
            factors+=[i]
    return factors

testing=1
while True:
    factors=get_factors(testing)
    if len(factors)==target:
        print("Total number of band members needed is: {}".format(testing))
        break
    else:
        testing+=1

print("Required layouts for band members are: ")
#create an array of factor pairs (first and last or factor array) to get layouts of the band
factor_pairs=[]
while factors!=[]:
    try:
        length=factors[0]
        width=factors.pop()
        factors.remove(length)
    #Except and if are to get around odd number length of array for odd targets
    except ValueError:
        width=length
    factor_pairs+=[[length,width]]
    print("{}x{}".format(length,width))
    if length!=width:
        print("{}x{}".format(width,length))

def square(side):
    bob.begin_fill()
    for i in range(4):
        bob.forward(side)
        bob.left(90)
    bob.end_fill()

def row(n, side):
    for i in range(n):
        square(side)
        bob.forward(side)
    bob.penup()
    bob.left(180)
    bob.forward(n * side)
    bob.left(180)
    bob.pendown()

def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
        bob.penup()
        bob.left(90)
        bob.forward(side)
        bob.right(90)
        bob.pendown()
    bob.penup()
    bob.right(90)
    bob.forward(m * side)
    bob.left(90)
    bob.pendown()
colour_count=0    
colours=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]


if plot==True:
    bob = turtle.Turtle()
    myWin=turtle.Screen()
    turtle.setworldcoordinates(-1, -1, target*5, target*5)
    bob.speed("fastest")

    for pair in factor_pairs:        
        bob.fillcolor(colours[colour_count])
        row_of_rows(pair[0],pair[1], 1)
        colour_count+=1
        bob.fillcolor(colours[colour_count])
        if pair[1]!=pair[0]:
            row_of_rows(pair[1],pair[0], 1)
            colour_count+=1
        
    
  

