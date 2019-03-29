BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "MUSIC" (
	"Id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"file_id"	VARCHAR(50),
	"right_answer"	VARCHAR(50),
	"wrong_answer"	VARCHAR(50)
);
INSERT INTO "MUSIC" VALUES (1,'02 Live Sheck Wes-cropped','Sheck Wes - Live Sheck Wes','2pac - All eyez on me, Rick Ross - 911, AFI - 1985');
INSERT INTO "MUSIC" VALUES (2,'07 - Rockabye Baby (feat. ScHoolboy Q)-cropped','Joey Badass - Rockabye Baby (feat. ScHoolboy Q)','Asap Rocky - Angels, Coldplay - Paradise, Flatbush Zombies - Headstone');
INSERT INTO "MUSIC" VALUES (3,'08 - Ring The Alarm (feat. Kirk Knight, Nyck Caution & Meechy Darko)-cropped','Joey Badass - Ring The Alarm (feat. Kirk Knight, Nyck Caution & Meechy Darko)','Schoolboy Q - Break the bank, Eminem - The Ringer, Lil Wayne - Dont Cry');
INSERT INTO "MUSIC" VALUES (4,'09 Mo Bamba-cropped','Sheck Wes - Mo Bamba','Vince Staples - Yeah Right, Dr.Dre The Next Episode, J.Cole - Wet Dreams');
INSERT INTO "MUSIC" VALUES (5,'A3 Survival Of The Fittest-cropped','Mobb Deep - Survival Of The Fittest','Skepta - Ghost Ride, Devin The Dude - What a Job, Jamie XX - See Saw ');
COMMIT;
