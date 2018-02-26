CREATE TABLE IF NOT EXISTS Users (
	id integer primary key autoincrement,
	username text not null,
	email text not null,
	pw_hash text not null
);
