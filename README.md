# ProyectoPracticas

## Descripcion 
Identificacion de outliers en la plataforma SIMEME aplicando metodos estadisticos y machine learning para observar y comparar su eficiencia, generando una separacion y notificacion al usuario final.

### Instalacion de Ambiente virtual y dependencias.
#### Primer Metodo
1. Abrir VScode
2. En consola instalar: virtualenv (pip install virtualenv)

%%% La instalacion de esta libreria es opcional, despues se explicara otro metodo para insatalar un ambiente virtual %%%

4. Consola escribir: virtualenv -p python < Nombre del ambiente >
5. Con esto seguira la activacion del ambiente, el comando sera: .\ < Nombre del ambiente >\Script\activate (Sin espacios)
6. Si todo salio bien en su Terminal debera de aparecer algo tal que : (< Nombre del ambiente >) PS D: ....
Entienda que en este caso es PS D: debido a que es el lugar donde esta instalado py, en su caso podria aparecer C: u otras letras. (Dado el caso en tener particiones en el disco o tener varios discos en el pc esta letra variara)
 ![Imagen alt](https://github.com/MhyloR/ProyectoPracticas/blob/0ed31e9e5c1f4e49cdeac00faa8d9ecd1747111a/image.png)

#### Segundo Metodo
1. Abrir la consola de VScode
2. Escribir en consola: python -m venv < Nombre del ambiente virtual >
3. Nuevamente escribir en consola: .\ < Nombre del ambiente virtual >\Scripts\Activate.ps1 (Sin espacios)
4. Si todo salio bien deberia de ver esto:
 ![Imagen alt](https://github.com/MhyloR/ProyectoPracticas/blob/0ed31e9e5c1f4e49cdeac00faa8d9ecd1747111a/image.png)

## TIP
Si al activar el ambiente virtual no funciona haz esto:
1. Identifica la carpeta que se creo con el nombre de tu ambiente
2. abre la carpeta de Scrips
3. identifica el archivo Activate.ps1
4. Copia la ruta de este archivo y copiala en el terminal
5. Listo
6. 
##### Como eliminar el ambiente virtual
Simplemente ubique la carpeta dentro de su computador y eliminela o dentro del mismo VScode elimine la carpeta creada.

#### Instalacion de dependencias.
1. Identifique el archivo requirements.txt (El que se encuentra en estos momentos es temporal)
2. En su ambiente virtual ejecute el siguiente comando: pip install -r .\requirements.txt
3. Espere la instalacion.
