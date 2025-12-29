import os
from pathlib import Path
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from dotenv import load_dotenv

# ЗАГРУЖАЕМ .env ИЗ ТЕКУЩЕЙ ПАПКИ
env_path = Path(__file__).parent / '.env'
load_dotenv(env_path)

def get_database_url() -> str:
    """
    Если DATABASE_URL не задан – используем SQLite (файл test.db в корне проекта).
    """
    url = os.getenv("DATABASE_URL", "sqlite:///test.db")
    print(f"DEBUG: Using database URL: {url}")  # Для отладки
    return url

def make_engine(echo: bool = False) -> Engine:
    return create_engine(get_database_url(), echo=echo, future=True)

# DDL для PostgreSQL (SERIAL для автоинкремента, BOOLEAN для булевых)
DDL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS test_students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    is_deleted BOOLEAN NOT NULL DEFAULT FALSE
);
"""

def ensure_schema(engine: Engine) -> None:
    """Создаёт таблицу, если её нет."""
    with engine.begin() as conn:
        conn.execute(text(DDL_CREATE_TABLE))
