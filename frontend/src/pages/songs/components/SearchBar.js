import {useState, useEffect} from 'react';
import {TextField, Box} from '@mui/material';

export default function SearchBar({rows, setFilteredRows}){
    const [searchText, setSearchText] = useState("");

    useEffect(() => {
          const lower = searchText.toLowerCase();
          if (!searchText){
            setFilteredRows(rows);
          }
          else {          
            setFilteredRows(
              rows.filter((row) =>
                Object.values(row).some(
                  (val) =>
                    typeof val === "string" && val.toLowerCase().includes(lower)
                )
              )
            );}

        }, [searchText, rows]);
        
    

   return  <TextField
    fullWidth
    variant="outlined"
    label="Search Songs"
    value={searchText}
    onChange={(e) => setSearchText(e.target.value)}
    sx={{ mb: 2 }}
  />
}