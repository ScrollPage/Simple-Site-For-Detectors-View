import { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

const apiUrl = "/api/data/";
const dbHost = "http://localhost:8000";

const instance = axios.create({
  baseURL: dbHost,
  headers: {
    'Content-Type': 'application/json',
  }
})

function App() {

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchUrl = async () => {
    await instance.get(apiUrl)
      .then(({ data }) => {
        setData(data);
      })
      .catch(e => {
        setError(e);
      })
    setLoading(false);
  }

  useEffect(() => {
    fetchUrl();
  }, [])

  if (error) {
    return <p>Ошибка</p>;
  }

  if (loading) {
    return <p>Загрузка...</p>;
  }

  return (
    <div className="App">
      {JSON.stringify(data, null, 2)}
    </div>
  );
}

export default App;
