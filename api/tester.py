def main():
    # COMMENT
    echo("Hello World")


def echo(sentence: str):
    print(sentence)
    print(say_something())


def say_something() -> str:
    return "Hello World"


if __name__ == '__main__':
    main()
