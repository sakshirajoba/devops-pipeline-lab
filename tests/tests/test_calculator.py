from app import calculator
from app.main import main


def test_add():
    assert calculator.add(2, 3) == 5


def test_subtract():
    assert calculator.subtract(5, 3) == 2


def test_multiply():
    assert calculator.multiply(2, 3) == 6


def test_divide():
    assert calculator.divide(6, 3) == 2


def test_divide_by_zero():
    try:
        calculator.divide(6, 0)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError when dividing by zero"


def test_cli_prints_result(capsys):
    assert main(["add", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "Result: 5"


def test_cli_reports_error(capsys):
    assert main(["divide", "1", "0"]) == 1
    assert "Error" in capsys.readouterr().out
