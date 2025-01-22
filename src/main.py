from crewai import Agent, Task, Crew
from typing import List

class SupportCrew:
    def __init__(self, support_adapter, knowledge_connector):
        self.support_adapter = support_adapter
        self.knowledge_connector = knowledge_connector
        self.crew = self._create_crew()
    
    def _create_agents(self) -> List[Agent]:
        ticket_analyzer = Agent(
            name="Ticket Analyzer",
            goal="Analyze and classify support tickets",
            backstory="Expert at understanding support tickets and their requirements",
            tools=[self.support_adapter.get_tickets]
        )
        
        resolution_predictor = Agent(
            name="Resolution Predictor",
            goal="Predict optimal resolution paths based on historical patterns",
            backstory="Specialist in pattern recognition and solution prediction",
            tools=[self.support_adapter.get_tickets]
        )
        
        knowledge_navigator = Agent(
            name="Knowledge Navigator",
            goal="Find relevant documentation and knowledge articles",
            backstory="Expert at searching and retrieving relevant documentation",
            tools=[self.knowledge_connector.search_articles]
        )
        
        ticket_scraper = Agent(
            name="Ticket Scraper",
            goal="Retrieve detailed ticket history and related web content",
            backstory="Specialist in extracting ticket information and related web content",
            tools=[
                self.support_adapter.get_ticket_details,
                self.support_adapter.scrape_ticket_logs,
                self.support_adapter.scrape_related_content
            ]
        )
        
        return [ticket_analyzer, resolution_predictor, knowledge_navigator, ticket_scraper]
    
    def _create_crew(self) -> Crew:
        agents = self._create_agents()
        return Crew(
            agents=agents,
            tasks=self._define_tasks(agents)
        )
    
    def _define_tasks(self, agents: List[Agent]) -> List[Task]:
        tasks = [
            Task(
                description="Analyze new support tickets",
                agent=agents[0]
            ),
            Task(
                description="Scrape ticket history and related content",
                agent=agents[3],
                context="Gather detailed ticket logs and any referenced web content"
            ),
            Task(
                description="Predict resolution paths",
                agent=agents[1]
            ),
            Task(
                description="Find relevant documentation",
                agent=agents[2]
            )
        ]
        return tasks 