CREATE TABLE "Student" (
	`sName`	TEXT,
	`sDorm`	TEXT,
	`SSN`	INTEGER
);

CREATE TABLE "Course" (
	`cNo`	INTEGER,
	`cName`	TEXT,
	`Credits`	INTEGER
);

CREATE TABLE "Schedule" (
	`cNo`	INTEGER,
	`SSN`	INTEGER
);


