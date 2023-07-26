import os

env_var = os.environ.get("VAR_FROM_DOCKER", "Valeur par défaut")

print(env_var)

import time

