# clog

Clog – the clunky cousin of Claude Code

A toy version of Claude Code using Google's free Gemini API! It's a fun, lightweight experiment meant to explore code generation, prompt engineering, and AI-assisted development workflows.

## Features

- 🤖 AI-powered coding assistant using Google's Gemini 2.0 Flash
- 📁 File system operations (list, read, write files)
- 🐍 Python code execution with command-line arguments
- 🧮 Includes a sample calculator application
- 🔧 Function calling capabilities for interactive development
- 🔄 Automatic retry logic for API reliability

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd clog
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Gemini API key:**
   - Get a free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

### Basic Usage

Run the AI assistant with a prompt:

```bash
python main.py "your prompt here"
```

### Examples

**Ask for help with the calculator:**
```bash
python main.py "How does the calculator app work?"
```

**Request code analysis:**
```bash
python main.py "Analyze the calculator code and suggest improvements"
```

**Ask for debugging help:**
```bash
python main.py "The calculator gives wrong results for 3 + 7 * 2, can you fix it?"
```

**Request new features:**
```bash
python main.py "Add support for parentheses in the calculator"
```

### Verbose Mode

For detailed function call information:
```bash
python main.py "your prompt" --verbose
```

## Sample Calculator App

The project includes a sample calculator application to demonstrate the AI assistant's capabilities.

### Running the Calculator

```bash
python calculator/main.py "3 + 7 * 2"
python calculator/main.py "10 / 2 - 1"
```

### Calculator Features

- Basic arithmetic operations (+, -, *, /)
- Proper order of operations (PEMDAS)
- Formatted output display
- Error handling for invalid expressions

## Project Structure

```
clog/
├── README.md              # This file
├── main.py               # Main AI assistant
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── .env                  # API key configuration (create this)
├── functions/            # AI assistant functions
│   ├── get_files_info.py # List files and directories
│   ├── get_file_content.py # Read file contents
│   ├── run_python.py     # Execute Python scripts
│   └── write_file.py     # Write/create files
└── calculator/           # Sample calculator application
    ├── main.py           # Calculator CLI
    ├── pkg/
    │   ├── calculator.py # Calculator logic
    │   └── render.py     # Output formatting
    └── tests.py          # Calculator tests
```

## Available Functions

The AI assistant can perform the following operations:

- **`get_files_info`**: List files and directories with sizes
- **`get_file_content`**: Read and return file contents
- **`run_python_file`**: Execute Python files with optional arguments
- **`write_file`**: Create or overwrite files with new content

All operations are constrained to the working directory for security.

## Configuration

- **`MAX_CHARS`**: Maximum characters for file operations (default: 10,000)
- **Working Directory**: Set to `./calculator` for AI operations
- **API Model**: Uses `gemini-2.0-flash-001`

## Error Handling

The assistant includes robust error handling:
- Automatic retry logic for API failures (503, 429, 502, 504 errors)
- Exponential backoff for rate limiting
- Graceful function call error reporting
- File operation safety checks

## Examples of AI Interactions

**Code Review:**
```bash
python main.py "Review the calculator code for potential bugs"
```

**Feature Development:**
```bash
python main.py "Add a square root function to the calculator"
```

**Testing:**
```bash
python main.py "Create comprehensive tests for the calculator"
```

**Documentation:**
```bash
python main.py "Generate docstrings for all calculator functions"
```

## Limitations

- Uses Google's free Gemini API (subject to rate limits)
- File operations restricted to project directory
- Python execution only (no other languages)
- No persistent conversation history

## Contributing

This is an experimental project. Feel free to:
- Report issues or bugs
- Suggest new features
- Submit improvements
- Add more sample applications

## License

See LICENSE file for details.

## Troubleshooting

**API Key Issues:**
- Ensure your `.env` file contains a valid `GEMINI_API_KEY`
- Check that your API key has proper permissions

**Rate Limiting:**
- The assistant will automatically retry with exponential backoff
- Use `--verbose` flag to see retry attempts

**File Access Errors:**
- All file paths must be relative to the working directory
- Check file permissions for write operations

---

*Happy coding with your clunky AI assistant! 🤖*