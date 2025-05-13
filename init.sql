CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  refresh_token TEXT
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  color TEXT,
  user_id INT REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE expenses (
  id SERIAL PRIMARY KEY,
  amount DECIMAL NOT NULL,
  description TEXT,
  date DATE NOT NULL,
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  category_id INT NOT NULL REFERENCES categories(id) ON DELETE CASCADE
);

CREATE TABLE fixed_expenses (
  id SERIAL PRIMARY KEY,
  amount DECIMAL NOT NULL,
  description TEXT,
  frequency TEXT, 
  user_id INT REFERENCES users(id) ON DELETE CASCADE,
  category_id INT NOT NULL REFERENCES categories(id) ON DELETE CASCADE

);
