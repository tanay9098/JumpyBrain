"""Shared helpers for line-by-line explainers."""


def lines_of(rel):
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    return (root / "frontend" / rel).read_text().splitlines()


def check(rel, tech, eli5):
    n = len(lines_of(rel))
    if len(tech) != n or len(eli5) != n:
        raise SystemExit(f"{rel}: have tech {len(tech)} eli5 {len(eli5)} want {n}")
    for i, (t, e) in enumerate(zip(tech, eli5), 1):
        if not str(t).strip() or not str(e).strip():
            raise SystemExit(f"{rel}:{i} empty explanation")
    return tech, eli5


def fill(rel, fn):
    tech, eli5 = [], []
    for i, raw in enumerate(lines_of(rel), 1):
        t, e = fn(i, raw)
        tech.append(t)
        eli5.append(e)
    return check(rel, tech, eli5)
