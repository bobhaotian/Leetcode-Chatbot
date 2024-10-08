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
   Please look at gptModel.py, and install all the required dependencies using pip
   The do
   ```bash
   npm i
   ```
   
3. Go to platform.openai.com to generate an API key and replace the one in gptModel.py

   
4. Set up the flask server:
    ```bash
    python3 gptModel.py
    ```
    
5. Start the user interface:
   ```bash
   npm run dev
   ```
   
6. Enter http://localhost:5173/ (default) then you can see
<img width="1509" alt="Screenshot 2024-10-07 at 1 49 17 AM" src="https://github.com/user-attachments/assets/72ab88e0-d30b-46b7-afa8-cb915a218bcf">

7. Type in any coding question, either the full description or a link, then click 'Generate'
<img width="1510" alt="Screenshot 2024-10-07 at 1 51 47 AM" src="https://github.com/user-attachments/assets/097ecefc-f738-4eaa-8efa-3c5bd539460f">

8. Wait for 2-5 seconds, the python solution with the template that Leetcode wants shows on the right
![image](https://github.com/user-attachments/assets/e6d4d172-c0af-44a7-8405-a73c3c2bc52b)

9. See the history by clicking 'History' button
<img width="1512" alt="Screenshot 2024-10-07 at 1 54 30 AM" src="https://github.com/user-attachments/assets/51a55877-e7f0-4f8b-88b5-b73f5940fc81">

## Values
Our project serves as a valuable tool for aspiring developers. By quickly generating code solutions, users can validate their own implementations, understand different coding approaches, and enhance their problem-solving skills. This not only accelerates learning but also fosters a deeper understanding of algorithms and data structures, and thus making it a significant resource in the coding community.
We noticed that high level Leetcoders have the ability and are eager to understand the code themselves and don't like to see lots of explanations to the answer. The output we provide contains a concise code that can directly copy to the Leetcode page, and they can view the code themselves in a very efficient way.

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

## Credits
Robert Bao
Yiyun Zhang
Steven Zhu


