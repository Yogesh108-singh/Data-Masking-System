🛡️ Data Masking System

A modern Streamlit web application that helps you detect and mask sensitive data (like emails, phone numbers, PAN, SSN, etc.) in CSV files to ensure data privacy and regulatory compliance — all with a clean dark theme interface.



🚀 Features<img width="1366" height="728" alt="Data Masking System and 3 more pages - Profile 1 - Microsoft​ Edge 09-11-2025 16_23_51" src="https://github.com/user-attachments/assets/8cfe2a43-0e2e-4035-a9e5-c791c3e36ce8" />


✅ Automatic Detection — Finds sensitive columns (Email, Phone, PAN, Aadhar, etc.)
✅ Three Masking Modes:

🟥 Redact: Fully hide values (⬛REDACTED⬛)

🟨 Partial: Keep last 4 characters visible

🟩 Hash: Hash data securely using SHA-256

✅ Modern Dark UI — Built with Streamlit’s flexible layout and custom CSS
✅ Full-Width Layout — Optimized for large CSVs and readability
✅ Instant CSV Download — Download your masked data immediately
✅ Local Execution — No cloud upload, all processing is done locally

🧩 Tech Stack
Component	Description
Python	Core programming language
Streamlit	Frontend web framework for UI
Pandas	For CSV file handling
Hashlib	For secure data hashing
HTML + CSS	For styling and layout customization
🛠️ Installation and Setup

1️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/CSV-Sensitive-Data-Masker.git
cd CSV-Sensitive-Data-Masker


2️⃣ Install Dependencies

pip install streamlit pandas


3️⃣ Run the App

python -m streamlit run csv_masker_app.py


4️⃣ Open in Browser
Visit 👉 http://localhost:8501

🧠 How It Works

Upload your CSV file.

The app automatically detects sensitive columns.

Choose a masking mode:

Redact (completely hide)

Partial (keep last 4 digits visible)

Hash (generate unique hashed value)

Preview your masked data.

Download the clean, privacy-safe CSV.

📸 Screenshot 

<img width="1366" height="728" alt="Data Masking System and 3 more pages - Profile 1 - Microsoft​ Edge 09-11-2025 16_23_51" src="https://github.com/user-attachments/assets/70825a47-b9cd-4d5a-8c19-f3c95604cf46" />


🔒 Data Privacy Note

This tool performs all operations locally on your device.
Your data is never uploaded or shared anywhere outside your system.

🧠 Real-World Benefits of This Project
Benefit	Description
🔒 Data Privacy	Keeps personal and sensitive information (like financial or medical data) safe before it’s shared or analyzed.
⚖️ Compliance	Makes it easier for organizations to meet major data protection laws such as GDPR, HIPAA, PDPA, and SOX.
🧰 Usability	Designed for everyone — no coding needed. Just upload your file, click a button, and download the protected version.
📁 Automation	Quickly anonymizes large CSV files without any manual work, saving time and effort.
🚫 Error-Free	Minimizes the risk of human mistakes that could cause accidental data leaks.
🌐 Cross-Industry Use	Useful across many sectors including finance, healthcare, education, retail, HR, and data analytics.


