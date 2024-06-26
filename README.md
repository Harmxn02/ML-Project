# ML Project: Supervised Learning - Drunk Smurfs

## Assignment context

Among all international hotel guests, Smurfs are burdened with the upkeep of a singular reputation: they are (supposedly) the rowdiest bunch one can entertain, and are equally well-known for unbridled spending as for racking up extensive costs in damages to hotel infrastructure, staff, and occasionally also other guests – costs which typically cannot be recovered once the guest has sought out the safety of his (or her) homeland.
It is your job as a data scientist to screen applying Smurfs clients for an exclusive hotel in the Bahamas - yes, it's the kind of hotel you need to apply for!

## Content of this repository

In this repository you will find all of the `.ipynb` notebooks and datasets for a project I had for the course **Machine Learning**.

## Folder structure

### Guestlist

`/guestlist/` contains the lists of approved applicants

- There is a `README.md` in that folder, which you might want to read for clarification

### Files

1. `Prepare.ipynb` contains the code for Pre-processing the dataset
2. `Merging.ipynb` contains the code for merging all 3 exported datasets together
3. `Answer.ipynb` contains the code where the final list of guests is returned and exported

### Datasets

`/data/` contains all datasets

- `~/cleaned` contains the cleaned (pre-processed) `train_V2.csv`
- `~/exported` contains the exported datasets from all 3 models + 1 where all 3 are merged

### Model selection

`/model_selection/` contains the notebooks for the model comparisons

1. `~/outcome_profit.ipynb` contains the model selection for the first model
2. `~/outcome_damage_inc.ipynb` contains the model selection for the second model
3. `~/outcome_damage_amount.ipynb` contains the model selection for the third model

### Models

`/models/` contains the notebooks for the models

1. `~/Predict_Revenue/` directory contains my model for the first assignment
2. `~/Predict_Damage_Incident/` directory contains my model for the second assignment
3. `~/Predict_Damage_Amount/` directory contains my model for the third assignment

### Util

`/util/` contains utility modules

- `calculate_scores.py`, which is a module used to calculate the scores on `scores.csv`

&nbsp;

> Harman Singh

### Time spent on this project

| Day           | Time spent | Start time | End time |
| ------------- | ---------- | ---------- | -------- |
| Thu, 7 March  | 12h38      | 10h00      | 22h38    |
| Sun, 10 March | 0h50       | 15h35      | 16h25    |
| Thu, 14 March | 2h32       | 13h30      | 16h02    |
| Thu, 14 March | 0h50       | 17h35      | 18h25    |
| Thu, 14 March | 1h25       | 18h50      | 20h15    |
| Sun, 7 April  | 3h00       | 17h45      | 20h45    |
| Sun, 7 April  | 0h15       | 21h25      | 21h40    |
| Sun, 14 April | 0h50       | 17h30      | 18h20    |

### **TOTAL**: 22h20
