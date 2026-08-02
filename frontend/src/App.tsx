import { useEffect } from 'react';
import Lenis from 'lenis';
import ThreeCanvas from './components/ThreeCanvas';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import FeaturesGrid from './components/FeaturesGrid';
import InteractiveAnalyzer from './components/InteractiveAnalyzer';
import Footer from './components/Footer';

export default function App() {
  useEffect(() => {
    // Initialize Lenis smooth scroll
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      orientation: 'vertical',
      gestureOrientation: 'vertical',
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 2,
    });

    function raf(time: number) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);

    return () => {
      lenis.destroy();
    };
  }, []);

  return (
    <div style={{ minHeight: '100vh', position: 'relative', background: '#030712' }}>
      {/* 3D React Three Fiber Canvas Background */}
      <ThreeCanvas />

      {/* Glassmorphic Navbar */}
      <Navbar />

      {/* Main Content Sections */}
      <main style={{ position: 'relative', zIndex: 10 }}>
        <Hero />
        <FeaturesGrid />
        <InteractiveAnalyzer />
      </main>

      {/* Footer */}
      <Footer />
    </div>
  );
}
