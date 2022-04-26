from tkinter import *
import function as fun #함수 정의
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import os
import shutil
import random
from pathlib import Path

window = Tk()
window.title("Project_1_transformer")
window.geometry("600x400+%d+%d" % (window.winfo_screenwidth()/4, window.winfo_screenheight()/4))
window.resizable(False, False)

sample = ['.doc','.ppt','.pdf', '.hwp', '.jpg','.png','zip']
folder_name =list(range(random.randint(4,10)))

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

def File_Transform(A=False):
    for in_path in file_list:
        name, ext = os.path.splitext(in_path)
        if not os.path.isdir(name):
            if A ==True: pass #확장자 지정한걸로 바꾸기
            os.rename(name,name+ext)

def Make_Test():
    os.chdir('C:/Users/백 아울/Desktop/스크립트 언어/프로젝트1/Test_file')
    # 랜덤상위폴더
    head = random.sample(folder_name, (random.randint(1, 4)))
    # all_dir.append('c:/root_folder/'+str(i)+'dir')

    # 랜덤 파일구조 만들기
    for E in range(random.randint(10, 30)):
        file_name = str(random.randint(1000, 100000)) + str("".join(random.sample(sample, 1)))
        Path(file_name).touch()

    print("테스트 파일 생성 완료")

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
    type_1 =Button(text="(1)그냥 파일 변환하기", command=Button_Work_1)
    type_2 =Button(text="(2)대상 파일 확장자 선정 후 변환", command=Button_Work_1)
    #case_check =Checkbutton(text="대상 파일 확장자 선정 후 변환", varialbe =ignore_case )
    #type_1 = Button(text="파일 변환하기", command=Button_Work_1)
    #ignore_case.set(0)
    type_1.place(x=300,y=60)
    type_2.place(x=300,y=100)

def Button_Work_2():
    print("위치 이동")

def Button_Work_3():
    print("이름 변경")


def sub_Button_1_1():
    File_Select()
    File_Transform()

def sub_Button_1_2():
    File_Select()
    file_list += {"change to"}
    File_Select()
    File_Transform(True)

def print_result():
    pass

#프레임 라인
work_frame = Frame()
work_frame.pack()

#버튼 라인
Select1 =Button(text="파일 변환",command = Button_Work_1)
Select2 =Button(text="파일 이동",command = Button_Work_2)
Select3 =Button(text="이름 추가",command = Button_Work_3)

Select3.place(x=500,y=20)
Select2.place(x=400,y=20)
Select1.place(x=300,y=20)

#라벨 라인
ex_label1 =Label(text="이곳은 버튼공간")

ex_label1.pack()

#이외 라인
text = ScrolledText(width=40, height=30, font=("Consolas", 10))
text.delete("0.0", END)
text.insert(END, file_list)
text.pack(side=LEFT)

#단축키 라인
window.bind("<Escape>",stop)
window.bind("<Tab>",Make_Test)

window.mainloop()
