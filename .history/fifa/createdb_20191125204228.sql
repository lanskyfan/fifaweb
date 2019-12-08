show databases;
use fifadata;
show tables;

drop table fulldata;
CREATE TABLE `fifadata`.`fulldata` (
  `ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Age` INT NOT NULL,
  `Photo` VARCHAR(45) NOT NULL,
  `Nationality` VARCHAR(45) NOT NULL,
  `Flag` VARCHAR(45) NOT NULL,
  `Overall` INT NOT NULL,
  `Potential` INT NOT NULL,
  `Club` VARCHAR(45) NOT NULL,
  `Club_logo` VARCHAR(45) NOT NULL,
  `Value` VARCHAR(45) NOT NULL,
  `Wage` VARCHAR(45) NOT NULL,
  `preferred_foot` VARCHAR(45) NOT NULL,
  `international_reputation` INT NOT NULL,
  `weak_foot` INT NOT NULL,
  `skill_move` INT NOT NULL,
  `Position` VARCHAR(5) NOT NULL,
  `height` float8 NOT NULL,
  `weight` INT NOT NULL,
  `Crossing` INT NOT NULL,
  `Finishing` INT NOT NULL,
  `HeadingAccuracy` INT NOT NULL,
  `ShortPassing` INT NOT NULL,
  `Volleys` INT NOT NULL,
  `Dribbling` INT NOT NULL,
  `Curve` INT NOT NULL,
  `FKAccuracy` INT NOT NULL,
  `LongPassing` INT NOT NULL,
  `BallControl` INT NOT NULL,
  `Acceleration` INT NOT NULL,
  `SprintSpeed` INT NOT NULL,
  `Agility` INT NOT NULL,
  `Reactions` INT NOT NULL,
  `Balance` INT NOT NULL,
  `ShotPower` INT NOT NULL,
  `Jumping` INT NOT NULL,
  `Stamina` INT NOT NULL,
  `Strength` INT NOT NULL,
  `LongShots` INT NOT NULL,
  `Aggression` INT NOT NULL,
  `Interceptions` INT NOT NULL,
  `Positioning` INT NOT NULL,
  `Vision` INT NOT NULL,
  `Penalties` INT NOT NULL,
  `Composure` INT NOT NULL,
  `Marking` INT NOT NULL,
  `StandingTackle` INT NOT NULL,
  `SlidingTackle` INT NOT NULL,
  `GKDiving` INT NOT NULL,
  `GKHandling` INT NOT NULL,
  `GKKicking` INT NOT NULL,
  `GKPositioning` INT NOT NULL,
  `GKReflexes` INT NOT NULL,
  `nation_id` INT NOT NULL,
  `club_id` INT NOT NULL,
  `defending` INT NOT NULL,
  `pace` INT NOT NULL,
  `passing` INT NOT NULL,
  `dribbling2` INT NOT NULL,
  `shooting` INT NOT NULL,
  `physical` INT NOT NULL,
  `gk` INT NOT NULL,
  PRIMARY KEY (`ID`));

LOAD DATA LOCAL INFILE '/home/ubuntu/data/fifa19data4.csv'
INTO TABLE fulldata character set utf8
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;


select * from fulldata;

drop table player;
CREATE TABLE `fifadata`.`player` (
  `ID` INT NOT NULL,
  `name` VARCHAR(25) NOT NULL,
  `age` INT NOT NULL,
  `height` float8 NOT NULL,
  `weight` INT NOT NULL,
  `nation_id` INT NOT NULL,
  `club_id` INT NOT NULL,
  `photo` VARCHAR(20) NOT NULL,
  `overall` INT NOT NULL,
  `potential` INT NOT NULL,
  `value` VARCHAR(10) NOT NULL,
  `wage` VARCHAR(10) NOT NULL,
  `preferred_foot` VARCHAR(5) NOT NULL,
  `international_reputation` INT NOT NULL,
  `weak_foot` INT NOT NULL,
  `skill_move` INT NOT NULL,
  `position` VARCHAR(5) NOT NULL,
  PRIMARY KEY (`ID`));
  
INSERT INTO player
select ID, name, age, height, weight, nation_id, club_id, photo, overall, potential, 
value, wage, preferred_foot, international_reputation, weak_foot, skill_move, position
from fulldata;
select count(*) from player;
 
