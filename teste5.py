import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.grid_rowconfigure(1, weight=1)
# janela.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
# janela.grid_columnconfigure(1, weight=0)

# Exemplo de remoção de margens
frame = ctk.CTkFrame(app)
frame.grid(padx=10, pady=10, column=0)

frame2 = ctk.CTkFrame(app)
frame2.grid(padx=10, pady=10, column=1)

botao = ctk.CTkButton(frame, text="Clique1", width=50)
botao.grid(padx=0, pady=0, column=0)

botao2 = ctk.CTkButton(frame2, text="Clique2", width=50)
botao2.grid(padx=0, pady=0, column=1)

app.mainloop()   