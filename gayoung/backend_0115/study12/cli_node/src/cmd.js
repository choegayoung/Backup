import fs from 'fs'; //파일 읽기, 쓰기 기능

const getData = () => { 
    const f = fs.readFileSync("./data/memo.json", 'utf-8')  //("./data/memo.json", 'utf-8') 내용을 f에 문자열로 넣는다
    // const data = JSON.parse(f) //자료형을 obj로 바꿔주는 함수
    return JSON.parse(f)
}

export const add = (a, b) => {
    const data = getData();
    const result = Number(a) + Number(b)
    data.list.push(result) //result 값을 list에 넣는다
    console.log (data, result);
    fs.writeFileSync("./data/memo.json", JSON.stringify(data)/* data값을 문자열로 변환 */, 'utf-8') //memo파일에 새로운 숫자를 넣어주는 함수
}

export const list = () => {
    console.log("list() 호출됨");
    const arr = getData().list;
    for(const v of arr) console.log(v);
    }
