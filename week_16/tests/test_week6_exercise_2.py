import pytest
from week_6.exercise_5_task_functions import revert_string
from week_6.exercise_8_task_functions import get_prime_numbers

def test_revert_string_works_well():
    # Arrange
    string = "Hola Mundo"
    
    # Act
    result = revert_string(string) 
    
    # Assert
    assert result == string[::-1]

def test_get_prime_numbers_works_well():
    # Arrange

    # Act

    # Assert
    pass