import { API_URL } from '../App';


export async function SubmitPost(formData) {
  console.log(API_URL);
  console.log("SubmitPost");
  // formData의 구성요소를 console로 확인
  for (let [key, value] of formData.entries()) {
    if (value instanceof File) {
      console.log(`${key}: File - name: ${value.name}, size: ${value.size}, type: ${value.type}`);
    } else {
      console.log(`${key}:`, value);
    }
  }

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
  };

  