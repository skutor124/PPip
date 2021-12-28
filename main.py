import tkinter as tk
from normgostvrode1 import *
import os
import hashlib




key = 18318279387912387912789378912379821879387978238793278872378329832982398023031
def graphic_interface():

    def say_hello():
        print("здарова бандиты")
    def create_newlabel():
        label = tk.Label(win, text='some text').pack()
    # def counter():
    #     global count
    #     count+=1
    #     btn_4['text']=f'counter:{count}'
    def randomcolor():
        win.config(bg='#0e4c6a')
    def get_key():
        value=name.get()
        global key
        if value:
            key=new_key(value)



    def del_entry():
        name.delete(0,tk.END)
    def select_cipher():
        eee=chipher_val.get()
        chipher_text.set(f'вы выбрали{eee}')
        if eee==1:
            print("gost")
        elif eee == 2:
            print("aes")
        elif eee == 3:
            print("lol")



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

    # win.grid_columnconfigure(0, minsize=200)
    # win.grid_columnconfigure(1, minsize=150)
####
    name = tk.Entry(win, bg='orange', show='*')
    name.grid(row=0, column=1, stick='we')

    tk.Label(win, text='Enter key:').grid(row=0, column=0, stick='we')

    tk.Button(win, text='OK', command=get_key).grid(row=0, column=2, stick='we')

    tk.Button(win, text='del', command=del_entry).grid(row=1, column=1, stick='we')
    tk.Button(win, text='ins', command=lambda: name.insert('end','kekeek')).grid(row=1, column=2, stick='we')

    tk.Label(win, text='password:').grid(row=2, column=0, stick='we')
    tk.Entry(win, bg='orange', show='*').grid(row=2, column=1, stick='we') #пароль в звёздочках

    chipher_val = tk.IntVar()
    chipher_text=tk.StringVar()
    tk.Radiobutton(win, text='гост магма', variable=chipher_val, value=1, command=select_cipher).grid(row=0, column=3,stick='w')
    tk.Radiobutton(win, text='AES', variable=chipher_val, value=2, command=select_cipher).grid(row=1, column=3, stick='w')
    tk.Radiobutton(win, text='lol', variable=chipher_val, value=3, command=select_cipher).grid(row=2, column=3, stick='w')
    tk.Label(win, textvariable=chipher_text, bg='#b49add').grid(row=3, column=3, stick='w')

    win.mainloop()

def new_key(password):
    hash_object = hashlib.sha256(bytes(password, 'utf-8'))
    hex_dig = hash_object.hexdigest()
    keys = text_to_blocks(bytes(hex_dig, 'utf-8'), 32)
    key = keys[0]
    return key


def main():


    encript_route = r'1.txt'
    route = r'2.txt'
    decript_route = r'3.txt'

    graphic_interface()
    print(key)
    encrypt_gost(key, encript_route,route)
    decrypt_gost(key,route, decript_route )


if __name__ == "__main__":
    main()





# key = os.urandom(16)
# key=key.decode('utf-8')
# key=()
# print("key:",key,)
# iv = os.urandom(16)
# print("iv:",iv)
# rand = int(int(str(os.urandom(4), encoding="UTF-8")).encode('hex'), 16)
# print(rand)
#  # You can then 'cycle' it against the length.
# rand_char = chars_list[rand % 80] # or maybe '% len(chars_list)'


# encrypted = aes.AES(key).encrypt_ctr(b'Attack at dawn', iv)
# print(encrypted)
#
# print(aes.AES(key).decrypt_ctr(encrypted, iv))
# # key='hgfakavsdhdbf2141jhrbh32jtvjbdjm,'
# # a=encrypt(key, plaintext,)
