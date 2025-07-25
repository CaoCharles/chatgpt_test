import fs from 'fs';
import path from 'path';

const postsDirectory = path.join(process.cwd(), 'posts');

function parseFrontmatter(content) {
  const match = /^---\n([\s\S]+?)\n---\n([\s\S]*)$/m.exec(content);
  if (!match) return { metadata: {}, content };
  const meta = {};
  match[1].split('\n').forEach(line => {
    const [key, ...rest] = line.split(':');
    meta[key.trim()] = rest.join(':').trim();
  });
  return { metadata: meta, content: match[2] };
}

export function getPostSlugs() {
  return fs.readdirSync(postsDirectory).filter(f => f.endsWith('.md'));
}

export function getPostBySlug(slug) {
  const fullPath = path.join(postsDirectory, `${slug}.md`);
  const fileContents = fs.readFileSync(fullPath, 'utf8');
  const { metadata, content } = parseFrontmatter(fileContents);
  return { slug, metadata, content };
}

export function getAllPosts() {
  return getPostSlugs().map(name => {
    const slug = name.replace(/\.md$/, '');
    return getPostBySlug(slug);
  }).sort((a, b) => (a.metadata.date > b.metadata.date ? -1 : 1));
}
