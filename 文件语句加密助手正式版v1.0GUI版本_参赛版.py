# -*- coding:utf-8 -*-

#start
#python file
#python module file
from random import *
from tkinter.messagebox import *
from tkinter import *
from tkinter import ttk
true = True
false = False

def encryption(message,password):
    password = str(password)
    pwd_list = list(password)
    for i in range(len(pwd_list)):
        pwd_list[i] = ord(pwd_list[i])
        pwd_list[i] = str(pwd_list[i])
    password = '|'.join(pwd_list)
    
    message = str(message)
    list_ = list(message)
    for i in range(len(list_)):
        list_[i] = ord(list_[i])
        list_[i] = str(list_[i])

    join_ = ['23666#@','4@','33&$@','22537#^&@*','11425523#@*@&$SDF']
    join_ = ('11425523#@*@&$SDF22537#^&@*33&$@4@23666#@')
    join_ = list(join_)
    #混淆加密字符串的代码↑
    for i in range(10):    #←将这个混淆加密字符串的代码打乱十遍，很难复原
        shuffle(join_)  #←这个shuffle函数是modlue：system里的，使用 from random import shuffle导入，他的作用就是打乱列表，然后我用for循环打乱十遍
    
    if (message != ''): #if (not message == '')
        join_ = ''.join(join_)
        ciphertext = (join_).join(list_)
        ciphertext = ciphertext+(join_)+'+'+password
        return ciphertext
    else:
        return ''

def decrypt(message,password):
    list_ = message.split('+')
    remove_str = list_[0][-41:len(list_[0])+1]
    pwd = list_[1]
    pwd = pwd.split('|')
    for i in range(len(pwd)):
        try:
            pwd[i] = int(pwd[i])
            pwd[i] = chr(pwd[i])
        except Exception as error_all:
            pass
    
    pwd = ''.join(pwd)
    pwd = pwd.replace('\n','')
    
    if pwd == password:
        pass
    else:
        showerror('','密码不正确，退出重试')
        exit()
    
    list_ = list_[0]
    list_ = list_.split(remove_str)
    del list_[len(list_)-1]
    
    for i in range(len(list_)):
        list_[i] = int(list_[i])
        list_[i] = chr(list_[i])
    
    text = ''.join(list_)
    return text

def show_decrypt():
    sc = Tk()
    sc.geometry('500x400')
    willshowinfo = decrypt((decrypt_sc.message).get(),(decrypt_sc.password).get())
    selectableMsg = Text(sc,relief='flat',wrap='word',font=('consolas',15),height=1080,width=1920)
    selectableMsg.insert(1.0,willshowinfo)
    selectableMsg.configure(state='disabled')
    selectableMsg.pack()


def show_encryption():
    sc = Tk()
    sc.geometry('500x400')
    willshowinfo = encryption(encryption_sc.message.get(),encryption_sc.password.get())
    selectableMsg = Text(sc,relief='flat',wrap='word',font=('consolas',15),height=1080,width=1920)
    selectableMsg.insert(1.0,willshowinfo)
    selectableMsg.configure(state='disabled')
    selectableMsg.pack()

def encryption_sc():
        sc = Tk('500x500')
        sc.geometry('500x500')
        sc.title('加密')
        for i in range(2):
            ttk.Label(sc,text='\n').pack()
        ttk.Label(sc,text='要加密的语句\n').pack()
        encryption_sc.message = ttk.Entry(sc)
        encryption_sc.message.pack()
        ttk.Label(sc,text='\n').pack()
        ttk.Label(sc,text='\n').pack()
        ttk.Label(sc,text='设置密码').pack()
        encryption_sc.password = ttk.Entry(sc, show='*')
        encryption_sc.password.pack()
        ttk.Label(sc,text='\n').pack()
        ttk.Button(sc,text='确认',command=show_encryption).pack()  #show_encryption
    
        sc.mainloop()

def decrypt_sc():
    sc = Tk()
    sc.geometry('500x500')
    sc.title('解密')
    for i in range(2):
        ttk.Label(sc,text='\n').pack()
    ttk.Label(sc,text='要解密的语句\n').pack()
    decrypt_sc.message = ttk.Entry(sc)
    decrypt_sc.message.pack()
    ttk.Label(sc,text='\n').pack()
    ttk.Label(sc,text='\n').pack()
    ttk.Label(sc,text='输入密码').pack()
    decrypt_sc.password = ttk.Entry(sc, show='*')
    decrypt_sc.password.pack()
    ttk.Label(sc,text='\n').pack()
    ttk.Button(sc,text='确认',command=show_decrypt).pack()  #show_decrypt

    sc.mainloop()

def help_window():
    help_sc = Tk()
    help_sc.geometry('500x500')
    help_sc.title('帮助')
    help_pack = Text(help_sc, width=500, height=500)
    help_pack.pack()
    help_pack.insert('1.0','加密语句和解密语句的算法是由 "yuan" 独自一人开发, 没有任何python第三方模块的支持\n在开始界面, 点击 "加密语句" , 在新窗口内的第一个输入框输入你想加密的语句, 密码可选设置, 之后点击加密, 即可在新窗口内看到被加密的语句, 按下 Ctrl+A 全选, 之后按下 Ctrl+C 进行复制\n同理, 在使用解密语句的时候, 输入被加密的语句和密码, 即可进行解密\n本软件在github上面开源, 请转至: \nhttps://github.com/yuanmaker/File-Statement-Encryption-Assistant.git')

choose = Tk()
sc_width = choose.winfo_screenwidth()
sc_height = choose.winfo_screenheight()
sc_width = str(sc_width//2)
sc_height = str(sc_height//2)
choose.geometry('300x200'+'+'+sc_width+'+'+sc_height)
choose.title('文件语句加密助手')
encryption_button = ttk.Button(choose,text='加密语句',command=encryption_sc)
encryption_button.pack()
dectypt_button = ttk.Button(choose,text='解密语句',command=decrypt_sc)
dectypt_button.place()
dectypt_button.pack()
help_button = ttk.Button(choose, text='帮助', command=help_window)
help_button.pack()

choose.mainloop()