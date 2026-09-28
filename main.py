from pathlib import Path
from datetime import datetime, timedelta, date
import customtkinter as ctk
import sys
from playsound3 import playsound
import os

# customizando a janela do custom tkinter e guardando o arquivo de tempo em uma variável 
janela = ctk.CTk()

# variáveis de tempo e criação do arquivo "tempo.txt"
if getattr(sys, 'frozen', False):
    arquivo_tempo = Path(sys.executable).parent / "tempo.txt"
else:
    arquivo_tempo = Path(__file__).parent / "tempo.txt"


agora = datetime.now().strftime(fr"%H:%M:%S")
hoje = date.today()


if not arquivo_tempo.exists():
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    arquivo_tempo.touch()
    arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")


if arquivo_tempo.exists() and arquivo_tempo.open("r", encoding="utf-8").readlines()[0] == "" or arquivo_tempo.exists() and arquivo_tempo.open("r", encoding="utf-8").readlines()[1] == "":
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")

if arquivo_tempo.exists():
    passado = date(year=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y").year, month=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y").month, day=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y").day)

hoje = date.today()
if passado < hoje:
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")


# criação do arquivo de configurações "config.txt" e definindo as configurações da janela
if getattr(sys, 'frozen', False):
    arquivo_config = Path(sys.executable).parent / "config.txt"
else:
    arquivo_config = Path(__file__).parent / "config.txt"


if arquivo_config.exists():
    ctk.set_appearance_mode(arquivo_config.open("r", encoding="utf-8").readlines()[0][11:].strip())
    janela.configure(fg_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][7:].strip())

if not arquivo_config.exists():
    arquivo_config.touch()
    arquivo_config.open("w", encoding="utf-8").write("\n\n\n\n")
    linhas_config = arquivo_config.open("r", encoding="utf-8").readlines()
    arquivo_config.open("w", encoding="utf-8").write(linhas_config[0])
    if ctk.get_appearance_mode() == "Dark":
        linhas_config[0] = "mode_theme=Dark"
        linhas_config[1] = "color1=black"
        linhas_config[2] = "color2=white"
        linhas_config[3] = "mode_button_icon=☼"
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[0])
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[1])
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[2])
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[3])

    if ctk.get_appearance_mode() == "Light":
        linhas_config[0] = "mode_theme=Light"
        linhas_config[1] = "color1=white"
        linhas_config[2] = "color2=black"
        linhas_config[3] = "mode_button_icon=☾"
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[0])
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[1])
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[2])
        arquivo_config.open("w", encoding="utf-8").write(linhas_config[3])

if arquivo_config.exists():
    arquivo_config.open("w", encoding="utf-8").write("\n\n\n\n")
    linhas_config = arquivo_config.open("r", encoding="utf-8").readlines()
    arquivo_config.open("w", encoding="utf-8").write(linhas_config[0])
    if ctk.get_appearance_mode() == "Dark":
        linhas_config[0] = "mode_theme=Dark"
        linhas_config[1] = "color1=black"
        linhas_config[2] = "color2=white"
        linhas_config[3] = "mode_button_icon=☼"
        arquivo_config.open("w", encoding="utf-8").write(f"{linhas_config[0]}\n{linhas_config[1]}\n{linhas_config[2]}\n{linhas_config[3]}")
        
    if ctk.get_appearance_mode() == "Light":
        linhas_config[0] = "mode_theme=Light"
        linhas_config[1] = "color1=white"
        linhas_config[2] = "color2=black"
        linhas_config[3] = "mode_button_icon=☾"
        arquivo_config.open("w", encoding="utf-8").write(f"{linhas_config[0]}\n{linhas_config[1]}\n{linhas_config[2]}\n{linhas_config[3]}")

if arquivo_config.exists() and linhas_config[0] != "mode_theme=Dark" and linhas_config[0] != "mode_theme=Light" and linhas_config[0] != "":
    linhas_config[0] == "mode_theme=system"


janela.title("TimeBox")
janela.geometry("380x380")
janela.resizable(width=False, height=False)

