import { Link, useNavigate } from 'react-router-dom';
import { useState, useContext } from 'react';
import { API_URL } from '../App';

import { TextInput, TextareaInput } from './CreatePost/TextInput';
import ModelInput from './CreatePost/ModelInput';
import ImageInput from './CreatePost/ImageInput';
import TableDataInput from './CreatePost/TableDataInput';




export default function CreatePost({ setShowForm }) {
    const navigate = useNavigate();

    const [newPost, setNewPost] = useState({
      title: '',
      author: '',

      model: '',
      api_key: '',

      image_files: [],
      table_data: '',
      
      system_prompt: '',
      user_prompt: '',
      createdAt: ''
    });

    

    const handleSubmit = (e) => {
      e.preventDefault();
      console.log(e);
      
      if (newPost.title.trim() && newPost.system_prompt.trim() && newPost.user_prompt.trim()) {
        const post = {
          title: newPost.title,
          date: new Date().toISOString().split('T')[0],
          model: newPost.model,
          prompt_content: newPost.prompt_content,
          image_files: selectedPngFiles
        };
        SubmitPost(post);

        navigate("/")
        setShowForm(false);
      }
    };

    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setNewPost(prev => ({
        ...prev,
        [name]: value
      }));
    };

    const onClickCancel = () => {
      navigate("/");
      setShowForm(false);
    };

    
    return (
        (
            <div className="post-form">
              <h2>Prompt 작성</h2>
              <form onSubmit={handleSubmit}>


                <TextInput postObj={newPost} handleInputChange={handleInputChange} title="제목" id="title" name="title" placeholder="제목" required={true} />
                <TextInput postObj={newPost} handleInputChange={handleInputChange} title="작성자" id="author" name="author" placeholder="작성자" required={false} />
                <BoarderLine />

                <ModelInput postObj={newPost} handleInputChange={handleInputChange} />
                <TextInput postObj={newPost} handleInputChange={handleInputChange} title="API KEY" id="api_key" name="api_key" placeholder="API KEY" required={true} />
                <BoarderLine />

                <ImageInput postObj={newPost} />
                <BoarderLine />

                <TableDataInput postObj={newPost} />
                <BoarderLine />

                <TextareaInput postObj={newPost} handleInputChange={handleInputChange} title="System Prompt" id="system-prompt" name="system_prompt" placeholder="" rows={10} required={true} />
                <TextareaInput postObj={newPost} handleInputChange={handleInputChange} title="User Prompt" id="user-prompt" name="user_prompt" placeholder="Hello, World!" required={true} />

                <FormActions handleSubmit={handleSubmit} onClickCancel={onClickCancel} />
              </form>
            </div>
          )
    )
}

function FormActions({ handleSubmit, onClickCancel }) {
  return (
    <div className="form-actions">
      <button type="submit" className="btn btn-primary"
              onClick={handleSubmit}>
              등록하기
      </button>
      
      <button type="button" 
              className="btn btn-secondary"
              onClick={onClickCancel}>
              취소
      </button>
      
  </div>
  )
}


function BoarderLine() {
  return (
    <hr style={{ margin: "20px 0", border: "none", borderTop: "2px solid #e9ecef" }} />
  )
}



