import React from 'react';
import './Movie.css';
import proptypes from 'prop-types';
import LinesEllipsis from 'react-lines-ellipsis'
// class Movie extends Component {

//     static propTypes = {
//         title: proptypes.string.isRequired,
//         poster : proptypes.string.isRequired
//     }
// // proptype의 형과 반드시 있는지 없는지 확인을 할 수 있다.
//     render() {
//         return(
//             <div>
//             <h1>{this.props.title}</h1>
//             <MoviePoster poster={this.props.poster}/>
//             </div>
//         ) // this로 부모에게서 받은 prop을 출력가능하다.
//     }
// }
// class MoviePoster extends Component {

//     static propTypes = {
//         poster : proptypes.string.isRequired
//     }
//     render() {
//         return(
//             <img src={this.props.poster} alt="Test"></img>
//         )
//     }
// }

function Movie({title, poster, genres, synopsis}) {
    return(
        <div className="Movie">
            <div className="Movie_Columns">
            <MoviePoster poster={poster} alt={title}/>
            </div>
            <div className="Movie_Columns">
            <h1>{title}</h1>
                <div className="Movie_Genres">
                    {genres.map((genre, index) => <MovieGenre genre={genre} key={index}/>)}
                </div>
                <p className="Movie_Synopsis">
                    <LinesEllipsis
                    text={synopsis}
                    maxLine='3'
                    ellipsis='...'
                    trimRight
                    basedOn='letters'
                    />  
                </p>
            </div>
        </div>
    )
}
function MoviePoster({poster, alt}){
    return(
        <img src={poster} alt={alt} title={alt} className="Movie_Poster"></img>
    )
} // 이미지의 alt를 위해서 다로 컴포넌트 생성
function MovieGenre({genre}){
    return (
        <span className="Movie_Genres">{genre}</span>
    )
} // genre는 배열로 되어 있기 때문에 따로 컴포넌트 생성

Movie.propTypes = {
    title : proptypes.string.isRequired,
    poster : proptypes.string.isRequired,
    genres : proptypes.array.isRequired,
    synopsis : proptypes.string.isRequired
}

MoviePoster.propTypes = {
    poster : proptypes.string.isRequired, 
    alt : proptypes.string.isRequired
}
MovieGenre.propTypes = {
    genre : proptypes.string.isRequired
}
export default Movie

// stateless Function 구문 Smart vs Dumb Components render 거치지 않고, 순서도 거치지 않는다.