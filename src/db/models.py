import decimal
import uuid
from datetime import UTC, date, datetime, timedelta

from core.config import auth_settings
from db.base_models import Base, TimeStampMixin
from sqlalchemy import (
    TEXT,
    UUID,
    VARCHAR,
    BigInteger,
    Boolean,
    CheckConstraint,
    ForeignKey,
    Identity,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import (
    JSONB,
    MONEY,
    NUMERIC,
    TIMESTAMP,
    TSVECTOR,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.types import DATE, SMALLINT
from uuid_extensions import uuid7
