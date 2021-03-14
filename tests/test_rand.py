from fakeit import rand

_min_negative, _min, _max = -10, 2, 12
interval = f"{_min}:{_max}"
interval_negative = f"{_min_negative}:{_max}"


def test_rand_number():
    for _ in range(10):
        result: float = rand.number(interval=interval)
        assert _min <= result < _max


def test_rand_number_default():
    for _ in range(10):
        result: float = rand.number()
        assert 0 <= result < 1


def test_rand_number_negative():
    for _ in range(10):
        result: float = rand.number(interval=interval_negative)
        assert _min_negative <= result < _max


def test_rand_number_zero():
    for _ in range(10):
        result: float = rand.number(interval=0)
        assert result == 0


def test_rand_string():
    for _ in range(10):
        result: str = rand.string(interval=interval)
        assert _min <= len(result) < _max


def test_rand_string_min_negative():
    for _ in range(10):
        result: str = rand.string(interval=interval_negative)
        assert 0 <= len(result) < _max


def test_rand_array_string():
    result: list = rand.array("string", interval, interval)
    assert _min <= len(result) < _max
    for element in result:
        assert _min <= len(element) < _max


def test_rand_array_number():
    result: list = rand.array("number", interval, interval)
    assert _min <= len(result) < _max
    for element in result:
        assert _min <= element < _max


def test_rand_boolean():
    for _ in range(10):
        result: bool = rand.boolean()
        assert result in [True, False]
