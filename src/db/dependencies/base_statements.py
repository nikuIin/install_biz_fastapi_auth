from db.statement import Statement
from sqlalchemy import insert, text

# Tuple of insert statements for initial data loading
BASE_STATEMENTS: tuple[Statement, ...] = ()
