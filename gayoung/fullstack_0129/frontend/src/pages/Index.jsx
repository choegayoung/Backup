import React from 'react'
import { useNavigate } from 'react-router-dom'
import { useState } from 'react'

const Index = () => {
    const nav = useNavigate("")
    const [search, setSearch] = useState("")
    const post = [
        {"no": 1 , "title": "지환", "user": "지환"},
        {"no": 2 , "title": "가영", "user": "가영"},
        {"no": 3 , "title": "수아", "user": "수아"},
        {"no": 4 , "title": "윤우", "user": "윤우"},
    ]

    const searchEvent = e => {
        e.preventDefault()
    }
    
    const searchFilter = post.filter((item) => item.title.includes(search))

    return(
        <div className="container mt-3">
			<h1 className="display-1 text-center">게시판</h1>
			<div className="d-flex justify-content-between align-items-center mt-4">
				<div className="btn-group">
					<button onClick={()=>nav("")} className="btn btn-primary">게시글 작성</button>
				</div>
				<form className="d-flex" style={{ maxWidth: "300px" }} onSubmit={searchEvent}>
					<input className="form-control me-2" type="search" placeholder="검색어를 입력하세요" value={search} 
                    onChange={(e) => setSearch(e.target.value)}/>
					<button className="btn btn-outline-dark" type="submit">Search</button>
				</form>
			</div>
			<table className="table table-hover mt-3 text-center">
				<thead className="table-dark">
					<tr>
						<th>no</th>
						<th>게시글</th>
						<th>작성자</th>
					</tr>
				</thead>
				<tbody>
                    {searchFilter.length > 0 ? (
                        searchFilter.map((item) => (
                            <tr key={item.no} className="cursor-pointer" onClick={()=> nav(`/${item.no}`)}>
						<td>{item.no}</td>
						<td>{item.title}</td>
						<td>{item.user}</td>
					</tr>
                    ))
                    ) : (<tr><td colSpan="3">결과가 없습니다.</td></tr>) }
				</tbody>
			</table>
			<nav aria-label="Page navigation example">
				<ul className="pagination justify-content-center mt-4">
					<li className="page-item">
						<a className="page-link" href="#" aria-label="Previous">
							<span aria-hidden="true">&laquo;</span>
						</a>
					</li>
					<li className="page-item"><a className="page-link" href="#">1</a></li>
					<li className="page-item"><a className="page-link" href="#">2</a></li>
					<li className="page-item"><a className="page-link" href="#">3</a></li>
					<li className="page-item">
						<a className="page-link" href="#" aria-label="Next">
							<span aria-hidden="true">&raquo;</span>
						</a>
					</li>
				</ul>
			</nav>
		</div>
        )
}

export default Index