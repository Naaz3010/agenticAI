# 🌍 Agentic AI-Based Travel Planning Assistant Using LangChain

## 🚀 Live Demo

🌐 **Streamlit Application**

https://agentic-ai-based-travel-planning-assistant-using-langchain.streamlit.app/

---

# 📌 Project Overview

The **Agentic AI Travel Planning Assistant** is an intelligent travel recommendation platform built using **LangChain, Streamlit, Plotly, and Python**.

The system simulates an AI travel agent that analyzes user preferences and generates a personalized travel plan by combining:

* ✈️ Flight Recommendations
* 🏨 Hotel Selection
* 🌦️ Weather Forecasting
* 🗺️ Day-wise Itinerary Planning
* 💰 Budget Estimation
* 📊 Travel Analytics Dashboard
* 🤖 AI-Powered Travel Insights

The application follows an **Agentic AI architecture**, where multiple tools collaborate to create a complete travel plan.

---

# ✨ Key Features

| Feature                     | Description                                |
| --------------------------- | ------------------------------------------ |
| ✈️ Flight Recommendation    | Selects the best available flight option   |
| 🏨 Hotel Recommendation     | Suggests hotels based on budget and rating |
| 🌦️ Weather Forecast        | Displays weather conditions for the trip   |
| 🗺️ Itinerary Generation    | Creates day-wise travel activities         |
| 💰 Budget Optimization      | Calculates total travel expenses           |
| 📊 Analytics Dashboard      | Interactive visualizations using Plotly    |
| 🤖 AI Recommendation Engine | Generates intelligent travel insights      |
| 🌐 Streamlit Deployment     | Live web application                       |

---

# 🖼️ Application Screenshots

## 1️⃣ Home Dashboard

The user enters travel preferences such as departure city, destination, trip duration, and hotel budget.

![Home Dashboard](images/dashboard-home.png)

---

## 2️⃣ Trip Overview & Travel Intelligence Score

Displays key travel metrics including:

* Trip Duration
* Flight Cost
* Hotel Cost
* Total Budget
* Cost Per Day
* AI Travel Score

![Trip Overview](images/trip-overview.png)

---

## 3️⃣ Flight & Hotel Recommendation Engine

The AI selects a suitable flight and hotel based on the user's preferences.

### Flight Details

| Metric   | Value     |
| -------- | --------- |
| Airline  | Air India |
| Duration | 2 Hours   |
| Price    | ₹5356     |

### Hotel Details

| Metric      | Value                 |
| ----------- | --------------------- |
| Rating      | ⭐⭐⭐⭐⭐                 |
| Amenities   | WiFi, Breakfast, Pool |
| Price/Night | ₹1232                 |

![Recommendations](images/recommendations.png)

---

## 4️⃣ Interactive Travel Analytics Dashboard

The dashboard provides visual insights using Plotly.

### Weather Forecast Trend

* Maximum Temperature
* Minimum Temperature
* Temperature Analysis

### Budget Allocation

* Flight Cost
* Hotel Cost
* Local Expenses

![Travel Analytics](images/travel-analytics.png)

---

## 5️⃣ Day-wise Itinerary & AI Recommendation

The application generates a structured itinerary and provides AI-generated travel suggestions.

![Itinerary](images/itinerary-ai.png)

---

# 🏗️ System Architecture

```text
User Input
    │
    ▼
LangChain Travel Agent
    │
 ┌──┼───────────┬──────────┬──────────┐
 ▼  ▼           ▼          ▼          ▼

Flight Tool   Hotel Tool  Weather Tool
Place Tool    Budget Tool

    │
    ▼

Final Travel Plan

    │
    ▼

Streamlit Dashboard
```

---

# 📂 Project Structure

```text
Agentic-AI-Based-Travel-Planning-Assistant-Using-LangChain
│
├── agent/
│   ├── __init__.py
│   └── travel_agent.py
│
├── tools/
│   ├── budget_tool.py
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── weather_tool.py
│   ├── place_tool.py
│   └── data_loader.py
│
├── output/
│   └── final_output.py
│
├── Data_Sources/
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
│
├── images/
│   ├── dashboard-home.png
│   ├── trip-overview.png
│   ├── travel-analytics.png
│   ├── recommendations.png
│   └── itinerary-ai.png
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technology Stack

| Category             | Technologies              |
| -------------------- | ------------------------- |
| Programming Language | Python                    |
| Agent Framework      | LangChain                 |
| Frontend             | Streamlit                 |
| Data Processing      | Pandas                    |
| Visualization        | Plotly                    |
| Storage              | JSON                      |
| Version Control      | Git & GitHub              |
| Deployment           | Streamlit Community Cloud |

---

# 📊 Dashboard Metrics

The application tracks:

| KPI                       | Description                     |
| ------------------------- | ------------------------------- |
| Trip Duration             | Total days of travel            |
| Flight Cost               | Airfare expenses                |
| Hotel Cost                | Accommodation expenses          |
| Local Expenses            | Food & Travel                   |
| Cost Per Day              | Daily trip expenditure          |
| Travel Intelligence Score | AI-generated trip quality score |

---

# 🎯 Business Impact

This project demonstrates how Agentic AI can be used to:

* Automate travel planning
* Reduce manual itinerary creation
* Optimize travel budgets
* Provide personalized recommendations
* Deliver insights through analytics dashboards

---

# 🔮 Future Enhancements

* Real-Time Flight API Integration
* OpenWeather API Integration
* Google Places API Integration
* Hotel Booking APIs
* Dynamic Route Optimization
* Multi-City Travel Planning
* AI Chat-Based Travel Assistant
* Personalized Recommendation Engine

---

# 👩‍💻 Author

### Tonuja Ramesh

Data Science Undergraduate | AI & Analytics Enthusiast

# 🔗 Connect With Me

* GitHub: https://github.com/tonujaramesh
* LinkedIn: https://www.linkedin.com/in/tonuja-ramesh-s-38871b299

---

## ⭐ If you found this project useful, please consider giving it a star!
