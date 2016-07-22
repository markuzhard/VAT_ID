#!/usr/bin/env python
# encoding: utf-8
 
import requests
from XML import XML
      
request = u"""<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/xmlns:urn="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
   <soapenv:Header/>
   <soapenv:Body>
      <urn:checkVat>
        <urn:countryCode>MS</urn:countryCode>
        <urn:vatNumber>TESTVATNUMBER</urn:vatNumber>
      </urn:checkVat>
   </soapenv:Body>
</soapenv:Envelope>"""

encoded_request = request.encode('utf-8')
 
#headers = {"Host": "www.webservicex.net",
#           "Content-Type": "text/xml; charset=UTF-8",
#           "Content-Length": len(encoded_request)}
#                           
#response = requests.post(url="http://www.webservicex.net/CurrencyConvertor.asmx",
#                         headers = headers,
#                         data = encoded_request,
#                         verify=False)
#                          

print unicode(XML(response.text))
