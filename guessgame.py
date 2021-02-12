import random
from tkinter import*
from tkinter import messagebox
count = 0

def fun():
    x = w.get()
    x = int(x)
    global count
    if x>rand:
        count+=1
        messagebox.showinfo("Info","Number is Greater")
        w.delete(0, END)

    elif x<rand:
        count+=1
        messagebox.showinfo("info name","Number is lesser")
        w.delete(0, END)


    else:
        p = "You guessed the correct value" +str(rand)+" in "+str(count)+" time"
        messagebox.showinfo("info name",p)





if __name__=="__main__":
    rand = random.randint(1,100)
    m = Tk()

    m.geometry("200x250")
    m.title("Guessing game")
    l = Label(m,text ="Enter your guess")
    l.pack()
    w = Entry(m)
    w.pack()
    b = Button(m,text="Go",command = fun)
    b.pack()
    m.mainloop()

    """
    rand = random.randint(1,100)

    inp = int(input("Enter the number:"))
    count = 0
    while inp!=rand:

        if inp>rand:
            print("Your guess is larger")
            count+=1
            inp = int(input("Enter the number:"))

        elif inp<rand:
            print("Your guess is smaller")
            count+=1
            inp = int(input("Enter the number:"))



        print("You guessed correctly", inp)
        print(count)
    """



