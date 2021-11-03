Foi usado:
```virtualenv .venv```
para criar o ambiente virtual de python3 (container).

Para usar este ambiente executamos:
```source .venv/bin/activate``` (UNIX-like) ou ```.\.venv\scripts\activate``` (NT/Win32)

Para actualizar a lista de pacotes:
```pip freeze > requirements.txt```

Para instalar os pacotes do ambiente:
```pip install -r requirements.txt```

Para sair do ambiente virtual:
````deactivate```
