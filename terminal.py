import sys
import time
import os

def animacao_terminal():
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Cores exatas convertidas de Hexadecimal para ANSI RGB
    cor_host = "\033[38;2;138;207;49m"   # Verde (#8ACF31)
    cor_dir = "\033[38;2;78;168;222m"    # Azul (#4EA8DE)
    cor_texto = "\033[38;2;220;255;0m"   # Amarelo-Néon (#DCFF00)
    reset = "\033[0m"
    
    # O texto em inglês
    linhas = [
        "In the room, we can walk somewhat freely",
        "access the minigames or some books, with just a click",
        "we tried adding some reflections too",
        "and there are animations for when you're holding things"
    ]
    
    # Dá 2 segundos antes de começar para você preparar o gravador
    time.sleep(2)
    
    for linha in linhas:
        # 1. Aparece o prompt instantaneamente
        sys.stdout.write(f"{cor_host}kaike@desktop-kaike:{cor_dir}~/Kaike-readme/kaikea1meida$ {cor_texto}")
        sys.stdout.flush()
        
        time.sleep(0.4) # Pausa dramática antes de começar a digitar
        
        # 2. Efeito de digitação letra por letra
        for char in linha:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06) # Velocidade da digitação
        
        print(reset) # Pula a linha e reseta a cor
        time.sleep(0.8) # Pausa antes da próxima linha

    # Mantém a tela final parada um tempo antes do script acabar
    time.sleep(3)

if __name__ == "__main__":
    animacao_terminal()