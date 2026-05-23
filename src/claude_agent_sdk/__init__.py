"""Claude Agent SDK - A Python SDK for building agents with Claude.

This is a fork of anthropics/claude-agent-sdk-python with additional
features and improvements for agent-based workflows.

Fork notes:
- Added ConversationMemory to public API for easier stateful agent workflows
"""

from __future__ import annotations

__version__ = "0.1.0"
__author__ = "Claude Agent SDK Contributors"
__license__ = "MIT"

from claude_agent_sdk.client import ClaudeAgentClient
from claude_agent_sdk.agent import Agent
from claude_agent_sdk.memory import ConversationMemory
from claude_agent_sdk.types import (
    AgentConfig,
    Message,
    MessageRole,
    ToolDefinition,
    ToolResult,
)
from claude_agent_sdk.exceptions import (
    ClaudeAgentError,
    AuthenticationError,
    RateLimitError,
    ToolExecutionError,
    AgentTimeoutError,
)

__all__ = [
    # Core classes
    "ClaudeAgentClient",
    "Agent",
    "ConversationMemory",
    # Types
    "AgentConfig",
    "Message",
    "MessageRole",
    "ToolDefinition",
    "ToolResult",
    # Exceptions
    "ClaudeAgentError",
    "AuthenticationError",
    "RateLimitError",
    "ToolExecutionError",
    "AgentTimeoutError",
    # Version
    "__version__",
]
