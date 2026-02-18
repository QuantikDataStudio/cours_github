-- compter le nombre des rides par mois
SELECT
    strftime('%Y', departure_date) AS year,
    strftime('%m', departure_date) AS month,
    COUNT(*) AS nb_rides
FROM rides
GROUP BY strftime('%m', departure_date), strftime('%Y', departure_date)
ORDER BY nb_rides DESC