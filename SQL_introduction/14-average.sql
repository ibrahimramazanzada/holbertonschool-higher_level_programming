-- creates column avg of score
ALTER TABLE second_table ADD average FLOAT;
UPDATE second_table SET average = (SELECT AVG(score) FROM second_table);
