# TimeBox

Um temporizador com contagem regressiva desenvolvido em Python, com salvamento do tempo restante e opções de personalização da interface e do som de alerta.

## Download

A versão **1.1.1** está disponível na seção [Releases](../../releases) deste repositório.

O arquivo `.zip` da versão contém:

* `TimeBox.exe` — executável do programa.
* `Som_Alerta.mp3` — arquivo de áudio reproduzido quando o temporizador chega a `00:00:00`.

### Como utilizar

1. Baixe o arquivo `.zip` da versão desejada na seção Releases.
2. Extraia os arquivos para uma pasta de sua preferência.
3. Execute o arquivo `TimeBox.exe`.

> **Importante:** mantenha o arquivo `Som_Alerta.mp3` na mesma pasta do executável para que o som de alerta funcione corretamente.

## Funcionalidades

* **Contagem regressiva:** permite definir horas, minutos e segundos para iniciar o temporizador.
* **Salvamento do tempo restante:** salva o tempo restante para permitir que a contagem seja retomada posteriormente.
* **Retomada do temporizador:** permite continuar a contagem a partir do tempo salvo.
* **Temas claro e escuro:** acompanha o tema do sistema por padrão e permite alternar entre os temas pela interface.
* **Som de alerta personalizado:** permite substituir o áudio reproduzido quando o temporizador chega a `00:00:00`.

## Tecnologias utilizadas

O projeto foi desenvolvido utilizando:

* **Python**
* **CustomTkinter** — criação da interface gráfica.
* **playsound3** — reprodução do som de alerta.

Também são utilizadas bibliotecas da biblioteca padrão do Python:

* **pathlib** — manipulação de arquivos e diretórios.
* **datetime** — manipulação de datas e horários.
* **sys** — acesso a recursos relacionados ao sistema e à execução do programa.
* **os** — interação com recursos do sistema operacional.

## Como executar a partir do código-fonte

Caso queira executar o projeto diretamente pelo código-fonte, é necessário ter o **Python 3** instalado.

### 1. Instale as dependências

As bibliotecas externas utilizadas pelo projeto são:

```bash
pip install customtkinter playsound3
```

`pathlib`, `datetime`, `sys` e `os` fazem parte da biblioteca padrão do Python e não precisam ser instaladas separadamente.

### 2. Execute o programa

Na pasta do projeto, execute:

```bash
python main.py
```

> **Nota:** a versão `.exe` disponível nas Releases já possui as dependências necessárias incorporadas e não requer uma instalação separada do Python para ser executada.

## Personalização

### Tema da interface

O programa acompanha o tema do sistema por padrão, mas permite alternar entre os temas claro e escuro pela própria interface.

### Som de alerta

Para personalizar o som reproduzido quando o temporizador chega a `00:00:00`:

1. Localize o arquivo `Som_Alerta.mp3`.
2. Substitua-o pelo arquivo de áudio desejado.
3. Mantenha o nome `Som_Alerta.mp3`.
4. Mantenha a extensão `.mp3`.
5. Coloque o arquivo na mesma pasta do `TimeBox.exe`.

## Estrutura da versão executável

A versão disponibilizada nas Releases possui a seguinte estrutura:

```text
TimeBox/
├── TimeBox.exe
└── Som_Alerta.mp3
```

Manter os dois arquivos na mesma pasta é necessário para que o programa encontre e reproduza o som de alerta corretamente.
