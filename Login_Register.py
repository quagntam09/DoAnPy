import tkinter as tk
from tkinter import messagebox,ttk
import bcrypt
from user.CUser import UserManager
import re
class LoginWinDow(tk.Toplevel):
    def __init__(self,master, controller):
        super().__init__(master)
        self.controller = controller
        self.build_ui()
        self.controller.withdraw()
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_close(self.controller))

    def on_close(self, master):
        master.deiconify()
        self.destroy()


    def build_ui(self):

        title = tk.Label(self, text="Đăng Nhập", font=("Helvetica", 18, "bold"))
        title.pack(pady=(30, 20))


        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Tài Khoản:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="e", padx=5, pady=10)
        self.Id_entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30)
        self.Id_entry.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Mật Khẩu:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e", padx=5, pady=10)
        self.password_entry = tk.Entry(form_frame, show="*", font=("Helvetica", 12), width=30)
        self.password_entry.grid(row=1, column=1, padx=5)

        tk.Button(self, text="Đăng nhập", command=self.login, font=("Helvetica", 12), bg="#4CAF50", fg="white", width=20).pack(pady=(20, 10))

        tk.Button(self, text="Quay lại", command=lambda: self.on_close(self.controller), font=("Helvetica", 11), width=20).pack()


    def login(self):
        id = self.Id_entry.get()
        self.DanhSachUsers = UserManager()
        password = self.password_entry.get()
        user = None
        for u in self.DanhSachUsers.Users:
            if u.Account.get("AccountId") == id:  
                user = u
        if user:
            hashed_password = user.Account.get("Password").encode('utf-8')
            is_correct = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
            accountId = user.Account.get("AccountId")
            if is_correct and id == accountId:
                messagebox.showinfo("Đăng nhập thành công", "Xin chào, bạn đã đăng nhập thành công")
                self.controller.setUser(user)
                self.on_close(self.controller)

                
        else:
            messagebox.showerror("Đăng nhập thất bại", "Tài khoản hoặc mật khẩu không đúng.")

class RegisterWindow(tk.Toplevel):
    def __init__(self,master, controller):
        super().__init__(master)
        self.controller = controller
        self.build_ui()
        controller.withdraw()
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_close(controller))

    def on_close(self, master):
        master.deiconify()
        self.destroy()

    def build_ui(self):
        label_options = {"bg": "#f0f2f5", "fg": "#333", "font": ("Times", 11)}
        entry_options = {"width": 30, "bg": "white", "bd": 1, "relief": "solid", "font": ("Times", 11)}
        
        row = 0
        self.id_error = tk.Label(self, text="", fg="red", bg="#f0f2f5", font=("Times", 8))
        self.id_error.grid(row=row, column=1, columnspan=2, sticky="w", padx=(0, 20))
        row += 1
        tk.Label(self, text="Tài Khoản:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        self.id_entry = tk.Entry(self, **entry_options)
        self.id_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        row += 1
        self.pass_error = tk.Label(self, text="", fg="red", bg="#f0f2f5", font=("Times", 8))
        self.pass_error.grid(row=row, column=1, columnspan=2, sticky="w", padx=(0, 20))
        row += 1
        tk.Label(self, text="Mật khẩu:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        self.password_entry = tk.Entry(self, show="*", **entry_options)
        self.password_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        row += 1
        self.e_error = tk.Label(self, text="", fg="red", bg="#f0f2f5", font=("Times", 8))
        self.e_error.grid(row=row, column=1, columnspan=2, sticky="w", padx=(0, 20))
        row += 1
        tk.Label(self, text="Email:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        self.email_entry = tk.Entry(self, **entry_options)
        self.email_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        row += 1
        self.sdt_error = tk.Label(self, text="", fg="red", bg="#f0f2f5", font=("Times", 8))
        self.sdt_error.grid(row=row, column=1, columnspan=2, sticky="w", padx=(0, 20))
        row += 1
        tk.Label(self, text="SĐT:", **label_options).grid(row=row, column=0, sticky="e", padx=10, pady=8)
        self.sdt_entry = tk.Entry(self, **entry_options)
        self.sdt_entry.grid(row=row, column=1, columnspan=2, padx=(0, 20), sticky="w")

        row += 1
        self.radio_var = tk.IntVar()
        radio_btn_user = tk.Radiobutton(self, text="Người dùng", variable=self.radio_var, value=1)
        radio_btn_user.grid(row=row, column=0, columnspan=2)
        radio_btn_shipper = tk.Radiobutton(self, text="Shipper", variable=self.radio_var, value=2)
        radio_btn_shipper.grid(row=row, column=2, columnspan=1)

        row += 1
        self.register_button = tk.Button(self, text="Đăng ký", command=self.register, bg="#4CAF50", fg="white", font=("Times", 11, "bold"), bd=0, padx=10, pady=5)
        self.register_button.grid(row=row, column=0, columnspan=3, pady=(15,5))
        
        row += 1
        tk.Button(self, text="Quay lại", command=lambda: self.on_close(self.controller), bg="#2196F3", fg="white", font=("Times", 11, "bold"), bd=0, padx=10, pady=5).grid(row=row, column=0, columnspan=3, pady=(0,15))

    def register(self):
        has_error = False
        self.DanhSachUsers = UserManager()
        id = self.id_entry.get()
        email = self.email_entry.get()
        sdt = self.sdt_entry.get()
        role = self.radio_var.get()

        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            self.e_error.config(text="")
        else:
            self.e_error.config(text="Email không hợp lệ")
            has_error = True

        if re.match(r'^\d{10}$', sdt):
            self.sdt_error.config(text="")
        else:
            self.sdt_error.config(text="Số điện thoại không hợp lệ")
            has_error = True

        if not id:
            self.id_error.config(text="Vui lòng nhập tài khoản")
            has_error = True
        else:
            self.id_error.config(text="")
        password = self.password_entry.get()
        if not password:
            self.pass_error.config(text="Vui lòng điền mật khẩu")
            has_error = True
        else:
            self.pass_error.config(text="")
        for u in self.DanhSachUsers.Users:
            ac = u.Account
            if ac.get("AccountId") == id:
                self.id_error.config(text=f"Tài khoản {id} đã tồn tại")
                has_error = True
                break
        if not role:
            messagebox.showerror("Lỗi", "Vui lòng chọn vai trò")
            has_error = True
        
       
        if not has_error:
            self.DanhSachUsers.ThemUser(id, password, email, sdt, role)
            messagebox.showwarning("Thông báo", "Đăng kí thành công!")
            self.id_entry.delete(0,tk.END)
            self.password_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.sdt_entry.delete(0, tk.END)
