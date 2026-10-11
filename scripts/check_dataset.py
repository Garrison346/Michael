
from pathlib import Path
from collections import defaultdict
from PIL import Image, UnidentifiedImageError
import hashlib

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset" / "classification"

SPLITS = ("train", "val", "test")
CLASSES = ("fire", "nofire")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def check_dataset():
    image_hashes = defaultdict(list)
    total_images = 0
    errors = []

    for split in SPLITS:
        print(f"\n{split.upper()}")

        for label in CLASSES:
            folder = DATASET / split / label

            if not folder.is_dir():
                errors.append(f"Missing directory: {folder}")
                continue

            images = sorted(
                p for p in folder.iterdir()
                if p.is_file() and p.suffix.lower() in EXTENSIONS
            )

            print(f"  {label}: {len(images)} images")
            total_images += len(images)

            if not images:
                errors.append(f"No images in {folder}")

            for path in images:
                try:
                    with Image.open(path) as image:
                        image.verify()

                    file_hash = hashlib.sha256(
                        path.read_bytes()
                    ).hexdigest()

                    image_hashes[file_hash].append((split, path))

                except (OSError, ValueError, UnidentifiedImageError) as exc:
                    errors.append(f"Invalid image: {path} ({exc})")

    # Find exact duplicate files across different splits
    for locations in image_hashes.values():
        splits = {split for split, _ in locations}

        if len(splits) > 1:
            paths = ", ".join(str(path) for _, path in locations)
            errors.append(f"Cross-split duplicate: {paths}")

    print(f"\nTotal images: {total_images}")

    if errors:
        print("\nVALIDATION FAILED")
        for error in errors:
            print(f"  - {error}")
        return False

    print("Dataset validation passed!")
    return True


if __name__ == "__main__":
    if not check_dataset():
        raise SystemExit(1)
