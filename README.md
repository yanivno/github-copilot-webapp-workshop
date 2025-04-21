

# Setup on your IDE

## 1.1 : Activate your virtual environment
```bash
cd /path/to/your/project
source .venv/bin/activate
```
## 1.2 : Install dependencies
```bash
pip3 install -r requirements.txt
```
## 1.3 : Run the app
```bash
python3 app.py
```
app should now be accsessible in `http://127.0.0.1:5000`

# Labs 
##  Lab #1 : get to know the app

**Imagine you are a new developer that hired to developer team, you need to explore the project and understand the main components**
   - Open your IDE platform and access your repository
   - Press on GitHub Copilot icon to open a chat
   - Explore the app by asking a questions like :
      - Can you tell me about this repository ? 
      - What framework the repository using ? 
      - Where the api routes handled out ?  
      - Which API routes the repository includes ?
      - Where are the main ui components ? 
      - What packages is the app using ?

**Explore Python and module with GitHub Copilot**
   - In your IDE Open GitHub Copilot Chat
   > @Github provides the ability to search within your repositories. Feel free to ask additional questions to deepen your understanding of the projects technology stack & general questions.
   > Tip : you can switch between models by selecing it from the dropdown menu in the bottom right corner of the chat window.
   - Enter the prompts: 
      - ```@github How do I create an API route in Python Flask?```
      - ```@github What are Server Actions in Python?```
      - ```@github How does the routing system work in Python Flask?```
      - ```@github How to create a ui template in Python Flask?```  
   
## Lab #2 : Get to know Copilot and Generate some code
Lets generate a new API Call to allow us to search movies by partial title
   - Open `app.py` file and place the cursor where you want to add the new route function
   - Use the Inline code generator by opening the inline chat window 
        in VSCode [Command+I](Mac) or [Ctrl+I](Windows)
        in Jetbrains [Shift+Ctrl+I](Mac) or [Shift+Ctrl+G](Windows)
   - You can write your own prompt or use the following:
    ```code
    add a new route function that allows me to search for movies by partial title following the implementation instructions:
    - The route should accept a query parameter called 'title' and return a list of movies that contains the partial search.
    - the route should be called '/api/search' and accept a query parameter called 'query'.
    ```
   - Test the new route by running the app and accessing it in your browser

## Lab #3 : implement a new feature for Application with Edit Mode

## Lab #4 : Use Agent Mode to Implement a new feature for Application

## Lab #5 : Explore MCP Server with Agent Mode