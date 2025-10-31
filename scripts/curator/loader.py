from pathlib import Path
import yaml

def load_constitution(path: Path) -> dict:
    if not path.exists():
        print(f"⚠️ Constitution file not found: {path}")
        return {}

    if path.suffix in [".yaml", ".yml"]:
        try:
            return yaml.safe_load(path.read_text())
        except Exception as e:
            print(f"❌ Failed to parse YAML: {e}")
            return {}

    # fallback: parse structured markdown (simple frontmatter or headings)
    lines = path.read_text().splitlines()
    config = {}
    for line in lines:
        if line.startswith("### "):
            key = line[4:].strip().lower().replace(" ", "_")
            config[key] = []
        elif line.startswith("- [x] "):
            config.setdefault("principles", []).append(line[6:].strip())
    return config