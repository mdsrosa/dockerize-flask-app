Example project with Flask and Redis running with Docker.

Featuring:

 - Docker
 - Docker Compose
 - Docker Machine
 - Python 3.5
 - Flask
 - Redis

If you don't already have Docker on OS X: [Docker Toolbox](https://docs.docker.com/engine/installation/mac/#/docker-toolbox)

## Redis Master Instance
##### Inside `redis-master` directory:
1. Start new machine (`$ docker-machine -d virtualbox redis-master`)
2. Active machine (`$ eval $(docker-machine env redis-master)`)
3. Build images (`$ docker-compose build`)
4. Start service (`$ docker-compose up`)

## Redis Slave Instance
##### Inside `redis-slave` directory:
1. Start new machine (`$ docker-machine -d virtualbox redis-slave`)
2. Active machine (`$ eval $(docker-machine env redis-slave)`)
3. Build images (`$ docker-compose build`)
4. Start service (`$ docker-compose up`)

## Flask app
1. Start new machine (`$ docker-machine -d virtualbox flask-app`)
2. Activate machine (`$ eval $(docker-machine env flask-app)`)
3. Build images (`$ docker-compose build`)
4. Start services (`$ docker-compose up`)
5. Grab IP (`$ docker-machine ip flask-app`) and view in your browser
