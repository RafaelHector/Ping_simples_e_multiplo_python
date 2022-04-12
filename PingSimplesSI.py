import os #Importa o módulo ou biblioteca os (integra os programas e recursos do sistema operacional)

print('#' * 60) #imprimir o 'sharp' 60 vezes
ip_ou_host = input("Digite o Ip ou Host a ser verificado:") #criando uma variável que vai receber do usuário o ip
print('-' * 60)
os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando system da biblioteca os - comando ping, -n é o numero de pacotes que serão 6 {}
print('-' * 60)
#Exemplo de Host a ser testados: www.google.com