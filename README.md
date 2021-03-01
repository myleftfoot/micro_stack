# Micro Service Stack

This is my sample micro service stack that I use to capture sensor data from my micro services and iot devices.

## Create external volumns
```
mkdir -p $PWD/data/influxdb
mkdir -p $PWD/data/grafana

docker volume create --driver local --opt type=none --opt device=$PWD/data/influxdb --opt o=bind influxdb-storage
docker volume create --driver local --opt type=none --opt device=$PWD/data/grafana --opt o=bind grafana-storage
```

## Docker Compose
```
FLUX_TOKEN=$(uuidgen) docker-compose up
```

## Docker Swarm
```
# docker swarm init  
FLUX_TOKEN=$(uuidgen) docker stack deploy -c docker-compose.yml dev
```