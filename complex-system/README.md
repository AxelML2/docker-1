```
docker volume create test
```

```
docker run -d -v test:/usr/src scraper
```

```
docker run -it -v test:/usr/src bash
```

#### Proof that I use only the volume and not the container


![csv dans vol scraping](https://github.com/AxelML2/docker-1/assets/140382386/60d9aec9-9e38-4b2b-aa18-e4aa2221b327)


![csv sans le vol scraping](https://github.com/AxelML2/docker-1/assets/140382386/43b22061-222f-4b94-b98d-17555aa8243f)
