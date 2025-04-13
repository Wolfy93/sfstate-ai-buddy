**📦 Data Model for SFSU AI Chatbot Web App**

---

### 1. Users

Stores authenticated SFSU students and optionally guest users.

```json
{
  "user_id": "uuid",
  "email": "student@sfsu.edu",
  "auth_provider": "google" | "email_password" | "guest",
  "role": "student" | "admin" | "guest",
  "name": "Jane Doe",
  "created_at": "2025-04-12T09:00:00Z",
  "last_login": "2025-04-12T11:00:00Z",
  "preferences": {
    "theme": "dark",
    "language": "en-US"
  }
}
```

---

### 2. Conversations

Each chat session between a user and the AI.

```json
{
  "conversation_id": "uuid",
  "user_id": "uuid",
  "title": "How to get a locker at SFSU?",
  "created_at": "2025-04-12T09:01:00Z",
  "updated_at": "2025-04-12T09:05:00Z",
  "status": "active" | "archived",
  "folder_id": "uuid",
  "tags": ["locker", "facilities"],
  "summary": "Chat about locker availability, cost, and key process",
  "context_config": {
    "model": "gpt-4",
    "temperature": 0.2,
    "retrieval_enabled": true,
    "retrieved_sources": 5
  }
}
```

---

### 3. Messages

Core unit of each conversation, including AI and user content.

```json
{
  "message_id": "uuid",
  "conversation_id": "uuid",
  "sender": {
    "type": "user" | "assistant" | "system",
    "id": "uuid",
    "name": "Jane"
  },
  "content": "How much does a locker cost on campus?",
  "timestamp": "2025-04-12T09:01:30Z",
  "reply_to": null,
  "metadata": {
    "format": "markdown",
    "copied": false,
    "bookmarked": true,
    "tags": ["locker", "student-life"],
    "feedback": {
      "thumbs": "up" | "down" | null,
      "comment": "Helpful!"
    },
    "rag": {
      "enabled": true,
      "sources": [
        {
          "url": "https://sfsu.edu/lockers",
          "title": "Locker Rental Policy",
          "confidence": 0.94,
          "snippet": "Lockers cost $15 per semester and are available at the Student Center..."
        }
      ]
    },
    "tool_call": {
      "type": "search" | "calendar_lookup" | "insight_inject",
      "status": "success",
      "latency_ms": 842
    }
  }
}
```

---

### 4. Threads (optional for reply trees)

```json
{
  "thread_id": "uuid",
  "parent_message_id": "uuid",
  "conversation_id": "uuid",
  "messages": [
    { "message_id": "uuid", "sender": "user", "content": "..." },
    { "message_id": "uuid", "sender": "assistant", "content": "..." }
  ]
}
```

---

### 5. Folders

To organize user conversations like a file manager.

```json
{
  "folder_id": "uuid",
  "user_id": "uuid",
  "name": "Campus Life",
  "created_at": "2025-04-12T09:00:00Z",
  "color": "#FFD700"
}
```

---

### 6. Actions / Analytics Log

Track user actions on messages.

```json
{
  "action_id": "uuid",
  "message_id": "uuid",
  "user_id": "uuid",
  "type": "copy" | "like" | "tag" | "share" | "followup_triggered",
  "timestamp": "2025-04-12T09:05:10Z",
  "details": {
    "tag_name": "fees",
    "copied_to_clipboard": true
  }
}
```

---

### 7. RAG Sources (Optional but extensible)

Keep a cache of source documents used in retrieval.

```json
{
  "source_id": "uuid",
  "url": "https://sfsu.edu/policies/locker",
  "title": "Locker Rental Policy",
  "content_excerpt": "Lockers are issued on a first-come, first-serve basis...",
  "domain": "sfsu.edu",
  "last_scraped": "2025-04-10T12:00:00Z"
}
```

---

### Future Additions

- Event Tracker
- Campus Marketplace Listings
- Student Verification via SFSU OAuth
- Discord/Instagram community index
- Notification preferences

---


