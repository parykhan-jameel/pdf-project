import React, { useState } from "react";
import axios from "axios";

const SearchForm = () => {
  const [query, setQuery] = useState("");
  const [title, setTitle] = useState(""); 
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query) {
      alert("Please enter a search term");
      return;
    }
    setLoading(true);

    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/search/?query=${encodeURIComponent(query)}&title=${encodeURIComponent(title)}`
      );
      
      setResults(response.data.results); 
    } catch (error) {
      console.error("Error fetching search results:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-10 p-4 border rounded shadow">
      <h2 className="text-xl font-semibold mb-4">Search PDF</h2>
      <input
        type="text"
        placeholder="Enter search term"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="mb-2 p-2 border rounded w-full"
      />
      <input
        type="text"
        placeholder="Enter title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="mb-2 p-2 border rounded w-full"
      />
      <button
        onClick={handleSearch}
        className="w-full bg-green-500 text-white py-2 rounded hover:bg-green-600"
      >
        Search
      </button>
      {loading && <p className="mt-4">Loading...</p>}
      {results.length > 0 && (
        <ul className="mt-4">
          {results.map((item, index) => (
            <li key={index} className="mb-2 p-2 border-b">
              <h3 className="font-semibold">{item.title}</h3>
              <p>File URL: <a href={item.file_url} className="text-blue-500" target="_blank" rel="noopener noreferrer">{item.file_url}</a></p>
              {item.highlights.length > 0 && (
                <div>
                  <h4 className="font-semibold">Results:</h4>
                  <ul className="list-decimal pl-4">
                    {item.highlights.map((highlight, i) => (
                      <li key={i} dangerouslySetInnerHTML={{ __html: highlight }} />
                    ))}
                  </ul>
                </div>
              )}
            </li>
          ))}
        </ul>
      )}
      {results.length === 0 && !loading && <p className="mt-4">No results found</p>}
    </div>
  );
};

export default SearchForm;
