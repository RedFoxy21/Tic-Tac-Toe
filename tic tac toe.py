import tkinter
self = tkinter.Tk()
self.title('Tic Tac Toe')
canvas = tkinter.Canvas()
canvas.pack()

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0

def left_click(self):
    xL = self.x
    yL = self.y
    if xL in range(50, 100) and yL in range(50, 100) and x1 == 0: 
        canvas.create_text(75, 75, text = 'X')
        def glob1():
            global x1
            x1 = x1 + 1
        glob1()
    elif xL in range(100, 150) and yL in range(50, 100) and x2 == 0: 
        canvas.create_text(125, 75, text = 'X')
        def glob2():
            global x2
            x2 = x2 + 1
        glob2()
    elif xL in range(150, 200) and yL in range(50, 100) and x3 == 0: 
        canvas.create_text(175, 75, text = 'X')
        def glob3():
            global x3
            x3 = x3 + 1
        glob3()
    elif xL in range(50, 100) and yL in range(100, 150) and x4 == 0: 
        canvas.create_text(75, 125, text = 'X')
        def glob4():
            global x4
            x4 = x4 + 1
        glob4()
    elif xL in range(100, 150) and yL in range(100, 150) and x5 == 0: 
        canvas.create_text(125, 125, text = 'X')
        def glob5():
            global x5
            x5 = x5 + 1
        glob5()
    elif xL in range(150, 200) and yL in range(100, 150) and x6 == 0: 
        canvas.create_text(175, 125, text = 'X')
        def glob6():
            global x6
            x6 = x6 + 1
        glob6()
    elif xL in range(50, 100) and yL in range(150, 200) and x7 == 0: 
        canvas.create_text(75, 175, text = 'X')
        def glob7():
            global x7
            x7 = x7 + 1
        glob7()
    elif xL in range(100, 150) and yL in range(150, 200) and x8 == 0: 
        canvas.create_text(125, 175, text = 'X')
        def glob8():
            global x8
            x8 = x8 + 1
        glob8()
    elif xL in range(150, 200) and yL in range(150, 200) and x9 == 0: 
        canvas.create_text(175, 175, text = 'X')
        def glob9():
            global x9
            x9 = x9 + 1
        glob9()
    else:
        print('Click outside the grid // Double-input')

def right_click(self):
    xr = self.x
    yr = self.y
    if xr in range(50, 100) and yr in range(50, 100) and x1 == 0: 
        canvas.create_text(75, 75, text = 'O')
        def glob1():
            global x1
            x1 = x1 + 1
        glob1()
    elif xr in range(100, 150) and yr in range(50, 100) and x2 == 0: 
        canvas.create_text(125, 75, text = 'O')
        def glob2():
            global x2
            x2 = x2 + 1
        glob2()
    elif xr in range(150, 200) and yr in range(50, 100) and x3 == 0:
        canvas.create_text(175, 75, text = 'O')
        def glob3():
            global x3
            x3 = x3 + 1
        glob3()
    elif xr in range(50, 100) and yr in range(100, 150) and x4 == 0: 
        canvas.create_text(75, 125, text = 'O')
        def glob4():
            global x4
            x4 = x4 + 1
        glob4()
    elif xr in range(100, 150) and yr in range(100, 150) and x5 == 0: 
        canvas.create_text(125, 125, text = 'O')
        def glob5():
            global x5
            x5 = x5 + 1
        glob5()
    elif xr in range(150, 200) and yr in range(100, 150) and x6 == 0: 
        canvas.create_text(175, 125, text = 'O')
        def glob6():
            global x6
            x6 = x6 + 1
        glob6()
    elif xr in range(50, 100) and yr in range(150, 200) and x7 == 0: 
        canvas.create_text(75, 175, text = 'O')
        def glob7():
            global x7
            x7 = x7 + 1
        glob7()
    elif xr in range(100, 150) and yr in range(150, 200) and x8 == 0: 
        canvas.create_text(125, 175, text = 'O')
        def glob8():
            global x8
            x8 = x8 + 1
        glob8()
    elif xr in range(150, 200) and yr in range(150, 200) and x9 == 0: 
        canvas.create_text(175, 175, text = 'O')
        def glob9():
            global x9
            x9 = x9 + 1
        glob9()
    else:
        print('Click outside the grid // Double-input')
   
def grid():
    r1 = canvas.create_rectangle(50,50,100,100)
    r2 = canvas.create_rectangle(100,50,150,100) 
    r3 = canvas.create_rectangle(150,50,200,100) 
    r4 = canvas.create_rectangle(50,100,100,150) 
    r5 = canvas.create_rectangle(100,100,150,150) 
    r6 = canvas.create_rectangle(150,100,200,150) 
    r7 = canvas.create_rectangle(50,150,100,200) 
    r8 = canvas.create_rectangle(100,150,150,200) 
    r9 = canvas.create_rectangle(150,150,200,200) 

grid()

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)
