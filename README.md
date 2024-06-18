# MCQ Generator

**MCQ Generator** is an end-to-end web application designed to effortlessly generate multiple-choice questions (MCQs) from text or PDF files. Leveraging advanced AI technology, this tool streamlines the quiz creation process for students, educators, and quiz enthusiasts.

## Features

- **AI-powered MCQ Generation**: Utilizes the OpenAI model `gpt-3.5-turbo` via API to generate high-quality MCQs from provided text or PDF files.
- **User-Friendly Interface**: Offers a simple and intuitive interface for uploading files, specifying the number of MCQs, and setting subject and difficulty level.
- **Flexible Input Formats**: Supports both text and PDF file formats, making it convenient for users to generate MCQs from various sources.
- **Downloadable Output**: Provides the option to download the generated quiz as CSV for further analysis or distribution.
- **LangChain Integration**: Seamlessly integrates with LangChain for enhanced natural language processing capabilities.

## Getting Started

To get started with **MCQ Generator**, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project.
4. Add your OpenAI API key to the `.env` file in the following format:
    OPENAI_API_KEY="your_openai_api_key"
5. Run the Streamlit app using the command `streamlit run StreamlitAPP.py`.
6. Upload your text or PDF file, specify the number of MCQs, and set subject and difficulty level.
7. Click the "Generate MCQs" button to generate the quiz.
8. Explore the generated MCQs and download the quiz as CSV if needed.

## Live Demo

Check out the live demo of the MCQ Generator [here](https://mcqgenerator-mayankchandak.streamlit.app/).

## Contributing

Contributions to **MCQ Generator** are welcome! To contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure the code is properly documented.
4. Test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

## Support

For any questions, issues, or feedback, please open an issue on GitHub or contact [Mayank Chandak](mailto:mayank.chandak21@gmail.com).

## License

This project is licensed under the [MIT License](https://github.com/open-source-ideas/open-source-ideas.github.io/blob/master/LICENSE).


