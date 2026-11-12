"""make.fun news-summary-01 entry: copies the summary to the output."""
import os
import shutil
from pathlib import Path

src = Path(__file__).parent / "entry.txt"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
# Copy via a temp file and rename, so the output is never a truncated
# entry.txt if the process dies mid-copy.
tmp = out_dir / "entry.txt.tmp"
shutil.copyfile(src, tmp)
tmp.replace(out_dir / "entry.txt")