# funçao pra poder criar os arquivos de texto na mesma pasta do executável do programa
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

janela.iconbitmap(resource_path("TimeBox_Icone5.ico"))

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)
janela.grid_columnconfigure(4, weight=1)

# função pra evitar que escrevam qualquer coisa além de números nas entrys
def somente_numeros(event):
    if event.keysym in (
        "BackSpace",
        "Delete",
        "Left",
        "Right",
        "Home",
        "End",
        "Up",
        "Down"
    ):
        return

    if not event.char.isdigit():
        return "break"

# função pra passar de uma entry pra outra apertando "enter", mais detalhes nos "command=" das entrys
def proxima_entry(event, entrada):
    entrada.focus()

# organizando a interface com grid
frame_entradas = ctk.CTkFrame(janela, width=380, height=120, bg_color="transparent", fg_color="transparent", corner_radius=0)
frame_entradas.grid(row=0, column=0, columnspan=5, pady=0, sticky="n")
frame_entradas.grid_propagate(False)

frame_tudo = ctk.CTkFrame(frame_entradas, width=280, height=90, bg_color="transparent", fg_color="transparent", border_width=5, corner_radius=100, border_color=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
frame_tudo.grid(row=0, column=0, columnspan=5, padx=50, pady=(5, 15))
frame_tudo.grid_propagate(False)

frame_esquerda = ctk.CTkFrame(frame_tudo, width=60, height=60, bg_color="transparent", fg_color="transparent")
frame_esquerda.grid(row=0, column=0, padx=(20 , 10), pady=(15, 0))
frame_esquerda.grid_propagate(False)

limite_entrada_hora = ctk.CTkEntry(frame_esquerda, bg_color="transparent", border_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][7:].strip(), fg_color="transparent", corner_radius=0, font=(ctk.CTkFont(size=35)), width=60, height=60, placeholder_text="H", validate="key", validatecommand=(janela.register(lambda p: len(p) <= 2), '%P'), justify="center")
limite_entrada_hora.grid(row=0, column=0)
limite_entrada_hora.bind("<KeyPress>", somente_numeros)
limite_entrada_hora.bind("<Return>", lambda event: proxima_entry(event, limite_entrada_minuto))

frame_pontos1 = ctk.CTkFrame(frame_tudo, width=10, height=60, bg_color="transparent", fg_color="transparent")
frame_pontos1.grid(row=0, column=1, padx=0, pady=(15, 0))
frame_pontos1.grid_propagate(False)
ctk.CTkLabel(frame_pontos1, bg_color="transparent", fg_color="transparent", font=(ctk.CTkFont(size=35)), text=":", width=10, height=60).grid(row=0, column=0)

frame_centro = ctk.CTkFrame(frame_tudo, width=60, height=60, bg_color="transparent", fg_color="transparent")
frame_centro.grid(row=0, column=2, padx=10, pady=(15, 0))
frame_centro.grid_propagate(False)

limite_entrada_minuto = ctk.CTkEntry(frame_centro, bg_color="transparent", border_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][7:].strip(), fg_color="transparent", corner_radius=0, font=(ctk.CTkFont(size=35)), width=60, height=60, placeholder_text="M", validate="key", validatecommand=(janela.register(lambda p: len(p) <= 2), '%P'), justify="center")
limite_entrada_minuto.grid(row=0, column=0)
limite_entrada_minuto.bind("<KeyPress>", somente_numeros)
limite_entrada_minuto.bind("<Return>", lambda event: proxima_entry(event, limite_entrada_segundo))
# limite_entrada_minuto.pack()

frame_pontos2 = ctk.CTkFrame(frame_tudo, width=10, height=60, bg_color="transparent", fg_color="transparent")
frame_pontos2.grid(row=0, column=3, padx=0, pady=(15, 0))
frame_pontos2.grid_propagate(False)
ctk.CTkLabel(frame_pontos2, fg_color="transparent", bg_color="transparent", font=(ctk.CTkFont(size=35)), text=":", width=10, height=60).grid(row=0, column=0)

