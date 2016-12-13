import csv
import json

csvfile = open('./dist/Public_Schools.csv', 'r')
jsonfile = open('./dist/PublicSchools.json', 'w')

fieldnames = ("X","Y","OBJECTID","BLDG_NAME", "BLDG_NAME", "ADDRESS", "CITY", "ZIPCODE", "CSP_SCH_ID", "SCH_ID", "SCH_NAME", "SCH_LABEL", "SCH_TYPE", "SHARED", "COMPLEX")
reader = csv.DictReader( csvfile, fieldnames)

for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n')