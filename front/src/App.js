import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Home from './comonents/home';
import About from './comonents/about';
import Nav from './comonents/nav';
function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Nav/>
        <Routes>
          
          <Route path='/' element={<Home/>}/>
          <Route path='/about' element={<About/>}/>
        </Routes>
        
      </BrowserRouter>
    </div>
  );
}

export default App;
