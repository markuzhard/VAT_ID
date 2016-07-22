import xmlrpclib

server_url = 'https://evatr.bff-online.de/'
server     = xmlrpclib.Server(server_url)

# daten zum testen
UstId_1    = 'DE123456789'
UstId_2    = 'AB123456789012'
Firmenname = 'Firmenname einschl. Rechtsform'
Ort        = 'Ort'
PLZ        = '1234567'
Strasse    = 'Strasse und Hausnummer'
Druck      = 'nein'

rpc = server.evatrRPC(UstId_1, UstId_2, Firmenname, Ort, PLZ, Strasse, Druck)

print rpc
