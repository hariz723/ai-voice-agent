from click.termui import prompt
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    google,
    noise_cancellation,
)

# local imports
from constants import load_environment
import prompt as agent_prompt


load_environment()


class Assistant(Agent):
    def __init__(self) -> None:
        """
        Initializes the Assistant object.

        This method is called when the Assistant object is created. It calls the
        constructor of the parent class, passing in an instruction string as an
        argument. The instruction string is used to set the initial state of the
        agent.

        The instruction string is as follows:
        You are a helpful voice AI assistant.
        """
        super().__init__(instructions=agent_prompt.AGENT_PROMPT) # type: ignore


async def entrypoint(ctx: agents.JobContext):
    """
    This is the entry point for the agent. It is called when the agent is started,
    and it is responsible for setting up the agent's state and starting the agent's
    main loop.

    This function takes a `JobContext` object as an argument, which contains
    information about the job that the agent is running in.

    The function returns a coroutine that performs the following steps:

    1. Creates an `AgentSession` object, which is used to manage the agent's state
       and interactions with the user.
    2. Calls the `start` method on the `AgentSession` object, passing in the
       `JobContext` object and the `Assistant` object as arguments. This starts the
       agent's main loop and begins listening for user input.
    3. Calls the `generate_reply` method on the `AgentSession` object, passing in
       an instruction string as an argument. This sends a reply to the user based
       on the instruction string.

    The function does not return a value.
    """
    session = AgentSession(
    llm=google.beta.realtime.RealtimeModel(
        model="gemini-2.0-flash-exp",
        voice="Puck",
        temperature=0.8,
        instructions=agent_prompt.AGENT_PROMPT,
    ),
)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` instead for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions=agent_prompt.AGENT_RESPONSE_PROMPT
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))