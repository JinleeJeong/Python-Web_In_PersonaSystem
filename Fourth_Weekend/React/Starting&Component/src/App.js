import React, { Component } from 'react';
import './App.css';
import Movie from './Movie';


// 배열로써 정리한다. 
class App extends Component {

  componentDidMount(){
    this._getMovies();
  }
 
  state = {
  }

  _renderMovies = () => {
    const movies = this.state.movies.map((movie) => {
      return <Movie 
      title = {movie.title} 
      poster = {movie.medium_cover_image} 
      key = {movie.id} 
      genres= {movie.genres}
      synopsis = {movie.synopsis}/>
    }) 
    return movies;
  }
  
  _getMovies = async() => {
    const movies = await this._callApi()
    this.setState({
      movies
    });
  };

  _callApi = () => {
    return fetch('https://yts.am/api/v2/list_movies.json?sort_by=rating')
    .then(response => response.json())
    .then(json => json.data.movies)
    .catch(err => console.log(err))
  }
 // movies 변수에 저장하는 방식
 // = () => {} 는
 
  render() {
    const {movies} = this.state;
    return (
      <div className={movies ? "App" : "App--loading"}>
          {movies ? this._renderMovies() : 'Loading'} 
      </div>
    );
  }
}
// map을 해서, 배열을 새로 만들고, index를 key에 넘겨준다. prop로 title, poster을 넘겨준다.
// movies가 있을때는 _renderMovies()실행! 언더바의 이유는, 기존에 있는거 중복을 회피하기 위해서이다. >>> 이 방식이 Loading state 방식! 
export default App;

// DidMount > getMovie > CallAPI > movies 저장 > render에서 renderMovies호출 > render의 movies를 받아온다. > props로 넘겨줌