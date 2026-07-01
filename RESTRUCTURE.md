# Restructure guide (pyforge)

This file documents the one-time reorganization from the old flat layout into the
`pyforge` flagship structure. Run the script below **locally** from a clean clone,
review the result, then push. Deleting files and moving folders in bulk is safest
done on your machine rather than one-by-one in the GitHub web UI.

> After the reorg is pushed and verified, this `RESTRUCTURE.md` file can be removed.

## 1. Reorganize into the new structure

```bash
# from the repo root, on a fresh branch
git checkout -b chore/restructure

# --- create the target layout ---
mkdir -p src dsa learning archive

# --- flagship + core projects -> src/ ---
git mv flagship_fastapi_service src/fastapi_service
git mv project src/core            # date_range*, heatmap*, api.py, utils.py, etc.

# --- consolidate DSA (merge the duplicates into one folder) ---
# top-level DSA/ becomes the canonical location; move nested copies in too
git mv src/core/dsa/*      dsa/ 2>/dev/null || true
git mv src/core/dsa_pack/* dsa/ 2>/dev/null || true
rmdir src/core/dsa src/core/dsa_pack 2>/dev/null || true

# --- learning / practice scripts -> learning/ ---
git mv basic_Python learning/basics
git mv Dictonaries  learning/dictionaries   # fixes the spelling too
git mv if-statement learning/conditionals
git mv "SnakeGame " learning/snake_game     # fixes the trailing-space folder name

# --- streak log -> archive/ (or delete, see section 2) ---
git mv streak-log archive/streak-log

git add -A
git commit -m "chore: restructure into pyforge layout (src/, dsa/, learning/)"
```

## 2. Remove the misfits

These do not belong in the repo. Review each, then delete (or archive):

```bash
# file.py is Google Apps Script (JS), unrelated to this Python repo.
# If you still need it, move it to a separate gist/repo first.
git rm file.py

# Touple.py is a misspelled duplicate of Tuple.py
git rm learning/basics/Touple.py

git commit -m "chore: remove unrelated Apps Script file and duplicate script"
```

## 3. Fix imports / module paths

Because modules moved, update any `import` paths and the CI workflow / `pyproject.toml`
references (e.g. `project.date_range` -> `src.core.date_range`). Then:

```bash
ruff check .
pytest
```

## 4. Push and open a PR

```bash
git push -u origin chore/restructure
# open a pull request, review the diff, then merge
```

## 5. Rename the repository (do this yourself)

Renaming happens in **Settings -> General -> Repository name**: change `2026streak`
to `pyforge`, then click **Rename**. GitHub keeps redirects from the old name.
After renaming, update your local remote:

```bash
git remote set-url origin https://github.com/arunb-lab/pyforge.git
```
