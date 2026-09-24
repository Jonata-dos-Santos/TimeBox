import customtkinter

app = customtkinter.CTk()
app.geometry("400x200")

# Configura a coluna 0 para ocupar 50% do espaço e a coluna 1 para 50%
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

botao1 = customtkinter.CTkButton(app, text="Botão 1")
botao1.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

botao2 = customtkinter.CTkButton(app, text="Botão 2")
botao2.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

app.mainloop()   