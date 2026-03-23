create database if not exists P3793;
use P3793;

CREATE TABLE if not exists prompts (
    user_id INT,
    prompt VARCHAR(255),
    tokens INT
);

Truncate table prompts;
insert into prompts (user_id, prompt, tokens)
values ('1', 'Write a blog outline', '120');
insert into prompts (user_id, prompt, tokens)
values ('1', 'Generate SQL query', '80');
insert into prompts (user_id, prompt, tokens)
values ('1', 'Summarize an article', '200');
insert into prompts (user_id, prompt, tokens)
values ('2', 'Create resume bullet', '60');
insert into prompts (user_id, prompt, tokens)
values ('2', 'Improve LinkedIn bio', '70');
insert into prompts (user_id, prompt, tokens)
values ('3', 'Explain neural networks', '300');
insert into prompts (user_id, prompt, tokens)
values ('3', 'Generate interview Q&A', '250');
insert into prompts (user_id, prompt, tokens)
values ('3', 'Write cover letter', '180');
insert into prompts (user_id, prompt, tokens)
values ('3', 'Optimize Python code', '220');

select user_id, count(*) prompt_count, round(avg(tokens), 2) avg_tokens
from prompts
group by user_id
having prompt_count >= 3 and max(tokens) > avg(tokens)
order by avg_tokens desc, prompt_count;