import pytest
from palindrome_number import Solution


x = Solution()
@pytest.mark.parametrize(
        'n, res', [(121, True),
                   (-121, False),
                   (10, False),
                   (0, True)]
        )
def test_Solution(n, res):
    assert x.isPalindrome(n) == res

