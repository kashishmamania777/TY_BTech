import networkx as nx
import random

class MobileAgent:
    def __init__(self):
        self.data = {
            'battery': 100,
            'network': {'bandwidth': random.randint(5, 50)},  # Mbps
            'cloudlet': {'status': 'available', 'queue': 0}
        }
        
    def create_multistage_graph(self, tasks):
        """Create 3-stage graph with random dependencies"""
        G = nx.DiGraph()
        stages = 3
        
        for stage in range(stages):
            nodes = [f"Task_{stage}_{i}" for i in range(random.randint(2,5))]
            G.add_nodes_from(nodes, stage=stage)
            
            if stage > 0:
                prev_nodes = [n for n,d in G.nodes(data=True) if d['stage']==stage-1]
                for node in nodes:
                    G.add_edge(random.choice(prev_nodes), node)
        
        return G

    def categorize_tasks(self, G):
        """Classify tasks into three arrays"""
        categories = {
            'unoffloadable': [],
            'must_offload': [],
            'offloadable': []
        }
        
        for node in G.nodes():
            rand = random.random()
            if rand < 0.2:
                categories['unoffloadable'].append(node)
            elif rand < 0.5:
                categories['must_offload'].append(node)
            else:
                categories['offloadable'].append(node)
                
        return categories

    def offload_decision(self, categories):
        """Simple offloading logic based on cloudlet status"""
        decisions = {}
        
        # Process unoffloadable locally
        for task in categories['unoffloadable']:
            decisions[task] = 'local'
            
        # Process must-offload in cloudlet
        for task in categories['must_offload']:
            if self.data['cloudlet']['status'] == 'available':
                decisions[task] = 'cloudlet'
                self.data['cloudlet']['queue'] += 1
            else:
                decisions[task] = 'postponed'
        
        # Offloadable tasks decision
        for task in categories['offloadable']:
            if self.data['network']['bandwidth'] > 20:
                decisions[task] = 'cloudlet' 
            else:
                decisions[task] = 'local'
                
        return decisions

# Simulation
if __name__ == "__main__":
    agent = MobileAgent()
    tasks = [f"Task_{i}" for i in range(10)]
    
    # Create multistage graph
    workflow_graph = agent.create_multistage_graph(tasks)
    
    # Categorize tasks
    task_categories = agent.categorize_tasks(workflow_graph)
    
    # Make offloading decisions
    decisions = agent.offload_decision(task_categories)
    
    # Visualize results
    print("Task Categorization:")
    print(task_categories)
    print("\nOffloading Decisions:")
    print(decisions)
    
    # Draw graph
    pos = nx.multipartite_layout(workflow_graph, subset_key="stage")
    nx.draw(workflow_graph, pos, with_labels=True, node_color='lightblue')
