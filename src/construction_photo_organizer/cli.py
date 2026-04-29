import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="photo-organizer",
        description="Organize image files by modified date.",
    )
    parser.add_argument("input_dir", help="Input directory containing image files")
    parser.add_argument("output_dir", help="Output directory for organized files")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned operations without copying files",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    print("input_dir:", args.input_dir)
    print("output_dir:", args.output_dir)
    print("dry_run:", args.dry_run)


if __name__ == "__main__":
    main()
