function showTab(tabName) {
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));

    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));

    document.getElementById(`${tabName}-tab`).classList.add('active');
    event.target.classList.add('active');
}

document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        engagement_momentum: parseFloat(document.getElementById('engagement_momentum').value),
        behavioral_drift: parseFloat(document.getElementById('behavioral_drift').value),
        silence_index: parseFloat(document.getElementById('silence_index').value),
        response_degradation: parseFloat(document.getElementById('response_degradation').value),
        session_decay_rate: parseFloat(document.getElementById('session_decay_rate').value),
        consistency_score: parseFloat(document.getElementById('consistency_score').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (result.success) {
            displayResults(result.data);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error connecting to server: ' + error);
    }
});

function displayResults(data) {
    document.getElementById('result-section').style.display = 'block';

    document.getElementById('churn-score').textContent = data.churn_probability;

    const badge = document.getElementById('risk-badge');
    badge.textContent = data.risk_category + ' Risk';
    badge.style.backgroundColor = data.risk_color;

    const factorsList = document.getElementById('risk-factors-list');
    factorsList.innerHTML = '';

    data.risk_factors.forEach(factor => {
        const factorDiv = document.createElement('div');
        factorDiv.className = 'risk-factor-item';
        factorDiv.innerHTML = `
            <div class="factor-name">${factor.feature}</div>
            <div class="factor-details">
                <span>Value: ${factor.value}</span>
                <span>Importance: ${factor.importance}%</span>
            </div>
        `;
        factorsList.appendChild(factorDiv);
    });

    document.getElementById('recommendation-text').textContent = data.recommendation;

    document.getElementById('result-section').scrollIntoView({ behavior: 'smooth' });
}

async function trainModel() {
    const button = event.target;
    button.disabled = true;
    button.textContent = 'Training...';

    try {
        const response = await fetch('/train', {
            method: 'POST'
        });

        const result = await response.json();

        if (result.success) {
            document.getElementById('train-results').innerHTML = `
                <div class="success-message">
                    <h3>Model Trained Successfully!</h3>
                    <p><strong>Training Accuracy:</strong> ${result.data.train_accuracy}%</p>
                    <p><strong>Test Accuracy:</strong> ${result.data.test_accuracy}%</p>
                    <p><strong>Features Used:</strong> ${result.data.features.join(', ')}</p>
                </div>
            `;
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error: ' + error);
    } finally {
        button.disabled = false;
        button.textContent = 'Train Model';
    }
}

async function analyzeBatch() {
    const button = event.target;
    button.disabled = true;
    button.textContent = 'Analyzing...';

    try {
        const response = await fetch('/analyze_dataset');
        const result = await response.json();

        if (result.success) {
            let tableHTML = `
                <table class="batch-table">
                    <thead>
                        <tr>
                            <th>Customer ID</th>
                            <th>Churn Risk %</th>
                            <th>Risk Category</th>
                            <th>Actual Churn</th>
                        </tr>
                    </thead>
                    <tbody>
            `;

            result.data.forEach(customer => {
                const actualChurn = customer.actual_churn === 1 ? 'Yes' : 'No';
                tableHTML += `
                    <tr>
                        <td>${customer.customer_id}</td>
                        <td>${customer.churn_probability}%</td>
                        <td><span style="color: ${getRiskColor(customer.risk_category)}">${customer.risk_category}</span></td>
                        <td>${actualChurn}</td>
                    </tr>
                `;
            });

            tableHTML += `
                    </tbody>
                </table>
            `;

            document.getElementById('batch-results').innerHTML = tableHTML;
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        alert('Error: ' + error);
    } finally {
        button.disabled = false;
        button.textContent = 'Analyze Top 50 Customers';
    }
}

function getRiskColor(category) {
    const colors = {
        'Low': '#10b981',
        'Medium': '#f59e0b',
        'High': '#ef4444'
    };
    return colors[category] || '#6b7280';
}