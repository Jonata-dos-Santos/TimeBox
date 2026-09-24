from datetime import timedelta
import time

# Inicializa o tempo em 2 horas
tempo = timedelta(hours=2)

print("Timer iniciado!")

# Loop enquanto o tempo for maior que zero
while tempo.total_seconds() > 0:
    # Formata o tempo atual para HH:MM:SS
    total_segundos = int(tempo.total_seconds())
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    
    # Exibe o tempo no formato desejado
    print(f"\rFaltam: {horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)
    
    # Aguarda 1 segundo real
    time.sleep(1)
    
    # Reduz 1 segundo
    tempo -= timedelta(seconds=1)

print("\nTempo esgotado!")   