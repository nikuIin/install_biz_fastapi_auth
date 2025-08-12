import uuid

from sqlalchemy import (
    TEXT,
    UUID,
    Boolean,
    ForeignKey,
    String,
)
from sqlalchemy.dialects.postgresql import (
    TIMESTAMP,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import CheckConstraint
from sqlalchemy.sql.sqltypes import Integer

from db.base_models import Base, TimeStampMixin


class User(Base, TimeStampMixin):
    """
    Represents a user in the system with authentication details and roles.
    Includes timestamps for creation and last update.
    """

    __tablename__ = "user"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
    )
    login: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(320),
        nullable=True,
    )
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("role.role_id", ondelete="CASCADE"),
        nullable=False,
    )
    is_registered: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    __table_args__ = (
        CheckConstraint("length(login) > 0", name="user_login_check"),
        CheckConstraint("length(password) > 0", name="user_password_check"),
        CheckConstraint("length(email) >= 3", name="user_email_check"),
    )

    # Relationships
    role: Mapped["Role"] = relationship("Role", back_populates="users")
    refresh_token: Mapped[list["RefreshToken"]] = relationship(
        "RefreshToken", back_populates="user"
    )
    # A user has one associated metadata profile (one-to-one relationship)
    md_user: Mapped["MdUser"] = relationship(
        "MdUser", back_populates="user", uselist=False
    )


class Role(Base):
    """
    Defines a user role within the system, with associated permissions.
    """

    __tablename__ = "role"

    role_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )

    __table_args__ = (
        CheckConstraint("length(name) > 0", name="role_name_check"),
    )

    # Relationships
    users: Mapped[list["User"]] = relationship("User", back_populates="role")


class RefreshToken(Base, TimeStampMixin):
    """
    Stores refresh tokens used for user session management.
    Includes timestamps for creation and last update.
    """

    __tablename__ = "refresh_token"

    refresh_token_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("user.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    fingerprint: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    ip: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    is_blocked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
    expire_at: Mapped[float] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )

    # Relationship to User
    user: Mapped["User"] = relationship("User", back_populates="refresh_token")


class MdUser(Base):
    """
    Stores additional metadata for a user, such as name and profile details.
    This model maintains a one-to-one relationship with the User model via user_id.
    """

    __tablename__ = "md_user"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("user.user_id", ondelete="CASCADE"),
        primary_key=True,
    )
    first_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    middle_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    profile_picture_link: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )
    description: Mapped[str | None] = mapped_column(
        TEXT,
        nullable=True,
    )

    __table_args__ = (
        CheckConstraint(
            "length(first_name) > 0", name="md_user_first_name_check"
        ),
        CheckConstraint(
            "length(last_name) > 0", name="md_user_last_name_check"
        ),
        CheckConstraint(
            "length(middle_name) > 0", name="md_user_middle_name_check"
        ),
        CheckConstraint(
            "length(profile_picture_link) > 0",
            name="md_user_profile_picture_link_check",
        ),
    )

    # Relationship to User
    user: Mapped["User"] = relationship("User", back_populates="md_user")
