import { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    const res = await axios.post("http://localhost:8000/ask", {
      query: query,
    });

    setResponse(res.data.response);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Multimodal Agentic RAG</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={handleSubmit}>Ask</button>

      <p>{response}</p>
    </div>
  );
}

export default App;