import sys
from reader import get_data


if __name__ == '__main__':
    filepath = sys.argv[-1]
    (data, success) = get_data(filepath)

    if success is False:
        print(data)
        sys.exit(-1)

    title = data.title or "FakeIt"
    description = data.description or "Return pseudorandom data"

    print(title)
    print(description)
