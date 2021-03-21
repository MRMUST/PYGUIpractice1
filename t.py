import os
from tkinter import *

root = Tk()
root.title("제목 없음 - 연습용 메모장")
root.geometry("640x480+100+200")

filename = "note.txt"

def o():
    if os.path.isfile(filename):
        with open(filename,"r",encoding="utf8") as file:
            t.delete("1.0",END)
            t.insert(END, file.read())

def s():
    with open(filename,"w",encoding="utf8") as file:
       file.write(t.get("1.0",END))

menu = Menu(root)



menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기",command=o)
menu_file.add_command(label="저장",command=s)
menu_file.add_separator()
menu_file.add_command(label="닫기", command=root.quit)
menu.add_cascade(label="파일",menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

sb = Scrollbar(root)
sb.pack(side="right",fill = "y")

t = Text(root, yscrollcommand=Scrollbar.set)
t.pack(side="left",fill="both",expand=True)

sb.config(command=t.yview)

root.config(menu=menu)





root.mainloop()