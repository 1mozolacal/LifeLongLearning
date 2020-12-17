-- Selects all event that contain atleast sighting
-- note that event 6 does not show up as it 
SELECT * FROM Event e
WHERE EXISTS
(SELECT * FROM Sighting s
WHERE e.eventId = s.partofevent); 

-- selection all sighting in a lat,long 'box'
SELECT * FROM sighting
where latloc > 20
and latloc < 80
and longloc > -60
and longloc < -35;

--select statement that will return calculated values for herdsize of the sighted animals
SELECT animaltype AS animal,
AVG(herdsize) as Average, 
MIN(herdsize) as Miniume,
MAX(herdsize) as Maxium, 
VARIANCE(herdsize) as Variance, 
ROUND(stddev(herdsize),2) as StandardDeivation 
FROM animalsighting
GROUP BY animaltype;

--Select flags and inner joins them with the correct sighting
SELECT * FROM Flag
INNER JOIN Sighting
ON Flag.flagId = Sighting.sightId;

--Select sighting and left joins them with the correct comments 
SELECT Sighting.Title, SightingComment.Content FROM Sighting
LEFT JOIN SightingComment ON Sighting.SightId = SightingComment.onSighting WHERE CONTENT IS NOT NULL;

SELECT UserAccount.Username, Sighting.Title, Sighting.Notes, SightingComment.Content
FROM ((UserAccount
INNER JOIN Sighting ON UserAccount.UserId = Sighting.SightedBy)
INNER JOIN SightingComment ON Sighting.sightid = SightingComment.onsighting);

--Selects users, their sightings’ contents, and the comments on them
SELECT Sighting.Title, Sighting.Notes, UserAccount.Username AS Commentor, SightingComment.Content, SightingComment.posttime
FROM ((SightingComment
INNER JOIN Sighting ON Sighting.sightId = SightingComment.onSighting)
INNER JOIN UserAccount ON UserAccount.userId = SightingComment.CreatedBy) ORDER BY SightingComment.posttime;

--Shows what events are being hosted by who that are happening in the future
SELECT  eventDate, Username, eventDescription, eventId FROM UserAccount LEFT JOIN Event ON UserAccount.userId = Event.hostedBy
WHERE Event.eventDate > CURRENT_TIMESTAMP ORDER BY Event.eventDate;
