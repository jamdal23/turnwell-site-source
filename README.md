# Turnwell Website — Owner's Guide

This repo holds the **source** for turnwellusa.com. The live site is built from
`build.py` and published to the `jamdal23/turnwell-rebuild-preview` repo, which
GitHub Pages serves at turnwellusa.com.

## What's here

- `build.py` — the site generator. Edit content here, run `python3 build.py`,
  and it rebuilds every page as static HTML.
- `assets/` — images, PDFs, and other media (also mirrored in the preview repo).

## How the site gets published

1. Edit `build.py` (content lives in Python strings near the top of each page function).
2. Run `python3 build.py` to regenerate all HTML.
3. Upload the HTML files + `CNAME` to the `jamdal23/turnwell-rebuild-preview`
   repo (see `upload.py` for the script that does this via the GitHub API).
4. GitHub Pages rebuilds automatically — changes are live in ~1 minute.

## Quick edits without the generator

Every page of the live site exists as a plain `.html` file in the
`turnwell-rebuild-preview` repo. For small text changes you can edit those files
directly on github.com (click the file → pencil icon → Commit). No rebuild needed.
Just note: the next `build.py` run will overwrite manual edits, so for anything
bigger than a typo, change `build.py` instead.

## Handing management to someone else

1. On github.com, go to the `turnwell-rebuild-preview` repo → Settings →
   Collaborators → add them. They'll be able to edit and publish.
2. Give them this repo too (same steps) so they have the generator.
3. They'll need: a GitHub account (free), and Python 3 on their computer to run
   `build.py`.

## Key credentials & services (kept by the site owner, not in this repo)

- **GitHub account**: jamdal23 (owns both repos)
- **Domain**: turnwellusa.com registered at GoDaddy (auto-renew on)
- **DNS**: A records point to GitHub Pages; MX records point to Microsoft 365
  (email) — do not touch MX records when changing web hosting
- **Contact form**: Formspree (free tier), account under info@turnwellusa.com,
  form endpoint `https://formspree.io/f/mrpeazne`. Submissions are emailed to
  info@turnwellusa.com and also visible in the Formspree dashboard.
- **Email**: Microsoft 365 (GoDaddy-hosted), info@turnwellusa.com and
  jdalton@turnwellusa.com

## If something breaks

- Site down? Check https://www.githubstatus.com first.
- Wrong content live? The preview repo keeps full commit history — any change can
  be reverted on github.com.
- DNS issues? The domain's DNS is managed in the GoDaddy control panel.