frame_direita = ctk.CTkFrame(frame_tudo, width=60, height=60, fg_color="transparent")
frame_direita.grid(row=0, column=4, padx=(10 , 0), pady=(15, 0))
frame_direita.grid_propagate(False)

limite_entrada_segundo = ctk.CTkEntry(frame_direita, bg_color="transparent", border_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][7:].strip(), fg_color="transparent", corner_radius=0, font=(ctk.CTkFont(size=35)), width=60, height=60, placeholder_text="S", validate="key", validatecommand=(janela.register(lambda p: len(p) <= 2), '%P'), justify="center")
limite_entrada_segundo.grid(row=0, column=0)
limite_entrada_segundo.bind("<KeyPress>", somente_numeros)
limite_entrada_segundo.bind("<Return>", lambda event: proxima_entry(event, limite_entrada_hora))

frame_centro_label = ctk.CTkFrame(janela, width=340, height=140, fg_color="transparent", bg_color="transparent")
frame_centro_label.grid(row=1, column=0, padx=30, columnspan=5, pady=(30, 0))
frame_centro_label.grid_propagate(False)

label_tempo = ctk.CTkLabel(frame_centro_label, fg_color="transparent", bg_color="transparent", corner_radius=100, border_width=5, border_color=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip(), font=(ctk.CTkFont(size=60)), text=arquivo_tempo.open("r", encoding="utf-8").readlines()[0].strip(), width=300, height=86, anchor="center")
label_tempo.grid(row=0, column=0, pady=(17, 0))



# a seguir a variável que usei só pra sair do programa ao clicar no botão "pausar" e a função que funciona como o timer do programa
contagem = 0

