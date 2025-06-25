import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from "react";

function App() {
  const [songs, setSongs] = useState([]);
  useEffect(() => {
    fetch("http://localhost:8000/api/songs/")
      .then((res) => res.json())
      .then((songs) => {
        setSongs(songs);
      });
  }, []);
  return (
    <div>
      {songs.map((song, index) => (
        <div key={index}>{song.title}</div>
      ))}
    </div>
  );
}

export default App;
