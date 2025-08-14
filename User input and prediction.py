# User Input Section
st.markdown("### 📝 House Details")
col1, col2 = st.columns(2)

with col1:
    bed = st.number_input("🛏 Bedrooms", min_value=1, max_value=10, value=3)
    stor = st.number_input("🏢 Stories", min_value=1, max_value=5, value=1)

with col2:
    bath = st.number_input("🛁 Bathrooms", min_value=1, max_value=10, value=2)
    ac = st.selectbox("❄ Air Conditioning", ["Yes", "No"])
    ac_val = 1 if ac == "Yes" else 0

st.markdown("---")

# Prediction Button
if st.button("🔮 Predict Price", use_container_width=True):
    prediction = model.predict(pd.DataFrame([[bed, bath, stor, ac_val]], columns=required_cols))
    st.success(f"💰 **Predicted House Price:** ${prediction[0]:,.2f}")
    st.balloons()
