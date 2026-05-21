CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR, 
	email VARCHAR, 
	password VARCHAR, 
	puntos INTEGER, 
	nivel INTEGER, 
	PRIMARY KEY (id)
);
CREATE UNIQUE INDEX ix_users_email ON users (email);
CREATE INDEX ix_users_username ON users (username);
CREATE INDEX ix_users_id ON users (id);
CREATE TABLE cursos (
	id INTEGER NOT NULL, 
	title VARCHAR NOT NULL, 
	description TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_cursos_id ON cursos (id);
CREATE TABLE foro (
	id INTEGER NOT NULL, 
	nombre VARCHAR, 
	descripcion VARCHAR, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_foro_id ON foro (id);
CREATE TABLE estado_sesion (
	id INTEGER NOT NULL, 
	estado VARCHAR, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_estado_sesion_id ON estado_sesion (id);
CREATE TABLE recompensas (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	nombre VARCHAR, 
	fecha VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id)
);
CREATE INDEX ix_recompensas_id ON recompensas (id);
CREATE TABLE logros (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	titulo VARCHAR, 
	fecha VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id)
);
CREATE INDEX ix_logros_id ON logros (id);
CREATE TABLE habilidades (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	nivel INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id)
);
CREATE INDEX ix_habilidades_id ON habilidades (id);
CREATE TABLE manejo_sesion (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	estado_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id), 
	FOREIGN KEY(estado_id) REFERENCES estado_sesion (id)
);
CREATE INDEX ix_manejo_sesion_id ON manejo_sesion (id);
CREATE TABLE vidas (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	vidas_actuales INTEGER, 
	tiempo_recarga INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id)
);
CREATE INDEX ix_vidas_id ON vidas (id);
CREATE TABLE unidades (
	id INTEGER NOT NULL, 
	curso_id INTEGER, 
	titulo VARCHAR, 
	estado VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(curso_id) REFERENCES cursos (id)
);
CREATE INDEX ix_unidades_id ON unidades (id);
CREATE TABLE temas (
	id INTEGER NOT NULL, 
	foro_id INTEGER, 
	titulo VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(foro_id) REFERENCES foro (id)
);
CREATE INDEX ix_temas_id ON temas (id);
CREATE TABLE inscripciones (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	curso_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id), 
	FOREIGN KEY(curso_id) REFERENCES cursos (id)
);
CREATE INDEX ix_inscripciones_id ON inscripciones (id);
CREATE TABLE respuestas (
	id INTEGER NOT NULL, 
	tema_id INTEGER, 
	contenido VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(tema_id) REFERENCES temas (id)
);
CREATE INDEX ix_respuestas_id ON respuestas (id);
CREATE TABLE lecciones (
	id INTEGER NOT NULL, 
	titulo VARCHAR, 
	contenido VARCHAR, 
	curso_id INTEGER, 
	unidad_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(curso_id) REFERENCES cursos (id), 
	FOREIGN KEY(unidad_id) REFERENCES unidades (id)
);
CREATE INDEX ix_lecciones_id ON lecciones (id);
CREATE TABLE ejercicios (
	id INTEGER NOT NULL, 
	leccion_id INTEGER, 
	tipo VARCHAR, 
	contenido VARCHAR, 
	respuesta_correcta VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(leccion_id) REFERENCES lecciones (id)
);
CREATE INDEX ix_ejercicios_id ON ejercicios (id);
CREATE TABLE progreso (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	leccion_id INTEGER, 
	porcentaje_completado FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id), 
	FOREIGN KEY(leccion_id) REFERENCES lecciones (id)
);
CREATE INDEX ix_progreso_id ON progreso (id);
CREATE TABLE intentos (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	ejercicio_id INTEGER, 
	validacion_respuesta VARCHAR, 
	fecha VARCHAR, 
	tiempo VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES users (id), 
	FOREIGN KEY(ejercicio_id) REFERENCES ejercicios (id)
);
CREATE INDEX ix_intentos_id ON intentos (id);
