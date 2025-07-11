import logo from './logo.svg';
import './App.css';
import { styled } from "@mui/material/styles";

import Songs from "./pages/songs/Songs";

const FullscreenContainer = styled("div")({
  height: "100vh",
  width: "100vw",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  background: "lightblue",
});

function App() {
  return (
    <FullscreenContainer>
      <Songs />
    </FullscreenContainer>
  );
}

export default App;
