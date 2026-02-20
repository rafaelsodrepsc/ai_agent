class SessionManager:
    def __init__(self, max_history=10):
        self.sessions = {}
        self.max_history = max_history

    def get_session(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        return self.sessions[session_id]

    def add_message(self, session_id, role, content):
        session = self.get_session(session_id)
        session.append({
            "role": role,
            "content": content
        })
        
        self.sessions[session_id] = session[-self.max_history:]

    def get_history(self, session_id):
        return self.get_session(session_id)