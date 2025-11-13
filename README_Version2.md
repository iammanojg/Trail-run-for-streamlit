```markdown
# Smart Spending Advisor (Streamlit)

Files
- app.py — Streamlit app.
- data/customers.csv — sample dataset (optional).
- requirements.txt — Python dependencies.

Run locally
1. Create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows

2. Install dependencies:
   pip install -r requirements.txt

3. Run Streamlit:
   streamlit run app.py

Notes
- The app will try to load data/customers.csv from the repo if present.
- You can also upload a CSV using the sidebar file uploader while the app is running.
- CSV should include columns: Customer ID, Category, Total Spent, Payment Method.
```