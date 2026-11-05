import urllib.parse

def gerar_codigo_readme():
    print("Digite o seu texto (use ' PULA ' para quebrar as linhas):")
    entrada = input("> ")

    # Separa o texto em linhas limpando os espaços nas bordas
    linhas = [linha.strip() for linha in entrada.split(" PULA ")]
    num_linhas = len(linhas)
    
    # Strings base já codificadas para URL (Host e Diretório)
    host_base = "kaike%40desktop-kaike%3A"
    dir_base = "~%2FKaike-readme%2Fkaikea1meida%24"
    
    # Multiplica o Host e o Diretório pela quantidade de linhas e junta com ";"
    str_host = ";".join([host_base] * num_linhas)
    str_dir = ";".join([dir_base] * num_linhas)
    
    # Codifica o texto do utilizador para URL (transforma espaços em +, acentos em %C3, etc.)
    # O parâmetro safe='!.' impede que pontuações básicas sejam convertidas, mantendo a estética limpa
    str_texto = ";".join([urllib.parse.quote_plus(linha, safe='!.') for linha in linhas])
    
    # Altura dinâmica: 110px serve bem para até 4 linhas. Aumenta automaticamente se houver mais linhas.
    altura = max(110, num_linhas * 28)
    
    # Template HTML com as variáveis interpoladas
    html_final = f"""<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Ubuntu+Mono&size=15&color=8ACF31&duration=20&pause=2980&multiline=true&repeat=true&width=150&height={altura}&v=5&lines={str_host}" alt="Host" valign="top" /><!--
  --><img src="https://readme-typing-svg.demolab.com?font=Ubuntu+Mono&size=15&color=4EA8DE&duration=20&pause=2980&multiline=true&repeat=true&width=225&height={altura}&v=5&lines={str_dir}" alt="Caminho" valign="top" /><!--
  --><img src="https://readme-typing-svg.demolab.com?font=Ubuntu+Mono&size=15&color=DCFF00&duration=2000&pause=1000&multiline=true&repeat=true&width=380&height={altura}&v=5&lines={str_texto}" alt="Texto" valign="top" />
</div>"""

    # Salva o código num ficheiro de texto
    nome_ficheiro = "readme_terminal.txt"
    with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
        ficheiro.write(html_final)
        
    print(f"\nSucesso! O código HTML foi gerado e guardado no ficheiro '{nome_ficheiro}'.")

if __name__ == "__main__":
    gerar_codigo_readme()

    #python3 gerador.py
    #Hi there! PULA I'm Kaíke!!! PULA It's a pleasure to meet you! PULA Thats my readme, I hope you like it.