import argparse

from app import calculator

OPERATIONS = {
    "add": calculator.add,
    "subtract": calculator.subtract,
    "multiply": calculator.multiply,
    "divide": calculator.divide,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="A Tiny Calculator")
    parser.add_argument("operation", choices=OPERATIONS.keys())
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")

    args = parser.parse_args(argv)

    try:
        result = OPERATIONS[args.operation](args.a, args.b)
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print(f"Result: {result:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
