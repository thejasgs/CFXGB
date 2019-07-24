# CFXGB : Cascaded Forest and XGBoost Classifier

This is a supervised machine learning model created by Surya Dheeshjith and Thejas Gubbi Sadashiva. The model is based on paper [1]. CFXGB is an extension of the model proposed in [2]. 
Implementation of code for cascaded forest has been used from https://github.com/kingfengji/gcForest.

Model implementation done in python2.7

For more details, contact Surya Dheeshjith : surya.dheeshjith@gmail.com (or) Thejas Gubbi Sadashiva : tgs001@fiu.edu
                 
### References
[1] CFXGB: An Optimized and Effective Learning Approach for Click Fraud Detection
[2]  Z.-H. Zhou and J. Feng. Deep Forest: Towards an Alternative to Deep Neural Networks.
In IJCAI-2017. (https://arxiv.org/abs/1702.08835v2 )

## Details

We have included demo code for execution and a detailed explanation of how you can use your own dataset with custom model parameters.

### Running demo code

```python2 Main.py -d Kad -p DefaultParameters.json```

### How to run code for different dataset and model parameters

```python2 Main.py -d <Dataset_Name> -p <Parameter_list>.json```






