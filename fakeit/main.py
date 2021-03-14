import sys
from reader import get_data, get_definitions_mapping
from serve import serve


filepath = sys.argv[-1]

(data, success) = get_data(filepath)
if success is False:
    print(data)
    sys.exit(-1)

(definitions_mapping, success) = get_definitions_mapping(data)
if success is False:
    print(definitions_mapping)
    sys.exit(-1)

serve(
    data.__dict__.get("title"),
    data.__dict__.get("description"),
    definitions_mapping
)
