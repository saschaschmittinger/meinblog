# Time: 00:41:16

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

Models:

class BlogContentModel(models.Model):
pass

class Meta:
verbose_name_plural = 'Markdown content'

     def __str__(self):
     return self.title
