import fs from 'fs'

const getData = () => { 
    const f = fs.readFileSync("./data/memo.json", 'utf-8')  //("./data/memo.json", 'utf-8') 내용을 f에 문자열로 넣는다
    // const data = JSON.parse(f) //자료형을 obj로 바꿔주는 함수
    return JSON.parse(f)
}

const setData = () => {
    fs.writeFileSync("./data/memo.json", JSON.stringify(data), 'utf-8')
    list()
}

export const add = (word) => { 
    const data = getData();
    const list = data.list;
    const key = (list.length === 0) ? 1 : list.at(-1).key + 1 // key값을 구하는 코드
    const result = {key, word}

    list.push(result) //result 값을 list에 넣는다
    data.list =  list
    console.log (data, result, key);
    fs.writeFileSync("./data/memo.json", JSON.stringify(data)/* data값을 문자열로 변환 */, 'utf-8') //memo파일에 새로운 숫자를 넣어주는 함수
}

export const list = () => {
    console.log("list() 호출됨");
    const arr = getData().list;
    for(const v of arr) console.log(v);
    }

export const remove = (key) => {
    console.log("단어 삭제됨")
    const data = getData();
    const list = data.list;
    data.list = list.filter(v => v.key !== Number(key))
    setData(data)
    //fs.writeFileSync("./data/memo.json", JSON.stringify(data)/* data값을 문자열로 변환 */, 'utf-8')
}

export const edit = (word, editword) => {
    console.log("단어 수정")
    const data = getData();
    const list = data.list //따로 변수로 만들고
    list[list.indexOf(word)] = editword // 해당 값의 인덱스를 찾아 그 자리에 새 단어를 넣는다
    console.log (data.list);
    fs.writeFileSync("./data/memo.json", JSON.stringify(data)/* data값을 문자열로 변환 */, 'utf-8')
}