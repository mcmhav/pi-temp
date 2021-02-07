CREATE TEMP TABLE tmp_table
AS
SELECT *
FROM temperatures
WITH NO DATA;

COPY tmp_table FROM '/var/lib/postgresql/tempratures.csv' DELIMITER ',' CSV HEADER;

INSERT INTO temperatures
SELECT *
FROM tmp_table
ON CONFLICT DO NOTHING;

DROP TABLE tmp_table;

