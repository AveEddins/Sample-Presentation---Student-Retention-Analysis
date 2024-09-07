import pandas as pd
import scipy.stats as stats

studentDataFrame = pd.read_excel('Example Dataset.xlsx')

resultsDict = {}
column1 = 'Retention'
for column2 in studentDataFrame.columns:
        
    # Create contingency table
    contingency_table = pd.crosstab(studentDataFrame[column1], studentDataFrame[column2])
    
    # Ignore contingency tables with any element with 5 or fewer counts
    contingencyHas5CountsPerCell = True
    for column in contingency_table.columns:
        for row in contingency_table.index:
            if contingency_table[column][row] < 5:
                continue
                
    rowCount, columnCount = contingency_table.shape
    entryCount = rowCount*columnCount
    
    result = stats.chi2_contingency(contingency_table)
        
    CramerV = stats.contingency.association(contingency_table)
        
    # Per column pair: Cramer's V value, p value, degrees of freedom, and chi-2 value
    resultsDict[column1 + ' x ' + column2] = [CramerV, result.pvalue, result.dof, result.statistic]
    for element in resultsDict:
        print(element, resultsDict[element], '\n')