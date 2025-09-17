'''
5.	Напишите программу, которая отображает квадратное окно размером 600 на 600, полностью заполненное областью для рисования. 
По центру области должна отображаться окружность радиусом 200. Вдоль этой окружности по часовой стрелке должна двигаться точка. 
6.	Попробуйте изменить скорость и направление движения точки. Сделайте переменную, которая задает скорость и направление движения. 
'''
from tkinter import*
import math

window = Tk() #создает главное окно приложения
holst = Canvas(window, width = 600, height = 600, bg = 'white') #создает холст 600 на 600 
holst.pack() #размещает холст в окне

centr_x = 300
centr_y = 300
rad = 200
ball = holst.create_oval(centr_x - rad, centr_y - rad, centr_x + rad, centr_y + rad, fill = 'pink', outline = 'yellow') # окружность

nach_x = 100
nach_y = 300
rad_point = 5
point = holst.create_oval(nach_x - rad_point, nach_y - rad_point, nach_x + rad_point, nach_y + rad_point, fill = 'blue')

napravl = int(input('Введите "1", если хотите, чтобы точка двигалась по часовой стрелке, против часовой стрелки - "-1"')) # если 1, то по часовой стрелке, если -1, то против часовой стрелки
if napravl != 1 and napravl != -1:
    print('Не правильно выбрано направление, 1 - по часовой стрелке, -1 - против часовой стрелки')
else:
    speed = 0.05
    angle = 0 #угол для движения
    def motion():
        global angle #увеличиваем угол
        angle += speed * napravl
        x = centr_x + rad * math.cos(angle)
        y = centr_y + rad * math.sin(angle)
        holst.coords(point, x - 5, y - 5, x + 5, y + 5)
        window.after(30, motion)


motion()
window.mainloop()