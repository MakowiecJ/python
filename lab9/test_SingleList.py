import pytest

from nodes import Node
from single_lists import SingleList

class TestSingleList:

    @pytest.fixture
    def listA(self):
        a = SingleList()
        a.insert_head(Node(1))
        a.insert_head(Node(2))
        a.insert_head(Node(3))
        return a
    
    @pytest.fixture
    def listB(self):
        b = SingleList()
        b.insert_head(Node(4))
        b.insert_head(Node(5))
        b.insert_head(Node(6))
        return b
    
    def testJoinAndRemoveTail(self, listA, listB):
        joined = listA.join(listB)
        assert 6 == joined.remove_tail().data
        assert 5 == joined.remove_tail().data
        assert 4 == joined.remove_tail().data
        assert 3 == joined.remove_tail().data
        assert 2 == joined.remove_tail().data
        assert 1 == joined.remove_tail().data
        
        with pytest.raises(ValueError):
            joined.remove_tail()
    
    def testClear(self, listA):
        a = listA
        a.clear()
        
        assert a.length == 0
        assert a.head == None
        assert a.tail == None

if __name__ == "__main__":
    pytest.main()