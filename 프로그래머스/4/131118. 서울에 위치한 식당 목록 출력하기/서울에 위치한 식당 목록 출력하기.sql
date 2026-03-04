with temp as (
    select rr.REST_ID as REST_ID, round(avg(rr.REVIEW_SCORE), 2) as SCORE
    from rest_review as rr
    group by REST_ID
) 
select ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, temp.SCORE as SCORE
FROM REST_INFO as ri, temp
WHERE ri.ADDRESS like "서울%" and temp.REST_ID = ri.REST_ID
ORDER BY SCORE DESC, ri.FAVORITES DESC;