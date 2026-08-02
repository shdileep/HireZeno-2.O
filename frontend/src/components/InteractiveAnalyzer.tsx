import { useState } from 'react';
import { motion } from 'motion/react';
import { Play, CheckCircle2, AlertCircle, FileText, Briefcase } from 'lucide-react';

export default function InteractiveAnalyzer() {
  const [resumeText, setResumeText] = useState(
    `Senior Full-Stack Engineer with 6+ years of experience building scalable web applications. Proficient in Python, React, TypeScript, Node.js, Docker, Kubernetes, AWS, and Machine Learning integration. Led a team of 5 engineers to deliver microservices.`
  );

  const [jobDesc, setJobDesc] = useState(
    `Looking for a Senior AI Engineer with expertise in Python, React, TypeScript, Machine Learning models, Docker, AWS, and PyTorch.`
  );

  const [score, setScore] = useState<number | null>(88);
  const [matchedSkills, setMatchedSkills] = useState(['Python', 'React', 'TypeScript', 'Docker', 'AWS', 'Machine Learning']);
  const [missingSkills, setMissingSkills] = useState(['PyTorch']);

  const handleAnalyze = () => {
    // Simple client-side simulation logic for demo
    const resumeLower = resumeText.toLowerCase();
    const jobKeywords = ['python', 'react', 'typescript', 'docker', 'aws', 'machine learning', 'pytorch', 'kubernetes', 'node.js'];
    
    const matched = jobKeywords.filter(kw => resumeLower.includes(kw));
    const missing = jobKeywords.filter(kw => !resumeLower.includes(kw));
    
    const calculatedScore = Math.min(100, Math.round((matched.length / jobKeywords.length) * 100));
    
    setScore(calculatedScore);
    setMatchedSkills(matched.map(s => s.charAt(0).toUpperCase() + s.slice(1)));
    setMissingSkills(missing.map(s => s.charAt(0).toUpperCase() + s.slice(1)));
  };

  return (
    <section id="analyzer" style={{ padding: '6rem 2rem', maxWidth: '1200px', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h2 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '1rem' }}>
          Interactive <span className="gradient-text">ATS Simulator</span>
        </h2>
        <p style={{ color: '#9ca3af', fontSize: '1.1rem' }}>
          Paste candidate resume and job requirements to test real-time keyword scoring.
        </p>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
        gap: '2rem'
      }}>
        {/* Input Panel */}
        <div className="glass-panel" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', color: '#60a5fa', fontWeight: 600 }}>
            <FileText size={20} /> Candidate Resume Text
          </div>
          <textarea
            value={resumeText}
            onChange={(e) => setResumeText(e.target.value)}
            style={{
              width: '100%',
              height: '140px',
              background: '#030712',
              border: '1px solid #1f2937',
              borderRadius: '12px',
              padding: '1rem',
              color: '#f3f4f6',
              fontFamily: 'inherit',
              fontSize: '0.9rem',
              resize: 'none',
              outline: 'none',
              marginBottom: '1.5rem'
            }}
          />

          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', color: '#a78bfa', fontWeight: 600 }}>
            <Briefcase size={20} /> Target Job Description
          </div>
          <textarea
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            style={{
              width: '100%',
              height: '120px',
              background: '#030712',
              border: '1px solid #1f2937',
              borderRadius: '12px',
              padding: '1rem',
              color: '#f3f4f6',
              fontFamily: 'inherit',
              fontSize: '0.9rem',
              resize: 'none',
              outline: 'none',
              marginBottom: '1.5rem'
            }}
          />

          <button
            onClick={handleAnalyze}
            style={{
              width: '100%',
              background: 'linear-gradient(135deg, #2563eb, #7c3aed)',
              color: '#fff',
              border: 'none',
              padding: '0.9rem',
              borderRadius: '12px',
              fontWeight: 700,
              fontSize: '1rem',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '0.5rem'
            }}
          >
            <Play size={18} />
            Calculate ATS Score
          </button>
        </div>

        {/* Results Panel */}
        <div className="glass-panel" style={{ padding: '2rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
          <div>
            <h3 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '1.5rem' }}>
              Evaluation Results
            </h3>

            {score !== null && (
              <motion.div
                key={score}
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ duration: 0.4 }}
                style={{ textAlign: 'center', padding: '2rem 1rem', background: 'rgba(59, 130, 246, 0.08)', borderRadius: '16px', border: '1px solid rgba(59, 130, 246, 0.2)', marginBottom: '1.5rem' }}
              >
                <div style={{ fontSize: '3.5rem', fontWeight: 800 }} className="gradient-text">
                  {score}%
                </div>
                <div style={{ fontSize: '0.9rem', color: '#9ca3af', fontWeight: 600 }}>
                  {score >= 75 ? '🔥 High Candidate Match' : '⚠️ Moderate Skill Gap'}
                </div>
              </motion.div>
            )}

            <div style={{ marginBottom: '1.5rem' }}>
              <div style={{ fontSize: '0.9rem', fontWeight: 600, color: '#34d399', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                <CheckCircle2 size={16} /> Matched Skills ({matchedSkills.length})
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.4rem' }}>
                {matchedSkills.map((sk, i) => (
                  <span key={i} style={{ background: 'rgba(16, 185, 129, 0.15)', color: '#34d399', border: '1px solid rgba(16, 185, 129, 0.3)', padding: '0.2rem 0.6rem', borderRadius: '20px', fontSize: '0.8rem', fontWeight: 600 }}>
                    {sk}
                  </span>
                ))}
              </div>
            </div>

            <div>
              <div style={{ fontSize: '0.9rem', fontWeight: 600, color: '#f87171', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
                <AlertCircle size={16} /> Missing Keywords ({missingSkills.length})
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.4rem' }}>
                {missingSkills.map((sk, i) => (
                  <span key={i} style={{ background: 'rgba(239, 68, 68, 0.15)', color: '#f87171', border: '1px solid rgba(239, 68, 68, 0.3)', padding: '0.2rem 0.6rem', borderRadius: '20px', fontSize: '0.8rem', fontWeight: 600 }}>
                    {sk}
                  </span>
                ))}
              </div>
            </div>
          </div>

          <div style={{ marginTop: '2rem', textAlign: 'center', fontSize: '0.85rem', color: '#6b7280' }}>
            Full multi-resume batch processing & PDF parsing available in the Streamlit suite.
          </div>
        </div>
      </div>
    </section>
  );
}
