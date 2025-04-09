import React from 'react'
import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <div className="py-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <div className="text-center mb-16">
        <h1 className="text-4xl md:text-5xl font-bold text-indigo-900 mb-4">
          Discover Your Cosmic Blueprint
        </h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          Unlock ancient Vedic wisdom with personalized astrological insights and guidance.
        </p>
      </div>

      <div className="grid md:grid-cols-3 gap-8 mb-16">
        <div className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition">
          <div className="text-indigo-600 text-3xl mb-4">
            <i className="fas fa-star"></i>
          </div>
          <h3 className="text-xl font-semibold mb-2">Birth Chart Analysis</h3>
          <p className="text-gray-600">
            Get detailed interpretation of your Vedic birth chart and planetary positions.
          </p>
          <Link to="/chart" className="mt-4 inline-block text-indigo-600 hover:text-indigo-800 font-medium">
            Get Started →
          </Link>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition">
          <div className="text-indigo-600 text-3xl mb-4">
            <i className="fas fa-file-alt"></i>
          </div>
          <h3 className="text-xl font-semibold mb-2">Detailed Reports</h3>
          <p className="text-gray-600">
            Download comprehensive PDF reports with personalized predictions and remedies.
          </p>
          <Link to="/reports" className="mt-4 inline-block text-indigo-600 hover:text-indigo-800 font-medium">
            Explore Reports →
          </Link>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition">
          <div className="text-indigo-600 text-3xl mb-4">
            <i className="fas fa-comments"></i>
          </div>
          <h3 className="text-xl font-semibold mb-2">AI Astrologer Chat</h3>
          <p className="text-gray-600">
            Get instant answers to your astrology questions from our AI expert.
          </p>
          <Link to="/chat" className="mt-4 inline-block text-indigo-600 hover:text-indigo-800 font-medium">
            Ask Questions →
          </Link>
        </div>
      </div>

      <div className="bg-indigo-50 rounded-xl p-8 text-center">
        <h2 className="text-2xl font-bold text-indigo-900 mb-4">Ready to Begin Your Journey?</h2>
        <p className="text-gray-600 mb-6 max-w-2xl mx-auto">
          Create your free account to access all features and save your astrological data.
        </p>
        <button className="bg-indigo-700 hover:bg-indigo-800 text-white px-6 py-3 rounded-lg font-medium transition">
          Sign Up Now
        </button>
      </div>
    </div>
  )
}

export default Home
