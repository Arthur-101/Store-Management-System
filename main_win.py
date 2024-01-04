from customtkinter import *
from PIL import Image
import os
from Employee_win import EmployeeWindow
from Admin_win import AdminWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        set_appearance_mode('DARK')
        self.root.wm_state("zoomed")
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        self.root.title('Main')

        bg_img_path = os.getcwd() + "\\backgrounds\\bg_login_as.png"
        emp_img_path = os.getcwd() + "\\logos\\employee.png"
        adm_img_path = os.getcwd() + "\\logos\\admin.png"

        img_bg = CTkImage(dark_image=Image.open(bg_img_path), size=(window_width, window_height))
        img_emp = CTkImage(dark_image=Image.open(emp_img_path), size=(100, 100))
        img_adm = CTkImage(dark_image=Image.open(adm_img_path), size=(100, 100))

        label = CTkLabel(root,text="",image=img_bg)
        label.place(x=0,y=0)

        Emp_btn = CTkButton(self.root, image=img_emp, corner_radius=3,fg_color='white',text="Employee",anchor='s',text_color='#5C243C',
        font=('poppins',13,'bold'),border_color='white',border_width=1,compound='top',hover_color='#b7b7b7', command=self.show_employee_win)
        Emp_btn.place(relx=0.31, rely=0.5, relwidth=0.125, relheight=0.179)

        Adm_btn = CTkButton(self.root, image=img_adm, corner_radius=3,fg_color='white',text="Admin",anchor='s',text_color='#5C243C',
        font=('poppins',13,'bold'),border_color='white',border_width=1,compound='top',hover_color='#b7b7b7', command=self.show_admin_win)
        Adm_btn.place(relx=0.61, rely=0.5, relwidth=0.125, relheight=0.179)

    def show_employee_win(self):
        # Clearing existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Creating an instance of EmployeeWindow
        employee_win = EmployeeWindow(self.root, self.show_main_win)

    def show_main_win(self):
        # Recreating the main window widgets
        self.__init__(self.root)

    def show_admin_win(self):
        # Clearing existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        admin_win = AdminWindow(self.root, self.show_main_win)

if __name__ == "__main__":
    root = CTk()
    main_win = MainWindow(root)
    root.mainloop()
