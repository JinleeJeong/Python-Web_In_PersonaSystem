import React, { Component } from 'react';
import Logo from './Image/logo.png';
import './App.css';
import Template from './component/Template';
import test from './Image/test.png';
class App extends Component {
  render() {
    return (
      <Template img={Logo} alt="" test={test}>
      </Template>
    );
  }
}

export default App;
