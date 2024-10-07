# AI Chatbot for LeetCode Solutions

This repository contains an AI chatbot fine-tuned using **GPT-4o** to provide efficient solutions to LeetCode questions, focusing on optimizing runtime performance. The project follows three key stages: **data preparation**, **fine-tuning**, and **deployment**.

## Features
- **AI-powered LeetCode solutions**: The chatbot provides optimized code solutions to a wide variety of LeetCode problems.
- **High runtime efficiency**: All solutions are validated to ensure they pass LeetCode tests with optimal performance.
- **Support for multiple tags**: The chatbot handles problems from various categories such as Arrays, Strings, Hash Tables, Dynamic Programming, and more.

## Project Stages

### 1. Data Preparation
We start by preparing the training data. This involves:
- **Python Crawler**: We implemented a Python web crawler to collect user solutions marked as "beat 100%" or "O(1)" from LeetCode for problems tagged with:
  - Array, String, Hash Table, Dynamic Programming, Math, Sorting, Greedy, Depth-First Search, Database, Binary Search, Matrix, Breadth-First Search, Tree, Bit Manipulation, Two Pointers, Binary Tree, Heap (Priority Queue), Prefix Sum.
  
  For each question, we collected **5 top user solutions**.

- **Data Augmentation**: Since some tags lacked enough high-quality solutions, we augmented our data by leveraging GPT-4o. We used **5 test cases** as prompts for GPT-4o to generate solutions for an additional **30 questions** per tag where high-quality data was lacking.

- **Validation**: The generated solutions were validated by submitting them to LeetCode to ensure they passed all test cases and had competitive runtime efficiency. This process yielded **540 high-quality training samples**.

### 2. Fine-tuning
Once the training data was ready, we uploaded the 540 validated solutions to OpenAI to fine-tune the GPT-4o model. This custom model is now optimized for solving LeetCode problems with a focus on runtime efficiency.

### 3. Deployment
We developed a user-friendly interface where users can interact with the fine-tuned GPT-4o model, input LeetCode problems, and receive high-performance solutions.

## How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/leetcode-ai-chatbot.git
    cd leetcode-ai-chatbot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the chatbot interface:
    ```bash
    python app.py
    ```

4. Enter a LeetCode problem description, and the chatbot will generate an optimized solution.

## Tags Supported
The chatbot supports problems in the following categories:
- Array
- String
- Hash Table
- Dynamic Programming
- Math
- Sorting
- Greedy
- Depth-First Search
- Database
- Binary Search
- Matrix
- Breadth-First Search
- Tree
- Bit Manipulation
- Two Pointers
- Binary Tree
- Heap (Priority Queue)
- Prefix Sum

## Future Work
- **Expand dataset**: We plan to collect more training data for additional tags.
- **Improve solution quality**: By fine-tuning with even larger datasets and incorporating more advanced validation techniques.
- **Enhance user interface**: Adding more features such as solution explanations and code analysis.

## Contributing
We welcome contributions! If you'd like to help improve the chatbot, feel free to open a pull request or issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
