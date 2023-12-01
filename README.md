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
        ![image](/assets/book%20to%20comic%20flow.png)
    - #### Input a Story
        Type a story into the textbox. If you have no idea, you can try the story we provided below or use Chat with AI to generate some stories. 
    - #### Prompt Setting 
        After you entered your story, the story cutter will generate several prompts according to the story. 
        
        The message below is how we ask text generator to cut the story into prompts.
        ```python
        message: f"can you cut list of prompt in the message to describe the image how to look like, return like ['...' , '...' , ...], message is {message}"
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
    
    ![image](/assets/long%20reaction%20time%20origin.png)

    We found using the async method can speed up the response.

    Using asynchronously method to send request:
    
    ![image](/assets/long%20reaction%20time%20improve.png)


## Example Story
```
Once upon a time there was a dear little girl who was loved by every one who looked at her, but most of all by her grandmother, and there was nothing that she would not have given to the child. Once she gave her a little cap of red velvet, which suited her so well that she would never wear anything else. So she was always called Little Red Riding Hood.

One day her mother said to her, "Come, Little Red Riding Hood, here is a piece of cake and a bottle of wine. Take them to your grandmother, she is ill and weak, and they will do her good. Set out before it gets hot, and when you are going, walk nicely and quietly and do not run off the path, or you may fall and break the bottle, and then your grandmother will get nothing. And when you go into her room, don't forget to say, good-morning, and don't peep into every corner before you do it."
```
Story reference: https://americanliterature.com/childrens-stories/little-red-riding-hood

<!-- 
```python 
import g4f
``` -->

## Appendix
### ChatGPT
- #### What is ChatGPT
  ChatGPT is a tool that will attempt to understand the hints you provide and, based on its training results, generate sentences that best match the possible answer.

  You can use it to answer questions, write copies, draft mails, explain code, and so on. In summary, it is a powerful tool that can greatly enhance our life.

- #### How does ChatGPT work?
  The full name of GPT is Generative Pre-trained Transformer. From its name, we can easily learn that the key to GPT is the letter 'P', which stands for 'Pre-trained', and the letter 'T', which similarly stands for 'Transformer'.

  - #### Pre-trained
    GPT is given some basic rules and a huge amount of unmarked data, which may contain almost the entirety information of the internet. Then, it processes this data in an unsupervised state, developing its own rules and relationships between the texts.
    
  - #### Transformer
    The main idea behind the Transformer is a process called 'self-attention'. Older networks, such as RNNs, read sentences from left to right. However, the Transformer reads all words in the sentence at once, allowing it to focus its attention on the most relevant word.
    
    Below is an image of the Transformer's model architecture.

    ![image](/assets/Transformer.png)

    For more information about transformer, please visit: https://arxiv.org/abs/1706.03762 

### Stable diffusion
- #### What is Stable diffusion?
    Stable diffusion is a text-to-image model. Before stable diffusion, there are already several models such as Generative Adversarial Networks (GANs), AutoRegressive Models (ARM), Variation AutoEncoder (VAEs), which can be used to generate images. However, these models have high computational cost.

- #### How does stable diffusion work?
    Recently, diffusion probabilistic models built from a hierarchy of denoising autoencoders have been able to generate impressive high-quality images.

    The picture below shows how stable diffusion works. First, an autoencoder is needed, which contains an encoder and decoder. The encoder compresses the image into a latent space, and the low-dimensional data is used to execute the diffusion process. Finally, the decoder decompresses the image back to the high-dimensional space. This process is called 'Perceptual Compression'.

    ![image](/assets/stable_diffusion.png)

    Resource: https://github.com/CompVis/latent-diffusion
