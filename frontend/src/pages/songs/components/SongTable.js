import { useState, useEffect } from "react";

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
import SongToolbar from "./SongToolbar"

function column(field, headerName, { style } = {}, editable = false) {
  return {
    field: field,
    headerName: headerName,
    ...style,
    editable: editable,
    flex: 1
  };
}
export default function SongTable({ songs, setSongs }) {
  const [rows, setRows] = useState([])
  const [filteredRows, setFilteredRows] = useState([])
  useEffect(() => {
    setRows(songs)
  }, [songs])
  const columns = [
    column("title", "Name", {}, true),
    column("show", "Show or Album", {}, true),
    column("composer", "Composer or Artist", {}, true),
    column("lyricist", "Lyricist", {}, true),
    column("genre", "Genre", {}, true),
    column("year", "Year", {}, true),
    column("character", "Character", {}, true),
  ];


  return (
      <DataGrid
        rows={filteredRows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}
        editMode="row"
        slots={{toolbar: SongToolbar}}
        slotProps={{toolbar: {rows, setFilteredRows, setSongs}}}
        showToolbar
        experimentalFeatures={{ newEditingApi: true }}
        onProcessRowUpdateError={(error) => {
          console.error("Update failed:", error);
        }}
        pageSizeOptions={[5, 10]}
      />
  );
}
