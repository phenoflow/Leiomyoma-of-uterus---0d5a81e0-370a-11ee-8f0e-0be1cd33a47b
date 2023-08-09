# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"BBK0000","system":"readv2"},{"code":"BBK0300","system":"readv2"},{"code":"BBK0500","system":"readv2"},{"code":"BBK0600","system":"readv2"},{"code":"12512","system":"med"},{"code":"28324","system":"med"},{"code":"32719","system":"med"},{"code":"33691","system":"med"},{"code":"3402","system":"med"},{"code":"41134","system":"med"},{"code":"4117","system":"med"},{"code":"432","system":"med"},{"code":"55349","system":"med"},{"code":"61105","system":"med"},{"code":"61404","system":"med"},{"code":"67322","system":"med"},{"code":"72251","system":"med"},{"code":"759","system":"med"},{"code":"8655","system":"med"},{"code":"93437","system":"med"},{"code":"98291","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('leiomyoma-of-uterus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["leiomyoma-of-uterus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["leiomyoma-of-uterus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["leiomyoma-of-uterus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
