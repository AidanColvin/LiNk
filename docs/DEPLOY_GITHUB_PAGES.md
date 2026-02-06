## Deploy to GitHub Pages

This repository contains a static frontend (HTML, JS and JSON) that can be hosted on GitHub Pages so anyone can access it without a GitHub account.

What I added
- A GitHub Actions workflow at `.github/workflows/pages.yml` that publishes the repository root to GitHub Pages on every push to `main`.

How to enable
1. Commit and push the new workflow to GitHub:

```bash
git add .github/workflows/pages.yml DEPLOY_GITHUB_PAGES.md
git commit -m "Add GitHub Pages deploy workflow"
git push origin main
```

2. After the push, GitHub Actions will run and publish the site. You can check the Action run under the repository's **Actions** tab.

3. The public URL will be:

```
https://<your-github-username>.github.io/<repo-name>/
```

For example: `https://AidanColvin.github.io/LiNk/`

Notes
- The repository must be public for the Pages site to be accessible without login.
- If you'd rather use Netlify, Vercel, Render, or another host, I can add a deploy config for that instead.
