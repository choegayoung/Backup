import axios from 'axios' // << 서버에 데이터를 달라고 요청하거나 데이터를 보낼 때 쓰는 라이브러리

const Home = () => {
  const btn1Event = () => {
    console.log("호출")
    axios.get("http://localhost:23306/") // << 백엔드 서버로 데이터를 보내달라고 요청 (get)
      .then(res => {                     // << 요청이 성공하면 실행 (res = 서버의 응답 객체)
        console.log(res.data)            // << 서버가 보내준 데이터를 출력
        if(res.data.status) {            // << 서버 응답 데이터 중 status가 true인지 확인
          alert(res.data.result[0])}     // << result 배열의 첫 번째 내용을 띄움
          else {
            alert("오류")                 // << 서버는 응답했지만, status가 False인 경우
          }
        }) // 성공 시
      .catch(err => console.log(err))     // << 서버 접속 실패 
      .finally(() => console.log("완료"))  // << 성공하든 실패하든 통신이 끝나면 무조건 실행
  }
  return (
    <div className="text-center">
      <h1>메인 화면입니다.</h1>
      <button type="button" onClick={btn1Event}>fastAPI확인</button>
    </div>
  )
}

export default Home