<code>docker volume create test</code>
docker run -v test:/usr/src scaper

docker run -d -v test:/usr/src scraper

docker run -it -v test:/usr/src bash

avec le volume

![csv dans vol scraping](https://github.com/AxelML2/docker-1/assets/140382386/60d9aec9-9e38-4b2b-aa18-e4aa2221b327)

sans le volume

![csv sans le vol scraping](https://github.com/AxelML2/docker-1/assets/140382386/43b22061-222f-4b94-b98d-17555aa8243f)
