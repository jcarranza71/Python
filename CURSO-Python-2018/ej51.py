# xml

import untangle

r = untangle.parse('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')

for i in r.gesmes_Envelope.Cube.Cube.Cube:
	if i['currency']=='GBP':
		print(i['currency'],i['rate'])

print(r.gesmes_Envelope.Cube.Cube.Cube[5]['currency'])