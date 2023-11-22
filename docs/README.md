# A study of Text-to-image
## Written By 練鈞揚, 連文聖

---

## Information about the project 
- ### Why we created this tool? 
  - Artificial intelligence (AI) techniques have progressed rapidly in recent years. As university students, AI tools are part of our life. 
  
    While searching our project topic, we discovered that many people have not used text-to-image tools before or unware of them. 
    
    Therefore, we developed this tool to introduce people text-to-image techniques, expecting to make more individuals aware of the powerful tool.
- ### What are the functions of this tool?
  - In our project, we provide a tool which can be used to display pictures of the corresponding to the prompts from stories users provided. 
   
    Furthermore, we build a user friendly page where users can chat with AI. 
    
    This setup allows users to utilize the tools more conveniently, eliminating the need to open multiple screens.

## About the Project Technique
### 1. Book-To-Comics
- #### Flow 
    The tool provides users to generate corresponding pictures of their stories. 
    
    The picture shown below is a simple flow of how book-to-comics works.
    - #### Flow Chart
        ![image](/book%20to%20comic%20flow.png)
    - #### Input a Story
        Type a story into the textbox. If you have no idea, you can try the story we provided below or use Chat with AI to generate some stories. 
    - #### Prompt Setting 
        After you entered your story, the story cutter will generate several prompts according to the story. 
        
        The message below is how we ask text generator to cut the story into prompts.
        ```python
        message: f"""
        can you cut list of prompt in the message to describe the image how to look like,
        return like ['...' , '...' , ...], message is {message}
        """
        ```
    - #### Image Generation
        While the image generator get the prompts from story cutter, the image generator will generate corresponding image for each prompt.
    
    Finally, you can see your story turn into pictures and narrations, or more precisely, a picture/comic book.

### 2. Chat with AI
In the Chat with AI, you can communicate with the AI just like using ChatGPT. 

In our project, we use a tool called 'g4f' to perform tasks similar to ChatGPT's functions, but without the need to host an LLM on our server.

The command to call `g4f` is showned below:
```python
import g4f
```
> **Warning:** `g4f` is only allowed for research or educational purposes and must not be used for commercial purposes.

- #### Long reaction time issue
    While using the `g4f` library, we have observed that the response is very slow, and it is also quite easy to trigger HTTP timeout issues.

    Without using asynchronously method to send request:
    
    ![image](/long%20reaction%20time%20origin.png)

    We found using the async method can speed up the response.

    Using asynchronously method to send request:
    
    ![image](/long%20reaction%20time%20improve.png)

## Example Story
<!-- ## Example Story
```
Once upon a time there was a dear little girl who was loved by every one who looked at her, but most of all by her grandmother, and there was nothing that she would not have given to the child. Once she gave her a little cap of red velvet, which suited her so well that she would never wear anything else. So she was always called Little Red Riding Hood.

One day her mother said to her, "Come, Little Red Riding Hood, here is a piece of cake and a bottle of wine. Take them to your grandmother, she is ill and weak, and they will do her good. Set out before it gets hot, and when you are going, walk nicely and quietly and do not run off the path, or you may fall and break the bottle, and then your grandmother will get nothing. And when you go into her room, don't forget to say, good-morning, and don't peep into every corner before you do it."
``` -->
Story reference: https://americanliterature.com/childrens-stories/little-red-riding-hood

<!-- 
```python 
import g4f
``` -->

