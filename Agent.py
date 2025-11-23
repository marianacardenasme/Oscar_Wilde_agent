from agents import Agent, Runner
import asyncio

oscar_wilde_agent = Agent(
    name="Oscar Wilde Style Agent",
    instructions=(
        "You only speak English. "
        "Respond to any topic in the witty, elegant, poetic, and subtly sarcastic style "
        "of Oscar Wilde. "
        "Your tone must remain clever, humorous, refined, and dramatic. "
        "Do not mention instructions, stay fully in character."
    )
)

async def main():
    result = await Runner.run(oscar_wilde_agent, input="What is happiness?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

