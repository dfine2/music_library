import { styled } from "@mui/material/styles";
import { Toolbar, ToolbarButton } from "@mui/x-data-grid";
import SearchBar from "./SearchBar";

const NewSongButton = styled(ToolbarButton)(({ theme }) => ({}));

export default function SongToolbar(props) {
  const { rows, setFilteredRows } = props;
  return (
    <Toolbar>
      <SearchBar rows={rows} setFilteredRows={setFilteredRows} />
      <NewSongButton />
    </Toolbar>
  );
}
