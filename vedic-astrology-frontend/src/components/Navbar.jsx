import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="bg-indigo-900 text-white shadow-lg">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold flex items-center">
          <i className="fas fa-moon mr-2"></i>
          Vedic Astrology
        </Link>
        
        <div className="hidden md:flex space-x-6">
          <Link to="/" className="hover:text-indigo-200 transition">Home</Link>
          <Link to="/chart" className="hover:text-indigo-200 transition">Chart</Link>
          <Link to="/reports" className="hover:text-indigo-200 transition">Reports</Link>
          <Link to="/chat" className="hover:text-indigo-200 transition">Chat</Link>
        </div>

        <div className="flex items-center space-x-4">
          <button className="bg-indigo-700 hover:bg-indigo-600 px-4 py-2 rounded-md transition">
            Sign In
          </button>
          <button className="bg-white text-indigo-900 hover:bg-gray-100 px-4 py-2 rounded-md transition">
            Sign Up
          </button>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
