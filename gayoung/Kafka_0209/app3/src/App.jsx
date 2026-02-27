import { useState } from "react";
import axios from "axios"

function App() {
  const[token,setToken] = useState("")
  const event1 = e => {
    e.preventDefault()
    console.log("코드 발급",e.target.email.value)
    axios.post("http://localhost:8001/login", {"email":e.target.email.value})
    .then(res => {
      console.log(res)
      if (res.data.status){
      e.target.email.value = ""
    alert("email 발급")}
    else alert("email존재하지 않습니다")})
    .catch(err => console.err(err))
  }
  const event2 = e => {
    e.preventDefault()
    console.log("토큰 발급")
    axios.post("http://localhost:8001/code",  {"code":e.target.code.value})
    .then(res => {
      console.log(res)
      if (res.data.status) {
        e.target.code.value = ""
        setToken(res.data.access_token)
        alert("토큰 발급")}
        else alert("코드가 유효하지 않습니다")
        .catch(err => console.log(err))
    })
  }
  const event3 = () => {
    console.log("사용자 정보 요청")
    axios.post("http://localhost:8001/me",{}
      ,{headers: {"Authorization":`Bearer ${token}`}})
    .then(res => console.log(res))
    .catch(err => console.error(err))
  }
  return(
    <>
      <form onSubmit={event1}>
        <input type="email" name = "email" required autoComplete="off"/>
        <button type ="submit">코드 발급</button>
      </form>
      <hr/>
      <form onSubmit={event2}>
        <input type="text" name = "code"/>
        <button type ="submit">토큰 발급</button>
      </form>
      <hr/>
      <button type="button" onClick={event3}>사용자 정보</button>
    </>
  )
}

export default App