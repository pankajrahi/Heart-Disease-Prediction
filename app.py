import numpy as np
# from flask import Flask, request, jsonify, render_template
import pickle
import streamlit as st

# app = Flask(__name__)
model = pickle.load(open('logisticmodel.pkl','rb')) 
# @app.route('/')
# def home():
  
#     return render_template("index.html")
  
# @app.route('/predict',methods=['GET'])
def predict(chol):
    

    
    # '''
    # For rendering results on HTML GUI
    # '''
    # exp = float(request.args.get('exp'))
    
    prediction = int(model.predict([[float(chol)]]))
    
        
    # return render_template('index.html', prediction_text='Regression Model  has predicted salary for given experinace is Rs.  : {}'.format(prediction))
    # return tenure,login_device,city_tier,warehouse_to_home,preferred_payment_mode,gender,hour_spend_on_app,prefered_order_cat,satisfaction_score,marital_status,number_of_address,complain,order_amount_hike_from_last_year,coupon_used,order_count,day_since_last_order,cash_back_amount
    if prediction == 0:
        text = "No"
    else:
        text = "Yes- Person have sign and symptoms of Heart disease"

    return text

def main():

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction using ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    # exp = st.number_input('Experience', 2, 40)
    chol = st.number_input('cholestrol',step =1., format="%.2f")
    

    result=""
    if st.button("Predict"):
        result=predict(float(chol))
    st.success(result)

    if st.button("About me"):
        st.text("By Dr. Pankaj Rahi")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

