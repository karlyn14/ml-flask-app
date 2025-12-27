"""
Silent Customer Churn Predictor - Backend
Author: Churn Analytics System
Description: Flask API for predicting silent customer churn based on behavioral disengagement
"""

from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

app = Flask(__name__)

class ChurnPredictor:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = [
            'engagement_momentum', 'behavioral_drift', 'silence_index',
            'response_degradation', 'session_decay_rate', 'consistency_score'
        ]

    def train_model(self, data_path='customer_churn_data.csv'):
        """Train the churn prediction model"""
        df = pd.read_csv(data_path)

        X = df[self.feature_names]
        y = df['churn']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            random_state=42,
            class_weight='balanced'
        )

        self.model.fit(X_train_scaled, y_train)

        train_score = self.model.score(X_train_scaled, y_train)
        test_score = self.model.score(X_test_scaled, y_test)

        joblib.dump(self.model, 'churn_model.pkl')
        joblib.dump(self.scaler, 'scaler.pkl')

        return {
            'train_accuracy': round(train_score * 100, 2),
            'test_accuracy': round(test_score * 100, 2),
            'features': self.feature_names
        }

    def load_model(self):
        """Load pre-trained model"""
        if os.path.exists('churn_model.pkl') and os.path.exists('scaler.pkl'):
            self.model = joblib.load('churn_model.pkl')
            self.scaler = joblib.load('scaler.pkl')
            return True
        return False

    def predict_churn(self, customer_data):
        """Predict churn probability and get risk factors"""
        features_df = pd.DataFrame([customer_data])[self.feature_names]
        features_scaled = self.scaler.transform(features_df)

        churn_probability = self.model.predict_proba(features_scaled)[0][1]
        prediction = int(self.model.predict(features_scaled)[0])

        feature_importance = self.model.feature_importances_

        risk_factors = []
        for i, (feature, value) in enumerate(customer_data.items()):
            if feature in self.feature_names:
                importance = feature_importance[self.feature_names.index(feature)]

                risk_indicators = {
                    'engagement_momentum': value < -20,
                    'behavioral_drift': value > 40,
                    'silence_index': value > 8,
                    'response_degradation': value > 100,
                    'session_decay_rate': value > 30,
                    'consistency_score': value < 50
                }

                if risk_indicators.get(feature, False):
                    risk_factors.append({
                        'feature': feature.replace('_', ' ').title(),
                        'value': round(value, 2),
                        'importance': round(importance * 100, 2)
                    })

        risk_factors.sort(key=lambda x: x['importance'], reverse=True)

        if churn_probability < 0.3:
            risk_category = 'Low'
            risk_color = '#10b981'
        elif churn_probability < 0.6:
            risk_category = 'Medium'
            risk_color = '#f59e0b'
        else:
            risk_category = 'High'
            risk_color = '#ef4444'

        return {
            'churn_probability': round(churn_probability * 100, 2),
            'prediction': prediction,
            'risk_category': risk_category,
            'risk_color': risk_color,
            'risk_factors': risk_factors[:3],
            'recommendation': self._get_recommendation(risk_category, risk_factors)
        }

    def _get_recommendation(self, risk_category, risk_factors):
        """Generate business recommendations"""
        if risk_category == 'Low':
            return "Customer is engaged. Continue standard engagement practices."
        elif risk_category == 'Medium':
            actions = []
            for factor in risk_factors[:2]:
                if 'Engagement Momentum' in factor['feature']:
                    actions.append("Send personalized re-engagement campaign")
                elif 'Behavioral Drift' in factor['feature']:
                    actions.append("Trigger feature discovery onboarding")
                elif 'Silence Index' in factor['feature']:
                    actions.append("Schedule proactive check-in call")
            return " | ".join(actions) if actions else "Monitor engagement patterns closely"
        else:
            return "URGENT: Assign dedicated account manager | Offer retention incentive | Immediate human outreach required"

predictor = ChurnPredictor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    """Train the model endpoint"""
    try:
        result = predictor.train_model()
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    """Predict churn for a customer"""
    try:
        if not predictor.model:
            predictor.load_model()

        customer_data = request.json

        result = predictor.predict_churn(customer_data)
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/analyze_dataset', methods=['GET'])
def analyze_dataset():
    """Analyze the full dataset"""
    try:
        if not predictor.model:
            predictor.load_model()

        df = pd.read_csv('customer_churn_data.csv')

        predictions = []
        for _, row in df.head(50).iterrows():
            customer_data = row[predictor.feature_names].to_dict()
            result = predictor.predict_churn(customer_data)
            predictions.append({
                'customer_id': row['customer_id'],
                'churn_probability': result['churn_probability'],
                'risk_category': result['risk_category'],
                'actual_churn': int(row['churn'])
            })

        return jsonify({'success': True, 'data': predictions})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    if not predictor.load_model():
        print("Training new model...")
        predictor.train_model()

    app.run(host="0.0.0.0",port=5000,debug=True)
