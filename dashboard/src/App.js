import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);  // State to store list of options
  const [selectedOption, setSelectedOption] = useState("");  // State for selected option

  useEffect(() => {
    // Fetch data from Flask API on component mount
    axios.get('http://127.0.0.1:5000/api/databaselist')  // Update with your actual API endpoint
      .then(response => {
        setData(response.data);  // Assuming response.data is an array of options
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const handleChange = (event) => {
    setSelectedOption(event.target.value);
  };

  return (
    <div className="App">
      <h1>React and Flask</h1>
      <select 
        name="dblist" 
        id="optionSelector" 
        value={selectedOption}
        onChange={handleChange}
      >
        <option value="" disabled>Select an option</option>
        {data.map((option, index) => (
          <option key={index} value={option}>{option}</option>
        ))}
      </select>
      
    </div>
  );
}
export default App;
