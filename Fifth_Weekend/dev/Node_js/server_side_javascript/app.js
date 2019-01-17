/* 
	노드 다운로드 후, node x.js로 실행 가능
	supervisor 설치 후 하면 자동 업데이트
	file 생성 후 npm init해서, 모듈을 가져올 수 있도록 함
	underscore, uglifyjs
	sync, Async : sync_async.js 참조 비동기는 콜백 함수 필요
	express > node.js보다 편리함 
	프레임워크로 서버 연결, 다양한 템플릿 엔진, 정적 동적 제공 JS 제공
	Ex) vim ~~ & <img src="~"> 가능
	About pug 퍼그는 템플릿 엔진으로 언어가 다르지만, 프로그래머블함
	
*/







// express로 구현하는 방식 node.js보다 훨씬 편리함
// supervisor app.js로 실행하면 자동으로 동적도 넘겨준다.
var express = require('express');
var app = express();
// express는 함수로 되어 있어, app으로 받아서 넘긴다.
app.use(express.static('public'));
app.set('views', './views');
app.set('view engine', 'pug');
app.locals.pretty = true;
// Express 템플릿 엔진 jade 사용 views 파일에 jade 확장자를 읽음

app.get('/route', (req,res) => {
	res.send('Route <img src="/logo.png">');
})
// static을 써서 정적인 파일을 넣은 후 아래 img와 같이 출력 가능하다.

app.get('/', (req,res) => {
	res.send('Come in ');
});

app.get('/dynamic', (req,res) => {
	var lie = '';
	var time = Date();
	for(i = 1 ; i<5 ; i++){
		lie += '<li>Testing</li>';
	}
	var dynamic = `
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta http-equiv="X-UA-Compatible" content="ie=edge">
		<title>Document</title>
	</head>
	<body>
		<h1>Dynamic File</h1>
		
		${time}
	</body>
	</html>`
	res.send(dynamic);
}) // Static File은 node app.js 없이 자동 변환 가능
	/* Dynamic file은 Ctrl + C 서버 종료 후 변환 가능 해결 > supervisor
	JS을 사용해, 그레이브 엑센트에 ${x} 변수 사용 가능 */
app.get('/login', (req,res) => {
	res.send('<h2>login plz<h2>');
})
app.listen(1337,() => {
	console.log('connected 1337 port!');
});
// listen으로 포트번호와 hostname을 전달해주는 것이 일반적

app.get('/template', (req,res) => {
	res.render('temp', {time:Date(), _title:'Pug'});
})
/* Express 템플릿 엔진 사용 법 
	1. npm install pug --save < console
	2. app.set('views', './views');
	3. app.set('view engine', 'pug');
	4. app.get('/template', (req,res) => {
		res.render('temp');
	})
// 4번에서 send가 아닌, 템플릿 엔진을 렌더링해서 만들어 줌
	resistence 객체도 render() 함수 가지고 있음 > Express API
	*/
