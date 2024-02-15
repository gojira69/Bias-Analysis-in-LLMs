* Separate stereotypical tuples -----> `Done`

* Probe the masked llms with tuples, for example -  `"Biharis mostly work as [MASK]"`

* Do this for `region`, `religion` and `caste`.

* Try probing for gender analysis using names. For example - `"Gender of @ is [MASK]"`, where `@` is the name

* Generate similairty scores for religion ----> Done

* Generate simialrity scores for region ---> will take lot of time. do it in google collab and do rest of the tasks. and do automate stuff. 

* Probe the mlms using gender id terms. but you will not get the bias in context of india, but in a global pov. 

* refine and work on the similairty scores for religion and region.

* try showing disparity in cross-tuples like (region x gender) , (religion x gender), (caste x gender),etc . for that first cross product  the tuples. then repeat the shit that we did.  ----> Done with generating tuples from lms. ----> Now analyze the output  

* also generate the full sequences for all social axis, including the cross product tuples ---> Done

* Generate heat maps for religion and region ----> done with religion. started generating similarity scores for region.  ----> done with region

* assign stereotypical nature of an lm by calcualting how many common tuples are there with the human-annotaetd set of stereotypes. This would definitely change from model to model. 

# End Goal

Can you leverage this dataset to assess bias encoded into NLP models? Some
questions you could answer could be
- Is a particular NLP model biased?
- Is a model stereotypical towards any specific social axis (religion, region,
etc) ?
- Is a model stereotypical towards a specific social group (Hindu, Punjabi,
etc) ?
- How would you quantify bias through this method?

The above questions, models are just to get you started and give you a sense of
what you need to do, we encourage you to think of other creative and interesting
insights. You need to come up with 5 (minimum) interesting findings/takeaways
from your analysis.
