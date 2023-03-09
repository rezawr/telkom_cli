import argparse
import pathlib

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('errorpath', type=pathlib.Path)

    parser.add_argument('-o', help='the path to the export file')
    parser.add_argument('-t', default='plain', choices=['plain', 'json'], type=str.lower)

    return parser


def main():
    from telkom_cli.export import export_json, export_plain


    args = create_parser().parse_args()

    file = None
    if args.o:
        file = open(args.o, 'w', newline='')

    if args.t == 'json':
        export_json(file, args.errorpath)
    else:
        export_plain(file, args.errorpath)
