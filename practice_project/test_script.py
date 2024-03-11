import pytest
from .script import is_prime


def test_is_prime():
     assert is_prime(17) is True
     assert is_prime(13) is True
     assert is_prime(11) is True
     assert is_prime(7) is True
     assert is_prime(5) is True
     assert is_prime(107) is True
     assert is_prime(207) is True


def test_is_not_prime():
     assert is_prime(4) is False
     assert is_prime(6) is False
     assert is_prime(8) is False
     assert is_prime(10) is False
     assert is_prime(12) is False
     assert is_prime(108) is False
     assert is_prime(206) is False
     
     
