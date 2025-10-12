import { useState } from "react";


export default function ImageInput({ postObj }) {
    const [imageFiles, setImageFiles] = useState([]);


    const handleImageChange = (e) => {
        const files = Array.from(e.target.files);
        const imageFiles = files.filter(file => file.type.startsWith('image/'));
        postObj.image_files = imageFiles;
        // console.log(postObj.image_files);

        setImageFiles(imageFiles);
    }


    return (
              <div className="form-group">
                <label htmlFor="image-files">이미지 파일 선택</label>
                <input
                  type="file"
                  id="image-files"
                  name="image_files"
                  multiple
                  accept="image/*"
                  onChange={handleImageChange}
                />


                {imageFiles && imageFiles.length > 0 && (
                  <div className="selected-data-list">
                    <h4>
                      선택된 PNG 파일 목록 ({imageFiles.filter(file => file.name).length}개)
                    </h4>
                    <ul>
                      {imageFiles
                        .filter(file => file.name)
                        .map((file, idx) => (
                          <li className="selected-data-file" key={idx}>{file.name}</li>
                        ))}
                    </ul>
                  </div>
                )}
              </div>
      )
    }