SELECT LobbyistInfo.Lobbyist_ID, LobbyistInfo.First_Name, 
LobbyistInfo.Last_Name, LobbyistInfo.Phone,
SUM(Compensation.Compensation_Amount) as totalComp
FROM LobbyistInfo
JOIN Compensation
ON LobbyistInfo.Lobbyist_ID = Compensation.Lobbyist_ID
JOIN ClientInfo
ON Compensation.Client_ID = ClientInfo.Client_ID
WHERE strftime('%Y', date(Period_End)) = '2019'
GROUP BY LobbyistInfo.Lobbyist_ID
ORDER BY totalComp DESC
LIMIT 10;

SELECT Client_Name
FROM ClientInfo 
JOIN Compensation
ON ClientInfo.Client_ID = Compensation.Client_ID
JOIN LobbyistInfo
ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
WHERE LobbyistInfo.Lobbyist_ID = '14921'
AND strftime('%Y', date(Period_End)) = '2019'
GROUP BY ClientInfo.Client_ID
ORDER BY Client_Name ASC;
