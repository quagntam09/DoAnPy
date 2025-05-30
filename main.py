import tkinter as tk
from Login_Register import LoginWinDow, RegisterWindow


menu_bar_color = '#383838'

class UserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('tk Hub')
        self.geometry('1000x600')
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
        home_button.pack(side= "left", padx=10, pady=5)

        other_button = tk.Button(menu_bar_frame, text="Tài Khoản", fg='white', bg=menu_bar_color,
                                bd=0, activebackground=menu_bar_color, command=lambda: self.Account_frame(main_frame))
        other_button.pack(side= "left", padx=10, pady=5)

        login_button = tk.Button(menu_bar_frame, text="Đăng Nhập", fg='white', bg=menu_bar_color,
                                bd=0, activebackground=menu_bar_color, command=lambda: LoginWinDow(menu_bar_frame, controller= self))
        register_button = tk.Button(menu_bar_frame, text="Đăng Ký", fg='white', bg=menu_bar_color,
                                    bd=0, activebackground=menu_bar_color, command=lambda: RegisterWindow(menu_bar_frame, controller= self))
        login_button.pack(side= "right", padx=10, pady=5)
        register_button.pack(side= "right", padx=10, pady=5)

    def Account_frame(self, master):
        account_frame = tk.Frame(master, bg="green")
        account_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        if self.user is None:
            label_error = tk.Label(account_frame, text="Vui lòng đăng nhập", fg="red", font=("Arial", 30))
            label_error.pack()
        else:

            label_name = tk.Label(account_frame, text="Tên: " + self.user.Ten, fg= "red", font=("Arial", 20))
            label_name.grid(x=80, y=80)
            label_email = tk.Label(account_frame, text="Email: " + self.user.Email, fg="red", font=("Arial", 20))
            label_email.grid(x=80, y=120)
            label_sdt = tk.Label(account_frame, text="Số điện thoại: " + self.user.Sdt, fg="red", font=("Arial", 20))
            label_sdt.grid(x=80, y=160)
            label_tien = tk.Label(account_frame, text="Tiền: " + str(self.user.Tien), fg="red", font=("Arial", 20))
            label_tien.grid(x=80, y=200)


        account_frame.tkraise()
    def home_frame(self, master):
        home_frame = tk.Frame(master, bg="white")
        home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        bar_frame = tk.Frame(home_frame, bg="red")
        bar_frame.pack(side= "left", fill=tk.Y, padx=5, pady=5 )
        bar_frame.propagate(flag= False)

        bar_frame.config(width= 45, bg= menu_bar_color)

        content_frame = tk.Frame(home_frame, bg="blue")
        content_frame.pack(side= "left", fill=tk.BOTH, expand=True, padx=(0,5), pady=5)
        content_frame.propagate(flag= False)
    
        home_frame.tkraise()


if __name__ == '__main__':
    app = UserApp()
    app.mainloop()