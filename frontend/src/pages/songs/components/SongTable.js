import { useState, useEffect } from "react";

import { Tooltip, Box } from "@mui/material";


import {
  GridRowModes,
  DataGrid,
  GridActionsCellItem,
  GridRowEditStopReasons,
  Toolbar,
  ToolbarButton,
  useGridApiRef
} from "@mui/x-data-grid";

import { Add, Edit, Delete, Save, Cancel } from "@mui/icons-material";
import SongToolbar from "./SongToolbar";
import EditCell from "./EditCell";

function column({
  field,
  headerName,
  style = {},
  editable = false,
  renderEditCell
}) {
  return {
    field,
    headerName,
    ...style,
    editable,
    flex: 1,
    ...(renderEditCell && { renderEditCell }),
  };
}




export default function SongTable({ songs = [], setSongs }) {
  const [rows, setRows] = useState([]);
  const [filteredRows, setFilteredRows] = useState([]);
  const apiRef = useGridApiRef()
  useEffect(() => {
    setRows(songs);
    setFilteredRows(songs);
  }, [songs]);
  const columns = [
    column({ field: "title", headerName: "Name", editable: true }),
    column({
      field: "show",
      headerName: "Show or Album",
      editable: true,
      renderEditCell: (params) => <EditCell {...params} />,
    }),
    column({
      field: "composer",
      headerName: "Composer or Artist",
      editable: true,
    }),
    column({ field: "lyricist", headerName: "Lyricist", editable: true }),
    column({ field: "genre", headerName: "Genre", editable: true }),
    column({ field: "year", headerName: "Year", editable: true }),
    column({ field: "character", headerName: "Character", editable: true }),
  ];


  const doubleClickHandler = ((params) => {
    const { id } = params;
    const rowMode = apiRef.current.getRowMode(id);
    if (rowMode === "view") {
      apiRef.current.startRowEditMode({ id: id });
    }
  })

  return (
    <DataGrid
      apiRef={apiRef}
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
      slots={{ toolbar: SongToolbar }}
      slotProps={{ toolbar: { rows, setFilteredRows, setSongs } }}
      showToolbar
      experimentalFeatures={{ newEditingApi: true }}
      onProcessRowUpdateError={(error) => {
        console.error("Update failed:", error);
      }}
      pageSizeOptions={[5, 10]}
    />
  );
}
