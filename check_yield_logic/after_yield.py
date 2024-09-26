import pytest

@pytest.fixture
def some_yield_function():
    dict_value = []

    def setup(par_1, par_2, par_3):
        print('--> show params:', par_1, par_2, par_3, par_1+par_2+par_3)
        dict_value.append(par_1+par_2+par_3)
        return par_1+par_2+par_3, dict_value
    
    yield setup

    # clear global value
    dict_value = []
    print('I should execute', dict_value)


def test_after_yield(some_yield_function):
    print('start test')
    for i in range(5):
        sum_value, dict_value = some_yield_function(i+2,i+4,i+6)
        print('--> value:', sum_value, dict_value)
    
    try:
        assert True == True
    finally:
        print('I should execute too')