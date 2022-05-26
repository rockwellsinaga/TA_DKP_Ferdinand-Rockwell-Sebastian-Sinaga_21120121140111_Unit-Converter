from tkinter import *

root = Tk()
root.title("Unit Converter")

Units = ['meter' , 'foot' , 'yard' , 'inch']
menu = StringVar()
menu.set("From")

dropmenu1 = OptionMenu(root , menu , *Units)
dropmenu1.grid(row=1 , column=1)

menu2 = StringVar()
menu2.set("To")

dropmenu2 = OptionMenu(root , menu2, *Units)
dropmenu2.grid(row=1 , column=2)

input = Entry(root,font=(20))
input.grid(row=2, column=1)

output = Label(root,width = 20,borderwidth=3 , relief="solid")
output.grid(row=2 , column=2)

def Clear():
    input.delete(0,"end")
    output.config(text = "")

def Convert():
    
    unit1 = menu.get()
    unit2 = menu2.get()

    try:
        num = float(input.get())
        converted_num = num
        if unit1 == 'meter' and unit2 == 'foot':
            converted_num = num*3.281

        elif unit1 == 'meter' and unit2 == 'yard':
            converted_num = num*1.094
        
        elif unit1 == 'meter' and unit2 == 'inch':
            converted_num = num*39.37
            
        elif unit1 == 'foot' and unit2 == 'meter':
            converted_num = num/3.281
            
        elif unit1 == 'foot' and unit2 == 'yard':
            converted_num = num/3
        
        elif unit1 == 'foot' and unit2 == 'inch':
            converted_num = num*12

        elif unit1 == 'yard' and unit2 == 'meter':
            converted_num = num/1.094
            
        elif unit1 == 'yard' and unit2 == 'foot':
            converted_num = num*3
        
        elif unit1 == 'yard' and unit2 == 'inch':
            converted_num = num*36
            
        elif unit1 == 'inch' and unit2 == 'meter':
            converted_num = num/39.37
            
        elif unit1 == 'inch' and unit2 == 'foot':
            converted_num = num/12
        
        elif unit1 == 'inch' and unit2 == 'yard':
            converted_num = num/36
        
        output.config(text=str(converted_num))
    except:
        output.config(text="Invalid")

b_convert = Button(root , text = "Convert",command = Convert)
b_convert.grid(row=3 , column=1)

b_clear = Button(root, text="Clear" , command=Clear)
b_clear.grid(row=3,column=2)

root.mainloop()