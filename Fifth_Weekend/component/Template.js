import React, { Component, Fragment } from 'react';
import './Template.css';
import { ButtonToolbar, Button, MenuItem, DropdownButton, Row, Col, Image, Glyphicon} from 'react-bootstrap';
class Template extends Component {

    

    render() {
        
        const title = '한국어';
        const i = 0;
        
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
                      <ul>
                            <li className="nav_master"><Button>
                                                            <Glyphicon glyph="align-justify" />
                                                        </Button>
                                <ul className="nav">
                                    <li>회원가입</li>
                                    <li>로그인</li>
                                    <li>
                                        <DropdownButton
                                            bsStyle=''
                                            title={title}
                                            key={i}
                                            id={`dropdown-basic-${i}`}
                                            >
                                            <MenuItem eventKey="1"  active>English</MenuItem>
                                            <MenuItem eventKey="2">Chinese</MenuItem>
                                            <MenuItem eventKey="3">Japnese</MenuItem>
                                            </DropdownButton> 
                                        </li>
                                    <li>새 그룹 시작하기</li> 
                                </ul>
                                </li>
                        </ul>
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
                                    <input type="text" ></input>
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
                            <div className="info_photo"> 
                            
                                <Row className="show-grid">
                                    <Col xs={12} sm={8} md={4}>
                                        <Image src={this.props.test} />
                                    </Col>
                                    <Col xshidden sm={8} md={4}>
                                        <Image src={this.props.test} />
                                    </Col>
                                    <Col  xshidden smHidden md={4}>
                                        <Image src={this.props.test} />
                                    </Col>
                                    <Col xs={8} md={4}>
                                        <Image src={this.props.test} />
                                    </Col>
                                    <Col xs={8} md={4}>
                                        <Image src={this.props.test} />
                                    </Col>
                                    <Col xshidden md={4}>
                                        <Image src={this.props.test} />
                                    </Col>
                                </Row>
                            
                            </div>                        
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