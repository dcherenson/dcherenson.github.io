"""Check the assembled Pages artifact before deployment (standard library only)."""

from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import unquote, urljoin, urlsplit


ORIGIN = "https://dcherenson.github.io"
root = Path(sys.argv[1]).resolve()
errors = []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.canonical = None
        self.refresh = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in ("href", "src"):
            if attrs.get(name):
                self.links.append(attrs[name])
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "meta" and attrs.get("http-equiv", "").lower() == "refresh":
            self.refresh = attrs.get("content")


for route in ("index.html", "publications/index.html", "research/index.html",
              "notes/index.html", "demos/reroot/index.html"):
    if not (root / route).is_file():
        errors.append(f"Missing page: {route}")

for path in root.rglob("*.html"):
    page = Page()
    page.feed(path.read_text())
    relative = path.relative_to(root).as_posix()
    for link in page.links:
        url = urlsplit(urljoin(f"{ORIGIN}/{relative}", link))
        if url.scheme not in ("http", "https") or url.netloc != "dcherenson.github.io":
            continue
        target = root / unquote(url.path).lstrip("/")
        if not target.is_file() and not (target / "index.html").is_file():
            errors.append(f"{relative}: missing local target {link}")

    expected = {
        "publications.html": "/publications/",
        "research.html": "/research/",
        "notes.html": "/notes/",
        "budget-planning.html": "/demos/reroot/",
    }.get(relative)
    if expected and (page.canonical != ORIGIN + expected or
                     not page.refresh or ORIGIN + expected not in page.refresh):
        errors.append(f"{relative}: incorrect redirect to {expected}")

for route in ("publications.html", "research.html", "notes.html", "budget-planning.html"):
    if not (root / route).is_file():
        errors.append(f"Missing legacy redirect: {route}")

versions = json.loads((root / "deployment.json").read_text())
for name in ("website", "demo"):
    sha = versions.get(name, "")
    if len(sha) != 40 or any(char not in "0123456789abcdef" for char in sha):
        errors.append(f"Invalid {name} revision in deployment.json")

if errors:
    raise SystemExit("\n".join(errors))
print("Verified page routes, legacy redirects, local assets, and deployed revisions.")
