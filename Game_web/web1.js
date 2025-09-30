// src/components/GameCard.jsx
import React from 'react';

const GameCard = ({ title, description, colorClass, icon }) => {
  return (
    <div 
      // Tailwind classes for the dark card background, shadow, padding, and hover effects
      className="p-6 m-4 w-72 rounded-xl shadow-2xl transition-all duration-300 transform hover:scale-[1.03] 
                 bg-[#161b22] border border-[#21262d] hover:border-cyan-500 cursor-pointer"
    >
      {/* Icon/Circle (the colorful button from the screenshot) */}
      <div className={`w-14 h-14 ${colorClass} rounded-full flex items-center justify-center mb-4 mx-auto shadow-lg`}>
        {icon}
      </div>
      
      <h3 className="text-xl font-semibold text-white text-center mb-1">{title}</h3>
      <p className="text-sm text-gray-400 text-center">{description}</p>
      
    </div>
  );
};

export default GameCard;