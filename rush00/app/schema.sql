CREATE TABLE IF NOT EXISTS Users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	username TEXT NOT NULL,
	email TEXT NOT NULL,
	pw_hash TEXT NOT NULL,
	admin INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Orders (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user INTEGER NOT NULL,
	contents TEXT NOT NULL,
	FOREIGN KEY(user) REFERENCES Users(id)
);
