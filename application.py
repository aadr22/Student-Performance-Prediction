from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

def create_prediction(form_data):
    """
    Create a prediction based on form data.
    
    Args:
        form_data: Flask form data containing student information
        
    Returns:
        tuple: (prediction_result, error_message)
    """
    try:
        # Print form data for debugging
        print("Received form data:", dict(form_data))
        
        data = CustomData(
            gender=form_data.get('gender'),
            # Note the change from ethnicity to race_ethnicity to match your CustomData class
            race_ethnicity=form_data.get('race_ethnicity'),
            parental_level_of_education=form_data.get('parental_level_of_education'),
            lunch=form_data.get('lunch'),
            test_preparation_course=form_data.get('test_preparation_course'),
            reading_score=float(form_data.get('reading_score')),
            writing_score=float(form_data.get('writing_score'))
        )
        
        pred_df = data.get_data_as_data_frame()
        print("Created DataFrame:", pred_df)  # Debug print
        
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        print("Prediction results:", results)  # Debug print
        
        return results[0], None
    except Exception as e:
        print("Error occurred:", str(e))  # Debug print
        return None, str(e)

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    """
    Handle prediction requests.
    
    GET: Display the prediction form
    POST: Process the form data and display results
    """
    if request.method == 'GET':
        return render_template('home.html')
    
    result, error = create_prediction(request.form)
    
    if error:
        print("Error in prediction:", error)  # Debug print
        return render_template('home.html', error=error)
    
    print("Rendering template with result:", result)  # Debug print
    return render_template('home.html', results=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)