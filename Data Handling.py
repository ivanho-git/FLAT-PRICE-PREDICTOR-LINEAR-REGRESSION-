# Load Data
try:
    data = pd.read_csv("Housing.csv")
except FileNotFoundError:
    st.error("❌ 'Housing.csv' not found in the same folder as this script.")
    st.stop()

# Data Preprocessing
if "airconditioning" in data.columns:
    data['airconditioning'] = data['airconditioning'].apply(lambda x: 1 if str(x).lower() == 'yes' else 0)

required_cols = ['bedrooms', 'bathrooms', 'stories', 'airconditioning']
target_col = 'price'

if not all(col in data.columns for col in required_cols + [target_col]):
    st.error(f"❌ CSV must contain these columns: {', '.join(required_cols + [target_col])}")
    st.stop()
