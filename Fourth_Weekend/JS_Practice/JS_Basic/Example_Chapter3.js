var site = prompt("네이버, 다음, 구글 중 \
좋아하는 사이트?");

var url;

switch(site){
    case "네이버" : url = "www.naver.com";
    break;
    case "다음" : url ="www.daum.net";
    break;
    case "구글" : url = "www.google.com";
    break;

    default: alert("주소값에 없습니다.");
}

if(url){
    location.href = "Http://"+url;
}