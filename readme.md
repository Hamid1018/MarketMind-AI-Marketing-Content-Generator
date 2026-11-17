# MarketMind – AI Marketing Content Generator

An AI-powered, full-stack web application that helps users create marketing campaigns, platform-specific content, and AI-generated visuals from a simple product description.

## 📌 Project Overview

MarketMind is designed to make digital marketing content creation easier and faster. Users provide basic information about their product, target audience, marketing platform, and campaign objective. The system uses Generative AI to create a marketing strategy, generate platform-specific content, and produce image prompts and visual creatives.

The project combines a React frontend with a FastAPI backend and Generative AI services.

## ✨ Key Features

### 1. Campaign Brief
- Enter product name and description.
- Define the target audience.
- Select a marketing platform.
- Choose a campaign objective.
- Select content tone and language.

### 2. AI Marketing Strategy
- Generate campaign ideas.
- Identify the target audience's interests.
- Highlight product benefits and selling points.
- Suggest calls to action (CTAs).
- Recommend suitable content types.

### 3. Platform-Specific Content Generation
Generate marketing content for different platforms:

- Instagram
- Instagram Stories
- Facebook
- LinkedIn
- YouTube

The generated content includes platform-specific formats, captions, headlines, hooks, CTAs, and hashtags where appropriate.

### 4. AI Image Generation
- Generate image prompts based on campaign information.
- Create platform-specific visual concepts.
- Generate marketing images.
- Preview and select generated visuals.
- Regenerate images when needed.

### 5. AI Marketing Campaign Agent
The campaign agent coordinates the complete content-generation workflow:

1. Understand the campaign requirements.
2. Generate a marketing strategy.
3. Create a campaign plan.
4. Generate platform-specific content.
5. Create image prompts.
6. Generate marketing visuals.

### 6. Campaign Management
- Save campaign information.
- View previous campaigns.
- Regenerate individual campaign outputs.
- Review generated content before using it.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| React.js | Frontend user interface |
| Vite | Frontend development and build tool |
| Python | Backend programming |
| FastAPI | REST API development |
| SQLite | Database |
| SQLAlchemy | Database management |
| Groq API | Large Language Model (LLM) integration |
| Pollinations AI | AI image generation |
| HTML, CSS, JavaScript | Frontend development |

## 🏗️ Project Architecture

The application follows a frontend-backend architecture.

```text
MarketMind/
│
├── Backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── database/
│   │
│   ├── requirements.txt
│   ├── .env.example
│   └── ...
│
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── .env.example
│   └── ...
│
├── .gitignore
└── README.md
```

*Note: The folder structure above is an example. Adjust it to match your actual project files.*

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or later
- Node.js and npm
- Git

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd MarketMind
```

### 2. Backend Setup

Open the backend directory:

```bash
cd Backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file inside the Backend folder.

Add your API configuration:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_model_name
POLLINATIONS_API_KEY=your_pollinations_api_key
DATABASE_URL=sqlite:///./marketing.db
FRONTEND_ORIGIN=http://localhost:5173
```

Replace the placeholder values with your actual configuration. Never upload your real API keys to GitHub.

### 4. Run the Backend

From the Backend directory, run:

```bash
python -m uvicorn app.main:app --reload --port 8000
```

Backend API:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Frontend Setup

Open another terminal and navigate to the Frontend directory:

```bash
cd Frontend
```

Install dependencies:

```bash
npm install
```

If your frontend uses an API base URL, create a `.env` file:

```env
VITE_API_BASE_URL=http://localhost:8000
```

Run the frontend:

```bash
npm run dev
```

Open the local URL shown in your terminal, usually:

```text
http://localhost:5173
```

## 🔄 Application Workflow

```text
User Enters Campaign Details
           |
           v
    AI Marketing Strategy
           |
           v
     Campaign Planning
           |
           v
 Platform-Specific Content
           |
           v
      Image Prompts
           |
           v
     AI Image Generation
           |
           v
   Review and Select Content
           |
           v
       Save Campaign
```

## 🧪 Testing and Evaluation

The application can be evaluated using different types of products and industries, such as:

- E-commerce products
- Educational services
- Restaurants
- Software products
- Clothing brands
- Real estate

Important evaluation points:

- Relevance of generated content.
- Quality of marketing strategies.
- Correct content format for each platform.
- Image relevance to the product.
- Error handling and API reliability.
- Overall user experience.

## 🔐 Security

- Store API keys in environment variables.
- Keep `.env` files out of GitHub.
- Validate user inputs.
- Handle API errors safely.
- Avoid exposing private configuration information.

## 🚀 Future Improvements

- User authentication and account management.
- More social media platform support.
- Advanced campaign analytics.
- Improved content quality evaluation.
- Export campaigns into downloadable formats.
- Social media scheduling and publishing integration.
- Better campaign performance recommendations.

## 🎓 Internship Project

This project was developed as part of the **Big Brains Generative AI Internship**.

Through this project, I gained practical experience in:

- Generative AI and Large Language Models.
- Prompt engineering.
- LLM API integration.
- Full-stack web development.
- AI agents and workflow automation.
- AI image generation.
- Backend API development.
- Testing and evaluating AI-generated content.

## 👨‍💻 Author

Developed as a Generative AI internship project.

**Project Name:** MarketMind – AI Marketing Content Generator

**Technologies:** React.js, FastAPI, Python, SQLite, Groq API, and Pollinations AI.