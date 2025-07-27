import Link from 'next/link';
import { getAllPosts } from '../../lib/posts';

export async function getStaticProps() {
  return { props: { posts: getAllPosts() } };
}

export default function Blog({ posts }) {
  return (
    <div>
      <h2>Articles</h2>
      {posts.map(post => (
        <div key={post.slug} className="card">
          <h3>
            <Link href={`/posts/${post.slug}`}>{post.metadata.title}</Link>
          </h3>
          <small>{post.metadata.date}</small>
        </div>
      ))}
    </div>
  );
}
