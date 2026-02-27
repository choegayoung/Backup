import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Signup = () => {

    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [pwd, setPwd] = useState("")
    const [gender, setGender] = useState("male")
    const [userlist, setUserlist] = useState([])
	const nav = useNavigate("")

    const submitEvent = e => {
        e.preventDefault()
        const data = {name, email, pwd, gender}
        setUserlist([...userlist, data])
        console.log(userlist)
		alert("회원가입이 완료되었습니다")
		nav("/login")

    }

return(

<div className="container mt-3">
			<h1 className="display-1 text-center">회원가입</h1>
			<form onSubmit={submitEvent}>
				<div className="mb-3 mt-3">
					<label htmlFor="name" className="form-label">이름:</label>
					<input type="text" className="form-control" id="name" placeholder="이름을 입력하세요." required value={name} onChange={(e)=>setName(e.target.value)} />
				</div>
				<div className="mb-3 mt-3">
					<label htmlFor="email" className="form-label">이메일:</label>
					<input type="email" className="form-control" id="email" placeholder="이메일를 입력하세요." required value={email} onChange={(e)=>setEmail(e.target.value)} />
				</div>
				<div className="mb-3">
					<label htmlFor="pwd" className="form-label">비밀번호:</label>
					<input type="password" className="form-control" id="pwd" placeholder="비밀번호를 입력하세요." required onChange={(e)=>setPwd(e.target.value)} />
				</div>
				<div className="d-flex">
					<div className="p-2 flex-fill">
						<div className="form-check">
							<input type="radio" className="form-check-input" id="radio1" name="gender" value="male" checked={gender === "male"} onChange={(e)=> setGender(e.target.value) }/>남성
							<label className="form-check-label" htmlFor="radio1"></label>
						</div>
					</div>
					<div className="p-2 flex-fill">
						<div className="form-check">
							<input type="radio" className="form-check-input" id="radio2" name="gender" value="female" checked={gender === "female"}onChange={(e)=> setGender(e.target.value)}/>여성
							<label className="form-check-label" htmlFor="radio2"></label>
						</div>
					</div>
				</div>
			<div className="d-flex">
				<div className="p-2 flex-fill d-grid">
					<button type="submit" className="btn btn-primary">가입</button>
				</div>
				<div className="p-2 flex-fill d-grid">
					<button type="button" className="btn btn-primary" onClick={() => nav("/")} >취소</button>
				</div>
			</div>
			</form>
        </div>
        )
    }

    export default Signup