<h1 align="center">DocSummarize</h1>

<p align="center">AI-powered TUI application for fast and concise document summarization</p>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/XST-BD/DocSummary.svg)](https://github.com/XST-BD/DocSummary/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/XST-BD/DocSummary.svg)](https://github.com/XST-BD/DocSummary/pulls)

</div>

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Idea / Solution](#idea--solution)
- [Dependencies / Limitations](#dependencies--limitations)
- [Future Scope](#future-scope)
- [Getting Started](#getting-started)
    - [Prerequisites](#setup-before-1st-run)
    - [Setup before every run](#setup-before-every-run)
    - [Running the Application](#run-the-application)
- [Usage](#usage)
- [Built With](#built-with)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Problem Statement

It is useful to design and follow a specific format when writing a problem statement. While there are several options
for doing this, the following is a simple and straightforward template often used in Business Analysis to maintain
focus on defining the problem.

- IDEAL: This section is used to describe the desired or “to be” state of the process or product. At large, this section
  should illustrate what the expected environment would look like once the solution is implemented.
- REALITY: This section is used to describe the current or “as is” state of the process or product.
- CONSEQUENCES: This section is used to describe the impacts on the business if the problem is not fixed or improved
  upon.
  This includes costs associated with loss of money, time, productivity, competitive advantage, and so forth.

Following this format will result in a workable document that can be used to understand the problem and elicit
requirements that will lead to a winning solution.

## Idea / Solution

This section is used to describe potential solutions.

Once the ideal, reality, and consequences sections have been
completed, and understood, it becomes easier to provide a solution for solving the problem.

## Dependencies / Limitations

- What are the dependencies of your project?
- Describe each limitation in detailed but concise terms
- Explain why each limitation exists
- Provide the reasons why each limitation could not be overcome using the method(s) chosen to acquire.
- Assess the impact of each limitation in relation to the overall findings and conclusions of your project, and if
  appropriate, describe how these limitations could point to the need for further research.

## Future Scope

Write about what you could not develop during the course of the Hackathon; and about what your project can achieve
in the future.

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup before 1st run

1. Clone the repository
    ```bash
    git clone 
    ````
2. Navigate to the project directory
    ```bash
    cd path/to/folder/DocSummarize
    ```
3. Set up a virtual environment (optional but recommended)
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment
- On Windows
    ```bash
    venv\Scripts\activate
    ```
- On macOS / Linux
    ```bash
    source venv/bin/activate
    ```
5. Install the required dependencies
    ```bash
    pip install -r requirements.txt
    ```

### Setup before every run
1. Navigate to the project directory
    ```bash
    cd path/to/folder/DocSummarize
    ```
2. Activate the virtual environment
- On Windows
    ```bash
    venv\Scripts\activate
    ```
- On macOS / Linux
    ```bash
    source venv/bin/activate
    ```

### Run the Application

#### Windows
```bash
python main.py
```

#### macOS / Linux
```bash
python3 main.py
```

## Usage

- Enter the path of the document you want to summarize.
- (Optional) Provide custom prompt.
- Press the "Generate" button to generate the summary.
- View the generated summary in the designated area.

## Built With

- [**Python**](https://www.python.org/) - Core Language
- [**Textual**](https://textual.textualize.io/) - TUI Framework
- **Other Tools:**

## Authors

- [**Atia Farha**](https://github.com/Atia-Farha) - Frontend Developer
- [**S.M Nazmus Sadat**](https://github.com/smsadat-dev) - Backend Developer