from tkinter import *


from future.moves.tkinter import messagebox


def Cal():
    try:
        if int(en_Amount.get()) < 3000:
            messagebox.showerror("STATUS FEEDBACK", "You do not qualify to go to Malaysia")
        else:
            messagebox.showinfo("STATUS FEEDBACK", "Congratulations. You qualify to go to Malaysia")
    except:
        messagebox.showerror("Error", "Please make sure you put in an integer")


def ex():
    mess = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if mess == 'yes':
        Amount.destroy()


# Window Start
Amount = Tk()
Amount.title("Exception Handling")
Amount.geometry("550x300")
Amount["bg"] = "blue"

# Heading start
lbl_Heading = Label(Amount, text="Please enter amount in your account", bg="blue")
lbl_Heading["font"] = "Arial", 20
lbl_Heading.place(x=50, y=50)
# Heading end

# Amount start
en_Amount = Entry(Amount)
en_Amount["font"] = "Arial", 20
en_Amount.place(x=170, y=100, width=200)
# Amount end

# Cal start
btn_Cal = Button(Amount, text="Calculate", command=Cal)
btn_Cal["font"] = "Arial", 20
btn_Cal.place(x=50, y=150, width=200)
# Cal end

# Exit start
btn_Exit = Button(Amount, text="Exit", command=ex)
btn_Exit["font"] = "Arial", 20
btn_Exit.place(x=300, y=150, width=200)
# Exit end

Amount.mainloop()
# Window End
