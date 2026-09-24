import customtkinter as ctk
from pathlib import Path

janela = ctk.CTk()
arquivo_config = Path("config.txt")
janela.title("Contador e Limitador de Tempo de Trabalho")
janela.geometry("400x300")
janela.resizable(width=False, height=False)
ctk.set_appearance_mode(arquivo_config.open("r", encoding="utf-8").readlines()[0][12:])
ctk.set_default_color_theme(arquivo_config.open("r", encoding="utf-8").readlines()[1][13:])

janela.grid_rowconfigure(0, weight=1)
# janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)
# janela.grid_columnconfigure(1, weight=0)


def formatar_tempo(event):
    valor = limite_entrada.get()

    # Remove tudo que não for número
    valor = "".join(c for c in valor if c.isdigit())

    # Limita a 6 números
    valor = valor[:6]

    # Preenche com zeros à esquerda
    valor = valor.zfill(6)

    # Coloca os :
    valor = f"{valor[:2]}:{valor[2:4]}:{valor[4:]}"

    limite_entrada.delete(0, "end")
    limite_entrada.insert(0, valor)


limite_entrada = ctk.CTkEntry(
    janela,
    font=(ctk.CTkFont(size=35)),
    width=150,
    height=100,
    placeholder_text="00:00:00",
    justify="right"
)

limite_entrada.insert(0, "00:00:00")

limite_entrada.bind("<KeyRelease>", formatar_tempo)

limite_entrada.grid(row=0, column=0)

janela.mainloop()