import { BrowserRouter, Routes, Route } from "react-router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import Login from './Login'
import Signup from "./Signup";
import User_edit from "./User_edit";
import Index from ".";
import User_viwe from "./User_view";


const App = () => {
  const paths = [
    {path: "/", element: <Index />},
    {path: "/login", element: <Login />},
    {path: "/signup", element: <Signup />},
    {path: "/useredit", element: <User_edit />},
    {path: "/userview", element: <User_viwe />},


  ]
  return (
          <BrowserRouter>
            <Routes>
              { paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />) }
            </Routes>
          </BrowserRouter>

  )
}

export default App
