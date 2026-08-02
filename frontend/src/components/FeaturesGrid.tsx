import { motion } from 'motion/react';
import { Target, Cpu, TrendingUp, Layers, MessageSquareCode, Award } from 'lucide-react';

const features = [
  {
    icon: Target,
    title: 'ATS Resume Scoring',
    desc: 'Weighted evaluation combining Cosine Similarity, Skill Gap, Experience, and Education credentials.',
    color: '#3b82f6'
  },
  {
    icon: Cpu,
    title: 'NLP Entity Extraction',
    desc: 'Named Entity Recognition (NER) & TF-IDF vectors extracting tools, institutions, and domain competencies.',
    color: '#8b5cf6'
  },
  {
    icon: TrendingUp,
    title: 'ML Salary Prediction',
    desc: 'Random Forest & XGBoost regression models estimating competitive compensation benchmarks.',
    color: '#06b6d4'
  },
  {
    icon: Layers,
    title: 'Deep Learning Classifier',
    desc: 'Neural Network classification mapping candidates to enterprise department hierarchies with confidence bounds.',
    color: '#10b981'
  },
  {
    icon: MessageSquareCode,
    title: 'AI Career Coach',
    desc: 'Conversational LLM engine producing tailored learning roadmaps, interview prep, and cold outreach emails.',
    color: '#f59e0b'
  },
  {
    icon: Award,
    title: 'Recruiter Leaderboard',
    desc: 'Multi-resume batch screening and candidate ranking engine for rapid shortlist generation.',
    color: '#ec4899'
  }
];

export default function FeaturesGrid() {
  return (
    <section id="features" style={{ padding: '6rem 2rem', maxWidth: '1200px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '1rem' }}>
          Powered by Advanced <span className="gradient-text">AI Architecture</span>
        </h2>
        <p style={{ color: '#9ca3af', fontSize: '1.1rem', maxWidth: '600px', margin: '0 auto' }}>
          Comprehensive suite designed for candidate evaluation, skill gap recommendation, and hiring decisions.
        </p>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
        gap: '2rem'
      }}>
        {features.map((feat, idx) => (
          <motion.div
            key={idx}
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: idx * 0.1 }}
            whileHover={{ y: -8, scale: 1.02 }}
            className="glass-panel"
            style={{
              padding: '2rem',
              position: 'relative',
              overflow: 'hidden',
              cursor: 'pointer'
            }}
          >
            <div style={{
              width: '50px',
              height: '50px',
              borderRadius: '14px',
              background: `rgba(${parseInt(feat.color.slice(1, 3), 16)}, ${parseInt(feat.color.slice(3, 5), 16)}, ${parseInt(feat.color.slice(5, 7), 16)}, 0.15)`,
              border: `1px solid ${feat.color}40`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              marginBottom: '1.2rem'
            }}>
              <feat.icon size={26} color={feat.color} />
            </div>

            <h3 style={{ fontSize: '1.3rem', fontWeight: 700, marginBottom: '0.6rem' }}>
              {feat.title}
            </h3>

            <p style={{ color: '#9ca3af', fontSize: '0.95rem', lineHeight: 1.6 }}>
              {feat.desc}
            </p>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
