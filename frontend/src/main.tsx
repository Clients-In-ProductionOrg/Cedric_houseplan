import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./index.css";

// Debug: Check environment variables
setTimeout(() => {
  console.log('API URL:', import.meta.env.VITE_API_URL);
  console.log('Frontend URL:', import.meta.env.VITE_FRONTEND_URL);
}, 1000);

createRoot(document.getElementById("root")!).render(<App />);
