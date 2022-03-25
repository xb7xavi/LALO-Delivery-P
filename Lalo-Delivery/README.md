# Lalo-Delivery
Aplicación web de Lalo Delivery, desarrollo de frontend con conexion a backend mediante Flask

## Instrucciones de instalacion
Para ejecutar el servidor, se debe star en un entorno virtual, en ubuntu se puede instalar con la orden:

```
$ sudo apt-get install python-virtualenv virtualenv
```

Luego hay que crear el entorno virtual usando el comando
```
python3 -m venv env
```

Luego, iniciar el entorno virtual con elcomando
```
source env/bin/activate
```

Y finalmente, instalar los requerimeintos del virtualenv con el comando
```
pip3 install -r requirements.txt
```

Cuando pip haya instalado todos los requerimeintos, se inicia el server con:
```
flask run
```