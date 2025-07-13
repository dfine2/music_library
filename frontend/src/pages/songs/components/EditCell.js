import { useGridApiContext } from "@mui/x-data-grid";
import { TextField, IconButton, Stack } from "@mui/material";
import CheckIcon from "@mui/icons-material/Check";
import CloseIcon from "@mui/icons-material/Close";

export default function EditCell(props) {
  const { id, value, field } = props;
  const apiRef = useGridApiContext();
  const [inputValue, setInputValue] = React.useState(value);

  const handleSave = () => {
    apiRef.current.setEditCellValue({ id, field, value: inputValue }, event);
    apiRef.current.stopRowEditMode({ id });
  };

  const handleCancel = () => {
    apiRef.current.stopRowEditMode({ id, ignoreModifications: true });
  };

  return (
    <Stack direction="row" spacing={1} alignItems="center">
      <TextField
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        variant="standard"
        size="small"
      />
      <IconButton onClick={handleSave} size="small" color="success">
        <CheckIcon fontSize="small" />
      </IconButton>
      <IconButton onClick={handleCancel} size="small" color="error">
        <CloseIcon fontSize="small" />
      </IconButton>
    </Stack>
  );
}
