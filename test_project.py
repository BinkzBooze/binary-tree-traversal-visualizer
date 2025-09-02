import pytest
from project import prompt_user_traversal, prompt_user_level, prompt_user_nodes

def test_prompt_user_traversal():
    # Valid integer input.
    assert prompt_user_traversal(1) == 'preorder'
    assert prompt_user_traversal(2) == 'inorder'
    assert prompt_user_traversal(3) == 'postorder'

    #Invalid integer input.
    with pytest.raises(ValueError):
        prompt_user_traversal(5)

    # Non-integer input.
    with pytest.raises(ValueError):
        prompt_user_traversal('inorder')

def test_prompt_user_level():
    # Valid integer input.
    assert prompt_user_level(1) == 1
    assert prompt_user_level(2) == 2
    assert prompt_user_level(3) == 3
    assert prompt_user_level(4) == 4

    # Invalid integer input.
    with pytest.raises(ValueError):
        prompt_user_level(5)

    # Non-integer input.
    with pytest.raises(ValueError):
        prompt_user_level('three')

def test_prompt_user_nodes():
    # Valid amount of nodes.
    assert prompt_user_nodes(1, 2) == 2
    assert prompt_user_nodes(2,5) == 5
    assert prompt_user_nodes(3,12) == 12
    assert prompt_user_nodes(4,27) == 27

    # Invalid amount of nodes.
    with pytest.raises(ValueError):
        prompt_user_nodes(1, 4)
    with pytest.raises(ValueError):
        prompt_user_nodes(2, 2)
    with pytest.raises(ValueError):
        prompt_user_nodes(3, 2)
    with pytest.raises(ValueError):
        assert prompt_user_nodes(4, 2)

    # Non-integer input.
    with pytest.raises(ValueError):
        prompt_user_nodes(3, 'twelve')
