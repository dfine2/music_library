import { styled } from "@mui/material/styles";
import { Toolbar } from "@mui/x-data-grid";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";

import SearchBar from "./SearchBar";

const ToolbarContainer = styled(Toolbar)(({ theme }) => ({
  padding: theme.spacing(1),
  display: "flex",
  justifyContent: "space-between",
}));
const NewSongButton = styled(Button)(({ theme }) => ({}));

export default function SongToolbar(props) {
  const { rows, setFilteredRows, setSongs } = props;
  return (
    <ToolbarContainer>
      <Stack
        direction="row"
        spacing={4}
        sx={{ width: "100%", display: "flex", justifyContent: "space-between" }}
      >
        <SearchBar rows={rows} setFilteredRows={setFilteredRows} />
        <NewSongButton variant="contained">New Song</NewSongButton>
      </Stack>
    </ToolbarContainer>
  );
}
