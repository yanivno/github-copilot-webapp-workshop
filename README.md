

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

### New Code Generation

Lets generate a new API Call to allow us to search movies by partial title
- Open `app.py` file and place the cursor where you want to add the new route function
- Use the Inline code generator by opening the inline chat window 
      in VSCode [Command+I](Mac) or [Ctrl+I](Windows)
      in Jetbrains [Shift+Ctrl+I](Mac) or [Shift+Ctrl+G](Windows)

we would like to implement a new feature for the application - an API for searching movies by partial title.
write a propmt to generate a new route function in 'app.py' file
<details>
<summary>or use the following prompt</summary>
add a new route function that allows me to search for movies by partial title following the implementation instructions:
- The route should accept a query parameter called 'title' and return a list of movies that contains the partial search.
- the route should be called '/api/search' and accept a query parameter called 'query'.
</details>

Test the new route by running the app by using curl

```bash
curl -X GET -v "http://127.0.0.1:5000/api/search?query=inter"
```
<details>
<summary>sample response</summary>
<pre>
* Trying 127.0.0.1:5000...
* Connected to 127.0.0.1 (127.0.0.1) port 5000
> GET /api/search?query=inter HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Server: Werkzeug/3.1.3 Python/3.13.3
< Date: Tue, 22 Apr 2025 10:45:17 GMT
< Content-Type: application/json
< Content-Length: 294
< Connection: close
< 
[
  {
    "country": "USA",
    "director": "Christopher Nolan",
    "id": 3,
    "main_actors": [
      "Matthew McConaughey",
      "Anne Hathaway",
      "Jessica Chastain"
    ],
    "poster": "static/resources/posters/interstellar.jpg",
    "title": "Interstellar",
    "year": 2014
  }
]
* Closing connection 0
</pre>
</details>

### Generate Unit Tests

Lets write some testing for the code we just generated
- Open `app.py` file and the Github Copilot chat window, switch to Edit Mode
  (app.py file would be added to the context automatically)
- Write a prompt to generate unit tests for methods in the app.py file
<details>
<summary>or use the following prompt</summary>
add unit test module that tests all application routes in the 'app.py' file.  
The tests should cover positive test cases and negative test cases for each route.
The tests should be written in the 'test_app.py' file and use the unittest framework.
</details>

>Tip: you can use the built-in '/tests' command in Ask mode to ask GitHub Copilot to generate tests for app in @workspace context.

>Tip: in VSCode you can use the built-in '@terminal' extension in Ask mode to ask GitHub Copilot to diagnose errors or fix the falied tests for app, if there are any. sample prompt: @terminal fix tests in test_app.py

### Customize Code generation

Github Copilot responses can be customized by providing additional context or instructions. This can help Copilot generate code that is more aligned with your specific requirements.
those instructsion can be provided in the form of comments or docstrings in the code, or by using specific keywords or phrases in your prompts. 
   - In the root of your repository, create a file named ```.github/copilot-instructions.md```
     Create the .github directory if it does not already exist.
   - Add natural language instructions to the file, in Markdown format.
     Whitespace between instructions is ignored, so the instructions can be written as a single paragraph, each on a new line, or separated by blank lines for legibility
   - Instructions: 
     - ```Use snake_case for variable and function names.```
     - ```Use CamelCase for class names.```
     - ```Follow PEP 8 style guidelines.```
     - ```Include type hints for function parameters and return types.```
     - ```Write docstrings for all public modules, classes, functions, and methods.```

### Add Comments to Code
   One of the common frustrations for developers is documenting their code properly, but don’t worry — Copilot is here to help!:
   - Open app.py
   - Use GitHub Copilot Chat to gain insights into the code. Simply select the code and choose the /explain option for a detailed breakdown.
   - Use the Inline code generator by opening the inline chat window 
      in VSCode [Command+I](Mac) or [Ctrl+I](Windows)
      in Jetbrains [Shift+Ctrl+I](Mac) or [Shift+Ctrl+G](Windows) 
   and enter /doc.
    > GitHub Copilot will generate a documentation-style function declaration.
   - You can also use Copilot Chat to generate additional documentation. Open GitHub Copilot Chat and enter a prompt: ```Add comments to my code```
   - Add /docs and comments to other functions as well.
   > When adding comments to the code, ensure that GitHub Copilot Chat applies custom instructions with each request.

## Lab #3 : implement a new feature for Application with Edit Mode

Edit Mode is a powerful feature of GitHub Copilot that allows you to edit and modify code snippets generated by Copilot. It provides a more interactive and collaborative experience, enabling you to refine and customize the generated code to better suit your needs.

Edit Mode is particularly useful when you want to make changes to existing code or when you want to generate code that requires more context or specific requirements. It allows you to provide additional instructions and context to Copilot, which can lead to more accurate and relevant code suggestions.

### New Feature Generation
We are going to implement a new feature that allows for UI Filtering of movies based on year and genre, using Edit Mode. 
- In Github Copilot chat window, switch to Edit Mode by Selecting 'Edit' (Jetbrains) or 'Edit' in dropdown (VSCode)
- Click on the 'Add FIles' (Jetbrains) or 'Add Context' (VSCode) to add a file to the context and select `app.py`, `test_app.py`, `movies.json` and `templates/index.html` files.
- Write a prompt to generate a new feature that allows for UI Filtering of movies based on year and genre

