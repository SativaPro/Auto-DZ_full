import pytest
from sqlalchemy import text, bindparam
from sqlalchemy.engine import Engine
from .db import make_engine, ensure_schema


@pytest.fixture(scope="session")
def engine() -> Engine:
    eng = make_engine(echo=False)
    ensure_schema(eng)
    return eng

#@pytest.fixture(scope="session")
#def engine() -> Engine:
    #eng = make_engine(echo=True)  # Включите echo для отладки SQL запросов
    #print(f"DEBUG: Engine created with URL: {eng.url}")
    #ensure_schema(eng)
    #return eng

@pytest.fixture
def cleanup(engine: Engine):
    """
    Копит id созданных записей и удаляет их после теста.
    Используем IN с expanding=True (работает и в SQLite, и в Postgres).
    """
    ids = []
    yield ids
    if ids:
        stmt = (
            text("DELETE FROM test_students WHERE id IN :ids")
            .bindparams(bindparam("ids", expanding=True))
        )
        with engine.begin() as conn:
            conn.execute(stmt, {"ids": ids})
