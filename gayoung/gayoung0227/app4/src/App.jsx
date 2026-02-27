import { useEffect, useState } from "react"
import axios from "axios"
import './App.css'
// import { useAuth } from "@hooks/AuthProvider"

const App = () => {
  const api = axios.create({
    baseURL: "http://aiedu.tplinkdns.com:6203/app1" || "http://localhost:8001",
    withCredentials: true,
    headers: {
      "Content-Type": "application/json",
    },
  })
  const [nickname, setNickname] = useState("")
  const [profilePath, setProfilePath] = useState("")
  const Login = () => {
    window.location.href = "http://aiedu.tplinkdns.com:6203/app1/login/kakao"
          }
  useEffect(() => {
    api.get("/me")
      .then(res => {
        setNickname(res.data.userInfo["nickname"])
        setProfilePath(res.data.userInfo["profile_image"])
      })
    }, [])
          
  return (
    <div className="container mt-3 position-relative">
      <button onClick={()=> Login()}>로그인</button>
      <h1 className="display-1 text-center">회원정보</h1>
      <div>
        <img src={profilePath} className="user_pt_view" />
      </div>
      <form>
          <div className="mb-3 mt-3">
            <label htmlFor="name" className="form-label">Nickname</label>
            <input type="text" className="form-control" id="name" name="name" readOnly="readonly" defaultValue={nickname}/>
          </div>
        <div className="d-flex">
          <div className="p-2 flex-fill d-grid">
            <button type="button"  className="btn btn-primary">취소</button>
          </div>
          <div className="p-2 flex-fill d-grid">
            <button type="button" className="btn btn-primary">수정</button>
          </div>
          <div className="p-2 flex-fill d-grid">
            <button type="button" className="btn btn-primary">탈퇴</button>
          </div>
        </div>
      </form>
    </div>
  )
}

export default App