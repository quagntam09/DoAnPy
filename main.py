import tkinter as tk
from Login_Register import LoginWinDow, RegisterWindow


menu_bar_color = '#383838'

class UserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('tk Hub')
        self.geometry('700x600')
        self.title('tk Hub')
        self.resizable(False, False)
        self.build_ui()
        self.user = None
    def setUser(self, user):
        self.user = user


    def build_ui(self):

        menu_bar_frame = tk.Frame(self, bg=menu_bar_color)
        menu_bar_frame.pack(side=tk.TOP, fill=tk.X)
        menu_bar_frame.configure(height=30)

        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)



        home_button = tk.Button(menu_bar_frame, text="Trang Chủ", fg='white', bg=menu_bar_color,
                                bd=0, activebackground=menu_bar_color, command=lambda: self.home_frame(main_frame))
        home_button.place(x=4, y=4)

        other_button = tk.Button(menu_bar_frame, text="Tài Khoản", fg='white', bg=menu_bar_color,
                                bd=0, activebackground=menu_bar_color, command=lambda: self.Account_frame(main_frame))
        other_button.place(x=100, y=4)

        login_button = tk.Button(menu_bar_frame, text="Đăng Nhập", fg='white', bg=menu_bar_color,
                                bd=0, activebackground=menu_bar_color, command=lambda: LoginWinDow(menu_bar_frame, controller= self))
        register_button = tk.Button(menu_bar_frame, text="Đăng Ký", fg='white', bg=menu_bar_color,
                                    bd=0, activebackground=menu_bar_color, command=lambda: RegisterWindow(menu_bar_frame, controller= self))
        login_button.place(x=196, y=4)
        register_button.place(x=292, y=4)

    def Account_frame(self, master):
        account_frame = tk.Frame(master, bg="green")
        account_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        print(self.user)
        account_frame.tkraise()
    def home_frame(self, master):
        home_frame = tk.Frame(master, bg="red")
        home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        home_frame.tkraise()


if __name__ == '__main__':
    app = UserApp()
    app.mainloop()