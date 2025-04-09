import React from 'react'

const Footer = () => {
  return (
    <footer className="bg-indigo-900 text-white py-8">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div>
            <h3 className="text-xl font-bold mb-4">Vedic Astrology</h3>
            <p className="text-indigo-200">
              Bringing ancient wisdom to the modern world through authentic Vedic astrology.
            </p>
          </div>
          
          <div>
            <h4 className="font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-indigo-200 hover:text-white">Home</a></li>
              <li><a href="#" className="text-indigo-200 hover:text-white">About</a></li>
              <li><a href="#" className="text-indigo-200 hover:text-white">Services</a></li>
              <li><a href="#" className="text-indigo-200 hover:text-white">Contact</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Services</h4>
            <ul className="space-y-2">
              <li><a href="#" className="text-indigo-200 hover:text-white">Birth Chart</a></li>
              <li><a href="#" className="text-indigo-200 hover:text-white">Predictions</a></li>
              <li><a href="#" className="text-indigo-200 hover:text-white">Remedies</a></li>
              <li><a href="#" className="text-indigo-200 hover:text-white">Consultations</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold mb-4">Connect</h4>
            <div className="flex space-x-4">
              <a href="#" className="text-indigo-200 hover:text-white text-xl">
                <i className="fab fa-facebook"></i>
              </a>
              <a href="#" className="text-indigo-200 hover:text-white text-xl">
                <i className="fab fa-twitter"></i>
              </a>
              <a href="#" className="text-indigo-200 hover:text-white text-xl">
                <i className="fab fa-instagram"></i>
              </a>
              <a href="#" className="text-indigo-200 hover:text-white text-xl">
                <i className="fab fa-youtube"></i>
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-indigo-800 mt-8 pt-6 text-center text-indigo-300">
          <p>© {new Date().getFullYear()} Vedic Astrology Portal. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}

export default Footer
