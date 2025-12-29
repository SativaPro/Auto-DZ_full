from sqlalchemy import text

# --------- INSERT (добавление) ---------

def test_insert_student(engine, cleanup):
    with engine.begin() as conn:
        # Добавляем
        r = conn.execute(
            text("INSERT INTO test_students (name, age) VALUES (:n, :a) RETURNING id"),
            {"n": "Alice", "a": 20},
        )
        new_id = r.scalar_one()
        cleanup.append(new_id)

        # Проверяем
        row = conn.execute(
            text("SELECT id, name, age, is_deleted FROM test_students WHERE id = :id"),
            {"id": new_id},
        ).mappings().one()

    assert row["name"] == "Alice"
    assert row["age"] == 20
    # Для PostgreSQL булево - это True/False
    assert row["is_deleted"] == False

# --------- UPDATE (изменение) ---------

def test_update_student(engine, cleanup):
    with engine.begin() as conn:
        new_id = conn.execute(
            text("INSERT INTO test_students (name, age) VALUES (:n, :a) RETURNING id"),
            {"n": "Bob", "a": 18},
        ).scalar_one()
        cleanup.append(new_id)

        conn.execute(
            text("UPDATE test_students SET name = :n, age = :a WHERE id = :id"),
            {"n": "Bobby", "a": 19, "id": new_id},
        )

        row = conn.execute(
            text("SELECT name, age FROM test_students WHERE id = :id"),
            {"id": new_id},
        ).mappings().one()

    assert row["name"] == "Bobby"
    assert row["age"] == 19

# --------- SOFT DELETE (мягкое удаление) ---------

def test_soft_delete_student(engine, cleanup):
    with engine.begin() as conn:
        new_id = conn.execute(
            text("INSERT INTO test_students (name, age) VALUES (:n, :a) RETURNING id"),
            {"n": "Carol", "a": 21},
        ).scalar_one()
        cleanup.append(new_id)

        conn.execute(
            text("UPDATE test_students SET is_deleted = TRUE WHERE id = :id"),
            {"id": new_id},
        )

        row = conn.execute(
            text("SELECT is_deleted FROM test_students WHERE id = :id"),
            {"id": new_id},
        ).mappings().one()

    assert row["is_deleted"] == True
