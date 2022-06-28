from tkinter import *


def calculator(source, side):
    storedata = Frame(source, borderwidth=5, bd=5, bg="peach puff")
    storedata.pack(side=side, expand=YES, fill=BOTH)
    return storedata


def button(source, side, text, command=None):
    storedata = Button(source, text=text, command=command, bg="peach puff")
    storedata.pack(side=side, expand=YES, fill=BOTH)
    return storedata


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'ubuntu 22 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Arithmetic Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right'
              , bd=20, bg="beige").pack(side=TOP,
                                        expand=YES, fill=BOTH)

        for clearButton in (["C"]):
            erase = calculator(self, TOP)
            for char in clearButton:
                button(erase, LEFT, char, lambda
                    storedata=display, q=char: storedata.set(''))

        for numButton in ("789*", "456+", "123-", ".0/"):
            FunctionNum = calculator(self, TOP)
            for Equals in numButton:
                button(FunctionNum, LEFT, Equals, lambda
                    storedata=display, q=Equals: storedata
                       .set(storedata.get() + q))

        EqualButton = calculator(self, TOP)
        for Equals in "=":
            if Equals == '=':
                ButtonEquals = button(EqualButton, LEFT, Equals)
                ButtonEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                            storedata=display: s.calc(storedata), '+')


            else:
                ButtonEquals = button(EqualButton, LEFT, Equals,
                                    lambda storedata=display, s=' %s ' % Equals: storedata.set
                                    (storedata.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    app().mainloop()
