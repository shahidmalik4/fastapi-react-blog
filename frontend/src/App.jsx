import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import BlogList from './components/BlogList';
import BlogDetail from './pages/BlogDetail';
import CreatePost from './pages/CreatePost';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <Navbar />
        <Routes>
          <Route path="/" element={<BlogList />} />
          <Route path="/blogs/:id" element={<BlogDetail />} />
          <Route path="/create" element={<CreatePost />} />
        </Routes>
    </Router>
  );
}

export default App;
