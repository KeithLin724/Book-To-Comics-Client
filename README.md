# A study of Text-to-image
## Written By 練鈞揚, 連文聖

---
## Setup
> Please look here [Setup.md](./setup.md)

---
## Demo Video
[![Video](https://img.youtube.com/vi/c06yysTPTJQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=c06yysTPTJQ)

---
## Information about the project 
- ### Why we created this tool? 
  - Artificial intelligence (AI) techniques have progressed rapidly in recent years. As university students, AI tools are part of our life. 
  
    While searching our project topic, we discovered that many people have not used text-to-image tools before or unaware of them. 
    
    Therefore, we developed this tool to introduce people text-to-image techniques, expecting to make more individuals aware of the powerful tool.
- ### What are the functions of this tool?
  - In our project, we provide a tool which can be used to display pictures of the corresponding to the prompts from stories users provided. 
   
    Furthermore, we build a user friendly page where users can chat with AI. 
    
    This setup allows users to utilize the tools more conveniently, eliminating the need to open multiple screens.

---

## About the Project Technique
### 1. Book-To-Comics
- #### Flow 
    The tool provides users to generate corresponding pictures of their stories. 
    
    The picture shown below is a simple flow of how book-to-comics works.
    - #### Flow Chart
        ![image](/assets/project/book_to_comics-Flow-chat.png)
    - #### Input a Story
        Type a story into the textbox. If you have no idea, you can try the story we provided below or use Chat with AI to generate some stories. 
    - #### Prompt Setting 
        After you entered your story, the story cutter will generate several prompts according to the story. 
        
        The message below is how we ask text generator to cut the story into prompts.
        ```python
        message: f"""
        Given an image, I need your help to generate a clear list of prompts describing how the image looks.
        The prompts should be in list format. 
        Please use the information in the provided message {message} to craft the prompts.
        Return your responses in the format ['...', '...', ...]. Be as detailed and imaginative as possible. 
        Thank you!
        """
        ```
    - #### Image Generation
        While the image generator get the prompts from story cutter, the image generator will generate corresponding image for each prompt.
    
    Finally, you can see your story turn into pictures and narrations, or more precisely, a picture/comic book.

### 2. Chat with AI
In the Chat with AI, you can communicate with the AI just like using ChatGPT. 

In our project, we use a tool called 'g4f' to perform tasks similar to ChatGPT's functions, but without the need to host an LLM on our server.

The command to call `g4f` is show in below:
```python
import g4f
```
> **Warning:** `g4f` is only allowed for research or educational purposes and must not be used for commercial purposes.
> [More detail](https://github.com/xtekky/gpt4free)

- #### Long reaction time issue
    While using the `g4f` library, we have observed that the response is very slow, and it is also quite easy to trigger HTTP timeout issues.

    Without using asynchronously method to send request:
    
    ![image](/assets/project/book_to_comics-chat.png)

    We found using the async method can speed up the response.

    Using asynchronously method to send request:
    
    ![image](/assets/project/book_to_comics-chat-speed%20up.png)


## Example Story
```
Once upon a time there was a dear little girl who was loved by every one who looked at her, but most of all by her grandmother, and there was nothing that she would not have given to the child. Once she gave her a little cap of red velvet, which suited her so well that she would never wear anything else. So she was always called Little Red Riding Hood.

One day her mother said to her, "Come, Little Red Riding Hood, here is a piece of cake and a bottle of wine. Take them to your grandmother, she is ill and weak, and they will do her good. Set out before it gets hot, and when you are going, walk nicely and quietly and do not run off the path, or you may fall and break the bottle, and then your grandmother will get nothing. And when you go into her room, don't forget to say, good-morning, and don't peep into every corner before you do it."
```
Story reference: [here](https://americanliterature.com/childrens-stories/little-red-riding-hood)

> More Story example: [here](https://gist.github.com/KeithLin724/b5b2688ca626e92432e292929e47d05d)

---

## Server Technque
- #### Project App Architecture
  The picture below illustrates the architecture of our project app. For the client part, we use Reflex to build the pages. For the server part, we utilize FastAPI.
  
  ![image](/assets/project/book_to_comics-app.png)

- #### Handle Process Image Traffic Problem
  When the client requests the server to process a long-time task, the server will enqueue the job in Redis, returning a task ID. After the Redis queue completes the job, it will store the results in the Redis database, awaiting the client to retrieve the results.

  ![image](/assets/project/book_to_comics-Task%20Queue.png)

- #### Client Fetch Data
  After the Redis queue receives the job, the client will use the task ID to query the job status or result if the job is completed. If the job is completed, it will be stored in the database. When the task ID is in Redis, it will return the result to the client.

  ![image](/assets/project/book_to_comics-fetch%20data.png)

- #### Micro Service
  Normally, if a server wants to add new services, it will shut down, add the code for the new services, and then turn on the server. This process can cause interruptions in the server service.
  
  To mitigate these issues, integrate services from the main server, extract them, and divide them into independent services that solely provide services to the main server. This approach, known as microservices, enables us to easily add or remove services without disrupting the overall system.

  ![image](/assets/project/book_to_comics-micro%20service%20connect.png)

---

## Appendix
### ChatGPT
- #### What is ChatGPT
  ChatGPT is a tool that will attempt to understand the hints you provide and, based on its training results, generate sentences that best match the possible answer.

  You can use it to answer questions, write copies, draft mails, explain code, and so on. In summary, it is a powerful tool that can greatly enhance our life.

- #### How does ChatGPT work?
  The full name of GPT is Generative Pre-trained Transformer. From its name, we can easily learn that the key to GPT is the letter 'P', which stands for 'Pre-trained', and the letter 'T', which similarly stands for 'Transformer'.

  ![image](/assets/project/GPT3_flow_chart.jpeg)

  > Resource: [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

  - #### Pre-trained
    GPT is given some basic rules and a huge amount of unmarked data, which may contain almost the entirety information of the internet. Then, it processes this data in an unsupervised state, developing its own rules and relationships between the texts.
    
  - #### Transformer
    The main idea behind the Transformer is a process called 'self-attention'. Older networks, such as RNNs, read sentences from left to right. However, the Transformer reads all words in the sentence at once, allowing it to focus its attention on the most relevant word.
    
    Below is an image of the Transformer's model architecture.

    ![image](/assets/project/Transformer.png)

    > For more information about transformer, please visit: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

### Stable diffusion
- #### What is Stable diffusion?
    Stable diffusion is a text-to-image model. Before stable diffusion, there are already several models such as Generative Adversarial Networks (GANs), AutoRegressive Models (ARM), Variation AutoEncoder (VAEs), which can be used to generate images. However, these models have high computational cost.

- #### How does stable diffusion work?
    Recently, diffusion probabilistic models built from a hierarchy of denoising autoencoders have been able to generate impressive high-quality images.

    The picture below shows how stable diffusion works. First, an autoencoder is needed, which contains an encoder and decoder. The encoder compresses the image into a latent space, and the low-dimensional data is used to execute the diffusion process. Finally, the decoder decompresses the image back to the high-dimensional space. This process is called 'Perceptual Compression'.

    ![image](/assets/project/stable_diffusion.png)

    > Resource: [Latent Diffusion Models (Github)](https://github.com/CompVis/latent-diffusion)

--- 
## Tools 

[ <img src="https://www.python.org/static/community_logos/python-powered-w.svg" alt="Python"  height="50"> ](https://www.python.org/)
[ <img src="https://logosmarcas.net/wp-content/uploads/2021/03/Docker-Logo.png" alt="Docker"  height="50"> ](https://www.docker.com/)
[ <img src="https://www.logo.wine/a/logo/Redis/Redis-Logo.wine.svg" alt="Redis"  height="50"> ](https://redis.io/)
[ <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"  height="50"> ](https://fastapi.tiangolo.com/)
[ <img src="https://th.bing.com/th/id/OIP.UP5P6iEpL1u0VfOXC52rTwHaCv?rs=1&pid=ImgDetMain" alt="Hugging Face"  height="50"> ](https://huggingface.co/)
[ <img src="https://raw.githubusercontent.com/reflex-dev/reflex/main/docs/images/reflex_light.svg#gh-dark-mode-only" alt="Reflex"  height="50"> ](https://reflex.dev/)
[ <img src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.svg" alt="Git"  height="50"> ](https://git-scm.com/)
[ <img src="https://storage.ko-fi.com/cdn/useruploads/63f85360-cf6c-43e7-b9a7-6e97b5f09488_png_fdc7b0ca-92fb-4c2d-82e0-60798794bb38cover.png" alt="g4f"  height="50"> ](https://github.com/xtekky/gpt4free)


