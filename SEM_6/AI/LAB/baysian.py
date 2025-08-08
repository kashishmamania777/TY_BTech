# Install pgmpy if not already installed
# !pip install pgmpy

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = DiscreteBayesianNetwork([
    ('Season', 'Weather'),
    ('Season', 'Major Event'),
    ('Weather', 'Crowds'),
    ('Major Event', 'Crowds'),
    ('Crowds', 'Hotel Price'),
    ('Major Event', 'Hotel Price'),
    ('Weather', 'Visit Satisfaction'),
    ('Crowds', 'Visit Satisfaction'),
    ('Hotel Price', 'Visit Satisfaction')
])

# Define the CPDs (Conditional Probability Distributions)
cpd_season = TabularCPD(
    variable='Season', variable_card=2,
    values=[[0.5], [0.5]],
    state_names={'Season': ['Summer', 'Winter']}
)

cpd_weather = TabularCPD(
    variable='Weather', variable_card=2,
    values=[[0.8, 0.3],   # Sunny: Summer, Winter
            [0.2, 0.7]],  # Rainy: Summer, Winter
    evidence=['Season'], evidence_card=[2],
    state_names={'Weather': ['Sunny', 'Rainy'], 'Season': ['Summer', 'Winter']}
)

cpd_major_event = TabularCPD(
    variable='Major Event', variable_card=2,
    values=[[0.4, 0.1],   # Yes: Summer, Winter
            [0.6, 0.9]],  # No: Summer, Winter
    evidence=['Season'], evidence_card=[2],
    state_names={'Major Event': ['Yes', 'No'], 'Season': ['Summer', 'Winter']}
)

cpd_crowds = TabularCPD(
    variable='Crowds', variable_card=2,
    values=[
        [0.95, 0.6, 0.7, 0.2],  # High: [Sunny,Yes], [Sunny,No], [Rainy,Yes], [Rainy,No]
        [0.05, 0.4, 0.3, 0.8]   # Low:  [Sunny,Yes], [Sunny,No], [Rainy,Yes], [Rainy,No]
    ],
    evidence=['Weather', 'Major Event'], evidence_card=[2, 2],
    state_names={
        'Crowds': ['High', 'Low'],
        'Weather': ['Sunny', 'Rainy'],
        'Major Event': ['Yes', 'No']
    }
)

cpd_hotel_price = TabularCPD(
    variable='Hotel Price', variable_card=2,
    values=[
        [0.9, 0.5, 0.6, 0.1],  # Expensive: [High,Yes], [High,No], [Low,Yes], [Low,No]
        [0.1, 0.5, 0.4, 0.9]   # Affordable: [High,Yes], [High,No], [Low,Yes], [Low,No]
    ],
    evidence=['Crowds', 'Major Event'], evidence_card=[2, 2],
    state_names={
        'Hotel Price': ['Expensive', 'Affordable'],
        'Crowds': ['High', 'Low'],
        'Major Event': ['Yes', 'No']
    }
)

cpd_visit_satisfaction = TabularCPD(
    variable='Visit Satisfaction', variable_card=2,
    values=[
        # High Satisfaction
        [0.7, 0.6, 0.8, 0.95, 0.5, 0.4, 0.6, 0.3],
        # Low Satisfaction
        [0.3, 0.4, 0.2, 0.05, 0.5, 0.6, 0.4, 0.7]
    ],
    evidence=['Weather', 'Crowds', 'Hotel Price'], evidence_card=[2, 2, 2],
    state_names={
        'Visit Satisfaction': ['High', 'Low'],
        'Weather': ['Sunny', 'Rainy'],
        'Crowds': ['High', 'Low'],
        'Hotel Price': ['Expensive', 'Affordable']
    }
)

# Add CPDs to the model
model.add_cpds(
    cpd_season, cpd_weather, cpd_major_event,
    cpd_crowds, cpd_hotel_price, cpd_visit_satisfaction
)

# Validate the model
assert model.check_model()

# Create an inference object
inference = VariableElimination(model)

# Example queries
# Query 1: P(Visit Satisfaction=High | Season=Summer, Major Event=No)
query1 = inference.query(
    variables=['Visit Satisfaction'],
    evidence={'Season': 'Summer', 'Major Event': 'No'}
)

# Query 2: P(Hotel Price=Expensive | Season=Winter, Major Event=Yes)
query2 = inference.query(
    variables=['Hotel Price'],
    evidence={'Season': 'Winter', 'Major Event': 'Yes'}
)

# Query 3: P(Crowds=High | Weather=Sunny, Major Event=Yes)
query3 = inference.query(
    variables=['Crowds'],
    evidence={'Weather': 'Sunny', 'Major Event': 'Yes'}
)

# Query 4: P(Weather=Sunny | Season=Winter)
query4 = inference.query(
    variables=['Weather'],
    evidence={'Season': 'Winter'}
)

# Query 5: P(Visit Satisfaction=High | Hotel Price=Affordable, Crowds=Low)
query5 = inference.query(
    variables=['Visit Satisfaction'],
    evidence={'Hotel Price': 'Affordable', 'Crowds': 'Low'}
)

# Print results
print("Query 1:", query1)
print("Query 2:", query2)
print("Query 3:", query3)
print("Query 4:", query4)
print("Query 5:", query5)
