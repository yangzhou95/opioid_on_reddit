## A set of classifiers to classify short text (comments, posts, etc)

Supported Classifiers:
### KNN
### Logistic regression
### SVM

## SVM using LibShortText Library
LibShortText Library is already forked in this project. To begin, you must be using a Linux based machine. Change your directory to the libshort folder and run the command 'make'. After these steps are completed you are now ready to to use LibShortText. For more information about the LibShortText Library, please visit the official websites of [LibShortText](https://www.csie.ntu.edu.tw/~cjlin/libshorttext/).
**Link to Libshort Folder:** https://github.com/yangzhou95/opioid_on_reddit/code/text_classifier/tree/master/libshorttext-1.1


**Required OS:** Linux
**Terminal Command Required:** `$ make`

### Accuracy Prediction

In order to use LibShortText through the terminal be sure to format the data as described below ( for each row, the format is <LABEL><TAB><TEXT>, and there is no header). Once that is done, you are able to use the library from the terminal. **Text files must be classified into 2 or more categories**, as shown below.

**Text File Format (addict_nonaddict.txt,<LABEL><TAB><TEXT>, addict->1, nonaddict->0 ):** <LABEL><TAB><TEXT>
```
0    Not the guy you asked but benzodiazepines like xanax are a really bad mix with alcohol and a lot of other drugs and can potentiate the drug and often be fatal
1    45 days clean and now I am drunk and high
0    you do not really owe them any more explanation than medical issues
1    what to say when returning to work from drug treatment
1    watching tv sober
0    I would always have to rewatch GoT the next morning because I remembered about 10% of what I would seen the night before
0    hehe I was the absolute same with GoT. I would get so drunk and high I would have no idea who was banging who and just end up turning it off
```
  
**Text File Format (recov_nonrecov.txt,<LABEL><TAB><TEXT>, recovering->1, nonrecovering->0):** <LABEL><TAB><TEXT>
```
1    45 days clean and now I am drunk and high
0    list your top 5 favorite drugs, all you have tried and your wish list
0    I had a good time being on drugs but in 3 hours I am going to jail wish me good luck See you soon folks
1    10 days clean
1    finally trying to quit
0    how to get the most out of Kratom
```
  
**Train Text File:**
Train a properly formatted text file to obtain a model. This process will generate a train_file.model folder that will be used to help predict results

```
$ python text-train.py -f -P 5 train_data.txt
[output information]
```

*Note:* '-f', will overwrite existing model so you don't have to keep deleting the folder. '-P 5', will remove perform stopword removal with no stemming and bigram

**Predict Results:**
Predicts the results of the test file using the trained model that was generated from above. The output of this command is an accuracy precentage of how well the model processed the test file.
```
$ python text-predict.py train_data.txt train_data.txt.model predict_result

**Full Example:**
$ python text-train.py train_data.txt
$ python text-predict.py test_data.txt train_data.txt.model predict_result

### Precision, Recall and F-Measure(F-Score)
1. Create predict file from the steps above
2. Name file: **predict_results**
3. Place, **predict_results** in that same folder as **SVM-Analyzer.py**
4. Run `$ python SVM-Analyzer.py`

**Output Example:**
```
Precision: 0.933098591549
Recall: 0.920138888889
F-measure: 0.926573426573
```
 
### Sample SVM Output on Rescue Data
**Accuracy:** 87.4627%
**Precision:** 0.933098591549
**Recall:** 0.920138888889
**F-Measure(F-Score):** 0.926573426573

This submodule is modified based on our previsous project about tweet classification, for more information about tweet classification, plese visit the [harvey-classifier](https://github.com/litpuvn/harvey-classifier)