# NoDota
Two Sigma Financial Modeling Challenge
https://www.kaggle.com/c/two-sigma-financial-modeling


This dataset contains anonymized features pertaining to a time-varying value for a financial instrument. Each instrument has an id. Time is represented by the 'timestamp' feature and the variable to predict is 'y'. No further information will be provided on the meaning of the features, the transformations that were applied to them, the timescale, or the type of instruments that are included in the data. Moreover, in accordance with competition rules, participants must not use data other than the data linked from the competition website for the purpose of use in this competition to develop and test their models and submissions.

Data is saved and accessed as a .h5 file in the Kernels environment. We have used the .h5 file format instead of the standard .csv format to achieve faster read speeds. The training set file is available for download and offline modeling outside of Kernels. The test set is not available for download.

In addition to the data, you will need to familiarize yourself with the Kernels environment and the competition data API. The API is designed to prevent accessing data beyond the timestamp for which you are predicting and informs you which ids require predictions at which timestamps. The API also provides a "reward" for each timestamp, in the form of an average R value over the predicted values for the previous day. You may choose to use this reward to do reinforcement-style learning. Your code should expect and handle missing values.

We have setup the kernels environment such that the code structure you use for training on the test set (clicking "Run") will ideally work for submissions on the test set (clicking "Submit"). To achieve this, we have partitioned the training set such that the first half is provided as a training set at the start of a run, and the latter half is streamed through the API, as though it is a holdout set. In other words:

Run: first half of training set (split by time) provided initially, second half of training set used for API/predictions.
Submit: all of training set provided initially, test set used for API/predictions.
Getting Started Tips

Submissions must happen via a Script. Notebooks are available for exploratory analysis on the training set, but can not be used to submit.
Use the "Run" functionality in Kernels to check your method against the training set before you submit. Since this competition has an error limit per day, you'll want to eliminate basic syntax/typo errors before attempting to submit.
For more on how to make a submission, see the submission instructions tab. For an overview of the Kaggle Gym API, follow this tutorial notebook.
