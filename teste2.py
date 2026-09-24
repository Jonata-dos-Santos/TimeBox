import customtkinter as ctk

# Configura o tema (opcional, padrão é claro)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Controle Numérico")
        self.geometry("300x150")

        # Variável para rastrear o valor numérico
        self.valor_var = ctk.StringVar(value="0")

        # 1. Cria o Entry (apenas leitura visual, pode ser editável se desejar)
        self.entry = ctk.CTkEntry(
            self, 
            textvariable=self.valor_var, 
            width=100,
            font=("Arial", 20, "bold")
        )
        self.entry.pack(pady=20)

        # 2. Frame para os botões de controle
        frame_botoes = ctk.CTkFrame(self)
        frame_botoes.pack()

        # Botão Decrementar (-)
        btn_minus = ctk.CTkButton(
            frame_botoes, 
            text="-", 
            width=50, 
            height=40, 
            font=("Arial", 16),
            command=self.decrementar
        )
        btn_minus.pack(side="left", padx=5)

        # Botão Incrementar (+)
        btn_plus = ctk.CTkButton(
            frame_botoes, 
            text="+", 
            width=50, 
            height=40, 
            font=("Arial", 16),
            command=self.incrementar
        )
        btn_plus.pack(side="left", padx=5)

    def incrementar(self):
        try:
            # Pega o valor atual e converte para int (ou float se preferir)
            atual = int(self.valor_var.get())
            self.valor_var.set(atual + 1)
        except ValueError:
            # Se o usuário digitar algo inválido manualmente, reseta para 0
            self.valor_var.set("0")

    def decrementar(self):
        try:
            atual = int(self.valor_var.get())
            self.valor_var.set(atual - 1)
        except ValueError:
            self.valor_var.set("0")

if __name__ == "__main__":
    app = App()
    app.mainloop()   