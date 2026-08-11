from crewai.tools import BaseTool
import pypdf

class ResumeReaderTool(BaseTool):
    name: str = "Resume File Reader"
    description: str = "Reads a PDF resume file at a given path and returns its raw text content"

    def _run(self, file_path: str) -> str:
        reader = pypdf.PdfReader(file_path)
        return "\n".join(page.extract_text() for page in reader.pages)