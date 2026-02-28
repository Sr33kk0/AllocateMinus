<br />
<div align="center">
  <h1 align="center">AllocateMinus</h3>

  <p align="center">
    A Python-powered scheduling engine that finds overlapping free time for students.
    <br />
    <br />
    <a href="https://github.com/Sr33kk0/AllocateMinus/issues">Report Bug</a>
    ·
    <a href="https://github.com/Sr33kk0/AllocateMinus/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage">How to Use</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

---

## About The Project

**AllocateMinus** isn't just another calendar viewer. Finding overlapping free time for a group project or study session requires manually cross-referencing multiple complex schedules over WhatsApp. 

I built this engine to solve that. By ingesting live `.ical` feeds and running an interval-overlap algorithm, the application calculates the exact time blocks where everyone in your group is free.



---

## Built With

* **Python 3.11** (Backend Logic & Math)
* **FastAPI** (REST API Framework)
* **Tailwind CSS** (Frontend Styling)
* **Docker** (Containerization)
* **PyWebView** (Native Desktop UI Wrapper)

---

## Getting Started

Want to try it out? You can run it as a standalone Windows app or host it on your own server.

### Prerequisites

* **For Desktop:** A Windows machine.
* **For Self-Hosting:** Docker & Docker Compose installed.

### Installation (Local Development)

1. **Clone the repository:**
   ```sh
   git clone [https://github.com/Sr33kk0/AllocateMinus.git](https://github.com/Sr33kk0/AllocateMinus.git)
   cd AllocateMinus

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv .venv
   
   # For Windows:
   .venv\Scripts\activate
   
   # For macOS/Linux:
   source .venv/bin/activate

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt

4. **Run the development server:**
   ```sh
   uvicorn main:app --reload

### Installation (Docker)

To host this 24/7 on your local network (or via Tailscale):
  ```sh
  docker-compose up -d
  ```

## Usage

If using the compiled `.exe` version, simply double-click `AllocateMinus.exe` to open the native desktop window.

* **Objective**: Find the exact times you and your friends are free to meet up on campus.
* **Mechanics**: 
    1. Paste your live  Allocate+ `.ical` link into the input field.
    2. Click **"Add another person"** to add as many group members as you need.
    3. Hit **Calculate**, and the engine will display the overlapping free blocks.

---

## Roadmap

- [x] Build core `.ical` parsing engine
- [x] Implement multi-calendar overlap algorithm
- [x] Build RESTful API using FastAPI
- [x] Create native Windows Executable via PyInstaller + PyWebView
- [ ] Implement **Interval Merging Algorithm** (Combine consecutive 30-min blocks into continuous sessions)
- [ ] Add one-click **Google Calendar invite** generation

---

## Contact

**Ho Shou Yee (Daniel)** - Bachelor of Computer Science Student at Monash University Malaysia  
Project Link: [https://github.com/Sr33kk0/AllocateMinus](https://github.com/Sr33kk0/AllocateMinus)

## Acknowledgments
* [FastAPI Framework](https://fastapi.tiangolo.com/)
