import pytest
from src import statistics_functions

def test_fun1():
    assert statistics_functions.fun1([1, 2, 3, 4, 5]) == 3.0
    assert statistics_functions.fun1([10, 20, 30]) == 20.0
    assert statistics_functions.fun1([0, 0, 0]) == 0.0
    assert statistics_functions.fun1([-1, 1]) == 0.0

def test_fun2():
    assert statistics_functions.fun2([1, 3, 5]) == 3.0
    assert statistics_functions.fun2([1, 2, 3, 4]) == 2.5
    assert statistics_functions.fun2([7]) == 7.0
    assert statistics_functions.fun2([-3, -1, 1, 3]) == 0.0

def test_fun3():
    assert round(statistics_functions.fun3([2, 4, 4, 4, 5, 5, 7, 9]), 2) == 2.14
    assert round(statistics_functions.fun3([1, 2, 3]), 4) == 1.0
    with pytest.raises(ValueError):
        statistics_functions.fun3([5])

def test_fun4():
    result = statistics_functions.fun4([1, 2, 3, 4, 5])
    assert result["mean"] == 3.0
    assert result["median"] == 3.0
    assert "std_dev" in result

    result2 = statistics_functions.fun4([10, 20, 30])
    assert result2["mean"] == 20.0
    assert result2["median"] == 20.0