drop table nation; 
CREATE TABLE `fifadata`.`nation` (
  `nation_id` INT NOT NULL,
  `nationality` VARCHAR(25) NOT NULL,
  `flag` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`nation_id`));

INSERT INTO nation
select distinct nation_id, nationality, flag
from fulldata;
select * from nation;

drop table club;
CREATE TABLE `fifadata`.`club` (
  `club_id` INT NOT NULL,
  `club_name` VARCHAR(40) NOT NULL,
  `logo` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`club_id`));
  
INSERT INTO club
select distinct club_id, club, club_logo
from fulldata;
select * from club;

drop table rating;
CREATE TABLE `fifadata`.`rating` (
  `ID` INT NOT NULL,
  `pace_score` INT NOT NULL,
  `shooting_score` INT NOT NULL,
  `passing_score` INT NOT NULL,
  `defending_score` INT NOT NULL,
  `dribbling_score` INT NOT NULL,
  `physical_score` INT NOT NULL,
  `GK_score` INT NOT NULL,
  PRIMARY KEY (`ID`));
  
INSERT INTO rating
select ID, pace, shooting, passing, defending, dribbling2, physical, GK
from fulldata;
select * from rating;
  
drop table physical;  
CREATE TABLE `fifadata`.`physical` (
  `ID` INT NOT NULL,
  `jumping` INT NOT NULL,
  `stamina` INT NOT NULL,
  `strength` INT NOT NULL,
  `aggression` INT NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO physical 
select ID, jumping, stamina, strength, aggression
from fulldata;
select * from physical;

drop table defending;
CREATE TABLE `fifadata`.`defending` (
  `ID` INT NOT NULL,
  `interceptions` INT NOT NULL,
  `headingaccuracy` INT NOT NULL,
  `marking` INT NOT NULL,
  `standing_tackle` INT NOT NULL,
  `sliding_tackle` INT NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO defending 
select ID, interceptions, headingaccuracy, marking, standingtackle, slidingtackle
from fulldata;
select * from defending;

drop table passing;
CREATE TABLE `fifadata`.`passing` (
  `ID` INT NOT NULL,
  `vision` INT NOT NULL,
  `crossing` INT NOT NULL,
  `FK_accuracy` INT NOT NULL,
  `short_passing` INT NOT NULL,
  `long_passing` INT NOT NULL,
  `curve` INT NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO passing 
select ID,vision,crossing,FKAccuracy,shortpassing,longpassing,curve
from fulldata;
select * from passing;

drop table pace;
CREATE TABLE `fifadata`.`pace` (
  `ID` INT NOT NULL,
  `acceleration` INT NOT NULL,
  `sprint_speed` INT NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO pace
select ID, acceleration, sprintspeed
from fulldata;
select * from pace;

drop table shooting;
CREATE TABLE `fifadata`.`shooting` (
  `ID` INT NOT NULL,
  `positioning` VARCHAR(45) NOT NULL,
  `finishing` VARCHAR(45) NOT NULL,
  `shot_power` VARCHAR(45) NOT NULL,
  `long_shots` VARCHAR(45) NOT NULL,
  `volleys` VARCHAR(45) NOT NULL,
  `penalties` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));
  
INSERT INTO shooting
select ID, positioning, finishing, shotpower, longshots, volleys, penalties
from fulldata;
select * from shooting;

drop table dribbling2;
CREATE TABLE `fifadata`.`dribbling2` (
  `ID` INT NOT NULL,
  `agility` INT NOT NULL,
  `balance` INT NOT NULL,
  `reactions` INT NOT NULL,
  `ball_control` INT NOT NULL,
  `dribbling` INT NOT NULL,
  `composure` INT NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO dribbling2
select ID, agility, balance, reactions, ballcontrol, dribbling,composure
from fulldata;
select * from dribbling2;
  
drop table GK;
CREATE TABLE `fifadata`.`GK` (
  `ID` INT NOT NULL,
  `GK_handling` INT NOT NULL,
  `GK_kicking` INT NOT NULL,
  `GK_positioning` INT NOT NULL,
  `GK_reflexes` INT NOT NULL,
  PRIMARY KEY (`ID`));

INSERT INTO GK
select ID, GKhandling,GKkicking, GKpositioning, GKreflexes
from fulldata;
select * from GK;




SHOW GLOBAL VARIABLES LIKE 'local_infile';
show variables like 'secure_file_priv';


select * from player
where name like "%ISco";





