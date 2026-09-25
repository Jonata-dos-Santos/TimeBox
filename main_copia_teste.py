from pathlib import Path
from datetime import datetime, timedelta, date
import time
import os
from dateutil.relativedelta import relativedelta
import customtkinter as ctk

janela = ctk.CTk()

arquivo_config = Path("config.txt")

if not arquivo_config.exists():
    arquivo_config.touch()
    arquivo_config.open("w", encoding="utf-8").write(f"mode_string=system\ncolor_string=blue")

janela.title("Contador e Limitador de Tempo de Trabalho")
janela.geometry("380x380")
janela.resizable(width=False, height=False)
ctk.set_appearance_mode(arquivo_config.open("r", encoding="utf-8").readlines()[0][12:])
ctk.set_default_color_theme(arquivo_config.open("r", encoding="utf-8").readlines()[1][13:])

janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)


# HORA
frame_esquerda = ctk.CTkFrame(
    janela,
    width=120,
    height=120,
    fg_color="transparent"
)
frame_esquerda.grid(row=0, column=0)

limite_entrada_hora = ctk.CTkEntry(
    frame_esquerda,
    font=ctk.CTkFont(size=35),
    width=60,
    height=60,
    placeholder_text="h",
    validate="key",
    validatecommand=(janela.register(lambda p: len(p) <= 2), "%P"),
    justify="center"
)
limite_entrada_hora.grid(row=0, column=0)


# MINUTO
frame_centro = ctk.CTkFrame(
    janela,
    width=120,
    height=120,
    fg_color="transparent"
)
frame_centro.grid(row=0, column=1)

limite_entrada_minuto = ctk.CTkEntry(
    frame_centro,
    font=ctk.CTkFont(size=35),
    width=60,
    height=60,
    placeholder_text="m",
    validate="key",
    validatecommand=(janela.register(lambda p: len(p) <= 2), "%P"),
    justify="center"
)
limite_entrada_minuto.grid(row=0, column=0)


# SEGUNDO
frame_direita = ctk.CTkFrame(
    janela,
    width=120,
    height=120,
    fg_color="transparent"
)
frame_direita.grid(row=0, column=2)

limite_entrada_segundo = ctk.CTkEntry(
    frame_direita,
    font=ctk.CTkFont(size=35),
    width=60,
    height=60,
    placeholder_text="s",
    validate="key",
    validatecommand=(janela.register(lambda p: len(p) <= 2), "%P"),
    justify="center"
)
limite_entrada_segundo.grid(row=0, column=0)


# FRAME MAIOR NO CENTRO
frame_centro_label = ctk.CTkFrame(
    janela,
    width=320,
    height=120,
    fg_color="blue"
)
frame_centro_label.grid(
    row=1,
    column=0,
    columnspan=3,
    padx=30,
    pady=0
)

def mostrar():
    global limite_entrada
    limite = limite_entrada.get()
    print(limite)
    









# print(arquivo_config.open("r", encoding="utf-8").readlines()[0][12:])

arquivo_tempo = Path("tempo.txt")
agora = datetime.now().strftime(fr"%H:%M:%S")
hoje = date.today()

passado = date(year=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y").year, month=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y").month, day=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y").day)
# contador = datetime(hour=0, minute=0, second=0)
# contador_ativado = 0
# tempo = 0

if not arquivo_tempo.exists():
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    arquivo_tempo.touch()
    arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")

# print(arquivo_tempo.exists() and arquivo_tempo.open("r", encoding="utf-8").readline(1))

if arquivo_tempo.exists() and arquivo_tempo.open("r", encoding="utf-8").readlines()[0] == "" or arquivo_tempo.exists() and arquivo_tempo.open("r", encoding="utf-8").readlines()[1] == "":
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")


# print(passado)
# print(type(datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[1], r"%d/%m/%Y")))
# print(int(arquivo.open("r", encoding="utf-8").readline(-1)[0]))

hoje = date.today()
if passado < hoje:
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    arquivo_tempo.open("w", encoding="utf-8").write(f"00:00:00\n{hoje}")
    # print(arquivo_tempo.open("r", encoding="utf-8").readlines()[1])



