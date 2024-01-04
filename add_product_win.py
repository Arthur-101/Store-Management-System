from customtkinter import *
from PIL import Image
import os

class AddProductWindow:
    def __init__(self, master, back_callback):
        self.master = master
        self.back_callback = back_callback  # Callback to be called when back button is clicked

        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        self.master.title('Add Product')
        
        bg_path = os.getcwd()+"\\backgrounds\\bg_product_details.png"
        bck_img_path = os.getcwd()+"\\logos\\back.png"
        clr_img_path = os.getcwd()+"\\logos\\clear.png"
        add_img_path = os.getcwd()+"\\logos\\add.png"
        
        self.bg = CTkImage(dark_image=Image.open(bg_path),size=(window_width,window_height))
        self.bck_img = CTkImage(dark_image=Image.open(bck_img_path), size=(60, 50))
        self.clr_img = CTkImage(dark_image=Image.open(clr_img_path), size=(60, 50))
        self.add_img = CTkImage(dark_image=Image.open(add_img_path), size=(60, 50))

        self.label = CTkLabel(self.master,text="",image=self.bg)
        self.label.place(x=0,y=0)#
        
        #####  BATCH FRAME
        self.frame1 = CTkFrame(self.master)
        self.frame1.place(relx=0.15,rely=0.12,relheight=0.08,relwidth=0.7)

        self.batch_no_label = CTkLabel(self.frame1,text='Batch no :',font=('seoge ui',25))
        self.batch_no_label.place(relx=0.02,rely=0.2,)

        self.batch_no_entry = CTkEntry(self.frame1, placeholder_text='xxxxxxxx', font=('candara',18))
        self.batch_no_entry.place(relx=0.15,rely=0.1,relheight=0.70,relwidth=0.3)

        self.batch_date_lable = CTkLabel(self.frame1,text='Batch date :',font=('seoge ui',25))
        self.batch_date_lable.place(relx=0.51,rely=0.2,)

        self.batch_date_entry = CTkEntry(self.frame1, placeholder_text='yyyy-mm-dd', font=('candara',18))
        self.batch_date_entry.place(relx=0.67,rely=0.1,relheight=0.70,relwidth=0.3)

        ######  PRODUCT FRAME
        self.frame2 = CTkFrame(self.master)
        self.frame2.place(relx=0.15,rely=0.21,relheight=0.35,relwidth=0.7)

        self.product_name_label= CTkLabel(self.frame2,text="Product Name :",text_color='white',font=('verdana',20))
        self.product_name_label.place(relx=0.02,rely=0.05,)

        self.product_name_entry= CTkEntry(self.frame2,placeholder_text="Name of the product", font=('candara',18))
        self.product_name_entry.place(relx=0.2,rely=0.05,relheight=0.15,relwidth=0.45)

        self.quantity_label = CTkLabel(self.frame2,text='Quanity :',text_color='white',font=('verdana',20))
        self.quantity_label.place(relx=0.67,rely=0.06,)

        self.quantity_entry = CTkEntry(self.frame2,placeholder_text="W/V/etc.", font=('candara',18))
        self.quantity_entry.place(relx=0.78,rely=0.05,relheight=0.15,relwidth=0.08)

        self.quantity_list=['gms','kg','pcs','litre','ml','other']
        self.quantity_option = CTkOptionMenu(self.frame2,fg_color='#6C3756',values=self.quantity_list,button_color='#5C243C',dropdown_fg_color='#792746',dropdown_hover_color='#5C243C')
        self.quantity_option.place(relx=0.87,rely=0.05,relheight=0.15,relwidth=0.1)

        self.brand_label = CTkLabel(self.frame2,text='Brand :',text_color='white',font=('verdana',20))
        self.brand_label.place(relx=0.02,rely=0.23,)

        self.brand_entry = CTkEntry(self.frame2,placeholder_text="Name of the Brand", font=('candara',18))
        self.brand_entry.place(relx=0.11,rely=0.23,relheight=0.15,relwidth=0.4)

        self.cat_option_label= CTkLabel(self.frame2,text='Category :',text_color='white',font=('verdana',20))
        self.cat_option_label.place(relx=0.54,rely=0.24,)

        self.cat_list = ['Dairy','Snacks','Staples','Beverages','Bakery','Frozen Foods','Personal Care','Stationary','other']
        self.cat_option = CTkOptionMenu(self.frame2,fg_color='#6C3756',values=self.cat_list,button_color='#5C243C',dropdown_fg_color='#792746',dropdown_hover_color='#5C243C')
        self.cat_option.place(relx=0.67,rely=0.23,relheight=0.15,relwidth=0.2)

        self.PID_label = CTkLabel(self.frame2,text="PID :",text_color='white',font=('verdana',20))
        self.PID_label.place(relx=0.02,rely=0.41,)

        self.PID_entry = CTkEntry(self.frame2,placeholder_text="Product ID", font=('candara',18))
        self.PID_entry.place(relx=0.1,rely=0.41,relheight=0.15,relwidth=0.25)

        self.cp_label = CTkLabel(self.frame2,text='Cost Price : ₹',text_color='white',font=('verdana',19))
        self.cp_label.place(relx=0.37,rely=0.42,)

        self.cp_entry = CTkEntry(self.frame2,placeholder_text="C.P.", font=('candara',18))
        self.cp_entry.place(relx=0.51,rely=0.41,relheight=0.15,relwidth=0.15)

        self.sp_label = CTkLabel(self.frame2,text='Selling Price : ₹',text_color='white',font=('verdana',19))
        self.sp_label.place(relx=0.675,rely=0.42,)

        self.sp_entry = CTkEntry(self.frame2,placeholder_text="S.P.", font=('candara',18))
        self.sp_entry.place(relx=0.84,rely=0.41,relheight=0.15,relwidth=0.15)

        self.stock_label = CTkLabel(self.frame2,text="Stock :",text_color='white',font=('verdana',20))
        self.stock_label.place(relx=0.02,rely=0.59,)

        self.stock_entry = CTkEntry(self.frame2,placeholder_text="Stock", font=('candara',18))
        self.stock_entry.place(relx=0.1,rely=0.59,relheight=0.15,relwidth=0.18)

        self.Exp_label = CTkLabel(self.frame2,text='Expiry Date :',text_color='white',font=('verdana',19))
        self.Exp_label.place(relx=0.33,rely=0.59,)

        self.Exp_entry = CTkEntry(self.frame2,placeholder_text="yyyy-mm-dd", font=('candara',18))
        self.Exp_entry.place(relx=0.48,rely=0.59,relheight=0.15,relwidth=0.18)

        self.GST_label = CTkLabel(self.frame2,text='GST :',text_color='white',font=('verdana',20))
        self.GST_label.place(relx=0.71,rely=0.6,)

        self.gst_list = ['None','5%','12%','18%','28%']
        self.GST_option = CTkOptionMenu(self.frame2,fg_color='#6C3756',values=self.gst_list,button_color='#5C243C',dropdown_fg_color='#792746',dropdown_hover_color='#5C243C')
        self.GST_option.place(relx=0.79,rely=0.59,relheight=0.15,relwidth=0.16)

        self.product_desc_label= CTkLabel(self.frame2,text="Product Desc :",text_color='white',font=('verdana',20))
        self.product_desc_label.place(relx=0.02,rely=0.77,)

        self.product_desc_entry = CTkEntry(self.frame2,placeholder_text="Any Description of the Product (Optional)", font=('candara',18))
        self.product_desc_entry.place(relx=0.19,rely=0.77,relheight=0.2,relwidth=0.77)
        
        ####  SUPPLIER FRAME
        self.frame3 = CTkFrame(self.master)
        self.frame3.place(relx=0.15,rely=0.57,relheight=0.3,relwidth=0.7)

        self.supp_label = CTkLabel(self.frame3,text="Supplier Details",text_color='white',font=('tahoma',30))
        self.supp_label.place(relx=0.4,rely=0.03,)

        self.supplier_label = CTkLabel(self.frame3,text="Supplier :",text_color='white',font=('verdana',20))
        self.supplier_label.place(relx=0.02,rely=0.25,)

        self.supplier_entry = CTkEntry(self.frame3,placeholder_text="Name of Supplier", font=('candara',18))
        self.supplier_entry.place(relx=0.14,rely=0.25,relheight=0.2,relwidth=0.4)

        self.supp_id_label = CTkLabel(self.frame3,text="Supplier ID :",text_color='white',font=('verdana',20))
        self.supp_id_label.place(relx=0.57,rely=0.25,)

        self.supp_id_entry = CTkEntry(self.frame3,placeholder_text="SID", font=('candara',18))
        self.supp_id_entry.place(relx=0.73,rely=0.25,relheight=0.2,relwidth=0.25)

        self.supplier_mobile_label = CTkLabel(self.frame3,text="Supplier Mobile :",text_color='white',font=('verdana',20))
        self.supplier_mobile_label.place(relx=0.02,rely=0.5,)

        self.supplier_mobile_entry = CTkEntry(self.frame3,placeholder_text="xxxxxxxxxx", font=('candara',18))
        self.supplier_mobile_entry.place(relx=0.21,rely=0.5,relheight=0.2,relwidth=0.23)

        self.supplier_Email_label = CTkLabel(self.frame3,text="Supplier Email :",text_color='white',font=('verdana',20))
        self.supplier_Email_label.place(relx=0.47,rely=0.5,)

        self.supplier_Email_entry = CTkEntry(self.frame3,placeholder_text="supplier123@gmail.com", font=('candara',18))
        self.supplier_Email_entry.place(relx=0.65,rely=0.5,relheight=0.2,relwidth=0.33)

        self.supp_address_label = CTkLabel(self.frame3,text="Supplier Address :",text_color='white',font=('verdana',20))
        self.supp_address_label.place(relx=0.02,rely=0.74,)

        self.supp_address_entry = CTkEntry(self.frame3,placeholder_text="Address of Supplier (Optional)", font=('candara',18))
        self.supp_address_entry.place(relx=0.22,rely=0.74,relheight=0.2,relwidth=0.76)

        #####  Buttons
        self.back_btn = CTkButton(self.master, image=self.bck_img,corner_radius=6,fg_color='white',text="Back",anchor='e',text_color='#5C243C',
            font=('poppins',14,'bold'),border_color='white',border_width=1,compound='left',hover_color='#f56c94',
            command=self.back_to_admin)
        self.back_btn.place(relx=0.2, rely=0.89, relheight=0.07, relwidt=0.1)

        self.clear_btn = CTkButton(self.master, image=self.clr_img,corner_radius=6,fg_color='white',text="Clear",anchor='e',text_color='#5C243C',
            font=('poppins',14,'bold'),border_color='white',border_width=1,compound='left',hover_color='#f56c94',
            command=self.clear_all)
        self.clear_btn.place(relx=0.45, rely=0.89, relheight=0.07, relwidt=0.1)

        self.add_btn = CTkButton(self.master, image=self.add_img,corner_radius=6,fg_color='white',text="Add",anchor='e',text_color='#5C243C',
            font=('poppins',14,'bold'),border_color='white',border_width=1,compound='left',hover_color='#f56c94',
            command=self.add_product)
        self.add_btn.place(relx=0.7, rely=0.89, relheight=0.07, relwidt=0.1)



    def back_to_admin(self):
        # Calling the callback function to go back to the main window
        if self.back_callback:
            self.back_callback()

    def clear_all(self):
        pass

    def add_product(self):
        pass

