## Q : Modifier le code pour que l’application utilise des variables environnementales à la place des identifiants et mot de passes écrits en dur dans le fichier docker-compose.yml

## R : 
create .env-file with :
```bash
POSTGRES_USERR=root
POSTGRES_PASSWORDD=root
POSTGRES_DBB=root
```
and in the script.sh
```bash
    environment:
      - POSTGRES_USER=${POSTGRES_USRERR}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORDD}
      - POSTGRES_DB=${POSTGRES_DBB}
```
and I run my build command : 
```bash
docker-compose --env-file .env-file up --build
```