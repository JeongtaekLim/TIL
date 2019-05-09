# Create updated column
```
CREATE TABLE orders(
  id INT NOT NULL AUTO_INCREMENT,
  user_id INT NULL,
  amount FLOAT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE now(),
  PRIMARY KEY(id)
);
Query OK, 0 rows affected (0.02 sec)
```