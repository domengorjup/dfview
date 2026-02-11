import dfview


def test_version():
    assert dfview.__version__ == "0.1.0"


def test_import():
    import dfview

    assert True


if __name__ == "__main__":
    test_version()
    test_import()
