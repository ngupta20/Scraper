import csv
import os


headers = []
for entry in os.scandir(r".\Tests"):
    if ".csv" in entry.path and "Final" not in entry.path:
        with open(entry.path[2:], encoding = "utf-8", newline = "") as f:

            d = csv.reader(f)
            
            for head in next(d):
                if head not in headers:
                    headers.append(head)    


out = [headers]
for entry in os.scandir(r".\Tests"):
    if ".csv" in entry.path and "Final" not in entry.path:
        with open(entry.path[2:], encoding = "utf-8", newline = "") as f:
        
            d = csv.reader(f)
        
            rows = []
            for row in d:
                rows.append(row)
        
            dheads = []
            for head in rows[0]:
                dheads.append(headers.index(head))

            for line_index in range(1, len(rows)):
                ground = [""] * len(headers)
        
                isEmpty = True
                for element in rows[line_index]:
                    if element != "":
                        isEmpty = False
                if isEmpty:
                    continue
        
                for i in range(len(dheads)):
                    ground[dheads[i]] = rows[line_index][i]
        
                out.append(ground)


with open("Final.csv", "w", encoding = "utf-8", newline = "") as f:

    w = csv.writer(f)

    w.writerows(out)
