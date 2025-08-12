"""
The custom exceptions of the project.
"""

from pathlib import Path

from core.logger.logger import get_configure_logger

logger = get_configure_logger(filename=Path(__file__).stem)


# ===============================
#         Tokens errors         #
# ===============================


class TokenSessionExpiredError(Exception):
    """The error, which occurs, when the token session is expired"""

    def __init__(self, message="Token session expired."):
        super().__init__(message)


class InvalidTokenDataError(Exception):
    """The error, which occurs, that the JWT-payload is invalid"""

    def __init__(self, message="Invalid JWT-payload."):
        super().__init__(message)
        logger.warning(
            "The wrong jwt data was received to the server", exc_info=True
        )


class AccessTokenAbsenceError(Exception):
    """The error occurs, while the access token wasn't finds in the cookies"""

    def __init__(self, message="There are no access token in the cookies."):
        super().__init__(message)


class RefreshTokenAbsenceError(Exception):
    """The error occurs, while the refresh token
    wasn't finds in the cookies

    """

    def __init__(self, message="There are no refresh token in the cookies."):
        super().__init__(message)


class RefreshTokenCreationError(Exception):
    """The error occurs, while the refresh token wasn't created"""

    def __init__(self, message="The refresh token wasn't created."):
        super().__init__(message)


class RefreshTokenIdAbsenceError(Exception):
    """The error occurs, while the refresh token
    payload doesn't have token_id

    """

    def __init__(self, message="The refresh token id must have token_id."):
        logger.warning(message, exc_info=True)
        super().__init__(message)


class RefreshTokenBlackListError(Exception):
    """The error occurs, while the refresh token is in the black list"""

    def __init__(self, message="The refresh token is in the black list."):
        super().__init__(message)


class TokenDatabaseError(Exception):
    """The error occurs, while the refresh token is in the black list"""

    def __init__(self, message="The database error during token operations"):
        super().__init__(message)


# ===============================
#          Email errors         #
# ===============================


class EmailDBError(Exception):
    """The error related to the error with email data in the database."""

    def __init__(
        self,
        message="The database error.",
    ):
        super().__init__(message)


# ===============================
#          User errors          #
# ===============================


class UserDBError(Exception):
    """The error related to the error with user data in the database."""

    def __init__(
        self,
        message="The db error of user data.",
    ):
        super().__init__(message)


class UserIntegrityError(Exception):
    """The error occurs with attempt to adding the user."""

    def __init__(self, message="The integrity error of user data."):
        super().__init__(message)


class UserDoesNotExistsError(Exception):
    """
    The error occurs, while the user wasn't
    exists in the DB
    """

    def __init__(
        self,
        message=("User with this data doesn't exists."),
    ):
        super().__init__(message)


class UserAlreadyExistsError(Exception):
    """The user with this data already exists in the database"""

    def __init__(
        self,
        message="The user with this data already exists in the database",
    ):
        super().__init__(message)


# ===================================== #
#        Email verification errors      #
# ===================================== #


class SetVerificationKeyError(Exception):
    """The error with setting verification key in the Redis"""

    def __init__(
        self, message="The internal server error when set verification key"
    ):
        super().__init__(message)


class GetVerificationKeyError(Exception):
    """The error with getting verification key in the Redis"""

    def __init__(
        self, message="The internal server error when get verification key"
    ):
        super().__init__(message)


class ValidateVerificationKeyError(Exception):
    """The error with validating verification key in the Redis"""

    def __init__(
        self, message="The internal server error when get validate key"
    ):
        super().__init__(message)


class DeleteVerificationKeyError(Exception):
    """The error with deliting verification key in the Redis"""

    def __init__(
        self, message="The internal server error with verification key"
    ):
        super().__init__(message)


class RateLimitingError(Exception):
    """The error occurs with a lot of attempts of auth with the same data
    in the one time period"""

    def __init__(self, message="A lot of attempts to auth."):
        super().__init__(message)


class UserRateLimitingError(RateLimitingError):
    pass


class EmailRateLimitingError(RateLimitingError):
    pass


class NextCodeAttemptNotPassedError(Exception):
    """The error occurs when client ask new code in the time interval
    when new attemnt does't allowed"""

    def __init__(
        self,
        message="Attempt to get new code not allowed yet."
        + " Please wait a bit more",
    ):
        super().__init__(message)
