import React from 'react'
import ReactDOM from 'react-dom/client'
import ChatbotContainer from './component/ChatbotContainer.tsx'
import "./types.d.ts"
import "./index.css"

const chatbotContainer = document.createElement("div");
document.body.appendChild(chatbotContainer);
ReactDOM.createRoot(chatbotContainer).render(
  <React.StrictMode>
    <ChatbotContainer/>
  </React.StrictMode>,
)
