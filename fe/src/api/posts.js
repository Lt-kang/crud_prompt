export async function SubmitPost(API_URL, post, files = []) {
    const formData = new FormData();
    formData.append('id', post.id);
    formData.append('title', post.title);
    formData.append('date', post.date); 
    formData.append('model', post.model);
    
    
    post.image_files.forEach(file => {
      formData.append('image_files', file, file.name);
    });

    const response = await fetch(`${API_URL}/api/v1/submit`, {
      method: 'POST',
      body: formData
    });
    
    if (response.status === 200) {
      alert("등록 완료!");
    }
    else {
      alert("등록 실패!");
    }
  }

  const [selectedPngFiles, setSelectedPngFiles] = useState([]);
  // 파일 목록에서 PNG 파일만 필터링해서 저장하도록 수정
  const handleFolderChange = (e) => {
    const files = Array.from(e.target.files);
    // 확장자가 .png 또는 .PNG인 파일만 필터링
    const pngFiles = files.filter(file => file.name.toLowerCase().endsWith('.png'));
    setSelectedPngFiles(pngFiles);
  };