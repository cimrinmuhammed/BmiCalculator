from tkinter import *

window = Tk()
window.minsize(width=250,height=300)
window.config(padx=20,pady=20)
window.title("Bmı Calculator")


def calculator_bmi():
    weight = kg_text.get()
    height = size_text.get()

    if weight == "" or height == "":
        result_label.config(text="Boş geçmeyiniz !")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)

        except:
            result_label.config(text="Sadece rakam giriniz !")


    if bmi <= 18.5:
        result_label.config(text=f"Zayıfsınız {bmi:.2f}")

    elif bmi >18.5 and bmi <=24.9:
        result_label.config(text=f"Normal {bmi:.2f}")

    elif bmi >24.9 and bmi <=29.9:
        result_label.config(text=f"Fazla Kilolu {bmi:.2f}")

    else:
        result_label.config(text=f"Obezsiniz {bmi:.2f}")



#KG :
kg_label = Label(text="Kilonuzu giriniz (Kg) ")
kg_label.pack()
kg_text = Entry()
kg_text.pack()

#SİZE
size_label =Label(text="Boyunuzu Giriniz(Cm)")
size_label.pack()
size_text = Entry()
size_text.pack()

result_label = Label()
result_label.pack()



calculate_button = Button(text="Hesapla",pady=10,padx=10,command=calculator_bmi)
calculate_button.pack()

window.mainloop()