import React, { Component, Fragment } from 'react';
import './App.css';
import Logo from './Image/logo.png';
import background from './Image/background.PNG';
class App extends Component {
  state = {
    
  }

  render() {
    return (
      <Fragment>
            <header className="header">
              <div className="logo">
                <img src={Logo}></img>
              </div>
                <div className="header_nav">
                  <ul>
                    <li>회원가입</li>
                    <li>로그인</li>
                    <li>한국어</li>
                    <li>새 그룹 시작하기</li>
                  </ul>
                </div>
              </header>


          <div className="container">
            <section className="background">
                      <img src={background}></img>
                      <div className="background_text">
                          <ul className="background_li">
                            <li>Study Web Project</li>
                            <li><a href="">회원가입</a></li>
                          </ul>
                      </div>
                      
                      <div className="background_search">
                        <input type="text"></input>
                      </div> 
            </section>

            <section>
              영상
            </section>
          </div>

          <div>
            <footer></footer>
          </div>
      </Fragment>
    );
  }
}

export default App;
