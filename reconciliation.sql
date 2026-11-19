-- 查询同币种对账差异
WITH payment_totals AS (SELECT order_id,
       currency,
       COUNT(*) AS payment_count,
       SUM(paid_minor) AS paid_total_minor
FROM payments
GROUP BY order_id,currency
)
SELECT o.order_id,
       o.currency,
       o.expected_minor,
       p.paid_total_minor,
       o.expected_minor - p.paid_total_minor AS diff_minor,
 CASE
    WHEN p.paid_total_minor IS NULL THEN '无同币种付款记录'
    WHEN o.expected_minor = paid_total_minor THEN '金额一致'
    ELSE '金额不一致'
END AS recon_status
FROM orders AS o
LEFT JOIN payment_totals AS p
    ON o.order_id = p.order_id
   AND o.currency= p.currency
WHERE p.paid_total_minor IS NULL
   OR o.expected_minor <> paid_total_minor ;
-- 查询没有付款记录的订单
SELECT orders.order_id,payments.payments_id,payments.paid_minor
from orders
left join payments
on orders.order_id=payments.order_id
where payments_id is null;   
-- 查询重复的渠道流水号
SELECT gateway_ref, COUNT(*) AS record_count
FROM payments
WHERE gateway_ref IS NOT NULL
GROUP BY gateway_ref
HAVING record_count>1;