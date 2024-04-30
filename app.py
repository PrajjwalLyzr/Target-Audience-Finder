import os
from PIL import Image
import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger
from dotenv import load_dotenv; load_dotenv()
from utils import utils

# Setup your config
utils.page_config()
utils.style_app()

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Target Audience Finder")
st.markdown("### Welcome to the Target Audience Finder by Lyzr!")
st.markdown("This app helps you to find the target audience based on Demographics, Interests and their Behaviour for marketing Campaign !!!")



# replace this with your openai api key or create an environment variable for storing the key.
API_KEY = os.getenv('OPENAI_API_KEY')

 

open_ai_model_text = OpenAIModel(
    api_key= API_KEY,
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.5,
        "max_tokens": 1500,
    },
)

def Target_Audience_Finder(product_service):
    
    content_strategy_analyst = Agent(
        prompt_persona="""You are a Content Strategy Analyst expert who are expert to find the target audience based on their Demographics, Interests, and Behaviour for marketing campaign.""",
        role="Content Strategy Analyst", 
    )

    audience_finder =  Task(
        name="Audience Finder",
        agent=content_strategy_analyst,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model_text,
        instructions=f"Use the description provided, Describe the ideal target audience for a content marketing campaign, including demographics, interests, and behaviors for {product_service}, [!Important] Avoid Introduction and conclusion from the response, just provide the Demographics, Interests and Behaviour",
        log_output=True,
        enhance_prompt=False,
        default_input=product_service
    )


    logger = Logger()
    

    main_output = LinearSyncPipeline(
        logger=logger,
        name="Target Audience Finder",
        completion_message="App Generated all things!",
        tasks=[
            audience_finder,
        ],
    ).run()

    return main_output


if __name__ == "__main__":
    product_services = st.text_input("Write about your product or services")
    
    if product_services == '':
        st.warning('Specific product or service for the marketing campaign was not provided in your input')

    button=st.button('Submit')
    if (button==True):
        generated_output = Target_Audience_Finder(product_service=product_services)
        output = generated_output[0]['task_output']
        st.write(output)
        st.markdown('---')
   
    utils.template_end()