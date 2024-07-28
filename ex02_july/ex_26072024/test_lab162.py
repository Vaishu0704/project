import pytest
@pytest.fixture()
def sample_data():
    data=[1,2,3,4,5] #type list
    return data

@pytest.fixture()
def sample_data1():
    return True

def test_sample_1(sample_data,sample_data1):
    print(sample_data)
    print(sample_data1)
    assert len(sample_data)==5
    assert sample_data1==True
