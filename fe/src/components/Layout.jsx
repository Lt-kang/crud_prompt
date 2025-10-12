import { useEffect } from "react";
import { Outlet, useNavigate, useLocation } from "react-router-dom";



function LinkButton({ to, children, showForm }) {
  const navigate = useNavigate();

  const handleClick = () => {
    if (!showForm) {
        navigate(to);
    }
    else {
        navigate("/");
    }
  };

  return (
    <button className="btn btn-primary"
            onClick={handleClick}>
        {children}
    </button>
  );
}

export default function Layout( { showForm, setShowForm }) {
  const location = useLocation();
  const pathName = location.pathname;

  useEffect(() => {
    if (pathName === '/create-post') {
      setShowForm(true);
    }
    else {
      setShowForm(false);
    }
  }, [pathName]);


  return (
    <div className="app">
        <header className="app-header">
            <h1>📝 Prompt Test Page</h1>
            <LinkButton to="create-post" 
                        showForm={showForm}>
                {showForm ? '작성 취소' : '새 글 작성'}
            </LinkButton>
        </header>
      
      <Outlet />
    </div>
  );
}