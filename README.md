# Debate Challenge | Gemini-2.0-flash vs. GPT-5-nano

This is a customized Debate agent from an [Agentic AI Udemy course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/?srsltid=AfmBOoqWwA_Ja04s6gKZgCrD87nAeo5gzqASLcFFjzoHcAUcXM2S6gHq&couponCode=KEEPLEARNINGOCTA) dictated by Ed Donner which is based on the one developed on this [repo](https://github.com/ed-donner/agents/tree/main/3_crew/debate/src/debate), but with with some subtle changes:

1) Here we put to compete LLMs from 2 of the most cutting-edge companies in AI development, Google with Gemini-2.0-flash and OpenAI with GPT-5-nano.
2) We use as a judge a reasoning LLM (or SLM as its classified in some forums) which is Phi-4-reasoning, deployed from Azure AI Foundry.
3) We define the LLMs used on the crew.py file in a different manner from the project we based for this.
4) There is an example of how to define a LLM which was raised from Azure AI Foundry (because is not that easy as you may think). 
