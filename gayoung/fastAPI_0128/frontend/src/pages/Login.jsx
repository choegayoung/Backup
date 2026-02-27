import { useContext } from 'react' // << 데이터를 꺼내 쓰겠다
import { AuthContext } from '@hooks/AuthContext.js' // << 여기에 전역변수를 저장했지롱
import axios from "axios"

// api 라는 변수를 이용하는 이유? 일일이 다 쓰기 귀찮으니까.
const api = axios.create({              // 새로운 Axios 인스턴스 생성
  baseURL: "http://localhost:23306",    // 요청을 보낼 백엔드 주소
  withCredentials: true,                // 백엔드랑 통신할 때 쿠키나 인증헤더를 같이 보낼지?
  headers: {                          
    "Content-Type": "application/json", // fastapi에게 데이터가 json이라는걸 미리 알려준다
  },
})

const Login = () => {                   
  const auth = useContext(AuthContext)  // << AuthContext 안에 있는 내용물을 이용하겠다
  const submitEvent = e => {
    e.preventDefault()

    const params = {                    // 입력받은 값을 params에 저장하겠다
      "email": e.target.email.value,
      "pwd": e.target.pwd.value
    } 
    api.post("/login", params)          // params를 /login 도메인으로 보내겠다
    .then(res => {                      // 성공하면 응답값을
      console.log(res)                  // 콘솔로 보여주고
      auth.setIsLogin(res.data.status)  // 그 값의 상태를 바꿔주는 함수를 실행하겠다. (전역변수)
    })
    .catch(err => console.error(err))   // 실패하면 에러

  }
  const checkEvent = () => {               
    api.get("/user")                    // 백엔드에서 정보(쿠키)를 불러오겠다
    .then(res => console.log(res))      // 성공하면 응답값을 보여줄게
    .catch(err => console.error(err))   // 실패하면 에러

  }
  return (
    <>
    
    <div className="container mt-3">
			<h1 className="display-1 text-center">로그인</h1>
			<form onSubmit={submitEvent}>
				<div className="mb-3 mt-3">
					<label htmlFor="email" className="form-label">이메일</label>
					<input type="email" className="form-control" id="email" placeholder="이메일를 입력하세요." name="email" required={true} autoComplete="off" />
				</div>
				<div className="mb-3">
					<label htmlFor="pwd" className="form-label">비밀번호</label>
					<input type="password" className="form-control" id="pwd" placeholder="비밀번호를 입력하세요." name="pwd" required={true} autoComplete="off" />
				</div>
        <div className="d-flex">
          <div className="p-2 flex-fill d-grid">
            <button type="submit" className="btn btn-primary" onClick={submitEvent} >로그인</button>
          </div>
          <div className="p-2 flex-fill d-grid">
            <button type="button" className="btn btn-primary" onClick={checkEvent}>취소</button>
          </div>
        </div>
			</form>
		</div>
    </>
  )
}

export default Login