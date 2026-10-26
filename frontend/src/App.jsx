import { useState } from 'react';
import './App.css';

function App() {
  const [skills, setSkills] = useState('');
  const [role, setRole] = useState('Data Analyst');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
 const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';

  async function analyzeSkills(event) {
    event.preventDefault();

    if (!skills.trim()) {
      alert('Please enter your current skills.');
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          role: role,
          skills: skills,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Unable to analyze skills.');
      }

      setResult(data);
    } catch (error) {
      alert(
        'Could not connect to the backend. Please check that Flask is running.'
      );
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <header>
        <h1>AI Skill Gap Detector</h1>
        <p>Discover your skill gaps and plan your career growth.</p>
      </header>

      <main className="container">
        <section className="card">
          <h2>Analyze Your Skills</h2>
          <p>Enter your skills and select your desired career.</p>

          <form onSubmit={analyzeSkills}>
            <label htmlFor="role">Choose your career</label>

            <select
              id="role"
              value={role}
              onChange={(event) => {
                setRole(event.target.value);
                setResult(null);
              }}
            >
              <option>Data Analyst</option>
              <option>Web Developer</option>
              <option>Python Developer</option>
            </select>

            <label htmlFor="skills">Your current skills</label>

            <textarea
              id="skills"
              value={skills}
              onChange={(event) => setSkills(event.target.value)}
              placeholder="Example: Python, SQL, Excel"
              rows="4"
            />

            <button type="submit" disabled={loading}>
              {loading ? 'Analyzing...' : 'Analyze Skills'}
            </button>
          </form>
        </section>

        {result && (
  <section className="card results">

    <div className="match-score">
      <h3>🎯 Your Skill Match</h3>

      <div className="score-number">
        {Math.round(
          (result.matched_skills.length /
            (result.matched_skills.length +
              result.missing_skills.length || 1)) *
            100
        )}%
      </div>

      <p>
        You match {result.matched_skills.length} out of{' '}
        {result.matched_skills.length +
          result.missing_skills.length}{' '}
        required skills.
      </p>
    </div>

    <h2>Your Skill Gap Report</h2>

            <h3>✅ Skills You Have</h3>
            {result.matched_skills.length > 0 ? (
              <ul>
                {result.matched_skills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>No matching skills found yet.</p>
            )}

            <h3>📚 Skills You Need to Learn</h3>
            {result.missing_skills.length > 0 ? (
              <ul>
                {result.missing_skills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>Great! You have all the listed skills for this role.</p>
            )}

            <h3>🚀 Recommended Skills</h3>
            {result.recommended_skills.length > 0 ? (
              <ul>
                {result.recommended_skills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>No additional skills recommended for this role.</p>
            )}

            <h3>🗺️ Your Learning Roadmap</h3>{result.missing_skills.length > 0 ? (

  <ol className="roadmap">
    {result.missing_skills.map((skill, index) => (
      <li key={skill}>
        <strong>Step {index + 1}:</strong> Learn {skill}
        <p>Study the basics of {skill} and practise with a small project.</p>
      </li>
    ))}
  </ol>
) : (
  <p>🎉 You have all the listed skills! Explore advanced projects to keep improving.</p>
)}
          </section>
        )}
      </main>

      <footer>
        AI-Based Skill Gap Detector | Student Project
      </footer>
    </div>
  );
}

export default App;
