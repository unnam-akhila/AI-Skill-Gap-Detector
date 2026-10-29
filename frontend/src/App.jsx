import { useEffect, useState } from 'react';
import './App.css';

const API_URL =
  import.meta.env.VITE_API_URL ||
  'https://ai-skill-gap-detector-x325.onrender.com';
function App() {
  const [skills, setSkills] = useState('');
  const [role, setRole] = useState('Data Analyst');
  const [search, setSearch] = useState('');
  const [roles, setRoles] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [rolesLoading, setRolesLoading] = useState(true);

  useEffect(() => {
    async function fetchRoles() {
      try {
        const response = await fetch(`${API_URL}/roles`);

        if (!response.ok) {
          throw new Error('Could not load career roles.');
        }

        const data = await response.json();
        setRoles(data.roles || []);
      } catch (error) {
        console.error('Role loading error:', error);

        setRoles([
          'Data Analyst',
          'Web Developer',
          'Python Developer',
        ]);
      } finally {
        setRolesLoading(false);
      }
    }

    fetchRoles();
  }, []);

  const filteredRoles = roles.filter((jobRole) =>
    jobRole.toLowerCase().includes(search.toLowerCase())
  );

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
          role,
          skills,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Unable to analyze skills.');
      }

      setResult(data);
   } catch (error) {
console.error('Analysis error:', error);
alert('Analysis failed: ' + error.message);
} finally {
setLoading(false);
}
  }

  const matchedSkills = result?.matched_skills || [];
  const missingSkills = result?.missing_skills || [];
  const recommendedSkills = result?.recommended_skills || [];
  const roadmap = result?.roadmap || [];

  const totalSkills = matchedSkills.length + missingSkills.length;

  const matchPercentage = totalSkills
    ? Math.round((matchedSkills.length / totalSkills) * 100)
    : 0;

  return (
    <div className="app">
      <header>
        <h1>AI Skill Gap Detector</h1>
        <p>
          Discover your skill gaps and plan your career growth.
        </p>
      </header>

      <main className="container">
        <section className="card">
          <h2>Analyze Your Skills</h2>

          <p>
            Enter your current skills and select your desired career.
          </p>

          <form onSubmit={analyzeSkills}>
            <label htmlFor="role-search">
              Search for your career
            </label>

            <input
              id="role-search"
              type="text"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Type a role, e.g. Data Scientist"
            />

            <label htmlFor="role">
              Choose your career
            </label>

            <select
              id="role"
              value={role}
              onChange={(event) => {
                setRole(event.target.value);
                setResult(null);
              }}
              disabled={rolesLoading}
            >
              {rolesLoading && (
                <option value="Data Analyst">
                  Loading careers...
                </option>
              )}

              {filteredRoles.map((jobRole) => (
                <option key={jobRole} value={jobRole}>
                  {jobRole}
                </option>
              ))}
            </select>

            {!rolesLoading && filteredRoles.length === 0 && (
              <p>
                No matching careers found. Try another search.
              </p>
            )}

            <label htmlFor="skills">
              Your current skills
            </label>

            <textarea
              id="skills"
              value={skills}
              onChange={(event) => setSkills(event.target.value)}
              placeholder="Example: Python, SQL, Excel"
              rows="4"
            />

            <button
              type="submit"
              disabled={
                loading ||
                rolesLoading ||
                !filteredRoles.includes(role)
              }
            >
              {loading ? 'Analyzing...' : 'Analyze Skills'}
            </button>
          </form>
        </section>

        {result && (
          <section className="card results">
            <div className="match-score">
              <h3>🎯 Your Skill Match</h3>

              <div className="score-number">
                {matchPercentage}%
              </div>

              <p>
                You match {matchedSkills.length} out of{' '}
                {totalSkills} required skills for {result.role}.
              </p>
            </div>

            <h2>Your Skill Gap Report</h2>

            <h3>✅ Skills You Have</h3>

            {matchedSkills.length > 0 ? (
              <ul>
                {matchedSkills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>
                No matching skills found yet. Start with the
                learning roadmap below.
              </p>
            )}

            <h3>📚 Skills You Need to Learn</h3>

            {missingSkills.length > 0 ? (
              <ul>
                {missingSkills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>
                Great! You have all the listed skills for this role.
              </p>
            )}

            <h3>🚀 Recommended Skills</h3>

            {recommendedSkills.length > 0 ? (
              <ul>
                {recommendedSkills.map((skill) => (
                  <li key={skill}>{skill}</li>
                ))}
              </ul>
            ) : (
              <p>
                No additional skills recommended for this role.
              </p>
            )}

            <h3>🗺️ Your Learning Roadmap</h3>

            <p>
              Follow these steps to improve your skills for the{' '}
              <strong>{result.role}</strong> role.
            </p>

            {roadmap.length > 0 ? (
              <ol className="roadmap">
                {roadmap.map((item, index) => (
                  <li key={item.skill}>
                    <strong>
                      Step {index + 1}: Learn {item.skill}
                    </strong>

                    <p>
                      <strong>🎯 Focus Areas:</strong>{' '}
                      {item.topics}
                    </p>

                    <p>
                      <strong>🛠️ Practical Task:</strong>{' '}
                      {item.task}
                    </p>
                  </li>
                ))}
              </ol>
            ) : (
              <p>
                🎉 You have all the listed skills! Try advanced
                projects to keep improving.
              </p>
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