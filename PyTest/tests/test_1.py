def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }


