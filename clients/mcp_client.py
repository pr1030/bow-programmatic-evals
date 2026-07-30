import asyncio
import json
import time
import httpx

import asyncio
import time
import httpx

from mcp.client.streamable_http import streamable_http_client
from mcp.client.session import ClientSession

from core.arrange import arrange
from core.runner import run_tests
from core.summary import print_summary

# Replace with your API key
API_KEY = "bow_lTHUcS9mtBZ4S0Uzvfsix5HxxShPo5uyP-dDuzlMyrY"

# MCP endpoint
MCP_URL = "http://localhost:3000/api/mcp"


async def main():

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    async with httpx.AsyncClient(headers=headers) as http_client:

        async with streamable_http_client(
            MCP_URL,
            http_client=http_client,
        ) as (read_stream, write_stream, _):

            async with ClientSession(read_stream, write_stream) as session:

                print("Initializing...")
                await session.initialize()
                print("Connected!")

                start_time = time.perf_counter()

                # -----------------------------
                # Arrange
                # -----------------------------
                report_id, test_cases = await arrange(session)

                # -----------------------------
                # Act + Assert
                # -----------------------------
                results = await run_tests(
                    session,
                    report_id,
                    test_cases
                )

                execution_time = time.perf_counter() - start_time

                # -----------------------------
                # Summary
                # -----------------------------
                print_summary(
                    results,
                    execution_time
                )


if __name__ == "__main__":
    asyncio.run(main())