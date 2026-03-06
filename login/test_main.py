import pytest
from main import validar_usuario, Usuario
from exceptions import NombreInvalidoError, EdadInvalidaError

class TestUsuario:
    def test_registro_valido(self):
        u = Usuario(nombre="Ana", edad=25, correo="ana@correo.com")
        validar_usuario(u)

    def test_nombre_vacio(self):
        with pytest.raises(NombreInvalidoError):
            u = Usuario(nombre="   ", edad=25, correo="ana@correo.com")
            validar_usuario(u)

    def test_edad_invalida(self):
        with pytest.raises(EdadInvalidaError):
            u = Usuario(nombre="Ana", edad=-1, correo="ana@correo.com")
            validar_usuario(u)

    def test_correo_invalido(self):
        with pytest.raises(Exception):
            Usuario(nombre="Ana", edad=25, correo="correo_malo")