def contar(contador_ativado):
    global arquivo_tempo
    global hoje
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    global janela
    global limite_entrada_hora
    global limite_entrada_minuto
    global limite_entrada_segundo
    global label_tempo
    global tempo_restante
    global contagem

    # essa parte (parte 1) faz o programa iniciar a contagem, caso o tempo seja 00:00:00 e o usuário defina o tempo depois
    if contador_ativado == 0:
        limite_h = limite_entrada_hora.get()
        limite_m = limite_entrada_minuto.get()
        limite_s = limite_entrada_segundo.get()

        limite_td = timedelta(0)
        if limite_h.isdigit() or limite_m.isdigit() or limite_s.isdigit():
                
            if limite_h == "": limite_h = 0
            if limite_m == "": limite_m = 0
            if limite_s == "": limite_s = 0

            limite_td += timedelta(hours=int(limite_h), minutes=int(limite_m), seconds=int(limite_s))
        
                
            limite_tds = limite_td.total_seconds()
            tempo_restante = limite_tds
        
        else: tempo_restante = 0
        
        label_tempo.grid_configure(pady=0)

    # essa parte (parte 3) faz o programa continuar de onde parou, após ter salvo o tempo restante no "tempo.txt" (nota: ele só salva o tempo se o programa for fechado)
    if contador_ativado == 2:
        tempo_restante = int((timedelta(hours=datetime.strptime(open(arquivo_tempo, "r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(open(arquivo_tempo, "r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(open(arquivo_tempo, "r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").second)).total_seconds())
        label_tempo.grid_configure(pady=0)

    # (continuação da parte 1 e 2): é aqui onde o temporizador funciona
    if tempo_restante >= 0:
        
        tempo = f"{int(tempo_restante // 3600):02d}:{int((tempo_restante % 3600) // 60):02d}:{int(tempo_restante % 60):02d}"
        
        tempo_restante -= 1
        
        arquivo_tempo_linhas = [f"{tempo}\n", f"{hoje}"]
        arquivo_tempo.open("w", encoding="utf-8").writelines(arquivo_tempo_linhas)
        
        label_tempo.configure(text=tempo)
        
        janela.after(1000, lambda: contar(1))
        
        if tempo_restante == -1:
            label_tempo["text"] = "00:00:00"
            arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")
            playsound("Som_Alerta.mp3")
            botao_comecar.configure(command=lambda: contar(0), text="INICIAR")
            label_tempo.grid_configure(pady=0)
        if tempo_restante != 0 and tempo_restante != -1:
            botao_comecar.configure(command=pausar, text="FECHAR")
            label_tempo.grid_configure(pady=0)

# criando o botão principal do programa (por enquanto é o único botão), posicionando ele na grid e definindo suas funções (nota: o "command=" do botão muda para a função pausar() lá dentro da função contar(); as outras funções são chamadas logo abaixo)
frame_centro_botao = ctk.CTkFrame(janela, width=120, height=120, fg_color="transparent")
frame_centro_botao.grid(row=2, column=2)

botao_comecar = ctk.CTkButton(frame_centro_botao, text="INICIAR", command=lambda: contar(0), fg_color="#072f3c", width=160, height=70, font=(ctk.CTkFont(size=30)), corner_radius=0)
botao_comecar.grid(row=2, column=1, pady=30)

# função de pausar (ela não pausa realmente; o programa fecha, mas o tempo é salvo do arquivo "tempo.txt")
def pausar():
    sys.exit()

if arquivo_tempo.exists():
    if int(timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").second).total_seconds()) == 0:
        
        botao_comecar.configure(command=lambda: contar(0))

    if int(timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").second).total_seconds()) > 0:
        
        botao_comecar.configure(command=lambda: contar(2), text="CONTINUAR")


def trocar_modo():
    global arquivo_config
    global janela
    # global botao_comecar
    global limite_entrada_hora
    global limite_entrada_minuto
    global limite_entrada_segundo
    global frame_centro_label
    if arquivo_config.exists():
        if arquivo_config.open("r", encoding="utf-8").readlines()[0] == "mode_theme=Dark":
            arquivo_config.open("w", encoding="utf-8").write("mode_theme=Light\ncolor1=white\ncolor2=white\nmode_button_icon=☾")

            ctk.set_appearance_mode(arquivo_config.open("r", encoding="utf-8").readlines()[0][12:].strip())
            janela.configure(fg_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][9:].strip())
            limite_entrada_hora.configure(background_corner_colors=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
            limite_entrada_minuto.configure(background_corner_colors=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
            limite_entrada_segundo.configure(background_corner_colors=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
            frame_centro_label.configure(background_corner_colors=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())

        if arquivo_config.open("r", encoding="utf-8").readlines()[0] == "mode_theme=Light":
            arquivo_config.open("w", encoding="utf-8").write("mode_string=Dark\ncolor1=black\ncolor2=black\nmode_button_icon=☼")

            ctk.set_appearance_mode(arquivo_config.open("r", encoding="utf-8").readlines()[0][12:].strip())
            janela.configure(fg_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][9:].strip())
            limite_entrada_hora.configure(border_color=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
            limite_entrada_minuto.configure(border_color=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
            limite_entrada_segundo.configure(border_color=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())
            frame_centro_label.configure(background_corner_colors=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip())

frame_botao_modo = ctk.CTkFrame(frame_entradas, width=30, height=30, fg_color="transparent")
frame_botao_modo.grid(row=0, column=4, sticky="ne")

botao_trocar_modo = ctk.CTkButton(frame_botao_modo, text=arquivo_config.open("r", encoding="utf-8").readlines()[3][-1:].strip(), fg_color=arquivo_config.open("r", encoding="utf-8").readlines()[1][7:].strip(), border_color=arquivo_config.open("r", encoding="utf-8").readlines()[2][7:].strip(), command=trocar_modo, width=30, height=30, font=(ctk.CTkFont(size=15)), corner_radius=100)
botao_trocar_modo.grid(row=0, column=0)

if arquivo_config.open("r", encoding="utf-8").readlines()[0] == "mode_theme=Dark":
    botao_trocar_modo.configure(background_corner_colors="white")
if arquivo_config.open("r", encoding="utf-8").readlines()[0] == "mode_theme=Light":
    botao_trocar_modo.configure(background_corner_colors="black")



janela.mainloop()