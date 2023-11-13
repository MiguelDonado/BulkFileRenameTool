import argparse
from BulkFileRenamer import BulkFileRenamer


def main():
    args = parsear()
    if not args.order_by:
        renamer = BulkFileRenamer(args.source, args.replace, args.search)
    else:
        renamer = BulkFileRenamer(
            args.source,
            args.replace,
            args.search,
            args.order_by,
            args.number_files,
            args.rev,
        )


def parsear():
    parser = argparse.ArgumentParser(
        prog="Welcome to the Bulk File Rename Tool", epilog="Thanks for your time"
    )

    # ----------------PARSER-------------------------------------------------------------------------------------------------------

    parser.add_argument("source", help="Directory source.")
    parser.add_argument("-r", "--replace", default="File", help="Replace pattern")
    parser.add_argument("-s", "--search", default=None, help="Search pattern")

    # --------------SUBPARSERS------------------------------------------------------------------------------------------------------------------------

    subparsers = parser.add_subparsers(dest="order_by", help="Sort by: ")

    # Order by file size
    size_parser = subparsers.add_parser("size", help="Sort by size")
    size_parser.add_argument("number_files", type=int)
    size_parser.add_argument(
        "-rev", action="store_true", help="Reverse direction"
    )  # Si pongo -rev, almacena el valor True ///
    # True = Descendente ; False = Ascendente
    # Order by name
    name_parser = subparsers.add_parser("name", help="Sort by name")
    name_parser.add_argument("number_files", type=int)
    name_parser.add_argument("-rev", action="store_true", help="Reverse direction")

    # Order by time of file creation
    time_parser = subparsers.add_parser("time", help="Sort by time of modification")
    time_parser.add_argument("number_files", type=int)
    time_parser.add_argument("-rev", action="store_true", help="Reverse direction")

    return parser.parse_args()


if __name__ == "__main__":
    main()
