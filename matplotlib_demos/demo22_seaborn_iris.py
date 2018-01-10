'''
set the python PATH environment variable
open cmd
run this cmd:   pip install seaborn

it will install both seaborn and pandas
'''
# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load iris data
iris = sns.load_dataset("iris")

# Construct iris plot
sns.swarmplot(x="species", y="petal_length", data=iris)

# Show plot
plt.show()
