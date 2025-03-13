import argparse

def hello():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default="stylish", help="set format of output"
    )

    # args = parser.parse_args()
    # print(args)

    return parser.parse_args()
