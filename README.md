🗓️ AllocateMinus: The Monash Group Scheduler

<br />
<div align="center">
<h3 align="center">AllocateMinus</h3>

<p align="center">
A Python-powered scheduling engine that finds overlapping free time for Monash students.
<br />
<br />
<a href="https://www.google.com/search?q=https://github.com/Sr33kk0/AllocateMinus/issues">Report Bug</a>
·
<a href="https://www.google.com/search?q=https://github.com/Sr33kk0/AllocateMinus/issues">Request Feature</a>
</p>
</div>

<details>
<summary>Table of Contents</summary>
<ol>
<li><a href="#about-the-project">About The Project</a></li>
<li><a href="#built-with">Built With</a></li>
<li><a href="#getting-started">Getting Started</a></li>
<li><a href="#usage">How to Use</a></li>
<li><a href="#the-nerdy-stuff">The Nerdy Stuff</a></li>
<li><a href="#roadmap">Roadmap</a></li>
<li><a href="#contact">Contact</a></li>
</ol>
</details>

About The Project

AllocateMinus isn't just another calendar viewer. Monash University uses Allocate+ to distribute student timetables. While great for individuals, finding overlapping free time for a group project or study session requires manually cross-referencing multiple complex schedules over WhatsApp. I built this engine to solve that. By ingesting live .ical feeds and running an interval-overlap algorithm, the application calculates the exact time blocks where everyone in your group is free.

Built With

Python 3.11 (Backend Logic & Math)

FastAPI (REST API Framework)

PyWebView (Native Desktop UI Wrapper)

Tailwind CSS (Frontend Styling)

Docker (Containerization)

Getting Started

Want to try it out? You can run it as a standalone Windows app or host it on your own server.

Prerequisites

For Desktop: A Windows machine.

For Self-Hosting: Docker & Docker Compose installed.

Installation (Local Development)

Clone the repository:

git clone [https://github.com/Sr33kk0/AllocateMinus.git](https://github.com/Sr33kk0/AllocateMinus.git)


Create a virtual environment and activate it:

python -m venv .venv
source .venv/Scripts/activate


Install the dependencies:

pip install -r requirements.txt


Run the development server:

uvicorn main:app --reload


Installation (Docker)

To host this 24/7 on your local network (or via Tailscale):

docker-compose up -d


Usage

If using the compiled .exe version, simply double-click AllocateMinus.exe to open the native desktop window.

Objective: Find the exact times you and your friends are free to meet up on campus.

Mechanics: Paste your live Monash Allocate+ .ical link into the input field. Click "Add another person" to add as many group members as you need. Hit Calculate, and the engine will spit out the overlapping free blocks.

The Nerdy Stuff

This project demonstrates several advanced programming concepts beyond standard introductory scripting:

Algorithmic Design: Replaces complex interval subtraction with a grid-based boolean search algorithm, slicing the operational day into 30-minute chunks to find intersection points across multiple arrays.

Single Executable Routing: Utilizes a custom get_resource_path() function to override PyInstaller's sys._MEIPASS temporary directory, allowing a full FastAPI web server and an HTML frontend to be bundled and served from inside a single standalone .exe.

Timezone Manipulation: Implements the arrow library to parse UTC server times from Monash APIs and accurately convert them to Asia/Kuala_Lumpur local time, handling edge cases like midnight rollovers.

Dual Architecture: Architected so the backend can be compiled as a multi-threaded native desktop application (via pywebview) or spun up as a headless microservice inside a Docker container.

Roadmap

[x] Build core .ical parsing engine

[x] Implement multi-calendar overlap algorithm

[x] Build RESTful API using FastAPI

[x] Create native Windows Executable via PyInstaller + PyWebView

[ ] Implement Interval Merging Algorithm (Combine consecutive 30-min blocks into continuous sessions)

[ ] Add one-click Google Calendar invite generation

[ ] Migrate scheduling logic to a Discord Bot for easier group access

Contact

Ho Shou Yee (Daniel) - Bachelor of Computer Science Student at Monash University Malaysia

Project Link: https://github.com/Sr33kk0/AllocateMinus

Acknowledgments

Monash University

FastAPI Framework
