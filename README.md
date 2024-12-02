
<body>
    <h1>Real-Time Pose Detection with YOLOv8</h1>
    <p>
        This project demonstrates real-time human pose detection using YOLOv8, visualizing a skeleton animation 
        based on keypoints detected in the video feed. The application uses a webcam to detect human poses and 
        displays both the skeleton animation and the original camera feed.
    </p>

    <hr>

    <h2>Folder Structure</h2>
    <pre>
project-folder/
├── images/
│   ├── result_screenshot.png     # Screenshot showing detection result
│   ├── keypoints_diagram.png     # Diagram explaining keypoint indices
├── requirements.txt              # Project dependencies
├── src/
│   ├── skeleton.py               # Main Python code for pose detection
│   └── yolov8/
│       └── yolov8n-pose.pt       # YOLOv8 pose detection model
    </pre>

    <hr>

    <h2>Installation</h2>
    <h3>1. Clone the Repository</h3>
    <pre>
git clone &lt;repository-link&gt;
cd project-folder
    </pre>

    <h3>2. Set Up the Environment</h3>
    <ul>
        <li>Ensure you have Python 3.8 or higher installed.</li>
        <li>Install the required libraries:</li>
    </ul>
    <pre>
pip install -r requirements.txt
    </pre>

    <h3>3. Verify YOLOv8 Model</h3>
    <p>
        Ensure the YOLOv8 model <code>yolov8n-pose.pt</code> is placed in the <code>src/yolov8</code> folder.
    </p>

    <hr>

    <h2>Usage</h2>
    <h3>1. Run the Pose Detection Script</h3>
    <pre>
python src/skeleton.py
    </pre>

    <h3>2. Exit</h3>
    <p>Press the <code>q</code> key to exit the application.</p>

    <hr>

    <h2>How It Works</h2>
    <ul>
        <li>The YOLOv8 model processes the webcam feed to detect keypoints corresponding to human body parts.</li>
        <li>Skeleton lines are drawn between the keypoints to create an animated visual representation of the detected poses.</li>
        <li>The results are displayed in two windows:
            <ul>
                <li><b>Skeleton Animation</b>: Shows the extracted skeleton.</li>
                <li><b>Original Camera Feed</b>: Displays the webcam feed with overlaid annotations.</li>
            </ul>
        </li>
    </ul>

    <hr>

    <h2>Screenshots</h2>
    <h3>1. Detection Result</h3>
    <img src="images/result_screenshot.png" alt="Result Screenshot" style="max-width: 100%;">

    <h3>2. Keypoints Diagram</h3>
    <img src="images/keypoints_diagram.png" alt="Keypoints Diagram" style="max-width: 100%;">

    <hr>

    <h2>Key Features</h2>
    <ul>
        <li>Real-time pose detection using YOLOv8.</li>
        <li>Skeleton visualization extracted from keypoint data.</li>
        <li>Displays pose data on webcam feed and a separate skeleton window.</li>
    </ul>

    <hr>

    <h2>Dependencies</h2>
    <p>The following dependencies are listed in the <code>requirements.txt</code> file:</p>
    <ul>
        <li><code>ultralytics</code>: For YOLOv8 model support.</li>
        <li><code>opencv-python</code>: For video processing and rendering.</li>
        <li><code>numpy</code>: For numerical computations.</li>
    </ul>
    <p>Install them using:</p>
    <pre>
pip install -r requirements.txt
    </pre>

    <hr>

    <h2>Acknowledgments</h2>
    <ul>
        <li><b>YOLOv8</b> by <a href="https://ultralytics.com/" target="_blank">Ultralytics</a>.</li>
        <li><b>OpenCV</b> for computer vision tools.</li>
    </ul>

    <hr>

    <h2>License</h2>
    <p>This project is licensed under the MIT License. Feel free to use and modify it for your needs!</p>
</body>

