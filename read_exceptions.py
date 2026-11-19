import csv

with open("reconciliation_exceptions.csv", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        raw_diff = row["diff_minor"]

        if raw_diff == "":
            diff = None
        else:
            diff = int(raw_diff)

        if diff is None or abs(diff) >= 1000:
            print(row["order_id"], diff)