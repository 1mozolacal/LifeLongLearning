CREATE TABLE UserAccount(
userId int CONSTRAINT pk_useraccount_userid PRIMARY KEY,
Username varchar(32),
password varchar(255),
lastUpdated TIMESTAMP NOT NULL
);

CREATE TABLE Event(
eventId int CONSTRAINT pk_event_eventid PRIMARY KEY,
eventDate TIMESTAMP NOT NULL,
eventDescription  varchar(255),
hostedBy int,
CONSTRAINT fk_event_hostedby
    FOREIGN KEY (hostedby)  
    REFERENCES UserAccount(userID)
    ON DELETE Cascade
);


CREATE TABLE Sighting(
sightId int NOT NULL UNIQUE,
title varchar(63),
notes varchar(500), 
latLoc float,
longLoc float,
lastUpdated TIMESTAMP NOT NULL,
timeRecorded  TIMESTAMP NOT NULL,
sightedBy int,
partOfEvent int,
CONSTRAINT fk_sighting_sightedby 
    FOREIGN KEY (sightedBy)  
    REFERENCES UserAccount(userID)
    ON DELETE CASCADE,
CONSTRAINT fk_sighting_partofevent 
    FOREIGN KEY (partOfEvent)  
    REFERENCES Event(eventId)
    ON DELETE SET NULL
);

CREATE TABLE UserSightingSaved(
savedOn TIMESTAMP,
savedBy int,
sightingId int,
CONSTRAINT fk_uss_savedby
    FOREIGN KEY (savedBy)  
    REFERENCES UserAccount(userId)
    ON DELETE CASCADE,
CONSTRAINT fk_uss_sightingid 
    FOREIGN KEY (sightingId)
    REFERENCES Sighting(sightId)
    ON DELETE CASCADE
);

CREATE TABLE SightingComment (
commentId int,
content  varchar(2047),
postTime TIMESTAMP,
createdBy int,
onSighting int,
CONSTRAINT fk_sightingcomment_createdby
    FOREIGN KEY (createdBy)  
    REFERENCES UserAccount(userId)
    ON DELETE CASCADE,
CONSTRAINT fk_sightingcomment_onsighting 
    FOREIGN KEY (onSighting)
    REFERENCES Sighting(sightId)
    ON DELETE CASCADE,
CONSTRAINT pk_sightingcomment_commentid PRIMARY KEY (commentId)
);

CREATE TABLE Attends(
eventId int,
personId int, 
CONSTRAINT fk_attends_event
    FOREIGN KEY (eventId)
    REFERENCES Event(eventId)
    ON DELETE CASCADE,
CONSTRAINT fk_attends_personid
    FOREIGN KEY  (personId)
    REFERENCES UserAccount(userId)
    ON DELETE CASCADE
);

CREATE TABLE Animal(
 animalId int,
 diet varchar(255),
 name varchar(255),
 description varchar(255),
 animalType varchar(255) ,
CONSTRAINT pk_animal_animalid PRIMARY KEY (animalId)
);

CREATE TABLE Plant(
plantId int,
name varchar(255),
scientificName varchar(255),
averageHeight NUMERIC(8),
plantDescription varchar(255),
fruitBearing NUMERIC(1),
lightRequirement varchar(255),
waterRequirement varchar(255),
leafType varchar(255),
plantType varchar(255),
CONSTRAINT pk_plant_plantid PRIMARY KEY(plantId)
);

CREATE TABLE AnimalSighting(
sightId int,
animalType int,
seasonalBehavior varchar(255),
health varchar(255),
herdSize int,
CONSTRAINT fk_animalsighting_sightid
    FOREIGN KEY (sightId)
    REFERENCES Sighting(sightId) 
    ON DELETE CASCADE,
CONSTRAINT fk_animalsighting_animaltype
    FOREIGN KEY (animalType)
    REFERENCES Animal(animalId)
    ON DELETE CASCADE,
CONSTRAINT sighId_pk PRIMARY KEY( sightId)
);

CREATE TABLE PlantSighting(
sightId int REFERENCES sighting(sightId),
soil varchar(255),
height NUMERIC(16),
health varchar(25),
flowering NUMERIC(1),
plantType int,
CONSTRAINT fk_plantsighting_planttype
    FOREIGN KEY (plantType) 
    REFERENCES  Plant(plantId) 
    ON DELETE CASCADE,
CONSTRAINT pk_plantsighting_sightid PRIMARY KEY(sightId)
);

CREATE TABLE ConsumeAnimal(
consumer int,
CONSTRAINT fk_consumeanimal_consumer 
    FOREIGN KEY(consumer) 
    REFERENCES Animal(animalId) 
    ON DELETE CASCADE,
consumed int,
CONSTRAINT fk_consumeanimal_consumed 
    FOREIGN KEY(consumed) 
    REFERENCES Animal(animalId) 
    ON DELETE CASCADE,
herdAttack int,  
scavenger  NUMERIC(1) DEFAULT 0,
CONSTRAINT comsume_pk PRIMARY KEY(consumer, consumed)
);

CREATE TABLE ConsumePlant(
consumer int,
CONSTRAINT fk_consumeplant_consumer 
    FOREIGN KEY(consumer) 
    REFERENCES Animal(animalId) 
    ON DELETE CASCADE,
consumed int,
CONSTRAINT fk_consumeplant_consumed 
    FOREIGN KEY(consumed) 
    REFERENCES Plant(plantId) 
    ON DELETE CASCADE
);

CREATE TABLE Location(
locationId int,
climate varchar(255),
commonName varchar(255),
latLoc float,
longLoc float,
CONSTRAINT pk_location_locationid PRIMARY KEY(locationId)
);

CREATE TABLE Flag(
flagId int,
CONSTRAINT fk_flag_flagid
    FOREIGN KEY(flagId)
    REFERENCES Sighting(sightId) 
    ON DELETE CASCADE,
colour char(6),
dangerLevel int,
latLoc float,
longLoc float,
type char(1),
referenceType int,
CONSTRAINT pk_flag_flagid PRIMARY KEY(flagId)
);

CREATE TABLE Lives(
plant int,
animal int,
location int,
CONSTRAINT fk_lives_plant
    FOREIGN KEY(plant)
    REFERENCES Plant(plantId)
    ON DELETE CASCADE,
CONSTRAINT fk_lives_animal
    FOREIGN KEY(animal)
    REFERENCES Animal(animalId)
    ON DELETE CASCADE,
CONSTRAINT fk_lives_location
    FOREIGN KEY(location)
    REFERENCES Location(locationId)
    ON DELETE CASCADE
);
