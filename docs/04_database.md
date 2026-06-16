Предлагаю структуру БД

Сразу делаем "на вырост".

# bonds

id
isin
ticker
name

issuer

bond_type

nominal

currency

maturity_date

created_at

# bond_snapshots

Ежедневные данные рынка.

id

bond_id

snapshot_date

market_price

nkd

yield_to_maturity

volume

created_at


# coupons
id

bond_id

coupon_date

coupon_value

# strategy_results

Что нашёл сканер.

id

bond_id

scan_date

expected_profit

expected_yield

days_to_maturity

status

# issuer_analysis

Понадобится позже.
id

bond_id

analysis_date

risk_score

summary

# Что получится в MVP

Каждый вечер:

MOEX
 ↓

bonds

 ↓

bond_snapshots

 ↓

strategy engine

 ↓

strategy_results

 ↓

Telegram