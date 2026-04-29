import csv
import os
from pathlib import Path

from construction_photo_organizer.cli import collect_image_files, organize_images


def test_collect_image_files_filters_and_sorts(tmp_path: Path) -> None:
    old_file = tmp_path / "b.jpg"
    same_time_a = tmp_path / "a.png"
    same_time_c = tmp_path / "c.jpeg"
    ignored_file = tmp_path / "memo.txt"

    old_file.write_text("old", encoding="utf-8")
    same_time_a.write_text("a", encoding="utf-8")
    same_time_c.write_text("c", encoding="utf-8")
    ignored_file.write_text("ignore", encoding="utf-8")

    old_time = 1_700_000_000
    same_time = 1_800_000_000

    os.utime(old_file, (old_time, old_time))
    os.utime(same_time_a, (same_time, same_time))
    os.utime(same_time_c, (same_time, same_time))
    os.utime(ignored_file, (1_600_000_000, 1_600_000_000))

    result = collect_image_files(tmp_path)

    assert [path.name for path in result] == ["b.jpg", "a.png", "c.jpeg"]


def test_organize_images_copies_files_and_writes_csv(tmp_path: Path) -> None:
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()

    image_file = input_dir / "photo.jpg"
    ignored_file = input_dir / "memo.txt"

    image_file.write_text("dummy image", encoding="utf-8")
    ignored_file.write_text("dummy text", encoding="utf-8")

    timestamp = 1_700_000_000
    os.utime(image_file, (timestamp, timestamp))

    count = organize_images(input_dir, output_dir, dry_run=False)

    copied_file = output_dir / "20231115_001.jpg"
    csv_file = output_dir / "rename_map.csv"

    assert count == 1
    assert copied_file.exists()
    assert not (output_dir / "memo.txt").exists()
    assert csv_file.exists()

    with csv_file.open("r", newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert rows == [
        {
            "original_name": "photo.jpg",
            "new_name": "20231115_001.jpg",
            "modified_time": "2023-11-15T07:13:20",
            "output_path": str(copied_file),
        }
    ]
