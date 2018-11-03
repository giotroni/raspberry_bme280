#!/usr/bin/python3
#coding: utf-8

import os
import requests
import util
import bme280_gt
#inserisci il link alla API del sito IoT
sito = "xxx"
#inserisci il ridferimento all'indirizzo dei dati da salvare sul sito
item_prefix = "datalog/..."
#nome del file locale su cui salvare i dati
nome_file = "/home/pi/datalog.csv"
        
util.log("Ciao Vecio")
bme280_gt.setup()
bme280_gt.get_calib_param()

dati = bme280_gt.readData()

#salva sul file locale
f = open(nome_file, 'a')
for x in dati:
        item = item_prefix + x
        csv = util.ora() +";" + util.origin + ";" + item + ";" + dati[x]
        print( csv )
        f.write (csv +'\n')
f.close()

#salva sul database
ip_local = util.get_ip_address() 
if( ip_local != '' ):
        util.log(ip_local)
        for x in dati:
                item = item_prefix + x
                payload = {'origin': util.origin, 'item':item, 'value':dati[x]}
                try:
                        r = requests.get(sito, params=payload)
                        #log( "comunicazione con server: " + r.text )
                except requests.exceptions.RequestException as e:
                        util.log( e )
else:
        util.log( "Nessuna rete" )
