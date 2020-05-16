import pytest
from reverseInteger import Solution


x = Solution()
@pytest.mark.parametrize(
        'n, res', [(123, 321),
                   (-123, -321),
                   (120, 21),
                   (-2147483648, 0),
                   (-2147483412, -2143847412),
                   (1534236469, 0)
                  ]
        )
def test_Solution(n, res):
    assert x.reverse(n) == res

