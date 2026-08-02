import { motion } from 'motion/react';
import { Sparkles, Brain, FileCheck, Bot, ChevronRight } from 'lucide-react';

export default function Hero() {
  return (
    <section style={{
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
      textAlign: 'center',
      padding: '8rem 2rem 4rem 2rem',
      position: 'relative',
      overflow: 'hidden'
    }}>
      {/* Ambient background glows */}
      <div className="glow-bg" style={{ top: '20%', left: '15%', width: '400px', height: '400px', background: '#3b82f6' }} />
      <div className="glow-bg" style={{ bottom: '15%', right: '15%', width: '450px', height: '450px', background: '#8b5cf6' }} />

      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: '0.6rem',
          padding: '0.5rem 1.2rem',
          borderRadius: '50px',
          background: 'rgba(59, 130, 246, 0.12)',
          border: '1px solid rgba(59, 130, 246, 0.3)',
          color: '#60a5fa',
          fontSize: '0.9rem',
          fontWeight: 600,
          marginBottom: '1.5rem'
        }}
      >
        <img src="/logo.png" alt="HireZeno 2.O" style={{ width: '22px', height: '22px', objectFit: 'contain' }} />
        HireZeno 2.O Enterprise Suite v12.0
      </motion.div>

      <motion.h1
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7, delay: 0.2 }}
        style={{
          fontSize: 'clamp(2.5rem, 6vw, 4.5rem)',
          fontWeight: 800,
          lineHeight: 1.1,
          maxWidth: '900px',
          marginBottom: '1.5rem',
          letterSpacing: '-0.03em'
        }}
      >
        Transform Talent Acquisition with <span className="gradient-text">3D & AI Intelligence</span>
      </motion.h1>

      <motion.p
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7, delay: 0.4 }}
        style={{
          fontSize: '1.2rem',
          color: '#9ca3af',
          maxWidth: '650px',
          marginBottom: '2.5rem',
          lineHeight: 1.6
        }}
      >
        ATS Keyword Extraction • Machine Learning Suitability • Neural NLP Parsing • AI Career Coaching & Salary Benchmarks
      </motion.p>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.7, delay: 0.6 }}
        style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', justifyContent: 'center' }}
      >
        <a
          href="#analyzer"
          style={{
            background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
            color: '#fff',
            padding: '0.9rem 2rem',
            borderRadius: '14px',
            fontSize: '1.05rem',
            fontWeight: 600,
            textDecoration: 'none',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            boxShadow: '0 10px 30px rgba(37, 99, 235, 0.4)'
          }}
        >
          Try Live Analyzer
          <ChevronRight size={18} />
        </a>

        <a
          href="http://localhost:8501"
          target="_blank"
          rel="noopener noreferrer"
          className="glass-panel"
          style={{
            color: '#f3f4f6',
            padding: '0.9rem 2rem',
            borderRadius: '14px',
            fontSize: '1.05rem',
            fontWeight: 600,
            textDecoration: 'none',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem'
          }}
        >
          Open Streamlit Suite
        </a>
      </motion.div>

      {/* Metrics Row */}
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.8 }}
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '1.5rem',
          maxWidth: '900px',
          width: '100%',
          marginTop: '5rem'
        }}
      >
        {[
          { icon: FileCheck, val: '99.4%', label: 'ATS Match Precision' },
          { icon: Brain, val: '15+', label: 'AI & ML Core Modules' },
          { icon: Bot, val: '5,000+', label: 'Skills Indexed' },
          { icon: Sparkles, val: '30+', label: 'Enterprise Departments' }
        ].map((item, idx) => (
          <div key={idx} className="glass-panel" style={{ padding: '1.5rem', textAlign: 'center' }}>
            <item.icon size={28} color="#60a5fa" style={{ marginBottom: '0.5rem' }} />
            <div style={{ fontSize: '1.8rem', fontWeight: 800 }} className="gradient-text">{item.val}</div>
            <div style={{ fontSize: '0.85rem', color: '#9ca3af', marginTop: '0.2rem' }}>{item.label}</div>
          </div>
        ))}
      </motion.div>
    </section>
  );
}
