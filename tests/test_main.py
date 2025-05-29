from src.main import add, divide
import pytest

def test_add():
    assert add(1, 2) == 3      # 测试1+2=3
    assert add(-1, 1) == 0     # 测试-1+1=0

def test_divide():
    assert divide(10, 2) == 5  # 测试10/2=5
    with pytest.raises(ValueError):
        divide(10, 0)          # 测试除以零会报错