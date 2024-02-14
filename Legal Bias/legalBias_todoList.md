* Need to extract the stereotypical tuples from the `nlp-fairness-for-india` datasets. ----> `Done`

* Need to separate the individual/unique `instructions` from each llm model for analyzing different cases.  

* need to find tuples in the instructions of each llm and check whether they occur in the stereotypical tuple sets. 

* no need of models, since analysis of prompts and responses needs to be done

* analysis is very dry for this

* better to serach for the stereotypical nature in these responses

# End Goal
* Your task is to analyze the prompts and true verdicts given and find patterns
    in the prompts and insights into how the prompts are distributed. Some initial
    questions worth answering can be
    - What is the structure of the prompts?
    - On what criteria are the prompts changing within the files?
    - What are the different actions, identity terms and genders used?

c. Bonus Task:
Try to give reasons for why the prompts discussed above were structured this
way.(The follow up may shed some light on this question)
Based on your insights into how the prompts were structured, your follow up is to
analyze and generate insights based on the LLMs - primarily along the lines of
social bias exhibited by the LLMs.
Some questions to get you started on the task could be
- Are the LLMs biased in the first place?
- To what extent are the LLMs biased?
- Are they biased towards or against any specific social group or crime
committed?
- Can we compare bias between the LLMs?
- Can we identify which LLM is the most and least biased? If we can, what
are they?
Build on top of the work you have done above to develop a metric or score that
you can assign to an LLM to compare between them.
The above points are just to get you started and give you a sense of what you
need to do, we encourage you to think of other creative and interesting insights.