<details>
<summary>or use the following prompt</summary>
<pre>
Implement a new feature that allows for UI Filtering of movies based on year and genre.
The feature should include the following:
- A dropdown menu for selecting the year of the movie.
- A dropdown menu for selecting the genre of the movie.
- A button to apply the filters.
- The filtered movies should be displayed in the same format as the original list of movies.
- The filtering should be done on the client side using JavaScript.
- The filtering should be done on the server side using Python Flask.
- add unit tests for the new feature in the 'test_app.py' file.
- The new feature should be implemented in the 'app.py' file and the 'index.html' file.
</pre>
</details>

Test the new feature by running the app and accessing the UI in your browser

you can continue to iterate on the code by asking Copilot to add more features or fix bugs in the code.

## Lab #4 : Use Agent Mode to Implement a new feature for Application ***

>The Main difference between Edit Mode and Agent Mode is that in Edit Mode, you are in control of the code generation process.You can ask Copilot to generate code snippets, and it will provide you with suggestions based on your prompts. In Agent Mode, Copilot takes the lead and generates code based on your requirements without needing to specify every detail.

>This Lab is designed for Visual Studio Code as Agent Mode is not available yet in other IDEs.

### New Feature Generation
We are going to implement a new feature that allows for UI of User Reviews of movies, using Agent Mode.
- In Github Copilot chat window, switch to Agent Mode by Selecting 'Agent' in dropdown
>Using GPT-4.1|Claude 3.7 or o4-mini will yeald different results and might be useful to experiment with.
- Prompt Copilot to generate a new feature that allows for UI of User Reviews of movies
<details>
<summary>or use the following prompt</summary>
Implement a new feature that allows for UI of User Reviews of movies.
The feature should include the following:
- A form for submitting user reviews.
- A section for displaying user reviews.
- The reviews should be stored in movies.json file.
- The reviews should be displayed in the same format as the original list of movies.
- Create a movie details page that displays the movie title, poster, and reviews.
</details>
- Test the new feature by running the app and accessing the UI in your browser
- You can continue to iterate on the code by asking Copilot to add more features or fix bugs in the code.

## Lab #5 : Explore MCP with Agent Mode

>This Lab is designed for Visual Studio Code as both MCP support in Jetbrains and Agent Mode are not available yet in those IDEs.

>MCP support in Visual Studio Code is in Public Preview and may be enhanced in future versions. Instructions for activation is available in [Official Documentation](https://github.com/github/github-mcp-server)

Model Context Protocol (MCP) is an open-source and universal communication protocol that allows AI models to connect to external data sources. MCP has been developed by Anthropic, and Google, OpenAI, and Microsoft are now working to adopt the universal standard. Many popular MCP servers, including Google Maps, Slack, GitHub, Gmail, and more, allow AI models to interact with these tools and services.

Native support in GitHub Copilot Chat for MCP allows you to use the protocol to connect to external data sources and services. This enables you to build more powerful and flexible applications that can leverage the capabilities of AI models and external data sources.

Further read on adding MCP Tools to Agent mode is available in [Here](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
MCP servers listing [Here](https://github.com/punkpeye/awesome-mcp-servers)
and [Here](https://mcp.so)

### Create a personal access token
To use the GitHub MCP server, you need to create a personal access token (PAT) with the necessary permissions. Follow these steps to create a PAT:
1. Go to your GitHub account settings.
2. Click on "Developer settings" in the left sidebar.
3. Click on "Personal access tokens" in the left sidebar.
4. Click on "Tokens (classic)".
5. Click on "Generate new token".
6. Give your token a descriptive name (e.g., "MCP Token").
7. Select the scopes you want to grant to the token. select "repo" to have access your repositories.
8. Click on "Generate token".
9. Copy the generated token and store it securely. You won't be able to see it again.


### Create mcp configuration file
We would create a local configuration file for MCP server in the root of your repository.
- Create a file named `.vscode/mcp.json` in your repository.
- Add the following content to the file:
```json
{
   "servers": {
      "github": {
         "command": "docker",
         "args": [
               "run",
               "-i",
               "--rm",
               "-e",
               "GITHUB_PERSONAL_ACCESS_TOKEN",
               "mcp/github"
         ],
         "env": {
               "GITHUB_PERSONAL_ACCESS_TOKEN": "<your Github PAT Token>"
         }
      }
   }
}
```
- Save the file.
- Switch Github Copilot Chat to Agent Mode by selecting the "Agent" option in the dropdown menu.
- Click on the Refresh Icon to list the new Github MCP server tools to be used by GitHub Copilot Chat.

### Use MCP with Agent Mode
- In the Github Copilot Chat window, switch to Agent Mode by selecting the "Agent" option in the dropdown menu.
- Use the natural language prompt to use tools with Github MCP server:
- Some samples: 
   - ```summarize issues in github/docs github repository```
   - ```summarize prs in github/docs github repository```
   - ```create a new private github repository name my-demo-repo```
   - ```create a new issue in repository my-demo-repo github repository with title "test issue" and body "this is a test issue"```
   - ```assign myself to issue #1 in my-demo-repo github repository```
   - ```add a comment to issue #1 in my-demo-repo github repository with the text "this is a test comment"```
   - ```label issue #1 in my-demo-repo github repository with "kind/bug"```

## Lab #6 : Code Review with Copilot Chat 
### Code Review with Copilot Chat

>This Lab is designed for Visual Studio Code.

   GitHub Copilot can review your code and provide feedback. Where possible, Copilot's feedback includes suggested changes which you can apply with a couple of clicks.
   - Open the `app.py` file 
   - In MacOS press [Cmd+Shift+P] | in Windows [Ctrl+Shift+P] po open the command pallette and prompt: GitHub Copilot: Review and comment
   - GitHub Copilot will suggest code improvements, which you can choose to accept, reject, or skip to move on to the next suggestion. You'll also find the complete suggestions in the comments section.