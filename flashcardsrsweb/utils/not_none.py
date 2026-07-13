# This was created to silence pyright's warning, when it complains that a certain value might be None. In some cases, we know for sure that the value will never be None at that point (for instance a domain object after being persisted will always have an id, even though it's type is int | None). To avoid pyright's warning, we're just asserting that the value is indeed not None. We're using TypeVar instead of just int because this way it can be used with any type.
from typing import TypeVar


T = TypeVar('T')

def assert_not_none(value: T | None) -> T:
    assert value is not None
    return value
