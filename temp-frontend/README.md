CREATE TABLE temperatures (
  epoch BIGINT PRIMARY KEY,
  temp float(16),
  temp_hum float(16),
  temp_pres float(16),
  pressure float(16),
  humidity float(16),
  temp_calibrated float(16),
  cpu_tmp float(16)
);


\copy temperatures FROM '/var/lib/postgresql/tempratures.csv' DELIMITER ',' CSV HEADER;
CREATE USER grafana WITH PASSWORD '';
GRANT ALL PRIVILEGES ON TABLE temperatures TO grafana;

# update db
docker exec -it postgres bash -c 'cd var/lib/postgresql && psql -U postgres -a -f update_temp_table.sql'
