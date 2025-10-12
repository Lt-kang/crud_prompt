import { createContext, useState } from "react";

export const PostContext = createContext();

export const PostProvider = ({ children }) => {
  const [newPost, setNewPost] = useState({
                                            title: '',
                                            author: '',

                                            api_key: '',
                                            model: '',

                                            image_files: [],
                                            table_data: '',
                                            
                                            system_prompt: '',
                                            user_prompt: '',
                                            createdAt: ''
                                          });

  
    return (
      <PostContext.Provider value={{ newPost, setNewPost }}>
        {children}
      </PostContext.Provider>
    );
  };