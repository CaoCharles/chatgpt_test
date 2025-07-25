# Tech Portfolio

This project is a minimal Next.js site designed for deployment on GitHub Pages or Vercel. It features a futuristic look with gradient backgrounds and glassmorphism.

## Pages
- **Home**: introduction with an AI assistant that can answer questions about the biography stored in `public/bio.json`.
- **Blog**: lists Markdown articles from the `posts` folder. Each post contains frontmatter metadata.
- **Certifications**: placeholder for certificates.
- **About**: personal biography.
- **Timeline**: simple chronological timeline.

To enable the AI assistant, provide an OpenAI API key when prompted. The key is stored in `localStorage` in the browser.

### Deploying to GitHub Pages

Run `npm run export` to generate the static files in the `out` directory and push them to the repository's `gh-pages` branch or GitHub Pages folder.
