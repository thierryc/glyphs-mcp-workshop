"""Build a deterministic participant ZIP, without presenter/private assets."""
from hashlib import sha256
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def package():
    source = ROOT / "template"
    destination = ROOT / "dist"
    destination.mkdir(exist_ok=True)
    archive = destination / "glyphs-mcp-workshop.zip"
    expanded = 0
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for file in sorted(source.rglob("*")):
            if file.is_symlink():
                raise ValueError(f"Symlink rejected: {file}")
            if not file.is_file() or any(p in {"__pycache__", ".git", ".DS_Store"} for p in file.parts):
                continue
            data = file.read_bytes()
            expanded += len(data)
            name = "glyphs-mcp-workshop/" + file.relative_to(source).as_posix()
            entry = zipfile.ZipInfo(name, date_time=(2026, 9, 23, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            output.writestr(entry, data)
    if archive.stat().st_size >= 20 * 1024 * 1024 or expanded > 64 * 1024 * 1024:
        raise ValueError("Archive exceeds the app template limits")
    digest = sha256(archive.read_bytes()).hexdigest()
    (destination / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    print(f"{archive.name}: {archive.stat().st_size} bytes; SHA-256 {digest}")


if __name__ == "__main__":
    package()
