# ML Project: Supervised Learning - Drunk Smurfs

## TODO

1. Actually finalize the project :)
2. Check, double check and triple check for mistakes
3. Reformat the code
4. Adjust markdown sections of notebooks to be more clear
5. Whitening the black box (explaining why models do certain things)

## Content of this repository

In this repository you will find all of the `.ipynb` notebooks and datasets for a project I had for the course **Machine Learning**.

## Folder structure

### Guestlist

`/guestlist/` contains the lists of approved applicants

- There is a `README.md` in that folder, which you might want to read for clarification

### Files

1. `Prepare.ipynb` contains the code for Pre-processing the dataset
2. `Merging.ipynb` contains the code for merging all 3 exported datasets together
3. `Answer.ipynb` contains the code where the final list of guests is returned

### Datasets

`/data/` contains all datasets

- `/data/cleaned` contains the cleaned (pre-processed) `train_V2.csv`
- `/data/exported` contains the exported datasets from all 3 models + 1 where all 3 are merged

### Model Selection

`/model_selection/` contains the notebooks for the model comparisons

1. `/model_selection/outcome_profit.ipynb` contains the model selection for the first model
2. `/model_selection/outcome_damage_inc.ipynb` contains the model selection for the second model
3. `/model_selection/outcome_damage_amount.ipynb` contains the model selection for the third model

### Models

`/models/` contains the notebooks for the models

1. `/models/Project_Revenue/` directory contains my model for the first assignment
2. `/models/Project_Damage_Incident/` directory contains my model for the second assignment
3. `/models/Project_Damage_Amount/` directory contains my model for the third assignment

### Util

`/util/` contains utility modules

- `calculate_scores.py`, which is a module used to calculate the scores on `scores.csv`

## Assignment context

Among all international hotel guests, Smurfs are burdened with the upkeep of a singular reputation: they are (supposedly) the rowdiest bunch one can entertain, and are equally well-known for unbridled spending as for racking up extensive costs in damages to hotel infrastructure, staff, and occasionally also other guests – costs which typically cannot be recovered once the guest has sought out the safety of his (or her) homeland.
It is your job as a data scientist to screen applying Smurfs clients for an exclusive hotel in the Bahamas - yes, it's the kind of hotel you need to apply for!

&nbsp;

> Harman Singh

### Time spent on this project

| Day           | Time spent    | Start time | End time |
| ------------- | ------------- | ---------- | -------- |
| Thu, 7 March  | 12h38         | 10h00      | 22h38    |
| Sun, 10 March | 0h50          | 15h35      | 16h25    |
| Thu, 14 March | 2h32          | 13h30      | 16h02    |
| Thu, 14 March | 0h50          | 17h35      | 18h25    |
| Thu, 14 March | 1h25          | 18h50      | 20h15    |

### **TOTAL**: 18h15
