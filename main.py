from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    rand_letters = [choice(letters) for letter in range(randint(8, 10))]
    rand_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    rand_nums = [choice(numbers) for num in range(randint(2, 4))]

    password_list = rand_letters + rand_symbols + rand_nums

    shuffle(password_list)

    password = ''.join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = website_entry.get()
    email_user = email_username_entry.get()
    pword = password_entry.get()
    save_data_entry = f'{web} | {email_user} | {pword} \n'
    new_data = {
        web: {
            'email': email_user,
            'password': pword
        }
    }

    if len(web) < 1 or len(pword) < 1:
        messagebox.showerror(title='Empty field', message='Please do not leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title='website name', message=f'These are the details entered: \nWebsite: {web} \nEmail: {email_user} \n'
                                                    f'Password: {pword} \n Is it ok to save?')
        if is_ok:
            try:
                with open('data.json', mode='r') as file:
                    data = json.load(file) #Reading old data
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data) #Updating old data with new data

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4) #Saving updated data
            finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # print("Search button pressed.")
    with open('data.json') as file:
        data = json.load(file)
        # print(type(data))
        # print(data)
        search = website_entry.get()
        if search in data:
            # print(f"Website: {website}")
            # print(f"Email: {data[website]['email']}")
            # print(f"Password: {data[website]['password']}")
            messagebox.showinfo(message = f"Website: {search}\n Email: {data[search]['email']}\n Password: {data[search]['password']}")
        else:
            messagebox.showerror(message = "No details for the website exist!")

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

website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=37)
email_username_entry.insert(0, 'example@email.com')
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_pword_button = Button(text='Generate Password', command=gen_pword)
generate_pword_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()