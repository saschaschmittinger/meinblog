# Time: 02:14:14

#####

pip install trailwindcss
npm install flowbite

npm run watch:css

Tailwindcss+Flowbite

// tailwind.config.js
/** @type {import('tailwindcss').Config} \*/
module.exports = {
content: ["./templates/**/", "./node\*modules/flowbite/\*\*/\_.js"], // updated line here!
theme: {
extend: {},
},
plugins: [require("flowbite/plugin")],
};

 
 

 

