-- report the first login date for each player
SELECT player_id, min(event_date) AS first_login FROM Activity
    GROUP BY player_id;
