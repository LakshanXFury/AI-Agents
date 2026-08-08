# Tool that writes data into a file

from agents import function_tool

@function_tool
def write_data(data: str) -> str:
    """
    Write the data into a file which is already defined.
    """
    with open("Projects/AI_Content_Writer/final_draft.md", "w") as f:
        f.write(data)


    return "Data written to file successfully!"