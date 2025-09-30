// src/App.jsx
import React from 'react';
import GameCard from './components/GameCard';

function App() {
  // Data for each of the game cards
  const games = [
    { 
      title: "Tic Tac Toe", 
      description: "Classic 3x3 grid strategy game", 
      // The colorful gradients for each card icon
      colorClass: "bg-gradient-to-tr from-cyan-400 to-blue-600",
      icon: <span className="text-2xl text-white">X/O</span> 
    },
    { 
      title: "Connect Four", 
      description: "Drop tokens to connect four in a row", 
      colorClass: "bg-gradient-to-tr from-red-400 to-pink-600",
      icon: <span className="text-2xl text-white">4</span> 
    },
    { 
      title: "Battleship", 
      description: "Naval warfare strategy game", 
      colorClass: "bg-gradient-to-tr from-teal-400 to-green-600",
      icon: <span className="text-2xl text-white">🚢</span> 
    },
  ];

  return (
    // Main container setup for the dark background and centering the content
    <div className="min-h-screen flex flex-col items-center justify-center p-8">
      
      {/* Title Area (Game Zone) */}
      <header className="text-center mb-16">
        <h1 className="text-6xl md:text-7xl font-extrabold mb-2 
                       /* Gradient text effect to match the screenshot */
                       bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-500">
          Game Zone
        </h1>
        <p className="text-xl text-gray-400 tracking-wider">
          Choose your battle, pick your challenge
        </p>
      </header>

      {/* Game Cards Layout */}
      <div className="flex flex-wrap justify-center max-w-5xl">
        {/* Map over the game data to render a GameCard component for each game */}
        {games.map((game) => (
          <GameCard 
            key={game.title}
            title={game.title}
            description={game.description}
            colorClass={game.colorClass}
            icon={game.icon}
          />
        ))}
      </div>
      
    </div>
  );
}

export default App;