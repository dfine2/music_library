import { useState, useEffect } from "react";
import styled from "@emotion/styled";

import {Tooltip, Box } from "@mui/material";

import {
  GridRowModes,
  DataGrid,
  GridActionsCellItem,
  GridRowEditStopReasons,
  Toolbar,
  ToolbarButton,
} from "@mui/x-data-grid";
import { Add, Edit, Delete, Save, Cancel } from "@mui/icons-material";
import SearchBar from "./SearchBar"

function column(field, headerName, { style } = {}, editable = false) {
  return {
    field: field,
    headerName: headerName,
    ...style,
    editable: editable,
    flex: 1
  };
}
export default function SongTable({ songs }) {
  const [allRows, setAllRows] = useState([]);
  const [filteredRows, setFilteredRows] = useState([]);
  const [rowsMode, setRowsMode] = useState({});
  useEffect(() => {
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
      setAllRows(rows_from_songs);
    }
  }, [songs]);
  useEffect(() => {
    setFilteredRows(allRows);
  }, [allRows]);
  const columns = [
    column("title", "Name"),
    column("show", "Show or Album"),
    column("composer", "Composer or Artist"),
    column("lyricist", "Lyricist"),
    column("genre", "Genre"),
    column("year", "Year"),
    column("character", "Character"),
  ];


  const SongGrid = styled(DataGrid)(({theme}) => {

  })
  return (
    <Box sx={{width: '100%', height: '100%'}}>
      <SearchBar rows={allRows} setFilteredRows={setFilteredRows}/>
      <SongGrid
        rows={filteredRows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}
        showToolbar
        experimentalFeatures={{ newEditingApi: true }}
        onProcessRowUpdateError={(error) => {
          console.error("Update failed:", error);
        }}
        pageSizeOptions={[5, 10]}
      />
    </Box>
  );
}
