import pytest

from randomqueue import RandomQueue

def test_insert():
    queue = RandomQueue()
    queue.insert(1)
    assert not queue.is_empty()


def test_remove():
    queue = RandomQueue()
    queue.insert(1)
    queue.insert(2)
    item = queue.remove()
    assert item in [1, 2]
    assert not queue.is_empty()

def test_remove_on_empty_queue():
    queue = RandomQueue()
    with pytest.raises(IndexError):
        queue.remove()

def test_clear():
    queue = RandomQueue()
    queue.insert(1)
    queue.clear()
    assert queue.is_empty()


if __name__ == "__main__":
    pytest.main()