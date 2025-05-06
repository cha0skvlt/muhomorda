-- Таблица пользователей (если понадобится в будущем)
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица постов (история отправленных)
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица тем/грибов для генерации
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    enabled BOOLEAN DEFAULT 1
);
