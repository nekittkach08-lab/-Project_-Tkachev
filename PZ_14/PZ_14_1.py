#https://files.codegrape.com/62259/screenshot2.png

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Contact Form")
root.geometry("500x600")
root.configure(bg="white")


# Функция подсказки
def add_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="gray")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


# Заголовок
Label(root, text="Contact Form",
      font=("Arial", 24),
      bg="white").pack(pady=20)

# Name
Label(root, text="Name *", bg="white").pack(anchor="w", padx=30)

name = Entry(root, width=50)
name.pack(pady=5)
add_placeholder(name, "First & Last Name")

# Email
Label(root, text="Email *", bg="white").pack(anchor="w", padx=30)

email = Entry(root, width=50)
email.pack(pady=5)
add_placeholder(email, "Email")

# Phone
Label(root, text="Phone Number *", bg="white").pack(anchor="w", padx=30)

phone = Entry(root, width=50)
phone.pack(pady=5)
add_placeholder(phone, "Phone Number")

# Subject
Label(root, text="Subject *", bg="white").pack(anchor="w", padx=30)

combo = ttk.Combobox(root, values=[
    "Support",
    "Question",
    "Feedback"
])

combo.pack(pady=5)
combo.set("Select Subject")

# Message
Label(root, text="Message *", bg="white").pack(anchor="w", padx=30)

text = Text(root, width=40, height=8)
text.pack(pady=5)

# Checkbox
Checkbutton(root,
            text="I'm not a robot",
            bg="white").pack(pady=15)

# Button
Button(root,
       text="Submit",
       bg="blue",
       fg="white",
       padx=20,
       pady=5).pack()

root.mainloop()