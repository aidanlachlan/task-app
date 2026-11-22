import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from fastmcp import FastMCP
from core import tasks

mcp = FastMCP("Task App")

@mcp.tool
def list_tasks(status: str = "todo") -> list:
    """List tasks by status: "todo", "done" or "all"."""
    return tasks.list_tasks(status)

@mcp.tool
def add_task(title: str, priority: str="medium", due: str | None = None):
    """Add a task. Priority is low, medium or high. Due date must be an ISO date or omitted."""
    return tasks.add_task(title, priority, due)
    
@mcp.tool()
def complete_task(id: int) -> dict:
    """Mark the task with this id as done."""
    return tasks.complete_task(id)
    
@mcp.tool()
def delete_task(id: int) -> int:
    """Delete the task with this id."""
    return tasks.delete_task(id)
    
mcp.run()