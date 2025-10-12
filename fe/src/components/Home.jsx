import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { API_URL } from "../App";

function PostItem({ post }) {
    const navigate = useNavigate();
    return (
        <div key={post.id} className="post-item"
        onClick={() => navigate(`/post/${post.id}`)}>
        <div className="post-info">
          <h3 
            className="post-title"
            style={{ margin: 0, flex: 1}}
          >
            {post.title}
          </h3>
{/* 
          <button 
            className="btn btn-danger btn-small"
            onClick={() => handleDelete()}
          >
            삭제
          </button> */}
          <div className="post-meta">
            {/* <span>작성자: {post.author}</span> */}
            <span>{post.date}</span>
            <span>{post.prompt_tag}</span>
          </div>
        </div>

      </div>
    )
}


export default function Home( {posts} ) {
  // const [posts, setPosts] = useState([
  //   {
  //     id: 1,
  //     title: '첫 번째 게시글입니다',
  //     content: '안녕하세요! 이것은 첫 번째 게시글의 내용입니다.',
  //     author: '관리자',
  //     date: '2024-01-15',
  //     tag: 'Caption'
  //   },
  //   {
  //     id: 2,
  //     title: '두 번째 게시글 제목',
  //     content: '두 번째 게시글의 내용을 작성합니다. 다양한 내용을 포함할 수 있습니다.',
  //     author: '사용자1',
  //     date: '2024-01-14',
  //     tag: 'QA'
  //   },
  //   {
  //     id: 3,
  //     title: '공지사항',
  //     content: '중요한 공지사항을 전달합니다. 모든 사용자가 확인해주세요.',
  //     author: '관리자',
  //     date: '2024-01-13',
  //     tag: 'Caption + OCR'
  //   }
  // ]);




    return (
        <main className="app-main">
          <div className="post-list">
            <h2>게시글 목록 ({posts.length}개)</h2>
            {posts.length === 0 ? (
              <p className="no-posts">게시글이 없습니다.</p>
            ) : (
              <div className="posts">
                {posts.map(post => (
                    <PostItem key={post.id} post={post} />
                ))}
              </div>
            )}
          </div>
      </main>
    );
  }
  