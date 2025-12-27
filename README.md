# Silent Customer Churn Predictor

## 🎯 Project Overview

**Silent Customer Churn Predictor** is an enterprise-ready system that predicts customer churn by detecting early behavioral disengagement patterns before customers explicitly leave. Unlike traditional churn systems that react to cancellations, this solution identifies pre-churn signals through behavioral analytics.

## 💡 The Business Problem

Most companies detect churn too late. Customers don't just cancel—they silently disengage:
- Login frequency drops
- Session durations decrease
- Feature exploration stops
- Response times increase
- Engagement patterns become erratic

This system provides **early warning signals** that enable proactive retention strategies.

## 🔬 What Makes This Different

**Traditional Churn Models:**
- Last purchase date
- Subscription end date
- Complaint history
- Usage drops (late signal)

**This Model:**
- Engagement momentum tracking
- Behavioral drift analysis
- Silence index measurement
- Response degradation detection
- Session decay rate monitoring
- Consistency score evaluation

## 📊 Feature Engineering

The system creates sophisticated behavioral signals:

1. **Engagement Momentum**: Acceleration/deceleration of usage patterns
2. **Behavioral Drift**: Reduction in feature diversity usage
3. **Silence Index**: Increasing inactivity gaps over time
4. **Response Degradation**: Growing delays in customer responses
5. **Session Decay Rate**: Declining session duration patterns
6. **Consistency Score**: Behavioral predictability vs. erratic patterns

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **ML**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas, numpy

## 📁 Project Structure

```
silent-churn-predictor/
├── app.py                      # Flask backend API
├── customer_churn_data.csv     # Simulated behavioral dataset
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html             # Web interface
├── static/
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
├── churn_model.pkl            # Trained model (generated)
└── scaler.pkl                 # Feature scaler (generated)
```

## 🚀 Installation & Setup

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Access the Web Interface

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 📱 Using the Application

### 1. Train Model (First Time)
- Click on the **Train Model** tab
- Click **Train Model** button
- Wait for training to complete (shows accuracy metrics)

### 2. Single Customer Prediction
- Go to **Single Prediction** tab
- Enter behavioral metrics:
  - **Engagement Momentum**: Negative values indicate declining activity
  - **Behavioral Drift**: High values mean fewer features used
  - **Silence Index**: High values indicate more inactivity
  - **Response Degradation**: High values mean slower responses
  - **Session Decay Rate**: High values indicate shorter sessions
  - **Consistency Score**: Low values indicate erratic behavior
- Click **Predict Churn Risk**
- View results:
  - Churn risk score (0-100%)
  - Risk category (Low/Medium/High)
  - Top contributing risk factors
  - Business recommendations

### 3. Batch Analysis
- Click **Batch Analysis** tab
- Click **Analyze Top 50 Customers**
- View risk assessment for multiple customers

## 📈 Model Details

- **Algorithm**: Random Forest Classifier
- **Why Random Forest?**
  - Interpretable (businesses need to understand predictions)
  - Handles non-linear patterns
  - Provides feature importance
  - Robust to overfitting
  - No need for feature scaling (but we scale for consistency)

- **Training Strategy**:
  - 80/20 train-test split
  - Stratified sampling (maintains churn ratio)
  - Class balancing (handles imbalanced data)
  - 100 estimators for stability

## 💼 Business Use Cases

Companies can use predictions to:
1. **Trigger proactive outreach** to high-risk customers
2. **Send personalized retention offers** before cancellation
3. **Redesign features** causing disengagement
4. **Improve onboarding** for new customers
5. **Optimize customer success workflows**

## 🎓 Internship/Project Value

This project demonstrates:
- ✅ **Business-first thinking** (solves real problems)
- ✅ **Feature engineering expertise** (not just raw ML)
- ✅ **Explainable AI** (businesses trust interpretable models)
- ✅ **Full-stack development** (backend + frontend)
- ✅ **Production-ready code** (clean, documented, scalable)

## 📊 Sample Predictions

**High Risk Customer:**
```
Engagement Momentum: -45% (declining)
Behavioral Drift: 65% (fewer features)
Silence Index: 15 (high inactivity)
→ Churn Risk: 82% | HIGH RISK
→ Recommendation: Urgent account manager assignment
```

**Low Risk Customer:**
```
Engagement Momentum: +12% (growing)
Behavioral Drift: 10% (stable)
Silence Index: 2 (minimal gaps)
→ Churn Risk: 18% | LOW RISK
→ Recommendation: Continue standard engagement
```

## 🔮 Future Enhancements

- Real-time prediction API integration
- Time-series forecasting for trend prediction
- Customer segmentation clustering
- A/B testing framework for retention strategies
- Email/SMS alert system for high-risk customers
- Dashboard with historical trend visualization

## 🛡️ Defense Against "This Already Exists"

**Response:**
"Traditional churn systems focus on explicit exit signals like cancellation or reduced transactions. This project focuses on early behavioral disengagement, which appears much earlier and allows intervention before revenue loss occurs. It's about detecting the silent signals, not the loud exits."

## 👨‍💻 One-Line Pitch

"I built a system that predicts silent customer churn by detecting early behavioral disengagement patterns before customers explicitly leave."

## 📝 Dataset Information

- **Size**: 1,000 customers
- **Features**: 18 (6 engineered behavioral signals)
- **Churn Rate**: ~30% (realistic business scenario)
- **Type**: Simulated but realistic behavioral patterns

## ⚡ Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Access web interface
# Open browser: http://127.0.0.1:5000
```

## 🎨 UI Features

- **Modern gradient design** with smooth animations
- **Responsive layout** (works on mobile/tablet/desktop)
- **Real-time predictions** with visual risk indicators
- **Color-coded risk categories** (Green/Yellow/Red)
- **Interactive forms** with helpful tooltips
- **Professional tables** for batch analysis

## 📞 API Endpoints

- `GET /` - Web interface
- `POST /train` - Train ML model
- `POST /predict` - Predict single customer churn
- `GET /analyze_dataset` - Batch analysis

## 🏆 Why This Project Stands Out

1. **Focus on business value** over ML complexity
2. **Explainable predictions** with feature importance
3. **Actionable recommendations** for retention teams
4. **Clean, production-ready code** structure
5. **Full-stack implementation** (not just notebooks)
6. **Scalable architecture** (easy to extend)

---

**Built with 💜 for detecting the whisper before the exit**
