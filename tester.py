import app


def main():
    # COMMENT
    echo("Hello word")


def echo(sentence: str):
    print(sentence)


def something(arg) -> str:
    return "hello world"

if __name__ == '__main__':
    main()
