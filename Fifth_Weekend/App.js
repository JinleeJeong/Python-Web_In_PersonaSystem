import React, { Component } from 'react';
import './App.css';
import Template from './component/Template';
import Logo from './Image/logo.png';
class App extends Component {
  state = {
    
  }

  render() {
    return (
        <Template img={Logo} alt="">
        </Template>
    );
  }
}

export default App;
