import React, { Component } from 'react';
import './App.css';
import Movie from './Movie';

const movies = [
  {
    title: "Martrix",
    poster : "https://images-na.ssl-images-amazon.com/images/I/51EG732BV3L.jpg"
  },
  {
    
    title : "Full Metal Jacket",
    poster : "https://images-na.ssl-images-amazon.com/images/I/81U3cu+0RAL._RI_.jpg"
  },
  { 
    title : "Oldboy",
    poster : "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Oldboykoreanposter.jpg/220px-Oldboykoreanposter.jpg"
  },
  { 
    title : "Star Wars",
    poster : "https://lumiere-a.akamaihd.net/v1/images/og-generic_02031d2b.png?region=0%2C0%2C1200%2C1200"
  }
]

// 배열로써 정리한다. 
class App extends Component {


  componentWillMount() {
    console.log('will mount');
  }
  componentDidMount(){
    console.log('did mount')
  }
  render() {
    console.log('did render')
    return (
      <div className="App">
          {movies.map((movie, index) => {
            return <Movie title = {movie.title} poster = {movie.poster} key = {index}/>
          })} 
      </div>
    );
  }
}
// map을 해서, 배열을 새로 만들고, index를 key에 넘겨준다. prop로 title, poster을 넘겨준다.
export default App;

