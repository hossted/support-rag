from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseSupportAdapter(ABC):
    """Base class for support platform integrations."""
    
    @abstractmethod
    async def get_tickets(self, **kwargs) -> List[Dict[str, Any]]:
        """Retrieve tickets from the platform."""
        pass
    
    @abstractmethod
    async def update_ticket(self, ticket_id: str, data: Dict[str, Any]) -> bool:
        """Update a ticket with new information."""
        pass
    
    @abstractmethod
    async def add_comment(self, ticket_id: str, comment: str) -> bool:
        """Add a comment to a ticket."""
        pass

class BaseKnowledgeConnector(ABC):
    """Base class for knowledge base integrations."""
    
    @abstractmethod
    async def search_articles(self, query: str) -> List[Dict[str, Any]]:
        """Search for relevant articles."""
        pass
    
    @abstractmethod
    async def get_article_content(self, article_id: str) -> str:
        """Retrieve full content of an article."""
        pass 