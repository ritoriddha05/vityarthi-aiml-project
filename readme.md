# 🧠 Smart Study Planner (Tkinter Desktop App)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview

The **Smart Study Planner** is an AI-inspired desktop application built using **Python and Tkinter** that helps students create an optimized and personalized study schedule.

It intelligently distributes study time based on:

* 📚 Subject difficulty
* ⏳ Available study hours
* 📅 Days remaining before exams

The system also includes **revision planning**, making it more effective than traditional planners.

---

## 🚀 Key Features

* 📅 Automatic timetable generation
* ⚖️ Difficulty-based time allocation
* 🔁 Revision scheduling (every 3rd day)
* 🖥️ Clean & modern dark-themed GUI
* 💾 Save plan to text file
* ⚡ Fast and lightweight

---

## 🧠 AI Logic Used

This project applies basic Artificial Intelligence concepts:

* **Heuristic Decision Making** → prioritizing subjects
* **Weighted Algorithm** → distributing study hours
* **Rule-Based System** → revision after every 3 days
* **Agent-Based Thinking** → system acts like a planner

---

## 🛠️ Tech Stack

| Component | Technology        |
| --------- | ----------------- |
| Language  | Python            |
| GUI       | Tkinter           |
| Libraries | tkinter, ttk      |
| IDE       | VS Code / PyCharm |

---

## 📂 Project Structure

```
Smart-Study-Planner/
│── app.py
│── README.md
│── screenshots/
│     ├── input.png
│     └── output.png
│── schedule.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Install Python

Check Python installation:

```
python --version
```

---

### 2️⃣ Clone Repository

```
git clone https://github.com/your-username/smart-study-planner.git
cd smart-study-planner
```

---

### 3️⃣ Run the Application

```
python app.py
```

👉 The GUI application will open.

---

## 🧪 How to Use

1. Enter **Subjects** (comma-separated)
   Example: `Maths, AI, Chemistry`

2. Enter **Difficulty Levels**
   (1 = Easy, 2 = Medium, 3 = Hard)
   Example: `2,3,1`

3. Enter:

   * Hours per day → `5`
   * Days left → `4`

4. Click **Generate Plan**

5. View your study schedule

6. Click **Save Plan** to export it

---

## 📸 Screenshots

### 🔹 Application Interface

![Screenshot 2026-03-25 204008.png](Screenshot%202026-03-25%20204008.png)

---

### 🔹 Generated Study Plan

![Screenshot 2026-03-25 204122.png](Screenshot%202026-03-25%20204122.png)

---

## 📈 Sample Output

```
Day 1
• Maths → 1.67 hrs
• AIML → 2.5 hrs
• Chemistry → 0.83 hrs

Day 3 (Revision)
• Maths → 1.67 hrs
• AIML → 2.5 hrs
• Chemistry → 0.83 hrs
```

---

## ⚠️ Limitations

* No real-time tracking
* No ML prediction yet
* Requires manual input

---

## 🔮 Future Enhancements

* 📊 Progress tracking dashboard
* 🤖 Machine learning integration
* 📱 Mobile/Web version
* 🔔 Smart reminders

---

## 👨‍💻 Author

**Ritoriddha Barman**
📌 Registration Number: 25BCE10854

---

## 📚 License

This project is developed for academic purposes only.

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
