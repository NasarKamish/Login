from tkinter import *

from future.moves.tkinter import messagebox


def ex():
    mess = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if mess == 'yes':
        Login.destroy()


def verify():
    for key, value in Logins.items():
        if en_username.get() == key and en_password.get() == value:
            Login.destroy()
            import Amount
        else:
            messagebox.showerror("Error", "Incorrect Password or UserName")


# Logins
Logins = {"Test": "123", "Person": "Secure", "Steve": "Fox", "Skrtel": "Dultchi"}

# window start
Login = Tk()
Login.title("Verify Form")
Login.geometry("700x300")
Login.config(bg="blue")

# Heading Start
lbl_Heading = Label(Login, text="Please Enter Login Details", bg="blue")
lbl_Heading["font"] = "Arial", 20
lbl_Heading.place(x=100, y=10)
# Heading End

# Username start
lbl_username = Label(Login, text="Please enter username:", bg="blue")
lbl_username["font"] = "Arial", 15
lbl_username.place(x=50, y=100)

en_username = Entry(Login)
en_username["font"] = "Arial", 15
en_username.place(x=350, y=100, width=300)
# Username end

# Password start
lbl_password = Label(Login, text="Please enter password:", bg="blue")
lbl_password["font"] = "Arial", 15
lbl_password.place(x=50, y=150)

en_password = Entry(Login)
en_password["font"] = "Arial", 15
en_password.place(x=350, y=150, width=300)
# Password end

# Button Group Start
btn_Verify = Button(Login, text="Verify", bg="White", command=verify)
btn_Verify["font"] = "Arial", 15
btn_Verify.place(x=50, y=200, width=200)

btn_Exit = Button(Login, text="Exit", bg="white", command=ex)
btn_Exit["font"] = "Arial", 15
btn_Exit.place(x=450, y=200, width=200)
# Button Group End

Login.mainloop()
# window end
