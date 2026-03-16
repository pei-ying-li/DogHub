
import React, { useEffect, useState } from "react";

function App() {

  const [dogs, setDogs] = useState([]);
  const [parks, setParks] = useState([]);

  useEffect(() => {

    fetch("http://127.0.0.1:8000/api/dogs/")
      .then(r => r.json())
      .then(setDogs);

    fetch("http://127.0.0.1:8000/api/parks/")
      .then(r => r.json())
      .then(setParks);

  }, []);

  return (
    <div style={{padding:40}}>

      <h1>DogHub 🐶</h1>

      <h2>Dogs</h2>
      {dogs.map(d => (
        <div key={d.id}>{d.name} ({d.breed})</div>
      ))}

      <h2>Parks</h2>
      {parks.map(p => (
        <div key={p.id}>{p.name}</div>
      ))}

    </div>
  );
}

export default App;
