# Debate Crew

Welcome to the Debate Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/debate/config/agents.yaml` to define your agents
- Modify `src/debate/config/tasks.yaml` to define your tasks
- Modify `src/debate/crew.py` to add your own logic, tools and specific args
- Modify `src/debate/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the debate Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The debate Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Debate Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## FOR WINDOWS USERS: Possibility to work with uv and CrewAI on a Conda or Mamba environment

I was able to develop  this project using a Mamba environment with Python 3.12, and a huge recommendation is to create your *.venv* file pointing to your python from your mamba environment.

1) For Windows, run in the cmd:

```bash
where python
```

2) Extract the path for the *python.exe* asociated to the Mamba/Conda environment you're working on (remember to activate it).

3) Add this path on the following uv command:

```bash
uv venv -p C:\Users\jsmith\.local\share\mamba\envs\crewai_env\python.exe
```

*Please notice that crewai_env is the mamba environment I created*

4) Then connect to this new environemnt (CMD):

```bash
.venv\Scripts\activate
```

5) You should be close to ready for running `crewai run` command, but first is really recommendable (and sometimes really problem solving) to run this following command first:

```bash
uv sync
``` 

