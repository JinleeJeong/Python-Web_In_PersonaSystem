var fs = require('fs');
// Sync
console.log(1);
var data = fs.readFileSync('data.txt', {encoding: 'utf8'});
console.log(data);

// Async
console.log(2);
var data2 = fs.readFile('data.txt', {encoding:'utf8'}, (err, data) => 
{
    console.log(3);
    if(err) throw err;
    console.log(data);
});
console.log(4);

// readFile을 맡긴 후, 완료되면 return

// 만약 쓰고 싶다면
/*
    fs.writeFile('data/'+title, description, (err)=> {
        if(err){
            console.log(err);
            res.status(500).send('Internal Server Error');
        }
    })
    여기서 콜백함수가 필요하며, status(500)은 내부적으로 서버 오류가 있을 때 사용. 
    여기서는 파일이 dataa라고 되어있는 곳에 저장하려면 생김. 
    data의 폴더가 이미 생성 되어야 한다.

    fs.readdir('data', (err,files) => {
        if(err){
            console.log(err);
            res.status(500).send('Internal Server Error');
        }
        res.render('view', {topics:files});
    })
    디렉토리를 읽어오는 부분, 출력해주는 부분은 pug를 통해서, 변수를 topics로 저장한 후 출력

    ----pug >
    a(href='/') ~

    반복문
    each topic in topics
        li
                a(href='/topic/'+topic)= topic
    article
        h2= title
            =description 두개가 나온다.
*/