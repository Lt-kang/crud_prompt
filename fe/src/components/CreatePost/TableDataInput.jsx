import { useState } from "react";


export default function TableDataInput({ postObj }) {
    const [tableDataFile, setTableDataFile] = useState();


    const handleDataChange = (e) => {
        const files = Array.from(e.target.files);
        const tableDataFile = files[0];
        postObj.table_data = tableDataFile;

        // console.log(tableDataFile);
        setTableDataFile(tableDataFile);
    }


    return (
              <div className="form-group">
                <label htmlFor="table_data">Table Data 파일 선택</label>
                <input
                  type="file"
                  id="table-data"
                  name="table_dataes"
                //   multiple
                  accept=".xlsx,.xls,.csv"
                  onChange={handleDataChange}
                />

              </div>
      )
    }