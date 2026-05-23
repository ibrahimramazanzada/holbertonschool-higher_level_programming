-- creates column avg of score
UPDATE second_table SET average = (SELECT AVG(score) FROM second_table);
