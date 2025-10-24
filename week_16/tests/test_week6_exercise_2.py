from week_6.exercise_4_task_functions import sum_list_numbers
from week_6.exercise_5_task_functions import revert_string
from week_6.exercise_6_task_functions import number_of_cases
from week_6.exercise_7_task_functions import sort_alphabetically
from week_6.exercise_8_task_functions import get_prime_numbers

def test_sum_list_numbers_with_integers():
    # Arrange
    test_list = [100,200,300,400,500]

    # Act
    result = sum_list_numbers(test_list)
    # Assert
    assert result == 1500

def test_sum_list_numbers_with_float():
    # Arrange
    test_list = [1.00,2.00,3.00,4.00,5.00]

    # Act
    result = sum_list_numbers(test_list)
    # Assert
    assert result == 15.00

def test_sum_list_numbers_with_negative_numbers():
    # Arrange
    test_list = [-1,-2,-3,-4,-5]

    # Act
    result = sum_list_numbers(test_list)
    # Assert
    assert result == -15


def test_revert_string_with_Hello_World():
    # Arrange
    string = "Hola Mundo"
    
    # Act
    result = revert_string(string) 
    
    # Assert
    assert result == string[::-1]

def test_revert_string_with_empty_string():
    # Arrange
    string = ""
    
    # Act
    result = revert_string(string) 
    
    # Assert
    assert result == ""

def test_revert_string_with_white_spaces_only():
    # Arrange
    string = "   "
    
    # Act
    result = revert_string(string) 
    
    # Assert
    assert result == "   "

def test_number_of_cases_with_lower_cases_only(capsys):
    # Arrange
    string = "  hola  "

    # Act
    number_of_cases(string)
    result = capsys.readouterr().out
    
    # Assert
    assert result == 'There’s 0 upper cases and 4 lower cases\n'

def test_number_of_cases_with_upper_cases_only(capsys):
    # Arrange
    string = "  JOHAN  "

    # Act
    number_of_cases(string)
    result = capsys.readouterr().out
    
    # Assert
    assert result == 'There’s 5 upper cases and 0 lower cases\n'

def test_number_of_cases_with_both_cases(capsys):
    # Arrange
    string = "hola JOHAN"

    # Act
    number_of_cases(string)
    result = capsys.readouterr().out
    
    # Assert
    assert result == 'There’s 5 upper cases and 4 lower cases\n'

def test_sort_alphabetically_with_letters():
    # Arrange
    string = 'z-x-y-c-b-a'

    # Act
    result = sort_alphabetically(string)

    # Assert
    assert result == 'a-b-c-x-y-z'

def test_sort_alphabetically_with_words():
    # Arrange
    string = 'bed-room-tv-movie'

    # Act
    result = sort_alphabetically(string)

    # Assert
    assert result == 'bed-movie-room-tv'

def test_sort_alphabetically_with_numbers():
    # Arrange
    string = '4-2-3-1'

    # Act
    result = sort_alphabetically(string)

    # Assert
    assert result == '1-2-3-4'

def test_get_prime_numbers_with_even_numbers_only():
    # Arrange
    even_list = [2,4,6,8,10]

    # Act
    result = get_prime_numbers(even_list)
    
    # Assert
    assert result == [2]

def test_get_prime_numbers_with_odd_numbers_only():
    # Arrange
    even_list = [9,15,18,21,25, 31]

    # Act
    result = get_prime_numbers(even_list)
    
    # Assert
    assert result == [31]

def test_get_prime_numbers_with_large_numbers():
    # Arrange
    my_list = [101, 203, 307, 409, 503, 1001, 2021, 3031, 4043, 5051]

    # Act
    result = get_prime_numbers(my_list)
    
    # Assert
    assert result == [101, 307, 409, 503, 5051]