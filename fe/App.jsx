import React, { useState, useEffect, useContext } from 'react';
import './App.css';
import CreatePost from './components/CreatePost';
import { Routes, Route, Outlet, useNavigate } from "react-router-dom";
import { PostProvider } from './context/PostContext';
import Layout from './components/Layout';
import Home from './components/Home';
import PostDetail from './components/PostDetail';


export const API_URL = "http://localhost:8020";





async function GetPosts() {
  const response = await fetch(`${API_URL}/api/v1/posts`);
  if (response.status === 200) {
      const data = await response.json();
      return data;
  } else {
      console.error("Failed to fetch posts");
      return null;
  }
}


export default function App() {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    const fetchPosts = async () => {
      const posts = await GetPosts();
      if (posts) {
        setPosts(posts);
      }
    };
    
    fetchPosts();
    setPostIndex(posts.length + 1);
  }, []);

  


  const [showForm, setShowForm] = useState(false);
  const [postIndex, setPostIndex] = useState(1);


  return (
    <PostProvider>
      <Routes>
        <Route element={<Layout showForm={showForm} setShowForm={setShowForm} />}>
          <Route index element={<Home posts={posts}/>} />

          <Route path="post/:id" element={<PostDetail/>} />

          <Route path="create-post" element={<CreatePost 
                                                        setShowForm={setShowForm} 
                                                        postIndex={postIndex}
                                                        />} />
        </Route>
      </Routes>
    </PostProvider>
  )
}

