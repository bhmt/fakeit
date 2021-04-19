import argparse
from reader import check_data, check_definitions_mapping
from serve import serve

DEFAULT_PORT = 9876
parser = argparse.ArgumentParser()
parser.add_argument(
    "filepath",
    type=str,
    help="Set the input json file."
)
parser.add_argument(
    "-p", "--port",
    type=int,
    help="Set the port for the applicaiton to use. Default value is 9876."
)
args = parser.parse_args()
port = args.port or DEFAULT_PORT

data = check_data(args.filepath)
definitions_mapping = check_definitions_mapping(data)

title = data.__dict__.get("title") or "FakeIt"
description = data.__dict__.get("description") or "Return pseudorandom data"

if __name__ == "__main__":
    serve(title, description, definitions_mapping, port)
