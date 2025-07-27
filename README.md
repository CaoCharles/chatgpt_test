# Tech Portfolio

This project provides a small static site built with **Next.js**. It showcases a futuristic design using gradients, glassmorphism and simple hover animations. The site works well on GitHub Pages thanks to the base path configuration in `next.config.js`.

## Features
- **Home** – displays your name, title and a mini AI assistant that answers questions about your biography stored in `public/bio.json`.
- **Blog** – loads Markdown articles from the `posts` folder (each file uses frontmatter for metadata).
- **Certifications** – placeholder section for certificates or awards.
- **About** – short biography page.
- **Timeline** – list of milestones.

The AI assistant prompts the visitor for an OpenAI API key the first time they ask a question. The key is kept in `localStorage` so it only needs to be entered once.

## Project structure
```
components/      reusable React components (Layout)
lib/             helper functions for loading posts
pages/           Next.js pages including dynamic `[slug]` posts
posts/           Markdown blog articles
public/          static assets such as `bio.json`
styles/          global CSS styles
```

## Getting started
1. Install dependencies
   ```bash
   npm install
   ```
2. Run the development server
   ```bash
   npm run dev
   ```
   The site will be available at `http://localhost:3000`.

## Deploying to GitHub Pages
1. Ensure `basePath` and `assetPrefix` in `next.config.js` match your repository name. By default they are set to `/chatgpt_test`.
2. Build and export the static site
   ```bash
   npm run export
   ```
   The output will be placed in the `out` directory.
3. Commit the contents of `out` to a `gh-pages` branch (or configure Pages to serve from the `/docs` folder) and push to GitHub.
4. Enable GitHub Pages in your repository settings, selecting the branch and folder that contain the exported files.

After a few moments the site will be available at `https://<username>.github.io/<repo>/`.
