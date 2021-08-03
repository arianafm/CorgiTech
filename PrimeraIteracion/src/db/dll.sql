/* Si la base de datos 'mercatodo' existe, la borramos. */
DROP DATABASE IF EXISTS mercatodo;

/* Creamos la base de datos 'mercatodo'. */
CREATE DATABASE mercatodo CHARACTER SET utf8mb4;

/* Accesamos a la base de datos 'mercatodo'. */
USE mercatodo;

/*
* Tabla para un usuario.
*/
CREATE TABLE usuario (
  usuario VARCHAR(20) NOT NULL,
  correo VARCHAR(50) NOT NULL,
  telefono CHAR(10) NOT NULL,
  contrasena VARCHAR(250) NOT NULL,
  CONSTRAINT PK_usuarioUsuario PRIMARY KEY (usuario),
  CONSTRAINT unique_usuario UNIQUE (usuario),
  CONSTRAINT unique_correo UNIQUE (correo)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/* 
* Tabla para un producto
*/
CREATE TABLE producto (
  id INT UNSIGNED AUTO_INCREMENT NOT NULL,
  nombre VARCHAR(25) NOT NULL,
  descripcion VARCHAR(5000) NOT NULL,
  imagen VARCHAR(2000) NOT NULL,
  precio INT UNSIGNED NOT NULL,
  palabras_clave VARCHAR(250) NOT NULL,
  cantidad_vendidos INT NOT NULL,
  CONSTRAINT PK_idProducto PRIMARY KEY (id),
  CONSTRAINT check_precio CHECK (precio >= 0),
  CONSTRAINT check_cantidadVendidos CHECK(cantidad_vendidos >= 0)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


/*
* Creamos tabla para la relación opinar. Usuario opina sobre un producto.
*/
CREATE TABLE opinar (
  usuario VARCHAR(20) NOT NULL,
  id_producto INT UNSIGNED NOT NULL,
	calificaión VARCHAR(1) NOT NULL,
  comentario VARCHAR(300),
  CONSTRAINT PK_opinar PRIMARY KEY (usuario, id_producto),
  CONSTRAINT FK_usuarioOpinar FOREIGN KEY (usuario) REFERENCES usuario(usuario) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK_idProductoOpinar FOREIGN KEY (id_producto) REFERENCES producto(id) ON UPDATE CASCADE ON DELETE CASCADE
);

/* 
* Creamos la tabla comprar cuya llave primaria será usuario. 
*/
CREATE TABLE comprar (
  usuario VARCHAR(20) NOT NULL,
  id_producto INT UNSIGNED NOT NULL,
  CONSTRAINT PK_comprar PRIMARY KEY (usuario, id_producto),
  CONSTRAINT FK_usuarioComprar FOREIGN KEY (usuario) REFERENCES usuario(usuario)  ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK_idProductoComprar FOREIGN KEY (id_producto) REFERENCES producto(id) ON UPDATE CASCADE ON DELETE CASCADE
);

/* 
* Creamos la tabla actualizar cuya llave primaria será usuario. 
*/
CREATE TABLE actualizar (
  usuario VARCHAR(20) NOT NULL,
  id_producto INT UNSIGNED NOT NULL,
  CONSTRAINT PK_actualizar PRIMARY KEY (usuario, id_producto),
	CONSTRAINT FK_usuarioActualizar FOREIGN KEY (usuario) REFERENCES usuario(usuario) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK_idProductoActualizar FOREIGN KEY (id_producto) REFERENCES producto(id) ON UPDATE CASCADE ON DELETE CASCADE
);

/* 
* Creamos la tabla borrar cuya llave primaria será usuario. 
*/
CREATE TABLE borrar (
  usuario VARCHAR(20) NOT NULL,
  id_producto INT UNSIGNED NOT NULL,
  CONSTRAINT PK_borrar PRIMARY KEY (usuario, id_producto),
  CONSTRAINT FK_usuarioBorrar FOREIGN KEY (usuario) REFERENCES usuario(usuario) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK_idProductoBorrar FOREIGN KEY (id_producto) REFERENCES producto(id) ON UPDATE CASCADE ON DELETE CASCADE
);

/* 
* Creamos la tabla crear cuya llave primaria será usuario. 
*/
CREATE TABLE crear (
  usuario VARCHAR(20) NOT NULL,
  id_producto INT UNSIGNED NOT NULL,
  CONSTRAINT PK_crear PRIMARY KEY (usuario, id_producto),
  CONSTRAINT FK_usuarioCrear FOREIGN KEY (usuario) REFERENCES usuario(usuario) ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT FK_idProductoCrear FOREIGN KEY (id_producto) REFERENCES producto(id) ON UPDATE CASCADE ON DELETE CASCADE
);
