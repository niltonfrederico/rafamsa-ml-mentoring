import shutil
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: lab <class_number>")
        print("Example: poetry run lab 01")
        sys.exit(1)

    class_num: str = sys.argv[1].zfill(2)
    root: Path = Path(__file__).parent.parent
    class_dir: Path = root / f"class-{class_num}"

    if not class_dir.exists():
        print(f"Error: class-{class_num}/ not found in {root}")
        sys.exit(1)

    notebooks: list[Path] = list(class_dir.glob("*.ipynb"))
    if not notebooks:
        print(f"Error: no .ipynb found in class-{class_num}/")
        sys.exit(1)

    notebook: Path = notebooks[0]
    labs_dir: Path = class_dir / "labs"
    labs_dir.mkdir(exist_ok=True)

    dest: Path = labs_dir / notebook.name
    shutil.copy2(notebook, dest)
    print(f"✓ {notebook.name}  →  class-{class_num}/labs/")
