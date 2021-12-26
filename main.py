
import tkinter as tk
from normgostvrode1 import *
def graphic_interface():
    count=0
    def say_hello():
        print("здарова бандиты")
    def create_newlabel():
        label = tk.Label(win,text='some text').pack()
    def counter():
        global count
        count+=1
        btn_4['text']=f'counter:{count}'
    def randomcolor():
        win.config(bg='#0e4c6a')
    def get_entry():
        value=name.get()
        if value:
            print(value)
    def del_entry():
        name.delete(0,tk.END)



    win = tk.Tk()
    win.title('    супер мега пупре шифратор')
    win.iconphoto(False, tk.PhotoImage(file='christmas-ball-11530976313ayoldrza17.png'))
    w, h = 1280, 720
    win.geometry(f'{w}x{h}+130+28')
    win.resizable(True, True)
    win.minsize(600, 400)
    win.config(bg='#b49add', )
    # win['bg']='red'
    # label_1 = tk.Label(win,
    #                    text='anime na ave',
    #                    bg='cyan',
    #                    fg='#097a6a',
    #                    font=('Arrial', 30, 'bold'),
    #                    padx=40,pady=5, # отступ по х у от краев
    #                    width=20, height=2, # ширина высота лейбла
    #                    anchor='se',
    #                    relief=tk.RAISED,
    #                    bd=10, # ширина рамок
    #                    # justify=tk.CENTER
    #                    ).pack()
    # btn_1 = tk.Button(win, fg='#097a6a', bg='red', text='здарова бандит',command=say_hello).pack()
    #
    # btn_2 = tk.Button(win, bg='cyan', fg='#097a6a', text='if u wanna create new label, just touch me',
    #                   command=create_newlabel).pack()
    #
    # btn_3 = tk.Button(win, bg='cyan', fg='#097a6a', text='if u wanna lambda, just touch me', activebackground='blue',
    #                   command=lambda: tk.Label(win, bg='black', fg='white', text='lambda lives matter').pack()).pack()
    #
    # btn_4 = tk.Button(win, bg='orange', fg='#097a6a', text=f'counter:{count}',
    #                   command=counter).pack()
    # btn_5 = tk.Button(win, bg='PURPLE', fg='#097a6a', text='change bg color',
    #                   command=randomcolor).pack()
    # btn_6 = tk.Button(win, text='griddddd1').grid(row=0, column=0, stick='w')
    # btn_7 = tk.Button(win, text='griddddd2').grid(row=0, column=1, stick='w')
    # btn_8 = tk.Button(win, text='griddddd3').grid(row=1, column=0, stick='e')
    # btn_9 = tk.Button(win, text='gridddddeeeeeer4').grid(row=1, column=1)
    # btn_10 = tk.Button(win, text='griddddd5').grid(row=2, column=0, stick='we')
    # btn_11 = tk.Button(win, text='griddddd6').grid(row=3, column=0,columnspan=2,stick='we')
    # btn_1w = tk.Button(win, text='griddddd7').grid(row=0, column=2, rowspan=4, stick='ns')
    # for i in range(5):
    #     for j in range(4):
    #         tk.Button(win, bg='orange', fg='#097a6a', text=f'Hi: {i}\t{j}').grid(row=i, column=j, stick='we')

    win.grid_columnconfigure(0, minsize=200)
    win.grid_columnconfigure(1, minsize=150)
    name = tk.Entry(win, bg='orange')
    name.grid(row=0, column=1, stick='we')

    tk.Label(win, text='Name:').grid(row=0, column=0, stick='we')

    tk.Button(win, text='OK', command=get_entry).grid(row=1, column=0, stick='we')

    tk.Button(win, text='del', command=del_entry).grid(row=1, column=1, stick='we')
    tk.Button(win, text='ins', command=lambda: name.insert('end','kekeek')).grid(row=1, column=2, stick='we')

    tk.Label(win, text='password:').grid(row=2, column=0, stick='we')
    tk.Entry(win, bg='orange', show='*').grid(row=2, column=1, stick='we') #пароль в звёздочках



    win.mainloop()

def main():

    graphic_interface()

    # cryptMode = input("[E]ncrypt | [D]escrypt: ").upper()
    key = 18318279387912387912789378912379821879387978238793278872378329832982398023031
    print(len(str(key)))
    encript_route = r'1.txt'
    route = r'2.txt'
    decript_route = r'3.txt'

    # шифровка
    cyphred = []  # тут будет хранится зашифрованный текст
    gost = Crypt(key, blocks)
    # try:
    s = []
    # Читаем из файла текст и шифруем каждую букву
    with open(encript_route, 'rb') as file:
        s = file.read()
        print(s)
        print(len(s))
    b = text_to_blocks(s)

    print(b)
    print(len(b))
    for x in b:
        cyphred.append(gost.encrypt(x))
    """except: # если не удалось открыть файл, выходим
        print(f"Не удалось открыть файл {encript_route}")
        return"""
    # try:
    s = blocks_to_text(cyphred)
    # записываем зашифрованный текст в файл
    with open(route, 'wb') as file:
        file.write(s)
    print("Файл зашифрован")
    """except:
        print(f"Не удалось открыть файл {decript_route}")
        return"""
    # дешифровка
    decyphred = []  # тут будет храниться расшифрованный текст
    gost = Crypt(key, blocks)
    # try:
    with open(route, 'rb') as file:
        s = file.read()
    b = text_to_blocks(s)
    for x in b:
        #  расшифровываем текст из файла и добавляем его в список
        decyphred.append(gost.decrypt(x))
    """except:
        print(f"Не удалось открыть файл {decript_route}")
        return"""
    s = blocks_to_text(decyphred)
    # try:
    with open(decript_route, 'wb') as file:
        # объеденяем расшифрованные символы в строку и записываем в файл
        file.write(s)
    print("Файл расшифрован")
    """except:
        print(f"Не удалось открыть файл {encript_route}")
        return"""



if __name__ == "__main__":
    main()














# key = os.urandom(16)
# key=key.decode('utf-8')
# print("key:",key,)
# iv = os.urandom(16)
# print("iv:",iv)
#
# encrypted = aes.AES(key).encrypt_ctr(b'Attack at dawn', iv)
# print(encrypted)
#
# print(aes.AES(key).decrypt_ctr(encrypted, iv))
# # key='hgfakavsdhdbf2141jhrbh32jtvjbdjm,'
# # a=encrypt(key, plaintext,)
