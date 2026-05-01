"""Sharkbase shared configuration loader.

Reads config/local.yaml and exposes paths and settings.
All scripts should use this instead of hardcoded paths.
"""
import os
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    yaml = None

_CONFIG: dict[str, Any] | None = None


def _find_config_path() -> Path:
    """Locate config/local.yaml relative to the project root."""
    # scripts/lib/config.py → scripts/lib/ → scripts/ → project root
    project_root = Path(__file__).resolve().parent.parent.parent
    return project_root / "config" / "local.yaml"


def _parse_yaml(path: Path) -> dict[str, Any]:
    """Parse YAML file, falling back to a simple hand-parser if PyYAML is missing."""
    text = path.read_text(encoding="utf-8")
    if yaml:
        return yaml.safe_load(text) or {}

    # Minimal YAML parser: only handles flat key: value and one level of nesting
    result: dict[str, Any] = {}
    current_section = result
    current_key = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" ") and ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if not val:
                current_key = key
                result[key] = {}
                current_section = result[key]
            else:
                result[key] = val
        elif line.startswith("  ") and ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if current_key and isinstance(current_section, dict):
                current_section[key] = val
    return result


def load_config() -> dict[str, Any]:
    """Load and cache the configuration."""
    global _CONFIG
    if _CONFIG is not None:
        return _CONFIG

    config_path = _find_config_path()
    if config_path.exists():
        _CONFIG = _parse_yaml(config_path)
    else:
        _CONFIG = {}
    return _CONFIG


def get_path(key: str, default: str = "") -> Path:
    """Get a path from config, returning Path object. Key uses dot notation: 'workspace.bili_dir'."""
    cfg = load_config()
    parts = key.split(".")
    val = cfg
    for p in parts:
        if isinstance(val, dict):
            val = val.get(p)
        else:
            val = None
            break
    if val:
        return Path(str(val))
    return Path(default)


def get_value(key: str, default: str = "") -> str:
    """Get a string value from config. Key uses dot notation: 'models.kimi_api_base'."""
    cfg = load_config()
    parts = key.split(".")
    val = cfg
    for p in parts:
        if isinstance(val, dict):
            val = val.get(p)
        else:
            val = None
            break
    return str(val) if val is not None else default


def project_root() -> Path:
    """Return the project root directory."""
    return _find_config_path().parent.parent


def kimi_api_key() -> str:
    """Get KIMI_API_KEY from environment. Raises only when called, not at import time."""
    key = os.environ.get("KIMI_API_KEY")
    if not key:
        # Try loading from .env file in project root
        env_path = project_root() / ".env"
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("KIMI_API_KEY="):
                    key = line.split("=", 1)[1].strip()
                    os.environ["KIMI_API_KEY"] = key
                    break
    if not key:
        raise RuntimeError(
            "KIMI_API_KEY is required. Set it in environment variables or .env file.\n"
            "  Example: export KIMI_API_KEY=sk-xxx"
        )
    return key
