import tkinter as tk
root = tk.Tk()
root.title('Piškvarky')
canvas = tk.Canvas(width=700, height=350)
canvas.pack()

x1 = 0; x2 = 0; x3 = 0; x4 = 0; x5 = 0; x6 = 0; x7 = 0; x8 = 0; x9 = 0; x10 = 0
x11 = 0; x12 = 0; x13 = 0; x14 = 0; x15 = 0; x16 = 0; x17 = 0; x18 = 0; x19 = 0; x20 = 0
x21 = 0; x22 = 0; x23 = 0; x24 = 0; x25 = 0


def left_click(self):
    xL = self.x
    yL = self.y
    if xL in range(50, 100) and yL in range(50, 100) and x1 == 0:
        canvas.create_text(75, 75, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f1():
            global x1
            x1 = x1 + 1
        f1()
    elif xL in range(100, 150) and yL in range(50, 100) and x2 == 0: 
        canvas.create_text(125, 75, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f2():
            global x2
            x2 = x2 + 1
        f2()
    elif xL in range(150, 200) and yL in range(50, 100) and x3 == 0: 
        canvas.create_text(175, 75, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f3():
            global x3
            x3 = x3 + 1
        f3()
    elif xL in range(200, 250) and yL in range(50, 100) and x4 == 0: 
        canvas.create_text(225, 75, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f4():
            global x4
            x4 = x4 + 1
        f4()
    elif xL in range(250, 300) and yL in range(50, 100) and x5 == 0: 
        canvas.create_text(275, 75, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f5():
            global x5
            x5 = x5 + 1
        f5()
    elif xL in range(50, 100) and yL in range(100, 150) and x6 == 0: 
        canvas.create_text(75, 125, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f6():
            global x6
            x6 = x6 + 1
        f6()
    elif xL in range(100, 150) and yL in range(100, 150) and x7 == 0: 
        canvas.create_text(125, 125, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f7():
            global x7
            x7 = x7 + 1
        f7()
    elif xL in range(150, 200) and yL in range(100, 150) and x8 == 0: 
        canvas.create_text(175, 125, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f8():
            global x8
            x8 = x8 + 1
        f8()
    elif xL in range(200, 250) and yL in range(100, 150) and x9 == 0: 
        canvas.create_text(225, 125, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f9():
            global x9
            x9 = x9 + 1
        f9()
    elif xL in range(250, 300) and yL in range(100, 150) and x10 == 0: 
        canvas.create_text(275, 125, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f10():
            global x10
            x10 = x10 + 1
        f10()
    elif xL in range(50, 100) and yL in range(150, 200) and x11 == 0: 
        canvas.create_text(75, 175, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f11():
            global x11
            x11 = x11 + 1
        f11()
    elif xL in range(100, 150) and yL in range(150, 200) and x12 == 0: 
        canvas.create_text(125, 175, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f12():
            global x12
            x12 = x12 + 1
        f12()
    elif xL in range(150, 200) and yL in range(150, 200) and x13 == 0: 
        canvas.create_text(175, 175, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f13():
            global x13
            x13 = x13 + 1
        f13()
    elif xL in range(200, 250) and yL in range(150, 200) and x14 == 0: 
        canvas.create_text(225, 175, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f14():
            global x14
            x14 = x14 + 1
        f14()
    elif xL in range(250, 300) and yL in range(150, 200) and x15 == 0: 
        canvas.create_text(275, 175, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f15():
            global x15
            x15 = x15 + 1
        f15()
    elif xL in range(50, 100) and yL in range(200, 250) and x16 == 0: 
        canvas.create_text(75, 225, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f16():
            global x16
            x16 = x16 + 1
        f16()
    elif xL in range(100, 150) and yL in range(200, 250) and x17 == 0: 
        canvas.create_text(125, 225, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f17():
            global x17
            x17 = x17 + 1
        f17()
    elif xL in range(150, 200) and yL in range(200, 250) and x18 == 0: 
        canvas.create_text(175, 225, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f18():
            global x18
            x18 = x18 + 1
        f18()
    elif xL in range(200, 250) and yL in range(200, 250) and x19 == 0: 
        canvas.create_text(225, 225, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f19():
            global x19
            x19 = x19 + 1
        f19()
    elif xL in range(250, 300) and yL in range(200, 250) and x20 == 0: 
        canvas.create_text(275, 225, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f20():
            global x20
            x20 = x20 + 1
        f20()
    elif xL in range(50, 100) and yL in range(250, 300) and x21 == 0: 
        canvas.create_text(75, 275, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f21():
            global x21
            x21 = x21 + 1
        f21()
    elif xL in range(100, 150) and yL in range(250, 300) and x22 == 0: 
        canvas.create_text(125, 275, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f22():
            global x22
            x22 = x22 + 1
        f22()
    elif xL in range(150, 200) and yL in range(250, 300) and x23 == 0: 
        canvas.create_text(175, 275, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f23():
            global x23
            x23 = x23 + 1
        f23()
    elif xL in range(200, 250) and yL in range(250, 300) and x24 == 0: 
        canvas.create_text(225, 275, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f24():
            global x24
            x24 = x24 + 1
        f24()
    elif xL in range(250, 300) and yL in range(250, 300) and x25 == 0: 
        canvas.create_text(275, 275, tag="txt", text = 'X', font="Comic_Sans_MS 20")
        def f25():
            global x25
            x25 = x25 + 1
        f25()
    elif  x1==x2==x3==x4==x5==x6==x7==x8==x9==x10==x11==x12==x13==x14==x15==x16==x17==x18==x19==x20==x21==x22==x23==x24==x25==1:
        print("No... A ideme znova")
        clr()
    else:
        print('Klikmimo mriežku // dvojitý vstup')

def right_click(self):
    xr = self.x
    yr = self.y
    if xr in range(50, 100) and yr in range(50, 100) and x1 == 0: 
        canvas.create_text(75, 75, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f1():
            global x1
            x1 = x1 + 1
        f1()
    elif xr in range(100, 150) and yr in range(50, 100) and x2 == 0: 
        canvas.create_text(125, 75, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f2():
            global x2
            x2 = x2 + 1
        f2()
    elif xr in range(150, 200) and yr in range(50, 100) and x3 == 0: 
        canvas.create_text(175, 75, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f3():
            global x3
            x3 = x3 + 1
        f3()
    elif xr in range(200, 250) and yr in range(50, 100) and x4 == 0: 
        canvas.create_text(225, 75, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f4():
            global x4
            x4 = x4 + 1
        f4()
    elif xr in range(250, 300) and yr in range(50, 100) and x5 == 0: 
        canvas.create_text(275, 75, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f5():
            global x5
            x5 = x5 + 1
        f5()
    elif xr in range(50, 100) and yr in range(100, 150) and x6 == 0: 
        canvas.create_text(75, 125, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f6():
            global x6
            x6 = x6 + 1
        f6()
    elif xr in range(100, 150) and yr in range(100, 150) and x7 == 0: 
        canvas.create_text(125, 125, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f7():
            global x7
            x7 = x7 + 1
        f7()
    elif xr in range(150, 200) and yr in range(100, 150) and x8 == 0: 
        canvas.create_text(175, 125, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f8():
            global x8
            x8 = x8 + 1
        f8()
    elif xr in range(200, 250) and yr in range(100, 150) and x9 == 0: 
        canvas.create_text(225, 125, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f9():
            global x9
            x9 = x9 + 1
        f9()
    elif xr in range(250, 300) and yr in range(100, 150) and x10 == 0: 
        canvas.create_text(275, 125, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f10():
            global x10
            x10 = x10 + 1
        f10()
    elif xr in range(50, 100) and yr in range(150, 200) and x11 == 0: 
        canvas.create_text(75, 175, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f11():
            global x11
            x11 = x11 + 1
        f11()
    elif xr in range(100, 150) and yr in range(150, 200) and x12 == 0: 
        canvas.create_text(125, 175, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f12():
            global x12
            x12 = x12 + 1
        f12()
    elif xr in range(150, 200) and yr in range(150, 200) and x13 == 0: 
        canvas.create_text(175, 175, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f13():
            global x13
            x13 = x13 + 1
        f13()
    elif xr in range(200, 250) and yr in range(150, 200) and x14 == 0: 
        canvas.create_text(225, 175, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f14():
            global x14
            x14 = x14 + 1
        f14()
    elif xr in range(250, 300) and yr in range(150, 200) and x15 == 0: 
        canvas.create_text(275, 175, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f15():
            global x15
            x15 = x15 + 1
        f15()
    elif xr in range(50, 100) and yr in range(200, 250) and x16 == 0: 
        canvas.create_text(75, 225, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f16():
            global x16
            x16 = x16 + 1
        f16()
    elif xr in range(100, 150) and yr in range(200, 250) and x17 == 0: 
        canvas.create_text(125, 225, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f17():
            global x17
            x17 = x17 + 1
        f17()
    elif xr in range(150, 200) and yr in range(200, 250) and x18 == 0: 
        canvas.create_text(175, 225, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f18():
            global x18
            x18 = x18 + 1
        f18()
    elif xr in range(200, 250) and yr in range(200, 250) and x19 == 0: 
        canvas.create_text(225, 225, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f19():
            global x19
            x19 = x19 + 1
        f19()
    elif xr in range(250, 300) and yr in range(200, 250) and x20 == 0: 
        canvas.create_text(275, 225, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f20():
            global x20
            x20 = x20 + 1
        f20()
    elif xr in range(50, 100) and yr in range(250, 300) and x21 == 0: 
        canvas.create_text(75, 275, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f21():
            global x21
            x21 = x21 + 1
        f21()
    elif xr in range(100, 150) and yr in range(250, 300) and x22 == 0: 
        canvas.create_text(125, 275, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f22():
            global x22
            x22 = x22 + 1
        f22()
    elif xr in range(150, 200) and yr in range(250, 300) and x23 == 0: 
        canvas.create_text(175, 275, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f23():
            global x23
            x23 = x23 + 1
        f23()
    elif xr in range(200, 250) and yr in range(250, 300) and x24 == 0: 
        canvas.create_text(225, 275, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f24():
            global x24
            x24 = x24 + 1
        f24()
    elif xr in range(250, 300) and yr in range(250, 300) and x25 == 0: 
        canvas.create_text(275, 275, tag="txt", text = 'O', font="Comic_Sans_MS 20")
        def f25():
            global x25
            x25 = x25 + 1
        f25()
    elif  x1==x2==x3==x4==x5==x6==x7==x8==x9==x10==x11==x12==x13==x14==x15==x16==x17==x18==x19==x20==x21==x22==x23==x24==x25==1:
        print("No... A ideme znova")
        clr()
    else:
        print('Klikmimo mriežku // dvojitý vstup')

def clr():
    canvas.delete("txt")
    global x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25
    x1=x2=x3=x4=x5=x6=x7=x8=x9=x10=x11=x12=x13=x14=x15=x16=x17=x18=x19=x20=x21=x22=x23=x24=x25 = 0    

B = tk.Button(root, text = "Reset", command = clr)
B.configure(width = 8, height=1)
B.place(x=370, y=120)

Q = tk.Button(root, text = "Quit", command = root.quit)
Q.configure(width = 8, height=1)
Q.place(x=370, y=150)

   
def grid():
    for i in range(1,6):
        canvas.create_rectangle(i*50, 50, 50*(i+1), 100)
        canvas.create_rectangle(i*50, 100, 50*(i+1), 150)
        canvas.create_rectangle(i*50, 150, 50*(i+1), 200)
        canvas.create_rectangle(i*50, 200, 50*(i+1), 250)
        canvas.create_rectangle(i*50, 250, 50*(i+1), 300)

grid()

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)

root.mainloop()
