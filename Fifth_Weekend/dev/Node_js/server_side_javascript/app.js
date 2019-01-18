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
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: false}));
// post 방식의 body를 사용하기 위해서는 bodyParser를 install 한 후, 입력 후 사용 가능


app.use(express.static('public'));

app.set('views', './views');
app.set('view engine', 'pug');
app.locals.pretty = true;
// Express 템플릿 엔진 jade 사용 views 파일에 jade 확장자를 읽음

app.get('/route', (req,res) => {
	res.send('Route <img src="/logo.png">');
})
// static을 써서 정적인 파일을 넣은 후 아래 img와 같이 출력 가능하다. node static.js public에 들어있어!

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
		${lie}
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
// listen으로 포트번호와 hostname을 전달해주는 것이 일반적 여기서 연결해준다.★★★★★

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

	

	
app.get('/topic/:id', (req,res) => {
	

	var topics = [
		'JS',
		'Node',
		'Express',
	]
	var output = `
		<a href="/topic/0">JS</a><br>
		<a href="/topic/1">Node</a><br>
		<a href="/topic/2">Express</a><br>
		${topics[req.params.id]}
	`
	res.send(output);
})

// 쿼리 스트링 : url 뒤에 ?이후에 나오는 요소들 설정 id=1,2,3설정 가능 
//	req.query.id로 설정 /topic?id=0으로 설정 하지만 이 방법보다는 params가 더 현대적
// 자세한건 Express
// Document 참조
// ? 가 아니라, /topic/1~3 으로 표현하는 것은 시멘틱 URL이다. req.params.id로 바꾼다.
// 그리고 get('/topic/:id') 이런식으로 표현한다. 아래의 id와 위의 id는 같아야 한다.
app.get('/topic/:id/:mode', (req,res) => {
	res.send(req.params.id+ ',' + req.params.mode)
})


/*
	Get 방식 => 사용자가 서버에게 요청한 페이지를 그대로 App을 통해서 받아옴
	Post 방식 => 사용자가 입력하여 정보를 전달함 (로그인 : Id, Pwd를 서버로 전달)
*/

app.get('/form', (req,res) => {
	res.render('form');
})
app.get('/form_receiver', (req,res) => {
	var x = req.query.title;
	var y = req.query.description;
	res.send(x+','+y);
})

app.post('/form_receiver', (req,res) => {
	var x = req.body.title;
	var y = req.body.description;
	res.send(x+','+y)
})
/* 
	form을 만들어서, 사용자가 제목 내용을 입력하도록 하고, form의 action으로 어떠한
	페이지로 넘긴다. 그 후에 ?title=1&description=2 이런식으로 나와서 그것을 query로
	받아온다. 변수에 저장 가능! 하지만 form 형식 method='post'로 하면 주소에 출력X
	데이터로만 넘어올 수 있다. 그래서 app.get형식이면 method='get'으로 하면 
	가져올 수 있음.


	하지만 form 형식으로 가져오려면 express의 플로그인(미들웨어)이 필요하다.
	npm install body-parser --save & multer 로 가능하다.
	그래서 사용자의 req가 들어오면 body-parser 미들웨어를 통해서 결과적으로 express가
	req상태에서 미들웨어를 통해 body를 인식 한 후 res를 가능하게 한다. 

	==> get은 1/2/3/4 edit 등 간단한 곳에서 위험 노출되도 되고, 정보전달, 짧을 때 사용
	==> post는 보안 > id, pwd나 긴 글과 같은 곳에서 사용한다.

	또한 post로 받아와서 변수로 저장하는 부분들은 get으로 라우팅을 해줘야 한다. 
	
*/