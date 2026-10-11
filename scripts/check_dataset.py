from pathlib import Path
from collections import defaultdict
from PIL import Image, UnidentifiedImageError
import hashlib

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset" / "detection"

SPLITS = ("train", "valid", "test")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def check_dataset():
    image_hashes = defaultdict(list)
    total_images = 0
    total_labels = 0
    errors = []

    for split in SPLITS:
        print(f"\n{split.upper()}")

        split_dir = DATASET / split
        images_dir = split_dir / "images"
        labels_dir = split_dir / "labels"

        if not split_dir.is_dir():
            errors.append(f"Missing split directory: {split_dir}")
            continue

        if not images_dir.is_dir():
            errors.append(f"Missing images directory: {images_dir}")
            continue

        if not labels_dir.is_dir():
            errors.append(f"Missing labels directory: {labels_dir}")
            continue

        # Gather all images
        images = sorted(
            p for p in images_dir.iterdir()
            if p.is_file() and p.suffix.lower() in EXTENSIONS
        )

        print(f"  Images: {len(images)}")
        total_images += len(images)

        if not images:
            errors.append(f"No images found in {images_dir}")

        # Check images and corresponding labels
        for img_path in images:
            try:
                # Verify image integrity
                with Image.open(img_path) as img:
                    img.verify()

                # Check for matching label file (.txt)
                label_path = labels_dir / f"{img_path.stem}.txt"
                if not label_path.exists():
                    errors.append(f"Missing label file for image: {img_path.name}")
                else:
                    total_labels += 1

                # Hash check for duplicate tracking across splits
                file_hash = hashlib.sha256(
                    img_path.read_bytes()
                ).hexdigest()

                image_hashes[file_hash].append((split, img_path))

            except (OSError, ValueError, UnidentifiedImageError) as exc:
                errors.append(f"Invalid image: {img_path} ({exc})")

    # Find exact duplicate files across different splits
    for locations in image_hashes.values():
        split_list = {split for split, _ in locations}

        if len(split_list) > 1:
            paths = ", ".join(str(path) for _, path in locations)
            errors.append(f"Cross-split duplicate: {paths}")

    print(f"\nTotal images: {total_images}")
    print(f"Total matched labels: {total_labels}")

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