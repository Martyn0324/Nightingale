# Nightingale
Tell me the patient's symptoms, I'll help you treat him


## AI for Primary Health Care

Use her to catalog possible sicknesses a patient might have, helping you to investigate the correct diagnosis as well as determine the right treatment

### Ideas
Possible Multiclassifier where each label(y) will correspond to a disease, while each feature(X) will correspond to symptoms. The AI will determine the probability of
each disease being the correct diagnosis and will show up in a list every disease that has a probability higher than 1% of being the correct one, as well as the
probability it deduced.

* Problem: Not every patient develops the same symptoms for the same sickness. How to make the AI take this factor into account during training and while in action?
* Considering this, how can one mount the data in order for the AI to be properly trained? A single dataframe where each disease is assigned to many symptoms column?
Or perhaps organizing it in a better way(which I have no idea right now). How can one add more data in order to test it?
* OBS: Perhaps 1% will still show up too much information. It might be interesting to let the user itself to decide this number.
* Problem²: Considering we want to deal with human lives, what is the minimum accuracy that the model must have? How big should the dataset be?
* Problem³: If we want to complement our dataset, how difficult would it be to obtain the symptoms and diagnosis of each patient admitted to a hospital?

** It seems it's just a matter of time before GPT starts being used for this task. How would be able to make our model be better than GPT? Considering the structure behind OpenAI, it's unlikely that we would be able to make a model even better than GPT-4 or even an eventual 5, 6... Our advantage, however, would be in optimization and cheapness. OpenAI is having trouble with its openess. No one can be so open while also using models with billions of parameters, trained on dozens of last generation GPUs. **

## Further Development
Making Nightingale not only say the diagnosis, but also the active component that can treat such sickness
