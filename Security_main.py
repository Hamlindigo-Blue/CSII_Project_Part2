from Security_gui import *


def main():
    window = Tk()
    window.title('Project Part 2')
    window.geometry('225x125')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()



if __name__ == '__main__':
    main()