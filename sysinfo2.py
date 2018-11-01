import os, csv
from typing import List, Any

home = os.path.expanduser('~')
dsktp = os.path.join(home, 'Desktop')
csvfilep = os.path.join(dsktp, 'sysinfo' + '.csv')
diagdir = os.path.join(dsktp, 'DxDiag')
diagfiles = os.listdir(diagdir)

def csv_writer(rows):
    with open(csvfilep, 'a') as csvfile:
        csvwrite = csv.writer(csvfile, dialect = 'excel', quoting = csv.QUOTE_MINIMAL)
        if os.stat(csvfilep).st_size == 0:
            csvwrite.writerow(['Operating System', 'System Manufacturer', 'System Model', 'Processor', 'Memory', 'Ethernet Interaface', 'X2 pro Image build version', 'iX Developer version'])
        else:
            csvwrite.writerow(rows)


def diaginfo(files, dir):
    for filename in files:
        filepath = os.path.join(dir, filename)
        with open(filepath, 'rt') as fin:
            fulldiag = list(fin)

        row = [filename, fulldiag[6].strip(), fulldiag[8].strip(), fulldiag[9].strip(), fulldiag[11].strip(), fulldiag[12].strip()]
        print(row)
        eth = [x for x in fulldiag if 'Ethernet' in x]
        print(eth)
        # nic = str(fulldiag[fulldiag.index(eth[0])]).strip()
        # row.append(nic)

        # csv_writer(row)

diaginfo(diagfiles, diagdir)
