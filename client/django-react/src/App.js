import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Axios from 'axios'
import Loader from './Loader'

class App extends Component {
  constructor(props) {
      super(props)
      this.state = {
          isLoaded:false
      }
      
  } 
    componentDidMount= async ()=>{
        const response = await Axios.get('/reddit/post/hot/new')
        const redditPosts = response.data.data.map((item)=>{
            return(
                <div>
                <h3>{item.title}</h3>
            </div>
            )
            
        })
        console.log(response.data);
        this.setState({
            posts: redditPosts,
            isLoaded: true
            })
        
    }
  
  
    render() {
    return (
      <div className="App">
        <header className="App-header">
        <div>{this.state.isLoaded ? this.state.posts : <Loader/>}</div>
          
        </header>
      </div>
    );
    
  }
}


export default App;
