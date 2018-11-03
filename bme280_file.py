#!/usr/bin/python3
#coding: utf-8

import os
import requests
import util
import bme280_gt

sito = "http://troni.it/iot_log/php/add.php"
item_prefix = "datalog/mauve/"

util.log("Ciao Vecio")
bme280_gt.setup()
bme280_gt.get_calib_param()

dati = bme280_gt.readData()
f = open("/home/pi/datalog.csv", 'a')
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
