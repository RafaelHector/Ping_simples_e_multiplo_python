import os #importando a biblioteca que traz as dependências do sistema operacional
import time #biblioteca que vai trabalhar com o tempo, minimizando-o

with open('host.txt') as file: #com abertura do host.txt como arquivo: jogue dentro do dump para ler arquivo, e em splitlines para deixar a leitura impressa em ordem.
    dump = file.read() #variável chamada dump, para ler arquivo e imprimir em linhas separadas
    dump = dump.splitlines()

    for ip in dump: #para cada ip no dump: vamos printar....
        print('verificando o  ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip)) #comando ping -n 2 para enviar 2 pacotes
        print('-' * 60)
        time.sleep(5) #a espera de 5 segundos do tempo de execução de um comando para o outro