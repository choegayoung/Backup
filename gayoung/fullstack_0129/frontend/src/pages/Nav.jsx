import { useNavigate } from 'react-router-dom'
import { useEffect } from 'react'

const Nav = () => {
    const navi = useNavigate("")
    

    return(
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
		<div className="container-fluid">
			<a className="navbar-brand" href="http://localhost:5173/">TEAM3</a>
			<button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
				<span className="navbar-toggler-icon"></span>
			</button>
			<div className="collapse navbar-collapse" id="navbarNav">
				<ul className="navbar-nav">
					<li className="nav-item">
						<button className="nav-link" onClick={() => navi("/login")}>로그인</button>
					</li>
					<li className="nav-item">
						<a className="nav-link" href="../index.html">로그아웃</a>
					</li>
					<li className="nav-item">
						<button className="nav-link" onClick={() => navi("/signup")}>회원가입</button>
					</li>
					<li className="nav-item">
						<button className="nav-link" onClick={() => navi("/userview")} >회원정보</button>
					</li>
				</ul>
			</div>
		</div>
		</nav>
    )
}

export default Nav