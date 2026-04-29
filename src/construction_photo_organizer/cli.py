import argparse
import csv
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


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


def collect_image_files(input_dir: Path) -> list[Path]:
    return sorted(
        [
            path
            for path in input_dir.iterdir()
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
        ],
        key=lambda path: (path.stat().st_mtime, path.name.lower()),
    )


def build_new_name(path: Path, index: int) -> str:
    modified_date = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y%m%d")
    return f"{modified_date}_{index:03d}{path.suffix.lower()}"


def organize_images(input_dir: Path, output_dir: Path, dry_run: bool) -> int:
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    if not input_dir.is_dir():
        raise NotADirectoryError(f"Input path is not a directory: {input_dir}")

    image_files = collect_image_files(input_dir)
    counters: dict[str, int] = defaultdict(int)
    rows: list[dict[str, str]] = []

    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    for source_path in image_files:
        modified_dt = datetime.fromtimestamp(source_path.stat().st_mtime)
        date_key = modified_dt.strftime("%Y%m%d")

        counters[date_key] += 1
        new_name = build_new_name(source_path, counters[date_key])
        destination_path = output_dir / new_name

        print(f"{source_path.name} -> {new_name}")

        rows.append(
            {
                "original_name": source_path.name,
                "new_name": new_name,
                "modified_time": modified_dt.isoformat(timespec="seconds"),
                "output_path": str(destination_path),
            }
        )

        if not dry_run:
            shutil.copy2(source_path, destination_path)

    if not dry_run:
        csv_path = output_dir / "rename_map.csv"
        with csv_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["original_name", "new_name", "modified_time", "output_path"],
            )
            writer.writeheader()
            writer.writerows(rows)

    return len(image_files)


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)

    try:
        count = organize_images(input_dir, output_dir, args.dry_run)
    except (FileNotFoundError, NotADirectoryError) as error:
        parser.error(str(error))

    if args.dry_run:
        print(f"Dry run complete. {count} file(s) found.")
    else:
        print(f"Complete. {count} file(s) copied.")


if __name__ == "__main__":
    main()
