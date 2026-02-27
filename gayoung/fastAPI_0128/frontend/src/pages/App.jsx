import { useState } from 'react'
import { AuthContext } from '@hooks/AuthContext.js' // << 제일 상위파일에서 전역변수를 이용할 수 있게 함
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import { BrowserRouter, Routes, Route } from "react-router";
import '@styles/App.css'
import Home from '@pages/Home.jsx'
import NotFound from '@pages/NotFound.jsx'
import Nav from '@pages/Nav.jsx'
import Login from '@pages/Login.jsx'
import Log_in from './log_in';

const App = () => {
  const [isLogin, setIsLogin] = useState(false) // << 제일 상위파일에서 선언.
  const paths = [
    {path: "/", element: <Home />},
    {path: "/login", element: <Login />},
    {path: "*", element: <NotFound />},
    {path: "/test", element: <Log_in />},
  ]
  return (
    <AuthContext.Provider value={{ isLogin, setIsLogin }}> {/*<< 태그 안에 있는 것들에게 적용시킴*/}
      <Nav />
      <BrowserRouter>
        <Routes>
          { paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />) }
        </Routes>
      </BrowserRouter>
    </AuthContext.Provider>
  )
}

export default App