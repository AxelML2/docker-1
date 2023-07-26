docker volume create test

docker run -v test:/usr/src scaper

docker run -d -v test:/usr/src scraper

docker run -it -v test:/usr/src bash


