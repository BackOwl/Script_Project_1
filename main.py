from tkinter import *
import function as fun #함수 정의
from tkinter.ttk import *

window = Tk()
window.title("Project_1_transformer")
window.geometry("600x400+%d+%d" % (window.winfo_screenwidth()/4, window.winfo_screenheight()/4))
window.resizable(False, False)
#함수 라인
def stop(event=None):
    window.quit()

def File_Select():
    print("파일 선택")

def Foam_Select():
    print("확장자 선택")

def Button_Work_1():
    print("변환")

def Button_Work_2():
    print("위치 이동")

def Button_Work_3():
    print("이름 변경")


#버튼 라인
Select1 =Button(text="File Select",command = File_Select)
Select2 =Button(text="Foam Select",command = Foam_Select)

Select1.pack(side=RIGHT)
Select2.pack(side =RIGHT)
#라벨 라인
ex_label1 =Label(text="이곳은 버튼공간")

ex_label1.pack()

#이외 라인

#단축키 라인
window.bind("<Escape>",stop)

window.mainloop()
