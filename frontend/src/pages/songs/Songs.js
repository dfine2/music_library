import { useState, useEffect } from "react";

import { styled } from '@mui/material/styles';
import SongTable from "./components/SongTable";
import { Grid, Box } from "@mui/material";

const StyledGrid = styled(Grid)(({ theme }) => ({
  backgroundColor: "#fff",
  border: "3px inset #e0e0e0",
  borderRadius: "12px",
  boxShadow: "3px 10px 10px hsla(0, 71.40%, 1.40%, 0.61)",
  padding: theme.spacing(4),
  display: "flex",
  overflow: "auto",
  fontFamily: "Arial, sans-serif",
  width: "70%",
  maxHeight: "80vh", // optional scroll limit
}));

export default function Songs() {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/songs/")
      .then((res) => {
        return res.json();
      })
      .then((songs) => {
        setSongs(songs);
        if (songs && songs.length > 0) {
          const rows_from_songs = songs.map((song) => ({
            id: song.id,
            title: song.title,
            composer: song.composer,
            lyricist: song.lyricist,
            artist: song.artist,
            show: song.show,
            album: song.album,
            genre: song.genre,
            character: song.character,
            year: song.year,
          }));
        }
      });
  }, []);

  return (
    <StyledGrid>
      <Box sx={{ width: "100%", height: "100%" }}>
        <SongTable songs={songs} />
      </Box>
    </StyledGrid>
  );
}

