from langgraph.agents import MultiAgentManager

def simulate_multi_agent():
    agents = {
        "content_fetcher": lambda data: f"Fetched content based on {data}.",
        "content_ranker": lambda data: f"Ranked content based on {data}.",
    }

    manager = MultiAgentManager(agents)
    result = manager.run(initial_data="AI and Data Science")
    return result
