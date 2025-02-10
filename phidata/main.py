from phi.agent import Agent, RunResponse
from phi.model.ollama import Ollama

agent = Agent(
    model=Ollama(id="qwen2.5-coder:7b"),
    markdown=True
)

# Get the response in a variable
run: RunResponse = agent.run("Share a 2 sentence horror story.")
print(run)
print(run.content)

# Print the response in the terminal
# agent.print_response("Share a 2 sentence horror story.")