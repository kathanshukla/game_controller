# Game_controller using hand gestures

This project allows you to control the Hill Climber game using hand gestures. The system uses a webcam to capture hand movements and the gestures are processed to simulate keyboard presses, allowing you to control the game in a fun and interactive way.

## Features

- **Hand Detection**: Uses the `cvzone` and `mediapipe` libraries to detect hand gestures.
- **Keyboard Simulation**: Uses `pynput` to simulate keyboard presses based on hand gestures.
- **Real-time Processing**: Captures video from the webcam and processes hand gestures in real-time.

## Requirements

- Python 3.x
- `cvzone`
- `mediapipe`
- `opencv-python`
- `pynput`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/hand-gesture-controlled-hill-climber.git
   cd hand-gesture-controlled-hill-climber
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your webcam is connected.

2. Run the `main.py` script:
   ```sh
   python main.py
   ```

3. Open the Hill Climber game on your computer.

4. Use the following hand gestures to control the game:
   - **Move Right**: Raise your index finger (gesture: [0,1,0,0,0]).
   - **Move Left**: Raise your thumb or both thumb and index finger (gestures: [1,0,0,0,0] or [1,1,0,0,0]).

5. To quit the application, press the 'q' key.

## Code Overview

- `main.py`: The main script that captures video from the webcam, detects hand gestures, and simulates keyboard presses.
- `requirements.txt`: Lists the Python dependencies required for the project.
