import uuid
from datetime import datetime

class HistoryService:
    _history_storage = []

    @classmethod
    def save_attempt(cls, data):
        """
        Saves an attempt to the in-memory list.
        data: dict containing equations, initial_vector, solution, error, graph, etc.
        """
        attempt_id = str(uuid.uuid4())
        
        document = {
            "id": attempt_id,
            "timestamp": datetime.utcnow(),
            "equations": data.get('equations'),
            "initial_vector": data.get('initial_vector'),
            "relaxation_factor": data.get('relaxation_factor'),
            "tolerance": data.get('tolerance'),
            "max_iter": data.get('max_iter'),
            "solution": data.get('solution'),
            "iterations": data.get('iterations'),
            "error": data.get('error'),
            "history": data.get('history'),
            "graph": data.get('graph') # Base64 string
        }
        
        cls._history_storage.append(document)
        return attempt_id

    @classmethod
    def get_history(cls):
        """
        Returns a list of attempts (summary).
        """
        # Sort by timestamp descending
        sorted_history = sorted(cls._history_storage, key=lambda x: x['timestamp'], reverse=True)
        
        history_summary = []
        for doc in sorted_history:
            history_summary.append({
                "id": doc['id'],
                "timestamp": doc['timestamp'].isoformat(),
                "error": doc.get('error'),
                "iterations": doc.get('iterations')
            })
            
        return history_summary

    @classmethod
    def get_attempt(cls, attempt_id):
        """
        Returns full details of an attempt.
        """
        for doc in cls._history_storage:
            if doc['id'] == attempt_id:
                # Return a copy to avoid mutation if necessary, 
                # but for read-only views it's fine.
                # We need to format timestamp for JSON response
                response_doc = doc.copy()
                response_doc['timestamp'] = response_doc['timestamp'].isoformat()
                return response_doc
        return None
