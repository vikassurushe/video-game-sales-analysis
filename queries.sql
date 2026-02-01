USE video_game_db;

-- 1. Total number of games
SELECT COUNT(*) AS total_games
FROM merged_game_data;

-- 2. Top 10 highest-rated games
SELECT Title, Rating
FROM merged_game_data
ORDER BY Rating DESC
LIMIT 10;

-- 3. Most reviewed games
SELECT Title, `Number of Reviews`
FROM merged_game_data
ORDER BY `Number of Reviews` DESC
LIMIT 10;

-- 4. Games count by Team
SELECT Team, COUNT(*) AS total_games
FROM merged_game_data
GROUP BY Team
ORDER BY total_games DESC;

-- 5. Most popular games (Times Listed)
SELECT Title, `Times Listed`
FROM merged_game_data
ORDER BY `Times Listed` DESC
LIMIT 10;
