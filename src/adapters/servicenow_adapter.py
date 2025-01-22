from core.base_adapters import BaseSupportAdapter
from typing import List, Dict, Any
import aiohttp
import json
import base64

class ServiceNowAdapter(BaseSupportAdapter):
    def __init__(self, instance_url: str, username: str, password: str):
        """
        Initialize ServiceNow adapter
        
        Args:
            instance_url: Your ServiceNow instance URL (e.g., 'https://your-instance.service-now.com')
            username: ServiceNow username
            password: ServiceNow password
        """
        self.instance_url = instance_url.rstrip('/')
        self.auth = base64.b64encode(
            f"{username}:{password}".encode()
        ).decode()
        self.headers = {
            'Authorization': f'Basic {self.auth}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    async def get_tickets(self, **kwargs) -> List[Dict[str, Any]]:
        """
        Retrieve tickets (incidents) from ServiceNow
        
        Kwargs:
            limit: Maximum number of tickets to retrieve
            query: Encoded query string for filtering
            active: Only retrieve active tickets
        """
        limit = kwargs.get('limit', 10)
        query = kwargs.get('query', '')
        
        endpoint = f"{self.instance_url}/api/now/table/incident"
        params = {
            'sysparm_limit': limit,
            'sysparm_query': query,
            'sysparm_display_value': 'true'
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('result', [])
                else:
                    error_msg = await response.text()
                    raise Exception(f"Failed to get tickets: {error_msg}")

    async def update_ticket(self, ticket_id: str, data: Dict[str, Any]) -> bool:
        """
        Update a ServiceNow incident
        
        Args:
            ticket_id: System ID of the incident
            data: Dictionary containing fields to update
        """
        endpoint = f"{self.instance_url}/api/now/table/incident/{ticket_id}"
        
        async with aiohttp.ClientSession() as session:
            async with session.patch(endpoint, headers=self.headers, json=data) as response:
                if response.status == 200:
                    return True
                else:
                    error_msg = await response.text()
                    raise Exception(f"Failed to update ticket: {error_msg}")

    async def add_comment(self, ticket_id: str, comment: str) -> bool:
        """
        Add a work note to a ServiceNow incident
        
        Args:
            ticket_id: System ID of the incident
            comment: Work note content
        """
        update_data = {
            'work_notes': comment
        }
        
        return await self.update_ticket(ticket_id, update_data)

    async def get_ticket_details(self, ticket_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific incident
        
        Args:
            ticket_id: System ID of the incident
        """
        endpoint = f"{self.instance_url}/api/now/table/incident/{ticket_id}"
        params = {
            'sysparm_display_value': 'true'
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint, headers=self.headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('result', {})
                else:
                    error_msg = await response.text()
                    raise Exception(f"Failed to get ticket details: {error_msg}") 