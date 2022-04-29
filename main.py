from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import function_fun as fun #함수 정의




#프레임 라인
work_frame = Frame()
work_frame.pack()

#버튼 라인
Select1 =Button(text="파일 변환",command = fun.Button_Work_1)
Select2 =Button(text="파일 이동",command = fun.Button_Work_2)
Select3 =Button(text="이름 추가",command = fun.Button_Work_3)
Retry_button =Button(text="Retry",command = fun.delete_button)
Exit_button =Button(text="Exit",command = fun.stop)

Select3.place(x=500,y=20)
Select2.place(x=400,y=20)
Select1.place(x=300,y=20)
Retry_button.place(x=410,y=350)
Exit_button.place(x=510,y=350)

#라벨 라인
ex_label1 =Label(text="파일 변환기")

ex_label1.pack()

#이외 라인

fun.text.delete("0.0", END)
fun.text.insert(END, fun.file_list)
fun.text.pack(side=LEFT)
fun.print_result()

#단축키 라인
fun.window.bind("<Escape>",fun.stop)
fun.window.bind("<Tab>",fun.Make_Test)

fun.window.mainloop()
