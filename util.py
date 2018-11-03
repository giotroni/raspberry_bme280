#!/usr/bin/python3

import datetime
import socket

#inserisci il nome del device
origin = "xxx"
log_file = "/home/pi/Desktop/log.txt"

#funzione che ritorna l'ora in formato stringa
def ora():
        now = datetime.datetime.now()
        return now.strftime('%Y/%m/%d %H:%M')

#salva i messaggi su di un file di log
def log(s):
        f = open(log_file, 'a')
        f.write( ora() +'; ')
        f.write( s )
        f.write( '\n' )
        f.close()
        return

#prova a trovare il IP e lo ritorna, altrimenti stringa vuota
def get_ip_address():
    ip_address = '';
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip_address = s.getsockname()[0]
    except socket.error:
        log(  socket.error )
    finally:
        s.close()
        return ip_address
