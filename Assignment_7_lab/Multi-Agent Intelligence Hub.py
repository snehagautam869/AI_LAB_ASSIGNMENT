# Multi-Agent Intelligence Hub

agent_registry = {
    "Agent_Alpha": {
        "Location": (10, 20),
        "Knowledge": {"grid_map", "comm_protocol", "telemetry_sync"}
    },

    "Agent_Beta": {
        "Location": (15, 5),
        "Knowledge": {"grid_map", "comm_protocol", "power_grid"}
    },

    "Agent_Gamma": {
        "Location": (0, 0),
        "Knowledge": {"grid_map", "comm_protocol", "power_grid", "telemetry_sync"}
    }
}


# Find knowledge common to all agents
def find_common_intelligence(registry):
    knowledge_sets = []

    for data in registry.values():
        knowledge_sets.append(data["Knowledge"])

    return set.intersection(*knowledge_sets)


common = find_common_intelligence(agent_registry)

print("--- Common Intelligence Across All Agents ---")
print(common)


# Movement log
movement_log = {}


def relocate_agent(registry, log, agent_id, new_location):

    old_location = registry[agent_id]["Location"]

    print("Trying to change the old location tuple...")

    try:
        old_location[0] = new_location[0]

    except TypeError:
        print("TypeError caught!")
        print("Tuple cannot be changed, so we will create a new tuple.")

    # Change complete Location value
    registry[agent_id]["Location"] = new_location

    # Store movement
    log.setdefault(agent_id, [])
    log[agent_id].append(new_location)

    print("New state:", registry[agent_id])
    print("Movement Log:", log)


print("\n--- Relocating Agent_Alpha ---")

relocate_agent(
    agent_registry,
    movement_log,
    "Agent_Alpha",
    (12, 22)
)


print("\n--- Relocating Agent_Alpha Again ---")

relocate_agent(
    agent_registry,
    movement_log,
    "Agent_Alpha",
    (14, 25)
)


# Summary report
summary_report = {
    agent_id: len(data["Knowledge"])
    for agent_id, data in agent_registry.items()
}

print("\n--- Summary Report ---")
print(summary_report)
