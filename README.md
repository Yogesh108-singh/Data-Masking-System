🛡️ CSV Sensitive Data Masker

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

📸 Screenshot (Example)

(Add your own once the app runs — optional)

CSV Sensitive Data Masker (Dark Mode)
-------------------------------------
Upload File ➜ Detect ➜ Mask ➜ Download

🔒 Data Privacy Note

This tool performs all operations locally on your device.
Your data is never uploaded or shared anywhere outside your system.

👨‍💻 Author

👤 Yogesh Singh Kulegi
💼 Developer | 💡 Data Privacy Enthusiast
📧 [YourEmail@example.com
] (optional)
🌐 [LinkedIn / Portfolio link] (optional)

🏷️ License

This project is licensed under the MIT License — you are free to use, modify, and distribute it.
See the LICENSE
 file for more details.

⭐ Support the Project

If you like this project, give it a ⭐ on GitHub
!
Your support motivates further open-source contributions. 🙌
