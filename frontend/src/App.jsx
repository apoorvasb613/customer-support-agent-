import { useState } from "react"

export default function App() {

  const [query, setQuery] = useState("")
  const [result, setResult] = useState("")
  const [loading, setLoading] = useState(false)

  const sendQuery = async () => {

    if (!query) return

    setLoading(true)
    setResult("")

    try {

      const res = await fetch(
        `http://127.0.0.1:8000/test/CN1?query=${encodeURIComponent(query)}`
      )

      const data = await res.json()

      setResult(JSON.stringify(data, null, 2))

    } catch (err) {

      setResult("Error calling backend")

    }

    setLoading(false)
  }

  return (
    <div style={{ padding: 20 }}>

      <h2>Customer Support Bot</h2>

      <input
        style={{
          width: "400px",
          padding: "10px",
          marginBottom: "10px"
        }}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask customer question..."
      />

      <br />

      <button onClick={sendQuery}>
        {loading ? "Running..." : "Send"}
      </button>

      <pre style={{ marginTop: 20 }}>
        {result}
      </pre>

    </div>
  )
}
