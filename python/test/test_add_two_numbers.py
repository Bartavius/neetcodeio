import pytest
from add_two_numbers import ListNode, Solution

class TestAddTwoNumbers:
    """Test cases for Add Two Numbers problem."""
    
    @pytest.fixture
    def solution(self):
        return Solution()
    
    def create_linked_list(self, digits):
        """Helper function to create a linked list from a list of digits."""
        if not digits:
            return None
        
        dummy = ListNode(0)
        current = dummy
        for digit in digits:
            current.next = ListNode(digit)
            current = current.next
        return dummy.next
    
    def linked_list_to_list(self, head):
        """Helper function to convert linked list to list for easy comparison."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def test_basic_cases(self, solution):
        """Test basic examples from LeetCode."""
        # Example 1: 342 + 465 = 807
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [7, 0, 8]
        
        # Example 2: 0 + 0 = 0
        l1 = self.create_linked_list([0])
        l2 = self.create_linked_list([0])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [0]
        
        # Example 3: 9999999 + 9999 = 10009998
        l1 = self.create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.create_linked_list([9, 9, 9, 9])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]
    
    def test_carry_propagation(self, solution):
        """Test cases with carry propagation."""
        # 99 + 1 = 100
        l1 = self.create_linked_list([9, 9])
        l2 = self.create_linked_list([1])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [0, 0, 1]
        
        # 999 + 1 = 1000
        l1 = self.create_linked_list([9, 9, 9])
        l2 = self.create_linked_list([1])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [0, 0, 0, 1]
    
    def test_different_lengths(self, solution):
        """Test with linked lists of different lengths."""
        # 123 + 4 = 127
        l1 = self.create_linked_list([3, 2, 1])
        l2 = self.create_linked_list([4])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [7, 2, 1]
        
        # 1 + 999 = 1000
        l1 = self.create_linked_list([1])
        l2 = self.create_linked_list([9, 9, 9])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [0, 0, 0, 1]
    
    def test_edge_cases(self, solution):
        """Test edge cases."""
        # Single digit numbers
        l1 = self.create_linked_list([5])
        l2 = self.create_linked_list([5])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [0, 1]
        
        # Zero + number
        l1 = self.create_linked_list([0])
        l2 = self.create_linked_list([3, 2, 1])
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == [3, 2, 1]
    
    @pytest.mark.parametrize("digits1,digits2,expected", [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
        ([0], [0], [0]),  # 0 + 0 = 0
        ([9, 9], [1], [0, 0, 1]),  # 99 + 1 = 100
        ([5], [5], [0, 1]),  # 5 + 5 = 10
        ([1, 8], [0], [1, 8]),  # 81 + 0 = 81
        ([9, 9, 9], [9, 9, 9], [8, 9, 9, 1]),  # 999 + 999 = 1998
    ])
    def test_multiple_cases(self, solution, digits1, digits2, expected):
        """Test multiple cases with parametrize."""
        l1 = self.create_linked_list(digits1)
        l2 = self.create_linked_list(digits2)
        result = solution.add_two_numbers(l1, l2)
        assert self.linked_list_to_list(result) == expected
    
    @pytest.mark.slow
    def test_large_numbers(self, solution):
        """Test with very large numbers."""
        # Create a number with 100 digits (all 9s)
        l1 = self.create_linked_list([9] * 100)
        l2 = self.create_linked_list([1])
        result = solution.add_two_numbers(l1, l2)
        
        # Result should be 1 followed by 100 zeros
        expected = [0] * 100 + [1]
        assert self.linked_list_to_list(result) == expected

    def test_none_input_returns_empty_list(self, solution):
        """Test that None inputs return empty list as per implementation."""
        # Test with first list None
        l1 = None
        l2 = self.create_linked_list([1, 2, 3])
        result = solution.add_two_numbers(l1, l2)
        assert result == []  # code returns empty list
        
        # Test with second list None  
        l1 = self.create_linked_list([1, 2, 3])
        l2 = None
        result = solution.add_two_numbers(l1, l2)
        assert result == []  # code returns empty list
        
        # Test with both None
        result = solution.add_two_numbers(None, None)
        assert result == []  # code returns empty list