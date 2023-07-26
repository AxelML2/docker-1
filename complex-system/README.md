docker volume create test

docker run -v test:/usr/src scaper

docker run -d -v test:/usr/src scraper

docker run -it -v test:/usr/src bash


![csv dans vol scraping](https://github.com/AxelML2/docker-1/assets/140382386/b4e3df93-851f-4796-8735-affc0f94f316)
