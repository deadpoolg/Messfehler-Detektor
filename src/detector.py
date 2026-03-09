import csv
from statistic import berechne_mittelwert, berechne_median
import os

def read_csv(p):
    y = []
    with open(p, newline="") as f:
        r = csv.reader(f)
        first = True
        for row in r:
            if first:
                first = False
                continue
            if len(row) < 2:
                continue
            try:
                y.append(float(row[1]))
            except:
                try:
                    parts = row[0].split(";")
                    if len(parts) > 1:
                        v = parts[1].replace(",", ".")
                        y.append(float(v))
                except:
                    pass
    return y

def main():
    base = os.path.dirname(os.path.dirname(__file__))
    p = os.path.join(base, "daten", "test.csv")
    y = read_csv(p)
    if not y:
        y = [10.5, 11.0, 10.8, 50.0, 10.9]
    m = berechne_mittelwert(y)
    md = berechne_median(y)
    print("Mittelwert:", round(m, 2))
    print("Median:", md)

if __name__ == "__main__":
    main()
