import tkinter as tk
from normgostvrode1 import *
import os
import hashlib



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
    def get_key_inp_out():
        value_key=name_key.get()
        inpp=name_inp.get()
        outt=name_out.get()
        print(value_key)
        print(inpp)
        print(outt)
        if inpp=="":
            print(43424)
        global key, input_route, output_route
        if value_key:
            key = new_key(value_key)
        #если выбрано зашифровать
        if ed_val.get() == 1 :
            input_route = inpp
            if inpp == '':
                input_route = r'1.txt'
            output_route = outt
            if outt == '':
                output_route = r'2.txt'
            encrypt_gost(key, input_route, output_route)

        elif ed_val.get() == 2:
            input_route = inpp
            if inpp == '':
                input_route = r'2.txt'
            output_route = outt
            if outt == '':
                output_route = r'3.txt'
            decrypt_gost(key, input_route, output_route)

        print(input_route)
        print(output_route)

    def del_entry():
        name_key.delete(0,tk.END)

    chiphers = {
        1: 'гост магма',
        2: 'AES'
    }
    def select_cipher():
        chipher_val_get = chipher_val.get()
        chipher_text.set(f'вы выбрали {chiphers[chipher_val_get]}')

    eds = {
        1: 'encrypt',
        2: 'decrypt'
    }
    def select_ed():
        ed_val_get = ed_val.get()
        ed_text_get = ed_text.get()

        ed_text.set(f'вы выбрали {eds[ed_val_get]}')


    win = tk.Tk()
    win.title('    супер мега пупре шифратор')
    win.iconphoto(False, tk.PhotoImage(file='christmas-ball-11530976313ayoldrza17.png'))
    w, h = 640, 360
    win.geometry(f'{w}x{h}+130+28')
    win.resizable(True, True)
    win.minsize(600, 300)
    win.config(bg='#b49add', )

    win.grid_columnconfigure(2, minsize=150)
    win.grid_columnconfigure(3, minsize=150)

####
    name_key = tk.Entry(win, bg='orange', show='*')
    name_key.grid(row=0, column=1, stick='we')

    tk.Label(win, text='Enter key:', bg='black', fg='white').grid(row=0, column=0, stick='we')
    tk.Button(win, text='OK', command=get_key_inp_out, bg='blue').grid(row=2, column=2, stick='nswe')

    # tk.Button(win, text='del', command=del_entry).grid(row=1, column=1, stick='we')
    # tk.Button(win, text='ins', command=lambda: name.insert('end','kekeek')).grid(row=1, column=2, stick='we')

    tk.Label(win, text='Enter input file:', bg='black', fg='white').grid(row=1, column=0, stick='we')
    name_inp = tk.Entry(win, bg='orange')
    name_inp.grid(row=1, column=1, stick='we')

    tk.Label(win, text='Enter output file:', bg='black', fg='white').grid(row=2, column=0, stick='we')
    name_out = tk.Entry(win, bg='orange')
    name_out.grid(row=2, column=1, stick='we')

    ed_val = tk.IntVar()
    ed_text = tk.StringVar()
    tk.Radiobutton(win, text='encrypt', variable=ed_val, value=1, command=select_ed, bg='orange').grid(
        row=0, column=2, stick='we')
    tk.Radiobutton(win, text='decrypt', variable=ed_val, value=2, command=select_ed, bg='orange').grid(row=1,
                                                                                                            column=2,
                                                                                                            stick='we')

    tk.Label(win, textvariable=ed_text, bg='#b49add').grid(row=3, column=2, stick='w')


    chipher_val = tk.IntVar()
    chipher_text=tk.StringVar()
    tk.Radiobutton(win, text='гост магма', variable=chipher_val, value=1, command=select_cipher, bg='orange').grid(row=0, column=3,stick='we')
    tk.Radiobutton(win, text='AES', variable=chipher_val, value=2, command=select_cipher, bg='orange').grid(row=1, column=3, stick='we')

    tk.Label(win, textvariable=chipher_text, bg='#b49add').grid(row=3, column=3, stick='w')

    win.mainloop()

def new_key(password):
    hash_object = hashlib.sha256(bytes(password, 'utf-8'))
    hex_dig = hash_object.hexdigest()
    keys = text_to_blocks(bytes(hex_dig, 'utf-8'), 32)
    key = keys[0]
    return key


def main():
    global key, encript_route, route, decript_route
    key = 18318279387912387912789378912379821879387978238793278872378329832982398023031

    graphic_interface()
    


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
