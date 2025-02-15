# CFXGB : Cascaded Forest and XGBoost Classifier

This is a supervised machine learning model created by Surya Dheeshjith and Thejas Gubbi Sadashiva. The model is based on paper [1]. CFXGB is an extension of the model proposed in [2]. 
Implementation of cascaded forest is available at https://github.com/kingfengji/gcForest. 

This repository also exists in this [link](https://github.com/suryadheeshjith/CFXGB) with integrated Travis CI and Code coverage.  


Implementation done in Python 3.7.3

For more details, contact Surya Dheeshjith : surya.dheeshjith@gmail.com (or) Thejas Gubbi Sadashiva : tgs001@fiu.edu
                 

## Details

We have included demo code for execution and a detailed explanation of how you can use your own dataset with custom model parameters.


![Pipeline](/images/Pipeline2.png)

The implementation of using Parent nodes in the decision trees as stated in the paper has also been implemented

![Parent nodes](/images/DecisionTree4.png)



### Requirements

* All required packages are in requirements.txt

```pip install -r requirements.txt```

*If facing issues downloading xgboost package, use this conda command*

*```conda install py-xgboost```*

* Datasets Used in [1] -   

  - TalkingData : https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection
  - Avazu : https://www.kaggle.com/c/avazu-ctr-prediction/data
  - Kad : https://www.kaggle.com/tbyrnes/advertising/data


### Running demo code

```python3 Main.py -d Kad -p DefaultParameters.json```

### List of Command-line Parameters

* -h --help : List the parameters and their use. 

* -d --dataset : A dataset must be considered for learning. This parameter takes the dataset csv file name. This parameter **must** be passed.    

* -p --parameters : Model Parameters are passed using a json file. This parameter must be used to specify the name of json file. This parameter **must** be passed.  

* -i --ignore : Ignore the first column. (For some cases).  
                Default = False

* -r --randomsamp : Balance the dataset using random under sampling. (Use for imbalanced datasets).   
                    Default = False

* -v --parentvaluecols [ BETA ]: Addition of columns based on class distributions of parents of leaf nodes in the decision tree.    
                                Default = False

* -c --cores [ BETA ]: Number of cores to be used during addition of columns (When -v is True).    
                         Default = -1 (All cores)

### How to run code for different datasets and model parameters

```python3 Main.py -d <Dataset_Name> -p <Parameter_list>.json```


### References
[1] [CFXGB: An Optimized and Effective Learning Approach for Click Fraud Detection.](https://www.sciencedirect.com/science/article/pii/S2666827020300165)

[2] [Z.-H. Zhou and J. Feng. Deep Forest: Towards an Alternative to Deep Neural Networks.](https://arxiv.org/abs/1702.08835v2 ) 







###### Last updated : 22 June 2020


