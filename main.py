from demo.MockData import Simulation
from demo.ProcessData import ProcessData
import pandas as pd

if __name__ == '__main__':
    p_data = ProcessData(pd.DataFrame(columns=['user_id', 'timestamp', 'heart_rate', 'respiration_rate', 'activity']))
    simulation = Simulation()
    simulation.simulate_mock_data(3, p_data)
    p_data.get_df()
