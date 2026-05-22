from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from app.domain.models.user import User
from app.domain.ports.user_repository import UserRepository
from app.infrastructure.auth.strategy import AuthStrategy

SECRET_KEY = "clave_secreta_super_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/inicio-sesion")

ph = CryptContext(schemes=["bcrypt"], deprecated="auto")


class JWTAuthStrategy(AuthStrategy):
    def hash_password(self, plain_password: str) -> str:
        return ph.hash(plain_password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return ph.verify(plain_password, hashed_password)

    def create_token(self, subject: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {"sub": subject, "exp": expire}
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def authenticate(self, repository: UserRepository, email: str, password: str):
        user = repository.find_by_email(email)
        if not user or not self.verify_password(password, user.password):
            return None
        return user

    def get_current_user(self, repository: UserRepository, token: str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autorizado",
            headers={"WWW-Authenticate": "Bearer"}
        )

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        usuario = repository.find_by_email(email)
        if usuario is None:
            raise credentials_exception
        return usuario
