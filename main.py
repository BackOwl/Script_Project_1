from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import os
import shutil
import random
from pathlib import Path
#import function as fun #함수 정의

window = Tk()
window.title("Project_1_transformer")
window.geometry("600x400+%d+%d" % (window.winfo_screenwidth()/4, window.winfo_screenheight()/4))
window.resizable(False, False)

sample = ['.doc', '.ppt', '.pdf', '.hwp', '.jpg', '.png', 'zip']

history_frame = LabelFrame(text='Foam_Select')
history_listbox = Listbox(history_frame, selectmode='single', height=5)
file_list = [] #선택한 파일 주소들의 튜플

Acess_List =[] #떠잇는 위젯들

#함수 라인
def stop(event=None):
    window.quit()

def File_Select():
    global file_list
    global text
    print("파일 선택")
    file_names = filedialog.askopenfilenames(title='Select text files',filetypes=(("all files", "*.*"),("text files (.txt)", "*.txt") ))
    file_list.extend(file_names)
    #스크롤 갱신
    text.delete("0.0", END)
    text.insert(END, file_list)
    text.pack(side=LEFT)


def File_Transform(type):
    for in_path in file_list:
        name, ext = os.path.splitext(in_path)
        if not os.path.isdir(name):
            #확장자 지정한걸로 바꾸기
            print(name+ext,"을 변환합니다",name+type)
            os.rename(name+ext,name+type)
            print_result(f"{ext}확장자를 {type} 확장자로 변환성공")


def Make_Test():
    os.chdir('C:/Users/백 아울/Desktop/스크립트 언어/프로젝트1/Test_file')

    folder_name = list(range(random.randint(4, 10)))
    # 랜덤상위폴더
    head = random.sample(folder_name, (random.randint(1, 4)))
    # all_dir.append('c:/root_folder/'+str(i)+'dir')

    # 랜덤 파일구조 만들기
    for E in range(random.randint(10, 30)):
        file_name = str(random.randint(1000, 100000)) + str("".join(random.sample(sample, 1)))
        Path(file_name).touch()

    print("테스트 파일 생성 완료")

def select_pattern(event=None):
    print("select_pattern-----------------------" )
    history_frame.place_forget()
    File_Transform(history_listbox.get(history_listbox.curselection()))
    history_listbox.delete(history_listbox.curselection())

def Only_pattern(event=None):
    for in_path in file_list:
        name, ext = os.path.splitext(in_path)
        print(ext, history_listbox.get(history_listbox.curselection()))
        if not ext == history_listbox.get(history_listbox.curselection()):
            print(in_path + "삭제\n")
            # file_list.pop(in_path)
    print(history_listbox.get(history_listbox.curselection()))
    history_listbox.delete(history_listbox.curselection())
    next()



def File_Search(type):
    for in_path in file_list:
        name, ext = os.path.splitext(in_path)
        if not ext == type:
            print(in_path + "삭제\n")
            #file_list.pop(in_path)


def Foam_Select(acess):
    print_result("선택할 타입을 골라주세요")
    print("확장자 선택 전")
    now = False
    delete_button()
    history_frame.place(x=300,y=60)
    for i in range(0,7):
        history_listbox.insert(i,sample[i])
    history_listbox.insert(END, '.[]')
    history_listbox.pack(side=LEFT, fill=X, expand=True)
    history_listbox.bind('<<ListboxSelect>>',acess)
    scrollbar = Scrollbar(history_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    history_listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=history_listbox.yview)



def Button_Work_1(work=False):
    print("변환")
    type_1 =Button(text="(1)그냥 파일 변환하기", command=sub_Button_1_1)
    type_2 =Button(text="(2)대상 파일 확장자 선정 후 변환", command=sub_Button_1_2)
    Acess_List.append(type_1)
    Acess_List.append(type_2)
    type_1.place(x=300,y=60)
    type_2.place(x=300,y=100)

def Button_Work_2(work=False):
    print("위치 이동")

    Acess_List.append(Button_Work_2)

def Button_Work_3(work=False):
    print("이름 변경")

    Acess_List.append(Button_Work_3)


def sub_Button_1_1():
    global file_list
    file_list=[]
    File_Select()
    Foam_Select(select_pattern)
    #결과 출력

def sub_Button_1_2():
    global file_list
    file_list = []
    File_Select()
    print("파일1")
    Foam_Select(Only_pattern)


def next():
    print("파일2")
    Foam_Select(select_pattern)
    print_result("바꾸실 타입을 골라주세요")
    print("파일3")


def delete_button():
    global Acess_List
    for i in Acess_List:
        i.place_forget()
        #Acess_List.pop()
    print("버튼 지움 ")

def print_result(msg=' '):
    delete_button()
    text = ScrolledText(width=40, height=5, font=("Consolas", 10))
    text.delete("0.0", END)
    text.insert(END, msg)
    text.place(x=300,y=250)
    Acess_List.append(text)




#프레임 라인
work_frame = Frame()
work_frame.pack()

#버튼 라인
Select1 =Button(text="파일 변환",command = Button_Work_1)
Select2 =Button(text="파일 이동",command = Button_Work_2)
Select3 =Button(text="이름 추가",command = Button_Work_3)
Retry_button =Button(text="Retry",command = delete_button)
Exit_button =Button(text="Exit",command = stop)

Select3.place(x=500,y=20)
Select2.place(x=400,y=20)
Select1.place(x=300,y=20)
Retry_button.place(x=410,y=350)
Exit_button.place(x=510,y=350)

#라벨 라인
ex_label1 =Label(text="이곳은 버튼공간")

ex_label1.pack()

#이외 라인
text = ScrolledText(width=40, height=30, font=("Consolas", 10))
text.delete("0.0", END)
text.insert(END, file_list)
text.pack(side=LEFT)
print_result()

#단축키 라인
window.bind("<Escape>",stop)
window.bind("<Tab>",Make_Test)

window.mainloop()
