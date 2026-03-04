import pytest
from ..src.main import add

def test_main():
    # Arrange
    expected = 10
    
    # Act
    actual = add(4, 6)

    # Assert
    assert actual == expected

    assert add (-10, 20) == expected
    assert add(0, 0) == 0
    
    