import Link from 'next/link';
import '../styles/globals.css';

export default function Layout({ children }) {
  return (
    <div className="container">
      <header className="header">
        <h1 className="title">Tech Portfolio</h1>
        <nav>
          <Link href="/">Home</Link>
          <Link href="/blog">Articles</Link>
          <Link href="/certifications">Certifications</Link>
          <Link href="/about">About</Link>
          <Link href="/timeline">Timeline</Link>
        </nav>
      </header>
      <main>{children}</main>
    </div>
  );
}
