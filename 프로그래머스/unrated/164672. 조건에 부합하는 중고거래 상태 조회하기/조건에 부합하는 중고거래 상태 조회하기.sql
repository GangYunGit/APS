-- 코드를 입력하세요
SELECT
    A.BOARD_ID,
    A.WRITER_ID,
    A.TITLE,
    A.PRICE,
    CASE
        WHEN A.STATUS = 'SALE'
            THEN '판매중'
        WHEN A.STATUS = 'RESERVED'
            THEN '예약중'
        ELSE '거래완료'
        END AS STATUS
FROM USED_GOODS_BOARD AS A
WHERE SUBSTR(A.CREATED_DATE, 1, 10) = '2022-10-05'
ORDER BY A.BOARD_ID DESC
