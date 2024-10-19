import { useFetch } from './useFetch'
import {Comentario} from './Comentarios'
import './App.css'

function App() {
  const { data, loading, error } = useFetch("https://jsonplaceholder.typicode.com/comments")
  
  return (
    <div className="App">
      <h1>Mi primer Fetch</h1>
      <div className="card">
        <div>
          {error && <p>Error: {error}</p>}
          {loading && <p>Loading...</p>}
          <div className='grid'>
            {data?.map((post) => (
              <div className='comentario'
                key={post.id}>
                <h2 className='titulo'>{post.name}</h2>
                <p className='email'>{post.email}</p>
                <p className='mensaje'>{post.body}</p>
              </div>
            ))}
          </div>
        </div>
            
          
      </div>
    </div>
  )
} 
export default App