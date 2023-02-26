import os
os.system('clear')
print("""instalação/atualizaçao""")
os.system('sudo apt install nmap')
os.system('pip install nmap')
os.system('pkg install nmap')
os.system('apt install nmap')
os.system('clear')
print('''
███╗░░██╗███╗░░░███╗░█████╗░██████╗░
████╗░██║████╗░████║██╔══██╗██╔══██╗
██╔██╗██║██╔████╔██║███████║██████╔╝
██║╚████║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░╚███║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░''')
os.system('nmap -h')
print('')
print('')
print('''1 – Listar as portas abertas em um host remoto, como o scanme.nmap.org:

# nmap scanme.nmap.org

2 – Detecção de Versão de Serviços

A detecção de serviço é uma das técnicas mais usadas no nmap, permitindo por exemplo identificar vulnerabilidades de segurança ou simplesmente verificar se um serviço está rodando em uma porta específica.

A flag sV habilita detecção de serviço, retornando informações sobre serviços e versões.

# nmap -sV scanme.nmap.org

3 – Usar o Modo Agressivo

O modo agressivo é um modo de operação especial do nmap que é ativado com o uso da flag A, habilitando a detecção de S.O., versão, escaneamento de script e traceroute:

# nmap -A localhost

4 – Encontrar hosts ativos na rede

Podemos enumerar ou monitorar alvos ativos, usando a flag P (ping scanning):

# sudo nmap -sP 192.168.1.1/24

5 – Escanear portas específicas na rede

Podemos escanear uma porta ou grupo de portas específicas com a flag -p

# sudo nmap -p80 192.168.1.1/24

Outras formas de escanear portas específicas:

Lista de portas:

# sudo nmap -p80, 443 192.168.1.1/24
Faixa de portas:

# sudo nmap -p1-200 192.168.1.1/24
Todas as portas:

# sudo nmap -p- 192.168.1.1/24
Portas específicas por protocolos:

# sudo nmap -pT:22,U:53 192.168.1.1/24
Por nome de serviço:

# sudo nmap -p ftp 192.168.1.1/24

ISTO E O BASICO, ESTUDE SOBRE E USE COMO PAINEL APENAS''')
print('')
print('')
print('USE COM MODERAÇAO!')
