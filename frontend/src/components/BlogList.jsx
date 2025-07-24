import { Link } from 'react-router-dom';
import { useEffect, useState } from 'react';
import api from '../api';

function BlogList() {
  const [blogs, setBlogs] = useState([]);

  const fetchBlogs = async () => {
    try {
      const response = await api.get('/blogs');
      setBlogs(response.data);
    } catch (error) {
      console.error('Error fetching blogs:', error);
    }
  };

  useEffect(() => {
    fetchBlogs();
  }, []);

  return (
    <div className="container-fluid py-4 px-4">
      <div className="d-flex justify-content-between align-items-center mb-4">
        <div className="col text-center">
          <h2 className="mb-0">Blog Posts</h2>
        </div>
        {/* Optional: Show "New Post" button */}
        <Link to="/create" className="btn btn-primary">+ New Post</Link>
      </div>

      {blogs.length === 0 ? (
        <p className="text-center text-muted">No blogs found.</p>
      ) : (
        <div className="row g-4">
          {blogs.map((blog) => (
            <div key={blog.id} className="col-sm-12 col-md-6 col-lg-4">
              <div className="card h-100 shadow border rounded">
                <div className="card-body d-flex flex-column">
                  <h5 className="card-title mb-2">
                    <Link to={`/blogs/${blog.id}`} className="text-primary text-decoration-none">
                      {blog.title}
                    </Link>
                  </h5>
                  <p className="card-text flex-grow-1 text-secondary">
                    {blog.content.slice(0, 150)}...
                  </p>
                  <div className="mt-3 text-end">
                    <Link to={`/blogs/${blog.id}`} className="btn btn-sm btn-outline-primary">
                      Read More
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default BlogList;
