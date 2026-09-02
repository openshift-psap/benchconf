from __future__ import annotations

from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_CONFIGS_DIR = _REPO_ROOT / "configs"


def get_config(suite: str, name: str) -> Path:
    """Return the filesystem path to a benchmark config file.

    Args:
        suite: Config suite directory (e.g. "llm-d", "rhaiis-regression").
        name: Benchmark name without extension (e.g. "concurrent-1k-1k").

    Returns:
        Path to the YAML config file.

    Raises:
        FileNotFoundError: If the config does not exist.

    Example::

        >>> import benchconf
        >>> path = benchconf.get_config("llm-d", "concurrent-1k-1k")
        >>> path.name
        'concurrent-1k-1k.yaml'
    """
    path = _CONFIGS_DIR / suite / f"{name}.yaml"
    if not path.exists():
        available = list_configs(suite)
        raise FileNotFoundError(
            f"No config '{name}' in suite '{suite}'. Available: {available}"
        )
    return path


def list_suites() -> list[str]:
    """List available benchmark suites."""
    return sorted(
        p.name
        for p in _CONFIGS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )


def list_configs(suite: str | None = None) -> list[str]:
    """List available benchmark config names, optionally filtered by suite.

    Args:
        suite: If provided, list only configs in this suite.
            If None, list configs across all suites as "suite/name".
    """
    if suite:
        suite_dir = _CONFIGS_DIR / suite
        if not suite_dir.is_dir():
            return []
        return sorted(p.stem for p in suite_dir.iterdir() if p.suffix == ".yaml")

    result = []
    for suite_dir in sorted(_CONFIGS_DIR.iterdir()):
        if not suite_dir.is_dir() or suite_dir.name.startswith("."):
            continue
        for p in sorted(suite_dir.iterdir()):
            if p.suffix == ".yaml":
                result.append(f"{suite_dir.name}/{p.stem}")
    return result


def load_config(suite: str, name: str) -> dict:
    """Load and parse a benchmark config file as a dictionary.

    Args:
        suite: Config suite directory (e.g. "llm-d").
        name: Benchmark name without extension.

    Returns:
        Parsed YAML content as a dict.
    """
    import yaml

    path = get_config(suite, name)
    with open(path) as f:
        return yaml.safe_load(f)
