import axios from "axios"
import { useState } from "react"
import {jwtDecode} from "jwt-decode"


const api = axios.create({
    baseURL: "http://localhost:23306",
    withCredentials: true,
    headers: {
        "Content-Type" : "application/json"
    }
})

const Login = () => {

    const [email, setEmail] = useState("")
    const [pwd, setPwd ] = useState("")

    const submitEvent = e => {
      e.preventDefault()
      const params = {email, pwd}
      console.log("확인", params)
      api.post("/key", params)
      .then(res => {
        console.log(res)
        if (res.data.status) {
          console.log(res.data.access_token)
        }
      })
    }
    return(
         <>
    <div className="container mt-3">
			<h1 className="display-1 text-center">로그인</h1>
			<form onSubmit={submitEvent}>
				<div className="mb-3 mt-3">
					<label htmlFor="email" className="form-label">이메일</label>
					<input type="email" className="form-control" id="email" placeholder="이메일를 입력하세요." value={email} onChange={(e)=>setEmail(e.target.value)} required={true} autoComplete="off" />
				</div>
				<div className="mb-3">
					<label htmlFor="pwd" className="form-label">비밀번호</label>
					<input type="password" className="form-control" id="pwd" placeholder="비밀번호를 입력하세요." value={pwd} onChange={(e) => setPwd(e.target.value)} required={true} autoComplete="off" />
				</div>
        <div className="d-flex">
          <div className="p-2 flex-fill d-grid">
            <button type="submit" className="btn btn-primary">로그인</button>
          </div>
          <div className="p-2 flex-fill d-grid">
            <button type="button" className="btn btn-primary">취소</button>
          </div>
        </div>
			</form>
		</div>
    </>
    )
}

export default Login