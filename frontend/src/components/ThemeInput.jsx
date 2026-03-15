import React from 'react'
import { useState } from 'react'

const ThemeInput = ({ onSubmit }) => {

    const [theme, setTheme] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!theme.trim()) {
            setError("Please enter a theme.");
            return;
        }
        setError("");
        onSubmit(theme);
    };


  return (
    <div className="theme-input-container">
      <h2>Generate Your Adventure</h2>
      <p>Provide a theme for the story generator.</p>

      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <input
            type="text"
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
            placeholder="Enter a theme (e.g., fantasy, sci-fi, mystery ...)"
            className={error ? "error" : ""}
          />
          {error && <p className="error-text">{error}</p>}
        </div>
        <button type="submit" className="generate-btn">
          Generate Story
        </button>
      </form>
    </div>
  )
}

export default ThemeInput