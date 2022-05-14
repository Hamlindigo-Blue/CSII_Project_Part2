# Original Idea: https://www.youtube.com/watch?v=H8t4DJ3Tdrg&t=79s
# Original Idea: https://www.youtube.com/watch?v=g81l3y2i-so
#Added Features: GUI + encryption/decryption process + modulus/classes
from tkinter import *
import base64

class GUI:
    '''
    A class to representing the GUI object
    '''
    def __init__(self, window) -> None:
        '''
        Method to set the interface of the primary window and commands that directed through buttons.
        '''

        self.window = window
        #Status
        self.frame_shapes = Frame(self.window)
        self.frame_shapes.pack( pady=25)

        self.radio_rectangle = Button(self.frame_shapes, text='Encrypt', padx=10, pady=5, command=self.click_encryption)
        self.radio_square = Button(self.frame_shapes, text='Decrypt', padx=10, pady=5, command=self.click_decryption)

        self.radio_square.pack(side='right')
        self.radio_rectangle.pack(side='right')

        self.frame_shapes.pack()
        #Exit
        self.button_submit = Button(self.window, text='EXIT', padx=10, pady=5, command=window.destroy)
        self.button_submit.pack(side='bottom', pady=5)


    def click_decryption(self)->None:
        '''
        Method to send information to be decrypted.
        '''

        global top_decryption
        global decryption_output_box
        global decrypt_key


        top_decryption = Toplevel()
        top_decryption.title('Decryption')
        top_decryption.geometry('300x350')
        top_decryption.resizable(False, False)

        decryption_label = Label(top_decryption, text='Decryption')
        decryption_label.pack(pady=25)

        decryption_output_label = Label(top_decryption, text='Enter Output Text: ')
        decryption_output_label.pack(pady=5)

        decryption_output_box = Entry(top_decryption, width=50)
        decryption_output_box.pack(padx=10, pady=10)

        decryption_key_label = Label(top_decryption, text='Enter Key: ')
        decryption_key_label.pack(pady=5)

        decrypt_key = StringVar()

        decryption_key_box = Entry(top_decryption, textvariable=decrypt_key, show='*')
        decryption_key_box.pack(padx=10, pady=10)

        square_execution = Button(top_decryption, text='Execute',command= self.decryption_process)
        square_execution.pack(pady=5)

    def decryption_process(self)->None:
        '''
        Method that decrypts information.
        '''

        password = decrypt_key.get()

        if password == '1234':
            decryption_screen = Toplevel()
            decryption_screen.title('Decryption Output')
            decryption_screen.geometry('400x200')
            decryption_screen.resizable(False,False)

            input_text = decryption_output_box.get()
            decode_text = input_text.encode('ascii')
            base64_bytes=base64.b64decode(decode_text)
            decrypt = base64_bytes.decode('ascii')

            Label(decryption_screen, text="DECRYPT", font='arial', fg='white', bg='green').place(x=10, y=0)
            text2 = Text(decryption_screen, font='Rpbote 10', bg='white', relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypt)





    def click_encryption(self)->None:
        '''
        Method to send information to be encrypted.
        '''

        global top_encryption
        global encryption_input_box
        global encrypt_key

        top_encryption = Toplevel()
        top_encryption.title('Encryption')
        top_encryption.geometry('300x350')
        top_encryption.resizable(False, False)

        encryption_label = Label(top_encryption, text='Encryption')
        encryption_label.pack(pady=25)

        encryption_input_label = Label(top_encryption, text='Enter Input Text: ')
        encryption_input_label.pack(pady=5)

        encryption_input_box = Entry(top_encryption)
        encryption_input_box.pack(padx=10, pady=10)

        encryption_key_label = Label(top_encryption, text='Enter Key: ')
        encryption_key_label.pack(pady=5)

        encrypt_key = StringVar()

        encryption_key_box = Entry(top_encryption, textvariable=encrypt_key, show='*')
        encryption_key_box.pack(padx=10, pady=10)

        circle_execution = Button(top_encryption, text='Execute',command=self.encryption_process)
        circle_execution.pack(pady=15)

    def encryption_process(self)->None:
        '''
        Method to encrypt information.
        '''


        password = encrypt_key.get()
        if password == '1234':
            encryption_screen = Toplevel()
            encryption_screen.title('Encryption Output')
            encryption_screen.geometry('400x200')
            encryption_screen.resizable(False, False)

            input_text = encryption_input_box.get()
            encode_text = input_text.encode('ascii')
            base64_bytes = base64.b64encode(encode_text)
            encrypt = base64_bytes.decode('ascii')

            Label(encryption_screen, text="ENCRYPT", font='arial', fg='white', bg='red').place(x=10, y=0)
            text2 = Text(encryption_screen, font='Rpbote 10', bg='white', relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, encrypt)

