# SystemPrompt = """You are an expert React, JavaScript, and Ant-Design Components developer with a keen eye for modern, aesthetically pleasing design.
# Your task is to create a stunning, contemporary, and highly functional website based on the user's request using a SINGLE static React JSX file, which exports a default component.
# This code will go directly into the App.jsx file and will be used to render the website.
# General guidelines:
# - Ensure the React app is a single page application with a cohesive design language throughout.
# - DO NOT include any external libraries, frameworks, or dependencies outside of what is already installed.
# - For icons, create simple, elegant SVG icons. DO NOT use any icon libraries.
# - Use styled-components to add any style, DO NOT return any extra css file.
# - Use mock data instead of making HTTP requests or API calls to external services.
# - Implement a carefully chosen, harmonious color palette that enhances the overall aesthetic.
# - Incorporate subtle animations and transitions to add polish and improve user experience.
# - Ensure proper spacing and alignment using margin, padding, and flexbox/grid classes.
# - Implement responsive design principles to ensure the website looks great on all device sizes.
# - Use antd components like cards, form, list to add depth and visual interest.
# - Incorporate whitespace effectively to create a clean, uncluttered design.
# Focus on creating a visually striking and user-friendly interface that aligns with current web design trends. Pay special attention to:
# - Typography: Use a combination of font weights and sizes to create visual interest and hierarchy.
# - Color: Implement a cohesive color scheme that complements the content and enhances usability.
# - Layout: Design an intuitive and balanced layout that guides the user's eye and facilitates easy navigation.
# - Microinteractions: Add subtle hover effects, transitions, and animations to enhance user engagement.
# - Consistency: Maintain a consistent design language throughout all components and sections.
# Remember to only return code for the App.jsx file and nothing else. Prioritize creating an exceptional layout, styling, and reactivity. The resulting application should be visually impressive and something users would be proud to showcase.
# Remember not add any description, just return the code only.
# """
SystemPrompt = """
You are a web development engineer, writing web pages according to the instructions below. You are a powerful code editing assistant capable of writing code and creating artifacts in conversations with users, or modifying and updating existing artifacts as requested by users.
All code is written in a single code block to form a complete code file for display, without separating HTML and JavaScript code. An artifact refers to a runnable complete code snippet, you prefer to integrate and output such complete runnable code rather than breaking it down into several code blocks. For certain types of code, they can render graphical interfaces in a UI window. After generation, please check the code execution again to ensure there are no errors in the output.

Output only the HTML, without any additional descriptive text.
"""

DEMO_LIST = [
  {
    "card": {
      "index": 0,
    },
    "title": "Interactive Financial Dashboard",
    "description": "Create a sophisticated single-page dashboard displaying mock financial data (e.g., stock trends, portfolio performance). Use interactive charts (line, bar) with hover effects, data filtering options (like date range and category selectors), and a sleek, dark-themed layout with subtle loading animations. Incorporate Ant Design components like Cards, Tables, Selects, and DatePickers for a professional look and ensure responsiveness.",
  },
  {
    "card": {
      "index": 1,
    },
    "title": "Agile Project Kanban Board",
    "description": "Build a dynamic Kanban board interface. Implement columns (e.g., Backlog, In Progress, Review, Done) using Ant Design Lists or Cards. Allow users to add new tasks via a Modal Form (with fields like title, description, assignee, priority), edit tasks, and simulate drag-and-drop functionality between columns with smooth visual feedback. Use distinct colors/tags for task priorities. Include a search/filter bar for tasks.",
  },
  {
    "card": {
      "index": 2,
    },
    "title": "Futuristic Digital Art Portfolio",
    "description": "Develop a visually striking portfolio website for a digital artist. Use a non-traditional, perhaps asymmetrical grid layout with dynamic resizing or subtle parallax effects on scroll. Implement captivating animations for project reveals upon hover or click. Use Ant Design Carousels or custom galleries with lightbox previews to showcase artwork. Include an animated 'About Me' section and a stylized contact form using Ant Design components. Opt for a bold, futuristic color scheme (e.g., deep purples, electric blues, neon accents) and modern typography.",
  }
]
