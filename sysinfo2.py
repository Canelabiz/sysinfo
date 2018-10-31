import os, csv

dsktp = os.path.join('C:\\Users\\frago\\Desktop')
csvfile = os.path.join(dsktp, 'sysinfo' + '.csv')
diagdir = os.path.join(dsktp, 'DxDiag\\')
diagfiles = os.listdir(diagdir)

def main():

    excerpt = ['a', 'b', 'c']


    def csv_writer(file, row):
        fieldnames = ['Operating System', 'System Manufacturer', 'System Model', 'Processor', 'Memory', 'Ethernet Interaface', 'X2 pro Image build version', 'iX Developer version']
        with open(file, 'a') as csvfile:
            csvwrite = csv.DictWriter(csvfile, fieldnames = fieldnames, dialect = 'excel', quoting = csv.QUOTE_MINIMAL)
            if os.stat(file).st_size == 0:
                csvwrite.writeheader()
            else:
                csvwrite.writerow(row)


    csv_writer(csvfile, excerpt)

if __name__ == '__main__':
    main()
