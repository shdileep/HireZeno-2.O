import { Cpu } from 'lucide-react';

export default function Footer() {
  return (
    <footer style={{
      borderTop: '1px solid rgba(255, 255, 255, 0.08)',
      padding: '4rem 2rem 2rem 2rem',
      background: '#030712'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
        alignItems: 'center',
        gap: '2rem',
        marginBottom: '3rem'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <img src="/logo.png" alt="HireZeno 2.O" style={{ width: '36px', height: '36px', objectFit: 'contain' }} />
          <span style={{ fontSize: '1.2rem', fontWeight: 800 }}>
            HireZeno <span className="gradient-text">2.O</span>
          </span>
        </div>

        <div style={{ display: 'flex', gap: '2rem', fontSize: '0.9rem', color: '#9ca3af' }}>
          <a href="#features" style={{ color: 'inherit', textDecoration: 'none' }}>Features</a>
          <a href="#analyzer" style={{ color: 'inherit', textDecoration: 'none' }}>ATS Simulator</a>
          <a href="http://localhost:8501" target="_blank" rel="noopener noreferrer" style={{ color: '#60a5fa', textDecoration: 'none' }}>Streamlit App</a>
        </div>
      </div>

      <div style={{ textAlign: 'center', fontSize: '0.85rem', color: '#4b5563', borderTop: '1px solid rgba(255, 255, 255, 0.05)', paddingTop: '2rem' }}>
        © 2026 NEXUS AI Platform. All rights reserved. Enterprise Intelligence Suite.
      </div>
    </footer>
  );
}
