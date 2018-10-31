import os, csv
from typing import List, Any

dir = os.path.join('C:\\Users\\frago\\Desktop\\DxDiag')
files = os.listdir(dir)

for filename in files:
    filepath = os.path.join(dir, filename)
    with open(filepath, 'rt') as fin:
        alltxt = list(fin)

    row = [filename, alltxt[6].strip(), alltxt[8].strip(), alltxt[9].strip(), alltxt[11].strip(), alltxt[12].strip()]
    eth = [x for x in alltxt if 'Ethernet' in x]
    nic = str(alltxt[alltxt.index(eth[0])]).strip()
    row.append(nic)

    with open('C:\\temp\\pyfile.csv', 'a') as csvfile:
        csvwrite = csv.writer(csvfile, dialect = 'excel', quoting = csv.QUOTE_MINIMAL)
        csvwrite.writerow(row)