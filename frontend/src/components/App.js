import React, { Component } from "react";
import axios from 'axios';
import { BrowserRouter, Link, Route, Routes } from "react-router-dom";
import Home from "./Home";
import Recipy from "./Recipy";
import Recipies from "./Recipies";
import "../styles/styles.css";

class App extends Component{
    state = { details: [], }

    componentDidMount() {
        let data;
        axios.get('http://localhost:8000')
        .then(res => {
            data = res.data;
            this.setState({
                datails: data
            });
        })
        .catch(err => {
            console.log(err);
        })
    }
    render() {
        return (
        <div>
            <BrowserRouter>
                <nav>
                    <Link to="/">Home</Link>
                    <Link to="/recipies">Recipies</Link>
                </nav>
                    <Routes>
                    <Route path='/recipies' element={<Recipies />} />
                    <Route path='/recipies/:id' element={<Recipy />} />
                    <Route path='/' element={<Home />} />
                </Routes>
            </BrowserRouter>
            {this.state.details.map((output, title) => (
                <div key={title}>
                    <div>
                        <h2>{output.title}</h2>
                        <p>{output.description}</p>
                    </div>
                </div>
            ))}
        </div>
        );
    }
}

export default App; 
