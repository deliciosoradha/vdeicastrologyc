import React, { useState, useRef, useEffect } from 'react'

const Chat = () => {
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: "Hello! I'm your Vedic astrology assistant. How can I help you today?",
      sender: 'bot'
    }
  ])
  const [inputValue, setInputValue] = useState('')
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSubmit = (e) => {
    e.preventDefault()
    if (!inputValue.trim()) return

    // Add user message
    const newUserMessage = {
      id: messages.length + 1,
      text: inputValue,
      sender: 'user'
    }
    setMessages(prev => [...prev, newUserMessage])
    setInputValue('')

    // Simulate bot response
    setTimeout(() => {
      const newBotMessage = {
        id: messages.length + 2,
        text: "I'm analyzing your question based on Vedic principles...",
        sender: 'bot'
      }
      setMessages(prev => [...prev, newBotMessage])
    }, 1000)
  }

  return (
    <div className="py-12 px-4 sm:px-6 lg:px-8 max-w-3xl mx-auto">
      <div className="text-center mb-8">
        <h1 className="text-3xl md:text-4xl font-bold text-indigo-900 mb-2">
          AI Astrologer Chat
        </h1>
        <p className="text-gray-600">
          Ask any questions about your birth chart or Vedic astrology in general.
        </p>
      </div>

      <div className="bg-white rounded-xl shadow-md overflow-hidden">
        <div className="h-96 p-4 overflow-y-auto">
          <div className="space-y-4">
            {messages.map(message => (
              <div 
                key={message.id} 
                className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div 
                  className={`max-w-xs md:max-w-md rounded-lg px-4 py-2 ${message.sender === 'user' 
                    ? 'bg-indigo-600 text-white' 
                    : 'bg-gray-100 text-gray-800'}`}
                >
                  {message.text}
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
        </div>

        <form onSubmit={handleSubmit} className="border-t border-gray-200 p-4">
          <div className="flex">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask your astrology question..."
              className="flex-grow px-4 py-2 border border-gray-300 rounded-l-md focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
            />
            <button
              type="submit"
              className="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-r-md transition"
            >
              <i className="fas fa-paper-plane"></i>
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Chat
