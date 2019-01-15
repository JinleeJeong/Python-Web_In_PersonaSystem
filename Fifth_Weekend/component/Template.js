import React, { Component, Fragment } from 'react';
import './Template.css';
import { ButtonToolbar, Button } from 'react-bootstrap';
class Template extends Component {

    
    render() {

        
        return (
            <Fragment>
            <header className="header">
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"></link>
              <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" media="all"></link>
              <div className="logo">
                <img src={this.props.img} alt={this.props.alt}></img>
              </div>
                <div className="header_nav">
                  <ul>
                    <li>회원가입</li>
                    <li>로그인</li>
                    <li>
                      <div class="dropdown">
                        <button type ="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                          한국어 <span class="caret"></span>
                        </button>
                          <ul class="dropdown-menu">
                            <li><a href="https://github.com">Another action</a></li>
                            <li><a href="https://github.com">Action</a></li>
                            <li><a href="https://github.com">Something else here</a></li>
                            <li><a href="https://github.com">Separated link</a></li>
                          </ul>
                      </div> 
                    </li>
                    <li>새 그룹 시작하기</li>
                  </ul>
                </div>
              </header>


                <div className="_container">
                    <section className="background">
                            <div class ="background_image">
                                <div className="background_text">
                                    <ul className="background_li">
                                    <li>Study Web Project</li>
                                    <li>
                                        <ButtonToolbar>
                                        <Button>회원가입</Button>
                                        </ButtonToolbar>
                                    </li>
                                    </ul>
                                </div>
                                <div className="background_search">
                                
                                <div className="background_search_text">
                                    <input type="text" placeholder="원하는 지역을 입력하세요."></input>
                                    <span class="glyphicon glyphicon-search" aria-hidden="true"></span>
                                    <div className="background_search_text_middle">지역 : 서울, KR</div>
                                </div>

                                
                                </div>
                            </div>
                    </section>

                    <section className="info">
                        <div>
                        <div>
                            <div className="info_search">정렬 기준 : 정확도 순</div>
                                <ul className="info_photo">
                                        <li className="info_main1"></li>
                                        <li className="info_main2"></li>
                                        <li className="info_main3"></li>
                                        <li className="info_main4"></li>
                                        <li className="info_main5"></li>
                                        <li className="info_main6"></li>
                                    
                                </ul>       
                        </div>
                        </div>
                    </section>
                </div>
                
                <div className="footer">
                    <footer>
                        <div className="footer_introduce">
                            Study Project_Layout
                        </div>
                        <div>

                        </div>
            </footer>
          </div>
      </Fragment>
        );
    }
}

export default Template;