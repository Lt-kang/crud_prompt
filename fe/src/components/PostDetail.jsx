import { useNavigate, useParams } from "react-router-dom";
import { useState, useEffect } from "react";
import { API_URL } from "../App"

function BoarderLine() {
    return (
        <hr style={{ margin: "20px 0", border: "none", borderTop: "2px solid #e9ecef" }} />
    )
}


async function GetPostInfo(id) {
    const response = await fetch(`${API_URL}/api/v1/post/${id}`);
    if (response.status === 200) {
        const data = await response.json();
        return data;
    } else {
        console.error("Failed to fetch post info");
        return null;
    }
}


function LeftButton( { index, setIndex } ) {
    return (
        <button
            style={{ margin: "0 5px" }}
            onClick={() => setIndex(index - 1)}
            disabled={index === 0}
        >◀</button>
    )
}

function RightButton( { index, setIndex, maxIndex } ) {
    return (
        <button
            style={{ margin: "0 5px" }}
            onClick={() => setIndex(index + 1)}
            disabled={index === maxIndex}
        >▶</button>
    )
}

export default function PostDetail() {
    const navigate = useNavigate();
    const [index, setIndex] = useState(0);
    const { id } = useParams();
    const [selectedPost, setSelectedPost] = useState(null);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        const fetchPost = async () => {
            const post = await GetPostInfo(id);
            if (post) {
                setSelectedPost(post);
            }
            setLoading(false);
        };
        
        fetchPost();
    }, [id]);

    console.log(selectedPost);

    if (loading) {
        return <div>로딩 중...</div>;
    }

    if (!selectedPost) {
        return <div>게시글을 찾을 수 없습니다.</div>;
    }

    
    

    const handleBackToList = () => {
        navigate("/");
    };

    

    return (
    <div className="post-detail">
        <div className="post-header">
        
            <button className="btn btn-secondary back-btn"
                    onClick={handleBackToList}
            >← 목록으로 돌아가기
            </button>

        <h2>{selectedPost.title}</h2>
            <div className="post-meta">
                {/* <span>작성자: {selectedPost.author}</span> */}
                <span>작성일: {selectedPost.date}</span>
                <span>{selectedPost.prompt_tag}</span>
            </div>
        </div>

        <div className="post-content-prompt">
        <h3>사용된 모델</h3>
            
            <br></br>
            <div className="preserve-whitespace">
                {selectedPost.model}
            </div>
            <br></br>
            <br></br>


            <h3>사용된 프롬프트</h3>
            
            <br></br>
            <div className="preserve-whitespace">
                {selectedPost.prompt_content}
            </div>
            <br></br>
            <br></br>


            <BoarderLine />


            <h3>출력된 결과 {index+1}/{selectedPost.result.length}  
                <LeftButton index={index} setIndex={setIndex} /> 
                <RightButton index={index} setIndex={setIndex} maxIndex={selectedPost.result.length - 1} /> 
            </h3>
            
            <br></br>
            <div style={{ whiteSpace: 'pre-wrap' }}>
            {selectedPost.result[index]}
            </div>
            <br></br>
            <br></br>
        </div>


        <div className="post-actions">
            <button className="btn btn-danger"
                    onClick={() => alert("삭제 기능 미구현")}
            >삭제
            </button>
        </div>
    </div>
    )
}