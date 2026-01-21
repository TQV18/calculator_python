import customtkinter as ctk
app = ctk.CTk()
#processing function
def process(strs):
    temp = ""
    ans = "" 
    #processing in strs
    for i in strs:
        if i in "0123456789.%":
            temp += i
        else:
            if temp:
                if temp[len(temp)-1] == '%':
                    temp = float(temp[:-1])/100
                    if float(temp) == int(temp):
                        temp = int(temp)
                    temp = str(temp)
                ans += temp
                temp = ""
                ans += i
    #processing at the end of strs
    if temp:
        if temp[len(temp)-1] == '%':
            temp = float(temp[:-1])/100
            if float(temp) == int(temp):
                temp = int(temp)
            temp = str(temp)
        ans += temp
        temp = ""
    return ans
def enter(nums):
    entry_box.configure(state="normal")# enable the changing text permission
    if nums == "=":
        try:    
            data = entry_box.get()
            res = eval(process(data))
            entry_box.delete(0, "end")
            entry_box.insert(0, res)
        except: #preventing crashing if error appears
            entry_box.delete(0, "end")
            entry_box.insert(0, "Error")
    elif nums == "C":#clear all data in the entry_box
        entry_box.delete(0, "end")
        entry_box.insert(0, "")
    elif nums == "del":#delete the last element in the entry_box
        S = entry_box.get()
        S = S[:-1]
        entry_box.delete(0, "end")
        entry_box.insert(0, S)
    else:
        entry_box.insert("end", str(nums))
    entry_box.configure(state = "disable") # disable the changing text permission

#out function
def out():
    app.quit()
#introduce 
#width = 75 height = 75

def hex_converter(R, G, B):
    return f'#{R:02x}{G:02x}{B:02x}'
hcs = hex_converter(255, 182, 193)
entry_box = ctk.CTkEntry(app, width = 305, height = 80, font = ("Arial", 18))
entry_box.place(x=10, y=30)

button_OFF = ctk.CTkButton(app, text = "OFF", text_color = "white", width = 75, height = 60, command=out, fg_color = "#505050")
button_OFF.place(x=5, y=140)

button_clear = ctk.CTkButton(app, text = "C", text_color="white", width = 75, height = 60, command=lambda:enter("C"), fg_color = "#505050")
button_clear.place(x=85, y=140)

button_delete = ctk.CTkButton(app, text="⌫", text_color="white", width = 75, height = 60, command=lambda:enter("del"), fg_color = "#505050")
button_delete.place(x=165, y=140)

button_divide = ctk.CTkButton(app, text = "/", text_color="white", width = 75, height=60, command=lambda:enter("/"), fg_color = "#505050")
button_divide.place(x=245, y=140)

button_7 = ctk.CTkButton(app, text="7", text_color="white", height=60, width=75, command=lambda:enter(7), fg_color = "#6e6e6e")
button_7.place(x=5, y=210)

button_8 = ctk.CTkButton(app, text="8", text_color="white", height=60, width=75, command=lambda:enter(8), fg_color = "#6e6e6e")
button_8.place(x=85, y=210)

button_9 = ctk.CTkButton(app, text="9", text_color="white", height=60, width=75, command=lambda:enter(9), fg_color = "#6e6e6e")
button_9.place(x=165, y=210)

button_multiply = ctk.CTkButton(app, text="X", text_color="white", height=60, width=75, command=lambda:enter("*"), fg_color = "#505050")
button_multiply.place(x=245, y=210)

button_4 = ctk.CTkButton(app, text="4", text_color="white", height=60, width=75, command=lambda:enter(4), fg_color = "#6e6e6e")
button_4.place(x=5, y=280)

button_5 = ctk.CTkButton(app, text="5", text_color="white", height=60, width=75, command=lambda:enter(5), fg_color = "#6e6e6e")
button_5.place(x=85, y=280)

button_6 = ctk.CTkButton(app, text="6", text_color="white", height=60, width=75, command=lambda:enter(6), fg_color = "#6e6e6e")
button_6.place(x=165, y=280)

button_minus = ctk.CTkButton(app, text="_", text_color="white", height=60, width=75, command=lambda:enter("-"), fg_color = "#505050")
button_minus.place(x=245, y=280)

button_1 = ctk.CTkButton(app, text="1", text_color="white", height=60, width=75, command=lambda:enter(1), fg_color = "#6e6e6e")
button_1.place(x=5, y=350)

button_2 = ctk.CTkButton(app, text="2", text_color="white", height=60, width=75, command=lambda:enter(2), fg_color = "#6e6e6e")
button_2.place(x=85, y=350)

button_3 = ctk.CTkButton(app, text="3", text_color="white", height=60, width=75, command=lambda:enter(3), fg_color = "#6e6e6e")
button_3.place(x=165, y=350)

button_plus = ctk.CTkButton(app, text="+", text_color="white", height=60, width=75, command=lambda:enter("+"), fg_color = "#505050")
button_plus.place(x=245, y=350)

button_percentage = ctk.CTkButton(app, text="%", text_color="white", height=60, width=75, fg_color = "#505050", command=lambda:enter("%")) 
button_percentage.place(x=5, y=420)

button_0 = ctk.CTkButton(app, text="0", text_color="white", height=60, width=75, command=lambda:enter(0), fg_color = "#6e6e6e")
button_0.place(x=85, y=420)

button_point = ctk.CTkButton(app, text=".", text_color="white", height=60, width=75, command=lambda:enter("."), fg_color = "#505050")
button_point.place(x=165, y=420)

button_equal = ctk.CTkButton(app, text="=", text_color="white", height=60, width=75, command=lambda:enter("="), fg_color = "#505050")
button_equal.place(x=245, y=420)
#app setting
def convert_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
rgb_color = 38, 41, 46
ctk.set_appearance_mode("dark")
entry_box.configure(state = "disable")
app.configure(fg_color = convert_to_hex(*rgb_color))
app.resizable(False, False)
app.geometry("325x500")
app.title("Calculator=)))")
app.mainloop() 
