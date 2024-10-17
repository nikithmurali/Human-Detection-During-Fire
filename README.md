# Human Detection Using Fire

In this project, we focus on enhancing safety measures in fire-prone environments through the development of an intelligent video analysis system. The core functionality of the system revolves around real-time human detection and smoke identification using advanced machine learning techniques, specifically employing the YOLOv8 object detection model.

Objectives:
Real-time Detection: The primary aim is to monitor video feeds in real-time to identify individuals in environments where fire hazards may occur. This capability can significantly improve response times in emergencies by alerting authorities or rescue teams promptly.

Smoke Identification: The project integrates smoke detection using edge detection techniques, allowing the system to identify potentially dangerous situations, such as a fire outbreak. The combination of human detection and smoke identification ensures a comprehensive monitoring solution.

Visual Feedback: By overlaying bounding boxes and labels on detected individuals and smoke regions, the system provides visual feedback for better situational awareness. This feature can be beneficial for operators monitoring multiple video feeds simultaneously.

Implementation Overview:
The implementation uses OpenCV and the YOLOv8 model for detecting objects in video frames. The system captures video input, processes each frame to identify humans and smoke, and outputs a new video file highlighting detected entities. Key features of the code include:

Object Detection: Utilizing the YOLOv8 model to detect humans and fire in the video frames.
Smoke Detection: Applying image processing techniques to detect smoke using edge detection.
Output Visualization: Annotating detected objects with bounding boxes and confidence scores, providing a clear visual representation of the detected entities.
Impact:
This project aims to contribute to safety protocols in various settings, including residential areas, industrial sites, and public spaces. By providing timely alerts and visual cues, the system enhances the ability to protect lives during fire incidents, ensuring a safer environment for all.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Virtual environment setup for managing dependencies.
- Smooth integration with **PyCharm Community Edition**.
- Easy package installation and management using `pip`.
- Cloud support via **Google Colab**.
- Clear Python interpreter configuration steps for PyCharm.

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x**  
- **PyCharm Community Edition**  
- **pip** (Python's package installer)

## Getting Started

Follow these steps to set up and run the project using **PyCharm Community Edition**.

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone <repository-url>
cd <repository-folder>
```
## 2. Set Up a Virtual Environment (Optional but Recommended)

You can create a virtual environment to manage dependencies.

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
## 3. Install Dependencies

Run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file doesn’t exist, you can create it by running:

```bash
pip freeze > requirements.txt
```

## 4. Open the Project in PyCharm

Open PyCharm and click on "Open".  
Select the folder containing your project.  
If prompted, choose to use the virtual environment you created earlier.

## 5. Configure the Python Interpreter

Go to `File > Settings > Project: <your-project-name> > Python Interpreter`.  
Click the gear icon and select "Add Interpreter".  
Choose "Existing Environment" and browse to the Python interpreter inside your `venv` folder:  
- On macOS/Linux: `venv/bin/python`  
- On Windows: `venv\Scripts\python.exe`  
Click OK to apply the changes.

## 6. Run the Code

Open the main Python file (e.g., `main.py`).  
Click `Run > Run...`, and select the Python file to execute.  
The output will appear in the Run tab at the bottom of PyCharm.

## 7. (Optional) Use Google Colab

If you want to run the code on Google Colab, upload the files and install dependencies by running:

```python
!pip install -r requirements.txt
```

## Usage

- **Install Dependencies**: Follow the instructions to install dependencies using pip.  
- **Configure Interpreter**: Set the correct interpreter in PyCharm for smooth execution.  
- **Run Code Locally**: Use the Run option to execute the code directly in PyCharm.  
- **Optional Cloud Execution**: If needed, execute the code on Google Colab.

## Project Structure

```
project-name/
├── main.py             # Main Python file to run the code
├── requirements.txt    # List of required Python packages
├── venv/               # Virtual environment folder (optional)
└── README.md           # This README file
```

- `main.py`: Contains the main logic of your code.  
- `requirements.txt`: Stores the dependencies required for the project.  
- `venv/`: Optional virtual environment to isolate dependencies.  
- `README.md`: Documentation for the project.  

## Troubleshooting

If you encounter any issues:

- Ensure the virtual environment is activated before installing packages.  
- Verify the Python interpreter is correctly set in PyCharm.  
- Check if all required packages are listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature-branch-name
    ```

3. Make your changes.
4. Commit your changes:

    ```bash
    git commit -m "Add some feature"
    ```

5. Push to the branch:

    ```bash
    git push origin feature-branch-name
    ```

6. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Thanks to everyone who contributed to this project!

