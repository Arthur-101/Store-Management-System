from customtkinter import *
from PIL import Image
import os

class EmployeeWindow:
    def __init__(self, master, back_callback):
        self.master = master
        self.back_callback = back_callback  # Callback to be called when back button is clicked

        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        self.master.title('Employee')

        bg_path = os.getcwd() + "\\backgrounds\\bg_employee.png"
        bill_path = os.getcwd() + "\\logos\\bill.png"
        supp_path = os.getcwd() + "\\logos\\supplier.png"
        pro_path = os.getcwd() + "\\logos\\product.png"
        back_path = os.getcwd() + "\\logos\\back.png"

        self.bg = CTkImage(dark_image=Image.open(bg_path), size=(window_width, window_height))
        self.bill = CTkImage(dark_image=Image.open(bill_path), size=(120, 120))
        self.supplier = CTkImage(dark_image=Image.open(supp_path), size=(110, 110))
        self.product = CTkImage(dark_image=Image.open(pro_path), size=(100, 100))
        self.back = CTkImage(dark_image=Image.open(back_path), size=(70, 60))

        self.label = CTkLabel(self.master,text="",image=self.bg)
        self.label.place(x=0,y=0)

        self.Billing_btn = CTkButton(self.master, image=self.bill, text="Billing", corner_radius=3,fg_color='white',
            anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='top',hover_color='#b7b7b7', command=self.show_billing)
        self.Billing_btn.place(relx=0.43, rely=0.28, relwidth=0.15, relheight=0.22)

        self.proinfo_btn = CTkButton(self.master, image=self.product, corner_radius=3,fg_color='white',text="Product Info",
            anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='top',hover_color='#b7b7b7', command=self.show_product_info)
        self.proinfo_btn.place(relx=0.23, rely=0.5, relwidth=0.12, relheight=0.17)

        self.Supplier_btn = CTkButton(self.master, image=self.supplier, corner_radius=3,fg_color='white',text="Supplier Info",
            anchor='s',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='top',hover_color='#b7b7b7', command=self.show_supplier_info)
        self.Supplier_btn.place(relx=0.675, rely=0.5, relwidth=0.12, relheight=0.17)

        self.back_btn = CTkButton(self.master, image=self.back, corner_radius=7,fg_color='white',text="Back",
            anchor='e',text_color='#5C243C',font=('poppins',13,'bold'),border_color='white',border_width=1,
            compound='left',hover_color='#b7b7b7', command=self.back_to_main)
        self.back_btn.place(relx=0.05, rely=0.9, relwidth=0.11, relheight=0.07)

    def show_billing(self):
        pass

    def show_product_info(self):
        pass

    def show_supplier_info(self):
        pass

    def back_to_main(self):
        # Calling the callback function to go back to the main window
        if self.back_callback:
            self.back_callback()
