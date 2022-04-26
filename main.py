from tkinter import *
import function as fun #함수 정의
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

window = Tk()
window.title("Project_1_transformer")
window.geometry("600x400+%d+%d" % (window.winfo_screenwidth()/4, window.winfo_screenheight()/4))
window.resizable(False, False)

file_list =[] #선택한 파일 주소들의 리스트

#함수 라인
def stop(event=None):
    window.quit()

def File_Select():
    global file_list
    global text
    print("파일 선택")
    file_names = filedialog.askopenfilenames(title='Select text files',filetypes=(("all files", "*.*"),("text files (.txt)", "*.txt") ))
    file_list += file_names
    #스크롤 갱신
    text.delete("0.0", END)
    text.insert(END, file_list)
    text.pack(side=LEFT)

def select_pattern():
    pass

def Foam_Select():
    print("확장자 선택")
    history_frame = LabelFrame(text='Foam_Select')
    history_frame.pack(fill=X)
    history_listbox = Listbox(history_frame, selectmode='single', height=5)
    history_listbox.insert(0,'.jpg')
    history_listbox.insert(1,'.png')
    history_listbox.insert(END, '[a-zA-z]+')
    history_listbox.pack(side=LEFT, fill=X, expand=True)
    history_listbox.bind('<<ListboxSelect>>', select_pattern)
    scrollbar = Scrollbar(history_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    history_listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=history_listbox.yview)

def Button_Work_1():
    print("변환")

def Button_Work_2():
    print("위치 이동")

def Button_Work_3():
    print("이름 변경")

#프레임 라인
work_frame = Frame()
work_frame.pack()

#버튼 라인
Select1 =Button(text="File Select",command = File_Select)
Select2 =Button(text="Foam Select",command = Foam_Select)

Select1.place(x=480,y=20)
Select2.place(x=380,y=20)

#라벨 라인
ex_label1 =Label(text="이곳은 버튼공간")

ex_label1.pack()

#이외 라인
text = ScrolledText(width=50, height=30, font=("Consolas", 10))
text.delete("0.0", END)
text.insert(END, file_list)
text.pack(side=LEFT)

#단축키 라인
window.bind("<Escape>",stop)

window.mainloop()
