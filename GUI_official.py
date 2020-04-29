from tkinter import *
from PIL import ImageTk,Image
from  face_recognition import *
import os



window = Tk()

window.title("Graduate Thesis")

window.geometry('1000x600')

lbl = Label(window, text="Graduate Thesis",fg="Red", font=("arial",27,"bold"))
lbl.place(x=370,y=10)

lb2 = Label(window, text="Khoa điện - điện tử",fg="Blue", font=("arial",15,"bold"))
lb2.place(x=30,y=60)

lb3 = Label(window, text="Ngành tự động hóa",fg="Blue", font=("arial",15,"bold"))
lb3.place(x=30,y=90)

lb4 = Label(window, text="Đề tài:",fg="Black", font=("arial",13,"bold"))
lb4.place(x=30,y=120)

lb5 = Label(window, text="Nhận dạng khuôn mặt và lưu trữ thông tin",fg="Black", font=("arial",15,"bold"))
lb5.place(x=100,y=130)

lb6 = Label(window, text="Xuất thông tin để lưu trữ và kiểm tra",fg="Black", font=("arial",15,"bold"))
lb6.place(x=100,y=160)

lb7 = Label(window, text="Tên GVHD:",fg="Black", font=("arial",10,"bold"))
lb7.place(x=50,y=210)

lb8 = Label(window, text=" Nguyễn Hoàng Giáp",fg="Black", font=("arial",12,"bold"))
lb8.place(x=140,y=210)

lb9 = Label(window, text="Tên SVTH:",fg="Black", font=("arial",10,"bold"))
lb9.place(x=50,y=240)

lb10 = Label(window, text="Vũ Gia Bảo",fg="Black", font=("arial",12,"bold"))
lb10.place(x=140,y=240)



#inset logo
pic_frame = Frame(window, width=100, height=50)
pic_frame.place(x=600,y=100)
my_image = ImageTk.PhotoImage(Image.open("LOGO.png"))
LabelFrame= Label(pic_frame, image= my_image)
LabelFrame.pack()


def But_Start():
	main()

def But_Stop():
	stop_program()

def But_Check():
	lb1x.configure(text="Be my girl !!")


btn_quit = Button(window, text="Quit",bg="white",fg="Black", command=window.destroy)
btn_quit.place(x=950, y=10)

btn_start = Button(window, text="Bắt đầu",bg="Green",fg="Yellow", command= But_Start)
btn_start.place(x=500, y=500)

btn_stop = Button(window, text="Kết thúc",bg="Red",fg="Black", command=But_Stop)
btn_stop.place(x=700, y=500)

btn_check = Button(window, text="Kiểm tra",bg="Pink",fg="Black", command=But_Check)
btn_check.place(x=300, y=500)


lb1x = Label(window, text="Vũ Gia Bảo",fg="Black", font=("arial",12,"bold"))
lb1x.place(x=140,y=300)


	




window.mainloop()
