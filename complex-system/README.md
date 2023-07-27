### Création du volume

```bash
docker volume create storage
```


### Build et run du scraper
```bash
docker build -t scraper . 
```

```bash
docker run -v storage:/usr/src/app/data scraper
```

### Build et run du cleaner
```bash
docker build -t cleaner . 
```

```bash
docker run -v storage:/usr/src/app/data cleaner
```


### Vérification

**ON DOIT UTILISER UN AUTRE CONTENEUR POUR VERIFIER SI LES DONNEES SONT DANS LE VOLUME**

```bash
docker run -it -v storage:/usr/src/app/data bash
cd usr/src/app/data
ls scraped
ls cleaned
```