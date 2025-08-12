from sqlalchemy import text

from db.statement import Statement

INSERT_ROLE_STMT = text(
    """
    insert into role (role_id, name) values (:role_id, :name)
    on conflict (role_id) do nothing;
    """
)

# Tuple of insert statements for initial data loading
BASE_STATEMENTS: tuple[Statement, ...] = (
    Statement(
        description="Add role 'user'",
        statement=INSERT_ROLE_STMT,
        data={"role_id": 1, "name": "lead"},
    ),
)
