import customtkinter as ctk

#configuração da tela e variaveis
tela = ctk.CTk()
tela.title("Calculadora")
tela.geometry("350x450")
tela.resizable(width=False, height=False)

valor_actual = ""
butoes = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+", "="],
    ["C", "±", "%", "Modo"]

]
#widgets

display = ctk.CTkEntry(tela, font=("Arial", 24), justify="right")
display.pack(padx=20, pady=20, fill="x")

btn_frame = ctk.CTkFrame(tela)
btn_frame.pack(padx=20, pady=10, fill="both", expand=True)

for i, linha in enumerate(butoes):
    for j, texto in enumerate(linha):
        btn = ctk.CTkButton(btn_frame, text=texto, font=("Arial", 18), command=lambda t=texto:on_click(t))
        btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

for i in range(len(butoes)):
    btn_frame.grid_rowconfigure(i, weight=1)
for j in range(len(butoes[0])):
    btn_frame.grid_columnconfigure(j, weight=1)

def on_click(texto):
    global valor_actual

    if texto == "C":
        valor_actual = ""
    elif texto == "=":
        try:
            valor_actual = str(eval(valor_actual))
        except:
            valor_actual = "ERRO"
    elif texto == "±":
        try:
            if valor_actual:
                valor_actual = str(-float(valor_actual))
        except:
            pass
    elif texto == "%":
        try:
            if valor_actual:
                valor_actual = str(float(valor_actual)/100)
        except:
            pass
    elif texto == "Modo":
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")
    elif texto == "ERRO" or valor_actual == "ERRO":
        valor_actual = texto
    else:
        valor_actual += texto

    display.delete(0, "end")
    display.insert(0, valor_actual)


tela.mainloop()