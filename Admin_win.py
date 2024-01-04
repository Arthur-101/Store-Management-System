from customtkinter import *
from PIL import Image
import os
from add_product_win import AddProductWindow

class AdminWindow():
    def __init__(self, master, back_callback):
        self.master = master
        self.back_callback = back_callback  # Callback to be called when back button is clicked

        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        self.master.title('Admin')

        bg_path = os.getcwd()+"\\backgrounds\\bg_admin.png"
        bill_path = os.getcwd()+"\\logos\\bill.png"
        supp_path = os.getcwd()+"\\logos\\supplier.png"
        pro_path = os.getcwd()+"\\logos\\product.png"
        add_pro_path = os.getcwd()+"\\logos\\add-product.png"
        add_pro_ID_path = os.getcwd()+"\\logos\\add-product-id.png"
        supp_ID_path = os.getcwd()+"\\logos\\add-supplier-id.png"
        add_employee_path = os.getcwd()+"\\logos\\employee-2.png"
        back_path = os.getcwd() + "\\logos\\back.png"

        self.bg = CTkImage(dark_image=Image.open(bg_path),size=(window_width,window_height))
        self.bill = CTkImage(dark_image=Image.open(bill_path),size=(90,90))
        self.supplier = CTkImage(dark_image=Image.open(supp_path),size=(90,90))
        self.product = CTkImage(dark_image=Image.open(pro_path),size=(90,90))
        self.add_product = CTkImage(dark_image=Image.open(add_pro_path),size=(90,90))
        self.add_product_ID = CTkImage(dark_image=Image.open(add_pro_ID_path),size=(90,90))
        self.supplier_ID = CTkImage(dark_image=Image.open(supp_ID_path),size=(90,90))
        self.add_employee = CTkImage(dark_image=Image.open(add_employee_path),size=(90,90))
        self.back = CTkImage(dark_image=Image.open(back_path), size=(70, 60))

        self.label = CTkLabel(self.master,text="",image=self.bg)
        self.label.place(x=0,y=0)

        self.Billing_btn = CTkButton(self.master,image=self.bill,corner_radius=3,fg_color='white',text="Billing",anchor='s',
            text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,compound='top',
            hover_color='#b7b7b7')
        self.Billing_btn.place(relx=0.23, rely=0.28, relwidth=0.125, relheight=0.175)

        self.proinfo_btn = CTkButton(self.master,image=self.product,corner_radius=3,fg_color='white',text="Product Info",
            anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='top',hover_color='#b7b7b7')
        self.proinfo_btn.place(relx=0.46, rely=0.28, relwidth=0.125, relheight=0.175)

        self.Supplier_btn = CTkButton(self.master,image=self.supplier,corner_radius=3,fg_color='white',text="Supplier Info",
            anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='top',hover_color='#b7b7b7')
        self.Supplier_btn.place(relx=0.69, rely=0.28, relwidth=0.125, relheight=0.175)

        self.add_product_btn = CTkButton(self.master,image=self.add_product,corner_radius=3,fg_color='white',
            text="Add Product",anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',
            border_width=1,compound='top',hover_color='#b7b7b7', command=self.show_add_product)
        self.add_product_btn.place(relx=0.23, rely=0.53, relwidth=0.125, relheight=0.175)

        self.add_product_ID_btn = CTkButton(self.master,image=self.add_product_ID,corner_radius=3,fg_color='white',
            text="Add Product ID",anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',
            border_width=1,compound='top',hover_color='#b7b7b7')
        self.add_product_ID_btn.place(relx=0.46, rely=0.53, relwidth=0.125, relheight=0.175)

        self.Supplier_ID_btn = CTkButton(self.master,image=self.supplier_ID,corner_radius=3,fg_color='white',
            text="Add Supplier ID",anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',
            border_width=1,compound='top',hover_color='#b7b7b7')
        self.Supplier_ID_btn.place(relx=0.69, rely=0.53, relwidth=0.125, relheight=0.175)

        self.add_employee_btn = CTkButton(self.master,image=self.add_employee,corner_radius=3,fg_color='white',
            text="Employee",anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',
            border_width=1,compound='top',hover_color='#b7b7b7')
        self.add_employee_btn.place(relx=0.46, rely=0.78, relwidth=0.125, relheight=0.175)

        self.back_btn = CTkButton(self.master, image=self.back, corner_radius=7,fg_color='white',text="Back",
            anchor='e',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='left',hover_color='#b7b7b7', command=self.back_to_main)
        self.back_btn.place(relx=0.05, rely=0.9, relwidth=0.11, relheight=0.07)

    def show_admin_win(self):
        # Recreating the admin window widgets
        self.__init__(self.master, self.back_callback)

    def show_billing(self):
        pass

    def show_product_info(self):
        pass

    def show_supplier_info(self):
        pass

    def show_add_product(self):
        # Clearing existing widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        # Creating an instance of EmployeeWindow
        admin_win = AddProductWindow(self.master, self.show_admin_win)

    def show_add_product_id(self):
        pass

    def show_add_supplier_id(self):
        pass

    def show_employee_win(self):
        pass

    def back_to_main(self):
        # Calling the callback function to go back to the main window
        if self.back_callback:
            self.back_callback()
    
   

