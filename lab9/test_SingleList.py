import pytest

from nodes import Node
from single_lists import SingleList

class TestSingleList:

    @pytest.fixture
    def listA(self):
        a = SingleList()
        a.insert_head(Node(3))
        a.insert_head(Node(2))
        a.insert_head(Node(1))
        return a
    
    @pytest.fixture
    def listB(self):
        b = SingleList()
        b.insert_head(Node(6))
        b.insert_head(Node(5))
        b.insert_head(Node(4))
        return b
    
    def testRemoveTail(self, listA):
        a = listA
        assert 3 == a.remove_tail().data
        assert 2 == a.remove_tail().data
        assert 1 == a.remove_tail().data

        with pytest.raises(ValueError):
            a.remove_tail()

    def testJoinAndRemoveTail(self, listA, listB):
        a = listA
        b = listB

        a.join(b)

        assert 6 == a.remove_tail().data
        assert 5 == a.remove_tail().data
        assert 4 == a.remove_tail().data
        assert 3 == a.remove_tail().data
        assert 2 == a.remove_tail().data
        assert 1 == a.remove_tail().data
        
        with pytest.raises(ValueError):
            a.remove_tail()
    
    def testClear(self, listA):
        a = listA
        a.clear()
        
        assert a.length == 0
        assert a.head == None
        assert a.tail == None

if __name__ == "__main__":
    pytest.main()