from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = website_entry.get()
    email_user = email_username_entry.get()
    pword = password_entry.get()
    save_data_entry = f'{web} | {email_user} | {pword} \n'

    with open('data.txt', mode='a') as file:
        file.write(save_data_entry)
        website_entry.delete(0, END)
        # email_username_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.insert(0, 'example@email.com')
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_pword_button = Button(text='Generate Password')
generate_pword_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()