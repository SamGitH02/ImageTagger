# Image Captioning and Tagging App

This Streamlit app uses Google's Gemini AI model to generate captions and tags for uploaded images. It also allows users to provide their own captions and tags for comparison.

## Acess the app
https://imagetaggergit-yhbbvbstdbfzwjwjjcvtir.streamlit.app/

## Features

*   **AI-Powered Captioning and Tagging:** Automatically generates descriptive captions and relevant tags for images using Google's Gemini AI.
*   **User Input:**  Allows users to enter their own captions and tags, providing a comparison with AI-generated results.
*   **Interactive Interface:** Features a user-friendly interface with collapsible sections and visually appealing styling.
*   **Error Handling:** Includes robust error handling to provide informative feedback to users in case of issues.
*   **Clear Button:** Allows users to easily reset the app and upload a new image.

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install streamlit google-generativeai pillow
    ```

2.  **Get your Google API Key:**
    *   Obtain a Google API key from the [MakerSuite](https://makersuite.google.com/app/apikey)

3.  **Replace API Key:**
    *   In the `app.py` file, replace `"YOUR_ACTUAL_API_KEY"` with your actual Google API key.

## Usage

1.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

2.  **Upload an Image:**
    *   Click the "Browse files" button to select an image from your computer.

3.  **Generate Caption & Tags:**
    *   Click the "Generate Caption & Tags" button. The app will process the image and display the AI-generated caption and tags.

4.  **Enter Your Own Caption & Tags (Optional):**
    *   If you'd like, enter your own caption and tags in the provided input fields.

5.  **View Results:**
    *   The app will display both the AI-generated and your own (if provided) captions and tags in collapsible sections.

6.  **Clear:**
    *   Click the "Clear" button to reset the app and upload a new image.

## Important Notes

*   Make sure you have a valid Google API key and have replaced the placeholder in the code.
*   For production environments, consider using environment variables or a secure configuration management tool to store your API key instead of hardcoding it.
*   Feel free to further customize the styling and layout to match your preferences.

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please open an issue or submit a pull request.
