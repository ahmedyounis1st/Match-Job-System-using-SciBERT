from excel_manager import ExcelManager
from mysql_manager import MySQLManager
from scibert import SciBERT
import numpy as np

YEAR = "2018"
EXCEL_FILENAMES = ["18"+".xlsx"]

def main():
    mysql = MySQLManager()
    scibert = SciBERT()
    for filename in EXCEL_FILENAMES:
        excel = ExcelManager(filename)
        data = excel.get()
        # print(data, flush=True)
        #print("Inserting records from {}".format(filename), flush=True)
        print("Inserting records from {}".format(filename))
        for i in range(len(data)):
            if i > 0 and i % 100 == 0:
                print("Inserted {} records into MySQL. ".format(i))
            record = {}
            record["id"] = i
            record["photo"] = data[i]["Photo"]
            record["author"] = data[i]["Authors"]
            record["university"] = data[i]["University"]
            try:
                vector = scibert.vectorize(data[i]["Abstract"])
            except:
                continue
            record["vector"] = vector.dumps()
            record["title"] = data[i]["Title"]
            record["link"] = data[i]["Link"]
            record["abstract"] = data[i]["Abstract"]
            mysql.insert(record, YEAR)
    mysql.close()
    #print("Data Inserted", flush=True)

if __name__ == "__main__":
    main()
