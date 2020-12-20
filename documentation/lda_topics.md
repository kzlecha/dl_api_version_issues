# Topic Modeling

To conduct Topic Modelling, we used LDA on the questions and their respective answers.
These were filtered to include the code 

## General Topics

Deprecatated APIs:
    - most topics are about specifics of training
    - some reference to hardware
    - reference to versioning and batches
Explicit Reference
    - More questions explicitly about versioning
        - unsupported versions
        - deprecated models
        - Future and Deprecation
    - Lots of reference to training
        - layers
        - accuracy
        - cost
    - Discussion of Builds
    - Error
    - Hardware
    - Shell commands
    - Environments

## Conclusions
From the evidence drawn, we can see that the questions that explicitly reference
deprecation are more likely to be completely about deprecation. However, these 
questions have a number of different topics. Some reference installation, adopting
to a new version and looking towards the future, and even 

It is interesting that in both, there is a seperate topic about Theano. Since Theano
does not have very many questions about it, nor very many deprecations over it's
long lifetime.

Despite the library being deprecated, most topics were not about the deprecation.
This supports the results of the manual investigation, where it was noted that for
many questions the user did not understand what the error was and was asking for help.


