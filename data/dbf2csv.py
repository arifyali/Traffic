#!/usr/bin/python
import csv
from dbfpy import dbf
import os
import sys

for filename in sys.argv[1:]:
    if filename.endswith('.dbf'):
        print "Converting {} to csv".format(filename)
        csv_fn = filename[:-4]+ ".csv"
        with open(csv_fn, 'wb') as csvfile:
            in_dbf = dbf.Dbf(filename)
            out_csv = csv.writer(csvfile)
            names = []

            for field in in_db.header.fields:
                names.append(field.name)
            out_csv.writerow(names)

            for rec in in_dbf:
                out_csv.writerow(rec.fieldData)
            in_dbf.close()
            print "Completed"
    else:
      print "invalid filetype"
