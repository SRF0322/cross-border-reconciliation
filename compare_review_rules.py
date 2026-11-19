import csv
total_count = 0
broad_count = 0
narrow_count = 0
needs_review_ids = {"0002", "0003", "0004", "0028"}
broad_review_ids = set()
narrow_review_ids = set()
with open("reconciliation_all.csv", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        raw_diff = row["diff_minor"]

        if raw_diff == "":
            diff = None
        else:
            diff = int(raw_diff)

        total_count += 1
        order_id = row["order_id"].strip()
        if order_id in {"O002", "O003", "O004"}:
            order_id = "0" + order_id[1:]

        if diff is None or diff != 0:
            broad_count += 1
            broad_review_ids.add(order_id)

        if diff is None or abs(diff) >= 1000:
            narrow_count += 1
            narrow_review_ids.add(order_id)
print("订单总数：", total_count)
print("宽规则送审数：", broad_count)
print("窄规则送审数：", narrow_count)
print("宽规则误报：", sorted(broad_review_ids - needs_review_ids))
print("宽规则漏报：", sorted(needs_review_ids - broad_review_ids))
print("窄规则误报：", sorted(narrow_review_ids - needs_review_ids))
print("窄规则漏报：", sorted(needs_review_ids - narrow_review_ids))