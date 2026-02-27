import axios from "axios";


const Log_in = () => {
    const submitEvent = e => {
        const info = {
            "email" : e.target.email.value,
            "pwd" : e.target.pwd.value
        }
        console.log(info)
    }
    
    return(
        <>
    <div className="container mt-3">
			<h1 className="display-1 text-center">로그인</h1>
			<form onSubmit={submitEvent}>
				<div className="mb-3 mt-3">
					<label htmlFor="email" className="form-label">이메일</label>
					<input type="email" className="form-control" id="email" placeholder="이메일를 입력하세요." name="email" required={false} autoComplete="off" />
				</div>
				<div className="mb-3">
					<label htmlFor="pwd" className="form-label">비밀번호</label>
					<input type="password" className="form-control" id="pwd" placeholder="비밀번호를 입력하세요." name="pwd" required={false} autoComplete="off" />
				</div>
        <div className="d-flex">
          <div className="p-2 flex-fill d-grid">
            <button type="submit" className="btn btn-primary" onClick={submitEvent} >로그인</button>
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

export default Log_in