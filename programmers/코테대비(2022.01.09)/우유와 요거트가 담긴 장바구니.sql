SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Yogurt' OR NAME = 'Milk'
GROUP BY CART_ID
HAVING COUNT(DISTINCT(NAME)) = 2 -- CART_ID에 Milk나 Yogurt가 여러번 들어갈 수 있기 때문에
ORDER BY CART_ID
