from typing import Any, Optional
from smolagents.tools import Tool
from smolagents.agent_types import AgentImage
from PIL import Image

class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "Provides a final answer to the given problem. Can handle text, images, and other data types."
    inputs = {'answer': {'type': 'any', 'description': 'The final answer to the problem'}}
    output_type = "any"

    def forward(self, answer: Any) -> Any:
        # If it's already an AgentImage, return it
        if isinstance(answer, AgentImage):
            return answer
            
        # If it's a PIL Image, wrap it in AgentImage
        if isinstance(answer, Image.Image):
            return AgentImage(answer)
        
        # For other types, return as-is
        return answer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_initialized = False