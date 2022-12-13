import pytest

from nodes import Node
from single_lists import SingleList

class TestSingleList:

    @pytest.fixture
    def listA():
        a = SingleList()
        a.insert_head(Node(1))
        a.insert_head(Node(2))
        a.insert_head(Node(3))
        return a
    
    @pytest.fixture
    def listB():
        b = SingleList()
        b.insert_head(Node(4))
        b.insert_head(Node(5))
        b.insert_head(Node(6))
        return b
    
    def testJoinAndRemoveTail(listA, listB):
        joined = listA.join(listB)
        assert 6 == joined.remove_tail()
        assert 5 == joined.remove_tail()
        assert 4 == joined.remove_tail()
        assert 3 == joined.remove_tail()
        assert 2 == joined.remove_tail()
        assert 1 == joined.remove_tail()
        
        with pytest.raises(ValueError):
            joined.remove_tail()
    
    def testClear(listA):
        a = listA
        a.clear()
        
        assert a.lenght == 0
        assert a.head == None
        assert a.tail == None

if __name__ == "__main__":
    pytest.main()