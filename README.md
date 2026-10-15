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

Every push to `reroot-demo/main` runs that repository's **Deploy research
website** workflow, which dispatches this repository's Pages workflow. Each
website run resolves the latest demo commit on `main`, tests it, and publishes
the combined site. A published `deployment.json` records both source revisions.
The existing `/reroot-demo/` project site continues to deploy independently.

There is no scheduled polling, so GitHub's 60-day inactivity rule for scheduled
workflows does not apply. Workflow queueing and build time still apply.

### One-time cross-repository authorization

GitHub's built-in `GITHUB_TOKEN` is restricted to the repository running the
workflow. The demo workflow therefore needs a credential for this repository:

1. Create a [fine-grained personal access token](https://github.com/settings/personal-access-tokens/new)
   owned by `dcherenson`. Under **Only select repositories**, select only
   `dcherenson.github.io`. Grant **Repository permissions → Actions → Read and
   write**; leave other permissions unchanged (Metadata read is automatic).
2. Choose an expiration appropriate for this automation. **No expiration**, if
   available, avoids renewal dates; otherwise replace the secret before expiry.
3. In [reroot-demo's Actions secrets](https://github.com/dcherenson/reroot-demo/settings/secrets/actions),
   add a **repository secret** named `WEBSITE_DEPLOY_TOKEN` with that token.
   Store it directly in GitHub, never in source files or chat.
4. Push to `reroot-demo/main`, or manually run **Deploy research website** on
   `main`. Confirm that **Deploy website and ReRoot demo** starts here.

The token needs access to the website repository, while the secret is stored
in the demo repository. Missing, expired, or revoked credentials cause the
dispatch workflow to fail visibly. After replacing the secret, rerun the
failed job. See [GitHub's workflow-dispatch permissions](https://docs.github.com/en/rest/actions/workflows#create-a-workflow-dispatch-event).

## Validation

The deployment runs the demo's unit tests and
`python3 scripts/verify-site.py <assembled-site-directory>` before uploading.
The verifier checks clean routes, old redirects, local links and assets, and
source revision metadata.
