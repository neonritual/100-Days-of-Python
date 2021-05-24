import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    f = open("password_list.txt", "a")
    f.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()} \n")
    f.close()
    print("hej")
    print(website_input.get())

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg="white")

#Canvas and BG image
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=2)

#Website Row
website_label = tk.Label(text="Website: ")
website_label.grid(row=2, column=1)
website = ""
website_input = tk.Entry(width=35, textvariable=website)
website_input.grid(row=2, column=2, columnspan=2)
website_input.focus() #puts cursor in the website field

#Username Row
username_label = tk.Label(text="Email/Username: ")
username_label.grid(row=3, column=1)
username = ""
username_input = tk.Entry(width=35, textvariable=username)
username_input.grid(row=3, column=2, columnspan=2)
username_input.insert(0, "myemail@email.com") #populates username field with this.

#Password Row
password_label = tk.Label(text="Password: ")
password_label.grid(row=4, column=1)
password = ""
password_input = tk.Entry(width=21, textvariable=password)
password_input.grid(row=4, column=2)

password_gen_button = tk.Button(text="Generate Password", command=None)
password_gen_button.grid(row=4, column=3)

#Add Button
add_password = tk.Button(text="Add", width=36, command=save)
add_password.grid(row=5, column=2, columnspan=2)






window.mainloop()