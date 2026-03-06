-- 코드를 입력하세요
-- SELECT CATEGORY, MAX_PRICE, PRODUCT_NAME



select f.CATEGORY, m.MAX_PRICE, f.PRODUCT_NAME
from FOOD_PRODUCT f, (select f.CATEGORY, max(PRICE) as MAX_PRICE
                    from FOOD_PRODUCT f
                    where f.CATEGORY in ('과자', '국', '김치', '식용유')
                    group by f.CATEGORY) m
where m.CATEGORY = f.CATEGORY and m.MAX_PRICE = f.PRICE
order by m.MAX_PRICE desc;