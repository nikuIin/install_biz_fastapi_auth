from collections.abc import Callable
from typing import Any


class Statement:
    """Class representing an insert statement for database initialization."""

    def __init__(
        self,
        description: str,
        statement: Any,
        data: dict,
    ):
        self.description = description
        self.statement = statement
        self.data = data
