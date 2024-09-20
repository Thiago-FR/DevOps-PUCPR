from src.main import root, ping, sum, odd_even
from src.main import Numbers, Number
import pytest


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello, World!"}


@pytest.mark.asyncio
async def test_ping():
    result = await ping()
    assert result == {"message": "pong"}


@pytest.mark.asyncio
async def test_sum_error_no_body():
    with pytest.raises(TypeError) as excinfo:
        await sum()

    assert str(excinfo.value) == "sum() missing 1 required positional argument: 'numbers'"


@pytest.mark.asyncio
async def test_sum_success():
    numbers = Numbers(num1=10, num2=5)
    result = await sum(numbers)
    assert result == {'sum': 15.0}


@pytest.mark.asyncio
async def test_even():
    number = Number(num=10)
    result = await odd_even(number)
    assert result == {"odd_even": "even"}


@pytest.mark.asyncio
async def test_odd():
    number = Number(num=5)
    result = await odd_even(number)
    assert result == {"odd_even": "odd"}
