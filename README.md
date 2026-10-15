# Research website

Jekyll publishes the main pages at `/publications/`, `/research/`, and `/notes/`.
`jekyll-redirect-from` preserves the old `.html` links. The ReRoot demo is served
at `/demos/reroot/`; `/budget-planning.html` redirects there.

## Deployment

In this repository's **Settings → Pages → Build and deployment**, set **Source**
to **GitHub Actions**. Push to `main` or run **Deploy website and ReRoot demo**
from the Actions tab to publish.

The workflow checks out this website and `dcherenson/reroot-demo` separately,
tests and builds the demo, builds the Jekyll website, and copies the packaged
demo into the website artifact. No generated demo files are committed here.
Pull requests build and validate the artifact without deploying it.

Scheduled runs check the demo's `main` branch every 15 minutes. A published
`deployment.json` records the two source revisions so unchanged scheduled runs
skip the build and deployment. Updates go live after the next scheduled run
and successful build; GitHub can delay scheduled runs. No additional token or
repository secret is required. The existing `/reroot-demo/` project site can
continue to run independently.

GitHub disables scheduled workflows in public repositories after 60 days with
no repository activity. If this happens, re-enable the workflow in Actions.
See [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Validation

The deployment runs the demo's unit tests and
`python3 scripts/verify-site.py <assembled-site-directory>` before uploading.
The verifier checks clean routes, old redirects, local links and assets, and
source revision metadata.
