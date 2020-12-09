# coding: utf-8
import csv
import smtplib
import credentials
from email.mime.text import MIMEText

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = credentials.username
password = credentials.password

from_addr = credentials.username

# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)

MAIL_MESSAGE_BODY = 'Olá {}! Sentimos sua falta!\n Preparamos as melhores promoções para você, dos itens que você mais gosta!\n Acesse site.com.br/produtos para saber mais.'

ARCHIVE_NAME = 'clientes_filtrados.csv'

try:
    clientes_archive = open(ARCHIVE_NAME)
except FileNotFoundError as e:
    print(e)
    exit()

#Lendo CSV e popilando array
rowsClientesCsv = csv.reader(clientes_archive)
rowsClientes = []
for row in rowsClientesCsv:
    rowsClientes.append(row)

#Percorrendo array e eenviando emails
for row in rowsClientes[1:]:
    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    message = MIMEText(MAIL_MESSAGE_BODY.format(row[1]), 'plain', 'utf-8')
    message['subject'] = 'Estamos com saudades'
    message['from'] = from_addr
    message['to'] = row[2]
    server.sendmail(from_addr, row[2], message.as_string())

server.quit()