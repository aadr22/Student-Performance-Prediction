# Student Performance Predictor 📊
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0.1-brightgreen.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0.2-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning application that predicts students' mathematics performance based on various demographic and academic factors. Built with Python, Flask, and scikit-learn.

## 🎯 Features

- Predicts mathematics scores using ML model
- Web interface for easy data input
- RESTful API endpoints
- Detailed error handling
- Input validation
- Comprehensive logging

## 🛠️ Tech Stack

- Python (ML & Backend)
- Flask (Web Framework)
- scikit-learn (ML Library)
- Pandas (Data Processing)
- NumPy (Numerical Operations)
- HTML/CSS (Frontend)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student-performance-pred.git
cd student-performance-pred
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python application.py
```

Visit `http://localhost:5000` in your browser.

## 📁 Project Structure
```
├── .ebextensions/
├── artifacts/
├── catboost_info/
├── data/
├── logs/
├── mlproject.egg-info/
├── notebooks/
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── templates/
│   │   ├── home.html
│   │   └── index.html
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── venv/
├── .gitignore
├── application.py
├── README.md
├── requirements.txt
└── setup.py
```

## 🚀 Usage

### Web Interface

1. Start the application
2. Navigate to `http://localhost:5000`
3. Fill in student information:
   - Gender
   - Race/Ethnicity
   - Parental Education
   - Lunch Type
   - Test Preparation
   - Reading Score
   - Writing Score
4. Click "Predict" to get the mathematics score prediction

### API Endpoint

```http
POST /predictdata
Content-Type: application/json

{
    "gender": "male",
    "race_ethnicity": "group A",
    "parental_level_of_education": "bachelor's degree",
    "lunch": "standard",
    "test_preparation_course": "completed",
    "reading_score": 70,
    "writing_score": 75
}
```

## 🧪 Running Tests

```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Author

Aadil Rahman
- Email: aadil.rahman164@gmail.com
- GitHub: [@aadr22](https://github.com/aadr22)

## 📧 Contact

For questions and feedback, please contact: aadil.rahman164@gmail.com

---
⭐️ If you found this project helpful, please give it a star!
