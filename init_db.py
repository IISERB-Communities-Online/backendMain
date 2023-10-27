DB_INIT_QUERIES = '''
CREATE TYPE "Role" AS ENUM (
    'Advisor',
    'Coordinator',
    'Core Committee',
    'Volunteer Committee',
    'Member'
);

CREATE TABLE "Clubs" (
    "_id" SERIAL PRIMARY KEY,
    "name" varchar(64) NOT NULL,
    "label" varchar(16) NOT NULL,
    "description" text,
    "logo" image
);

CREATE TABLE "Members" (
    "_id" SERIAL PRIMARY KEY,
    "roll_no" integer NOT NULL,
    "name" varchar(64) NOT NULL,
    "role" Role NOT NULL,
    "description" text,
    "club_id" integer NOT NULL,
    "picture" image
);

CREATE TABLE "Events" (
    "_id" SERIAL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "venue" varchar(64),
    "time" timestamp,
    "end_time" timestamp DEFAULT null,
    "poster" image
);

CREATE TABLE "ev_cb" (
    "event_id" integer NOT NULL,
    "club_id" integer NOT NULL
);

CREATE INDEX "ev_cbId_index" ON "ev_cb" ("club_id");

CREATE INDEX "cb_evId_index" ON "ev_cb" ("event_id");

CREATE INDEX "mem_roll_no_indez" ON "Members" ("roll_no");

CREATE INDEX "mem_club_id_index" ON "Members" ("club_id");

CREATE INDEX "club_n_role" ON "Members" ("club_id", "role");

COMMENT ON COLUMN "Clubs"."name" IS 'Full name of the Club';

COMMENT ON COLUMN "Clubs"."label" IS 'Can be acronym of the club name';

COMMENT ON TABLE "Events" IS 'Events that are live/past';

COMMENT ON TABLE "Members" IS 'Members of the club';

ALTER TABLE "Members" ADD FOREIGN KEY ("club_id") REFERENCES "Clubs" ("_id");

ALTER TABLE "ev_cb" ADD FOREIGN KEY ("club_id") REFERENCES "Clubs" ("_id");

ALTER TABLE "ev_cb" ADD FOREIGN KEY ("event_id") REFERENCES "Events" ("_id");

'''