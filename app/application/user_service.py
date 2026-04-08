from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.domain.models.user import User

ph = CryptContext(schemes=["bcrypt"], deprecated="auto")


def obtener_usuario_por_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def verificar_password(password_plano: str, password_hash: str):
    return ph.verify(password_plano, password_hash)


def login_usuario(db: Session, email: str, password: str):
    usuario = obtener_usuario_por_email(db, email)

    if not usuario:
        return None

    if not verificar_password(password, usuario.password):
        return None

    return usuario