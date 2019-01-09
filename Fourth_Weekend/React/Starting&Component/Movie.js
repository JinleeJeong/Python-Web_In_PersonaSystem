import React, { Component } from 'react';
import './Movie.css';
import proptypes from 'prop-types';

class Movie extends Component {

    static propTypes = {
        title: proptypes.string.isRequired,
        poster : proptypes.string.isRequired
    }
// proptype의 형과 반드시 있는지 없는지 확인을 할 수 있다.
    render() {
        return(
            <div>
            <h1>{this.props.title}</h1>
            <MoviePoster poster={this.props.poster}/>
            </div>
        ) // this로 부모에게서 받은 prop을 출력가능하다.
    }
}

class MoviePoster extends Component {

    static propTypes = {
        poster : proptypes.string.isRequired
    }
    render() {
        return(
            <img src={this.props.poster} alt="Test"></img>
        )
    }
}

export default Movie
