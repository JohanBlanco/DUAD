from week_16.modules.sorting_algorithms import bubble_sort
import pytest

def test_bubble_sort_works_with_small_list():
    # Arrange
    test_list = [10,3,100]

    # Act
    result = bubble_sort(test_list)

    # Assert
    assert result == [3,10,100]

def test_bubble_sort_works_with_big_list():
    # Arrange
    sorted_hundred_elements = [number for number in range(100)]
    test_list = sorted_hundred_elements.copy()
    test_list.reverse()

    # Act
    result = bubble_sort(test_list)

    # Assert
    assert result == sorted_hundred_elements

def test_bubble_sort_works_with_empty_list():
    # Arrange
    test_list = []

    # Act
    result = bubble_sort(test_list)

    # Assert
    assert result == []

def test_bubble_sort_only_accept_lists_as_parameter():
    # Arrange
    string = "[1,2,3,4,5]"
    integer = 5
    tuple = (1,2,3,4)

    # Act and Assert
    with pytest.raises(ValueError):
        bubble_sort(string)


    # Act and Assert
    with pytest.raises(ValueError):
        bubble_sort(integer)

    # Act and Assert
    with pytest.raises(ValueError):
        bubble_sort(tuple)