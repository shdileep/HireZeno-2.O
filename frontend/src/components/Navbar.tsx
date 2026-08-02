import { motion } from 'motion/react';
import { Cpu, Sparkles, ArrowRight } from 'lucide-react';

export default function Navbar() {
  return (
    <motion.nav 
      initial={{ y: -50, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
      className="glass-nav"
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        zIndex: 50,
        padding: '1rem 2rem',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between'
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
        <img 
          src="/logo.png" 
          alt="HireZeno 2.O Logo" 
          style={{ width: '42px', height: '42px', objectFit: 'contain' }} 
        />
        <div>
          <span style={{ fontSize: '1.4rem', fontWeight: 800, letterSpacing: '-0.02em' }}>
            HireZeno <span className="gradient-text">2.O</span>
          </span>
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '2rem' }}>
        <a href="#features" style={{ color: '#9ca3af', textDecoration: 'none', fontWeight: 500, transition: 'color 0.2s' }}>Features</a>
        <a href="#analyzer" style={{ color: '#9ca3af', textDecoration: 'none', fontWeight: 500, transition: 'color 0.2s' }}>ATS Analyzer</a>
        <a href="#models" style={{ color: '#9ca3af', textDecoration: 'none', fontWeight: 500, transition: 'color 0.2s' }}>ML Models</a>
      </div>

      <a 
        href="http://localhost:8501" 
        target="_blank"
        rel="noopener noreferrer"
        style={{
          background: 'linear-gradient(135deg, #2563eb, #9333ea)',
          color: '#fff',
          padding: '0.65rem 1.4rem',
          borderRadius: '12px',
          fontWeight: 600,
          textDecoration: 'none',
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          boxShadow: '0 4px 15px rgba(37, 99, 235, 0.4)',
          transition: 'transform 0.2s, box-shadow 0.2s'
        }}
      >
        <Sparkles size={16} />
        Streamlit App
        <ArrowRight size={16} />
      </a>
    </motion.nav>
  );
}
