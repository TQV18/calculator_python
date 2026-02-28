import customtkinter as ctk

class GUI():
    def __init__(self):
        #call the LOGIC class
        self.LG = LOGIC(self, "")
        #configure the basic setting
        self.app = ctk.CTk() 
        self.app.configure(fg_color = self.hex_converter(38, 41, 46))
        self.app.resizable(False, False) # disabled window resizing
        self.app.geometry("325x500") #set the fixed window size
        self.app.title("Calculator") # set the title
        #run and setting up the system
        self.create_widget()
        self.entry_box.configure(state = "disabled") #only button is allowed, not typing
         
    def hex_converter(self, r, g, b): #convert RGB to hex
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def run(self):
        self.app.mainloop()

    def create_widget(self):
        self.entry_box = ctk.CTkEntry(self.app, width = 305, height = 80, font = ("Arial", 18)) #display screen
        self.entry_box.place(x=10, y=30)
        
        self.button_OFF = ctk.CTkButton(self.app, text = "OFF", text_color = "white", width = 75, height = 60, fg_color = "#505050", command=self.LG.quit)
        self.button_OFF.place(x=5, y=140)

        self.button_clear = ctk.CTkButton(self.app, text = "C", text_color="white", width = 75, height = 60, fg_color = "#505050", command=self.LG.clear)
        self.button_clear.place(x=85, y=140)

        self.button_delete = ctk.CTkButton(self.app, text="⌫", text_color="white", width = 75, height = 60, fg_color = "#505050", command=self.LG.delete)
        self.button_delete.place(x=165, y=140)

        self.button_divide = ctk.CTkButton(self.app, text = "/", text_color="white", width = 75, height=60, fg_color = "#505050", command=lambda:self.LG.add('/'))
        self.button_divide.place(x=245, y=140)

        self.button_7 = ctk.CTkButton(self.app, text="7", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('7'))
        self.button_7.place(x=5, y=210)

        self.button_8 = ctk.CTkButton(self.app, text="8", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('8'))
        self.button_8.place(x=85, y=210)

        self.button_9 = ctk.CTkButton(self.app, text="9", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('9'))
        self.button_9.place(x=165, y=210)

        self.button_multiply = ctk.CTkButton(self.app, text="X", text_color="white", height=60, width=75, fg_color = "#505050", command=lambda:self.LG.add('*'))
        self.button_multiply.place(x=245, y=210)

        self.button_4 = ctk.CTkButton(self.app, text="4", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('4'))
        self.button_4.place(x=5, y=280)

        self.button_5 = ctk.CTkButton(self.app, text="5", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('5'))
        self.button_5.place(x=85, y=280)

        self.button_6 = ctk.CTkButton(self.app, text="6", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('6'))
        self.button_6.place(x=165, y=280)

        self.button_minus = ctk.CTkButton(self.app, text="_", text_color="white", height=60, width=75, fg_color = "#505050", command=lambda:self.LG.add('-'))
        self.button_minus.place(x=245, y=280)

        self.button_1 = ctk.CTkButton(self.app, text="1", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('1'))
        self.button_1.place(x=5, y=350)

        self.button_2 = ctk.CTkButton(self.app, text="2", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('2'))
        self.button_2.place(x=85, y=350)

        self.button_3 = ctk.CTkButton(self.app, text="3", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('3'))
        self.button_3.place(x=165, y=350)

        self.button_plus = ctk.CTkButton(self.app, text="+", text_color="white", height=60, width=75, fg_color = "#505050", command=lambda:self.LG.add('+'))
        self.button_plus.place(x=245, y=350)

        self.button_percentage = ctk.CTkButton(self.app, text="%", text_color="white", height=60, width=75, fg_color = "#505050", command=lambda:self.LG.add('%')) 
        self.button_percentage.place(x=5, y=420)

        self.button_0 = ctk.CTkButton(self.app, text="0", text_color="white", height=60, width=75, fg_color = "#6e6e6e", command=lambda:self.LG.add('0'))
        self.button_0.place(x=85, y=420)

        self.button_point = ctk.CTkButton(self.app, text=".", text_color="white", height=60, width=75, fg_color = "#505050", command=lambda:self.LG.add('.'))
        self.button_point.place(x=165, y=420)

        self.button_equal = ctk.CTkButton(self.app, text="=", text_color="white", height=60, width=75, fg_color = "#505050", command=self.LG.calculate)
        self.button_equal.place(x=245, y=420)


class LOGIC:
    def __init__(self, gui, expression):
        self.expression = expression
        self.gui = gui
    def process(self, expression):
        temp = "" 
        ans = ""
        for ch in expression:
            if ch in "0123456789.%":
                temp += ch
            else:
                if temp:
                    if temp[-1] == '%':
                        temp = float(temp[:-1])/100
                        if float(temp) == int(temp):
                            temp = int(temp)
                    
                    ans += str(int(temp))
                    temp = ""
                    
                    
                ans += ch
        
                    
        if temp:
            if temp[-1] == '%':
                temp = float(temp[:-1])/100
                if float(temp) == int(temp):
                    temp = int(temp)
            ans += str(int(temp))
            temp = ""
        print(ans)
        return ans 
    def update_entry_box(self, val):
        self.gui.entry_box.configure(state = "normal") #allow changing data in the entry_box
        self.gui.entry_box.delete(0, "end") #clear all data in the entry_box
        self.gui.entry_box.insert("end", val) #add new data into it (new expression)
        self.gui.entry_box.configure(state = "disabled") #disabled changing data
    def add(self, num):
        self.expression += str(num)
        self.update_entry_box(self.expression)
    
    def calculate(self):
        #data = self.expression
        data = self.process(self.expression)
        try:
            res = eval(data)
            self.expression = str(res)
            self.update_entry_box(self.expression)
        except:
            self.expression = ""
            self.update_entry_box("Error!")

    def delete(self):
        self.expression = self.expression[:-1] #using slice method to remove the last element in an expression
        self.update_entry_box(self.expression)

    def clear(self):
        self.expression = ""
        self.update_entry_box(self.expression)

    def quit(self):
        self.gui.app.quit()
    


#  *The calculating engine is being updated ^^*
# ----------------------- #
class calc_engine:
    def __init__(self, expression):
        self.expression = expression
    def parse(self):
        pass
    def evaluate(self):
        pass
# ------------------------#
calcUI = GUI()
calcUI.run() #activate the GUI