def contar(contador_ativado):
    os.system("cls")
    global arquivo_tempo
    # global contador_ativado
    global hoje
    global janela
    hoje = datetime.now().strftime(fr"%d/%m/%Y")
    # tempo = datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S")
    # if timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").second) == timedelta(hours=0, minutes=0, seconds=0) and contador_ativado == 0:
    if contador_ativado == 0:
        # limite = ctk.CTkEntry(janela, 150, 50, )
        ...
        print("")
    # if timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").second) > timedelta(hours=0, minutes=0, seconds=0) and contador_ativado == 1:
    if contador_ativado == 1:
        tempo_restante = int((timedelta(hours=datetime.strptime(open(arquivo_tempo, "r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(open(arquivo_tempo, "r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(open(arquivo_tempo, "r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").second)).total_seconds())
    while True:

        if "limite" in locals():
            if limite.replace(".", "").isnumeric() and limite != "":
                limite = float(limite)
                # arquivo_tempo.open("w", encoding="utf-8").write(str(limite))
                limite_td = timedelta(hours=limite)
                limite_tds = limite_td.total_seconds()
                tempo_restante = int(limite_tds)
            elif not limite.replace(".", "").isnumeric() or limite == "":
                print("[ERRO] - Você não digitou nenhum número.")
        if tempo_restante != 0:
            while tempo_restante >= 0:
                time.sleep(1)
                tempo = f"{tempo_restante // 3600:02d}:{(tempo_restante % 3600) // 60:02d}:{tempo_restante % 60:02d}"
                # horas = int(f"{tempo_restante // 3600:02d}")
                # minutos = int(f"{(tempo_restante % 3600) // 60:02d}")
                # segundos = int(f"{tempo_restante % 60:02d}")
                # contador.seconds += 1
                # tempo_passado = limite_td - contador
                tempo_restante -= 1
                # tempo_restante -= contador.seconds
                # contador_ativado = 1
                arquivo_tempo_linhas = [f"{tempo}\n", f"{hoje}"]
                arquivo_tempo.open("w", encoding="utf-8").writelines(arquivo_tempo_linhas)
                # print(f"{tempo}\n{hoje}", end="", flush=True)
                print(f"\n\033[2A{tempo}\n{hoje}", end="", flush=True)
                # print(f"{hoje}", end="", flush=True)
            # contador_ativado = 0
            print("\n\nSeu tempo acabou!")
            limite = input("Digite o seu novo tempo limite em horas: ")
            print("")

if arquivo_tempo.exists():
    if int(timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").second).total_seconds()) == 0:
        # limite = input("Digite o seu tempo limite em horas: ")
        # if limite.replace(".", "").isnumeric() and limite != "":
        #     limite = float(limite)
        #     arquivo.open("w", encoding="utf-8").write(str(limite))
        #     limite_td = timedelta(hours=limite)
        #     limite_tds = limite_td.total_seconds()
        #     tempo_restante = limite_tds + 1
            # if tempo_restante > 0: 
        # contar(0)
        
        # print(int(timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").second).total_seconds()))
        ...
        # while tempo > 0:
        #     contador_ativado = 1
        # contador_ativado = 0
            # print(f"O tipo de limite é '{type(limite)}' e o valor é '{limite}'")
        


    if int(timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readlines()[0][:-1], fr"%H:%M:%S").second).total_seconds()) > 0:
        # tempo = float(arquivo.read_text(encoding="utf-8"))
        # contador_ativado = 1
        # contar(1)
        ...
        # print(int(timedelta(hours=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").hour, minutes=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").minute, seconds=datetime.strptime(arquivo_tempo.open("r", encoding="utf-8").readline(-1)[:-1], fr"%H:%M:%S").second).total_seconds()))


    # if float(arquivo.open("r", encoding="utf-8").readline(-1)[:-1]) == 0:
    #     arquivo.open("w", encoding="utf-8").write("0.0")
    #     # print(float(str(tempo_restante)[0]))
        # sys.exit(0)


frame_centro_botao = ctk.CTkFrame(janela, width=120, height=120, fg_color="transparent").grid(row=2, column=1, padx=0, pady=0)

botao_comecar = ctk.CTkButton(frame_centro_botao, text="Começar", command=mostrar)
botao_comecar.grid(row=2, column=1)

# botao_comecar.pack()








janela.mainloop()