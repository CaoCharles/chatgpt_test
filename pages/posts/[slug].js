import { getPostSlugs, getPostBySlug } from '../../lib/posts';
import { useEffect, useState } from 'react';

export async function getStaticPaths() {
  const slugs = getPostSlugs().map(n => n.replace(/\.md$/, ''));
  return { paths: slugs.map(s => ({ params: { slug: s } })), fallback: false };
}

export async function getStaticProps({ params }) {
  const post = getPostBySlug(params.slug);
  return { props: { post } };
}

export default function Post({ post }) {
  const [html, setHtml] = useState('');
  useEffect(() => {
    const load = async () => {
      const { default: marked } = await import('https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js');
      setHtml(marked.parse(post.content));
    };
    load();
  }, [post.content]);
  return (
    <article>
      <h1>{post.metadata.title}</h1>
      <small>{post.metadata.date}</small>
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </article>
  );
}
